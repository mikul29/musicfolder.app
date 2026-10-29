/* Smooth, eased scrolling for links to sections on the same page.
   The native smooth scroll is linear and abrupt over long distances (and the
   hero's scroll animation is 3 screens tall), so in-page links ease instead. */
(() => {
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)');
  const ease = t => (t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2);
  const headerH = () => (document.querySelector('.site-header') || {}).offsetHeight || 64;

  // where a target should land: story steps are centred (that's when the
  // pinned device shows their screen); everything else sits below the header
  const targetY = el => {
    // the fixed header (logo link, #top) means the very top of the page
    if (el.id === 'top' || getComputedStyle(el).position === 'fixed') return 0;
    const r = el.getBoundingClientRect();
    const top = r.top + window.scrollY;
    if (el.classList.contains('step')) return top + r.height / 2 - window.innerHeight / 2;
    return top - headerH() - 16;
  };

  let run = 0;
  const scrollToY = y => {
    const max = document.documentElement.scrollHeight - window.innerHeight;
    y = Math.max(0, Math.min(y, max));
    const start = window.scrollY, dist = y - start;
    if (reduce.matches || Math.abs(dist) < 2) { window.scrollTo(0, y); return; }
    const duration = Math.min(1200, Math.max(550, Math.abs(dist) * 0.22));
    const id = ++run, t0 = performance.now();
    // the user taking over (wheel, touch, keys) cancels the animation
    const cancel = () => { run++; detach(); };
    const events = ['wheel', 'touchstart', 'keydown'];
    const detach = () => events.forEach(ev => window.removeEventListener(ev, cancel));
    events.forEach(ev => window.addEventListener(ev, cancel, { passive: true }));
    const frame = now => {
      if (id !== run) return;
      const t = Math.min(1, (now - t0) / duration);
      window.scrollTo(0, start + dist * ease(t));
      if (t < 1) requestAnimationFrame(frame); else detach();
    };
    requestAnimationFrame(frame);
  };

  document.addEventListener('click', e => {
    const a = e.target.closest && e.target.closest('a[href*="#"]');
    if (!a || e.metaKey || e.ctrlKey || e.shiftKey) return;
    const url = new URL(a.getAttribute('href'), window.location.href);
    if (url.origin !== location.origin || url.pathname !== location.pathname || url.hash.length < 2) return;
    const el = document.getElementById(decodeURIComponent(url.hash.slice(1)));
    if (!el) return;
    e.preventDefault();
    const menu = a.closest('details');
    if (menu) menu.removeAttribute('open');
    history.pushState(null, '', url.hash);
    scrollToY(targetY(el));
  });

  /* ---------- Footer wordmark spans exactly the content width ---------- */
  const mark = document.querySelector('.footer-mark');
  if (mark) {
    const fit = () => {
      const box = mark.parentElement;
      const cs = getComputedStyle(box);
      const avail = box.clientWidth - parseFloat(cs.paddingLeft) - parseFloat(cs.paddingRight);
      mark.style.fontSize = '100px';
      // visible width = text width minus the trailing tracking (0.2em)
      const w = mark.scrollWidth - 20;
      if (w > 0) mark.style.fontSize = (100 * avail / w).toFixed(2) + 'px';
    };
    fit();
    window.addEventListener('resize', fit);
    if (document.fonts) document.fonts.ready.then(fit);
  }
})();

/* ---------- Primary nav: disclosure menus (Features, Who it's for) ---------- */
(() => {
  const hover = window.matchMedia('(hover: hover) and (pointer: fine)');
  const groups = [...document.querySelectorAll('.nav-group')];
  const closeOthers = keep => groups.forEach(g => { if (g !== keep && g._setOpen) g._setOpen(false); });
  groups.forEach(group => {
    const trigger = group.querySelector('.nav-trigger');
    const links = () => [...group.querySelectorAll('.nav-pop a')];
    let closeTimer = 0;
    const setOpen = open => {
      clearTimeout(closeTimer);
      if (open) closeOthers(group);
      group.classList.toggle('is-open', open);
      trigger.setAttribute('aria-expanded', String(open));
    };
    group._setOpen = setOpen;
    // a mouse click on a menu that hovering already opened keeps it open;
    // Enter / Space (a click with no pointer detail) toggles it
    trigger.addEventListener('click', e => {
      const open = trigger.getAttribute('aria-expanded') === 'true';
      setOpen(e.detail > 0 && hover.matches ? true : !open);
    });
    trigger.addEventListener('keydown', e => {
      if (e.key === 'ArrowDown') { e.preventDefault(); setOpen(true); links()[0].focus(); }
    });
    group.addEventListener('keydown', e => {
      if (e.key === 'Escape' && group.classList.contains('is-open')) { setOpen(false); trigger.focus(); }
      if ((e.key === 'ArrowDown' || e.key === 'ArrowUp') && e.target !== trigger) {
        const l = links(), i = l.indexOf(document.activeElement);
        if (i < 0) return;
        e.preventDefault();
        l[(i + (e.key === 'ArrowDown' ? 1 : l.length - 1)) % l.length].focus();
      }
    });
    // leaving the menu with Tab, or clicking anywhere else, closes it
    group.addEventListener('focusout', e => { if (!group.contains(e.relatedTarget)) setOpen(false); });
    document.addEventListener('click', e => { if (!group.contains(e.target)) setOpen(false); });
    // with a mouse, hovering opens it (a short grace period before closing)
    group.addEventListener('mouseenter', () => { if (hover.matches) setOpen(true); });
    group.addEventListener('mouseleave', () => {
      if (hover.matches) { clearTimeout(closeTimer); closeTimer = setTimeout(() => setOpen(false), 140); }
    });
  });
})();

/* ---------- Where visits come from (cookieless; README "Measurement") ----------
   Nothing is stored on a visitor's device. This page reads its own address and the address of
   the page before it (the browser's referrer) and:
   - on a visit's first page, sends one count to the site's own /hit: the page, the referring
     site's host name and any utm_source / utm_medium / utm_campaign in the address;
   - adds the same source to every App Store button (/get), so a tap carries it. One page later
     the campaign tags are still known (from the previous page's address); further in, the source
     is "unknown".
   The owner's own devices (opened /me once) are skipped: no landing count, taps marked o=1. */
(() => {
  let owner = false;
  try { owner = localStorage.getItem('mf-owner') === '1'; } catch (e) { /* storage blocked: not the owner's flag */ }
  let ref = null;
  try { ref = document.referrer ? new URL(document.referrer) : null; } catch (e) { ref = null; }
  const inside = !!ref && ref.origin === location.origin;
  const tags = u => ['utm_source', 'utm_medium', 'utm_campaign'].map(k => (u.searchParams.get(k) || '').slice(0, 60));
  const [us, um, uc] = tags(new URL(location.href));
  const source = new URLSearchParams();
  const put = (k, v) => { if (v) source.set(k, v); };
  if (!inside) {
    // the first page of a visit: its own tags and the site it came from
    put('us', us); put('um', um); put('uc', uc); put('r', ref ? ref.hostname : '');
    source.set('h', 'landing');
  } else {
    const [pus, pum, puc] = tags(ref);
    if (pus || pum || puc) { put('us', pus); put('um', pum); put('uc', puc); source.set('h', 'next'); }
    else source.set('h', 'unknown');
  }
  if (owner) source.set('o', '1');

  document.querySelectorAll('a[href^="/get?"]').forEach(a => {
    const url = new URL(a.getAttribute('href'), location.origin);
    source.forEach((v, k) => url.searchParams.set(k, v));
    a.setAttribute('href', url.pathname + url.search);
  });

  if (!inside && !owner) {
    const hit = new URLSearchParams(source);
    hit.set('p', location.pathname);
    const target = '/hit?' + hit.toString();
    if (!(navigator.sendBeacon && navigator.sendBeacon(target))) {
      fetch(target, { method: 'POST', keepalive: true, credentials: 'omit' }).catch(() => {});
    }
  }
})();
