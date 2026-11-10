"""Helpers for rewriting parts of an existing page while keeping its layout:
rows (the alternating text + screenshot blocks), the FAQ (visible and FAQPage JSON-LD
together, so they never drift apart), the "More from Music Folder" cards, and plain
text replacements that must match exactly once."""
from __future__ import annotations

import html
import json
import re

CHECK = ('<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.9" '
         'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 8.5l3 3 7-7"/></svg>')
SIZES = {"tablet": (900, 1200), "landscape": (1306, 980), "phone": (700, 1522), "tablet-tall": (900, 1306)}
CLASSES = {"tablet": "device tablet fit", "landscape": "device tablet landscape fit",
           "phone": "device phone fit", "tablet-tall": "device tablet fit"}


def device(src: str, alt: str, kind: str = "tablet") -> str:
    w, h = SIZES[kind]
    return (f'<div class="{CLASSES[kind]}"><div class="screen shot"><img src="/assets/{src}" '
            f'alt="{html.escape(alt, quote=True)}" width="{w}" height="{h}" loading="lazy"></div></div>')


def row(h2: str, p: str, points: list[str], visual: str, flip: bool, more: str = "") -> str:
    pts = "".join(f"<li>{CHECK}<span>{x}</span></li>" for x in points)
    extra = f'<p class="rf-more">{more}</p>' if more else ""
    return (f'<div class="row-feature{" flip" if flip else ""}">\n'
            f'      <div class="rf-text"><h2 class="heading-sm">{h2}</h2><p>{p}</p><ul class="rf-points">{pts}</ul>{extra}</div>\n'
            f'      <div class="rf-visual">{visual}</div>\n    </div>')


def set_rows(t: str, rows: list[str]) -> str:
    new = '<div class="wrap rows">\n    ' + "".join(rows) + "\n  </div>"
    t2, n = re.subn(r'<div class="wrap rows">.*?\n  </div>(?=\n</section>)', lambda m: new, t, count=1, flags=re.S)
    assert n == 1, "rows block not found"
    return t2


def set_faq(t: str, faq: list[tuple[str, str]]) -> str:
    vis = "\n".join(f'<details><summary>{html.escape(q)}<span class="plus" aria-hidden="true"></span></summary>'
                    f'<div class="answer"><p>{a}</p></div></details>' for q, a in faq)
    t, n = re.subn(r'(<div class="faq">).*?(</div>\n  </div>\n</section>)', lambda m: m.group(1) + vis + m.group(2),
                   t, count=1, flags=re.S)
    assert n == 1, "faq block not found"
    for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', t, re.S):
        d = json.loads(b)
        if d.get("@type") == "FAQPage":
            d["mainEntity"] = [{"@type": "Question", "name": q, "acceptedAnswer": {
                "@type": "Answer", "text": html.unescape(re.sub(r"<[^>]+>", "", a))}} for q, a in faq]
            t = t.replace(b, "\n" + json.dumps(d, ensure_ascii=False, indent=2) + "\n", 1)
    return t


def set_more(t: str, cards: list[tuple[str, str, str]]) -> str:
    inner = "".join(f'<a class="more-card" href="{h}"><h3>{n}</h3><p>{p}</p><span class="more-link" aria-hidden="true">Explore</span></a>'
                    for h, n, p in cards)
    t, n = re.subn(r'(<div class="more-grid four">).*?(</div>\n  </div>\n</section>)', lambda m: m.group(1) + inner + m.group(2),
                   t, count=1, flags=re.S)
    assert n == 1, "more block not found"
    return t


def replace_once(t: str, old: str, new: str) -> str:
    assert t.count(old) == 1, (t.count(old), old[:60])
    return t.replace(old, new)


def set_description(t: str, desc: str) -> str:
    """The meta description and the WebPage JSON-LD description, kept identical."""
    t, n = re.subn(r'<meta name="description" content="[^"]*">',
                   lambda m: f'<meta name="description" content="{html.escape(desc, quote=True)}">', t, count=1)
    assert n == 1
    for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', t, re.S):
        d = json.loads(b)
        if d.get("@type") == "WebPage":
            d["description"] = desc
            t = t.replace(b, "\n" + json.dumps(d, ensure_ascii=False, indent=2) + "\n", 1)
    return t
