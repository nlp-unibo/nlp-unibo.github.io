---
title: 'Overview of the CLEF-2024 CheckThat! lab: check-worthiness, subjectivity,
  persuasion, roles, authorities, and adversarial robustness'

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- Alberto Barrón-Cedeño
- Firoj Alam
- Julia Maria Struß
- Preslav Nakov
- Tanmoy Chakraborty
- Tamer Elsayed
- Piotr Przybyła
- Tommaso Caselli
- Giovanni Da San Martino
- Fatima Haouari
- Maram Hasanain
- Chengkai Li
- Jakub Piskorski
- Federico Ruggeri
- Xingyi Song
- Reem Suwaileh

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2024-01-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2026-02-27T15:55:09.461038Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- paper-conference

# Publication name and optional abbreviated publication name.
publication: '*Experimental IR Meets Multilinguality, Multimodality, and Interaction - 15th International Conference of the CLEF Association, CLEF 2024*'
publication_short: ''

doi: 10.1007/978-3-031-71908-0_2

abstract: >-
  We describe the seventh edition of the CheckThat! lab, part of the 2024
  Conference and Labs of the Evaluation Forum (CLEF). Previous editions of
  CheckThat! focused on the main tasks of the information verification pipeline:
  check-worthiness, identifying previously fact-checked claims, supporting
  evidence retrieval, and claim verification. In this edition, we introduced some
  new challenges, offering six tasks in fifteen languages (Arabic, Bulgarian,
  English, Dutch, French, Georgian, German, Greek, Italian, Polish, Portuguese,
  Russian, Slovene, Spanish, and code-mixed Hindi-English): Task 1 on estimation
  of check-worthiness (the only task that has been present in all CheckThat!
  editions), Task 2 on identification of subjectivity (a follow up of the
  CheckThat! 2023 edition), Task 3 on identification of the use of persuasion
  techniques (a follow up of SemEval 2023), Task 4 on detection of hero, villain,
  and victim from memes (a follow up of CONSTRAINT 2022), Task 5 on rumor
  verification using evidence from authorities (new task), and Task 6 on
  robustness of credibility assessment with adversarial examples (new task).
  These are challenging classification and retrieval problems at the document and
  at the span level, including multilingual and multimodal settings. This year,
  CheckThat! was one of the most popular labs at CLEF-2024 in terms of team
  registrations: 130 teams. More than one-third of them (a total of 46) actually
  participated.

# Summary. An optional shortened abstract.
summary: CheckThat! 2024 ran six shared tasks for fact-checking, from check-worthiness to adversarial attacks, in fifteen languages with 46 participating teams.

tags:
- CLEF
- shared task
- check-worthiness
- subjectivity detection
- persuasion techniques
- adversarial examples

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
  caption: 'The four core stages of the fact-checking pipeline and the six 2024 tasks attached to them, redrawn after Figure 1 of the paper.'
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
  - /publication_workshops/barron-etal-20240-overview/
topics: [fact-checking, benchmark]
---

## Research setting

Fact-checkers decide whether a claim is true, and language technology can support many steps of their work.
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

The first five editions of the lab focused on the core stages of the pipeline.
From 2023, the lab also opened to auxiliary tasks that help each stage.
Claims also hide in subjective sentences, in persuasive news, and in memes.
A classifier that flags misinformation can itself be fooled.
The 2024 edition adds tasks for these cases, and three of its six tasks ran for the first time.

{{< gap caption="How the 2024 edition relates to the earlier editions of the lab (Sections 1 to 3 and Table 1 of the paper). Partial: the 2023 edition asked to find authorities. It did not ask to retrieve evidence from them." >}}
label: Edition
columns: [Check-worthiness, Subjectivity, Persuasion, Meme roles, Authority evidence, Adversarial attacks]
rows:
  - name: 2018 to 2020
    cells: [true, false, false, false, false, false]
  - name: 2021 and 2022
    cells: [true, false, false, false, false, false]
  - name: '2023'
    cells: [true, true, false, false, "partial", false]
  - name: This paper (2024)
    ours: true
    cells: [true, true, true, true, true, true]
{{< /gap >}}

> **Objective.** Offer six tasks that support different steps of the verification pipeline, in mono-, multi-, and cross-lingual settings over fifteen languages. Then compare the systems of the participating teams.

## Approach

Each task has its own dataset, mostly with training, development, and test splits.
Teams submit runs, which are sets of predictions on the test data.
Each task scores the runs with its own metric and compares them with a baseline, a simple reference system built by the organizers.
In Task 6 the roles change: teams attack victim models, which are classifiers that detect misinformation.
An adversarial example is a text changed slightly so that the victim model changes its decision while the meaning stays the same.

{{< pipeline caption="How the 2024 lab ran (Sections 3 to 5 of the paper)." >}}
- title: Six tasks
  text: Each task supports one step of the pipeline.
  icon: tasks
  highlight: true
- title: Datasets
  text: Training, development, and test data per language.
  icon: database
- title: Runs
  text: Teams submit predictions on the test data.
  icon: users
- title: Scoring
  text: Each task scores the runs against a baseline.
  icon: sort-amount-down
{{< /pipeline >}}

| Task | Input | Output | Test languages | Metric |
|---|---|---|---|---|
| T1 Check-worthiness | A statement from a tweet, a transcript, or a political debate | Whether it needs fact-checking | Arabic, Dutch, English | F1 of the check-worthy class |
| T2 Subjectivity | A sentence from a news article | Subjective or objective | Arabic, Bulgarian, English, German, Italian, multilingual | Macro F1 |
| T3 Persuasion techniques | A news article | Text spans that use one of 23 persuasion techniques | Arabic, Bulgarian, English, Portuguese, Slovene | Micro F1 with partial span matching |
| T4 Roles in memes | A meme and an entity in it | Hero, villain, victim, or other | Bulgarian, English, code-mixed Hindi-English | F1 |
| T5 Evidence from authorities | A rumor in a tweet and the timelines of authorities, the sources that know the matter | Evidence tweets, then supported, refuted, or unverifiable | Arabic, English | MAP, macro F1 |
| T6 Adversarial robustness | A text and a victim model | An adversarial example | Not stated | BODEGA score |

*The 2024 tasks. Source: Sections 3, 4, and 5 of the paper.*

## Results

Each task was scored on its own test data, against its own baseline.
F1 combines precision and recall, from 0 to 1, and macro F1 averages it over the classes.
MAP (mean average precision), from 0 to 1, rewards a system that ranks the evidence tweets high in its list.
The BODEGA score, from the framework of the same name, rates adversarial examples automatically, and Task 6 also checked a sample by hand.

{{< numbers >}}
- value: "46"
  label: teams took part, out of 130 registered
- value: "15"
  label: languages across the six tasks
- value: "0.879"
  label: best macro F1 in English rumor verification, against 0.495 for the baseline
{{< /numbers >}}

| Task | Teams | Metric | Best score | Baseline |
|---|---|---|---|---|
| T1 Check-worthiness, English | 26 | F1 of the check-worthy class | 0.802 | Not reported |
| T2 Subjectivity, English | 15 (all languages) | Macro F1 | 0.744 | Not reported |
| T3 Persuasion techniques, English | 2 (all languages) | Micro F1 | 0.092 | 0.009 |
| T4 Roles in memes | 0 | F1 | No runs | 0.58 |
| T5 Evidence retrieval, English | 5 | MAP | 0.604 | 0.335 |
| T5 Rumor verification, English | 5 | Macro F1 | 0.879 | 0.495 |
| T6 Adversarial robustness | 6 | BODEGA score | 0.7458 | 0.4261 (BERT-ATTACK, an earlier attack method) |

*Participating teams and best official score per task. Source: Sections 5.1 to 5.6 and Tables 5, 7, 10, 12, 14, and 15 of the paper. The best Task 5 retrieval run came from a team of the task organizers.*

Most teams fine-tuned pretrained transformer models, and many also used large language models (LLMs).
In Task 5, systems fine-tuned on the task data retrieved evidence best, but only the two LLM-based systems beat the baseline in English rumor verification.
Task 4 attracted no participants, so only its baseline is available.
Task 6 shows a gap between automatic and manual evaluation, as the chart below shows.

{{< bars caption="Share of adversarial examples whose meaning annotators judged preserved. Each team had 100 successful examples from the fact-checking domain of Task 6. The two top teams of the automatic BODEGA ranking (OpenFact, TextTrojaners) score lowest here. Source: Section 5.6 of the paper." >}}
metric: Adversarial examples with preserved meaning (manual check)
unit: "%"
min: 0
max: 100
bars:
  - label: SINAI
    value: "99"
  - label: MMU_NLP
    value: "96"
  - label: TurQUaz
    value: "62"
  - label: Palöri
    value: "14"
  - label: OpenFact
    value: "11"
  - label: TextTrojaners
    value: "7"
{{< /bars >}}

## Takeaways

{{< takeaways >}}
- title: The lab grew beyond the core pipeline.
  text: Six tasks in fifteen languages cover subjectivity, persuasion, memes, authorities, and adversarial attacks next to check-worthiness.
- title: LLMs helped most in rumor verification.
  text: In English, the two LLM-based systems were the only ones above the baseline, with a best macro F1 of 0.879 against 0.495.
- title: Automatic scores can mislead.
  text: In Task 6, annotators preferred attacks based on homoglyphs, characters that look alike, while the automatic score ranked other methods first.
{{< /takeaways >}}
