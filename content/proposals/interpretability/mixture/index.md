---
title: Mixture of Experts for Rationalization
date: 2026-03-02
summary: Study whether a mixture of experts model can address interlocking in selective rationalization.
brief: Selective rationalization models can suffer from interlocking, a poor interplay between the component that selects highlights and the one that predicts. In a mixture of experts, several models are trained on the same data, each specializing in a subset. This proposal studies whether such a model can address interlocking.
contacts:
- federico-ruggeri
tags:
- interpretability
- selective rationalization
- mixture of experts
- interlocking
aliases:
- /proposals_interpretability/mixture/
---

## Context

Selective rationalization is the process of learning by providing highlights as explanations. Highlights, called rationales, are a subset of the input text meant to be interpretable by a user and to describe faithfully the inference process of a classification model.
A popular architecture for selective rationalization is the Select-then-Predict Pipeline (SPP): a generator selects the rationale, and a predictor classifies it.
The SPP has been shown to suffer from local minima derived from a suboptimal interplay between the generator and the predictor, a phenomenon known as interlocking.

## Objective

Mixture of experts (MoE) is a technique whereby several models are trained on the same data, each specializing in a certain subset.
MoE models have been successful in a variety of applications, and their original formulation dates back to the early 1990s.
The idea is to understand whether an MoE model for selective rationalization can address interlocking.

## References

**A Survey on Mixture of Experts in Large Language Models**\
W. Cai, J. Jiang, F. Wang, J. Tang, S. Kim and J. Huang.\
In IEEE Transactions on Knowledge and Data Engineering, vol. 37, no. 7, pp. 3896-3915, July 2025.\
[DOI](https://doi.org/10.1109/TKDE.2025.3554028)
