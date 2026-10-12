---
title: '{{ replace .Name "-" " " | title }}'
date: '{{ now.Format "2006-01-02" }}'
draft: true
# Card on the Work with us page: one sentence of at most about 18 words.
summary: "TODO: One sentence that says what the proposal does."
# Opened card on the Work with us page: two to four sentences, at most 70 words.
brief: "TODO: Two to four sentences: the problem, the idea, and what a student would do."
# Folder names in content/authors, or {name: ..., email: ...} for a person outside the lab.
# A reader who chooses this proposal writes to these contacts. TODO: add at least one.
contacts: []
# Plain words, not abbreviations; the opened card shows the first three.
tags:
  - TODO tag
# Set to true when the body uses LaTeX.
# math: true
---

<!-- The body is the proposal page, in the style of a publication page; each ## section appears in the page menu. -->
<!-- Build every sentence and diagram from the proposal's own definitions, and say so in each caption. -->

## Context

TODO: The research setting, with every technical term defined at its first use.

## Objective

TODO: What the proposal aims at, in one or two sentences.

{{ "{{<" }} pipeline caption="TODO: What the flow shows, and that it is built from the proposal's description." {{ ">}}" }}
- title: TODO input
  text: TODO one short sentence.
  icon: file-alt
- title: TODO new step
  text: TODO one short sentence.
  icon: lightbulb
  highlight: true
- title: TODO output
  text: TODO one short sentence.
  icon: check
{{ "{{<" }} /pipeline {{ ">}}" }}

<!-- Optional: ## Directions, with possible approaches, and a second flow when two settings are compared. -->

## References

<!-- Optional: copy each reference verbatim, with its DOI or PDF link. Delete the section when there is none. -->
