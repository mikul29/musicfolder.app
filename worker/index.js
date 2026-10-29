// The site's Worker. Static assets serve every page (wrangler.jsonc); this script runs only for
// /get (App Store buttons) and /hit (a visit starting), the site's own cookieless counters.
//
// /get: one Workers Analytics Engine point per tap (TAPS): the button (placement, page, position)
// and the visit's source (channel, utm_source/medium/campaign, referring host, how the source was
// known), then a 302 to the App Store.
// /hit: one point per landing (LANDINGS): the page and the same source fields. 204, nothing else.
// No IP address, User-Agent, cookie or any other identifier is stored. Crawlers (User-Agent test)
// and the owner's own devices (o=1: marked mf-owner in their own storage) aren't counted.

import { cleanPath, sourceFrom } from "./source.js";
import { looksAutomated, tapRedirect } from "./tap.js";

function counted(request, url) {
  return !looksAutomated(request.headers.get("User-Agent")) && url.searchParams.get("o") !== "1";
}

function write(dataset, point) {
  try {
    dataset?.writeDataPoint(point);
  } catch {
    // Counting must never stop the visitor.
  }
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    if (url.pathname === "/hit") {
      const path = cleanPath(url.searchParams.get("p"));
      if (path && counted(request, url)) {
        const s = sourceFrom(url.searchParams);
        write(env.LANDINGS, { indexes: [s.channel], doubles: [1],
                              blobs: [path, s.channel, s.utmSource, s.utmMedium, s.utmCampaign, s.ref] });
      }
      return new Response(null, { status: 204, headers: { "Cache-Control": "no-store" } });
    }

    if (url.pathname !== "/get") return env.ASSETS.fetch(request);

    const source = sourceFrom(url.searchParams);
    const tap = tapRedirect(url.searchParams.get("from"), env.APP_STORE_PROVIDER_TOKEN, source);
    if (request.method === "GET" && counted(request, url)) {
      write(env.TAPS, { indexes: [tap.placement], doubles: [1],
                        blobs: [tap.placement, tap.page, tap.position, source.channel, source.utmSource,
                                source.utmMedium, source.utmCampaign, source.ref, source.hop] });
    }
    return new Response(null, { status: 302, headers: { "Location": tap.location, "Cache-Control": "no-store" } });
  },
};
