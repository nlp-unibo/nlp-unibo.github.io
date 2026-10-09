---
title: Attention in Natural Language Processing

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- Andrea Galassi
- Marco Lippi
- Paolo Torroni

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2021-01-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2026-03-02T12:28:22.079050Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- article-journal

# Publication name and optional abbreviated publication name.
publication: '*IEEE Transactions on Neural Networks and Learning Systems*'
publication_short: ''

doi: 10.1109/TNNLS.2020.3019893

abstract: 'Attention is an increasingly popular mechanism used in a wide range of neural architectures. The mechanism itself has been realized in a variety of formats. However, because of the fast-paced advances in this domain, a systematic overview of attention is still missing. In this article, we define a unified model for attention architectures in natural language processing, with a focus on those designed to work with vector representations of the textual data. We propose a taxonomy of attention models according to four dimensions: the representation of the input, the compatibility function, the distribution function, and the multiplicity of the input and/or output. We present the examples of how prior information can be exploited in attention models and discuss ongoing research efforts and open challenges in the area, providing the first extensive categorization of the vast body of literature in this exciting domain.'

# Summary. An optional shortened abstract.
summary: 'A unified model and the first taxonomy of attention in natural language processing, charting a fast-growing literature along four dimensions and its open challenges.'

tags:
- task analysis
- computer architecture
- visualization
- neural networks
- natural language processing
- taxonomy
- computational modeling
- natural language processing (NLP)
- neural attention
- review
- survey

topics:
- interpretability

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
  caption: 'The general attention model: keys and a query yield attention weights, which turn the values into one context vector (Figure 4 of the paper, CC BY 4.0).'
  focal_point: ''
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects: ['internal-project']` links to `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []
categories:
  - Highlight
  - Journal
aliases:
  - /publication_highlights/9194070/
---

## Research setting

In many language tasks, a few words matter more than the rest.
In aspect-based sentiment analysis, for example, the word "excellent" says a lot about the service of a hotel and little about its location.
Attention is a part of a neural network that learns this relevance: it computes a weight for each input element, and a higher weight marks a more relevant element.
The weights can also be drawn over the text, which helps people see what the network relied on.

{{< figure src="example.png" caption="Attention weights over one hotel review for three aspects. A darker red marks a higher weight. Bold words are the ones that annotators marked as relevant (Figure 1 of the paper, CC BY 4.0)." >}}

## Motivation

After attention was introduced in natural language processing (NLP) for machine translation, new attention models appeared at a fast pace.
Different authors built almost identical models under different names, and the same name, such as context vector, came to mean different things.
The paper notes that, as a result, a systematic overview of attention was still missing.

{{< gap caption="How the survey relates to the overviews and studies it discusses (Section I of the paper)." >}}
label: Work
columns: [Centered on attention, Text as vector sequences, Across NLP tasks, Taxonomy of attention models]
rows:
  - name: Overview of neural architectures for NLP (Goldberg, 2017)
    cells: [false, true, true, false]
  - name: Survey of attention models in graphs (Lee et al., 2019)
    cells: [true, false, false, false]
  - name: Experimental studies on single tasks (e.g. Britz et al., 2017)
    cells: [true, true, false, false]
  - name: This paper
    ours: true
    cells: [true, true, true, true]
{{< /gap >}}

> **Objective.** Define a unified model of attention for NLP, use it to organize existing attention models into a taxonomy, and outline the open challenges of the area.

## Approach

The paper starts from a classic attention model for machine translation, RNNsearch, as a concrete instance.
An encoder turns each source word into a vector, called an annotation.
At each output step, the attention function scores every annotation against the current state of the decoder.
A softmax turns the scores into weights, and the weighted sum of the annotations is the context vector.

{{< figure src="rnnsearch.png" caption="RNNsearch (left) and its attention function (right). An alignment model scores the annotations h, and a softmax turns the scores e into weights a. A weighted sum yields the context vector c (Figure 2 of the paper, CC BY 4.0)." >}}

The unified model generalizes this example.
Keys are the vectors that attention scores, the query is an optional vector that says what to look for, and values are the vectors that attention combines.
In RNNsearch, the annotations act as both keys and values, and the decoder state acts as the query.
A compatibility function scores the keys, and a distribution function turns the scores into attention weights.

{{< pipeline caption="The core of the unified attention model (Section II-B of the paper). The taxonomy varies the components of this flow." >}}
- title: Keys and query
  text: Vectors for the input elements, plus an optional query.
  icon: list
- title: Score keys
  text: Rates how well each key matches the query.
  icon: balance-scale
  highlight: true
- title: Get weights
  text: Normalizes the scores, often with a softmax.
  icon: chart-bar
  highlight: true
- title: Weighted values
  text: Multiplies each value by its attention weight.
  icon: times
- title: Context vector
  text: Merges the weighted values into one compact vector.
  icon: compress-arrows-alt
{{< /pipeline >}}

The taxonomy then describes any attention model along four dimensions: what the inputs represent, which compatibility function it uses, which distribution function it uses, and how many distinct inputs and outputs it has, which the paper calls multiplicity.

## Results

The paper is a survey and runs no experiments.
The authors explain that attention usually sits inside larger, task-specific architectures, so a fair empirical comparison across tasks is beyond its scope.
Its results are the taxonomy and the map of the literature that the taxonomy makes possible.

{{< numbers >}}
- value: "4"
  label: dimensions in the first taxonomy of attention models
- value: "11"
  label: task families that use attention, from translation to sentiment analysis (Table I)
- value: "171"
  label: works cited in the survey
{{< /numbers >}}

| Dimension | Question it answers | Options charted in the paper |
|---|---|---|
| Input representation | What do keys and values encode? | Words in context (recurrent or convolutional layers), raw inputs (inner attention), self-attention, hierarchical inputs such as words within sentences |
| Compatibility function | How are keys matched with the query? | Comparing: similarity, multiplicative, scaled multiplicative, general. Combining: concat, additive, deep, convolution-based. Location-based |
| Distribution function | How do scores become weights? | Softmax, logistic sigmoid, sparsemax, structured attention, local attention, hard attention, adaptive temperature |
| Multiplicity | How many inputs and outputs? | Multiple outputs: multihead, multidimensional, labelwise. Multiple inputs: coattention, coarse-grained or fine-grained |

*The four dimensions of the taxonomy. Source: Section IV of the paper.*

Compatibility functions follow two main approaches: comparing keys with the query, which suits tasks where relevance means similarity to the query, and combining them into a joint representation.
The paper also shows three ways for knowledge to enter attention: supervising the weights, tracking how much attention each input has already received, and shaping the distribution function.
For instance, a distribution function can use distances along the syntactic structure of a sentence.
The paper closes with open directions: attention to inspect networks, to detect outliers and weigh training samples, to evaluate models, in unsupervised learning, and in neural-symbolic learning and reasoning.

## Takeaways

{{< takeaways >}}
- title: One core model covers most attention variants.
  text: Keys, a query, values, a compatibility function, and a distribution function describe almost all the attention models in the surveyed literature.
- title: Four dimensions make models comparable.
  text: Input representation, compatibility function, distribution function, and multiplicity give a shared vocabulary for models that were named and described in different ways.
- title: Attention is also a tool, not only a layer.
  text: It can help inspect networks and inject knowledge into them, although whether its weights explain a decision is still an open debate.
{{< /takeaways >}}
