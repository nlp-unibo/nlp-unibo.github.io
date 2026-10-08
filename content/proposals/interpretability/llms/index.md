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

Selective rationalization is the process of learning by providing highlights as explanations. Highlights, called rationales, are a subset of the input text meant to be interpretable by a user and to describe faithfully the inference process of a classification model.
A popular architecture for selective rationalization is the Select-then-Predict Pipeline (SPP): a generator selects the rationale, and a predictor classifies it.

## Objective

Large language models (LLMs) are ubiquitous in NLP.
The aim is to evaluate their capabilities in performing selective rationalization via prompting, and to compare them with traditional SPP models.

## References

**Towards Faithful Explanations: Boosting Rationalization with Shortcuts Discovery**\
Linan Yue, Qi Liu, Yichao Du, Li Wang, Weibo Gao, Yanqing An.\
The Twelfth International Conference on Learning Representations, 2024.\
[PDF](https://openreview.net/pdf?id=uGtfk2OphU)

**Learning Robust Rationales for Model Explainability: A Guidance-Based Approach**\
S Hu, K Yu.\
Proceedings of the AAAI Conference on Artificial Intelligence, 2024.\
[DOI](https://doi.org/10.1609/aaai.v38i16.29783)
| [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/29783/31352)
