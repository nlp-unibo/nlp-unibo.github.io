---
title: 'Sustainable Italian LLM Evaluation: Community Perspectives and Methodological
  Guidelines'

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- Luca Moroni
- Gianmarco Pappacoda
- Edoardo Barba
- Simone Conia
- Andrea Galassi
- Bernardo Magnini
- Roberto Navigli
- Paolo Torroni
- Roberto Zanoli

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2025-09-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2026-03-02T12:28:22.191705Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- paper-conference

# Publication name and optional abbreviated publication name.
publication: '*Proceedings of the Eleventh Italian Conference on Computational Linguistics
  (CLiC-it 2025)*'
publication_short: ''

doi: ''

abstract: 'The evaluation of large language models for Italian faces unique challenges due to morphosyntactic complexity, dialectal variation, cultural-specific knowledge, and limited availability of computational resources. This position paper presents a comprehensive framework for Italian LLM benchmarking, in which we identify key dimensions for LLM evaluation, including linguistic capabilities, knowledge domains, task types and prompt variations, proposing high-level methodological guidelines for current and future initiatives. We advocate a community-driven, sustainable benchmarking initiative that incorporates dynamic dataset management, open model prioritization, and collaborative infrastructure utilization. Our framework aims to establish a coordinated effort within the Italian NLP community to ensure rigorous, scientifically sound evaluation practices that can adapt to the evolving landscape of Italian LLMs.'

# Summary. An optional shortened abstract.
summary: 'A community roadmap for evaluating Italian LLMs: what to test, how to test it, where to find data, and how to keep benchmarking sustainable.'

tags:
- benchmarking
- italian language
- large language models
- evaluation methodology
- position paper

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
  caption: 'The three-dimensional framework for Italian LLM evaluation: linguistic competence, domain and knowledge, and task generalization (Figure 1 of the paper).'
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
  url: https://aclanthology.org/2025.clicit-1.71/
categories:
  - Conference
aliases:
  - /publication_conferences/moroni-etal-2025-sustainable/
topics: [llms, benchmark, sustainability]
---

## Research setting

A large language model (LLM) is a neural network trained on large amounts of text that answers questions and follows instructions in natural language.
Benchmarking an LLM means running it on tasks with known answers and scoring its outputs, so that models can be compared over time.
Several LLMs trained for Italian have appeared recently.
This position paper does not test a new model. It collects the experience of three Italian research groups and proposes how the community should evaluate these models.

{{< pipeline caption="One benchmark item, built from the multiple-choice example in Section 3.1 of the paper: the model must tell which Milano a sentence refers to." >}}
- title: Task item
  text: "Marco Rossi è nato a Milano nel 1985. Which Milano?"
  icon: file-alt
- title: Prompt
  text: The item with four options, from Milano, Texas to Milano, Italy.
  icon: list-ul
- title: LLM
  text: The model under evaluation.
  icon: robot
  highlight: true
- title: Answer
  text: The model outputs one option letter, here B.
  icon: comment
- title: Score
  text: The answer is compared with the correct option.
  icon: check
{{< /pipeline >}}

Terms used on this page:

- **Native benchmark**: a benchmark written directly in Italian, as opposed to one **translated** from English.
- **Probability-based evaluation** reads the probability that the model gives to each predefined answer option and takes the most likely one as its choice.
- **Generative evaluation** lets the model write a free-form answer and then checks that answer against criteria or a reference.
- **LLM-as-a-Judge** is a generative evaluation in which another LLM grades the free-form answers.
- **Zero-shot** and **few-shot** prompting give the model no solved examples or a few solved examples before the question.
- A benchmark is **saturated** when the best models solve it almost fully, so it no longer separates them.

## Motivation

Italian has rich inflection, a flexible word order, clitic pronouns, dropped subjects, and many regional varieties.
A direct translation of English benchmarks cannot capture these features, nor Italian culture and institutions.
Recent Italian LLM benchmarks are valuable.
They are also isolated efforts, with limits in methodology, scope, sustainability, and coordination.
The paper maps them onto its own evaluation framework and finds whole skill areas that no one tests.

{{< gap caption="Coverage of six evaluation dimensions by three Italian LLM evaluation frameworks, from Table 1 of the paper. Ling. instructions is linguistic instruction following, Task gen. is task generalization, and Cross-ling. is cross-linguistic transfer. For this paper, a check means that its framework defines the dimension: the paper itself releases no dataset." >}}
label: Framework
columns: [Morphology, Pragmatics, Register, Ling. instructions, Task gen., Cross-ling.]
rows:
  - name: ITA-Bench
    cells: [false, true, false, false, false, true]
  - name: Evalita-LLM
    cells: [false, true, false, true, false, false]
  - name: ITALIC
    cells: [true, false, false, false, false, false]
  - name: This paper
    ours: true
    cells: [true, true, true, true, true, true]
{{< /gap >}}

> **Objective.** Give the Italian NLP community a shared framework and practical guidelines for evaluating Italian LLMs, and a plan to keep that evaluation running over time.

## Approach

The paper organizes its guidelines around four questions.
The first question sets the skills to test, through the three dimensions shown in the figure at the top of this page.
The other three questions cover how to run a test, where to get the data, and how to keep the whole effort alive.

{{< pipeline caption="The four questions of the paper (Sections 2 to 5). The last one is the community plan that gives the paper its title." >}}
- title: What to benchmark
  text: Linguistic competence, domain and knowledge, task generalization.
  icon: sitemap
- title: How to benchmark
  text: Task format, scoring strategy, and prompt variations.
  icon: sliders-h
- title: Where to benchmark
  text: Translated, adapted, or native Italian data.
  icon: database
- title: Sustainable benchmarking
  text: A living benchmark run by the community.
  icon: recycle
  highlight: true
{{< /pipeline >}}

| Question | Main guideline of the paper |
|---|---|
| What | Task designers state which dimensions their task covers, so effort goes to the dimensions that few tasks test. |
| How: format | Multiple-choice questions are cheap and simple to score but far from real use. Open-ended generation is closer to real use but harder and costlier to score. |
| How: prompting | Zero-shot evaluation is the main measure. Few-shot prompting serves as a supplementary variation and a strong baseline. |
| How: variation | Prompts vary in register, explicitness, cultural framing, and random changes such as the order of options, to test robustness. |
| Where | Native development comes first for tasks that are critical for Italian. Translation and adaptation fill the remaining gaps. |
| Sustainable | Saturated or stale tasks leave the benchmark, and open models come first. Each model is reported with its parameters and training tokens. A rotating steering committee governs the effort, which runs on national compute such as CINECA's Leonardo supercomputer. |

*Guidelines from Sections 2 to 5 of the paper.*

## Results

The paper reports no new model experiments.
Its findings come from three sources: a coverage analysis of public datasets against the framework (Table 1), the authors' experience with Italian benchmarks, and a preliminary cost analysis.

{{< numbers >}}
- value: "25 + 3"
  label: public datasets and evaluation frameworks mapped onto the framework
- value: "3-5x"
  label: more compute for generative evaluation than for probability-based evaluation
- value: "500-750"
  label: GPU hours per quarter to evaluate 10 models on 50 tasks
{{< /numbers >}}

{{< figure src="coverage.png" caption="Coverage of 25 public datasets and 3 frameworks (ITA-Bench, Evalita-LLM, and ITALIC) by the dimensions of the framework. A check means covered, a cross means not covered (Table 1 of the paper)." >}}

Almost every dataset tests semantics, and many test lexical knowledge or a knowledge domain.
No dataset or framework in the table tests register adaptation or task generalization, and only ITA-Bench tests cross-linguistic transfer.
The paper calls for more tasks on pragmatics, register, and cross-linguistic transfer.

Translation can also change what a task measures.
In the Italian version of a WinoGrande item, grammar alone gives the answer away, because GPS is masculine and mappa (map) is feminine.

{{< annotate caption="A WinoGrande item translated into Italian, from Section 4 of the paper. The correct answer is mappa. The highlighted feminine forms rule out GPS without any common sense." >}}
labels: [Candidate, Feminine]
segments:
  - text: "Il"
  - text: "GPS"
    label: Candidate
  - text: "e la"
  - text: "mappa"
    label: Candidate
  - text: "mi hanno aiutato a tornare a casa. Mi sono perso quando"
  - text: "la"
    label: Feminine
  - text: "___ è"
  - text: "stata capovolta."
    label: Feminine
{{< /annotate >}}

Two more observations come from the authors' experience.
Italian models often perform better when prompted in English with the instruction to answer in Italian. This suggests that they benefit from higher-quality English training data.
For scoring free-form answers, no open-weight LLM-as-a-Judge model is trained explicitly for Italian yet.

## Takeaways

{{< takeaways >}}
- title: Know what a benchmark measures.
  text: Mapping each task onto the three dimensions of the framework shows the skills that Italian benchmarks miss, such as register adaptation.
- title: Translation is not enough.
  text: A translated task can lose difficulty or cultural content. Native Italian tasks matter most for cultural knowledge, idioms, and pragmatic language use.
- title: Benchmarks need to stay alive.
  text: A living benchmark retires saturated tasks and puts open models first. Run on national compute under community governance, it can keep Italian evaluation rigorous over time.
{{< /takeaways >}}
