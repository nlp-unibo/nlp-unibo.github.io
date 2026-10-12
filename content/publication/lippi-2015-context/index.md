---
title: Context-Independent Claim Detection for Argument Mining

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- Marco Lippi
- Paolo Torroni

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2015-01-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2026-03-02T12:28:22.187676Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- paper-conference

# Publication name and optional abbreviated publication name.
publication: '*Proceedings of the Twenty-Fourth International Joint Conference on
  Artificial Intelligence, IJCAI 2015, Buenos Aires, Argentina, July 25-31, 2015*'
publication_short: ''

doi: ''

abstract: 'Argumentation mining aims to automatically identify structured argument data from unstructured natural language text. This challenging, multi-faceted task is recently gaining a growing attention, especially due to its many potential applications. One particularly important aspect of argumentation mining is claim identification. Most of the current approaches are engineered to address specific domains. However, argumentative sentences are often characterized by common rhetorical structures, independently of the domain. We thus propose a method that exploits structured parsing information to detect claims without resorting to contextual information, and yet achieve a performance comparable to that of state-of-the-art methods that heavily rely on the context.'

# Summary. An optional shortened abstract.
summary: A tree kernel over parse trees spots sentences that contain claims without knowing the topic, and performs comparably to systems that rely on topic knowledge.

tags:
- argument mining
- claim detection
- tree kernels
- parse trees
- support vector machines

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
  - /publication_conferences/lippi-2015-context/
topics: [argument-mining]
# Key in data/venues.yaml, whose rank decides the Highlights carousel
venue_key: ijcai
---
