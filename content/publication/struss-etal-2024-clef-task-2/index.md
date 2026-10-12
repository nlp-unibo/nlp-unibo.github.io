---
title: Overview of the CLEF-2024 CheckThat! Lab Task 2 on Subjectivity in News Articles

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- Julia Maria Struß
- Federico Ruggeri
- Alberto Barrón-Cedeño
- Firoj Alam
- Dimitar Dimitrov
- Andrea Galassi
- Georgi Pachov
- Ivan Koychev
- Preslav Nakov
- Melanie Siegel
- Michael Wiegand
- Maram Hasanain
- Reem Suwaileh
- Wajdi Zaghouani

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2024-01-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2026-02-27T15:55:09.438095Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- paper-conference

# Publication name and optional abbreviated publication name.
publication: '*Working Notes of the Conference and Labs of the Evaluation Forum (CLEF
  2024), Grenoble, France, 9-12 September, 2024*'
publication_short: ''

doi: ''

abstract: 'We present an overview of Task 2 of the seventh edition of the CheckThat! lab at the 2024 iteration of the Conference and Labs of the Evaluation Forum (CLEF). The task focuses on subjectivity detection in news articles and was offered in five languages: Arabic, Bulgarian, English, German, and Italian, as well as in a multilingual setting. The datasets for each language were carefully curated and annotated, comprising over 10,000 sentences from news articles. The task challenged participants to develop systems capable of distinguishing between subjective statements (reflecting personal opinions or biases) and objective ones (presenting factual information) at the sentence level. A total of 15 teams participated in the task, submitting 36 valid runs across all language tracks. The participants used a variety of approaches, with transformer-based models being the most popular choice. Strategies included fine-tuning monolingual and multilingual models, and leveraging English models with automatic translation for the non-English datasets. Some teams also explored ensembles, feature engineering, and innovative techniques such as few-shot learning and in-context learning with large language models. The evaluation was based on macro-averaged F1 score. The results varied across languages, with the best performance achieved for Italian and German, followed by English. The Arabic track proved particularly challenging, with no team surpassing an F1 score of 0.50. This task contributes to the broader goal of enhancing the reliability of automated content analysis in the context of misinformation detection and fact-checking. The paper provides detailed insights into the datasets, participant approaches, and results, offering a benchmark for the current state of subjectivity detection across multiple languages.'

# Summary. An optional shortened abstract.
summary: A shared task on telling subjective from objective news sentences in five languages, where 15 teams show what current systems achieve and where they struggle.

tags:
- subjectivity detection
- shared task
- news articles
- multilingual
- sentence classification

# Display this page in a list of Featured pages?
featured: false

# Links
url_pdf: https://ceur-ws.org/Vol-3740/paper-25.pdf
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
  - /publication_workshops/struss-etal-2024-clef-task-2/
topics: [subjectivity, fact-checking, benchmark]
# Key in data/venues.yaml, whose name every list shows
venue_key: clef-wn
---
