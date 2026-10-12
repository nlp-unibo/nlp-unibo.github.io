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

# Homepage research card: one-line tagline and cover pattern (dots, graph, tokens, or wave)
tagline: "TODO: Add a tagline of at most 12 words."
cover_pattern: dots

# Argument views (optional): tabs under the overview, one argument each, grouped by argument model or domain.
# See content/research/am/index.md for the fields of a view.
# views: []

# Research areas: one block per area; selecting a block enlarges it and opens its tasks beside it.
fields:
  - key: first-field
    title: "TODO: Block title"
    icon: search
    question: "TODO: The question this family of tasks answers."
    summary: "TODO: One or two sentences."
    tasks:
      - name: "TODO: Task name"
        text: "TODO: Given <input>, the task is to <output>."

# Our focus: the lab topics, shown as a rotating carousel and one detail box per topic.
# Publications join a topic through their own `focus` field, such as `focus: [<this folder>/first-topic]`.
focus:
  - key: first-topic
    title: "TODO: Topic title"
    icon: comments
    summary: "TODO: Card text of at most two sentences."
    description: "TODO: Two to four sentences that define the topic for a reader outside the field."
---

## What is TODO?

TODO: Define the research area in three or four plain sentences.

