---
title: A Multi-Agent LLM Pipeline for Legal Argument Mining
authors:
- Safoura Banihashemi
- Giulia Grundler
- Andrea Galassi
author_notes: []
date: '2026-08-18'
publishDate: '2026-10-13'
publication_types:
- paper-conference
publication: Proceedings of the 2026 ACM Symposium on Document Engineering (DocEng '26)
publication_short: ''
venue_key: doceng
doi: 10.1145/3820755.3833404
abstract: Accurate extraction of argumentative information from legal documents allows transforming legal documents into structured
  representations that can support downstream applications, such as information retrieval, document analysis, and legal decision
  support. Legal Argument Mining addresses the identification and classification of argumentative structures and their relations
  in legal texts. Such a task can be decomposed into multiple interdependent reasoning steps. In this work, we investigate
  the implementation of an argument mining pipeline using LLM agents, each one dedicated to a separate task. We evaluate our
  system under three different settings that progressively expose the impact of error propagation, ranging from independent
  evaluation of each agent to a realistic end-to-end scenario. We perform an experimental evaluation on the Demosthenes corpus,
  comparing an open-weight model against a commercial one. Results show that cascading errors substantially degrade downstream
  performance, making the first stages of the pipeline a significant bottleneck. Our findings highlight the importance of
  evaluating modular LLM systems in their end-to-end behavior in addition to individual task performance.
summary: A pipeline of LLM agents mines arguments from legal texts, and its end-to-end evaluation shows that errors in the
  first stages substantially degrade later ones.
card_summary: ''
card_caption: ''
tags:
- legal argument mining
- LLM agents
- large language models
featured: false
url_pdf: ''
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
- Conference
affiliations: []
topics:
- legal
- argument-mining
- llms
focus: []
---
