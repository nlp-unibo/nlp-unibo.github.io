---
title: Rationalization via LLMs
date: 2026-03-02
summary: Evaluate whether large language models can perform selective rationalization through prompting.
brief: Selective rationalization explains a prediction with highlights of the input text. This proposal evaluates how well large language models perform it through prompting, compared with traditional Select-then-Predict Pipeline models.
contacts:
- federico-ruggeri
tags:
- interpretability
- selective rationalization
- large language models
- prompting
aliases:
- /proposals_interpretability/llms/
---

## Context

Selective rationalization explains a prediction with a rationale: a short part of the input text that a user can read and that faithfully shows what the prediction is based on.
The Select-then-Predict Pipeline (SPP) builds this into the model: a generator selects the rationale, and a predictor classifies the rationale only.

## Objective

Large language models (LLMs) can select a rationale and predict a label in a single answer when a prompt asks them to.
This proposal evaluates how well they perform selective rationalization through prompting, compared with traditional SPP models.

{{< svg src="settings.svg" caption="The two settings this proposal compares, on an illustrative sentence that comes from no dataset. In the SPP, the label comes from the rationale alone. The prompted LLM reads the whole text and returns both." >}}
