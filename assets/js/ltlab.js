// Scroll effects and publication year headers; every effect is optional progressive enhancement.
(() => {
  const navbar = document.getElementById("navbar-main");
  if (navbar) {
    const onScroll = () => navbar.classList.toggle("lt-scrolled", window.scrollY > 8);
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  // Long citation lists get a heading before the first entry of each year, unless their block sets `lt-no-years`.
  document.querySelectorAll(".wg-collection:not(.lt-no-years), .universal-wrapper").forEach((list) => {
    const items = list.querySelectorAll(".pub-list-item[data-year]");
    if (items.length < 6) return;
    let year = null;
    items.forEach((item) => {
      if (item.dataset.year === year) return;
      year = item.dataset.year;
      const heading = document.createElement("h2");
      heading.className = "lt-year";
      heading.textContent = year;
      item.before(heading);
    });
  });

  // Sections fade in once; the stylesheet disables this for reduced motion.
  if (!("IntersectionObserver" in window) || matchMedia("(prefers-reduced-motion: reduce)").matches) return;
  // The hero is excluded because it is already visible when the script runs.
  const targets = document.querySelectorAll(".home-section:not(#section-hero) .container, .lt-tile, .card-simple");
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add("lt-visible");
      observer.unobserve(entry.target);
    });
  }, { rootMargin: "0px 0px -8% 0px" });
  targets.forEach((target) => {
    target.classList.add("lt-reveal");
    observer.observe(target);
  });
})();
