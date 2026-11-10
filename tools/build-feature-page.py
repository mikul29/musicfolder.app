#!/usr/bin/env python3
"""Builds a feature page from a short spec, using features/set-lists.html as the template,
so header, nav, footer, structured data and App Store buttons match the rest of the site.

    python3 tools/build-feature-page.py tools/pages/<slug>.py

The spec module defines PAGE (see tools/pages/*.py). The page is written to features/<slug>.html.
App Store buttons use /get?from=features-<slug>-{nav,menu,hero,final}; add them to worker/tap.js.
"""
from __future__ import annotations

import html
import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "features/set-lists.html"
CHECK = ('<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.9" '
         'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 8.5l3 3 7-7"/></svg>')
BADGE = ('<a class="badge-link" href="/get?from={src}"><picture><img src="https://toolbox.marketingtools.apple.com/'
         'api/badges/download-on-the-app-store/black/en-us?size=250x83" alt="Download on the App Store" width="144" '
         'height="48"{lazy}></picture></a>')
SIZES = {"tablet": (900, 1200), "landscape": (1306, 980), "phone": (700, 1522)}


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def text(s: str) -> str:
    """Plain text of a fragment that may hold <em>/<a> markup."""
    return html.unescape(re.sub(r"<[^>]+>", "", s))


def device(img: dict, lazy: bool = True) -> str:
    kind = img.get("device", "tablet")
    w, h = SIZES[kind]
    cls = {"tablet": "device tablet fit", "landscape": "device tablet landscape fit", "phone": "device phone fit"}[kind]
    la = ' loading="lazy"' if lazy else ""
    return (f'<div class="{cls}"><div class="screen shot"><img src="/assets/{img["src"]}" alt="{esc(img["alt"])}" '
            f'width="{w}" height="{h}"{la}></div></div>')


def build(spec: dict) -> str:
    slug = spec["slug"]
    url = f"https://musicfolder.app/features/{slug}"
    page = f"features-{slug}"
    t = TEMPLATE.read_text()

    # ---- head ----
    t = re.sub(r"<title>.*?</title>", f"<title>{esc(spec['title'])}</title>", t, count=1)
    t = t.replace('href="https://musicfolder.app/features/set-lists"', f'href="{url}"')
    t = t.replace('content="https://musicfolder.app/features/set-lists"', f'content="{url}"')
    t = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{esc(spec["description"])}">', t, count=1)
    for prop in ("og:title", "twitter:title"):
        attr = "property" if prop.startswith("og") else "name"
        t = re.sub(rf'<meta {attr}="{prop}" content="[^"]*">', f'<meta {attr}="{prop}" content="{esc(spec["og_title"])}">', t, count=1)
    for prop in ("og:description", "twitter:description"):
        attr = "property" if prop.startswith("og") else "name"
        t = re.sub(rf'<meta {attr}="{prop}" content="[^"]*">', f'<meta {attr}="{prop}" content="{esc(spec["og_description"])}">', t, count=1)

    # ---- JSON-LD ----
    blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', t, re.S)
    out = []
    for b in blocks:
        d = json.loads(b)
        if d["@type"] == "WebPage":
            d["url"], d["name"], d["description"] = url, spec["title"], spec["description"]
        elif d["@type"] == "BreadcrumbList":
            d["itemListElement"][1].update({"name": spec["crumb"], "item": url})
        elif d["@type"] == "FAQPage":
            d["mainEntity"] = [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": text(a)}}
                               for q, a in spec["faq"]]
        out.append((b, "\n" + json.dumps(d, ensure_ascii=False, indent=2) + "\n"))
    for old, new in out:
        t = t.replace(old, new, 1)

    # ---- nav: current page + App Store buttons ----
    t = t.replace(' aria-current="page"', "")
    t = t.replace(f'<a href="/features/{slug}"><b>', f'<a href="/features/{slug}" aria-current="page"><b>')
    t = t.replace(f'<a href="/features/{slug}">{spec["menu_name"]}</a>',
                  f'<a href="/features/{slug}" aria-current="page">{spec["menu_name"]}</a>', 1)
    t = t.replace("/get?from=features-set-lists-", f"/get?from={page}-")

    # ---- main ----
    rows = []
    for i, r in enumerate(spec["rows"]):
        points = "".join(f"<li>{CHECK}<span>{p}</span></li>" for p in r["points"])
        flip = " flip" if i % 2 else ""
        visual = r.get("visual_html") or device(r["img"])
        rcls = (" " + r["row_class"]) if r.get("row_class") else ""
        vcls = (" " + r["visual_class"]) if r.get("visual_class") else ""
        more_link = f'<p class="rf-more">{r["more"]}</p>' if r.get("more") else ""
        rows.append(f'<div class="row-feature{flip}{rcls}">\n      <div class="rf-text"><h2 class="heading-sm">{r["h2"]}</h2>'
                    f'<p>{r["p"]}</p><ul class="rf-points">{points}</ul>{more_link}</div>\n'
                    f'      <div class="rf-visual{vcls}">{visual}</div>\n    </div>')
    how = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in spec["how"])
    faq = "\n".join(f'<details><summary>{esc(q)}<span class="plus" aria-hidden="true"></span></summary>'
                    f'<div class="answer"><p>{a}</p></div></details>' for q, a in spec["faq"])
    more = "".join(f'<a class="more-card" href="{h}"><h3>{n}</h3><p>{p}</p><span class="more-link" aria-hidden="true">Explore</span></a>'
                   for h, n, p in spec["more"])
    extra = spec.get("extra_section", "")
    if spec.get("band_cta"):  # a mid-page call to action, styled like Home's band (position "band")
        b = spec["band_cta"]
        extra += f"""
<section class="section band-cta mid" aria-labelledby="bandCtaTitle">
  <div class="wrap">
    <div class="bc-panel">
      <div class="bc-copy"><h2 class="heading" id="bandCtaTitle">{b['h2']}</h2><p class="bc-sub">{b['p']}</p></div>
      <div class="bc-actions">
        <div class="cta-row">{BADGE.format(src=page + '-band', lazy=' loading="lazy"')}</div>
        <a class="bc-link" href="{b['link_href']}">{b['link_text']} <span aria-hidden="true">→</span></a>
      </div>
    </div>
  </div>
</section>
"""
    main = f"""<main>

<section class="lp-hero">
  <div class="wrap lp-hero-grid">
    <div>
      <ol class="crumb" aria-label="Breadcrumb"><li><a href="/">Music Folder</a></li><li aria-current="page">{spec['crumb']}</li></ol>
      <h1 class="display">{spec['h1']}</h1>
      <p class="lede">{spec['lede']}</p>
      <div class="cta-row">{BADGE.format(src=page + '-hero', lazy='')}</div>
    </div>
    <div class="lp-visual{(' ' + spec['hero_class']) if spec.get('hero_class') else ''}">{device(spec['hero_img'], lazy=False)}</div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="section-head"><h2 class="heading">{spec['how_heading']}</h2></div>
    <ol class="how">{how}</ol>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap rows">
    {''.join(rows)}
  </div>
</section>
{extra}
<section class="section" style="padding-top:0">
  <div class="wrap lp-faq-grid">
    <h2 class="heading-sm">{spec['faq_heading']}</h2>
    <div class="faq">{faq}</div>
  </div>
</section>

<section class="section more">
  <div class="wrap">
    <div class="section-head"><h2 class="heading-sm">More from Music Folder.</h2></div>
    <div class="more-grid four">{more}</div>
  </div>
</section>

<!-- ============ FINAL CTA ============ -->
<section class="section final">
  <div class="wrap">
    <h2 class="heading">A better <em>home</em> for your sheet music.</h2>
    <p>Made by musicians, for musicians.</p>
    <div class="cta-row">
      {BADGE.format(src=page + '-final', lazy=' loading="lazy"')}
    </div>
  </div>
</section>

</main>"""
    t = re.sub(r"<main>.*?</main>", lambda m: main, t, count=1, flags=re.S)
    return t


if __name__ == "__main__":
    path = Path(sys.argv[1])
    mod_spec = importlib.util.spec_from_file_location("page", path)
    mod = importlib.util.module_from_spec(mod_spec)
    mod_spec.loader.exec_module(mod)
    spec = mod.PAGE
    out = ROOT / f"features/{spec['slug']}.html"
    out.write_text(build(spec))
    print("wrote", out.relative_to(ROOT))
