---
title: News
intro: "What is new in the lab: papers and preprints, the workshops and shared tasks we organize, and our calls for papers."

# The page is drawn by layouts/news/list.html as a timeline grouped by year. Every publication joins the
# timeline as a Paper or Preprint item on its publication date, so a new publication needs no news item.

# A news item has no page of its own: its preview shows the summary and the links of its body. Attachments such as
# program.pdf are still published next to where the page would be, so their links keep working.
cascade:
  - build:
      render: never
      list: always
      publishResources: true
    target:
      kind: page

# Events were merged into News. The former event pages and news pages redirect here.
aliases:
  - /events/
  - /events/2023clef/
  - /events/2024clef/
  - /events/2025clef/
  - /news/alma-ai/
  - /news/aminlaw-si-2026/
  - /news/argmining2026/
  - /news/equal/
  - /news/icail2026/
  - /news/ijcai2026/
  - /news/prima/
  - /news/tacl2026/
---
