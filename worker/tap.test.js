// Tests for worker/tap.js. No Node needed — macOS's JavaScriptCore runs them:
//   /System/Library/Frameworks/JavaScriptCore.framework/Versions/Current/Helpers/jsc -m worker/tap.test.js
// (tools/check-measurement.py runs this too.)

import { PLACEMENTS, PLAIN_APP_STORE_URL, looksAutomated, tapRedirect } from "./tap.js";

let failures = 0;
function check(name, actual, expected) {
  const ok = JSON.stringify(actual) === JSON.stringify(expected);
  if (!ok) {
    failures += 1;
    print(`FAIL ${name}: ${JSON.stringify(actual)} != ${JSON.stringify(expected)}`);
  }
}

check("known placement with token", tapRedirect("home-hero", "123456"), {
  placement: "home-hero", page: "home", position: "hero",
  location: "https://apps.apple.com/app/apple-store/id1611824311?pt=123456&ct=web-home-hero&mt=8",
});
check("multi-word position", tapRedirect("pricing-plan-premium", "123456").position, "plan-premium");
check("no token → plain link", tapRedirect("home-hero", "").location, PLAIN_APP_STORE_URL);
check("missing token → plain link", tapRedirect("home-hero", undefined).location, PLAIN_APP_STORE_URL);
check("malformed token → plain link", tapRedirect("home-hero", "12&ct=x").location, PLAIN_APP_STORE_URL);
check("unknown placement → other", tapRedirect("<script>", "123456").placement, "other");
check("unknown keeps no input", tapRedirect("evil-value", "123456").location.includes("evil"), false);
check("missing from → other", tapRedirect(null, "1").page, "other");
check("campaign tokens stay short", Math.max(...[...PLACEMENTS.keys()].map((p) => `web-${p}`.length)) <= 40, true);
check("67 buttons", PLACEMENTS.size, 67);
check("Safari counts", looksAutomated("Mozilla/5.0 (iPhone; CPU iPhone OS 18_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.6 Mobile/15E148 Safari/604.1"), false);
check("Googlebot doesn't", looksAutomated("Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"), true);
check("empty UA doesn't", looksAutomated(""), true);

print(failures === 0 ? `ok: worker/tap.js (${PLACEMENTS.size} placements)` : `${failures} failure(s)`);
if (failures) throw new Error("tap.test.js failed");
