---
title: Overview of MM-ArgFallacy2025 on Multimodal Argumentative Fallacy Detection
  and Classification in Political Debates

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- Eleonora Mancini
- Federico Ruggeri
- Serena Villata
- Paolo Torroni

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2025-07-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2026-02-27T15:55:09.465450Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- paper-conference

# Publication name and optional abbreviated publication name.
publication: '*Proceedings of the 12th Argument mining Workshop*'
publication_short: ''

doi: 10.18653/v1/2025.argmining-1.35

abstract: 'We present an overview of the MM-ArgFallacy2025 shared task on Multimodal
  Argumentative Fallacy Detection and Classification in Political Debates, co-located
  with the 12th Workshop on Argument Mining at ACL 2025. The task focuses on identifying
  and classifying argumentative fallacies across three input modes: text-only, audio-only,
  and multimodal (text+audio), offering both binary detection (AFD) and multi-class
  classification (AFC) subtasks. The dataset comprises 18,925 instances for AFD and
  3,388 instances for AFC, from the MM-USED-Fallacy corpus on U.S. presidential debates,
  annotated for six fallacy types: Ad Hominem, Appeal to Authority, Appeal to Emotion,
  False Cause, Slippery Slope, and Slogan. A total of 5 teams participated: 3 on classification
  and 2 on detection. Participants employed transformer-based models, particularly
  RoBERTa variants, with strategies including prompt-guided data augmentation, context
  integration, specialised loss functions, and various fusion techniques. Audio processing
  ranged from MFCC features to state-of-the-art speech models. Results demonstrated
  textual modality dominance, with best text-only performance reaching 0.4856 F1-score
  for classification and 0.34 for detection. Audio-only approaches underperformed
  relative to text but showed improvements over previous work, while multimodal fusion
  showed limited improvements. This task establishes important baselines for multimodal
  fallacy analysis in political discourse, contributing to computational argumentation
  and misinformation detection capabilities.'

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
  url: https://aclanthology.org/2025.argmining-1.35/
---

Add the **full text** or **supplementary notes** for the publication here using Markdown formatting.
