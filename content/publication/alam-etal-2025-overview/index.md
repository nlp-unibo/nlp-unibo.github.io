---
title: 'Overview of the CLEF-2025 CheckThat! Lab: Subjectivity, fact-checking, claim
  normalization, and retrieval'

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- Firoj Alam
- Julia Maria Struß
- Tanmoy Chakraborty
- Stefan Dietze
- Salim Hafid
- Katerina Korre
- Arianna Muti
- Preslav Nakov
- Federico Ruggeri
- Sebastian Schellhammer
- Vinay Setty
- Megha Sundriyal
- Konstantin Todorov
- V. Venktesh

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2025-01-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2026-02-27T15:55:09.456639Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- paper-conference

# Publication name and optional abbreviated publication name.
publication: '*Experimental IR Meets Multilinguality, Multimodality, and Interaction - 16th International Conference of the CLEF Association, CLEF 2025*'
publication_short: ''

doi: 10.1007/978-3-032-04354-2_13

abstract: >-
  This paper presents the eighth edition of the CheckThat! lab, part of the 2025
  Conference and Labs of the Evaluation Forum (CLEF). As in previous editions of
  CheckThat!, the lab offers tasks from the core of the verification pipeline,
  including check-worthiness, identifying previously fact-checked claims, supporting
  evidence retrieval, and claim verification as well as auxiliary tasks addressing
  different facets of individual steps of the pipeline: Task 1 is on identification
  of subjectivity (a follow-up of the CheckThat! 2024 edition), which is related to
  the check-worthiness task, Task 2 is on claim normalization, Task 3 addresses
  fact-checking numerical claims, and Task 4 focuses on scientific web discourse
  processing. These challenging classification and retrieval problems are offered
  in different mono-, multi- and crosslingual settings covering more than 20
  languages. This year, CheckThat! was one of the most popular labs at CLEF-2025 in
  terms of team registrations: 177 teams registered, almost half of them actually
  participating (a total of 83 teams) and 54 submitted system description papers.

# Summary. An optional shortened abstract.
summary: CheckThat! 2025 ran four shared tasks that help fact-checkers, from subjectivity detection to numerical claim verification, with 83 teams and more than 20 languages.

tags:
- CLEF
- shared task
- subjectivity detection
- claim normalization
- numerical claims
- scientific web discourse

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
  caption: 'The four core stages of the fact-checking pipeline and the 2025 tasks attached to them, redrawn after Figure 1 of the paper.'
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
  - /publication_workshops/alam-etal-2025-overview/
topics: [fact-checking, information-retrieval, benchmark]
---

## Research setting

Fact-checkers decide whether a claim is true, and much of their work can be supported by language technology.
CheckThat! is an evaluation lab at CLEF, the Conference and Labs of the Evaluation Forum.
Each year it runs shared tasks: the organizers release a dataset, teams build systems for it, and every system is scored on the same test data.
The tasks follow the verification pipeline below, plus auxiliary tasks that support its stages.

{{< pipeline caption="The four core stages of the verification pipeline, as described in Section 1 and Figure 1 of the paper." >}}
- title: Check-worthiness estimation
  text: Decide whether a statement deserves to be checked.
  icon: filter
- title: Verified claim retrieval
  text: Find claims that fact-checkers have already verified.
  icon: history
- title: Supporting evidence retrieval
  text: Collect evidence about the claim from the Web.
  icon: search
- title: Claim verification
  text: Decide whether the claim is true or false.
  icon: balance-scale
{{< /pipeline >}}

## Motivation

Claims rarely arrive as clean, neutral sentences.
They hide in subjective text and in noisy social media posts, they rest on numbers, or they point to scientific studies without citing them.
Up to 2022 the lab mainly focused on the core stages; the 2023 and 2024 editions added auxiliary tasks such as subjectivity.
The 2025 edition adds three new tasks for these harder inputs and covers more languages than any earlier edition.

{{< gap caption="How the 2025 edition relates to the earlier editions of the lab (Section 2, Table 1, and Section 6 of the paper)." >}}
label: Edition
columns: [Subjectivity, Claim normalization, Numerical claims, Scientific web discourse, 20 languages or more]
rows:
  - name: 2018 to 2020 (core verification pipeline)
    cells: [false, false, false, false, false]
  - name: 2021 and 2022 (multilinguality, fake news detection)
    cells: [false, false, false, false, false]
  - name: 2023 and 2024 (subjectivity, bias, authority finding, persuasion)
    cells: [true, false, false, false, false]
  - name: This paper (2025 edition)
    ours: true
    cells: [true, true, true, true, true]
{{< /gap >}}

> **Objective.** Offer four tasks that support different stages of the verification pipeline, with datasets in mono-, multi-, and cross-lingual settings. Then compare the systems of the participating teams.

## Approach

Each task has its own dataset with training, development, and test splits.
A zero-shot setting means that a test language has no training data, so systems must transfer what they learned from other languages.
Teams submit runs, which are sets of predictions on the test data.
Each task scores the runs with its own metric.

{{< pipeline caption="How the 2025 lab ran (Sections 3 to 5 of the paper)." >}}
- title: Four tasks
  text: Each task supports one stage of the pipeline.
  icon: tasks
  highlight: true
- title: Datasets
  text: Training, development, and test splits.
  icon: database
- title: Runs
  text: Teams submit predictions on the test data.
  icon: users
- title: Scoring
  text: Each task scores the runs with its own metric.
  icon: sort-amount-down
{{< /pipeline >}}

| Task | Input | Output | Languages | Metric |
|---|---|---|---|---|
| T1 Subjectivity | A sentence from a news article | Subjective or objective | Arabic, Bulgarian, English, German, Italian, multilingual; zero-shot: Greek, Polish, Romanian, Ukrainian | Macro F1 |
| T2 Claim normalization | A social media post | A clear, verifiable statement, the normalized claim | 13 with training data, 7 zero-shot | METEOR |
| T3 Numerical claims | A claim with numbers or dates, plus the top 100 pieces of evidence | True, False, or Conflicting | English, Spanish, Arabic | Macro F1 |
| T4a Scientific web discourse detection | A post from X | Any of: a scientific claim, a reference to a study, a mention of a scientific entity | Not stated | Macro F1 |
| T4b Claim-source retrieval | A post that mentions a paper without a link | The mentioned paper among 7,718 CORD-19 papers | Not stated | MRR@5 |

*The 2025 tasks. Source: Sections 3 and 4 of the paper.*

## Results

Each task was scored on its own test data.
Macro F1 averages the F1 score over the classes, from 0 to 1.
METEOR, from 0 to 1, measures how close a generated claim is to the reference claim.
MRR@5 rewards a system that ranks the right paper high among its top five answers, from 0 to 1.
The baselines include BM25, a classic keyword-based ranking method.

{{< numbers >}}
- value: "83"
  label: teams took part, out of 177 registered, and 54 wrote system papers
- value: "20+"
  label: languages across the four tasks
- value: "0.68"
  label: best MRR@5 in claim-source retrieval, against 0.43 for the BM25 baseline
{{< /numbers >}}

{{< bars caption="Best macro F1 per language in Task 1. Greek, Polish, Romanian, and Ukrainian are zero-shot languages. Source: Table 6 of the paper." >}}
metric: Best macro F1 in Task 1 (subjectivity)
unit: ""
min: 0
max: 1
bars:
  - label: Arabic
    value: "0.6884"
  - label: English
    value: "0.8052"
  - label: German
    value: "0.8520"
  - label: Italian
    value: "0.8104"
  - label: Multilingual
    value: "0.7550"
  - label: Greek (zero-shot)
    value: "0.5067"
  - label: Polish (zero-shot)
    value: "0.6922"
  - label: Romanian (zero-shot)
    value: "0.8126"
  - label: Ukrainian (zero-shot)
    value: "0.6424"
{{< /bars >}}

| Task | Teams | Metric | Best score | Baseline |
|---|---|---|---|---|
| T1 Subjectivity, English | 21 | Macro F1 | 0.8052 | Not reported |
| T2 Claim normalization, English | 18 | METEOR | 0.4569 | Not reported |
| T3 Numerical claims, English | 13 | Macro F1 (0 to 100) | 59.54 | Not reported |
| T4a Scientific web discourse detection | 10 | Macro F1 | 0.7998 | 0.7668 (DeBERTa-v3) |
| T4b Claim-source retrieval | 30 | MRR@5 | 0.68 | 0.43 (BM25) |

*Participating teams and best score per task. Teams count every language of a task. Source: Sections 5.1 to 5.4 and Tables 6, 9, 11, and 12 of the paper.*

Most teams fine-tuned pretrained transformer language models, and some also prompted or fine-tuned large language models (LLMs).
For subjectivity, the best scores in the zero-shot languages vary widely, from 0.5067 in Greek to 0.8126 in Romanian.
For numerical claims, most teams used LLMs to decompose each claim into simpler parts, retrieved evidence with BM25, and re-ranked it.
For claim-source retrieval, most teams combined keyword-based (sparse) or embedding-based (dense) retrieval with re-ranking, and LLM re-rankers did not always beat fine-tuned transformers.

## Takeaways

{{< takeaways >}}
- title: Fact-checking needs more than the core pipeline.
  text: Subjective sentences, noisy posts, numbers, and informal references to science each call for their own task.
- title: Multilingual coverage keeps growing.
  text: The 2025 edition covered more than 20 languages, and zero-shot settings test languages that have no training data.
- title: Retrieval plus re-ranking is the common recipe.
  text: In claim-source retrieval, the best team reached 0.68 MRR@5 against 0.43 for BM25, and most teams paired retrieval with a re-ranker.
{{< /takeaways >}}
