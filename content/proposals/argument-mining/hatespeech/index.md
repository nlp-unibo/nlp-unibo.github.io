---
title: Hate Speech Detection with Argumentative Reasoning
date: 2026-03-02
summary: Use argumentative reasoning to make the implicit content of hate speech explicit.
brief: Hate speech often relies on implicit content and subtle reasoning. This proposal applies argumentative reasoning to make that content explicit, toward hate speech detection systems that are more interpretable and more user-friendly.
contacts:
- federico-ruggeri
- arianna-muti
tags:
- hate speech
- argument mining
- reasoning
- large language models
aliases:
- /proposals_am/hatespeech/
---

## Context

Hate speech often relies on implicit content: meaning that a text suggests without stating it.
It also relies on subtle reasoning nuances.
Argument mining is the problem of automatically detecting and extracting arguments from text.
An argument usually combines a premise and a claim.
The premise is a fact, and it supports the claim, a subjective conclusion.

## Objective

This proposal applies argumentative reasoning to hate speech, to make its implicit content explicit.
The resulting hate speech detection systems should be more interpretable and more user-friendly.

{{< svg src="argument.svg" caption="Argumentative reasoning makes the implicit content of a text explicit as a premise that supports a claim, toward hate speech detection. The schema uses no example text." >}}
