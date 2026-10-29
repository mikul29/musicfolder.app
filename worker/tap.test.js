// Tests for worker/tap.js. No Node needed — macOS's JavaScriptCore runs them:
//   /System/Library/Frameworks/JavaScriptCore.framework/Versions/Current/Helpers/jsc -m worker/tap.test.js
// (tools/check-measurement.py runs this too.)

import { CAMPAIGN_MAX, PLACEMENTS, PLAIN_APP_STORE_URL, looksAutomated, tapRedirect } from "./tap.js";
import { CHANNELS, appleCampaign, channelOf, cleanHost, cleanPath, cleanTag, sourceFrom } from "./source.js";

// JavaScriptCore has no URLSearchParams: a stand-in with .get()
const params = (obj) => ({ get: (k) => (k in obj ? obj[k] : null) });

let failures = 0;
function check(name, actual, expected) {
  const ok = JSON.stringify(actual) === JSON.stringify(expected);
  if (!ok) {
    failures += 1;
    print(`FAIL ${name}: ${JSON.stringify(actual)} != ${JSON.stringify(expected)}`);
  }
}

const reddit = sourceFrom(params({ r: "www.reddit.com", h: "landing" }));
check("known placement with token: Apple campaign by source", tapRedirect("home-hero", "123456", reddit), {
  placement: "home-hero", page: "home", position: "hero", campaign: "web-communities",
  location: "https://apps.apple.com/app/apple-store/id1611824311?pt=123456&ct=web-communities&mt=8",
});
check("a tagged visit uses its campaign", tapRedirect("pricing-plan-free", "1",
  sourceFrom(params({ uc: "Church Music Nov", us: "reddit", h: "next" }))).campaign, "c-church-music-nov");
check("no source (old link, crawler) → unknown", tapRedirect("home-hero", "1").campaign, "web-unknown");
check("long campaigns are cut to Apple's 30", appleCampaign({ utmCampaign: "a".repeat(40) }).length, 30);

// source.js
check("channels", ["www.reddit.com", "old.reddit.com", "notreddit.com", "www.google.co.uk", "gemini.google.com",
  "microsoft.com", "linux.com", "t.co", "forum.example.org", ""].map(channelOf),
  ["communities", "communities", "other", "search", "ai", "other", "other", "social", "communities", "direct"]);
check("landing: channel from the referring site", sourceFrom(params({ r: "www.bing.com", h: "landing" })).channel, "search");
check("next page: channel unknown, tags kept", [sourceFrom(params({ us: "reddit", h: "next" })).channel,
  sourceFrom(params({ us: "reddit", h: "next" })).utmSource], ["unknown", "reddit"]);
check("self-referral is not a source", sourceFrom(params({ r: "musicfolder.app", h: "landing" })),
  { ref: "", channel: "unknown", utmSource: "", utmMedium: "", utmCampaign: "", hop: "unknown" });
check("bad hop → unknown", sourceFrom(params({ h: "<x>" })).hop, "unknown");
check("tags cleaned", [cleanTag(" Reddit "), cleanTag("a b"), cleanTag("<script>"), cleanTag("x".repeat(41))],
  ["reddit", "a-b", "", ""]);
check("hosts cleaned", [cleanHost("WWW.Reddit.com"), cleanHost("https://x.com/a"), cleanHost("localhost")],
  ["www.reddit.com", "", ""]);
check("paths cleaned", [cleanPath("/for/bands"), cleanPath("/x?y=1"), cleanPath("http://e.com/"), cleanPath("")],
  ["/for/bands", "", "", ""]);
check("every channel's Apple name fits 30", Math.max(...CHANNELS.map(([, slug]) => `web-${slug}`.length)) <= CAMPAIGN_MAX, true);
check("multi-word position", tapRedirect("pricing-plan-premium", "123456").position, "plan-premium");
check("no token → plain link", tapRedirect("home-hero", "").location, PLAIN_APP_STORE_URL);
check("missing token → plain link", tapRedirect("home-hero", undefined).location, PLAIN_APP_STORE_URL);
check("malformed token → plain link", tapRedirect("home-hero", "12&ct=x").location, PLAIN_APP_STORE_URL);
check("unknown placement → other", tapRedirect("<script>", "123456").placement, "other");
check("unknown keeps no input", tapRedirect("evil-value", "123456").location.includes("evil"), false);
check("a crafted campaign can't inject", tapRedirect("home-hero", "1", sourceFrom(params({ uc: "x&ct=evil" }))).location.includes("evil"), false);
check("missing from → other", tapRedirect(null, "1").page, "other");
check("67 buttons", PLACEMENTS.size, 67);
check("Safari counts", looksAutomated("Mozilla/5.0 (iPhone; CPU iPhone OS 18_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.6 Mobile/15E148 Safari/604.1"), false);
check("Googlebot doesn't", looksAutomated("Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"), true);
check("empty UA doesn't", looksAutomated(""), true);

print(failures === 0 ? `ok: worker/tap.js (${PLACEMENTS.size} placements)` : `${failures} failure(s)`);
if (failures) throw new Error("tap.test.js failed");
