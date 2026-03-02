---
title: 'TWOLAR: A TWO-Step LLM-Augmented Distillation Method for Passage Reranking'

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- Davide Baldelli
- Junfeng Jiang
- Akiko Aizawa
- Paolo Torroni

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2024-01-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2026-03-02T12:28:22.139415Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- paper-conference

# Publication name and optional abbreviated publication name.
publication: '*Advances in Information Retrieval*'
publication_short: ''

doi: ''

abstract: 'In this paper, we present TWOLAR: a two-stage pipeline for passage reranking
  based on the distillation of knowledge from Large Language Models (LLM). TWOLAR
  introduces a new scoring strategy and a distillation process consisting in the creation
  of a novel and diverse training dataset. The dataset consists of 20K queries, each
  associated with a set of documents retrieved via four distinct retrieval methods
  to ensure diversity, and then reranked by exploiting the zero-shot reranking capabilities
  of an LLM. Our ablation studies demonstrate the contribution of each new component
  we introduced. Our experimental results show that TWOLAR significantly enhances
  the document reranking ability of the underlying model, matching and in some cases
  even outperforming state-of-the-art models with three orders of magnitude more parameters
  on the TREC-DL test sets and the zero-shot evaluation benchmark BEIR. To facilitate
  future work we release our data set, finetuned models, and code (Code: https://github.com/Dundalia/TWOLAR;
  Models and Dataset: https://huggingface.co/Dundalia).'

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
---

Add the **full text** or **supplementary notes** for the publication here using Markdown formatting.
