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

  // Stage diagrams and argument views: tabs switch the visible panel; arrow keys move between tabs.
  // Argument views render every panel, so without the script all views stay visible.
  document.querySelectorAll(".lt-stages, .lt-arg-views").forEach((figure) => {
    const tabs = [...figure.querySelectorAll('[role="tab"]')];
    // A tab chosen by the reader announces its panel with an `lt-show` event, which starts the view animation, and
    // the panel it hides with an `lt-hide` event, which stops a view still playing.
    const select = (tab, chosen) => {
      tabs.forEach((other) => {
        const selected = other === tab;
        const panel = document.getElementById(other.getAttribute("aria-controls"));
        other.setAttribute("aria-selected", String(selected));
        other.tabIndex = selected ? 0 : -1;
        if (!selected && !panel.hidden) panel.dispatchEvent(new CustomEvent("lt-hide"));
        panel.hidden = !selected;
      });
      if (chosen) document.getElementById(tab.getAttribute("aria-controls")).dispatchEvent(new CustomEvent("lt-show"));
    };
    tabs.forEach((tab, index) => {
      tab.addEventListener("click", () => select(tab, true));
      tab.addEventListener("keydown", (event) => {
        const step = { ArrowRight: 1, ArrowLeft: -1 }[event.key];
        if (!step) return;
        const next = tabs[(index + step + tabs.length) % tabs.length];
        select(next, true);
        next.focus();
      });
    });
    select(tabs.find((tab) => tab.getAttribute("aria-selected") === "true") || tabs[0]);
  });

  // A view starts once it comes into sight, above the bottom quarter of the window, so its writing is seen from
  // the start. Without IntersectionObserver it starts at once.
  const onSight = (element, start) => {
    if (!("IntersectionObserver" in window)) { start(); return; }
    const sight = new IntersectionObserver((entries) => {
      if (!entries.some((entry) => entry.isIntersecting)) return;
      sight.disconnect();
      start();
    }, { rootMargin: "0px 0px -25% 0px" });
    sight.observe(element);
  };

  // Argument graphs: nodes sit in aligned columns, and each edge is an SVG path from its source node to its
  // target node, ending in an arrowhead at the target, with its relation written on it. Edges within a row
  // run straight across; edges between rows run straight down when the nodes are aligned, and otherwise
  // bend at right angles halfway between the rows. A graph redraws whenever its size changes,
  // which also covers a tab that becomes visible.
  // A view returns to its blank state at once: transitions and animations stay off while its classes change,
  // so marks, tags, and highlights vanish instead of fading out while the text is written again.
  const instantly = (view, change) => {
    view.classList.add("lt-instant");
    change();
    void view.offsetWidth;
    view.classList.remove("lt-instant");
  };
  // A side panel (argument graph or clause matrix) appears with `name` on its view: below the text it slides in,
  // and beside the text the text narrows to make room. Its content is laid out at once at its final width, measured
  // with transitions off, so it does not grow tall in the narrow opening column.
  const reveal = (view, panel, content, name) => new Promise((resolve) => {
    const below = getComputedStyle(view.querySelector(".lt-arg-panels")).gridTemplateColumns.split(" ").length < 2;
    instantly(view, () => view.classList.add(name));
    const width = content.offsetWidth;
    instantly(view, () => view.classList.remove(name));
    content.style.width = `${width}px`;
    view.classList.add(name);
    if (below) panel.animate([{ opacity: 0, transform: "translateY(16px)" }, { opacity: 1, transform: "none" }], { duration: 700, easing: "ease-out" });
    setTimeout(() => { content.style.width = ""; resolve(); }, 900);
  });
  // Replay scrolls smoothly back to the example tabs, with about two lines of their introduction above them and below
  // the navigation bar, once the view is reset and the page has its new height, so the shorter page cannot cut it short.
  const backToTabs = (view) => {
    const views = view.closest(".lt-arg-views");
    const top = (views.querySelector(".lt-arg-tabgroups") || views).getBoundingClientRect().top + scrollY - 150;
    requestAnimationFrame(() => scrollTo({ top, behavior: "smooth" }));
  };
  const svgNS = "http://www.w3.org/2000/svg";
  const svgElement = (name, attributes) => {
    const element = document.createElementNS(svgNS, name);
    Object.entries(attributes).forEach(([key, value]) => element.setAttribute(key, value));
    return element;
  };
  document.querySelectorAll("[data-lt-graph]").forEach((graph, index) => {
    const svg = graph.querySelector("svg");
    const edges = [...graph.querySelectorAll(".lt-arg-edges li")];
    const head = (relation) => `lt-arg-head-${index}-${relation}`;
    // During a view animation, `shown` holds the nodes already in place: only edges between them are drawn,
    // and an edge drawn for the first time grows from its source before its arrowhead and label appear.
    let shown = null;
    let seen = new Set();
    const draw = () => {
      const base = graph.getBoundingClientRect();
      if (!base.width) return;
      // A section out of focus is scaled down, so screen sizes are divided by the scale to get SVG units.
      const k = base.width / graph.offsetWidth || 1;
      const box = (id) => {
        const rect = graph.querySelector(`[data-lt-node="${id}"]`).getBoundingClientRect();
        const x = (rect.left - base.left) / k;
        const y = (rect.top - base.top) / k;
        return { x, y, w: rect.width / k, h: rect.height / k, cx: x + rect.width / k / 2 };
      };
      const defs = svgElement("defs", {});
      ["support", "attack", "link"].forEach((relation) => {
        const marker = svgElement("marker", { id: head(relation), viewBox: "0 0 10 10", refX: "10", refY: "5", markerWidth: "7", markerHeight: "7", orient: "auto-start-reverse" });
        marker.append(svgElement("path", { d: "M0 0 L10 5 L0 10 z", class: `lt-arg-edge-head is-${relation}` }));
        defs.append(marker);
      });
      svg.replaceChildren(defs);
      const ends = edges.map((edge) => {
        const a = box(edge.dataset.from);
        const b = box(edge.dataset.to);
        return { edge, a, b, across: a.y < b.y + b.h && b.y < a.y + a.h };
      });
      // Edges that enter the same side of a node spread along it, ordered by the position of their source.
      const entering = {};
      ends.filter((end) => !end.across).forEach((end) => {
        (entering[`${end.edge.dataset.to}:${end.a.y < end.b.y ? "top" : "bottom"}`] ||= []).push(end);
      });
      // A label takes the first of its candidate places that overlaps no box and no label already placed.
      const placed = edges.map((edge) => box(edge.dataset.from)).concat(edges.map((edge) => box(edge.dataset.to)));
      const clear = (r) => placed.every((o) => r.x + r.width + 3 < o.x || o.x + o.w + 3 < r.x || r.y + r.height + 2 < o.y || o.y + o.h + 2 < r.y);
      const label = (spots, text) => {
        const element = svgElement("text", { "text-anchor": "middle", class: "lt-arg-edge-label" });
        element.textContent = text;
        svg.append(element);
        let rect = null;
        for (const [x, y] of [...spots, spots[0]]) {
          element.setAttribute("x", x);
          element.setAttribute("y", y);
          rect = element.getBBox();
          if (clear(rect)) break;
        }
        placed.push({ x: rect.x, y: rect.y, w: rect.width, h: rect.height });
      };
      ends.forEach((end) => {
        const { edge, a, b } = end;
        const relation = edge.dataset.relation;
        if (shown && !(shown.has(edge.dataset.from) && shown.has(edge.dataset.to))) return;
        const fresh = shown && !seen.has(edge);
        if (fresh) seen.add(edge);
        const before = svg.querySelectorAll("text").length;
        const twin = edges.find((other) => other.dataset.from === edge.dataset.to && other.dataset.to === edge.dataset.from);
        const writes = !(twin && edges.indexOf(twin) < edges.indexOf(edge) && twin.dataset.label === edge.dataset.label);
        let d;
        if (end.across) {
          // Same row: a straight line between the facing sides; two opposite edges run 8px apart.
          const y = (Math.max(a.y, b.y) + Math.min(a.y + a.h, b.y + b.h)) / 2 + (twin ? (a.x < b.x ? -8 : 8) : 0);
          const [x1, x2] = a.x < b.x ? [a.x + a.w, b.x] : [a.x, b.x + b.w];
          d = `M${x1} ${y} H${x2}`;
          // A label too wide for the gap between the boxes moves below or above the row.
          const xm = (x1 + x2) / 2;
          if (writes) label([[xm, y - (twin ? 14 : 7)], [xm, Math.max(a.y + a.h, b.y + b.h) + 14], [xm, Math.min(a.y, b.y) - 6]], edge.dataset.label);
        } else {
          const down = a.y < b.y;
          const y1 = down ? a.y + a.h : a.y;
          const y2 = down ? b.y : b.y + b.h;
          const list = entering[`${edge.dataset.to}:${down ? "top" : "bottom"}`].sort((p, q) => p.a.cx - q.a.cx);
          const inside = list.length === 1 && a.cx > b.x + 12 && a.cx < b.x + b.w - 12;
          const x2 = inside ? a.cx : b.x + (b.w * (list.indexOf(end) + 1)) / (list.length + 1);
          const ym = (y1 + y2) / 2;
          if (Math.abs(a.cx - x2) < 1) {
            d = `M${x2} ${y1} V${y2}`;
            if (writes) label([[x2, ym + 4]], edge.dataset.label);
          } else {
            d = `M${a.cx} ${y1} V${ym} H${x2} V${y2}`;
            // The label sits on the middle leg, or on the leg into its target or out of its source when that is taken.
            if (writes) label([[(a.cx + x2) / 2, ym - 6], [x2, (ym + y2) / 2 + 4], [a.cx, (y1 + ym) / 2 + 4]], edge.dataset.label);
          }
        }
        const path = svgElement("path", { d, class: `lt-arg-edge is-${relation}` });
        svg.insertBefore(path, defs.nextSibling);
        const text = svg.querySelectorAll("text")[before];
        if (!fresh) {
          path.setAttribute("marker-end", `url(#${head(relation)})`);
          return;
        }
        const length = path.getTotalLength();
        path.style.strokeDasharray = length;
        if (text) text.style.opacity = 0;
        path.animate([{ strokeDashoffset: length }, { strokeDashoffset: 0 }], { duration: 900, easing: "ease-in-out" }).finished.then(() => {
          path.style.strokeDasharray = "";
          path.setAttribute("marker-end", `url(#${head(relation)})`);
          if (text) text.animate([{ opacity: 0 }, { opacity: 1 }], { duration: 400 }).finished.then(() => { text.style.opacity = ""; });
        });
      });
      graph.classList.add("is-drawn");
    };
    graph.ltShow = (ids) => {
      shown = ids;
      seen = new Set();
      draw();
    };
    graph.ltDraw = draw;
    new ResizeObserver(draw).observe(graph);
    draw();
  });

  // Pointing at or focusing a box of an argument graph, or a component in the text, lights the pair and dims the rest of the text.
  document.querySelectorAll(".lt-arg-view [data-lt-graph]").forEach((graph) => {
    const view = graph.closest(".lt-arg-view");
    const link = (event, on) => {
      const item = event.target.closest("[data-lt-node], [data-lt-span]");
      const id = item && (item.dataset.ltNode || item.dataset.ltSpan);
      // While a view plays, components exist for the reader only once Annotate has marked them.
      if (on && view.classList.contains("is-animating") && !view.classList.contains("is-marked")) return;
      if (!id || !view.querySelector(`[data-lt-span="${id}"]`)) return;
      view.classList.toggle("is-linking", on);
      view.querySelectorAll(`[data-lt-span="${id}"], [data-lt-node="${id}"]`).forEach((element) => element.classList.toggle("is-linked", on));
    };
    ["pointerover", "focusin"].forEach((type) => view.addEventListener(type, (event) => link(event, true)));
    ["pointerout", "focusout"].forEach((type) => view.addEventListener(type, (event) => link(event, false)));
  });

  // Pointing at or focusing a clause in a rules view, or its row in the matrix, lights both; while the view plays,
  // only once Detect has marked the clauses.
  document.querySelectorAll(".lt-rules").forEach((view) => {
    const link = (event, on) => {
      const item = event.target.closest("[data-lt-clause], [data-lt-card]");
      if (!item || (on && view.classList.contains("is-ready") && !view.classList.contains("is-marked"))) return;
      const n = item.dataset.ltClause || item.dataset.ltCard;
      view.querySelectorAll(`[data-lt-clause="${n}"], [data-lt-card="${n}"]`).forEach((element) => element.classList.toggle("is-linked", on));
    };
    ["pointerover", "focusin"].forEach((type) => view.addEventListener(type, (event) => link(event, true)));
    ["pointerout", "focusout"].forEach((type) => view.addEventListener(type, (event) => link(event, false)));
  });

  // Argument views play at reading pace. Picking a tab, or scrolling the first view into sight, writes the text;
  // the Annotate button then marks its components, and the Show graph button shows the argument graph, beside the text
  // or below it, and moves each component from the text to its box, with the page following the moving box; an edge grows once both of its
  // boxes are in place. Replay plays the view again. Under reduced motion, or without the script,
  // every view shows its final state and the buttons stay hidden.
  if (!matchMedia("(prefers-reduced-motion: reduce)").matches) {
    const pause = (ms) => new Promise((resolve) => { setTimeout(resolve, ms); });
    const ease = (t) => (t < 0.5 ? 4 * t * t * t : 1 - (-2 * t + 2) ** 3 / 2);
    const frames = (duration, step) => new Promise((resolve) => {
      const start = performance.now();
      const frame = (now) => {
        const t = Math.min(1, (now - start) / duration);
        if (step(t) === false || t === 1) resolve();
        else requestAnimationFrame(frame);
      };
      requestAnimationFrame(frame);
    });
    document.querySelectorAll(".lt-arg-views").forEach((views) => {
      const panels = [...views.querySelectorAll(".lt-arg-view:not(.lt-detect, .lt-rules, .lt-speech)")];
      const controls = (view) => {
        const bar = view.querySelector(".lt-arg-controls");
        return {
          bar,
          annotate: bar.querySelector('[data-lt-action="annotate"]'),
          skip: bar.querySelector('[data-lt-action="skip"]'),
          graph: bar.querySelector('[data-lt-action="graph"]'),
          link: bar.querySelector(".lt-arg-link"),
          replay: bar.querySelector('[data-lt-action="replay"]'),
        };
      };
      const finish = (view, replay) => {
        const run = view.ltRun;
        if (!run) return;
        view.ltRun = null;
        run.parts.forEach(([node, text]) => { node.textContent = text; });
        run.texts.forEach((text) => { text.style.minHeight = ""; });
        run.flying.forEach((fly) => fly.remove());
        view.querySelectorAll(".lt-arg-span").forEach((span) => {
          span.style.transitionDelay = "";
          span.classList.remove("is-sending");
        });
        instantly(view, () => {
          view.querySelectorAll(".is-shown, .is-linked").forEach((node) => node.classList.remove("is-shown", "is-linked"));
          view.classList.remove("is-animating", "is-marked", "is-graph", "is-linking");
        });
        run.graph.ltShow(null);
        const { bar, skip, annotate, graph, link, replay: again } = controls(view);
        skip.hidden = true;
        annotate.hidden = Boolean(replay);
        graph.hidden = Boolean(replay);
        link.hidden = Boolean(replay);
        again.hidden = !replay;
        bar.hidden = !replay;
      };
      // The blank state: the text is empty but keeps its final height, and the argument graph shows no box or edge.
      const prepare = (view) => {
        panels.forEach((other) => finish(other, false));
        // A view may hold several texts side by side; they are written one after the other. Unstated components are
        // not written: each appears just before its box is placed.
        const texts = [...view.querySelectorAll(".lt-arg-text:not(.lt-arg-unstated)")];
        const run = { texts, graph: view.querySelector("[data-lt-graph]"), ids: new Set(), flying: [], parts: [] };
        // The text is measured at the full width it takes before Show graph.
        instantly(view, () => view.classList.add("is-animating"));
        texts.forEach((text) => { text.style.minHeight = `${text.offsetHeight}px`; });
        texts.forEach((text) => {
          const walker = document.createTreeWalker(text, NodeFilter.SHOW_TEXT, {
            acceptNode: (node) => (node.parentElement.closest(".lt-arg-tag") ? NodeFilter.FILTER_REJECT : NodeFilter.FILTER_ACCEPT),
          });
          while (walker.nextNode()) run.parts.push([walker.currentNode, walker.currentNode.textContent]);
        });
        run.parts.forEach(([node]) => { node.textContent = ""; });
        view.ltRun = run;
        run.graph.ltShow(run.ids);
        const { bar, skip, annotate, graph, link, replay } = controls(view);
        skip.hidden = false;
        bar.hidden = false;
        annotate.hidden = false;
        graph.hidden = false;
        link.hidden = false;
        replay.hidden = true;
        bar.classList.remove("is-annotated");
        annotate.classList.remove("is-done");
        annotate.disabled = true;
        graph.disabled = true;
        return run;
      };
      // 1. The text is written at about 55 characters per second, between 1.5 and 6 seconds in total; Skip writes the rest at once.
      const write = async (view) => {
        const run = view.ltRun && !view.ltRun.started ? view.ltRun : prepare(view);
        run.started = true;
        const total = run.parts.reduce((sum, [, text]) => sum + text.length, 0);
        await frames(Math.min(6000, Math.max(1500, total * 18)), (t) => {
          if (view.ltRun !== run) return false;
          let left = run.skip ? total : Math.round(t * total);
          run.parts.forEach(([node, text]) => {
            node.textContent = text.slice(0, Math.max(0, Math.min(text.length, left)));
            left -= text.length;
          });
          return !run.skip;
        });
        if (view.ltRun !== run) return;
        const { skip, annotate: next } = controls(view);
        skip.hidden = true;
        next.disabled = false;
      };
      // 2. The components are marked one after the other: each tag opens and its underline appears.
      const annotate = async (view) => {
        const run = view.ltRun;
        if (!run) return;
        const spans = [...view.querySelectorAll("[data-lt-span]")];
        const { bar, annotate: button, graph: next } = controls(view);
        button.disabled = true;
        button.classList.add("is-done");
        spans.forEach((span, i) => { span.style.transitionDelay = `${i * 500}ms`; });
        view.classList.add("is-marked");
        await pause((spans.length - 1) * 500 + 800);
        if (view.ltRun !== run) return;
        // The connector fills toward the second step, which then becomes available.
        bar.classList.add("is-annotated");
        await pause(600);
        if (view.ltRun === run) next.disabled = false;
      };
      // The page scrolls just enough to keep a box between the navigation bar and the bottom of the window.
      const follow = (run, top, bottom) => {
        if (run.manual) return;
        const want = Math.min(Math.max(scrollY, bottom - innerHeight + 40), top - 100);
        scrollTo(0, scrollY + (want - scrollY) * 0.12);
      };
      // 3. Each component leaves the text as a copy of its box, which travels to its place in the argument graph;
      // the page follows the box unless the reader scrolls. Implicit components fade in after the others.
      const showGraph = async (view) => {
        const run = view.ltRun;
        if (!run) return;
        controls(view).graph.disabled = true;
        // The argument graph panel appears only now, before the first component leaves the text.
        const panel = view.querySelector(".lt-arg-graph-panel");
        await reveal(view, panel, panel.querySelector(".lt-arg-graph-scroll"), "is-graph");
        if (view.ltRun !== run) return;
        const stop = () => { run.manual = true; };
        ["wheel", "touchmove", "keydown"].forEach((type) => addEventListener(type, stop, { once: true, passive: true }));
        const spans = [...view.querySelectorAll("[data-lt-span]")];
        const nodes = [...run.graph.querySelectorAll("[data-lt-node]")];
        const order = [
          ...spans.map((span) => nodes.find((node) => node.dataset.ltNode === span.dataset.ltSpan)),
          ...nodes.filter((node) => !spans.some((span) => span.dataset.ltSpan === node.dataset.ltNode)),
        ];
        const land = (node) => {
          node.classList.add("is-shown");
          run.ids.add(node.dataset.ltNode);
          run.graph.ltDraw();
        };
        for (const node of order) {
          if (view.ltRun !== run) return;
          const span = spans.find((other) => other.dataset.ltSpan === node.dataset.ltNode);
          const unsaid = span?.closest(".lt-arg-unstated");
          if (unsaid && !unsaid.classList.contains("is-shown")) {
            unsaid.classList.add("is-shown");
            unsaid.animate([{ opacity: 0, transform: "translateY(6px)" }, { opacity: 1, transform: "none" }], { duration: 500, easing: "ease-out" });
            await pause(700);
            if (view.ltRun !== run) return;
          }
          if (!span) {
            land(node);
            node.animate([{ opacity: 0 }, { opacity: 1 }], { duration: 700, easing: "ease" });
            await pause(900);
            continue;
          }
          // The marked text is first enclosed, line by line, in frames of its role color; the frames then detach,
          // fill, and travel to the argument graph, where they meet as one box while its content fades in. Only the frames
          // change size; the content keeps the final box size, so its text never re-wraps on the way.
          // Positions are measured again at every frame, because a sticky text moves against the views as the page scrolls.
          const measure = () => {
            const base = views.getBoundingClientRect();
            const k = base.width / views.offsetWidth || 1;
            const local = (rect, pad) => ({
              x: (rect.left - base.left) / k - pad, y: (rect.top - base.top) / k - pad / 2, w: rect.width / k + 2 * pad, h: rect.height / k + pad,
            });
            return {
              k,
              baseTop: base.top + scrollY,
              lines: [...span.getClientRects()].filter((rect) => rect.width > 2).map((rect) => local(rect, 5)),
              b: local(node.getBoundingClientRect(), 0),
            };
          };
          const { lines, b } = measure();
          const role = [...node.classList].find((name) => name.startsWith("lt-role-"));
          const widest = lines.reduce((best, line) => (line.w > best.w ? line : best), lines[0]);
          const ghost = node.cloneNode(true);
          ghost.removeAttribute("data-lt-node");
          ghost.className = `${ghost.className} lt-arg-ghost`;
          ghost.style.width = `${b.w}px`;
          ghost.style.height = `${b.h}px`;
          const flights = lines.map((line) => {
            const frame = document.createElement("div");
            frame.className = `lt-arg-fly ${role}`;
            frame.setAttribute("aria-hidden", "true");
            if (line === widest) frame.append(ghost);
            views.append(frame);
            run.flying.push(frame);
            return { frame, lead: line === widest };
          });
          span.classList.add("is-sending");
          const place = (e, ring, fill, content, lift) => {
            const now = measure();
            const { b } = now;
            flights.forEach((flight, i) => { flight.a = now.lines[i] || flight.a || lines[i]; });
            flights.forEach(({ frame, a, lead }) => {
              const r = { x: a.x + (b.x - a.x) * e, y: a.y + (b.y - a.y) * e, w: a.w + (b.w - a.w) * e, h: a.h + (b.h - a.h) * e };
              frame.style.transform = `translate(${r.x}px, ${r.y}px)`;
              frame.style.width = `${r.w}px`;
              frame.style.height = `${r.h}px`;
              frame.style.setProperty("--lt-ring", ring);
              frame.style.setProperty("--lt-fill", lead ? fill : fill * (1 - e));
              frame.style.setProperty("--lt-lift", lead ? lift : 0);
            });
            ghost.style.opacity = content;
            const top = Math.min(...flights.map(({ a }) => a.y + (b.y - a.y) * e));
            const bottom = Math.max(...flights.map(({ a }) => a.y + a.h + (b.y + b.h - a.y - a.h) * e));
            follow(run, now.baseTop + top * now.k, now.baseTop + bottom * now.k);
          };
          await frames(500, (t) => { if (view.ltRun !== run) return false; place(0, ease(t), 0, 0, 0); return true; });
          await pause(150);
          await frames(1200, (t) => {
            if (view.ltRun !== run) return false;
            const e = ease(t);
            place(e, Math.min(1, (1 - e) / 0.4), e, Math.max(0, (e - 0.25) / 0.75), Math.sin(Math.PI * e));
            return true;
          });
          if (view.ltRun !== run) return;
          land(node);
          span.classList.remove("is-sending");
          flights.forEach(({ frame }) => frame.remove());
          await pause(300);
        }
        await pause(1500);
        if (view.ltRun === run) finish(view, true);
      };
      panels.forEach((view) => {
        view.addEventListener("lt-show", () => write(view));
        view.addEventListener("lt-hide", () => finish(view, false));
        const { skip, annotate: a, graph: b, replay } = controls(view);
        skip.addEventListener("click", () => { if (view.ltRun) view.ltRun.skip = true; });
        a.addEventListener("click", () => annotate(view));
        b.addEventListener("click", () => showGraph(view));
        replay.addEventListener("click", () => {
          write(view);
          backToTabs(view);
        });
      });
      // The first view is written once it comes into sight.
      const first = panels.find((view) => !view.hidden);
      if (!first) return;
      prepare(first);
      onSight(first, () => {
        if (first.ltRun && !first.ltRun.started) write(first);
      });
    });
  }

  // Document views (detect, rules, and voices): picking a tab, or the first view coming into sight, writes the
  // document at about 55 characters per second, between 1.5 and 6 seconds in total (a voices view at about 35, up to 9
  // seconds, since its readings appear one by one); Skip writes the rest at once.
  // Detect then plays the first step. In a detect view it scans the document one sentence at a time and highlights
  // each annotated clause with its category and level. In a rules view it opens the clause matrix beside the text, marks
  // each clause and fills its row, and Classify then shows the rules and, clause by clause, lights the rule with the
  // same pattern and labels the clause. The page follows the step unless the reader scrolls. Replay writes the document
  // again. Under reduced motion, or without the script, every view shows its final state and the buttons stay hidden.
  if (!matchMedia("(prefers-reduced-motion: reduce)").matches) {
    const pause = (ms) => new Promise((resolve) => { setTimeout(resolve, ms); });
    const docs = [...document.querySelectorAll(".lt-detect, .lt-rules, .lt-speech")];
    docs.forEach((view) => {
      const rules = view.classList.contains("lt-rules");
      const speech = view.classList.contains("lt-speech");
      const bar = view.querySelector(".lt-detect-controls");
      const button = (action) => bar.querySelector(`[data-lt-action="${action}"]`);
      const [skip, detect, classify, replay] = ["skip", "detect", "classify", "replay"].map(button);
      const link = bar.querySelector(".lt-arg-link");
      const steps = [detect, classify, link].filter(Boolean);
      const doc = view.querySelector(".lt-detect-doc");
      const units = [...view.querySelectorAll(rules ? "[data-lt-clause]" : "[data-lt-sentence]")];
      // The written text: every text node of the document except tags and clause numbers.
      const parts = [];
      const walker = document.createTreeWalker(doc, NodeFilter.SHOW_TEXT, {
        acceptNode: (node) => (node.parentElement.closest(".lt-detect-tag, .lt-rule-tag, .lt-rule-num, .lt-arg-tag, .lt-voice-cuename, .lt-voice-pause") ? NodeFilter.FILTER_REJECT : NodeFilter.FILTER_ACCEPT),
      });
      while (walker.nextNode()) parts.push([walker.currentNode, walker.currentNode.textContent]);
      const total = parts.reduce((sum, [, text]) => sum + text.length, 0);
      let run = 0;
      let manual = false;
      let skipping = false;
      const follow = (element) => { if (!manual) element.scrollIntoView({ block: "nearest", behavior: "smooth" }); };
      const watch = () => {
        manual = false;
        ["wheel", "touchmove", "keydown"].forEach((type) => addEventListener(type, () => { manual = true; }, { once: true, passive: true }));
      };
      // The marks and labels of the steps go back to their blank state; the text stays as it is.
      const clear = () => {
        run += 1;
        instantly(view, () => {
          view.classList.add("is-ready");
          view.classList.remove("is-detected", "is-marked", "is-detecting", "is-classifying", "is-classified", "is-listening");
          bar.classList.remove("is-annotated");
          view.querySelectorAll(".is-current, .is-hit, .is-shown, .is-labelled, .is-match, .is-linked").forEach((node) => node.classList.remove("is-current", "is-hit", "is-shown", "is-labelled", "is-match", "is-linked"));
          view.querySelectorAll("[style*=delay]").forEach((node) => { node.style.transitionDelay = ""; node.style.animationDelay = ""; });
        });
        steps.forEach((node) => { node.hidden = false; node.classList.remove("is-done"); });
        detect.disabled = true;
        if (classify) classify.disabled = true;
        replay.hidden = true;
        bar.hidden = false;
      };
      // The blank state keeps the final height of the document, so the page does not jump while it is written.
      // A voices view instead grows reading by reading, each one shown once its text starts.
      const readings = [...view.querySelectorAll(".lt-voice-reading")];
      const blank = () => {
        clear();
        if (!doc.style.minHeight && !readings.length) doc.style.minHeight = `${doc.offsetHeight}px`;
        parts.forEach(([node]) => { node.textContent = ""; });
      };
      const write = async () => {
        blank();
        const id = run;
        skipping = false;
        skip.hidden = false;
        const duration = readings.length ? Math.min(9000, Math.max(1500, total * 28)) : Math.min(6000, Math.max(1500, total * 18));
        const start = performance.now();
        await new Promise((resolve) => {
          const frame = (now) => {
            if (run !== id) return resolve();
            let left = skipping ? total : Math.round(Math.min(1, (now - start) / duration) * total);
            const done = left >= total;
            parts.forEach(([node, text]) => {
              node.textContent = text.slice(0, Math.max(0, Math.min(text.length, left)));
              left -= text.length;
            });
            readings.forEach((reading) => { reading.hidden = !reading.querySelector(".lt-arg-textlabel").textContent; });
            if (done) resolve();
            else requestAnimationFrame(frame);
          };
          requestAnimationFrame(frame);
        });
        doc.style.minHeight = "";
        if (run !== id) return;
        skip.hidden = true;
        detect.disabled = false;
      };
      const finish = () => {
        steps.forEach((node) => { node.hidden = true; });
        replay.hidden = false;
      };
      const scan = async () => {
        const id = run;
        detect.disabled = true;
        detect.classList.add("is-done");
        watch();
        for (const sentence of units) {
          const clause = sentence.classList.contains("lt-detect-clause");
          sentence.classList.add("is-current");
          follow(sentence);
          await pause(clause ? 700 : 350);
          if (run !== id) return;
          sentence.classList.remove("is-current");
          if (clause) {
            sentence.classList.add("is-hit");
            await pause(400);
            if (run !== id) return;
          }
        }
        view.classList.add("is-detected");
        finish();
      };
      const mark = async () => {
        const id = run;
        detect.disabled = true;
        detect.classList.add("is-done");
        const panel = view.querySelector(".lt-matrix-panel");
        await reveal(view, panel, panel.querySelector(".lt-matrix-scroll"), "is-detecting");
        if (run !== id) return;
        watch();
        for (const clause of units) {
          const card = view.querySelector(`[data-lt-card="${clause.dataset.ltClause}"]`);
          const spans = [...clause.querySelectorAll(".lt-rule-span")];
          spans.forEach((span, i) => { span.style.transitionDelay = `${i * 200}ms`; });
          card.querySelectorAll("th, td").forEach((cell, i) => { cell.style.animationDelay = `${i * 200}ms`; });
          clause.classList.add("is-current", "is-hit");
          follow(clause);
          await pause(spans.length * 200 + 500);
          if (run !== id) return;
          card.classList.add("is-shown", "is-current");
          follow(card);
          await pause(card.querySelectorAll("td").length * 200 + 700);
          if (run !== id) return;
          clause.classList.remove("is-current");
          card.classList.remove("is-current");
        }
        view.classList.add("is-marked");
        bar.classList.add("is-annotated");
        await pause(600);
        if (run === id) classify.disabled = false;
      };
      const label = async () => {
        const id = run;
        classify.disabled = true;
        classify.classList.add("is-done");
        view.classList.add("is-classifying");
        view.querySelector(".lt-matrix-rules").animate([{ opacity: 0 }, { opacity: 1 }], { duration: 600, easing: "ease-out" });
        watch();
        await pause(800);
        for (const clause of units) {
          if (run !== id) return;
          const n = clause.dataset.ltClause;
          const card = view.querySelector(`[data-lt-card="${n}"]`);
          const rule = view.querySelector(`[data-lt-rulecard="${clause.dataset.ltRule}"]`);
          card.classList.add("is-current");
          follow(card);
          await pause(700);
          if (run !== id) return;
          rule.classList.add("is-match");
          follow(rule);
          await pause(900);
          if (run !== id) return;
          card.classList.add("is-labelled");
          clause.classList.add("is-labelled");
          follow(card);
          await pause(900);
          if (run !== id) return;
          rule.classList.remove("is-match");
          card.classList.remove("is-current");
        }
        view.classList.add("is-classified");
        finish();
      };
      // In a voices view, Listen opens the cue strips in CSS, reading by reading, for the time its `data-lt-play` gives;
      // Classify then opens the answers panel and shows the answer of each model.
      const annotate = async () => {
        const id = run;
        detect.disabled = true;
        detect.classList.add("is-done");
        view.classList.add("is-marked");
        await pause(Number(view.dataset.ltPlay));
        if (run !== id) return;
        bar.classList.add("is-annotated");
        await pause(600);
        if (run === id) classify.disabled = false;
      };
      const listen = async () => {
        const id = run;
        classify.disabled = true;
        classify.classList.add("is-done");
        const panel = view.querySelector(".lt-speech-panel");
        await reveal(view, panel, panel.querySelector(".lt-speech-body"), "is-listening");
        if (run !== id) return;
        watch();
        follow(panel);
        await pause(600);
        for (const row of view.querySelectorAll(".lt-speech-row")) {
          if (run !== id) return;
          row.classList.add("is-shown");
          await pause(900);
        }
        if (run !== id) return;
        view.classList.add("is-classified");
        finish();
      };
      skip.addEventListener("click", () => { skipping = true; });
      detect.addEventListener("click", speech ? annotate : rules ? mark : scan);
      if (classify) classify.addEventListener("click", speech ? listen : label);
      replay.addEventListener("click", () => {
        write();
        backToTabs(view);
      });
      view.addEventListener("lt-show", write);
      view.addEventListener("lt-hide", clear);
      view.ltWrite = write;
      view.ltBlank = blank;
    });
    // The first visible document view is written once it comes into sight; until then it stays blank.
    document.querySelectorAll(".lt-arg-views").forEach((views) => {
      const first = docs.find((view) => views.contains(view) && !view.hidden);
      if (!first) return;
      let started = false;
      onSight(first, () => {
        if (!started) first.ltWrite();
        started = true;
      });
      first.addEventListener("lt-show", () => { started = true; }, { once: true });
      first.ltBlank();
    });
  }

  // Research areas: opening a block hides the others, enlarges it, and shows its panel beside it.
  // The back button, a second click on the block, or Escape returns to the grid.
  // Without the script every panel is visible below its block.
  document.querySelectorAll("[data-lt-fields]").forEach((fields) => {
    const grid = fields.querySelector(".lt-fields-grid");
    const blocks = [...fields.querySelectorAll(".lt-field")];
    const panel = (block) => document.getElementById(block.getAttribute("aria-controls"));
    let open = null;
    const show = (block) => {
      const previous = open;
      open = block;
      grid.classList.toggle("has-open", Boolean(block));
      blocks.forEach((other) => {
        other.setAttribute("aria-expanded", String(other === block));
        other.parentElement.classList.toggle("is-open", other === block);
        panel(other).hidden = other !== block;
      });
      if (!block && previous) previous.focus();
    };
    blocks.forEach((block) => block.addEventListener("click", () => show(open === block ? null : block)));
    fields.querySelectorAll(".lt-field-back").forEach((back) => {
      back.hidden = false;
      back.addEventListener("click", () => show(null));
    });
    fields.addEventListener("keydown", (event) => { if (event.key === "Escape" && open) show(null); });
    fields.classList.add("is-interactive");
    show(null);
  });

  // Research area focus topics: the centered card opens its detail box below the carousel, scrolls to it,
  // and holds the rotation; a faded neighbour card moves to the center instead. The box fades out when the
  // carousel moves to another topic, and its close button returns to the carousel.
  // Without the script every box is visible and the card links jump to it.
  document.querySelectorAll(".lt-focus").forEach((focus) => {
    const boxes = [...focus.querySelectorAll(".lt-topic-box")];
    const cards = [...focus.querySelectorAll(".lt-focus-card")];
    const carousel = focus.querySelector("[data-lt-carousel]");
    const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
    let open = null;
    const show = (key) => {
      open = key;
      boxes.forEach((box) => {
        box.classList.remove("is-leaving");
        box.hidden = box.dataset.ltTopic !== key;
      });
      cards.forEach((card) => card.classList.toggle("is-selected", card.dataset.ltTopic === key));
      if (carousel && carousel.ltHold) carousel.ltHold("topic", Boolean(key));
    };
    const close = () => {
      const box = boxes.find((other) => other.dataset.ltTopic === open);
      if (!box || reduce) return show(null);
      box.classList.add("is-leaving");
      setTimeout(() => { if (box.classList.contains("is-leaving")) show(null); }, 300);
    };
    focus.querySelectorAll("a[data-lt-topic]").forEach((link) => {
      link.addEventListener("click", (event) => {
        event.preventDefault();
        const card = link.closest(".lt-focus-card");
        if (carousel && carousel.ltGo && !card.classList.contains("is-active")) {
          carousel.ltGo(cards.indexOf(card));
          return;
        }
        show(link.dataset.ltTopic);
        history.replaceState(null, "", link.getAttribute("href"));
        const box = focus.querySelector(`#topic-${link.dataset.ltTopic}`);
        box.scrollIntoView({ behavior: reduce ? "auto" : "smooth", block: "start" });
        box.focus({ preventScroll: true });
      });
    });
    focus.querySelectorAll(".lt-topic-close").forEach((button) => {
      button.hidden = false;
      // The page scrolls back first and the box closes once the scroll ends, so that the shorter page
      // cannot cut the scroll short.
      button.addEventListener("click", () => {
        const card = cards.find((other) => other.dataset.ltTopic === open);
        history.replaceState(null, "", location.pathname);
        let done = false;
        const end = () => {
          if (done) return;
          done = true;
          show(null);
          if (card) card.querySelector("a[data-lt-topic]").focus({ preventScroll: true });
        };
        addEventListener("scrollend", end, { once: true });
        setTimeout(end, reduce ? 0 : 1000);
        carousel.scrollIntoView({ behavior: reduce ? "auto" : "smooth", block: "center" });
      });
    });
    if (carousel) {
      carousel.addEventListener("lt-slide", (event) => {
        if (open && cards[event.detail] && cards[event.detail].dataset.ltTopic !== open) close();
      });
    }
    // A link to #topic-<key> centers that topic in the carousel and opens its box, which holds the rotation.
    // This waits one frame, until the carousel below has been set up.
    const fromHash = boxes.find((box) => `#${box.id}` === location.hash);
    show(null);
    if (fromHash) {
      requestAnimationFrame(() => {
        const index = cards.findIndex((card) => card.dataset.ltTopic === fromHash.dataset.ltTopic);
        if (carousel && carousel.ltGo) carousel.ltGo(index);
        show(fromHash.dataset.ltTopic);
        fromHash.scrollIntoView({ block: "start" });
      });
    }
  });

  // Bar charts grow when they scroll into view; without the observer they render complete.
  const charts = document.querySelectorAll(".lt-bars");
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

  // Carousels (homepage preprints, research focus topics): dots and arrows scroll the track to a slide;
  // the track scrolls by itself without the script. `is-centered` centers the active slide, `data-lt-loop`
  // wraps from the last slide to the first, and `data-lt-autoplay` advances every N milliseconds.
  // There is no autoplay under reduced motion.
  document.querySelectorAll("[data-lt-carousel]").forEach((carousel) => {
    const track = carousel.querySelector(".lt-carousel-track");
    const slides = [...track.children];
    const dots = [...carousel.querySelectorAll("[data-lt-slide]")];
    const [previous, next] = carousel.querySelectorAll("[data-lt-step]");
    const loop = carousel.hasAttribute("data-lt-loop");
    const centered = carousel.classList.contains("is-centered");
    const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
    // A centered loop shows a copy of the last slide before the first and a copy of the first after the last,
    // so a neighbour always peeks on both sides; landing on a copy jumps to the slide it copies.
    const copies = new Map();
    if (centered && loop && slides.length > 2) {
      [[slides[slides.length - 1], "prepend"], [slides[0], "append"]].forEach(([slide, where]) => {
        const copy = slide.cloneNode(true);
        copy.classList.add("is-copy");
        copy.setAttribute("aria-hidden", "true");
        copy.querySelectorAll("[id]").forEach((element) => element.removeAttribute("id"));
        copy.querySelectorAll("a, button").forEach((element) => { element.tabIndex = -1; });
        // A copy stays clickable for the pointer: it moves the carousel one step toward the slide it copies.
        copy.addEventListener("click", (event) => {
          event.preventDefault();
          go(where === "append" ? slides.length : -1);
        });
        track[where](copy);
        copies.set(copy, slide);
      });
    }
    const items = [...track.children];
    let current = 0;
    const offset = (item) => (centered ? item.offsetLeft - (track.clientWidth - item.offsetWidth) / 2 : item.offsetLeft);
    const nearest = () => items.reduce((best, item) =>
      (Math.abs(offset(item) - track.scrollLeft) < Math.abs(offset(best) - track.scrollLeft) ? item : best), items[0]);
    let target = null;
    let settle = null;
    const go = (index) => {
      let item;
      if (copies.size && index === slides.length) item = items[items.length - 1];
      else if (copies.size && index === -1) item = items[0];
      else item = slides[loop ? (index + slides.length) % slides.length : Math.max(0, Math.min(slides.length - 1, index))];
      // The target stays active during the scroll, so the slides it passes do not light up on the way.
      target = item;
      track.scrollTo({ left: offset(item), behavior: reduce ? "auto" : "smooth" });
      update();
      wait();
    };
    // Landing on a copy jumps to the slide it copies, with transitions off so the jump is invisible.
    const jump = (item) => {
      carousel.classList.add("is-jumping");
      track.scrollTo({ left: offset(item), behavior: "auto" });
      items.forEach((other) => other.classList.toggle("is-active", other === item));
      requestAnimationFrame(() => requestAnimationFrame(() => carousel.classList.remove("is-jumping")));
    };
    const update = () => {
      const atEnd = !centered && track.scrollLeft + track.clientWidth >= track.scrollWidth - 2;
      const item = target || (atEnd ? slides[slides.length - 1] : nearest());
      const before = current;
      current = slides.indexOf(copies.get(item) || item);
      if (current !== before) carousel.dispatchEvent(new CustomEvent("lt-slide", { detail: current }));
      dots.forEach((dot, i) => dot.setAttribute("aria-current", String(i === current)));
      items.forEach((other) => other.classList.toggle("is-active", other === item));
      if (!loop) {
        previous.disabled = current === 0;
        next.disabled = current === slides.length - 1;
      }
    };
    // The scroll has settled 150 ms after its last event.
    const settled = () => {
      const landed = nearest();
      target = null;
      if (copies.has(landed)) jump(copies.get(landed));
      else update();
    };
    const wait = () => {
      clearTimeout(settle);
      settle = setTimeout(settled, 150);
    };
    dots.forEach((dot, i) => dot.addEventListener("click", () => go(i)));
    previous.addEventListener("click", () => go(current - 1));
    next.addEventListener("click", () => go(current + 1));
    track.addEventListener("scroll", () => { update(); wait(); }, { passive: true });
    // With the script the track does not scroll freely, so a vertical page scroll can never shift it.
    // A horizontal swipe, a horizontal wheel or trackpad gesture, or an arrow key moves one slide.
    let swipe = null;
    track.addEventListener("pointerdown", (event) => {
      if (event.pointerType !== "mouse") swipe = [event.clientX, event.clientY];
    });
    track.addEventListener("pointerup", (event) => {
      if (!swipe) return;
      const dx = event.clientX - swipe[0];
      const dy = event.clientY - swipe[1];
      swipe = null;
      if (Math.abs(dx) > 40 && Math.abs(dx) > Math.abs(dy)) go(current + (dx < 0 ? 1 : -1));
    });
    track.addEventListener("pointercancel", () => { swipe = null; });
    let sweep = 0;
    let sweeping = null;
    track.addEventListener("wheel", (event) => {
      if (Math.abs(event.deltaX) <= Math.abs(event.deltaY)) return;
      event.preventDefault();
      // One gesture moves one slide; the gesture ends 200 ms after its last wheel event.
      if (sweep !== null) sweep += event.deltaX;
      if (sweep !== null && Math.abs(sweep) > 60) {
        go(current + Math.sign(sweep));
        sweep = null;
      }
      clearTimeout(sweeping);
      sweeping = setTimeout(() => { sweep = 0; }, 200);
    }, { passive: false });
    track.addEventListener("keydown", (event) => {
      const step = { ArrowRight: 1, ArrowLeft: -1 }[event.key];
      if (!step || event.target !== track) return;
      event.preventDefault();
      go(current + step);
    });

    // Autoplay: the current dot fills over the delay, and the end of its fill moves to the next slide.
    // The fill holds while the pointer or the keyboard focus is inside, or while a detail box is open.
    const delay = Number(carousel.dataset.ltAutoplay) || 0;
    if (delay && !reduce) {
      const holds = new Set();
      carousel.ltHold = (reason, on) => {
        if (on) holds.add(reason); else holds.delete(reason);
        carousel.classList.toggle("is-holding", holds.size > 0);
      };
      carousel.style.setProperty("--lt-autoplay", `${delay}ms`);
      carousel.classList.add("is-autoplay");
      dots.forEach((dot) => dot.addEventListener("animationend", () => go(current + 1)));
      carousel.addEventListener("mouseenter", () => carousel.ltHold("pointer", true));
      carousel.addEventListener("mouseleave", () => carousel.ltHold("pointer", false));
      carousel.addEventListener("focusin", (event) => carousel.ltHold("focus", event.target.matches(":focus-visible")));
      carousel.addEventListener("focusout", () => carousel.ltHold("focus", false));
    }

    carousel.ltGo = go;
    carousel.classList.add("is-enhanced");
    carousel.querySelector(".lt-carousel-nav").hidden = false;
    if (centered) track.scrollLeft = offset(slides[0]);
    // Only a width change re-centers the track; mobile browsers also resize when their toolbars hide.
    let width = track.clientWidth;
    addEventListener("resize", () => {
      if (track.clientWidth === width) return;
      width = track.clientWidth;
      track.scrollLeft = offset(slides[current]);
    });
    update();
  });

  // Section focus: on the homepage and on research area pages, each section gets a focus value from 0 to 1 as
  // `--lt-f`, from its distance to a focus line, so it grows and takes its color while it nears the line and
  // shrinks and turns grey while it leaves it. The line starts at the top of the window, so the first section is in
  // focus at the top of the page; it reaches 40% of the window height after scrolling that far, and moves to the
  // bottom of the window over the last 40% of the page, so the last section takes the focus at the bottom.
  // Without the script, or under reduced motion, every section stays fully visible.
  if (matchMedia("(prefers-reduced-motion: reduce)").matches) return;
  const sections = [...document.querySelectorAll(".home-section, .lt-band")];
  if (sections.length > 1) {
    document.body.classList.add("lt-section-focus");
    let queued = false;
    const refocus = () => {
      queued = false;
      const h = innerHeight;
      const left = document.documentElement.scrollHeight - h - scrollY;
      // The line never sits above the first section, which may start below the navigation bar.
      const line = Math.max(sections[0].getBoundingClientRect().top, Math.min(scrollY, h * 0.4) + Math.max(0, h * 0.4 - left) * 1.5);
      const fade = h * 0.35;
      sections.forEach((section) => {
        // Only the content of a section is scaled, so the section box, and its focus value, stay put.
        const { top, bottom } = section.getBoundingClientRect();
        const d = line < top ? top - line : line > bottom ? line - bottom : 0;
        section.style.setProperty("--lt-f", Math.max(0, 1 - d / fade).toFixed(3));
      });
    };
    const queue = () => {
      if (!queued) requestAnimationFrame(refocus);
      queued = true;
    };
    addEventListener("scroll", queue, { passive: true });
    addEventListener("resize", queue);
    refocus();
  }

  // Cards outside those sections fade in once, for instance on list pages.
  if (!("IntersectionObserver" in window)) return;
  const targets = [...document.querySelectorAll(".card-simple, .lt-card")].filter((card) => !card.closest(".home-section, .lt-band"));
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
