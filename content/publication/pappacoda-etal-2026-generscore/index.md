---
title: 'GeNERscore: Semantic Alignment Metrics for Generative Named Entity Recognition'
authors:
- Gianmarco Pappacoda
- Federico Ruggeri
- Paolo Torroni
author_notes: []
date: '2026-10-01'
publishDate: '2026-11-10'
publication_types:
- paper-conference
publication: Proceedings of the 11th Workshop on Natural User-generated Text
publication_short: ''
venue_key: wnut
doi: 10.18653/2026.wnut-1.9
abstract: 'Traditional Named Entity Recognition (NER) metrics rely on syntactic span and type matching. While this may be
  appropriate if NER is framed as a sequence labeling task, the advent of generative models allows for alternative approaches,
  where model outputs are not extracted, but generated. In this perspective, generative NER calls for more semantically-aware
  scoring mechanisms. Generative models may produce valid aliases, paraphrases, or type variants that differ from the annotated
  gold, while also producing unsupported predictions. We propose a taxonomy of such cases and introduce an embedding-based
  parametric method to evaluate generative NER based on three metrics: soft precision, soft recall and unsupported rate. We
  validate this framework using standard and noisy datasets, across state-of-the-art systems such as GPT and GLiNER alongside
  older encoder-based models. We find that our metrics mostly agree with traditional ones on better-established, less noisy
  benchmarks, but differ in more recent, noisier ones, and can capture edge cases that arise from free-form generation.'
summary: Embedding-based soft precision, soft recall, and unsupported rate score generative NER outputs that paraphrase or
  alias the gold entities.
card_summary: ''
card_caption: ''
tags:
- NER
- evaluation metric
- LLMs
featured: false
url_pdf: https://aclanthology.org/2026.wnut-1.9.pdf
url_code: ''
url_dataset: ''
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
- Workshop
affiliations: []
topics:
- knowledge-extraction
- llms
focus: []
---
