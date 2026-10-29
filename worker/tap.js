// App Store button taps (decision D1): which button was tapped, and where the tap goes.
// Pure functions, no Cloudflare APIs, so they can be tested anywhere (worker/tap.test.js).

export const APP_ID = "1611824311";
export const PLAIN_APP_STORE_URL = `https://apps.apple.com/app/id${APP_ID}`;

// Every App Store button on the site, as <page>-<position>. A new button needs a line here,
// or its taps count as "other" (tools/check-measurement.py fails until it's added).
// Positions: nav (header button), menu (phone menu), hero (first badge), band (home's band
// call to action), plan-free / plan-premium (pricing table), final (closing badge).
export const BUTTONS = {
  "home": ["nav", "menu", "hero", "band", "final"],
  "pricing": ["nav", "menu", "plan-free", "plan-premium", "final"],
  "about": ["nav", "menu", "final"],
  "support": ["nav", "menu", "final"],
  "contact": ["nav", "menu"],
  "privacy": ["nav", "menu"],
  "notfound": ["nav", "menu", "final"],
  "planning-center": ["nav", "menu", "hero", "final"],
  "features-set-lists": ["nav", "menu", "hero", "final"],
  "features-page-turner": ["nav", "menu", "hero", "final"],
  "features-annotation": ["nav", "menu", "hero", "final"],
  "features-sharing": ["nav", "menu", "hero", "final"],
  "features-free-sheet-music": ["nav", "menu", "hero", "final"],
  "features-toolkit": ["nav", "menu", "hero", "final"],
  "for-bands": ["nav", "menu", "hero", "final"],
  "for-worship-teams": ["nav", "menu", "hero", "final"],
  "for-orchestras-choirs": ["nav", "menu", "hero", "final"],
  "for-students": ["nav", "menu", "hero", "final"],
};

// placement → [page, position]
export const PLACEMENTS = new Map(
  Object.entries(BUTTONS).flatMap(([page, positions]) =>
    positions.map((position) => [`${page}-${position}`, [page, position]])),
);

// The App Store Connect campaign name for a placement: "web-" + the placement without a leading
// "features-" / "for-" (App Store Connect allows 30 characters: web-free-sheet-music-final, not
// web-features-free-sheet-music-final). Still unique; tap.test.js checks both.
export const CAMPAIGN_MAX = 30;
export function campaignName(placement) {
  return `web-${placement.replace(/^(features|for)-/, "")}`;
}

// The tap's placement (unknown or missing `from` → "other", never the raw input) and its
// destination. With the App Store Connect provider token the link carries a campaign
// (ct=campaignName(placement)), so App Analytics → Campaigns can count downloads from the site
// (shown by Apple only at 5 or more). Without a valid token: the plain App Store link.
export function tapRedirect(from, providerToken) {
  const known = PLACEMENTS.get(from);
  const placement = known ? from : "other";
  const [page, position] = known ?? ["other", "other"];
  const campaign = campaignName(placement);
  const token = String(providerToken ?? "").trim();
  const location = /^\d{1,20}$/.test(token)
    ? `https://apps.apple.com/app/apple-store/id${APP_ID}?pt=${token}&ct=${campaign}&mt=8`
    : PLAIN_APP_STORE_URL;
  return { placement, page, position, campaign, location };
}

// Crawlers and link-preview fetchers follow links too; their visits are redirected but not
// counted. The User-Agent is only tested here, never stored.
const AUTOMATED = /bot|crawl|spider|slurp|preview|fetch|scan|monitor|curl|wget|python|java\/|go-http|headless|lighthouse|facebookexternalhit|embedly|whatsapp|telegram|discord|slack/i;

export function looksAutomated(userAgent) {
  return !userAgent || AUTOMATED.test(userAgent);
}
