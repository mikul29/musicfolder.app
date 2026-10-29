#!/usr/bin/env python3
"""Checks the site's measurement wiring (decision D1). Run from the repo folder:

    python3 tools/check-measurement.py            # before committing
    python3 tools/check-measurement.py --release  # before merging to main: real tokens filled in

- every App Store button goes through /get?from=<placement>, with a placement that matches its
  page and is listed in worker/tap.js (unlisted ones would be counted as "other");
- no page links straight to apps.apple.com (the JSON-LD downloadUrl on the home page is data
  for search engines, not a button, and stays direct);
- no page carries its own Cloudflare Web Analytics beacon: the site uses Cloudflare's automatic
  setup (the beacon is added at the edge), so a snippet in the HTML would count every visit twice;
- wrangler.jsonc runs the Worker for /get and binds the TAPS dataset;
- worker/tap.test.js passes (macOS JavaScriptCore; skipped where it's missing).
--release also fails on a missing App Store provider token.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
JSC = Path("/System/Library/Frameworks/JavaScriptCore.framework/Versions/Current/Helpers/jsc")
BEACON = "static.cloudflareinsights.com/beacon.min.js"


def page_name(path: Path) -> str:
    rel = path.relative_to(ROOT).with_suffix("").as_posix()
    return {"index": "home", "404": "notfound"}.get(rel, rel.replace("/", "-"))


def listed_placements() -> set[str]:
    source = (ROOT / "worker/tap.js").read_text(encoding="utf-8")
    block = re.search(r"export const BUTTONS = \{(.*?)\n\};", source, re.S).group(1)
    return {f"{page}-{pos}" for page, positions in re.findall(r'"([a-z0-9-]+)": \[([^\]]*)\]', block)
            for pos in re.findall(r'"([a-z-]+)"', positions)}


def main() -> int:
    release = "--release" in sys.argv
    problems: list[str] = []
    listed = listed_placements()
    used: dict[str, str] = {}
    pages = sorted(p for p in ROOT.rglob("*.html") if ".git" not in p.parts)
    for path in pages:
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT).as_posix()
        for href in re.findall(r'href="(https://apps\.apple\.com[^"]*)"', text):
            problems.append(f"{rel}: direct App Store link {href} (use /get?from=<placement>)")
        for placement in re.findall(r'href="/get\?from=([^"&]+)"', text):
            if placement in used:
                problems.append(f"{rel}: placement {placement} also used in {used[placement]}")
            used[placement] = rel
            if not placement.startswith(page_name(path) + "-"):
                problems.append(f"{rel}: placement {placement} doesn't start with this page's name {page_name(path)}-")
            if placement not in listed:
                problems.append(f"{rel}: placement {placement} isn't in worker/tap.js BUTTONS")
        if BEACON in text:
            problems.append(f"{rel}: has its own Web Analytics beacon; automatic setup already adds one (double count)")
    for placement in sorted(listed - set(used)):
        problems.append(f"worker/tap.js: {placement} is listed but no page uses it")

    wrangler = (ROOT / "wrangler.jsonc").read_text(encoding="utf-8")
    for needed in ('"main": "worker/index.js"', '"run_worker_first": ["/get"]', '"binding": "TAPS"'):
        if needed not in wrangler:
            problems.append(f"wrangler.jsonc: missing {needed}")
    if release and re.search(r'"APP_STORE_PROVIDER_TOKEN":\s*""', wrangler):
        problems.append("wrangler.jsonc: APP_STORE_PROVIDER_TOKEN is empty (no App Store campaign attribution)")
    if "Disallow: /get" not in (ROOT / "robots.txt").read_text(encoding="utf-8"):
        problems.append("robots.txt: crawlers should skip /get")

    if JSC.exists():
        result = subprocess.run([str(JSC), "-m", "worker/tap.test.js"], cwd=ROOT, capture_output=True, text=True)
        print(result.stdout.strip())
        if result.returncode != 0:
            problems.append(f"worker/tap.test.js failed: {result.stderr.strip()}")
    else:
        print("skipped worker/tap.test.js (no JavaScriptCore)")

    for problem in problems:
        print("✗", problem)
    if not problems:
        print(f"ok: {len(pages)} pages, {len(used)} App Store buttons through /get, no manual beacon"
              + (" (release check)" if release else ""))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
