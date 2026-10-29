// The site's Worker. Static assets serve every page (wrangler.jsonc); this script runs only
// for /get, the App Store button counter: count the tap, then send the visitor to the App Store.
//
// Each tap is one Workers Analytics Engine data point: the placement, its page and position.
// No IP address, User-Agent, cookie or any other identifier is stored.

import { looksAutomated, tapRedirect } from "./tap.js";

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.pathname !== "/get") return env.ASSETS.fetch(request);

    const tap = tapRedirect(url.searchParams.get("from"), env.APP_STORE_PROVIDER_TOKEN);
    if (request.method === "GET" && env.TAPS && !looksAutomated(request.headers.get("User-Agent"))) {
      try {
        env.TAPS.writeDataPoint({ indexes: [tap.placement], blobs: [tap.placement, tap.page, tap.position], doubles: [1] });
      } catch {
        // Counting must never stop the visitor reaching the App Store.
      }
    }
    return new Response(null, { status: 302, headers: { "Location": tap.location, "Cache-Control": "no-store" } });
  },
};
