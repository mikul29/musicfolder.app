// Where a visit came from (owner-approved design, step 2, 2026-10-29): campaign tags (utm_*) and the
// referring site's host, cleaned and grouped into channels. Pure functions, tested in tap.test.js.
// Nothing here identifies a person: a path, a host name and campaign words.

// The channel rules: a copy of the dashboard's config/channels.yaml (tools/check-measurement.py
// fails if the two drift apart). Pattern kinds: "reddit.com" = that domain or a subdomain;
// "google." = that name with any ending; "forum" = a word in any part of the host.
export const CHANNELS = [
  ["AI assistants", "ai", ["chatgpt.com", "chat.openai.com", "perplexity.ai", "gemini.google.com", "copilot.microsoft.com", "claude.ai", "you.com"]],
  ["Search", "search", ["google.", "bing.com", "duckduckgo.com", "search.yahoo.", "ecosia.org", "search.brave.com", "yandex.", "baidu.com", "startpage.com", "qwant.com"]],
  ["Communities", "communities", ["reddit.com", "news.ycombinator.com", "forum", "discourse", "lemmy"]],
  ["Social", "social", ["facebook.com", "instagram.com", "x.com", "t.co", "twitter.com", "threads.net", "threads.com", "youtube.com", "tiktok.com", "linkedin.com", "lnkd.in", "pinterest.", "mastodon", "bsky.app"]],
  ["Listings", "listings", ["alternativeto.net", "producthunt.com"]],
  ["Old site", "old-site", ["mikul29.github.io"]],
];
export const SITE_HOST = "musicfolder.app";

export function matches(host, pattern) {
  host = host.toLowerCase().replace(/^\.+|\.+$/g, "");
  pattern = pattern.toLowerCase();
  if (pattern.endsWith(".")) return ("." + host).includes("." + pattern);
  if (pattern.includes(".")) return host === pattern || host.endsWith("." + pattern);
  return host.split(".").some((label) => label.includes(pattern));
}

// "direct" = no referring site; "other" = a site not in the rules; ("unknown" comes from sourceFrom).
export function channelOf(host) {
  if (!host) return "direct";
  for (const [, slug, patterns] of CHANNELS) if (patterns.some((p) => matches(host, p))) return slug;
  return "other";
}

// utm_* values: lower-case letters, digits, "." "_" "-", 1–40 characters; anything else is dropped.
export function cleanTag(value) {
  const v = String(value ?? "").trim().toLowerCase().replace(/[\s+]+/g, "-");
  return /^[a-z0-9._-]{1,40}$/.test(v) ? v : "";
}

// A host name only (never a full address): letters, digits, "." and "-", up to 100 characters.
export function cleanHost(value) {
  const v = String(value ?? "").trim().toLowerCase();
  return /^[a-z0-9.-]{1,100}$/.test(v) && v.includes(".") ? v : "";
}

// A site path: starts with "/", up to 100 safe characters, no query or fragment.
export function cleanPath(value) {
  const v = String(value ?? "");
  return /^\/[A-Za-z0-9/._-]{0,99}$/.test(v) ? v : "";
}

// How the source of a tap was known: on the landing page, one page later, or not at all.
const HOPS = new Set(["landing", "next", "unknown"]);
export function cleanHop(value) {
  return HOPS.has(value) ? value : "unknown";
}

// The source fields from a query string (the page's own for /hit, the button's for /get).
// The channel is known only on a visit's first page ("landing"): one page later the browser no
// longer says which site the visit came from, so it's "unknown" there (campaign tags still known).
export function sourceFrom(params) {
  const raw = cleanHost(params.get("r"));
  const ref = raw === SITE_HOST ? "" : raw;
  const hop = raw === SITE_HOST ? "unknown" : cleanHop(params.get("h"));
  return {
    ref,
    channel: hop === "landing" ? channelOf(ref) : "unknown",
    utmSource: cleanTag(params.get("us")),
    utmMedium: cleanTag(params.get("um")),
    utmCampaign: cleanTag(params.get("uc")),
    hop,
  };
}

// The App Store Connect campaign (ct, at most 30 characters): the visit's own campaign when the
// link was tagged ("c-" + utm_campaign), else its channel ("web-search", "web-direct"…), else
// "web-unknown" when the tap came two or more pages into a visit. Few buckets, so Apple's
// 5-download minimum is reachable; per-button detail stays in the tap counter.
export function appleCampaign(source) {
  if (source.utmCampaign) return ("c-" + source.utmCampaign).slice(0, 30);
  if (source.hop === "unknown") return "web-unknown";
  return "web-" + source.channel;
}
