---
title: Publications
type: landing

# Every publication lives in content/publication/<slug>/.
# Its `categories` value selects exactly one list below.
aliases:
  - /publication_highlights/
  - /publication_journals/
  - /publication_conferences/
  - /publication_workshops/
  - /publication_preprints/

# Listing view
view: citation

# Page sections
sections:
  - block: collection
    content:
      count: 0
      title: Highlights
      text: ""
      filters:
        folders:
          - publication
        category: Highlight
    design:
      view: citation
      css_class: lt-no-years
      columns: '1'
  - block: collection
    content:
      title: Journals
      text: ""
      filters:
        folders:
          - publication
        category: Journal
    design:
      view: citation
      columns: '1'
  - block: collection
    content:
      title: Conferences
      text: ""
      filters:
        folders:
          - publication
        category: Conference
    design:
      view: citation
      columns: '1'
  - block: collection
    content:
      title: Workshops
      text: ""
      filters:
        folders:
          - publication
        category: Workshop
    design:
      view: citation
      columns: '1'
  - block: collection
    content:
      title: Preprints
      text: ""
      filters:
        folders:
          - publication
        category: Preprint
    design:
      view: citation
      columns: '1'
---
