---
title: '{{ replace .Name "-" " " | title }}'
date: '{{ now.Format "2006-01-02" }}'
draft: true
tags:
  - research
summary: "TODO: Add a one-sentence research-area summary."
# Font Awesome 5 solid icon shown on the homepage research card, such as comments or balance-scale
icon: "TODO: icon name"
# Position of the card on the homepage, after the existing areas
weight: 10

# Homepage research map: one-line tagline, cover pattern (dots, graph, tokens, or wave), and shared threads
tagline: "TODO: Add a tagline of at most 12 words."
cover_pattern: dots
threads:
  - "TODO: thread shared with other areas, such as Interpretability"

# Research map: an overview graph of subareas, then one detail panel per subarea.
# `key` names the node, `summary` is the hover text, and `links` lists related node keys.
# `status` is done (published), now (current work), or next (where we are heading).
# `cite` lists publication folder names, shown as "Surname et al., Year" links.
map:
  - column: "TODO: Column title"
    blocks:
      - key: first-subarea
        title: "TODO: Subarea title"
        summary: "TODO: One or two short sentences shown on hover."
        topics: []
        links: []
        items:
          - status: done
            text: "TODO: One short sentence on published work."
            cite: []
---

TODO: Define the research area in two or three plain sentences.

