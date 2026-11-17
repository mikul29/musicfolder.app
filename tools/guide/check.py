#!/usr/bin/env python3
"""Validates the built User Guide and the site's internal links. Run after build.py:

    python3 tools/guide/check.py          # all checks; exit 1 on any problem
    python3 tools/guide/check.py --words  # also print each guide's word count

Technical SEO: unique <title> and description, canonical = the page's own URL, exactly one <h1>,
no skipped heading levels, valid JSON-LD (BreadcrumbList), no noindex, every guide in the sitemap
once, every internal link and #anchor resolves, images exist with width/height/alt.
Writing: no em dashes, none of the banned phrases from WRITING.md, no runs of one-sentence
paragraphs, bold used sparingly, related guides 2–4.
This can't tell whether an instruction matches the app: that's the writers' and reviewers' job.
"""

from __future__ import annotations

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SITE = "https://musicfolder.app"
BANNED = ["whether you're", "whether you are", "next level", "unlock", "seamless", "effortless",
          "designed with musicians in mind", "more than just", "it's not just", "from rehearsals to",
          "everything you need", "all in one place", "say goodbye", "with just a few taps", "the result?",
          "here's where", "reimagined", "made simple", "powerful yet", "game-changing", "game changer",
          "streamline", "dive in", "let's ", "simply ", "effortlessly", "elevate", "supercharge",
          "in today's", "look no further", "the best part", "a breeze", "hassle-free", "at your fingertips",
          "journey", "empower", "harness", "robust"]


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = ""; self._in_title = False
        self.meta = {}; self.links = []; self.ids = set(); self.headings = []; self.imgs = []
        self.canonical = None; self.ld = []; self._in_ld = False; self._ld = ""
        self._h = None; self._htext = ""; self._main = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.add(a["id"])
        if tag == "title":
            self._in_title = True
        elif tag == "meta" and a.get("name"):
            self.meta[a["name"]] = a.get("content", "")
        elif tag == "link" and a.get("rel") == "canonical":
            self.canonical = a.get("href")
        elif tag == "a" and a.get("href"):
            self.links.append(a["href"])
        elif tag == "img":
            self.imgs.append(a)
        elif tag == "script" and a.get("type") == "application/ld+json":
            self._in_ld = True; self._ld = ""
        elif tag == "main":
            self._main = True
        elif re.fullmatch(r"h[1-6]", tag) and self._main:
            self._h = int(tag[1]); self._htext = ""

    def handle_endtag(self, tag):
        if tag == "main":
            self._main = False
        if tag == "title":
            self._in_title = False
        elif tag == "script" and self._in_ld:
            self._in_ld = False; self.ld.append(self._ld)
        elif self._h and tag == f"h{self._h}":
            self.headings.append((self._h, self._htext.strip())); self._h = None

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        if self._in_ld:
            self._ld += data
        if self._h:
            self._htext += data


def parse(path: Path) -> Page:
    p = Page(); p.feed(path.read_text(encoding="utf-8")); return p


def url_to_file(href: str) -> Path | None:
    path = href.split("#")[0].split("?")[0]
    if path in ("", "/"):
        return ROOT / "index.html"
    rel = path.lstrip("/")
    for cand in (ROOT / rel, ROOT / f"{rel}.html", ROOT / rel / "index.html"):
        if cand.is_file():
            return cand
    return None


def main() -> int:
    show_words = "--words" in sys.argv
    problems: list[str] = []
    inv = json.loads((ROOT / "tools/guide/inventory.json").read_text(encoding="utf-8"))
    slugs = [g["slug"] for ch in inv["chapters"] for g in ch["guides"]]
    pages = sorted(p for p in ROOT.rglob("*.html") if ".git" not in p.parts and "tools" not in p.parts)
    parsed = {p: parse(p) for p in pages}
    titles, descs = {}, {}
    for path, pg in parsed.items():
        rel = path.relative_to(ROOT).as_posix()
        if rel == "404.html":
            continue
        is_guide = rel == "guide.html" or rel.startswith("guide/")
        if is_guide:
            want = f"{SITE}/" + rel[:-5]
            if pg.canonical != want:
                problems.append(f"{rel}: canonical {pg.canonical} ≠ {want}")
            h1s = [h for h in pg.headings if h[0] == 1]
            if len(h1s) != 1:
                problems.append(f"{rel}: {len(h1s)} <h1> elements")
            last = 1
            for lvl, text in pg.headings:
                if lvl > last + 1 and not text.startswith("A better"):
                    problems.append(f"{rel}: heading level jumps to h{lvl} ({text[:40]})")
                last = lvl if lvl > 1 else last
            if "noindex" in pg.meta.get("robots", ""):
                problems.append(f"{rel}: noindex")
            for blob in pg.ld:
                try:
                    data = json.loads(blob)
                    if data.get("@type") == "BreadcrumbList":
                        for item in data["itemListElement"]:
                            f = url_to_file(item["item"].replace(SITE, "") or "/")
                            if not f:
                                problems.append(f"{rel}: breadcrumb item {item['item']} doesn't exist")
                except Exception as e:  # noqa: BLE001
                    problems.append(f"{rel}: invalid JSON-LD ({e})")
            for img in pg.imgs:
                if "toolbox.marketingtools.apple.com" in img.get("src", ""):
                    continue
                if img.get("alt") is None:
                    problems.append(f"{rel}: image {img.get('src')} has no alt attribute")
                for k in ("width", "height"):
                    if not img.get(k):
                        problems.append(f"{rel}: image {img.get('src')} has no {k}")
                src = img.get("src", "")
                if src.startswith("/") and not (ROOT / src.lstrip("/")).is_file():
                    problems.append(f"{rel}: image {src} is missing")
            if "Screenshot pending" in path.read_text(encoding="utf-8"):
                problems.append(f"{rel}: has a pending screenshot")
        t, d = pg.title.strip(), pg.meta.get("description", "")
        if t in titles:
            problems.append(f"{rel}: <title> duplicates {titles[t]}")
        if d and d in descs:
            problems.append(f"{rel}: description duplicates {descs[d]}")
        titles[t], descs[d] = rel, rel
        for href in pg.links:
            if not href.startswith("/") or href.startswith("//") or href.startswith("/get?"):
                continue
            target = url_to_file(href)
            if not target:
                problems.append(f"{rel}: broken link {href}")
            elif "#" in href:
                frag = href.split("#", 1)[1]
                if frag and frag not in parsed.get(target, parse(target)).ids:
                    problems.append(f"{rel}: link {href} points at a missing #{frag}")

    sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    locs = re.findall(r"<loc>([^<]+)</loc>", sitemap)
    for dup in {l for l in locs if locs.count(l) > 1}:
        problems.append(f"sitemap.xml: {dup} listed twice")
    for s in slugs + ["whats-new"]:
        if f"{SITE}/guide/{s}" not in locs:
            problems.append(f"sitemap.xml: /guide/{s} missing")
        if not (ROOT / "guide" / f"{s}.html").exists():
            problems.append(f"guide/{s}.html wasn't built")
    for l in locs:
        if not url_to_file(l.replace(SITE, "") or "/"):
            problems.append(f"sitemap.xml: {l} has no page")

    # writing checks on the sources
    for s in slugs:
        src = ROOT / "guide-src" / f"{s}.md"
        if not src.exists():
            continue
        text = src.read_text(encoding="utf-8")
        meta = json.loads(re.match(r"---\s*\n(.*?)\n---", text, re.S).group(1))
        body = text.split("\n---\n", 1)[1] if "\n---\n" in text else text
        low = re.sub(r"\*\*[^*]+\*\*", "", body).lower() + " " + meta.get("description", "").lower()
        if "—" in text:
            problems.append(f"{s}: em dash")
        for b in BANNED:
            if b in low:
                problems.append(f"{s}: banned phrase '{b.strip()}'")
        blocks = [p.strip() for p in re.split(r"\n\s*\n", body) if p.strip()]
        run = 0
        for p in blocks:
            if re.match(r"^(#|\d+\.|-|\{shot|Note:|Tip:|Important:|On iPhone:|On iPad:|On Mac:)", p):
                run = 0
                continue
            single = len(re.findall(r"[.!?](\s|$)", p)) <= 1 and len(p) < 140
            run = run + 1 if single else 0
            if run >= 3:
                problems.append(f"{s}: three one-sentence paragraphs in a row near: {p[:50]}")
                break
        words = len(re.findall(r"[A-Za-z0-9’']+", re.sub(r"\{[^}]+\}", "", body)))
        bolds = len(re.findall(r"\*\*[^*]+\*\*", body))
        if words and bolds / max(words, 1) > 0.06:
            print(f"! {s}: {bolds} bold spans in {words} words (check they're all interface labels)")
        if not 2 <= len(meta.get("related") or []) <= 4:
            problems.append(f"{s}: {len(meta.get('related') or [])} related guides (2–4)")
        if meta.get("open_questions"):
            print(f"? {s}: {len(meta['open_questions'])} open question(s)")
        if show_words:
            print(f"{words:5d}  {s}")

    for p in problems:
        print("✗", p)
    print(f"{'ok' if not problems else str(len(problems)) + ' problem(s)'}: {len(pages)} pages, {len(slugs)} guides checked")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
