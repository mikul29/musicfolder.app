#!/usr/bin/env python3
"""Links the marketing pages to the User Guide. Run from the repo folder after build.py:

    python3 tools/guide/crosslinks.py

- Feature, audience and pricing pages: a short "Step-by-step guides" list under their FAQ (same
  column), between <!-- guides:start --> and <!-- guides:end -->, so re-running replaces it.
- Every page's footer: "User Guide" in the Support column.
Marketing pages explain why; guides explain how. Keep each list to the 3–5 guides a reader of that
page is most likely to need, never a sitewide block.
"""

from __future__ import annotations

import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
INV = json.loads((ROOT / "tools/guide/inventory.json").read_text(encoding="utf-8"))
TITLES = {g["slug"]: g["title"] for ch in INV["chapters"] for g in ch["guides"]}

LINKS = {
    "features/sheet-music-organizer.html": ["import-music", "add-sections-to-a-book", "organize-music-in-folders",
                                            "find-music-with-search-and-filters", "organize-rotate-and-crop-pages"],
    "features/sheet-music-reader.html": ["the-reader-at-a-glance", "turn-pages", "change-the-page-view",
                                         "use-performance-mode", "jump-to-repeats-with-page-links"],
    "features/set-lists.html": ["create-and-edit-a-set-list", "add-pages-and-timing-to-a-set-list", "play-a-set-list"],
    "features/page-turner.html": ["turn-pages-hands-free", "turn-pages", "page-turner-isnt-turning-pages"],
    "features/annotation.html": ["mark-up-music-with-apple-pencil", "use-annotation-layers",
                                 "add-text-symbols-and-shapes"],
    "features/chord-charts.html": ["create-a-chord-chart", "transpose-capo-and-numbers", "set-the-song-order",
                                   "format-a-chord-chart", "turn-a-pdf-into-a-chord-chart"],
    "features/sharing.html": ["share-a-folder-or-set-list", "join-a-shared-folder-or-set-list",
                              "work-together-in-a-shared-folder-or-set-list", "send-a-copy-or-print"],
    "features/toolkit.html": ["use-the-metronome", "tune-and-play-reference-tones", "play-the-piano",
                              "play-along-with-recordings", "track-your-practice"],
    "features/free-sheet-music.html": ["get-free-sheet-music", "import-music", "add-sections-to-a-book"],
    "planning-center.html": ["connect-planning-center", "play-a-service-plan", "transpose-capo-and-numbers"],
    "for/bands.html": ["create-and-edit-a-set-list", "share-a-folder-or-set-list", "create-a-chord-chart",
                       "turn-pages-hands-free"],
    "for/worship-teams.html": ["connect-planning-center", "play-a-service-plan", "transpose-capo-and-numbers",
                               "share-a-folder-or-set-list"],
    "for/orchestras-choirs.html": ["add-sections-to-a-book", "mark-up-music-with-apple-pencil",
                                   "use-annotation-layers", "jump-to-repeats-with-page-links"],
    "for/students.html": ["track-your-practice", "use-the-metronome", "mark-up-music-with-apple-pencil",
                          "play-along-with-recordings"],
    "pricing.html": ["free-and-premium", "manage-your-subscription", "sync-with-icloud"],
}

START, END = "<!-- guides:start -->", "<!-- guides:end -->"


def block(slugs):
    items = "".join(f'<li><a href="/guide/{s}">{html.escape(TITLES[s])}</a></li>' for s in slugs)
    return (f'{START}<div class="lp-guides"><h3>Step-by-step guides</h3><ul>{items}</ul>'
            f'<p class="lp-guides-all"><a href="/guide">Browse the User Guide</a></p></div>{END}')


def main():
    changed = []
    for rel, slugs in LINKS.items():
        for s in slugs:
            assert s in TITLES, f"{rel}: unknown guide {s}"
        path = ROOT / rel
        text = path.read_text(encoding="utf-8")
        new = block(slugs)
        if START in text:
            text2 = re.sub(re.escape(START) + ".*?" + re.escape(END), new, text, flags=re.S)
        else:
            # after the FAQ list, as the next child of .lp-faq-grid
            m = re.search(r'(<div class="wrap lp-faq-grid">.*?<div class="faq">.*?</details></div>)', text, re.S)
            if not m:
                raise SystemExit(f"{rel}: no FAQ grid to attach the guides to")
            text2 = text[:m.end()] + "\n    " + new + text[m.end():]
        if text2 != text:
            path.write_text(text2, encoding="utf-8")
            changed.append(rel)

    # footer: User Guide first in the Support column, on every page
    old = '<li><a href="/support">Help &amp; FAQ</a></li>'
    new_li = '<li><a href="/guide">User Guide</a></li>\n          ' + old
    for path in sorted(ROOT.rglob("*.html")):
        if ".git" in path.parts or path.parts[-2] == "guide" or path.name == "guide.html":
            continue
        text = path.read_text(encoding="utf-8")
        if old in text and 'href="/guide">User Guide</a></li>' not in text:
            path.write_text(text.replace(old, new_li, 1), encoding="utf-8")
            changed.append(path.relative_to(ROOT).as_posix() + " (footer)")
    print("\n".join(changed) or "nothing to change")


if __name__ == "__main__":
    main()
