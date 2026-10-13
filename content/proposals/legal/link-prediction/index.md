---
title: Legal Argumentative Link Prediction with LLMs
date: 2026-10-13
summary: Predict the relations between arguments in CJEU decisions on Fiscal State Aid with large language models.
brief: Link prediction decides whether two argument components are related, for example whether a premise supports a conclusion. This proposal applies large language models to link prediction on decisions of the Court of Justice of the European Union on Fiscal State Aid. It studies how background information, such as the type of arguments and their distance, changes the answers, and it experiments with multi-prompt evaluation.
contacts:
- andrea-galassi
- giulia-grundler
- francesca-lagioia
tags:
- legal argument mining
- link prediction
- large language models
---

## Context

Legal argument mining identifies, extracts, and reconstructs the arguments of judicial texts automatically.
It can reduce manual analysis and support legal research, document retrieval, summarization, and outcome prediction.
Link prediction is one of its tasks: it decides whether two argument components are related.
For example, a premise can support a conclusion or attack another premise.

## Objective

This proposal applies link prediction to decisions of the Court of Justice of the European Union (CJEU) on Fiscal State Aid.
It studies how background information, such as the type of arguments and their distance in the text, changes the answers of the models, and it experiments with multi-prompt evaluation.

{{< svg src="relations.svg" caption="Link prediction on two argument components, built from the definitions of the proposal: the model sees the pair with background information and predicts the relation." >}}
