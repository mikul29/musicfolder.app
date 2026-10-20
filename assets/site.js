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
