---
title: Training Data and Transfer Learning in Legal Argument Mining
date: 2026-10-13
summary: Measure how the quantity and the legal domain of available data change legal argument mining with LLMs and traditional models.
brief: This proposal compares large language models and traditional models as the amount of available data changes, whether the data serves as training data, as demonstrations in the prompt, or as documents retrieved through retrieval-augmented generation. It also measures transfer learning between two legal domains, fiscal state aid and equal treatment.
contacts:
- andrea-galassi
- giulia-grundler
- francesca-lagioia
tags:
- legal argument mining
- transfer learning
- large language models
---

## Context

Legal argument mining identifies, extracts, and reconstructs the arguments of judicial texts automatically.
It can reduce manual analysis and support legal research, document retrieval, summarization, and outcome prediction.
Transfer learning trains a model on one dataset and applies it to another.

## Objective

This proposal studies large language models and traditional models, and the impact of the available data in quantity and in domain.
The data can serve as training data, as demonstrations in the prompt, or as documents that retrieval-augmented generation (RAG) finds for the model.
The proposal also measures transfer learning between two legal domains: fiscal state aid and equal treatment.

{{< svg src="data.svg" caption="The two questions of the proposal, built from its description: how the quantity and the form of the data change legal argument mining, and how a model transfers between two legal domains." >}}
