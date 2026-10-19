# Music Folder marketing site

Static, single page: `index.html` (inline CSS + JS, no build step). Visual rules and copy brief live in the app repo (DESIGN.md, WEBSITE_BRIEF.md).

Preview locally:

```sh
python3 -m http.server 8765
```

## Hero: the folder opens on scroll

`.hero` is 290vh tall with a sticky 100vh stage. `frame()` in the script maps scroll progress `p` (0–1) to three phases:

| p | What happens |
|---|---|
| 0 – 0.30 | the tilted folder straightens and moves to centre; hero copy fades out |
| 0.30 – 0.74 | the cover (`#cover`) swings open on its spine; the inside leaf (`#leaf`, the set-list sheet in its pocket) swings in from the other side and lands flat (`transform: none`, so its text stays crisp) |
| 0.70 – 0.90 | the "Every chart. Every set. One folder." caption fades in |

The folder is laid out at a fixed 450×600 and scaled as a whole. The iPad score inside is an SVG drawn by the script. With `prefers-reduced-motion`, the hero is static.

## Owner TODOs

- Replace every `[Screenshot: …]` slot (`.device .screen`) with real App Store screenshots: drop an `<img>` inside the `.screen` div.
- Add `assets/og-image.png` (1200×630) and set the final site URL in the Open Graph tags.
- The App Store badges are Apple's official ones, hotlinked from Apple's marketing toolbox (`toolbox.marketingtools.apple.com`). To self-host them, download them from Apple's Marketing Resources and point the `img`/`source` tags at them.
- There are no testimonials, ratings or user counts on purpose. If you add real ones later, use the program-card style.
