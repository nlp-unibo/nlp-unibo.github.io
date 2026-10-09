---
title: Knowledge Extraction from Rationalization
date: 2026-03-02
summary: Turn the rationales of single examples into a global explanation, such as a knowledge base.
brief: A rationale explains one prediction by highlighting part of the input. Samples of the same class might share similar rationales. This proposal aggregates and summarizes extracted rationales into a global explanation, such as a knowledge base.
contacts:
- federico-ruggeri
tags:
- interpretability
- selective rationalization
- knowledge extraction
aliases:
- /proposals_interpretability/extraction/
---

## Context

Selective rationalization is the process of learning by providing highlights as explanations. Highlights, called rationales, are a subset of the input text meant to be interpretable by a user and to describe faithfully the inference process of a classification model.
A rationale is a local explanation: it explains the prediction for one example.

## Objective

Samples belonging to the same class might share similar rationales.
The idea is to go from local explanations to a global explanation, such as a knowledge base, by aggregating and summarizing extracted rationales.

## Directions

Aggregation can rely on large language models (LLMs), for example through prompting techniques, or on other solutions.

## References

**A Game Theoretic Approach to Class-wise Selective Rationalization**\
Shiyu Chang, Yang Zhang, Mo Yu, Tommi S. Jaakkola.\
33rd Conference on Neural Information Processing Systems (NeurIPS), Vancouver, Canada, 2019.\
[PDF](https://papers.neurips.cc/paper_files/paper/2019/file/5ad742cd15633b26fdce1b80f7b39f7c-Paper.pdf)
