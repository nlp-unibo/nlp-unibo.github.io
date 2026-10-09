---
title: Dynamic Demonstrations Selection for Few-Shot Legal Argument Mining

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- Francesco Alfieri
- Giulia Grundler
- Francesca Galloni
- Rūta Liepiņa
- Francesca Lagioia
- Andrea Galassi
- Paolo Torroni

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2025-01-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2026-03-02T12:28:22.205828Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- paper-conference

# Publication name and optional abbreviated publication name.
publication: '*Proceedings of the First Argument Mining and Empirical Legal Research Workshop (AMELR 2025)*'
publication_short: ''

doi: ''

abstract: 'The selection of demonstrations for few-shot learning plays a pivotal role in the performance of LLMs. In the legal domain, selecting these examples becomes especially critical, since they must be both informative and economical. We address legal argument mining by adopting dynamic selection strategies where a specific set of demonstrations is selected for each inference, and we compare them to static approaches where examples are chosen by experts or by the LLMs themselves. We experiment with 34 learning configurations over 3 different tasks, i.e., classification of argumentative components, type of premises, and argumentative schemes. We find that dynamic selection methods are better than static ones in all three tasks, suggesting that similarity is an important criterion in this domain.'

# Summary. An optional shortened abstract.
summary: Choosing few-shot examples per query by similarity lets LLMs mine legal arguments in EU court rulings as well as or better than expert-chosen examples.

tags:
- student publication
- legal argument mining
- in-context learning
- few-shot learning
- demonstration selection
- large language models

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
  caption: 'The three families of demonstration selection compared in the paper, drawn for this page on illustrative points following the definitions of Section 4.1 (the paper has no figures).'
  focal_point: ''
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects: ['internal-project']` links to `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []
categories:
  - Workshop
aliases:
  - /publication_workshops/alfieri-2025-dynamic/
topics: [argument-mining, legal, llms]
---

## Research setting

Argument mining (AM) is the automatic detection and classification of arguments in text.
In court decisions, an argument is a chain of inferences in which one or more premises lead to a conclusion.
The paper works on Demosthenes, a corpus of 40 English decisions by the Court of Justice of the European Union (CJEU) on Fiscal State Aid.
Legal experts annotated it at three levels.
Each level gives one classification task.

{{< pipeline caption="The three classification tasks of the paper, one per annotation level of the Demosthenes corpus (Sections 3 and 4)." >}}
- title: Argumentative sentence
  text: A sentence from a CJEU decision.
  icon: gavel
- title: 1. Argument component
  text: Premise or conclusion.
  icon: sitemap
- title: 2. Premise type
  text: For premises. Factual, legal, or both.
  icon: balance-scale
- title: 3. Argument scheme
  text: For legal premises. One or more of five schemes.
  icon: tags
  highlight: true
{{< /pipeline >}}

Terms used on this page:

- A **factual premise** describes events or procedural aspects of the case. A **legal premise** refers to legal content such as laws, precedents, principles, or their interpretation.
- An **argument scheme** is the pattern of reasoning behind a legal premise. A premise can carry several schemes. The paper uses five:
  - Rule: an EU norm applies to the case.
  - Precedent: an earlier ruling of the Court applies.
  - Authoritative: a statement by an authority, such as an Advocate General, supports the outcome.
  - Classification: a legal concept is defined by its conditions.
  - Interpretative: a meaning is given to a legal source.
- A **large language model (LLM)** is a general-purpose text model that can solve a task from instructions in its prompt, without training.
- **Few-shot learning**, or in-context learning, adds a few labeled examples to the prompt. These examples are called **demonstrations**, and a prompt with *k* of them is a *k*-shot prompt.
- An **embedding** is a vector that represents the meaning of a sentence. Two sentences with close embeddings are similar.

{{< annotate caption="A legal premise from the corpus that carries three argument schemes at once (Appendix B.3 of the paper). The marked spans follow the rationale that the paper gives for each scheme." >}}
labels: [Precedent, Classification, Rule]
segments:
  - text: "First, it must be recalled that,"
  - text: "according to the Court’s settled case-law,"
    label: Precedent
  - text: "classification of a national measure as ‘State aid’,"
    label: Classification
  - text: "within the meaning of Article 107(1) TFEU,"
    label: Rule
  - text: "requires all the following conditions to be fulfilled …"
    label: Classification
{{< /annotate >}}

## Motivation

LLMs give mixed results in the legal domain, whose language is formal, layered, and often ambiguous.
In few-shot learning, the choice of demonstrations shapes performance, and in the legal domain the choice is especially hard.
Demonstrations must show the key reasoning patterns and cues, yet stay short because of the token limits of the models.
Some prior methods fix one set of demonstrations for all queries.
Others pick examples close to the query, but measure diversity only through labels or through the same similarity score.

{{< gap caption="How the paper relates to the demonstration selection methods it discusses (Section 2 of the paper)." >}}
label: Selection method
columns: [Chosen for each query, Similar to the query, Diverse in content]
rows:
  - name: Static selection by experts or by the LLM (Grundler et al., 2024; Qin et al., 2024)
    cells: [false, false, "not discussed"]
  - name: k-NN selection (Liu et al., 2022)
    cells: [true, true, false]
  - name: Reinforcement learning selection (Wang et al., 2025)
    cells: [true, true, "labels only"]
  - name: Complementary examples (Ye et al., 2023)
    cells: [true, true, "partial"]
  - name: This paper (dynamic graph selection)
    ours: true
    cells: [true, true, true]
{{< /gap >}}

> **Objective.** Measure how demonstration selection affects LLMs on legal argument mining. Compare static selection with dynamic selection, including a new graph-based method that also seeks diversity.

## Approach

The paper compares two families of selection, shown in the figure at the top of this page.
**Static** selection fixes the demonstrations once.
Legal experts choose them with explicit criteria, or the LLM itself chooses them from at most 50 training examples (self-selection).
**Dynamic** selection picks new demonstrations from the training set for each query, the sentence to classify.
Dynamic k-NN takes the *k* training examples whose embeddings are closest to the query.
The new dynamic graph method adds diversity, in five steps.

{{< pipeline caption="Dynamic graph selection (Section 4.1 of the paper). The two distance thresholds are set per task and number of demonstrations, in two configurations called c1 and c2 (Section 4.2)." >}}
- title: Build a graph
  text: Nodes are training examples, linked when close.
  icon: project-diagram
- title: Keep near nodes
  text: Drop nodes far from the query.
  icon: crosshairs
- title: Find groups
  text: The Louvain method splits them into dense groups.
  icon: object-group
  highlight: true
- title: Pick one each
  text: The most central node, by PageRank.
  icon: hand-pointer
- title: Prompt the LLM
  text: The picks go into the prompt.
  icon: comment-dots
{{< /pipeline >}}

A **balanced** variant of both dynamic methods includes about the same number of demonstrations for each class.
The LLMs are Llama 3.1 (8B, instruction tuned) and Gemini 2.0 Flash, with 0, 5, or 10 demonstrations.
Two trained classifiers serve as references: a LinearSVC on TF-IDF features and a fine-tuned LEGAL-BERT, one model per task.

## Results

The paper tests 34 configurations on a held-out split of 8 decisions, with 345 premises and 22 conclusions.
Scores are F1 per class and their macro average (macro-F1), from 0 to 1, where higher is better.

{{< numbers >}}
- value: "0.80"
  label: argument scheme macro-F1, Gemini 5-shot with k-NN, against 0.68 with static expert
- value: "0.84"
  label: premise type macro-F1, Gemini 10-shot with k-NN, against 0.81 with static expert
- value: "14"
  label: demonstrations chosen by both Gemini and the experts, 11 for argument schemes
{{< /numbers >}}

{{< bars caption="Argument scheme classification with Gemini 2.0 Flash and 10 demonstrations, against zero-shot Gemini and the trained references. Source: Table 2 of the paper." >}}
metric: Macro-F1 on argument schemes
unit: ""
min: 0
max: 1
bars:
  - label: Gemini zero-shot
    value: "0.61"
  - label: Static expert
    value: "0.71"
  - label: Static self-selection
    value: "0.75"
  - label: Dynamic k-NN
    value: "0.80"
  - label: Dynamic graph c1
    value: "0.79"
    ours: true
  - label: Dynamic graph c2
    value: "0.74"
    ours: true
  - label: LEGAL-BERT (fine-tuned)
    value: "0.75"
  - label: LinearSVC (trained)
    value: "0.83"
{{< /bars >}}

| Model and selection | Argument component | Premise type | Argument scheme |
|---|---|---|---|
| LinearSVC (trained) | 0.90 | 0.82 | **0.83** |
| LEGAL-BERT (fine-tuned) | **0.91** | **0.89** | 0.75 |
| Gemini 10-shot, static expert | 0.69 | 0.81 | 0.71 |
| Gemini 10-shot, static self-selection | 0.67 | 0.80 | 0.75 |
| Gemini 10-shot, dynamic k-NN | 0.65 | 0.84 | 0.80 |
| Gemini 10-shot, dynamic k-NN balanced | 0.67 | 0.82 | 0.80 |
| Gemini 10-shot, dynamic graph c1 | 0.65 | 0.79 | 0.79 |
| Gemini 10-shot, dynamic graph c2 | 0.67 | 0.83 | 0.74 |

*Macro-F1 per task. Source: Table 2 of the paper.*

Among the LLM configurations, dynamic k-NN is the best overall in all three tasks, which points to similarity as an important criterion in this domain.
At least one configuration of the graph method performs close to k-NN in most settings.
Neither c1 nor c2 is better overall.
Balancing matters for argument components with Llama: with 5 demonstrations, k-NN drops to 0.14 macro-F1 without balancing and reaches 0.69 with it.
The trained references still score best in every task.
However, they use the whole training set and one model per task, while one LLM serves all tasks with 5 or 10 demonstrations.

## Takeaways

{{< takeaways >}}
- title: Similarity is the key criterion.
  text: Picking demonstrations close to each query was the best LLM setting overall in all three tasks. In the paper's comparison, it matches or outperforms demonstrations chosen by legal experts.
- title: Expert curation is not required.
  text: Comparable or better results come without the cost and effort of manual selection. At least one configuration of the graph method performs close to k-NN, which leaves room to explore its thresholds.
- title: Training still wins.
  text: LinearSVC and LEGAL-BERT obtain the best results in all three tasks. The paper plans to test how less labeled data affects each approach.
{{< /takeaways >}}
