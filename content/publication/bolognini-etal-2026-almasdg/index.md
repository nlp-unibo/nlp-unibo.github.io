---
title: 'AlmaSDG: A Dataset of Scientific Articles'' Contributions to the UN Sustainable Development Goals'
authors:
- Luca Bolognini
- Elena Palmieri
- nicolo-donati
- Giulia Grundler
- Gianmarco Pappacoda
- Federico Ruggeri
- Andrea Galassi
- Paolo Torroni
author_notes: []
date: '2026-06-09'
publishDate: '2026-10-13'
publication_types:
- article-journal
publication: Scientific Data
publication_short: ''
venue_key: scientific-data
doi: 10.1038/s41597-026-07452-4
abstract: The UN Agenda 2030 motivates the development of scalable methods and tools for assessing the contribution of research
  and higher education institutions to sustainable development. Current research efforts suffer from the lack of rigorous
  evaluation benchmarks. This paper describes a collaborative work with sustainability experts aimed at constructing AlmaSDG,
  the first pilot dataset of scientific articles labeled by multiple annotators along all SDGs. AlmaSDG is validated using
  inter-annotator agreement and inference of pre-trained models and tools.
summary: AlmaSDG labels 139 scientific articles against all 17 UN Sustainable Development Goals, a human-annotated benchmark
  for tools that map research to the goals.
card_summary: ''
card_caption: 'How AlmaSDG was built and validated: article selection, annotation by four pairs of annotators, and two validations.
  Drawn from the Methods and Technical Validation sections of the paper.'
tags:
- dataset
- sustainable development goals
- scientific papers
- annotation guidelines
- inter-annotator agreement
featured: false
url_pdf: ''
url_code: ''
url_dataset: https://zenodo.org/records/19606053
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''
image:
  caption: ''
  focal_point: ''
  preview_only: false
projects: []
categories:
- Journal
affiliations: []
topics:
- sustainability
- annotation
focus: []
---

## Research setting

The UN Sustainable Development Goals (SDGs) are 17 goals adopted in 2015 by 193 UN states, such as no poverty, gender equality, and climate action.
Universities and research institutions want to know which of their articles contribute to which goal.
The paper frames this as multi-label document classification.
The input is the title, abstract, and keywords of a scientific article.
The output is one yes or no label for each of the 17 SDGs.
An article can contribute to several goals at once, or to none.

{{< figure src="example.png" caption="An input document of AlmaSDG and its positive labels: SDGs 7, 9, 11, and 13. The other 13 labels of this article are negative. Source: Figure 1 of the paper (CC BY 4.0)." >}}

## Motivation

Tools that map research to the SDGs already exist, but there is no gold standard to evaluate how accurate they are.
There is also no shared definition of what it means for an article to contribute to an SDG.
Existing SDG datasets are labeled automatically by queries, by crowd workers who see one goal at a time, or by the authors of the documents themselves.
Single-label data can miss an article's contribution to other goals and count it as a negative.

{{< gap caption="How AlmaSDG relates to the SDG datasets discussed in the paper (Background and Table 2 of the paper)." >}}
label: Dataset
columns: [Scientific publications, Several SDGs per document, Labeled by humans, Several annotators per document, Written guidelines and agreement reported]
rows:
  - name: Aurora Queries (1.4m documents)
    cells: [true, true, false, false, false]
  - name: Aurora Survey (10,682)
    cells: [true, "Mostly one", true, "Mostly one", false]
  - name: OSDG (41,689)
    cells: ["partial", false, "Crowd", "At least 3", false]
  - name: SDG Knowledge Hub (9,172)
    cells: [false, true, "Authors", "Author and editors", false]
  - name: SDG Academy (900)
    cells: [false, true, "Authors", "Not described", false]
  - name: This paper (AlmaSDG, 139)
    ours: true
    cells: [true, true, true, true, true]
{{< /gap >}}

> **Objective.** Define annotation guidelines that say when a scientific article contributes to an SDG, use them to build a dataset labeled by multiple annotators on all 17 SDGs, and validate it with agreement measures and existing models and tools.

## Approach

AlmaSDG is the result of a 12-month joint effort of stakeholders, academic experts in SDGs, and computer scientists.
A first pilot showed that the official SDG targets are too specific and too open to interpretation to serve as annotation instructions.
With five academic experts in sustainability, the team wrote new guidelines.
A direct contribution studies, develops, or applies methods and technologies.
An indirect contribution lays the groundwork for them, for example with a review or new data.
A cursory mention of an SDG topic is not a contribution.
The guidelines list 165 contribution areas across the 17 SDGs, with positive and negative examples.

{{< pipeline caption="How AlmaSDG was built (Methods section of the paper). Each of the four pairs labels all 139 articles on its own 4 or 5 SDGs." >}}
- title: Write guidelines
  text: Direct and indirect contributions, 165 contribution areas.
  icon: book
- title: Pick articles
  text: 139 articles from the University of Bologna repository.
  icon: search
- title: Label in pairs
  text: 8 annotators in 4 pairs; one yes or no per SDG.
  icon: user-edit
  highlight: true
- title: Measure, then resolve
  text: Agreement per SDG, then pairs discuss each disagreement.
  icon: comments
{{< /pipeline >}}

The source is a publication repository of the University of Bologna, chosen because large databases cover the humanities less than the sciences.
A random sample would contain mostly negative articles.
Instead, the team queried the repository with fragments of the SDG descriptions and kept 139 articles that look relevant, trying to cover all goals.
Eight NLP researchers formed four pairs, and each pair labeled all 139 articles on its own subset of 4 or 5 SDGs.
Each annotator worked independently, and each pair then discussed its disagreements to fix the final labels.

## Results

The paper validates the dataset in two ways.
First, it measures inter-annotator agreement for each SDG with Cohen's kappa, where 1 means perfect agreement and 0 means agreement at chance level.
Second, it prompts three LLMs (GPT, Gemini, Llama) zero-shot with the guidelines, and it runs three existing SDG classifiers (Aurora, Elsevier, OSDG).
The metrics are precision, recall, and F1 score, macro-averaged over the 17 SDGs.

{{< numbers >}}
- value: "2,363"
  label: labels over 139 articles and 17 SDGs
- value: "0.54"
  label: average Cohen's kappa, moderate agreement
- value: "0.68"
  label: best macro F1, GPT
{{< /numbers >}}

The dataset is sparse: on average 14.24 articles are positive for an SDG, from 5 for SDG 1 to 32 for SDG 10 (Table 3 of the paper).
Only 13 of the 139 articles contribute to no SDG, and about half contribute to several (Table 4 of the paper).

{{< bars caption="Agreement between the two annotators of each pair, by SDG; the pair is given in brackets (Table 5 of the paper)." >}}
metric: Cohen's kappa
unit: ""
min: 0
max: 1
bars:
  - label: SDG 1 (G1)
    value: "0.44"
  - label: SDG 2 (G1)
    value: "0.39"
  - label: SDG 3 (G1)
    value: "0.60"
  - label: SDG 4 (G2)
    value: "0.57"
  - label: SDG 5 (G2)
    value: "0.86"
  - label: SDG 6 (G3)
    value: "0.46"
  - label: SDG 7 (G3)
    value: "0.76"
  - label: SDG 8 (G1)
    value: "0.23"
  - label: SDG 9 (G3)
    value: "0.27"
  - label: SDG 10 (G2)
    value: "0.59"
  - label: SDG 11 (G3)
    value: "0.53"
  - label: SDG 12 (G4)
    value: "0.65"
  - label: SDG 13 (G4)
    value: "0.62"
  - label: SDG 14 (G4)
    value: "0.76"
  - label: SDG 15 (G4)
    value: "0.74"
  - label: SDG 16 (G2)
    value: "0.24"
  - label: SDG 17 (G4)
    value: "0.49"
  - label: Average
    value: "0.54"
{{< /bars >}}

Agreement depends on the goal, even within one pair.
SDG 5 (gender equality) reaches 0.86, "almost perfect agreement", because gender equality is often stated explicitly as a goal of the article.
SDG 8 (decent work and economic growth) and SDG 16 (peace, justice and strong institutions) reach only 0.23 and 0.24, "fair agreement", because their scope is broad.

| System | Macro precision | Macro recall | Macro F1 |
|---|---|---|---|
| GPT | 0.78 | 0.66 | **0.68** |
| Gemini | 0.54 | 0.81 | 0.63 |
| Llama | 0.36 | 0.87 | 0.48 |
| Elsevier-M | 0.54 | 0.66 | 0.54 |
| OSDG | 0.60 | 0.46 | 0.49 |
| Elsevier-S | 0.60 | 0.40 | 0.44 |
| Aurora | 0.63 | 0.28 | 0.35 |

*Zero-shot evaluation on AlmaSDG (Table 6 of the paper, rows reordered). GPT, Gemini, and Llama are prompted with the guidelines; the other rows are existing SDG classifiers. Elsevier-S keeps one label, and Elsevier-M keeps every SDG with probability above 0.1. Best value in bold, as in the paper. The paper reports no statistical significance test.*

GPT has the best macro F1 (0.68), followed by Gemini (0.63), while Llama is the weakest LLM (0.48).
Among the existing tools, Elsevier-M is best (0.54) and Aurora is lowest (0.35).
Per SDG, Gemini reaches 0.96 F1 on SDG 5 (Table 7 of the paper).
GPT is best on SDG 17 with 0.60, while Aurora, Elsevier, and OSDG all score 0.00 there.
Models often score lower where humans disagree more, such as on SDGs 8 and 9.
On SDG 5, the goal with the highest agreement, four of the seven systems reach at least 0.80 F1.

## Takeaways

{{< takeaways >}}
- title: Guidelines define what a contribution is.
  text: AlmaSDG comes with guidelines that separate direct and indirect contributions and list 165 contribution areas, so every label rests on a written criterion.
- title: Some goals are harder to judge.
  text: Agreement ranges from 0.23 on SDG 8 to 0.86 on SDG 5, with an average Cohen's kappa of 0.54.
- title: A benchmark for SDG tools.
  text: On the 139 articles, a guideline-based GPT prompt reaches 0.68 macro F1 and the best existing tool 0.54, and the existing tools score 0.00 on SDG 17.
{{< /takeaways >}}
