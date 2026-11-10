/* Face Gestures demo (Page Turner page).
   A faithful web port of the app's teaching loop (MyBandProject App/FaceGlyph.swift:
   FaceGlyphScript, FaceGlyphRenderer, FaceHoldRing, MiniScoreView): an ordered field of
   points on a sphere with capsule eyes and a smile, the hold ring, and a small score
   whose page turns over on its spine. Same geometry, timings and colours as the app.
   Runs only while on screen; Reduce Motion shows the app's four captioned stills. */
(() => {
  const root = document.querySelector('[data-face-demo]');
  if (!root) return;

  const INK = '42,42,45';          // FaceGlyphPalette.ink (light)  #2A2A2D
  const ACCENT = '224,113,47';     // AppAppearance.accent (Ember)  #E0712F
  const PAPER = '#FFFFFF', BACK1 = '#F4F2F0', BACK2 = '#E9E8E5';

  const KINDS = {
    headTurn: {
      detail: 'Turn your head right for the next page, left to go back.',
      next: 'Turn right and hold…', back: 'Now left, and hold…',
      label: 'A face turns right and holds for a moment, and the page turns.'
    },
    wink: {
      detail: 'Wink your right eye for the next page, your left to go back.',
      next: 'Wink your right eye and hold…', back: 'Now your left eye…',
      label: 'A face winks its right eye and holds for a moment, and the page turns.'
    },
    mouth: {
      detail: 'Pull your mouth to the right for the next page, to the left to go back.',
      next: 'Pull your mouth right and hold…', back: 'Now to the left…',
      label: 'A face pulls its mouth to the right and holds for a moment, and the page turns.'
    }
  };
  const ORDER = ['headTurn', 'wink', 'mouth'];

  // ---- The teacher's loop (FaceGlyphScript) ----
  const DURATION = 6.6, HOLD = 0.6, PULSE = 0.6, PAGE_BEAT = 0.09, EASE = 0.35;
  const MOVES = [
    { dir: 1, start: 0.7, held: 0.22 },   // the near miss
    { dir: 1, start: 2.2, held: HOLD },   // turns forward
    { dir: -1, start: 4.2, held: HOLD }   // turns back
  ].map(m => {
    const holdStart = m.start + EASE, release = holdStart + m.held;
    return { ...m, holdStart, release, end: release + EASE, turns: m.held >= HOLD };
  });
  const TURNS = MOVES.filter(m => m.turns);
  const smooth = x => { const c = Math.max(0, Math.min(1, x)); return c * c * (3 - 2 * c); };
  const NEUTRAL = { yaw: 0, bl: 0, br: 0, mouth: 0, jaw: 0 };
  const gesture = (kind, dir) => kind === 'headTurn' ? { ...NEUTRAL, yaw: 0.55 * dir }
    : kind === 'wink' ? { ...NEUTRAL, bl: dir < 0 ? 1 : 0, br: dir > 0 ? 1 : 0 }
    : { ...NEUTRAL, mouth: dir };
  const mix = (a, b, t) => ({ yaw: a.yaw + (b.yaw - a.yaw) * t, bl: a.bl + (b.bl - a.bl) * t,
    br: a.br + (b.br - a.br) * t, mouth: a.mouth + (b.mouth - a.mouth) * t, jaw: a.jaw + (b.jaw - a.jaw) * t });

  function moment(kind, time) {
    const local = ((time % DURATION) + DURATION) % DURATION;
    const page = (local >= TURNS[0].release + PAGE_BEAT && local < TURNS[1].release + PAGE_BEAT) ? 1 : 0;
    const m = { pose: NEUTRAL, page, hold: 0, active: false, beat: 'ready', pulse: 0, local };
    const last = TURNS.filter(t => t.release <= local).pop();
    if (last) {
      const since = local - last.release;
      if (since < PULSE) { m.pulse = 1 - since / PULSE; m.beat = 'turned'; }
    }
    const mv = MOVES.find(x => local >= x.start && local < x.end);
    if (!mv) return m;
    const g = gesture(kind, mv.dir);
    m.active = true;
    if (local < mv.holdStart) {
      m.pose = mix(NEUTRAL, g, smooth((local - mv.start) / EASE)); m.beat = 'holding';
    } else if (local < mv.release) {
      m.pose = g; m.hold = Math.min(1, (local - mv.holdStart) / HOLD); m.beat = 'holding';
    } else {
      const p = smooth((local - mv.release) / EASE);
      m.pose = mix(g, NEUTRAL, p);
      m.hold = mv.turns ? 0 : (1 - p) * mv.held / HOLD;
      if (!mv.turns) m.beat = 'ready';
    }
    return m;
  }

  function caption(kind, local) {
    const k = KINDS[kind];
    if (local < MOVES[1].start) return 'Relax — Face Gestures are ready.';
    if (local < TURNS[0].release + PAGE_BEAT) return k.next;
    if (local < MOVES[2].start) return '…and the page turns.';
    if (local < TURNS[1].release + PAGE_BEAT) return k.back;
    return '…and it turns back.';
  }
  // Reduce Motion: the app's still frames (FaceGlyphScript.stillFrames), without the near miss.
  const STILLS = [
    [0.3, 'Relax — Face Gestures are ready.'],
    [TURNS[0].release - 0.15, 'Hold the movement for a moment…'],
    [TURNS[0].release + PAGE_BEAT + 0.05, '…and the page turns.']
  ];

  // ---- The face (FaceGlyphRenderer) ----
  const EYE_X = 0.28, EYE_Y = (Math.sin(Math.PI / 34) + Math.sin(3 * Math.PI / 34)) / 2, EYE_HALF = 0.052;
  const MOUTH_Y = -Math.sin(3 * Math.PI / 34), MOUTH_HALF = 0.24, MOUTH_DEPTH = 0.075, CLEAR = 0.06;
  const EYE_STROKE_HALF = 0.042, EYE_STROKE_W = 0.058, SMILE_HALF = 0.21, SMILE_DEPTH = 0.058, SMILE_W = 0.034;
  const FIELD = (() => {
    const pts = [], step = Math.PI / 17;
    let row = 0;
    for (let lat = -Math.PI / 2 + step; lat < Math.PI / 2 - step / 2; lat += step, row++) {
      const r = Math.cos(lat), n = Math.max(6, Math.round(2 * Math.PI * r / step));
      const phase = row % 2 === 0 ? 0 : Math.PI / n;
      for (let i = 0; i < n; i++) {
        const lon = i / n * 2 * Math.PI + phase;
        pts.push({ x: r * Math.sin(lon), y: Math.sin(lat), z: r * Math.cos(lon) });
      }
    }
    return pts.filter(p => {
      if (p.z <= -0.2) return true;
      for (const s of [-1, 1]) if (Math.abs(p.x - s * EYE_X) < CLEAR && Math.abs(p.y - EYE_Y) < EYE_HALF + CLEAR * 0.8) return false;
      if (Math.abs(p.x) < MOUTH_HALF + CLEAR * 0.6 && Math.abs(p.y - (MOUTH_Y - MOUTH_DEPTH * 0.6)) < CLEAR * 0.9) return false;
      return true;
    });
  })();
  const US = Array.from({ length: 13 }, (_, i) => i / 12 * 2 - 1);

  function drawFace(ctx, size, pose, glow) {
    ctx.clearRect(0, 0, size, size);
    const radius = size / 2 * 0.9, cx = size / 2, cy = size / 2, unit = radius;
    const yaw = pose.yaw * 0.62, cosY = Math.cos(yaw), sinY = Math.sin(yaw);
    const project = (x, y, z) => [cx + (x * cosY + z * sinY) * radius, cy - y * radius, -x * sinY + z * cosY];
    const surfaceZ = (x, y) => Math.sqrt(Math.max(0, 1 - x * x - y * y));
    const eye = side => {
      const b = Math.max(0, Math.min(1, side < 0 ? pose.bl : pose.br)), t = b * b * (3 - 2 * b), ex = side * EYE_X;
      return US.map(u => {
        const ox = ex, oy = EYE_Y + u * EYE_STROKE_HALF;
        const clx = ex + u * 0.075, cly = EYE_Y - 0.022 - (1 - u * u) * 0.028;
        return [ox + (clx - ox) * t, oy + (cly - oy) * t];
      });
    };
    const mouth = US.map(u => [u * SMILE_HALF + pose.mouth * 0.11,
      MOUTH_Y - (1 - u * u) * (SMILE_DEPTH + pose.jaw * 0.035) + pose.mouth * u * 0.05]);
    const features = eye(-1).concat(eye(1), mouth);

    const turn = Math.min(1, Math.abs(pose.yaw) / 0.25) * glow, leading = yaw >= 0 ? 1 : -1;
    for (const p of FIELD) {
      const [px, py, depth] = project(p.x, p.y, p.z);
      if (depth <= 0.02) continue;
      const rim = Math.pow(depth, 0.8);
      let nearest = Infinity;
      if (p.z > 0.3) for (const f of features) { const dx = p.x - f[0], dy = p.y - f[1]; nearest = Math.min(nearest, dx * dx + dy * dy); }
      const halo = Math.max(0, Math.min(1, (Math.sqrt(nearest) - 0.065) / 0.09));
      if (halo < 0.05) continue;
      const d = Math.max(1, unit * 0.031 * (0.45 + 0.55 * rim));
      const base = (0.24 + 0.44 * rim) * (0.35 + 0.65 * halo);
      let fill = `rgba(${INK},${base})`;
      if (turn > 0) {
        const rx = (px - cx) / unit;
        const warm = Math.max(0, Math.min(1, (rx * leading - 0.4) / 0.5)) * turn * 0.7;
        if (warm > 0.02) fill = `rgba(${ACCENT},${(0.4 + 0.55 * rim) * warm + base * (1 - warm)})`;
      }
      ctx.fillStyle = fill;
      ctx.beginPath(); ctx.arc(px, py, d / 2, 0, Math.PI * 2); ctx.fill();
    }

    const turnMoving = Math.min(1, Math.abs(pose.yaw) / 0.18);
    const stroke = (pts, width, moving) => {
      ctx.beginPath();
      let started = false;
      for (const [x, y] of pts) {
        const [px, py, depth] = project(x, y, surfaceZ(x, y));
        if (depth <= 0.02) continue;
        started ? ctx.lineTo(px, py) : ctx.moveTo(px, py);
        started = true;
      }
      if (!started) return;
      ctx.lineWidth = width; ctx.lineCap = 'round'; ctx.lineJoin = 'round';
      ctx.strokeStyle = `rgba(${INK},0.92)`; ctx.stroke();
      const m = moving * glow;
      if (m > 0.02) { ctx.strokeStyle = `rgba(${ACCENT},${m})`; ctx.stroke(); }
    };
    for (const side of [-1, 1]) {
      const b = Math.max(0, Math.min(1, side < 0 ? pose.bl : pose.br));
      const open = unit * EYE_STROKE_W, closed = unit * EYE_STROKE_W * 0.7;
      stroke(eye(side), open + (closed - open) * b, Math.max(turnMoving, Math.min(1, b / 0.5)));
    }
    stroke(mouth, unit * SMILE_W, Math.max(turnMoving, Math.min(1, Math.abs(pose.mouth) / 0.5)));
  }

  // ---- The score (MiniScorePage) ----
  function drawPage(ctx, w, h, page, accent) {
    ctx.clearRect(0, 0, w, h);
    const r = Math.min(w, h) * 0.0375;
    ctx.beginPath(); ctx.roundRect(0.25, 0.25, w - 0.5, h - 0.5, r);
    ctx.fillStyle = PAPER; ctx.fill();
    ctx.strokeStyle = 'rgba(0,0,0,0.12)'; ctx.lineWidth = 0.5; ctx.stroke();
    const margin = w * 0.1, gap = h * 0.011, top = h * 0.1, systems = 6, sys = (h * 0.86 - top) / systems;
    const line = Math.max(0.6, h * 0.0024);
    for (let s = 0; s < systems; s++) {
      const y0 = top + s * sys;
      ctx.beginPath();
      for (let l = 0; l < 5; l++) { const y = y0 + l * gap; ctx.moveTo(margin, y); ctx.lineTo(w - margin, y); }
      ctx.strokeStyle = `rgba(${INK},0.35)`; ctx.lineWidth = line; ctx.stroke();
      for (let n = 0; n < 9; n++) {
        const x = margin + (w - 2 * margin) * ((n + 0.6) / 9);
        const step = (n * 3 + s * 5 + page * 7) % 9, y = y0 + gap * (4 - step * 0.5);
        ctx.fillStyle = `rgba(${INK},0.75)`;
        ctx.beginPath(); ctx.ellipse(x, y, gap * 0.65, gap * 0.45, 0, 0, Math.PI * 2); ctx.fill();
        ctx.beginPath(); ctx.moveTo(x + gap * 0.6, y); ctx.lineTo(x + gap * 0.6, y - gap * 3);
        ctx.strokeStyle = `rgba(${INK},0.75)`; ctx.lineWidth = line; ctx.stroke();
      }
    }
    const warm = accent > 0.02;
    ctx.font = `${warm ? 600 : 400} ${Math.max(7, h * 0.032)}px -apple-system, BlinkMacSystemFont, 'SF Pro Text', 'Inter', system-ui, sans-serif`;
    ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
    ctx.fillStyle = warm ? `rgba(${ACCENT},${0.5 + 0.5 * accent})` : 'rgb(140,140,140)';
    ctx.fillText(String(page + 1), w / 2, h * 0.95);
  }

  // ---- Wiring ----
  const stage = root.querySelector('.fd-stage');
  const faceCanvas = root.querySelector('.fd-face');
  const ring = root.querySelector('.fd-ring');
  const arc = ring.querySelector('.fd-arc'), ready = ring.querySelector('.fd-ready'), bloom = ring.querySelector('.fd-bloom');
  const score = root.querySelector('.fd-score');
  const under = score.querySelector('.fd-under'), top = score.querySelector('.fd-top');
  const underShade = under.querySelector('.fd-shade'), topShade = top.querySelector('.fd-shade');
  const underCanvas = under.querySelector('canvas'), topCanvas = top.querySelector('canvas');
  const captionEl = root.querySelector('.fd-caption');
  const detailEl = root.querySelector('.fd-detail');
  const tabs = [...root.querySelectorAll('.fd-tab')];
  const stepper = root.querySelector('.fd-steps');
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)');

  let kind = 'headTurn', auto = true, t0 = performance.now(), running = false, raf = 0;
  let glow = 0, lastNow = 0, shownPage = 0, turn = null, still = 0;
  let faceSize = 0, pageW = 0, pageH = 0, dpr = 1;

  function sizeCanvas(c, w, h) {
    c.width = Math.round(w * dpr); c.height = Math.round(h * dpr);
    const ctx = c.getContext('2d'); ctx.setTransform(dpr, 0, 0, dpr, 0, 0); return ctx;
  }
  let faceCtx, underCtx, topCtx;
  function layout() {
    dpr = Math.min(3, window.devicePixelRatio || 1);
    const fr = faceCanvas.getBoundingClientRect(), sr = under.getBoundingClientRect();
    faceSize = fr.width; pageW = sr.width; pageH = sr.height;
    faceCtx = sizeCanvas(faceCanvas, faceSize, faceSize);
    underCtx = sizeCanvas(underCanvas, pageW, pageH);
    topCtx = sizeCanvas(topCanvas, pageW, pageH);
    top.style.setProperty('--persp', `${pageW * 3}px`);
  }

  function setKind(k, byUser) {
    kind = k;
    if (byUser) auto = false;
    tabs.forEach(b => b.setAttribute('aria-pressed', String(b.dataset.kind === k)));
    detailEl.textContent = KINDS[k].detail;
    stage.setAttribute('aria-label', KINDS[k].label);
    t0 = performance.now(); shownPage = 0; turn = null; still = 0;
    if (!running) renderStill();
  }
  tabs.forEach(b => b.addEventListener('click', () => setKind(b.dataset.kind, true)));

  function setCaption(text) {
    if (captionEl.textContent !== text) captionEl.textContent = text;
  }

  function render(m, now, animate) {
    // glow eases like the app's .easeInOut(0.28) on `active`
    const target = m.active && m.beat === 'holding' ? 1 : 0;
    const dt = animate ? Math.min(0.1, (now - lastNow) / 1000) : 1;
    glow += (target - glow) * (1 - Math.exp(-dt / 0.09));
    lastNow = now;
    drawFace(faceCtx, faceSize, m.pose, animate ? glow : target);

    // ring (FaceHoldRing)
    const fill = Math.max(m.hold, m.pulse > 0 ? 1 : 0);
    arc.style.strokeDasharray = `${Math.max(0.0001, fill)} 1`;
    arc.style.opacity = fill > 0.005 ? 1 : 0;
    ready.style.opacity = m.beat === 'ready' && m.hold === 0 ? 1 : 0;
    bloom.style.opacity = m.pulse > 0 ? 0.35 * m.pulse : 0;
    bloom.style.transform = `scale(${1 + 0.025 * (1 - m.pulse)})`;

    // score (MiniScoreView): the page turns on its own 0.62 s clock
    if (animate && m.page !== shownPage) {
      turn = { from: shownPage, to: m.page, forward: m.page === (shownPage + 1) % 3, start: now };
      shownPage = m.page;
    }
    if (!animate) { shownPage = m.page; turn = null; }
    let p = 1;
    if (turn) {
      const x = Math.max(0, Math.min(1, (now - turn.start) / 620));
      p = x < 0.5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2;
      if (x >= 1) turn = null;
    }
    if (turn) {
      const f = turn.forward ? p : 1 - p;           // flip progress of the top layer
      const underPage = turn.forward ? turn.to : turn.from, topPage = turn.forward ? turn.from : turn.to;
      drawPage(underCtx, pageW, pageH, underPage, turn.forward ? m.pulse : 0);
      drawPage(topCtx, pageW, pageH, topPage, turn.forward ? 0 : m.pulse);
      top.style.transform = `perspective(var(--persp)) rotateY(${-88 * f}deg)`;
      top.style.opacity = f > 0.97 ? 0 : 1;
      topShade.style.background = `linear-gradient(to right, rgba(0,0,0,${0.04 * f}), rgba(0,0,0,${0.22 * f}))`;
      const sp = turn.forward ? p : 1 - p, strength = Math.sin(sp * Math.PI) * 0.16;
      underShade.style.background = `linear-gradient(to right, rgba(0,0,0,${strength}), rgba(0,0,0,0) ${(0.25 + 0.7 * sp) * 100}%)`;
    } else {
      drawPage(topCtx, pageW, pageH, shownPage, m.pulse);
      top.style.transform = 'none'; top.style.opacity = 1;
      topShade.style.background = 'none'; underShade.style.background = 'none';
    }
  }

  function frame(now) {
    if (!running) return;
    const time = (now - t0) / 1000;
    if (auto && time >= DURATION * 1) {   // next gesture each loop until the visitor picks one
      setKind(ORDER[(ORDER.indexOf(kind) + 1) % ORDER.length], false);
      raf = requestAnimationFrame(frame); return;
    }
    const m = moment(kind, time);
    render(m, now, true);
    setCaption(caption(kind, m.local));
    raf = requestAnimationFrame(frame);
  }

  function renderStill() {
    const [time, text] = STILLS[still];
    render(moment(kind, time), performance.now(), false);
    setCaption(text);
    stepper.querySelector('[data-step="prev"]').disabled = still === 0;
    stepper.querySelector('[data-step="next"]').disabled = still === STILLS.length - 1;
  }
  stepper.addEventListener('click', e => {
    const b = e.target.closest('[data-step]'); if (!b) return;
    still = Math.max(0, Math.min(STILLS.length - 1, still + (b.dataset.step === 'next' ? 1 : -1)));
    renderStill();
  });

  let visible = false;
  function update() {
    const want = visible && !document.hidden && !reduce.matches;
    root.classList.toggle('is-still', reduce.matches);
    if (want && !running) { running = true; t0 = performance.now(); lastNow = t0; shownPage = 0; turn = null; raf = requestAnimationFrame(frame); }
    if (!want && running) { running = false; cancelAnimationFrame(raf); }
    if (!running) renderStill();
  }
  new IntersectionObserver(es => { visible = es[0].isIntersecting; update(); }, { rootMargin: '80px' }).observe(stage);
  document.addEventListener('visibilitychange', update);
  reduce.addEventListener?.('change', update);
  new ResizeObserver(() => { layout(); if (!running) renderStill(); }).observe(stage);

  layout();
  setKind('headTurn', false);
  update();
})();
