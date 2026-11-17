/* Music Folder User Guide: search, clips and the guide's own counters.
   Pages work without this script (every guide is a plain link); it only adds search-as-you-type,
   plays demonstration clips when motion is welcome, and reports a few anonymous guide events.

   Counters (README "Measurement"): one beacon to the site's own /ev per event, cookieless, no
   identifiers, skipped on the owner's devices (mf-owner) and for crawlers (worker):
     search   a query someone settled on (typed and paused, or pressed Enter) + how many results
     noresult the same, when nothing matched
     open     a search result that was opened
     nav      a guide link to a feature, audience or pricing page
     contact  a guide link to Contact us
     read     the reader reached the end of the article (the Related section)
   Queries are lower-cased and cut to 60 characters before they leave the page. */
(() => {
  'use strict';
  let owner = false;
  try { owner = localStorage.getItem('mf-owner') === '1'; } catch (e) { /* storage blocked */ }
  const page = location.pathname;
  const sent = new Set();
  const ev = (type, value, n) => {
    if (owner) return;
    const key = type + '|' + (value || '');
    if (sent.has(key)) return;
    sent.add(key);
    const q = new URLSearchParams({ t: type, p: page });
    if (value) q.set('v', String(value).toLowerCase().replace(/\s+/g, ' ').trim().slice(0, 60));
    if (n !== undefined) q.set('n', String(n));
    const target = '/ev?' + q.toString();
    if (!(navigator.sendBeacon && navigator.sendBeacon(target))) {
      fetch(target, { method: 'POST', keepalive: true, credentials: 'omit' }).catch(() => {});
    }
  };

  /* ---------- links that leave the guide ---------- */
  document.addEventListener('click', e => {
    const a = e.target.closest && e.target.closest('a[data-ev]');
    if (a) ev(a.dataset.ev, a.getAttribute('href'));
  });
  const marker = document.querySelector('[data-read-marker]');
  if (marker && 'IntersectionObserver' in window) {
    const io = new IntersectionObserver(entries => {
      if (entries.some(x => x.isIntersecting)) { ev('read'); io.disconnect(); }
    });
    io.observe(marker);
  }

  /* ---------- clips: play only when motion is welcome and the clip is on screen ---------- */
  const still = window.matchMedia('(prefers-reduced-motion: reduce)');
  document.querySelectorAll('video[data-clip]').forEach(v => {
    const btn = v.parentElement.querySelector('.clip-toggle');
    const label = () => { if (btn) btn.textContent = v.paused ? 'Play' : 'Pause'; };
    v.addEventListener('play', label); v.addEventListener('pause', label);
    if (btn) {
      btn.hidden = false;
      btn.setAttribute('aria-label', (v.paused ? 'Play' : 'Pause') + ' demonstration: ' + (v.getAttribute('aria-label') || ''));
      btn.addEventListener('click', () => { if (v.paused) { v.preload = 'auto'; v.play().catch(() => {}); } else v.pause(); label(); });
    }
    if (still.matches || !('IntersectionObserver' in window)) return;
    new IntersectionObserver(entries => entries.forEach(x => {
      if (x.isIntersecting) { v.preload = 'auto'; v.play().catch(() => {}); } else v.pause();
    }), { threshold: 0.5 }).observe(v);
  });

  /* ---------- search ---------- */
  const forms = [...document.querySelectorAll('[data-guide-search]')];
  if (!forms.length) return;
  let data = null, loading = null;
  const load = () => loading || (loading = fetch('/assets/guide-search.json').then(r => r.json()).then(d => {
    data = d;
    data.guides.forEach(g => {
      g._t = norm(g.t); g._k = norm(g.k); g._h = norm(g.h); g._d = norm(g.d); g._b = norm(g.b);
      g._words = new Set((g._t + ' ' + g._k + ' ' + g._h).split(' '));
    });
    return d;
  }).catch(() => null));
  const norm = t => (t || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '')
    .replace(/[’']/g, '').replace(/[^a-z0-9#+]+/g, ' ').trim();
  const STOP = new Set(['a', 'an', 'the', 'to', 'in', 'on', 'of', 'for', 'and', 'or', 'my', 'i', 'how', 'do', 'can',
    'is', 'it', 'with', 'from', 'what', 'why', 'does', 'into', 'at', 'be', 'me', 'you', 'your', 'when', 'where', 'get']);
  // one typo allowed in longer words
  const near = (a, b) => {
    if (Math.abs(a.length - b.length) > 1 || a.length < 5) return false;
    let i = 0, j = 0, edits = 0;
    while (i < a.length && j < b.length) {
      if (a[i] === b[j]) { i++; j++; continue; }
      if (++edits > 1) return false;
      if (a.length > b.length) i++; else if (b.length > a.length) j++; else { i++; j++; }
    }
    return edits + (a.length - i) + (b.length - j) <= 1;
  };
  const expand = q => {
    const n = norm(q);
    const terms = n.split(' ').filter(w => w && !STOP.has(w));
    const extra = [];
    Object.entries(data.syn).forEach(([k, vs]) => { if ((' ' + n + ' ').includes(' ' + k + ' ')) vs.forEach(v => extra.push(norm(v))); });
    return { terms, extra };
  };
  const score = (g, terms, extra) => {
    let s = 0, matched = 0;
    terms.forEach(w => {
      let hit = 0;
      if (g._t.includes(w)) hit = Math.max(hit, 12);
      if (g._k.includes(w)) hit = Math.max(hit, 8);
      if (g._h.includes(w)) hit = Math.max(hit, 5);
      if (g._d.includes(w)) hit = Math.max(hit, 3);
      if (!hit && g._b.includes(w)) hit = 1.5;
      if (!hit && w.length >= 5) { for (const x of g._words) if (near(w, x)) { hit = 4; break; } }
      if (hit) matched++;
      s += hit;
    });
    extra.forEach(p => {
      if (g._t.includes(p)) s += 6; else if (g._k.includes(p) || g._h.includes(p)) s += 3; else if (g._b.includes(p)) s += 1;
    });
    if (terms.length && matched < Math.ceil(terms.length / 2) && !extra.some(p => g._t.includes(p) || g._k.includes(p))) return 0;
    return s;
  };
  const search = q => {
    const { terms, extra } = expand(q);
    if (!terms.length && !extra.length) return [];
    return data.guides.map(g => ({ g, s: score(g, terms, extra) })).filter(x => x.s > 0)
      .sort((a, b) => b.s - a.s).slice(0, 8).map(x => x.g);
  };
  const esc = t => t.replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

  forms.forEach(form => {
    const input = form.querySelector('input');
    const box = form.querySelector('.guide-results');
    let active = -1, timer = null, lastLogged = '';
    const items = () => [...box.querySelectorAll('a[role="option"]')];
    const close = () => { box.hidden = true; input.setAttribute('aria-expanded', 'false'); active = -1; };
    const log = (q, n) => {
      const v = norm(q);
      if (v.length < 3 || v === lastLogged) return;
      lastLogged = v;
      ev(n ? 'search' : 'noresult', v, n);
    };
    const show = () => {
      const q = input.value.trim();
      if (!q) { close(); return; }
      if (!data) { load().then(d => d && show()); return; }
      const res = search(q);
      if (res.length) {
        box.innerHTML = res.map((g, i) => `<a role="option" id="${input.id}-o${i}" href="/guide/${g.s}" aria-selected="false">` +
          `<span class="r-c">${esc(g.c)}</span><span class="r-t">${esc(g.t)}</span><span class="r-d">${esc(g.d)}</span></a>`).join('');
      } else {
        box.innerHTML = `<p class="r-empty">No guides match “${esc(q)}”. Try other words, browse <a href="/guide#get-started">all topics</a>, or <a href="/contact" data-ev="contact">ask us directly</a>.</p>`;
      }
      box.hidden = false; input.setAttribute('aria-expanded', 'true'); active = -1;
      clearTimeout(timer);
      timer = setTimeout(() => log(q, res.length), 1500);
    };
    input.setAttribute('role', 'combobox');
    input.setAttribute('aria-expanded', 'false');
    input.addEventListener('focus', () => { load(); if (input.value.trim()) show(); });
    input.addEventListener('input', show);
    input.addEventListener('keydown', e => {
      const list = items();
      if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
        if (!list.length) return;
        e.preventDefault();
        active = (active + (e.key === 'ArrowDown' ? 1 : list.length - 1)) % list.length;
        list.forEach((a, i) => a.setAttribute('aria-selected', i === active ? 'true' : 'false'));
        input.setAttribute('aria-activedescendant', list[active].id);
        list[active].scrollIntoView({ block: 'nearest' });
      } else if (e.key === 'Escape') {
        if (!box.hidden) { e.preventDefault(); close(); } else input.value = '';
      } else if (e.key === 'Enter') {
        e.preventDefault();
        if (!data) return;
        const res = search(input.value);
        clearTimeout(timer); log(input.value, res.length);
        const target = active >= 0 ? list[active] : list[0];
        if (target) { ev('open', target.getAttribute('href')); location.href = target.getAttribute('href'); }
      }
    });
    box.addEventListener('click', e => {
      const a = e.target.closest('a[role="option"]');
      if (a) { clearTimeout(timer); log(input.value, items().length); ev('open', a.getAttribute('href')); }
    });
    form.addEventListener('submit', e => e.preventDefault());
    form.addEventListener('focusout', e => { if (!form.contains(e.relatedTarget)) setTimeout(close, 120); });
  });

  // /guide?q=… (from a sidebar search with JavaScript off, or a shared link): fill in and search
  const q = new URLSearchParams(location.search).get('q');
  const hub = document.getElementById('guideSearch');
  if (q && hub) { hub.value = q.slice(0, 80); hub.focus(); }
})();
