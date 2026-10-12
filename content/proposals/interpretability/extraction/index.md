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

Selective rationalization explains the prediction of a classification model with highlights of the input text.
These highlights, called rationales, are a subset of the input that a user can read.
A rationale should also describe faithfully how the model reaches its prediction.
A rationale is a local explanation: it explains the prediction for one example.

## Objective

Examples that belong to the same class might share similar rationales.
This proposal aims to go from local explanations to a global explanation, such as a knowledge base, by aggregating and summarizing extracted rationales.

{{< svg src="aggregation.svg" caption="From local explanations to a global explanation, on illustrative sentences that come from no dataset. Aggregation turns the rationales of three examples of one class into one global explanation, such as a knowledge base." >}}
