---
title: Combining Transformers with Natural Language Explanations

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- Federico Ruggeri
- Marco Lippi
- Paolo Torroni

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2021-10-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2026-02-27T15:56:06.376606Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- article

# Publication name and optional abbreviated publication name.
publication: '*arXiv*'
publication_short: ''

doi: ''

abstract: Many NLP applications require models to be interpretable. However, many successful neural architectures, including transformers, still lack effective interpretation methods. A possible solution could rely on building explanations from domain knowledge, which is often available as plain, natural language text. We thus propose an extension to transformer models that makes use of external memories to store natural language explanations and use them to explain classification outputs. We conduct an experimental evaluation on two domains, legal text analysis and argument mining, to show that our approach can produce relevant explanations while retaining or even improving classification performance.

# Summary. An optional shortened abstract.
summary: A transformer extension that stores natural language explanations in an external memory and uses them to explain its predictions.
card_summary: A transformer that stores natural language explanations in memory to explain its predictions.

tags:
- interpretability
- legal
- argument mining

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
- name: arXiv
  url: https://arxiv.org/abs/2110.00125
categories:
  - Preprint
aliases:
  - /publication_preprints/ruggeri-etal-2024-combining/
---
