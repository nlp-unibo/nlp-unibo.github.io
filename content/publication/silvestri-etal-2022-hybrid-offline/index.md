---
title: Hybrid Offline/Online Optimization for Energy Management via Reinforcement
  Learning

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- Mattia Silvestri
- Allegra De Filippo
- Federico Ruggeri
- Michele Lombardi

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2022-01-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2026-02-27T15:55:09.418374Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- paper-conference

# Publication name and optional abbreviated publication name.
publication: '*Integration of Constraint Programming, Artificial Intelligence, and
  Operations Research - 19th International Conference, CPAIOR 2022, Los Angeles, CA,
  USA, June 20-23, 2022, Proceedings*'
publication_short: ''

doi: 10.1007/978-3-031-08011-1_24

abstract: 'Constrained decision problems in the real world are subject to uncertainty. If predictive information about the stochastic elements is available offline, recent works have shown that it is possible to rely on an (expensive) parameter tuning phase to improve the behavior of a simple online solver so that it roughly matches the solution quality of an anticipative approach but maintains its original efficiency. Here, we start from a state-of-the-art offline/online optimization method that relies on optimality conditions to inject knowledge of a (convex) online approach into an offline solver used for parameter tuning. We then propose to replace the offline step with (Deep) Reinforcement Learning (RL) approaches, which results in a simpler integration scheme with a higher potential for generalization. We introduce two hybrid methods that combine both learning and optimization: the first optimizes all the parameters at once, whereas the second exploits the sequential nature of the online problem via the Markov Decision Process framework. In a case study in energy management, we show the effectiveness of our hybrid approaches, w.r.t. the state-of-the-art and pure RL methods. The combination proves capable of faster convergence and naturally handles constraint satisfaction.'

# Summary. An optional shortened abstract.
summary: Reinforcement learning tunes the battery costs of a fast greedy energy manager and can beat optimality-condition tuning in similar time, without a convex solver.

tags:
- reinforcement learning
- offline/online optimization
- energy management
- constrained optimization
- uncertainty
topics: [sustainability]

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
  url: https://doi.org/10.1007/978-3-031-08011-1_24
categories:
  - Conference
aliases:
  - /publication_conferences/silvestri-etal-2022-hybrid-offline/
# Key in data/venues.yaml, whose rank decides the Highlights carousel
venue_key: cpaior
---
