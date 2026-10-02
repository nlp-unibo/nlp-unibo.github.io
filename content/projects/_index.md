---
title: Projects
date: 2026-02-27

type: landing

# The `categories` value of each project is `International project` or `National project`.
aliases:
  - /projects_international/
  - /projects_national/

# Project cards show no date and link straight to the project website in `external_link`,
# so each project page only redirects to that website.
cascade:
  - params:
      show_date: false
  - type: redirect
    sitemap:
      disable: true
    target:
      kind: page

sections:
  - block: collection
    content:
      title: International Projects
      text: ""
      count: 0
      filters:
        folders:
          - projects
        category: International project
    design:
      view: card
      columns: '1'
  - block: collection
    content:
      title: National Projects
      text: ""
      count: 0
      filters:
        folders:
          - projects
        category: National project
    design:
      view: card
      columns: '1'
---