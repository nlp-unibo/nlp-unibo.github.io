---
title: Interlocking-free Selective Rationalization Through Genetic-based Learning

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- Federico Ruggeri
- Gaetano Signorelli

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2025-07-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2026-02-27T15:55:53.548831Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- paper-conference

# Publication name and optional abbreviated publication name.
publication: '*Proceedings of the 63rd Annual Meeting of the Association for Computational
  Linguistics (Volume 1: Long Papers)*'
publication_short: ''

doi: 10.18653/v1/2025.acl-long.59

abstract: A popular end-to-end architecture for selective rationalization is the select-then-predict
  pipeline, comprising a generator to extract highlights fed to a predictor. Such
  a cooperative system suffers from suboptimal equilibrium minima due to the dominance
  of one of the two modules, a phenomenon known as interlocking. While several contributions
  aimed at addressing interlocking, they only mitigate its effect, often by introducing
  feature-based heuristics, sampling, and ad-hoc regularizations. We present GenSPP,
  the first interlocking-free architecture for selective rationalization that does
  not require any learning overhead, as the above-mentioned. GenSPP avoids interlocking
  by performing disjoint training of the generator and predictor via genetic global
  search. Experiments on a synthetic and a real-world benchmark show that our model
  outperforms several state-of-the-art competitors.

# Summary. An optional shortened abstract.
summary: GenSPP trains the generator and predictor of a self-explaining text classifier separately with genetic search, removing interlocking and producing more accurate highlights.

tags:
- selective rationalization
- interlocking
- genetic algorithms
- neuroevolution
- explainable AI
- hate speech

topics:
- interpretability
- benchmark

# Display this page in a list of Featured pages?
featured: false

# Links
url_pdf: ''
url_code: 'https://github.com/nlp-unibo/gen-spp'
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
  caption: 'The GenSPP fitness landscape (left) separates solutions that the standard regularized objective (right) scores the same (Figure 1 of the paper).'
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
  url: https://aclanthology.org/2025.acl-long.59/
categories:
  - Conference
aliases:
  - /publication_conferences/ruggeri-signorelli-2025-interlocking/
---

## Research setting

Selective rationalization builds text classifiers that explain themselves.
Besides the label, the model returns a highlight, also called a rationale: the subset of input tokens on which its decision is based.
The most popular design is the select-then-predict (SPP) architecture.
A generator (the selector) reads the text and marks each token as selected or not, and a predictor classifies the text from the selected tokens alone, so the highlight is by construction what the decision rests on.

{{< svg src="spp.svg" caption="The select-then-predict architecture on an example string built with the rules of the paper's Toy dataset, where class aba is defined by the hidden pattern a, b, a. The predictor sees only the highlight, so the highlight is a faithful explanation of the label." >}}

The model learns from labels only: no gold highlights are given during training.
Regularization terms push highlights to be short (sparsity) and made of connected tokens (contiguity).

## Motivation

Training the generator and the predictor together leads to a problem called interlocking.
If the generator gets stuck on a poor selection, the predictor adapts to that selection, which in turn pushes the generator to keep it.
The two modules then settle in a poor solution.
Prior work only mitigates interlocking with sampling, extra guidance modules, heuristics, or additional regularization.

{{< gap caption="How GenSPP relates to the prior work discussed in the paper (Sections 1, 3, and 4)." >}}
label: Approach
columns: [Interlocking-free, No feature-based heuristics, No extra modules or tools, Predictor feedback reaches the generator]
rows:
  - name: Differentiable sampling (Bao et al., 2018; Bastings et al., 2019)
    cells: [false, true, true, true]
  - name: Weight sharing, FR (Liu et al., 2022)
    cells: [false, true, true, true]
  - name: External guidance (Yu et al., 2021; Sha et al., 2023; Hu and Yu, 2024)
    cells: [false, true, false, true]
  - name: Heuristic generator pre-training (Jain et al., 2020)
    cells: [true, false, false, false]
  - name: Three-stage training (Li et al., 2022)
    cells: ["partial", true, true, true]
  - name: This paper (GenSPP)
    ours: true
    cells: [true, true, true, true]
{{< /gap >}}

> **Objective.** Remove interlocking altogether by training the generator and the predictor disjointly, without heuristics, extra regularization, or architectural changes.

## Approach

GenSPP keeps the select-then-predict architecture and changes only how it is trained.
The generator is not trained with gradients: a genetic algorithm searches over its weights.
Each candidate set of generator weights is an individual, and the set of individuals is the population.
To score an individual, GenSPP freezes it and trains a brand new predictor on its highlights, so a generator is never judged by a predictor that has adapted to an earlier selection.
The score, called fitness, comes from the validation set: the lower the classification loss and the highlight regularization, which weigh equally, the higher the fitness.

{{< stages caption="The GenSPP genetic algorithm (Algorithm 1 and Section 5 of the paper). Stages 1 to 3 run once on the initial population. Stages 4 to 8 form one generation, repeated for G generations (G = 100 in the main experiments)." >}}
flow: [Input text, Generator, Highlights, Predictor, Label]
legend:
  evolved: Optimized by the genetic search
  trained: Trained with gradients
  frozen: Kept frozen
stages:
  - title: 1. Initialize
    text: A population of I generators is initialized at random (I = 50 in the experiments). Each individual is one full set of generator weights.
    states: {Generator: evolved}
  - title: 2. Train predictor
    text: For each individual, a predictor is initialized from scratch and trained with gradient descent to minimize the classification loss, while the generator weights stay frozen.
    states: {Input text: data, Generator: frozen, Highlights: data, Predictor: trained, Label: data}
  - title: 3. Fitness
    text: "The trained predictor is evaluated on the validation set with the generator still frozen. Fitness is a minimization problem turned into a score: the lower the classification loss and the highlight regularization, which weigh equally, the higher the fitness."
    states: {Input text: data, Generator: frozen, Highlights: data, Predictor: frozen, Label: data}
  - title: 4. Select parents
    text: From the population of I generators, I/2 pairs of parents are drawn by roulette-wheel selection, where each individual is picked with probability proportional to its fitness.
    states: {Generator: evolved}
  - title: 5. Crossover
    text: One-point crossover mixes each pair. A swap point is drawn at random, and the two parents exchange the parameters beyond that point, so the I/2 pairs produce I new generators.
    states: {Generator: evolved}
  - title: 6. Mutation
    text: Each parameter of the new generators is perturbed with Gaussian noise, with mutation probability pm. Crossover explores the weight space globally, and mutation explores it locally.
    states: {Generator: evolved}
  - title: 7. Score offspring
    text: Every new generator goes through stages 2 and 3. It is frozen, a fresh predictor is trained on its highlights, and its fitness is computed.
    states: {Input text: data, Generator: frozen, Highlights: data, Predictor: trained, Label: data}
  - title: 8. Survival
    text: Old and new generators compete for the I places of the next generation. Half of the places go to the fittest individuals, and the other half are filled by roulette-wheel selection.
    states: {Generator: evolved}
{{< /stages >}}

The fitness does not need to be differentiable, so GenSPP needs no sampling tricks and no dataset-specific sparsity target.

## Results

The paper compares GenSPP with four select-then-predict systems: FR, MGR, MCD, and G-RAT.
All systems share the same recurrent architecture, and every score is an average over five runs with different random seeds.

Two datasets are used, both with gold highlights that serve only for evaluation:

- **Toy** is a synthetic dataset introduced in the paper. It has 10k random strings of 20 characters, and each of three classes is defined by one hidden pattern (aba, baa, or abc), which is the gold highlight. Strings also contain pieces of the other patterns, so the full pattern must be selected.
- **HateXplain** is a dataset of about 20k English social media posts from platforms such as X and Gab. Each post is labeled by at least three annotators, who also marked the words that justify the label. The paper uses it for binary hate speech classification and merges the annotators' highlights by majority voting.

Three metrics describe each system:

- **Highlight F1 (Hl-F1)** compares the selected tokens with the gold highlight, token by token. Higher is better.
- **Macro-F1 (Clf-F1)** measures classification quality, averaged over classes. Higher is better.
- **Selection rate (R)** is the percentage of input tokens that the generator selects, from 0 to 100. Lower means shorter highlights.

{{< numbers >}}
- value: "76.02"
  label: Hl-F1 on Toy, against 65.70 for the best baseline
- value: "42.62"
  label: Hl-F1 on HateXplain, against 36.17 for the best baseline
- value: "6.51%"
  label: selection rate on HateXplain, against 24.68% to 25.55% for the baselines
{{< /numbers >}}

{{< bars caption="Highlight quality when training from scratch. Source: Table 1 of the paper (average over five seed runs)." >}}
metric: Highlight F1 (Hl-F1) on Toy
unit: ""
min: 0
max: 100
bars:
  - label: FR
    value: "54.07"
    err: "4.02"
  - label: MGR
    value: "50.34"
    err: "11.23"
  - label: MCD
    value: "65.70"
    err: "3.76"
  - label: G-RAT
    value: "50.22"
    err: "7.78"
  - label: GenSPP
    value: "76.02"
    err: "0.64"
    ours: true
{{< /bars >}}

{{< bars caption="Highlight quality when training from scratch. Source: Table 1 of the paper (average over five seed runs)." >}}
metric: Highlight F1 (Hl-F1) on HateXplain
unit: ""
min: 0
max: 100
bars:
  - label: FR
    value: "31.15"
    err: "2.56"
  - label: MGR
    value: "29.38"
    err: "4.83"
  - label: MCD
    value: "27.92"
    err: "1.66"
  - label: G-RAT
    value: "36.17"
    err: "1.62"
  - label: GenSPP
    value: "42.62"
    err: "0.73"
    ours: true
{{< /bars >}}

| Model | Toy Clf-F1 | Toy R (%) | HateXplain Clf-F1 | HateXplain R (%) |
|---|---|---|---|---|
| FR | 99.78 | 14.80 | 72.14 | 25.55 |
| MGR | 99.92 | 15.05 | 71.14 | 25.30 |
| MCD | 99.90 | 15.18 | 70.37 | 25.07 |
| G-RAT | 99.36 | 14.81 | 73.85 | 24.68 |
| **GenSPP** | 99.00 | **11.47** | 69.71 | **6.51** |

*Classification quality and selection rate. Source: Table 1 of the paper.*

GenSPP selects the most accurate highlights on both datasets, 10.3 Hl-F1 points above the best baseline on Toy and 6.5 points above it on HateXplain.
Its classification macro-F1 stays comparable to the baselines, and its highlights are much shorter on HateXplain.
Its scores also vary less across seed runs, while MGR and G-RAT are notably unstable on Toy.
In a second test, the generator starts from a deliberately skewed state, pre-trained to select the first token according to the class label, which imitates interlocking: GenSPP recovers and reaches 74.28 Hl-F1 on Toy and 42.81 on HateXplain with G = 150 generations (Table 2 of the paper).

## Takeaways

{{< takeaways >}}
- title: Interlocking can be removed, not only mitigated.
  text: Judging each frozen generator with a freshly trained predictor breaks the dependency between the two modules that causes interlocking.
- title: Genetic search fits rationalization well.
  text: It needs no differentiable objective, no sampling, and no dataset-specific sparsity threshold, and it produced the best highlights on both benchmarks.
- title: The cost is training time.
  text: A seed run takes about 36 minutes on Toy and 78 minutes on HateXplain, against about 8 and 4 minutes for the baselines. The paper notes that parallel evaluation of individuals could reduce this.
{{< /takeaways >}}
