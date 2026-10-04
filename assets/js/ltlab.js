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

  // Copy buttons on publication pages copy the text of the element named by `data-lt-copy`.
  document.querySelectorAll("[data-lt-copy]").forEach((button) => {
    button.addEventListener("click", () => {
      const source = document.querySelector(button.dataset.ltCopy);
      if (!source || !navigator.clipboard) return;
      navigator.clipboard.writeText(source.textContent).then(() => {
        const label = button.querySelector("span");
        const text = label.textContent;
        label.textContent = "Copied";
        setTimeout(() => { label.textContent = text; }, 1600);
      });
    });
  });

  // Annotated examples: a legend entry toggles a filter that dims every other label.
  document.querySelectorAll(".lt-annotate").forEach((figure) => {
    const keys = figure.querySelectorAll(".lt-annotate-key");
    keys.forEach((key) => {
      key.addEventListener("click", () => {
        const active = key.getAttribute("aria-pressed") !== "true";
        keys.forEach((other) => other.setAttribute("aria-pressed", "false"));
        key.setAttribute("aria-pressed", String(active));
        figure.dataset.ltFocus = active ? key.dataset.ltLabel : "";
        figure.querySelectorAll("mark").forEach((mark) => {
          mark.classList.toggle("is-dim", active && mark.dataset.ltLabel !== key.dataset.ltLabel);
        });
      });
    });
  });

  // Stage diagrams: tabs switch the visible stage; arrow keys move between tabs.
  document.querySelectorAll(".lt-stages").forEach((figure) => {
    const tabs = [...figure.querySelectorAll('[role="tab"]')];
    const select = (tab) => {
      tabs.forEach((other) => {
        const selected = other === tab;
        other.setAttribute("aria-selected", String(selected));
        other.tabIndex = selected ? 0 : -1;
        document.getElementById(other.getAttribute("aria-controls")).hidden = !selected;
      });
    };
    tabs.forEach((tab, index) => {
      tab.addEventListener("click", () => select(tab));
      tab.addEventListener("keydown", (event) => {
        const step = { ArrowRight: 1, ArrowLeft: -1 }[event.key];
        if (!step) return;
        const next = tabs[(index + step + tabs.length) % tabs.length];
        select(next);
        next.focus();
      });
    });
  });

  // Research maps: a node or a "Connected to" link shows one detail panel and highlights its links in the overview.
  // A legend key highlights the items with its status; pressing it again shows all items.
  document.querySelectorAll(".lt-rmap").forEach((map) => {
    const panels = [...map.querySelectorAll(".lt-rmap-detail")];
    const nodes = map.querySelectorAll(".lt-rmap-node");
    const edges = map.querySelectorAll(".lt-rmap-edge");
    const show = (area) => {
      panels.forEach((panel) => { panel.hidden = panel.dataset.ltArea !== area; });
      nodes.forEach((node) => node.setAttribute("aria-current", String(node.dataset.ltArea === area)));
      edges.forEach((edge) => edge.classList.toggle("is-active", edge.dataset.ltA === area || edge.dataset.ltB === area));
    };
    map.classList.add("is-interactive");
    const fromHash = panels.find((panel) => `#${panel.id}` === location.hash);
    show((fromHash || panels[0]).dataset.ltArea);
    map.querySelectorAll("a[data-lt-area]").forEach((link) => {
      link.addEventListener("click", (event) => {
        event.preventDefault();
        show(link.dataset.ltArea);
        history.replaceState(null, "", link.getAttribute("href"));
        const panel = map.querySelector(`#area-${link.dataset.ltArea}`);
        if (link.classList.contains("lt-rmap-node")) {
          panel.scrollIntoView({ behavior: matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth", block: "nearest" });
        } else {
          panel.focus({ preventScroll: true });
        }
      });
    });

    const keys = map.querySelectorAll(".lt-rmap-key");
    keys.forEach((key) => {
      key.addEventListener("click", () => {
        const active = key.getAttribute("aria-pressed") !== "true";
        keys.forEach((other) => other.setAttribute("aria-pressed", "false"));
        key.setAttribute("aria-pressed", String(active));
        map.dataset.ltFocus = active ? key.dataset.ltStatus : "";
      });
    });
  });

  // Bar charts grow and research maps appear when they scroll into view; without the observer they render complete.
  const charts = document.querySelectorAll(".lt-bars, .lt-rmap");
  if ("IntersectionObserver" in window && !matchMedia("(prefers-reduced-motion: reduce)").matches) {
    const chartObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.remove("is-waiting");
        chartObserver.unobserve(entry.target);
      });
    }, { rootMargin: "0px 0px -10% 0px" });
    charts.forEach((chart) => {
      chart.classList.add("is-waiting");
      chartObserver.observe(chart);
    });
  }

  // Sections fade in once; the stylesheet disables this for reduced motion.
  if (!("IntersectionObserver" in window) || matchMedia("(prefers-reduced-motion: reduce)").matches) return;
  // The hero is excluded because it is already visible when the script runs.
  const targets = document.querySelectorAll(".home-section:not(#section-hero) .container, .card-simple, .lt-card, .lt-area");
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
