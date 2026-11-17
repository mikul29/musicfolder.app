#!/usr/bin/env python3
"""Builds the Music Folder User Guide: guide-src/*.md → guide.html (hub), guide/<slug>.html,
guide/whats-new.html, assets/guide-search.json, plus the guide's lines in sitemap.xml and
worker/tap.js (App Store placements). Run from the repo folder:

    python3 tools/guide/build.py            # build; missing articles/images fail the build
    python3 tools/guide/build.py --draft    # build what exists, mark missing images as pending

Every page is static HTML a crawler can read without JavaScript. The site chrome (header, footer)
is taken from support.html at build time, so it always matches the rest of the site.
Format of a source file and the writing rules: tools/guide/WRITING.md.
"""

from __future__ import annotations

import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "guide-src"
TOOLS = ROOT / "tools" / "guide"
OUT_DIR = ROOT / "guide"
IMG_DIR = ROOT / "assets" / "guide"
SITE = "https://musicfolder.app"
SITE_CSS = "61"          # keep in step with the other pages' site.css?v=
GUIDE_CSS = "4"
GUIDE_JS = "2"
SITE_JS = "6"
DRAFT = "--draft" in sys.argv

FEATURE_PAGES = {"/features/sheet-music-organizer", "/features/sheet-music-reader", "/features/set-lists",
                 "/features/page-turner", "/features/annotation", "/features/chord-charts",
                 "/features/sharing", "/features/toolkit", "/features/free-sheet-music", "/planning-center",
                 "/for/bands", "/for/worship-teams", "/for/orchestras-choirs", "/for/students", "/pricing",
                 "/support", "/contact", "/privacy", "/about"}

# Words people type that mean the same thing as words in the guide (search only; never shown).
SYNONYMS = {
    "bookmark": ["section"], "bookmarks": ["sections"], "playlist": ["set list"], "playlists": ["set lists"],
    "setlist": ["set list"], "setlists": ["set lists"], "pedal": ["page turner"], "pedals": ["page turner"],
    "footswitch": ["page turner"], "airturn": ["page turner"], "chord sheet": ["chord chart"],
    "chord sheets": ["chord charts"], "chordpro": ["chord chart"], "lead sheet": ["chord chart"],
    "score": ["music", "piece"], "scores": ["music", "pieces"], "song": ["piece"], "songs": ["pieces", "music"],
    "sheet music": ["music"], "pdf": ["music", "import"], "pdfs": ["music", "import"],
    "collaboration": ["share"], "collaborate": ["share"], "collab": ["share"], "band": ["share"],
    "draw": ["annotate", "mark up"], "drawing": ["annotate"], "markings": ["annotate"],
    "annotations": ["annotate"], "pencil": ["annotate"], "highlight": ["annotate"], "group": ["folder"],
    "groups": ["folders"], "transpose": ["key"], "key change": ["transpose"], "capo": ["transpose"],
    "subscription": ["premium"], "subscribe": ["premium"], "price": ["premium"], "cost": ["premium"],
    "refund": ["subscription"], "backup": ["back up"], "restore": ["back up"], "cloud": ["icloud", "sync"],
    "mac": ["mac"], "macbook": ["mac"], "computer": ["mac"], "turn page": ["turn pages"],
    "page turn": ["turn pages"], "flip": ["turn pages"], "dark mode": ["dark background"],
    "night mode": ["dark background"], "split": ["sections"], "hymnal": ["sections", "book"],
    "fake book": ["sections", "book"], "songbook": ["sections", "book"], "movement": ["sections"],
    "click track": ["metronome"], "click": ["metronome"], "bpm": ["tempo", "metronome"],
    "tuning": ["tuner"], "drone": ["tones"], "keyboard": ["piano", "shortcuts"], "audio": ["recording"],
    "mp3": ["recording"], "backing track": ["recording"], "service": ["planning center"],
    "pco": ["planning center"], "church": ["planning center"], "worship": ["planning center"],
    "delete": ["remove"], "trash": ["recently removed", "delete"], "undo": ["previous version"],
    "missing": ["empty", "sync"], "disappeared": ["empty", "sync"], "lost": ["empty", "restore"],
}


# ---------------------------------------------------------------------------------------------
# Loading
# ---------------------------------------------------------------------------------------------

def load_inventory():
    inv = json.loads((TOOLS / "inventory.json").read_text(encoding="utf-8"))
    order = []
    for ci, ch in enumerate(inv["chapters"]):
        for gi, g in enumerate(ch["guides"]):
            g["chapter"] = ch
            order.append(g)
    return inv, order


def parse_source(path: Path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"---\s*\n(.*?)\n---\s*\n(.*)\Z", text, re.S)
    if not m:
        raise SystemExit(f"{path.name}: no front matter between --- lines")
    try:
        meta = json.loads(m.group(1))
    except json.JSONDecodeError as e:
        raise SystemExit(f"{path.name}: front matter isn't valid JSON ({e})")
    return meta, m.group(2)


def load_icons():
    path = TOOLS / "icons.json"
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


# ---------------------------------------------------------------------------------------------
# Body rendering (the Markdown subset in WRITING.md §6)
# ---------------------------------------------------------------------------------------------

CALLOUTS = {"Note:": "note", "Tip:": "tip", "Important:": "important",
            "On iPhone:": "device", "On iPad:": "device", "On Mac:": "device"}


class Renderer:
    def __init__(self, slug, meta, icons, slugs, problems):
        self.slug, self.meta, self.icons, self.slugs, self.problems = slug, meta, icons, slugs, problems
        self.shots = {s["id"]: s for s in meta.get("shots") or []}
        self.used_icons: set[str] = set()
        self.headings: list[tuple[int, str, str]] = []
        self.first_image = True
        self.links: list[str] = []

    def inline(self, text: str) -> str:
        out = html.escape(text, quote=False)

        def icon(m):
            name = m.group(1)
            self.used_icons.add(name)
            svg = self.icons.get(name)
            if svg is None:
                if not DRAFT:
                    self.problems.append(f"{self.slug}: no icon drawn for sf:{name} (tools/guide/icons.json)")
                return f'<span class="ui-icon ui-icon-missing" aria-hidden="true"></span>'
            return (f'<svg class="ui-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
                    f'stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" '
                    f'focusable="false">{svg}</svg>')
        out = re.sub(r"\{sf:([A-Za-z0-9.]+)\}", icon, out)
        out = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", out)

        def link(m):
            label, href = m.group(1), m.group(2)
            self.links.append(href)
            attrs = ""
            if href.startswith("/guide/"):
                target = href.split("#")[0][len("/guide/"):]
                if target not in self.slugs and target != "whats-new":
                    self.problems.append(f"{self.slug}: link to unknown guide {href}")
            elif href.startswith("/"):
                base = href.split("#")[0]
                if base not in FEATURE_PAGES:
                    self.problems.append(f"{self.slug}: link to unknown page {href}")
                attrs = ' data-ev="nav"'
            elif href.startswith("https://"):
                attrs = ' rel="noopener"'
            else:
                self.problems.append(f"{self.slug}: link must be site-relative or https: {href}")
            return f'<a href="{html.escape(href)}"{attrs}>{label}</a>'
        out = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", link, out)
        return out

    def figure(self, shot_id: str) -> str:
        s = self.shots.get(shot_id)
        if not s:
            self.problems.append(f"{self.slug}: {{shot:{shot_id}}} isn't defined in shots")
            return ""
        kind = s.get("kind", "crop")
        alt = s.get("alt") or ""
        if not alt:
            self.problems.append(f"{self.slug}: shot {shot_id} has no alt text")
        cap = s.get("caption")
        figcap = f"<figcaption>{self.inline(cap)}</figcaption>" if cap else ""
        cls = f"shot shot-{kind} shot-{s.get('device', 'ipad')} shot-{s.get('orientation', 'portrait')}"
        lazy = "eager" if self.first_image and kind == "screen" else "lazy"
        self.first_image = False
        if kind == "clip":
            mp4 = IMG_DIR / f"{shot_id}.mp4"
            poster = IMG_DIR / f"{shot_id}.jpg"
            if not (mp4.exists() and poster.exists()):
                return self.pending(shot_id, s, cls, figcap)
            w, h = image_size(poster)
            return (f'<figure class="{cls}"><video class="clip" data-clip muted loop playsinline preload="none" '
                    f'width="{w}" height="{h}" poster="/assets/guide/{shot_id}.jpg" aria-label="{html.escape(alt)}">'
                    f'<source src="/assets/guide/{shot_id}.mp4" type="video/mp4"></video>'
                    f'<button class="clip-toggle" type="button" hidden>Play</button>{figcap}</figure>')
        jpg = IMG_DIR / f"{shot_id}.jpg"
        webp = IMG_DIR / f"{shot_id}.webp"
        if not jpg.exists():
            return self.pending(shot_id, s, cls, figcap)
        w, h = image_size(jpg)
        source = f'<source srcset="/assets/guide/{shot_id}.webp" type="image/webp">' if webp.exists() else ""
        fetch = ' fetchpriority="high"' if lazy == "eager" else ""
        # The link opens the full image (guide.js shows it in a viewer; without JavaScript the browser opens it)
        return (f'<figure class="{cls}"><a class="shot-zoom" href="/assets/guide/{shot_id}.jpg" '
                f'data-zoom data-w="{w}" data-h="{h}"><picture>{source}<img src="/assets/guide/{shot_id}.jpg" '
                f'alt="{html.escape(alt)}" width="{w}" height="{h}" loading="{lazy}" decoding="async"{fetch}>'
                f'</picture><span class="zoom-hint" aria-hidden="true"></span>'
                f'<span class="sr-only"> (opens the full-size image)</span></a>{figcap}</figure>')

    def pending(self, shot_id, s, cls, figcap):
        if not DRAFT:
            self.problems.append(f"{self.slug}: image for shot {shot_id} isn't in assets/guide/")
        return (f'<figure class="{cls} shot-pending"><div class="pending-box">Screenshot pending: '
                f'{html.escape(s.get("state", ""))}</div>{figcap}</figure>')

    def render(self, body: str) -> str:
        lines = body.strip("\n").split("\n")
        out: list[str] = []
        i = 0
        para: list[str] = []

        def flush():
            nonlocal para
            if para:
                text = " ".join(x.strip() for x in para)
                out.append(self.paragraph(text))
                para = []

        while i < len(lines):
            line = lines[i]
            if not line.strip():
                flush(); i += 1; continue
            m = re.match(r"^(#{2,3})\s+(.*)$", line)
            if m:
                flush()
                level = len(m.group(1))
                text = m.group(2).strip()
                hid = slugify(text)
                ids = {h[1] for h in self.headings}
                n = 2
                base = hid
                while hid in ids:
                    hid = f"{base}-{n}"; n += 1
                self.headings.append((level, hid, text))
                out.append(f'<h{level} id="{hid}">{self.inline(text)}</h{level}>')
                i += 1; continue
            m = re.match(r"^\{shot:([a-z0-9-]+)\}\s*$", line.strip())
            if m:
                flush(); out.append(self.figure(m.group(1))); i += 1; continue
            if re.match(r"^\s*(\d+)\.\s+", line) or re.match(r"^\s*-\s+", line):
                flush()
                ordered = bool(re.match(r"^\s*\d+\.", line))
                items: list[str] = []
                pat = r"^\s*\d+\.\s+(.*)$" if ordered else r"^\s*-\s+(.*)$"
                while i < len(lines):
                    l = lines[i]
                    mm = re.match(pat, l)
                    if mm:
                        items.append(mm.group(1).strip()); i += 1; continue
                    if l.startswith("   ") and l.strip() and items:
                        items[-1] += " " + l.strip(); i += 1; continue
                    break
                tag = "ol" if ordered else "ul"
                cls = ' class="steps"' if ordered else ""
                out.append(f"<{tag}{cls}>" + "".join(f"<li>{self.inline(x)}</li>" for x in items) + f"</{tag}>")
                continue
            if line.lstrip().startswith("#"):
                self.problems.append(f"{self.slug}: only ## and ### headings are allowed: {line.strip()[:40]}")
            para.append(line); i += 1
        flush()
        return "\n".join(out)

    def paragraph(self, text: str) -> str:
        for prefix, kind in CALLOUTS.items():
            if text.startswith(prefix):
                rest = text[len(prefix):].strip()
                return (f'<div class="callout callout-{kind}"><p><span class="callout-label">{prefix[:-1]}</span> '
                        f'{self.inline(rest)}</p></div>')
        return f"<p>{self.inline(text)}</p>"


def slugify(text: str) -> str:
    s = re.sub(r"\{sf:[^}]+\}", "", text)
    s = re.sub(r"[*_`]", "", s).lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s or "section"


_size_cache: dict[Path, tuple[int, int]] = {}


def image_size(path: Path) -> tuple[int, int]:
    if path not in _size_cache:
        from PIL import Image  # Pillow; only needed once images exist
        with Image.open(path) as im:
            _size_cache[path] = im.size
    return _size_cache[path]


def plain(html_text: str) -> str:
    t = re.sub(r"<[^>]+>", " ", html_text)
    return re.sub(r"\s+", " ", html.unescape(t)).strip()


# ---------------------------------------------------------------------------------------------
# Site chrome, taken from support.html
# ---------------------------------------------------------------------------------------------

def chrome():
    s = (ROOT / "support.html").read_text(encoding="utf-8")
    header = s[s.index('<header class="site-header"'):s.index("</header>") + len("</header>")]
    footer = s[s.index('<footer class="site-footer">'):s.index("</footer>") + len("</footer>")]
    return header, footer


def page_header(header: str, page: str) -> str:
    # support.html marks its own link as the current page; guide pages are in the Support section
    # (the group stays is-current), and only the hub is the User Guide page itself.
    h = header.replace('<a href="/support" aria-current="page">', '<a href="/support">')
    if page == "guide":
        h = h.replace('<a href="/guide">', '<a href="/guide" aria-current="page">')
    h = h.replace('href="/get?from=support-nav"', f'href="/get?from={page}-nav"')
    h = h.replace('href="/get?from=support-menu"', f'href="/get?from={page}-menu"')
    h = h.replace('src="assets/', 'src="/assets/')
    return h


def head(title, description, canonical, og_title, og_desc, extra=""):
    e = html.escape
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<link rel="canonical" href="{canonical}">
<meta name="description" content="{e(description)}">
<meta property="og:type" content="article">
<meta property="og:url" content="{canonical}">
<meta property="og:title" content="{e(og_title)}">
<meta property="og:description" content="{e(og_desc)}">
<meta property="og:image" content="{SITE}/assets/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Meet Music Folder: a black music folder with silver corners">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(og_title)}">
<meta name="twitter:description" content="{e(og_desc)}">
<meta name="twitter:image" content="{SITE}/assets/og-image.jpg">
<meta name="apple-itunes-app" content="app-id=1611824311">
<meta name="theme-color" content="#FBFAF8">
<meta name="color-scheme" content="light only">
<link rel="icon" type="image/png" href="/assets/favicon.png?v=2">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="preload" href="/assets/fonts/instrument-serif-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/instrument-serif-italic-latin.woff2" as="font" type="font/woff2" crossorigin>
{extra}<link rel="stylesheet" href="/assets/site.css?v={SITE_CSS}">
<link rel="stylesheet" href="/assets/guide.css?v={GUIDE_CSS}">
</head>
<body class="guide-page">
"""


def breadcrumb_ld(items):
    data = {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": u}
                                for i, (n, u) in enumerate(items)]}
    return '<script type="application/ld+json">\n' + json.dumps(data, indent=2, ensure_ascii=False) + "\n</script>\n"


def closing(page, footer):
    return f"""
<section class="section final guide-final">
  <div class="wrap">
    <h2 class="heading">A better <em>home</em> for your sheet music.</h2>
    <p>Made by musicians, for musicians.</p>
    <div class="cta-row">
      <a class="badge-link" href="/get?from={page}-final">
        <picture>
          <img src="https://toolbox.marketingtools.apple.com/api/badges/download-on-the-app-store/black/en-us?size=250x83" alt="Download on the App Store" width="144" height="48" loading="lazy">
        </picture>
      </a>
    </div>
  </div>
</section>
</main>
{footer}
<script>
(() => {{
  document.getElementById('year').textContent = new Date().getFullYear();
  const header = document.querySelector('.site-header');
  const onScroll = () => header.classList.toggle('scrolled', window.scrollY > 8);
  window.addEventListener('scroll', onScroll, {{ passive: true }});
  onScroll();
  const menu = document.querySelector('.menu');
  menu && menu.addEventListener('click', e => {{ if (e.target.tagName === 'A') menu.removeAttribute('open'); }});
}})();
</script>
<script src="/assets/site.js?v={SITE_JS}" defer></script>
<script src="/assets/guide.js?v={GUIDE_JS}" defer></script>
</body>
</html>
"""


SEARCH_SVG = ('<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" '
              'aria-hidden="true"><circle cx="8.5" cy="8.5" r="5.5"/><path d="M13 13l4 4"/></svg>')


def search_box(id_, placeholder, compact=False):
    cls = "guide-search compact" if compact else "guide-search"
    return f"""<form class="{cls}" role="search" action="/guide" method="get" data-guide-search>
  {SEARCH_SVG}
  <label class="sr-only" for="{id_}">Search the User Guide</label>
  <input id="{id_}" name="q" type="search" placeholder="{placeholder}" autocomplete="off" spellcheck="false" aria-controls="{id_}-results" aria-autocomplete="list">
  <div class="guide-results" id="{id_}-results" role="listbox" aria-label="Search results" hidden></div>
</form>"""


def sidebar(inv, current_slug):
    parts = ['<nav class="guide-nav" aria-label="User Guide">',
             '<a class="guide-nav-home" href="/guide">User Guide</a>']
    for ch in inv["chapters"]:
        here = any(g["slug"] == current_slug for g in ch["guides"])
        parts.append(f'<details class="guide-nav-ch"{" open" if here else ""}><summary>{html.escape(ch["title"])}</summary><ul>')
        for g in ch["guides"]:
            cur = ' aria-current="page"' if g["slug"] == current_slug else ""
            parts.append(f'<li><a href="/guide/{g["slug"]}"{cur}>{html.escape(g["title"])}</a></li>')
        parts.append("</ul></details>")
    cur = ' aria-current="page"' if current_slug == "whats-new" else ""
    parts.append(f'<a class="guide-nav-extra" href="/guide/whats-new"{cur}>What&#39;s New</a>')
    parts.append('<a class="guide-nav-extra" href="/contact" data-ev="contact">Contact support</a>')
    parts.append("</nav>")
    return "\n".join(parts)




def article_page(g, meta, body_html, renderer, inv, order, header, footer, by_slug):
    slug = g["slug"]
    ch = g["chapter"]
    page = f"guide-{slug}"
    url = f"{SITE}/guide/{slug}"
    crumbs = [("Music Folder", f"{SITE}/"), ("User Guide", f"{SITE}/guide"),
              (ch["title"], f"{SITE}/guide#{ch['slug']}"), (g["title"], url)]
    out = [head(meta["seo_title"], meta["description"], url, meta["seo_title"],
                meta["description"], breadcrumb_ld(crumbs))]
    out.append(page_header(header, page))
    out.append('<main id="main">')
    out.append('<div class="wrap guide-layout">')
    out.append(f'<aside class="guide-aside">{search_box("guideSearchSide", "Search the guide", compact=True)}{sidebar(inv, slug)}</aside>')
    out.append('<article class="guide-article">')
    out.append(f'''<nav class="crumbs" aria-label="Breadcrumb"><ol>
  <li><a href="/guide">User Guide</a></li>
  <li><a href="/guide#{ch["slug"]}">{html.escape(ch["title"])}</a></li>
  <li aria-current="page">{html.escape(g["title"])}</li>
</ol></nav>''')
    # phone: the chapter's guides, under a disclosure
    here = ' aria-current="page"'
    out.append(f'<details class="guide-topics-mobile"><summary>{html.escape(ch["title"])}: all guides</summary><ul>'
               + "".join(f'<li><a href="/guide/{x["slug"]}"{here if x["slug"] == slug else ""}>{html.escape(x["title"])}</a></li>' for x in ch["guides"])
               + '<li><a href="/guide">All chapters</a></li></ul></details>')
    out.append(f'<h1 class="guide-title">{html.escape(g["title"])}</h1>')
    av = meta.get("availability") or []
    if av:
        # Plain-text requirements under the title (Premium, device, OS, version): no badges or colour
        out.append('<div class="availability" role="note" aria-label="Requirements">' + "".join(
            f'<p data-kind="{html.escape(a["kind"])}">{renderer.inline(a["text"])}</p>' for a in av) + "</div>")
    h2s = [h for h in renderer.headings if h[0] == 2]
    if len(h2s) >= 3:
        cols = " on-page-cols" if len(h2s) >= 6 else ""
        out.append(f'<nav class="on-page{cols}" aria-label="On this page"><details open data-on-page>'
                   '<summary class="on-page-title">On this page</summary><ul>'
                   + "".join(f'<li><a href="#{hid}">{renderer.inline(t)}</a></li>' for _, hid, t in h2s)
                   + "</ul></details></nav>")
    out.append(f'<div class="guide-body">\n{body_html}\n</div>')
    related = [by_slug[r] for r in meta.get("related") or [] if r in by_slug]
    fl = meta.get("feature_link")
    if related or fl:
        out.append('<section class="related" aria-labelledby="related-title" data-read-marker><h2 id="related-title">Related</h2><ul>')
        for r in related:
            out.append(f'<li><a href="/guide/{r["slug"]}"><span class="rel-ch">{html.escape(r["chapter"]["title"])}</span>{html.escape(r["title"])}</a></li>')
        out.append("</ul>")
        if fl:
            out.append(f'<p class="feature-link">See what else this can do on <a href="{html.escape(fl["href"])}" data-ev="nav">{html.escape(fl["text"])}</a>.</p>')
        out.append("</section>")
    idx = next(i for i, x in enumerate(order) if x["slug"] == slug)
    prev_g = order[idx - 1] if idx > 0 else None
    next_g = order[idx + 1] if idx + 1 < len(order) else None
    out.append('<nav class="pager" aria-label="Previous and next guide">')
    out.append(f'<a class="pager-prev" href="/guide/{prev_g["slug"]}" rel="prev"><span>Previous</span>{html.escape(prev_g["title"])}</a>' if prev_g else "<span></span>")
    out.append(f'<a class="pager-next" href="/guide/{next_g["slug"]}" rel="next"><span>Next</span>{html.escape(next_g["title"])}</a>' if next_g else "<span></span>")
    out.append("</nav>")
    out.append('''<div class="guide-help">
  <div><h2>Still need help?</h2><p>Tell us what you were trying to do and what happened. Every message is read by the people who make Music Folder.</p></div>
  <a class="btn btn-primary" href="/contact" data-ev="contact">Contact us</a>
</div>''')
    out.append("</article></div>")
    out.append(closing(page, footer))
    return "\n".join(out)


def whats_new_page(inv, header, footer, problems):
    src = TOOLS / "whats-new.md"
    if not src.exists():
        problems.append("tools/guide/whats-new.md is missing")
        return None
    meta, body = parse_source(src)
    slugs = {g["slug"] for ch in inv["chapters"] for g in ch["guides"]}
    r = Renderer("whats-new", meta, load_icons(), slugs, problems)
    body_html = r.render(body)
    url = f"{SITE}/guide/whats-new"
    crumbs = [("Music Folder", f"{SITE}/"), ("User Guide", f"{SITE}/guide"), ("What's New", url)]
    out = [head(meta["seo_title"], meta["description"], url, "What's New in Music Folder", meta["description"],
                breadcrumb_ld(crumbs))]
    out.append(page_header(header, "guide-whats-new"))
    out.append('<main id="main"><div class="wrap guide-layout">')
    out.append(f'<aside class="guide-aside">{search_box("guideSearchSide", "Search the guide", compact=True)}{sidebar(inv, "whats-new")}</aside>')
    out.append('<article class="guide-article">')
    out.append('<nav class="crumbs" aria-label="Breadcrumb"><ol><li><a href="/guide">User Guide</a></li><li aria-current="page">What\'s New</li></ol></nav>')
    out.append(f'<h1 class="guide-title">{html.escape(meta["h1"])}</h1>')
    out.append(f'<div class="guide-body whats-new">\n{body_html}\n</div>')
    out.append('''<div class="guide-help">
  <div><h2>Still need help?</h2><p>Tell us what you were trying to do and what happened. Every message is read by the people who make Music Folder.</p></div>
  <a class="btn btn-primary" href="/contact" data-ev="contact">Contact us</a>
</div>''')
    out.append("</article></div>")
    out.append(closing("guide-whats-new", footer))
    return "\n".join(out)


COMMON_TASKS = ["import-music", "add-sections-to-a-book", "create-and-edit-a-set-list", "turn-pages-hands-free",
                "mark-up-music-with-apple-pencil", "transpose-capo-and-numbers", "share-a-folder-or-set-list",
                "music-isnt-syncing"]


def hub_page(inv, by_slug, header, footer):
    url = f"{SITE}/guide"
    crumbs = [("Music Folder", f"{SITE}/"), ("User Guide", url)]
    desc = ("Step-by-step help for Music Folder on iPhone, iPad and Mac: importing sheet music, sections, "
            "set lists, page turning, annotation, chord charts, sharing and more.")
    out = [head("Music Folder User Guide: Step-by-Step Help", desc, url, "Music Folder User Guide",
                "Step-by-step help for every part of Music Folder.", breadcrumb_ld(crumbs))]
    out.append(page_header(header, "guide"))
    out.append('<main id="main">')
    out.append(f'''<section class="guide-hero">
  <div class="wrap">
    <h1 class="display">Music Folder User <em>Guide</em></h1>
    <p class="lede">Step-by-step help for every part of the app, on iPhone, iPad and Mac. Looking for a quick answer about your account or a device? Try the <a href="/support">FAQ</a>.</p>
    {search_box("guideSearch", "Search the guide, e.g. sections, pedal, transpose")}
  </div>
</section>''')
    out.append('<section class="guide-common"><div class="wrap"><h2 class="guide-h2">Common tasks</h2><ul class="task-list">'
               + "".join(f'<li><a href="/guide/{s}">{html.escape(by_slug[s]["title"])}</a></li>' for s in COMMON_TASKS if s in by_slug)
               + "</ul></div></section>")
    out.append('<section class="guide-chapters"><div class="wrap"><h2 class="guide-h2">All topics</h2><div class="chapter-grid">')
    for i, ch in enumerate(inv["chapters"], 1):
        out.append(f'<section class="chapter-card" id="{ch["slug"]}" aria-labelledby="{ch["slug"]}-t">'
                   f'<p class="ch-num">{i:02d}</p><h3 id="{ch["slug"]}-t">{html.escape(ch["title"])}</h3>'
                   f'<p class="ch-sum">{html.escape(ch["summary"])}</p><ul>'
                   + "".join(f'<li><a href="/guide/{g["slug"]}">{html.escape(g["title"])}</a></li>' for g in ch["guides"])
                   + "</ul></section>")
    out.append('</div></div></section>')
    out.append('''<section class="guide-more"><div class="wrap guide-more-grid">
  <a class="more-card" href="/guide/whats-new"><h2>What's New</h2><p>What changed in each version of Music Folder.</p></a>
  <a class="more-card" href="/support"><h2>FAQ</h2><p>Quick answers about devices, pricing, sync and privacy.</p></a>
  <a class="more-card" href="/contact" data-ev="contact"><h2>Contact us</h2><p>Report a problem or ask a question. Every message is read by the people who make Music Folder.</p></a>
</div></section>''')
    out.append(closing("guide", footer))
    return "\n".join(out)


# ---------------------------------------------------------------------------------------------
# Generated lines in shared files
# ---------------------------------------------------------------------------------------------

def replace_block(path: Path, start: str, end: str, content: str, anchor_before: str | None = None):
    text = path.read_text(encoding="utf-8")
    if start in text:
        text = re.sub(re.escape(start) + r".*?" + re.escape(end), start + "\n" + content + end, text, flags=re.S)
    else:
        if anchor_before is None or anchor_before not in text:
            raise SystemExit(f"{path.name}: can't place the generated block")
        text = text.replace(anchor_before, start + "\n" + content + end + "\n" + anchor_before, 1)
    path.write_text(text, encoding="utf-8")


def main() -> int:
    inv, order = load_inventory()
    by_slug = {g["slug"]: g for g in order}
    slugs = set(by_slug)
    icons = load_icons()
    header, footer = chrome()
    problems: list[str] = []
    OUT_DIR.mkdir(exist_ok=True)
    index = []
    seen_titles, seen_desc = {}, {}
    built = 0
    used_icons: set[str] = set()
    for g in order:
        src = SRC / f"{g['slug']}.md"
        if not src.exists():
            problems.append(f"{g['slug']}: guide-src/{g['slug']}.md is missing")
            continue
        meta, body = parse_source(src)
        for key in ("slug", "h1", "seo_title", "description", "related"):
            if key not in meta:
                problems.append(f"{g['slug']}: front matter has no {key}")
        if meta.get("slug") != g["slug"]:
            problems.append(f"{g['slug']}: front matter slug is {meta.get('slug')}")
        if meta.get("h1") != g["title"]:
            problems.append(f"{g['slug']}: h1 {meta.get('h1')!r} differs from the inventory title {g['title']!r}")
        st, de = meta.get("seo_title", ""), meta.get("description", "")
        # "<Task> | Music Folder", or a title that already names Music Folder naturally (no suffix then)
        if "Music Folder" not in st or st.count("Music Folder") > 1 or "User Guide" in st or len(st) > 65:
            problems.append(f"{g['slug']}: seo_title must name Music Folder once (suffix ' | Music Folder' unless it's"
                            f" already in the title), no 'User Guide', ≤ 65 chars ({len(st)})")
        if not 100 <= len(de) <= 165:
            problems.append(f"{g['slug']}: description is {len(de)} chars (aim for 120–158)")
        if st in seen_titles:
            problems.append(f"{g['slug']}: seo_title duplicates {seen_titles[st]}")
        if de in seen_desc:
            problems.append(f"{g['slug']}: description duplicates {seen_desc[de]}")
        seen_titles[st], seen_desc[de] = g["slug"], g["slug"]
        for r in meta.get("related") or []:
            if r not in slugs:
                problems.append(f"{g['slug']}: related slug {r} doesn't exist")
            if r == g["slug"]:
                problems.append(f"{g['slug']}: relates to itself")
        if "—" in body or "—" in json.dumps(meta, ensure_ascii=False):
            problems.append(f"{g['slug']}: contains an em dash")
        r = Renderer(g["slug"], meta, icons, slugs, problems)
        body_html = r.render(body)
        used_icons |= r.used_icons
        page = article_page(g, meta, body_html, r, inv, order, header, footer, by_slug)
        (OUT_DIR / f"{g['slug']}.html").write_text(page, encoding="utf-8")
        built += 1
        text = plain(body_html)
        index.append({"s": g["slug"], "t": g["title"], "c": g["chapter"]["title"],
                      "k": " ".join(meta.get("searches") or []),
                      "h": " · ".join(plain(r.inline(h[2])) for h in r.headings),
                      "d": meta["description"], "b": text[:1600]})
    wn = whats_new_page(inv, header, footer, problems)
    if wn:
        (OUT_DIR / "whats-new.html").write_text(wn, encoding="utf-8")
        index.append({"s": "whats-new", "t": "What's New", "c": "User Guide", "k": "release notes update version changes",
                      "h": "", "d": "What changed in each version of Music Folder.", "b": ""})
    (ROOT / "guide.html").write_text(hub_page(inv, by_slug, header, footer), encoding="utf-8")
    (ROOT / "assets" / "guide-search.json").write_text(
        json.dumps({"syn": SYNONYMS, "guides": index}, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")

    # sitemap: the hub, What's New and every guide
    locs = [f"{SITE}/guide", f"{SITE}/guide/whats-new"] + [f"{SITE}/guide/{g['slug']}" for g in order if (OUT_DIR / f"{g['slug']}.html").exists()]
    replace_block(ROOT / "sitemap.xml", "  <!-- guide:start -->", "  <!-- guide:end -->",
                  "".join(f"  <url><loc>{u}</loc></url>\n" for u in locs), anchor_before="</urlset>")
    # App Store placements for every guide page (worker/tap.js BUTTONS)
    pages = ["guide", "guide-whats-new"] + [f"guide-{g['slug']}" for g in order]
    lines = "".join(f'  "{p}": ["nav", "menu", "final"],\n' for p in pages)
    replace_block(ROOT / "worker" / "tap.js", "  // guide:start (generated by tools/guide/build.py)", "  // guide:end",
                  lines, anchor_before="};\n\n// placement → [page, position]")
    (TOOLS / "icons-used.txt").write_text("\n".join(sorted(used_icons)) + "\n", encoding="utf-8")

    for p in problems:
        print("✗", p)
    print(f"built {built}/{len(order)} guides + hub + What's New" + (" (draft)" if DRAFT else ""))
    return 1 if problems and not DRAFT else 0


if __name__ == "__main__":
    sys.exit(main())
