---
title: '{{ replace .Name "-" " " | title }}'
authors:
  - "TODO: Author name"
author_notes: []
date: '{{ now.Format "2006-01-02" }}'
publishDate: '{{ now.Format "2006-01-02" }}'
draft: true
publication_types:
  # article-journal for a journal paper, paper-conference for a conference or workshop paper
  - article-journal
publication: "TODO: Venue"
publication_short: ""
doi: ""
abstract: "TODO: Add abstract."
# One sentence shown under the title of the publication page and on publication cards
summary: ""
tags:
  - selected
featured: false
url_pdf: ""
url_code: ""
url_dataset: ""
url_poster: ""
url_project: ""
url_slides: ""
url_source: ""
url_video: ""
image:
  caption: ""
  focal_point: ""
  preview_only: false
projects: []
# Keep Highlight and set the venue list: Journal, Conference, Workshop, or Preprint.
categories:
  - Highlight
  - Journal
# Optional affiliations shown under the authors
affiliations: []
# Research topics as keys of data/topics.yaml, shown as colored tags
topics: []
---

<!--
The body is the project page of the paper, shown after the abstract.
It guides a reader outside the field from the research setting, to the motivation, to the method, to the results.
Never show a number or a term before the text has given its context. The page links to no other publication.
Base every statement on the paper, and leave details to the paper itself.
Keep the five sections below, so that every page has the same structure; each `##` heading also appears in the section menu.

Visual components (see the README for their YAML):
  {{</* figure src="method.png" caption="..." */>}}  a figure from the paper, saved in this folder
  {{</* gap */>}} ... {{</* /gap */>}}                comparison with related work
  {{</* pipeline */>}} ... {{</* /pipeline */>}}      method diagram
  {{</* stages */>}} ... {{</* /stages */>}}          interactive diagram of what is trained, optimized, or frozen at each stage
  {{</* numbers */>}} ... {{</* /numbers */>}}        headline numbers, only in Results
  {{</* bars */>}} ... {{</* /bars */>}}              interactive results chart
  {{</* annotate */>}} ... {{</* /annotate */>}}      interactive annotated text example
  {{</* takeaways */>}} ... {{</* /takeaways */>}}    numbered takeaway cards
Save the representative figure as `featured.png`: it becomes the teaser and the preview on every card.
To publish only the abstract for now, delete everything below this comment.
-->

## Research setting

TODO: Introduce the task and the field for a newcomer, with a schema or a real example from the paper.

## Motivation

TODO: State the gap in related work with a gap table, then the objective of the paper in one blockquote.

## Approach

TODO: Explain the method around one figure from the paper or a pipeline diagram.

## Results

TODO: Say what was measured, show the headline numbers, then the main results as a chart, a table, or a paper figure.

## Takeaways

TODO: List three takeaways with the takeaways component.
