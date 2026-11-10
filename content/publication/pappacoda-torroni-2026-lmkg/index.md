---
title: 'LMKG: a flexible method for ontology-aware Knowledge Graph Extraction from text'
authors:
- Gianmarco Pappacoda
- Paolo Torroni
author_notes: []
date: '2026-10-01'
publishDate: '2026-11-10'
publication_types:
- paper-conference
publication: Proceedings of the 11th Workshop on Automated Knowledge Base Construction (AKBC 2026)
publication_short: ''
venue_key: akbc
doi: 10.18653/2026.akbc-1.23
abstract: 'Knowledge Graphs (KGs) are a practical representation of information that combines structural flexibility with
  expressiveness. With the recent advent of Large Language Models (LLMs), it has become possible to extract KGs from plain
  text. However, extracting facts from text is only one part of building a usable knowledge graph. A construction system must
  also reconcile entity mentions, control its relation vocabulary, integrate information across passages, and preserve a traceable
  connection between graph facts and their source. We present LMKG, a modular LLM-based pipeline that supports both open and
  ontology-constrained extraction. We also propose two construction strategies for long documents: fold, which accumulates
  a graph over successive chunks, and enrich, which combines whole-document and chunk-level extraction before graph refinement.
  We evaluate LMKG on three standard benchmarks: Text2KGBench, MINE-1, and HotpotQA. We find that our ontology conditioning
  substantially improves conformance to a given ontology in Text2KGBench. Our system consistently recovers facts, reaching
  the highest reported fact recovery of 90.80% in MINE-1. We observe degraded downstream question-answering performance on
  HotpotQA when supplying graphs rather than full passages.'
summary: A modular LLM pipeline builds knowledge graphs from long documents, with optional ontology constraints and traceable
  links to the source text.
card_summary: ''
card_caption: ''
tags:
- knowledge graph construction
- ontology
- LLMs
featured: false
url_pdf: https://aclanthology.org/2026.akbc-1.23.pdf
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
