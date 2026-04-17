/* ============================================================
   APEX CONSTRUCTION LIMITED — Main JavaScript
   ============================================================ */

document.addEventListener('DOMContentLoaded', () => {

  // ── Navbar scroll behaviour ──────────────────────────────
  const navbar = document.getElementById('navbar');
  const isHeroPage = document.querySelector('.hero') !== null;

  function updateNavbar() {
    if (!navbar) return;
    if (isHeroPage) {
      if (window.scrollY > 60) {
        navbar.classList.remove('transparent');
        navbar.classList.add('scrolled');
      } else {
        navbar.classList.add('transparent');
        navbar.classList.remove('scrolled');
      }
    } else {
      navbar.classList.add('scrolled');
      navbar.classList.remove('transparent');
    }
  }

  if (isHeroPage) navbar?.classList.add('transparent');
  else navbar?.classList.add('scrolled');

  window.addEventListener('scroll', updateNavbar, { passive: true });
  updateNavbar();

  // ── Active nav link ──────────────────────────────────────
  const navLinks = document.querySelectorAll('.nav-links a, .mobile-menu a');
  const currentPath = window.location.pathname;
  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPath || (href !== '/' && currentPath.startsWith(href))) {
      link.classList.add('active');
    }
  });

  // ── Hamburger menu ───────────────────────────────────────
  const hamburger = document.getElementById('hamburger');
  const mobileMenu = document.getElementById('mobileMenu');

  hamburger?.addEventListener('click', () => {
    hamburger.classList.toggle('open');
    mobileMenu?.classList.toggle('open');
  });

  document.addEventListener('click', (e) => {
    if (!hamburger?.contains(e.target) && !mobileMenu?.contains(e.target)) {
      hamburger?.classList.remove('open');
      mobileMenu?.classList.remove('open');
    }
  });

  // ── Hero slider ──────────────────────────────────────────
  const slides = document.querySelectorAll('.hero-slide');
  const dots   = document.querySelectorAll('.hero-dot');
  let currentSlide = 0;
  let slideInterval;

  function goToSlide(n) {
    slides[currentSlide]?.classList.remove('active');
    dots[currentSlide]?.classList.remove('active');
    currentSlide = (n + slides.length) % slides.length;
    slides[currentSlide]?.classList.add('active');
    dots[currentSlide]?.classList.add('active');
  }

  function startSlider() {
    slideInterval = setInterval(() => goToSlide(currentSlide + 1), 5500);
  }

  if (slides.length > 0) {
    goToSlide(0);
    startSlider();
    dots.forEach((dot, i) => {
      dot.addEventListener('click', () => {
        clearInterval(slideInterval);
        goToSlide(i);
        startSlider();
      });
    });
  }

  // ── Scroll reveal ────────────────────────────────────────
  const revealEls = document.querySelectorAll('.reveal, .reveal-left');
  const revealObs = new IntersectionObserver((entries) => {
    entries.forEach((entry, i) => {
      if (entry.isIntersecting) {
        setTimeout(() => {
          entry.target.classList.add('visible');
        }, (entry.target.dataset.delay || 0) * 1);
        revealObs.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12 });

  revealEls.forEach((el, i) => {
    el.dataset.delay = (i % 4) * 80;
    revealObs.observe(el);
  });

  // ── Counter animation ─────────────────────────────────────
  function animateCounter(el) {
    const target = parseInt(el.dataset.target || el.textContent.replace(/\D/g, ''), 10);
    const suffix = el.dataset.suffix || '';
    const duration = 1800;
    const start = performance.now();

    function update(now) {
      const elapsed = now - start;
      const progress = Math.min(elapsed / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3);
      el.textContent = Math.round(eased * target) + suffix;
      if (progress < 1) requestAnimationFrame(update);
    }
    requestAnimationFrame(update);
  }

  const counterEls = document.querySelectorAll('.stat-number[data-target]');
  const counterObs = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        animateCounter(entry.target);
        counterObs.unobserve(entry.target);
      }
    });
  }, { threshold: 0.5 });
  counterEls.forEach(el => counterObs.observe(el));

  // ── Testimonials slider ──────────────────────────────────
  const tTrack  = document.querySelector('.testimonials-track');
  const tCards  = document.querySelectorAll('.testimonial-card');
  const tPrev   = document.getElementById('tPrev');
  const tNext   = document.getElementById('tNext');
  let tIndex = 0;

  function slideTo(n) {
    if (!tTrack || tCards.length === 0) return;
    const cols = window.innerWidth < 768 ? 1 : window.innerWidth < 1024 ? 2 : 3;
    const max  = Math.max(0, tCards.length - cols);
    tIndex = Math.max(0, Math.min(n, max));
    const cardW = tCards[0].offsetWidth + 24;
    tTrack.style.transform = `translateX(-${tIndex * cardW}px)`;
  }

  tPrev?.addEventListener('click', () => slideTo(tIndex - 1));
  tNext?.addEventListener('click', () => slideTo(tIndex + 1));
  window.addEventListener('resize', () => slideTo(tIndex));

  // ── Contact/Booking form tabs ─────────────────────────────
  const tabBtns  = document.querySelectorAll('.forms-tab-btn');
  const formPanels = document.querySelectorAll('.form-panel');

  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const target = btn.dataset.tab;
      tabBtns.forEach(b => b.classList.remove('active'));
      formPanels.forEach(p => p.classList.remove('active'));
      btn.classList.add('active');
      document.getElementById(target)?.classList.add('active');
    });
  });

  // ── Project tabs ─────────────────────────────────────────
  const projTabBtns = document.querySelectorAll('.tab-btn');
  projTabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const target = btn.dataset.target;
      projTabBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      document.querySelectorAll('.project-tab-panel').forEach(p => {
        p.style.display = (p.id === target) ? 'grid' : 'none';
      });
    });
  });

  // ── Dismiss alerts ───────────────────────────────────────
  document.querySelectorAll('.alert-msg').forEach(alert => {
    setTimeout(() => {
      alert.style.opacity = '0';
      alert.style.transform = 'translateX(24px)';
      alert.style.transition = 'all .4s ease';
      setTimeout(() => alert.remove(), 400);
    }, 5000);
    alert.addEventListener('click', () => alert.remove());
  });

  // ── Smooth scroll for anchor links ───────────────────────
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', (e) => {
      const target = document.querySelector(anchor.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

});
