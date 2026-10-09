---
title: 'AMELIA - Argument Mining Evaluation on Legal documents in ItAlian: A CALAMITA
  Challenge'

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- Giulia Grundler
- Andrea Galassi
- Piera Santin
- Alessia Fidelangeli
- Federico Galli
- Elena Palmieri
- Francesca Lagioia
- Giovanni Sartor
- Paolo Torroni

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2024-12-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2026-03-02T12:28:22.209996Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- paper-conference

# Publication name and optional abbreviated publication name.
publication: '*Proceedings of the Tenth Italian Conference on Computational Linguistics
  (CLiC-it 2024)*'
publication_short: ''

doi: ''

abstract: 'This challenge consists of three classification tasks, in the context of
  argument mining in the legal domain. The tasks are based on a dataset of 225 Italian
  decisions on Value Added Tax, annotated to identify and categorize argumentative
  text. The objective of the first task is to classify each argumentative component
  as premise or conclusion, while the second and third tasks aim at classifying the
  type of premise: legal vs factual, and its corresponding argumentation scheme. The
  classes are highly unbalanced, hence evaluation is based on the macro F1 score.'

# Summary. An optional shortened abstract.
summary: AMELIA tests whether language models can classify legal arguments in Italian, with three tasks built on 225 expert-annotated decisions on Value Added Tax.

tags:
- argument mining
- legal analytics
- argument schemes
- value added tax
- italian
- calamita

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
  caption: "The three AMELIA tasks applied in sequence to a real argument component from the dataset, labeled premise, legal, and Rule (schema drawn for this page from Section 2 and Appendix A of the paper)."
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
  url: https://aclanthology.org/2024.clicit-1.124/
categories:
  - Conference
aliases:
  - /publication_conferences/grundler-etal-2024-amelia/
topics: [argument-mining, legal, benchmark, llms]
---

## Research setting

Argument mining is the automatic analysis of arguments in text.
An argument is a set of connected pieces of text, called argument components.
A premise is a component that gives a reason for the argument, and a conclusion is the point that the premises argue for.
CALAMITA is a collection of tests of the abilities of large language models (LLMs) in Italian.
AMELIA is its challenge on legal arguments: a model classifies argument components from Italian tax decisions in three tasks.

{{< svg src="task.svg" caption="The three AMELIA tasks on a real argument component of the dataset, shown in the English translation of Appendix A of the paper. Each task applies to the output of the previous one. Schema drawn from the task definitions in Section 2 of the paper." >}}

The second task asks whether a premise is factual, legal, or both.
A factual premise describes the events or the procedure of the case, and a legal premise states legal content such as rules, precedents, or principles.
The third task labels each legal premise with one or more argument schemes, the patterns of legal reasoning it follows:

| Scheme | The legal premise... |
|---|---|
| Rule | refers to codified law, such as an article or its text. |
| Precedent | refers to a previous decision of the Court of Cassation or the European Court of Justice. |
| Classification | defines a legal concept and qualifies a fact as having its properties. |
| Interpretative | states a new interpretation by the Court, which creates a new precedent. |
| Principle | refers explicitly to a principle of law, such as the principle of proportionality. |

*The five argument schemes for tax law. Source: Section 2 of the paper.*

## Motivation

Recognizing arguments is a first step toward reasoning, so even basic argument mining tasks tell us how well LLMs understand the logical relations expressed in text.
Legal texts are a hard test, because legal professionals build and take apart arguments in formal documents with technical language and complex syntax.
Many argument mining datasets exist in English, but resources for Italian are scarce.
Legal language processing in Italian has focused on other tasks, and the authors know of no earlier argument mining challenge on Italian legal documents.

{{< gap caption="How AMELIA relates to the work the paper discusses (Section 1 of the paper)." >}}
label: Resource
columns: [Italian, Legal documents, Argument mining]
rows:
  - name: English argument mining datasets (Habernal et al., 2024; Niculae et al., 2017; Poudyal et al., 2020; Mayer et al., 2021; Accuosto and Saggion, 2020)
    cells: [false, "partial", true]
  - name: Demosthenes, decisions of the Court of Justice of the European Union (Grundler et al., 2022)
    cells: [false, true, true]
  - name: Italian argument mining on news comments and tweets (Basile et al., 2016; Lai et al., 2018)
    cells: [true, false, true]
  - name: Italian legal NLP, such as article retrieval, outcome prediction, contracts, and summarization
    cells: [true, true, false]
  - name: This paper (AMELIA)
    ours: true
    cells: [true, true, true]
{{< /gap >}}

> **Objective.** Measure how well LLMs recognize and classify legal arguments in Italian, with three classification tasks on real tax decisions annotated by experts.

## Approach

The data come from real decisions of Italian Regional Tax Commissions on Value Added Tax (VAT), from 2010 to 2022.
The annotation guidelines adapt those of Demosthenes, an English corpus of the same authors, and keep its classes.
One change was needed: in the Italian decisions a component may span several sentences, and one sentence may hold several components.
The tasks assume that the argument components are already found, so a model only has to classify them.

{{< pipeline caption="How the AMELIA dataset was built and how models are tested (Section 3 of the paper)." >}}
- title: Collect
  text: 225 Italian VAT decisions, from 2010 to 2022.
  icon: gavel
- title: Extract
  text: Argument text from the reasoning part of each decision.
  icon: cut
- title: Mask
  text: Names, addresses, and places hidden; dates keep only the year.
  icon: user-secret
- title: Annotate
  text: Four tax law experts add the labels of the three tasks.
  icon: user-edit
  highlight: true
- title: Split
  text: Three splits by decision; zero-shot and few-shot prompts.
  icon: comments
{{< /pipeline >}}

The split follows the decisions, so all components of a decision fall in the same split, at a ratio of about 60:20:20.
For each task the paper gives two prompts in Italian.
The zero-shot prompt holds only the class definitions, and the few-shot prompt adds labeled examples from the training split.
The dataset is public on Hugging Face under the CC BY 4.0 license.

## Results

The paper presents the challenge and its data and reports no model results.
Its results are the composition of the dataset (Table 1) and the evaluation protocol.
The classes are highly unbalanced, so models are scored with the macro F1 score.
It averages the F1 score over the classes, so rare classes count as much as frequent ones.

{{< numbers >}}
- value: "225"
  label: Italian decisions on VAT
- value: "2910"
  label: premises in task 1
- value: "401"
  label: conclusions in task 1
{{< /numbers >}}

| Split | Rule | Precedent | Interpretative | Principle | Classification |
|---|---|---|---|---|---|
| Train | 350 | 264 | 224 | 92 | 51 |
| Validation | 107 | 82 | 83 | 21 | 22 |
| Test | 118 | 73 | 67 | 31 | 27 |
| **Total** | **575** | **419** | **374** | **144** | **100** |

*Legal premises labeled with each argument scheme. A premise may have several schemes. Source: Table 1 of the paper.*

| Split | Decisions | Premises | Conclusions | Factual | Legal |
|---|---|---|---|---|---|
| Train | 135 | 1866 | 242 | 1254 | 812 |
| Validation | 44 | 528 | 81 | 315 | 266 |
| Test | 46 | 516 | 78 | 323 | 260 |
| **Total** | **225** | **2910** | **401** | **1892** | **1338** |

*Composition of the dataset. Source: Table 1 of the paper.*

Premises far outnumber conclusions, and the five schemes range from 575 legal premises for Rule to 100 for Classification.
This is why the paper uses macro F1 and also reports the F1 score of each class.
As a reference for difficulty only, the best macro F1 scores on Demosthenes were 0.88 for component classification, 0.85 for premise type, and 0.75 for scheme classification.
The paper stresses that these scores are not directly comparable with AMELIA.

## Takeaways

{{< takeaways >}}
- title: A first argument mining challenge on Italian legal text.
  text: AMELIA tests whether LLMs can classify the components, premise types, and reasoning schemes of real Italian tax decisions.
- title: Expert labels on real decisions.
  text: Four tax law experts annotated 225 anonymized VAT decisions, and the data are public under CC BY 4.0.
- title: Rare classes decide the score.
  text: The classes are highly unbalanced, so macro F1 is the metric. The paper also notes the small size, the 2010 to 2022 time span, and the details lost to anonymization as limits.
{{< /takeaways >}}
