(() => {
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Mobile menu
  const btn = document.querySelector('.menu-btn'), nav = document.getElementById('nav');
  if (btn && nav) {
    const set = (open) => {
      nav.classList.toggle('open', open); btn.classList.toggle('open', open);
      btn.setAttribute('aria-expanded', String(open));
      btn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    };
    btn.addEventListener('click', () => set(!nav.classList.contains('open')));
    nav.addEventListener('click', (e) => { if (e.target.closest('a')) set(false); });
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape') set(false); });
  }

  // Scroll reveal
  const io = 'IntersectionObserver' in window ? new IntersectionObserver((es) => {
    es.forEach((e) => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
  }, { threshold: 0.14, rootMargin: '0px 0px -40px 0px' }) : null;
  document.querySelectorAll('.rv, .step').forEach((el) => io ? io.observe(el) : el.classList.add('in'));

  // Count-up: years roll forward 44 years to the target so the motion reads as time
  document.querySelectorAll('[data-count]').forEach((el) => {
    const end = +el.dataset.count, start = end - 44;
    if (reduce || !io) return;
    el.textContent = start;
    const o = new IntersectionObserver(([e]) => {
      if (!e.isIntersecting) return; o.disconnect();
      const t0 = performance.now(), d = 1600;
      const step = (t) => {
        const p = Math.min(1, (t - t0) / d), k = 1 - Math.pow(1 - p, 3);
        el.textContent = Math.round(start + (end - start) * k);
        if (p < 1) requestAnimationFrame(step);
      };
      requestAnimationFrame(step);
    }, { threshold: 0.6 });
    o.observe(el);
  });

  if (reduce) document.querySelectorAll('svg.plan').forEach((s) => s.pauseAnimations && s.pauseAnimations());

  // Hero live ticker (illustrative events) — flashes the matching device on the plan
  const hero = document.querySelector('.console');
  if (hero) {
    const plan = hero.querySelector('.plan'), list = hero.querySelector('.ticker');
    const events = [
      ['d1', 'ok', 'Badge granted', 'Main entrance'],
      ['c2', 'ok', 'Motion detected', 'Loading dock camera'],
      ['t1', 'ok', 'Single entry verified', 'Lobby lane 2'],
      ['d4', 'alert', 'Door held open', 'Warehouse'],
      ['c6', 'ok', 'Clip bookmarked', 'Lobby camera'],
      ['d3', 'ok', 'Badge granted', 'MDF / server room'],
      ['c3', 'ok', 'Person detected', 'Open office analytics'],
      ['up', 'alert', 'Signal received', 'Alarmco central station'],
      ['d2', 'ok', 'Badge granted', 'Office corridor'],
      ['d5', 'ok', 'Dock door opened', 'Video attached'],
      ['c4', 'ok', 'Line crossing', 'Warehouse aisle 3'],
      ['t1', 'alert', 'Tailgate blocked', 'Lobby lane 1'],
    ];
    let i = 0;
    const fmt = (d) => d.toTimeString().slice(0, 8);
    const fire = () => {
      const [id, kind, what, where] = events[i++ % events.length];
      const li = document.createElement('li');
      li.className = kind;
      li.innerHTML = `<span class="dot"></span><time>${fmt(new Date())}</time><span>${what} &middot; ${where}</span>`;
      list.prepend(li);
      while (list.children.length > 6) list.lastElementChild.remove();
      const el = plan.querySelector(`[data-id="${id}"]`);
      if (el) {
        el.classList.remove('hit', 'ok'); void el.getBBox();
        el.classList.add('hit'); if (kind === 'ok') el.classList.add('ok');
        setTimeout(() => el.classList.remove('hit', 'ok'), 1400);
      }
    };
    for (let n = 0; n < 4; n++) fire();
    if (!reduce) {
      let timer = setInterval(fire, 2300);
      document.addEventListener('visibilitychange', () => {
        clearInterval(timer); if (!document.hidden) timer = setInterval(fire, 2300);
      });
    }
  }

  // System explorer tabs
  const x = document.querySelector('.explore');
  if (x) {
    const plan = x.querySelector('.plan'), tabs = [...x.querySelectorAll('.xt')], panes = [...x.querySelectorAll('.xp')];
    const show = (l) => {
      plan.dataset.show = l;
      tabs.forEach((t) => t.setAttribute('aria-selected', String(t.dataset.l === l)));
      panes.forEach((p) => { p.hidden = p.dataset.l !== l; });
    };
    tabs.forEach((t, n) => {
      t.addEventListener('click', () => show(t.dataset.l));
      t.addEventListener('keydown', (e) => {
        const d = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0;
        if (d) { const nx = tabs[(n + d + tabs.length) % tabs.length]; nx.focus(); show(nx.dataset.l); }
      });
    });
    // Auto-tour until the visitor interacts
    if (!reduce) {
      let k = 0, touring = true;
      const tour = setInterval(() => { if (!touring) return clearInterval(tour); k = (k + 1) % tabs.length; show(tabs[k].dataset.l); }, 4200);
      x.addEventListener('pointerdown', () => { touring = false; }, { once: true });
      x.addEventListener('keydown', () => { touring = false; }, { once: true });
    }
  }
})();
