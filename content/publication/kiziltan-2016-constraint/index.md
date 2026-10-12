---
title: Constraint Detection in Natural Language Problem Descriptions

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- Zeynep Kiziltan
- Marco Lippi
- Paolo Torroni

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2016-01-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2026-03-02T12:28:22.183535Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- paper-conference

# Publication name and optional abbreviated publication name.
publication: '*Proceedings of the Twenty-Fifth International Joint Conference on Artificial
  Intelligence, IJCAI 2016, New York, NY, USA, 9-15 July 2016*'
publication_short: ''

doi: ''

abstract: 'Modeling in constraint programming is a hard task that requires considerable expertise. Automated model reformulation aims at assisting a naive user in modeling constraint problems. In this context, formal specification languages have been devised to express constraint problems in a manner similar to natural yet rigorous specifications that use a mixture of natural language and discrete mathematics. Yet, a gap remains between such languages and the natural language in which humans informally describe problems. This work aims to alleviate this issue by proposing a method for detecting constraints in natural language problem descriptions using a structured-output classifier. To evaluate the method, we develop an original annotated corpus which gathers 110 problem descriptions from several resources. Our results show significant accuracy with respect to metrics used in cognate tasks.'

# Summary. An optional shortened abstract.
summary: A sequence labeler marks the words of a natural language problem description that state constraints, a first step from informal text to formal models.

tags:
- constraint programming
- constraint detection
- sequence labeling
- structured output
- annotated corpus
topics: [knowledge-extraction]

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
categories:
  - Conference
aliases:
  - /publication_conferences/kiziltan-2016-constraint/
# Key in data/venues.yaml, whose rank decides the Highlights carousel
venue_key: ijcai
---
