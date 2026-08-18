/* Meta4U 인터랙티브 소개 — 스크립트 (vanilla JS, 의존성 없음) */
(function () {
  'use strict';

  var overlay = document.getElementById('m4uOverlay');
  if (!overlay) return;

  var stage    = document.getElementById('m4uStage'),
      inner    = document.getElementById('m4uInner'),
      slides   = Array.prototype.slice.call(inner.querySelectorAll('.m4u-slide')),
      rail     = document.getElementById('m4uRail'),
      dotsWrap = document.getElementById('m4uDots'),
      counter  = document.getElementById('m4uCounter'),
      wrap     = overlay.querySelector('.m4u-stagewrap'),
      prevBtn  = document.getElementById('m4uPrev'),
      nextBtn  = document.getElementById('m4uNext'),
      prevM    = document.getElementById('m4uPrevM'),
      nextM    = document.getElementById('m4uNextM'),
      total    = slides.length,
      current  = 0,
      busy     = false,
      lastFocus = null;

  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var pad = function (n) { return (n < 10 ? '0' : '') + n; };

  /* ── 내비게이션 생성 ─────────────────────────────── */
  var railItems = [], dots = [];
  slides.forEach(function (s, i) {
    var b = document.createElement('button');
    b.type = 'button';
    b.className = 'm4u-rail-item';
    b.innerHTML = pad(i + 1) + '<span>' + (s.dataset.title || '') + '</span>';
    b.setAttribute('aria-label', pad(i + 1) + ' ' + (s.dataset.title || ''));
    b.addEventListener('click', function () { go(i); });
    rail.appendChild(b);
    railItems.push(b);

    var d = document.createElement('button');
    d.type = 'button';
    d.className = 'm4u-dot';
    d.innerHTML = '<i></i>';
    d.setAttribute('aria-label', pad(i + 1) + ' / ' + pad(total) + ' ' + (s.dataset.title || ''));
    d.addEventListener('click', function () { go(i); });
    dotsWrap.appendChild(d);
    dots.push(d);
  });

  /* ── 화면 전환 ───────────────────────────────────── */
  function paint(i) {
    slides.forEach(function (s, k) {
      s.classList.toggle('is-active', k === i);
      s.classList.remove('is-entering');
    });
    railItems.forEach(function (b, k) {
      b.classList.toggle('is-current', k === i);
      b.setAttribute('aria-current', k === i ? 'true' : 'false');
    });
    dots.forEach(function (d, k) {
      d.classList.toggle('is-current', k === i);
      d.setAttribute('aria-current', k === i ? 'true' : 'false');
    });
    counter.innerHTML = '<b>' + pad(i + 1) + '</b> / ' + pad(total);
    prevBtn.disabled = prevM.disabled = (i === 0);
    nextBtn.disabled = nextM.disabled = (i === total - 1);
    stage.scrollTop = 0;
    wrap.classList.remove('is-scrolled');
    window.setTimeout(checkScrollable, 60);
    // 진입 애니메이션 재생
    void slides[i].offsetWidth;
    if (!reduce) slides[i].classList.add('is-entering');
  }

  function checkScrollable() {
    wrap.classList.toggle('is-scrollable', stage.scrollHeight - stage.clientHeight > 40);
  }
  stage.addEventListener('scroll', function () {
    if (stage.scrollTop > 20) wrap.classList.add('is-scrolled');
  }, { passive: true });
  window.addEventListener('resize', checkScrollable);

  function go(i) {
    if (busy || i === current || i < 0 || i >= total) return;
    current = i;
    if (reduce) { paint(i); return; }
    busy = true;
    inner.classList.add('is-fading');
    window.setTimeout(function () {
      paint(i);
      inner.classList.remove('is-fading');
      busy = false;
    }, 180);
  }

  function next() { go(current + 1); }
  function prev() { go(current - 1); }

  nextBtn.addEventListener('click', next);
  prevBtn.addEventListener('click', prev);
  nextM.addEventListener('click', next);
  prevM.addEventListener('click', prev);

  var restart = document.getElementById('m4uRestart');
  if (restart) restart.addEventListener('click', function () { go(0); });

  /* ── 열기 / 닫기 ─────────────────────────────────── */
  function open(startIndex) {
    lastFocus = document.activeElement;
    overlay.classList.add('is-open');
    overlay.setAttribute('aria-hidden', 'false');
    document.body.classList.add('m4u-locked');
    current = startIndex || 0;
    paint(current);
    window.requestAnimationFrame(function () { overlay.classList.add('is-visible'); });
    window.setTimeout(function () {
      var c = overlay.querySelector('.m4u-close');
      if (c) c.focus();
    }, 60);
  }

  function close() {
    overlay.classList.remove('is-visible');
    var done = function () {
      overlay.classList.remove('is-open');
      overlay.setAttribute('aria-hidden', 'true');
      document.body.classList.remove('m4u-locked');
      if (lastFocus && lastFocus.focus) lastFocus.focus();
    };
    if (reduce) done(); else window.setTimeout(done, 300);
  }

  /* 트리거: id="m4uOpen" 또는 data-m4u-open 속성이 붙은 모든 요소.
     data-m4u-open 값은 시작 화면 번호입니다. 0 = 첫 화면, 4 = 5번째 화면 */
  Array.prototype.forEach.call(document.querySelectorAll('#m4uOpen, [data-m4u-open]'), function (el) {
    var start = function (ev) {
      ev.preventDefault();
      var n = parseInt(el.getAttribute('data-m4u-open'), 10);
      open(isNaN(n) ? 0 : n);
    };
    el.addEventListener('click', start);
    el.addEventListener('keydown', function (ev) {
      if (ev.key === 'Enter' || ev.key === ' ' || ev.key === 'Spacebar') start(ev);
    });
  });
  Array.prototype.forEach.call(overlay.querySelectorAll('[data-m4u-close]'), function (el) {
    el.addEventListener('click', close);
  });

  /* ── 키보드 ──────────────────────────────────────── */
  document.addEventListener('keydown', function (e) {
    if (!overlay.classList.contains('is-open')) return;
    if (e.key === 'Escape') { e.preventDefault(); close(); }
    else if (e.key === 'ArrowRight') { e.preventDefault(); next(); }
    else if (e.key === 'ArrowLeft') { e.preventDefault(); prev(); }
    else if (e.key === 'Home') { e.preventDefault(); go(0); }
    else if (e.key === 'End') { e.preventDefault(); go(total - 1); }
    else if (e.key === 'Tab') {
      var f = overlay.querySelectorAll('button:not([disabled]), [href], [tabindex]:not([tabindex="-1"])');
      if (!f.length) return;
      var first = f[0], last = f[f.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    }
  });

  /* ── 모바일 스와이프 ─────────────────────────────── */
  var sx = 0, sy = 0, tracking = false;
  stage.addEventListener('touchstart', function (e) {
    if (e.touches.length !== 1) { tracking = false; return; }
    sx = e.touches[0].clientX; sy = e.touches[0].clientY; tracking = true;
  }, { passive: true });
  stage.addEventListener('touchend', function (e) {
    if (!tracking) return;
    tracking = false;
    var t = e.changedTouches[0], dx = t.clientX - sx, dy = t.clientY - sy;
    if (Math.abs(dx) > 60 && Math.abs(dx) > Math.abs(dy) * 1.6) { dx < 0 ? next() : prev(); }
  }, { passive: true });

  /* ── PAGE 7 명상실 갤러리 ────────────────────────── */
  var gimg = document.getElementById('m4uGalleryImg'),
      gcap = document.getElementById('m4uGalleryCap'),
      thumbs = document.getElementById('m4uThumbs');
  if (gimg && thumbs) {
    Array.prototype.forEach.call(thumbs.querySelectorAll('.m4u-thumb'), function (t) {
      t.addEventListener('click', function () {
        if (t.classList.contains('is-current')) return;
        Array.prototype.forEach.call(thumbs.querySelectorAll('.m4u-thumb'), function (o) { o.classList.remove('is-current'); });
        t.classList.add('is-current');
        var swap = function () {
          gimg.src = t.dataset.src;
          gimg.alt = '명상실 테마 영상 — ' + t.dataset.cap;
          gcap.textContent = t.dataset.cap;
          gimg.classList.remove('is-fading');
        };
        if (reduce) { swap(); return; }
        gimg.classList.add('is-fading');
        window.setTimeout(swap, 260);
      });
    });
  }

  /* 필요하면 다른 스크립트에서 Meta4U.open(2) 처럼 특정 화면부터 열 수 있습니다 */
  window.Meta4U = { open: open, close: close, go: go };
})();