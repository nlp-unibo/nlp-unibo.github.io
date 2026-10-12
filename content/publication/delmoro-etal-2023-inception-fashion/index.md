---
title: 'Inception Models for Fashion Image Captioning: An Extensive Study on Multiple
  Datasets'

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- Mirko Del Moro
- Serban Cristian Tudosie
- Francesco Vannoni
- Andrea Galassi
- Federico Ruggeri

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2023-01-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2026-02-27T15:55:09.399519Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- paper-conference

# Publication name and optional abbreviated publication name.
publication: '*Experimental IR Meets Multilinguality, Multimodality, and Interaction
  - 14th International Conference of the CLEF Association, CLEF 2023, Thessaloniki,
  Greece, September 18-21, 2023, Proceedings*'
publication_short: ''

doi: 10.1007/978-3-031-42448-9_1

abstract: "Fashion e-commerce platforms are becoming increasingly popular. However, scanning, rendering, and captioning fashion items are still done mostly manually. In this work, we address the task of generating a textual description of a fashion item from an image portraying it. We carry out an extensive study with several neural architectures based on InceptionV3. We consider two existing fashion image captioning datasets, FACAD and InFashAI. We also curate a novel dataset, Fashion-Cap, that contains more than 290,000 images and 40,000 corresponding captions. In our analysis, we observe significant differences between the three datasets’ captions, with Fashion-Cap having higher quality captions. To the best of our knowledge, this is the most extensive experimental study in fashion image captioning to date. Our experimental results show that our dataset is less challenging than FACAD but more than InFashAI, which confirms our insights, suggesting that it could be a valuable benchmark for this domain."

# Summary. An optional shortened abstract.
summary: Fashion-Cap, a new dataset for writing captions of fashion product photos, tested with InceptionV3 captioners against two existing datasets of different difficulty.

tags:
- fashion
- image captioning
- dataset
- encoder-decoder
- attention
- beam search

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
  url: https://doi.org/10.1007/978-3-031-42448-9_1
categories:
  - Conference
aliases:
  - /publication_workshops/delmoro-etal-2023-inception-fashion/
topics: [multimodal, benchmark]
# Key in data/venues.yaml, whose rank decides the Highlights carousel
venue_key: clef
---
