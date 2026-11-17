#!/usr/bin/env python3
"""Puts every User Guide screenshot in place: assets/guide/<id>.jpg + <id>.webp.

    python3 tools/guide/images.py [--raw <folder of simulator captures>] [--list]

For each `shots` entry in guide-src/*.md:
- `reuse`: an existing real capture in assets/ is converted to the guide's sizes;
- otherwise tools/guide/captures.json says which raw simulator capture (PNG) it comes from and,
  for crops, the crop box in the capture's own pixels: {"<id>": {"src": "name.png", "box": [x0, y0, x1, y1]}}.
Clips (kind "clip") are made separately (tools/guide/README in the repo README: simctl recordVideo +
avconvert); this script only makes their poster frame if captures.json names one.
Sizes are 2× the width the page shows them at, so they stay sharp on Retina screens.
--list prints every shot and whether its image exists.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "assets" / "guide"
# CSS widths in assets/guide.css × 2
MAX_W = {("screen", "ipad", "portrait"): 1040, ("screen", "ipad", "landscape"): 1440,
         ("screen", "iphone", "portrait"): 600, ("crop", "iphone", "portrait"): 600}


def shots():
    for src in sorted((ROOT / "guide-src").glob("*.md")):
        meta = json.loads(re.match(r"---\s*\n(.*?)\n---", src.read_text(encoding="utf-8"), re.S).group(1))
        for s in meta.get("shots") or []:
            yield src.stem, s


def save(im: Image.Image, shot: dict):
    kind, dev, ori = shot.get("kind", "crop"), shot.get("device", "ipad"), shot.get("orientation", "portrait")
    w = MAX_W.get((kind, dev, ori), 600 if dev == "iphone" else 920)
    im = im.convert("RGB")
    if im.width > w:
        im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
    OUT.mkdir(parents=True, exist_ok=True)
    im.save(OUT / f"{shot['id']}.jpg", "JPEG", quality=84, optimize=True, progressive=True)
    im.save(OUT / f"{shot['id']}.webp", "WEBP", quality=80, method=6)


def main() -> int:
    raw = Path(sys.argv[sys.argv.index("--raw") + 1]) if "--raw" in sys.argv else None
    caps_path = ROOT / "tools/guide/captures.json"
    caps = json.loads(caps_path.read_text(encoding="utf-8")) if caps_path.exists() else {}
    missing = []
    for slug, s in shots():
        sid = s["id"]
        have = (OUT / f"{sid}.jpg").exists()
        if "--list" in sys.argv:
            print(f"{'✓' if have else '·'} {s.get('kind'):6} {sid:34} {slug}  reuse={s.get('reuse')}")
            continue
        if s.get("kind") == "clip" and sid not in caps:
            if not have:
                missing.append(f"{sid} (clip, {slug})")
            continue
        if sid in caps and raw:
            c = caps[sid]
            im = Image.open(raw / c["src"])
            if c.get("box"):
                im = im.crop(tuple(c["box"]))
            save(im, s)
        elif s.get("reuse") and not have:
            name = s["reuse"]
            path = ROOT / "assets" / name if "." in name else ROOT / "assets" / f"{name}.jpg"
            if not path.exists():
                missing.append(f"{sid}: reuse {name} not found")
                continue
            save(Image.open(path), s)
        elif not have:
            missing.append(f"{sid} ({s.get('kind')}, {slug})")
    for m in missing:
        print("· still needed:", m)
    return 0


if __name__ == "__main__":
    sys.exit(main())
