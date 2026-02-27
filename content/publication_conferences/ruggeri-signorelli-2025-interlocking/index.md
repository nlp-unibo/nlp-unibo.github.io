---
title: Interlocking-free Selective Rationalization Through Genetic-based Learning

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- \textbfFederico Ruggeri
- Gaetano Signorelli

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2025-07-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2026-02-27T15:55:53.548831Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- paper-conference

# Publication name and optional abbreviated publication name.
publication: '*Proceedings of the 63rd Annual Meeting of the Association for Computational
  Linguistics (Volume 1: Long Papers)*'
publication_short: ''

doi: 10.18653/v1/2025.acl-long.59

abstract: A popular end-to-end architecture for selective rationalization is the select-then-predict
  pipeline, comprising a generator to extract highlights fed to a predictor. Such
  a cooperative system suffers from suboptimal equilibrium minima due to the dominance
  of one of the two modules, a phenomenon known as interlocking. While several contributions
  aimed at addressing interlocking, they only mitigate its effect, often by introducing
  feature-based heuristics, sampling, and ad-hoc regularizations. We present GenSPP,
  the first interlocking-free architecture for selective rationalization that does
  not require any learning overhead, as the above-mentioned. GenSPP avoids interlocking
  by performing disjoint training of the generator and predictor via genetic global
  search. Experiments on a synthetic and a real-world benchmark show that our model
  outperforms several state-of-the-art competitors.

# Summary. An optional shortened abstract.
summary: ''

tags: []

# Display this page in a list of Featured pages?
featured: false

# Links
url_pdf: ''
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

# Publication image
# Add an image named `featured.jpg/png` to your page's folder then add a caption below.
image:
  caption: ''
  focal_point: ''
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects: ['internal-project']` links to `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []
links:
- name: URL
  url: https://aclanthology.org/2025.acl-long.59/
---

Add the **full text** or **supplementary notes** for the publication here using Markdown formatting.
