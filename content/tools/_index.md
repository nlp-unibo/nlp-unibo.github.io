---
title: Tools
date: 2026-02-02

view: card

# Tool cards show no date and link straight to the tool website in `external_link`,
# so each tool page only redirects to that website.
cascade:
  - params:
      show_date: false
  - type: redirect
    sitemap:
      disable: true
    target:
      kind: page
---