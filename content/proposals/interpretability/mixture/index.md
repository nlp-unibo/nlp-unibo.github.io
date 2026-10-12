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

Selective rationalization trains a model to explain each prediction with highlights of its input text.
These highlights, called rationales, are a part of the input that a user can read and that faithfully shows how the model classifies.
In the Select-then-Predict Pipeline (SPP), a generator selects the rationale and a predictor classifies it.
Training an SPP can get stuck in poor solutions, called local minima, because of interlocking: a suboptimal interplay between generator and predictor.

## Objective

A mixture of experts (MoE) trains several models, called experts, on the same data, and each expert specializes in a subset of it.
This proposal studies whether an MoE model for selective rationalization can address interlocking.

{{< svg src="interlocking.svg" caption="The two ideas this proposal brings together. Left, the SPP, where the interplay between generator and predictor can cause interlocking. Right, an MoE, where three experts stand for several." >}}
