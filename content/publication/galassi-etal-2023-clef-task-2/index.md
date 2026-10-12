---
title: 'Overview of the CLEF-2023 CheckThat! Lab: Task 2 on Subjectivity Detection'

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- Andrea Galassi
- Federico Ruggeri
- Alberto Barrón-Cedeño
- Firoj Alam
- Tommaso Caselli
- Mücahid Kutlu
- Julia Maria Struß
- Francesco Antici
- Maram Hasanain
- Juliane Köhler
- Katerina Korre
- Folkert Leistra
- Arianna Muti
- Melanie Siegel
- Mehmet Deniz Türkmen
- Michael Wiegand
- Wajdi Zaghouani

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2023-01-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2026-02-27T15:55:09.403923Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- paper-conference

# Publication name and optional abbreviated publication name.
publication: '*Working Notes of the Conference and Labs of the Evaluation Forum (CLEF
  2023), Thessaloniki, Greece, September 18th to 21st, 2023*'
publication_short: ''

doi: ''

abstract: 'We describe the outcome of the 2023 edition of the CheckThat!Lab at CLEF. We focus on subjectivity (Task 2), which has been proposed for the first time. It aims at fostering the technology for the identification of subjective text fragments in news articles. For that, we produced corpora consisting of 9,530 manually-annotated sentences, covering six languages —Arabic, Dutch, English, German, Italian, and Turkish. Task 2 attracted 12 teams, which submitted a total of 40 final runs covering all languages. The most successful approaches addressed the task using state-of-the-art multilingual transformer models, which were fine-tuned on language-specific data. Teams also experimented with a rich set of other neural architectures, including foundation models, zero-shot classifiers, and standard transformers, mainly coupled with data augmentation and multilingual training strategies to address class imbalance. We publicly release all the datasets and evaluation scripts, with the purpose of promoting further research on this topic.'

# Summary. An optional shortened abstract.
summary: The first shared task on telling subjective from objective sentences in six languages, with 9,530 hand-labeled sentences and 12 teams testing current systems.

tags:
- subjectivity detection
- shared task
- multilingual
- news articles
- text classification

# Display this page in a list of Featured pages?
featured: false

# Links
url_pdf: https://ceur-ws.org/Vol-3497/paper-020.pdf
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
categories:
  - Workshop
aliases:
  - /publication_workshops/galassi-etal-2023-clef-task-2/
topics: [fact-checking, benchmark]
---
