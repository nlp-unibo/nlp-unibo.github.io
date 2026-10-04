---
# Leave the homepage title empty to use the site title
title:
date: 2026-02-26
type: landing

# Blocks named lt-* live in layouts/_partials/blocks/.
sections:
  - block: lt-hero
    id: section-hero
    content:
      eyebrow: Language Technologies Lab · University of Bologna
      title: Teaching machines to reason with *language*
      text: We build interpretable models of argumentation that adapt to specialised domains, from legal texts to multimodal data.
      # A button whose page is unpublished, such as a draft, is not shown.
      buttons:
        - text: Work with us
          url: /work-with-us/
  - block: lt-research
    id: research
    content:
      title: Research
      threads_text: The same questions return in every area. Each dot marks an area where we work on that thread.
      more:
        text: All research
        url: /research/
  - block: lt-news
    id: news
    content:
      eyebrow: News
      title: Latest from the lab
      count: 6
      featured: 3
      more:
        text: All news
        url: /news/
  - block: lt-preprints
    id: preprints
    content:
      eyebrow: Preprints
      title: Latest preprints
      subtitle: Our newest papers, openly available on arXiv.
      count: 3
      more:
        text: All publications
        url: /publication/
---
