# Music Folder marketing site

Static site, no build step: one HTML file per page (`index.html`, `pricing.html`, `features/*.html`, `for/*.html`, …), shared styles in `assets/site.css` (+ `assets/pages.css` for the landing/feature pages), shared behaviour in `assets/site.js`; the home page's hero script is inline at the bottom of `index.html`. Visual rules and copy brief live in the app repo (`DESIGN.md`, `WEBSITE_BRIEF.md`).

Deploys: Cloudflare Worker "musicfolder-app" serves the repo as static assets and redeploys on every push to `main` (about 1–3 minutes). `.assetsignore` keeps repo files like this README off the site. Work on a branch and merge to `main` when it's ready to go live.

Preview locally:

```sh
python3 -m http.server 8765
```

(Pretty URLs like `/about` only work on Cloudflare; locally open `about.html`.)

When `assets/site.css` changes, bump `site.css?v=N` on every page so returning visitors fetch it.

Fonts are served from `assets/fonts/` (Latin + Latin Extended subsets of the Google Fonts builds of Instrument Serif and Inter, OFL — licences beside them), declared at the top of `site.css`. Every page preloads the two Instrument Serif files in its `<head>`; Inter isn't preloaded, because Apple devices use the system font first and never fetch it. Don't go back to the Google Fonts stylesheet: it was the biggest delay before anything appeared on a phone (about 0.8 s in PageSpeed's mobile test).

## Home hero: the folder opens, everything flies into the iPad

`.hero` is 516vh tall with a sticky 100vh stage. `frame()` maps scroll progress through `pace()` (the cover opening and the practice card + closing line run faster than the flights) to the timeline `p` (0–1) used by the phases below; everything is scroll-linked except the review dots, which run on a timer.

| p | What happens |
|---|---|
| 0 – 0.13 | the tilted folder straightens and centres; hero copy fades |
| 0.13 – 0.31 | the cover swings open on an overstuffed pocket (6 paper folders, 4 scores, a printed set list) |
| 0.30 – 0.35 | the iPad on the right page wakes (screen content fades up from black) |
| 0.33 – 0.60 | the 11 items fly, top of the pile first: straight up out of the pocket, over the spine, down into their slot on the screen (one cubic Bézier each). Scores land in Recently opened, folders (already in their cover colours) become the Folders row's book covers, the set list turns into its card; each slot's mask fades as its item lands |
| 0.64 – 0.78 | the iPad slides out of the pocket and is handed to a stage layer (`.ipad-stage`) above the folder, travels front and centre; the cover closes and the folder settles behind as a tilted backdrop |
| 0.75 – 0.84 | today's practice fills in: the minutes count up to 42, the goal bar fills, "of 30 min" gives way to "Daily goal reached" |
| 0.82 – 0.88 | the week's bars rise (Sunday, then today) |
| 0.88 – 0.97 | "The last folder you'll ever need." fades in |

The folder is laid out at a fixed 450×600 (rig coordinates) and scaled as a whole. The iPad screen (a 340 × 444 body, 13-inch proportions) is a real 4.2 Home screen captured on the MF iPad Pro 13 27.2 simulator from a demo library seeded with the site's content (`tools/hero-seed.py` writes the seed for the app's DEBUG marketing seed: Summer Night Concert tomorrow, a 14-day streak with 42 minutes today, the six folders and their counts, and exactly the scores that fly in, opened last). `assets/hero-ipad-home.webp` is that capture at 1668 × 2224; positions are measured in the capture's own 2064 × 2752 pixels (`SHOT_W`/`SHOT_H`: `scoreSlot`, `folderSlot`, `setlistSlot`, `PRACTICE`) and scaled by `K`. The practice card is rebuilt crisp over the screenshot (its number, goal bar, goal label and week bars animate; the rest of the card is the screenshot's own), checked against the capture to within a pixel by rendering it at 1:1 in headless Chrome. The printed set list (`.mf-setlist`) is laid out as the card scaled to its 280 px width (× 280/952), so it lands line for line. If the screenshot is ever replaced, re-seed and recapture, re-measure those coordinates, and regenerate the phone copies `hero-ipad-home-800.webp` / `-1100.webp` (same picture resized, WebP quality 90; the `srcset` on both hero images picks them).

With `prefers-reduced-motion`, the hero is static.

## Device images

`assets/home-ipad.webp`, `assets/home-iphone.webp` and `assets/home-mac.webp` (home dark band; iPad and iPhone also on Students) are rendered by `tools/home-band.py` from the same seeded 4.2 captures as the hero (iPad portrait, iPhone top of Home, and iPad landscape with the sidebar for the Mac, which runs this same iPad UI). The iMac is `tools/imac-base.png` (the iMac, its wallpaper and an empty menu bar) with the 4.2 menu bar set in the system font and an app window: the real Mac title bar (`tools/mac-titlebar@2x.png`, cut from the owner's 4.2 Mac screenshot) over the landscape capture below its status bar, with iPadOS's window-resize handle patched out. The general recipe: an HTML page with the bezel and the screenshot, rendered with headless Chrome at 2×:

```sh
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --hide-scrollbars \
  --default-background-color=00000000 --force-device-scale-factor=2 \
  --window-size=600,851 --screenshot=out.png file:///path/to/frame.html
```

## Measurement (decision D1: cookieless, no GA4)

- **Visits:** Cloudflare Web Analytics with **automatic setup** (dashboard → Web analytics → musicfolder.app): Cloudflare adds the beacon at the edge, so the pages carry no snippet. Don't add one (it would count every visit twice; `tools/check-measurement.py` fails on it). No cookies, no identifiers.
- **App Store taps:** every App Store button links to `/get?from=<page>-<position>` (positions: `nav`, `menu`, `hero`, `band`, `plan-free`, `plan-premium`, `final`). `worker/index.js` (runs before the static assets only for `/get` and `/hit`) writes one Workers Analytics Engine point per tap to `musicfolder_app_store_taps`: the button (placement, page, position) plus the visit's source (below); never an IP or User-Agent; crawlers and the owner's devices aren't counted. Then a 302 to the App Store with Apple campaign `ct` named after the SOURCE (`c-<utm_campaign>`, else `web-<channel>`, `web-unknown`; `worker/source.js`), when `APP_STORE_PROVIDER_TOKEN` is set in `wrangler.jsonc`; otherwise the plain App Store link.
- **Where visits come from** (cookieless, nothing stored on visitors' devices; the end of `assets/site.js`): on a visit's first page the script sends one landing count to `/hit` (dataset `musicfolder_landings`: page, channel, utm_source/medium/campaign, referring host) and adds the same source to every `/get` link. One page later the campaign tags are still known (the previous page's address); further in, the source is `unknown`. Channel rules in `worker/source.js` are a copy of the dashboard's `config/channels.yaml` (the check script compares them).
- **Tag the links you post**, e.g. `https://musicfolder.app/?utm_source=reddit&utm_medium=social&utm_campaign=churchmusic-nov` (lower case, letters, digits, `.` `_` `-`, up to 40 characters; anything else is dropped). App browsers (Reddit, Instagram…) often hide the referring site, so untagged visits from them look "direct".
- **The owner's devices:** marked with `mf-owner=1` in their own browser storage (set 2026-10-29 by a temporary `/me` page, removed the same day at the owner's request; it's in git history — `git show 7f39fd6:me.html` — if a device ever needs marking again after its website data is cleared). On a marked device the site sends no landing counts and marks taps `o=1` (not counted). Cloudflare Web Analytics can't skip a device, so its visit count still includes the owner.
- **A new App Store button** needs its placement in `worker/tap.js` (`BUTTONS`). Check with `python3 tools/check-measurement.py` (add `--release` before merging to `main`: it also wants the App Store provider token). Locally `/get` 404s like the pretty URLs; it only works on Cloudflare.
- The privacy page's "This website" section describes all of this; change it with any change here. The private intelligence platform archives both datasets daily (Cloudflare keeps taps 3 months, unsampled visits 7 days).

## Notes

- App Store badges are Apple's official ones, hotlinked from Apple's marketing toolbox.
- `BingSiteAuth.xml` (site root) proves ownership to Bing Webmaster Tools. Keep it: deleting it un-verifies the site.
- Reviews in the hero are real App Store reviews; don't invent ratings, testimonials or user counts.
- Score images are public domain / CC0 (OpenScore) only; credits for CC BY sounds are on the privacy page.
