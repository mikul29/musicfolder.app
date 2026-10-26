# Music Folder marketing site

Static site, no build step: one HTML file per page (`index.html`, `pricing.html`, `features/*.html`, `for/*.html`, …), shared styles in `assets/site.css` (+ `assets/pages.css` for the landing/feature pages), shared behaviour in `assets/site.js`; the home page's hero script is inline at the bottom of `index.html`. Visual rules and copy brief live in the app repo (`DESIGN.md`, `WEBSITE_BRIEF.md`).

Deploys: Cloudflare Worker "musicfolder-app" serves the repo as static assets and redeploys on every push to `main` (about 1–3 minutes). `.assetsignore` keeps repo files like this README off the site. Work on a branch and merge to `main` when it's ready to go live.

Preview locally:

```sh
python3 -m http.server 8765
```

(Pretty URLs like `/about` only work on Cloudflare; locally open `about.html`.)

When `assets/site.css` changes, bump `site.css?v=N` on every page so returning visitors fetch it.

## Home hero: the folder opens, everything flies into the iPad

`.hero` is 530vh tall with a sticky 100vh stage. `frame()` maps scroll progress through `pace()` (the cover opening and the tool tiles run faster than the flights) to the timeline `p` (0–1) used by the phases below; everything is scroll-linked except the tool tiles' little hints and the review dots, which run on timers.

| p | What happens |
|---|---|
| 0 – 0.13 | the tilted folder straightens and centres; hero copy fades |
| 0.13 – 0.31 | the cover swings open on an overstuffed pocket (6 paper folders, 6 scores, a printed set list) |
| 0.30 – 0.35 | the iPad on the right page wakes (screen content fades up from black) |
| 0.33 – 0.63 | the 13 items fly, top of the pile first: straight up out of the pocket, over the spine, down into their slot on the screen (one cubic Bézier each). Folders square up into app icons, the set list turns into its card; each slot's mask fades as its item lands |
| 0.64 – 0.78 | the iPad slides out of the pocket and is handed to a stage layer (`.ipad-stage`) above the folder, travels front and centre; the cover closes and the folder settles behind as a tilted backdrop |
| 0.75 – 0.79 | the practice ring fills and Sun–Wed tick in |
| 0.79 – 0.99 | the four tool tiles lift one by one with live hints (piano keys, pendulum, drone bars, tuner needle) |
| 0.90 – 0.97 | "The last folder you'll ever need." fades in |

The folder is laid out at a fixed 450×600 (rig coordinates) and scaled as a whole. The iPad screen is the owner's real 11-inch iPad Home screenshot (October 2026 layout, + button top right), `assets/hero-ipad-home.webp` (1668×2420; positions are measured in a 1379×2000 space, `SHOT_W`/`SHOT_H`), retouched to the site's content: a clean 9:41, the "Summer Night Concert" card for tomorrow, the "Two weeks strong" practice card, a generic "Worship Team" title over the church's Planning Center folder, and the folders and scores the items fly into (the retouch is reproducible: `screens/` in the onboarding-video workspace, `~/Documents/Me/Music_Folder/Onboarding-Video-Preview`). Positions on it are in screenshot pixels (`folderSlot`, `scoreSlot`, `setlistSlot`, `TOOLS`, `OVERLAYS`) and scaled by `K`. Two parts are rebuilt crisp in HTML over the screenshot because they animate: the practice card (its ring fills and the days tick in) and the tool tiles (built at their lifted size so they stay sharp). The printed set list (`.mf-setlist`) is laid out as the card scaled to its 280 px width, so it lands line for line. If the screenshot is ever replaced, re-measure those coordinates.

With `prefers-reduced-motion`, the hero is static.

## Device images

`assets/home-ipad.webp` and `assets/home-iphone.webp` (home dark band, Students page) are framed renders of the owner's real Home screenshots, retouched to the same content as the hero (`screens/frame.py` in the onboarding-video workspace draws the bezel). The general recipe: an HTML page with the bezel and the screenshot, rendered with headless Chrome at 2×:

```sh
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --hide-scrollbars \
  --default-background-color=00000000 --force-device-scale-factor=2 \
  --window-size=600,851 --screenshot=out.png file:///path/to/frame.html
```

## Notes

- App Store badges are Apple's official ones, hotlinked from Apple's marketing toolbox.
- Reviews in the hero are real App Store reviews; don't invent ratings, testimonials or user counts.
- Score images are public domain / CC0 (OpenScore) only; credits for CC BY sounds are on the privacy page.
