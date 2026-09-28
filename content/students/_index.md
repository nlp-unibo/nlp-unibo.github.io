---
title: For Students
type: landing

aliases:
  - /students_publications/

# Listing view
view: compact

# Optional banner image (relative to `assets/media/` folder).
banner:
  caption: ''
  image: ''

# Page sections
sections:
  - block: markdown
    id: proposals
    content:
      title: Research Proposals
      text: '{{< section-cards "proposals" >}}'
    design:
      columns: '1'
  - block: collection
    content:
      title: Publications
      text: ""
      filters:
        tag: "student publication"

    design:
      view: citation
      columns: '1'
  - block: collection
    content:
      title: Master Theses
      text: ""
      filters:
        folders:
          - theses
        category: Master thesis
    design:
      view: citation
      columns: '1'
  - block: collection
    content:
      title: Bachelor Theses
      text: ""
      filters:
        folders:
          - theses
        category: Bachelor thesis
    design:
      view: citation
      columns: '1'
  - block: collection
    id: challenges
    content:
      title: International contests, benchmarks, and challenges
      text: "There are many other international challenges held every year. Developing models and techniques to tackle past or ongoing challenges may be good proposals for project works."
      filters:
        folders:
          - opportunities
        category: Challenge
    design:
      view: masonry
      columns: '1'
  - block: collection
    id: workshops
    content:
      title: Workshops
      text: "Academic workshops discussing topics and proposing shared tasks of our interest."
      filters:
        folders:
          - opportunities
        category: Academic workshop
    design:
      view: masonry
      columns: '1'
---

