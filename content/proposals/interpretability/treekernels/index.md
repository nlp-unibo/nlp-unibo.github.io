---
title: Structured Rationalization via Tree Kernel Methods
date: 2026-03-02
summary: Extract rationales from structured representations of text, such as trees, under structural constraints.
brief: Text can be transformed into structured content, such as parse trees or abstract meaning representation graphs. This proposal applies rationalization to such content and constrains which structures a rationale can take. With tree kernels, these structures are different types of trees.
contacts:
- federico-ruggeri
tags:
- interpretability
- selective rationalization
- structured rationales
- tree kernels
aliases:
- /proposals_interpretability/treekernels/
---

## Context

Selective rationalization explains the prediction of a classification model with highlights of the input text, called rationales.
A rationale should be readable by a user and should faithfully describe how the model reaches its prediction.
Several techniques transform text into structured content, such as parse trees and abstract meaning representation graphs.

## Objective

This proposal applies rationalization to structured content and constrains the structures that a rationale can take.
These structural constraints depend on the application scenario and define which types of structures the rationalization system can extract.
With tree kernels, functions that measure the similarity between two trees, the allowed structures are different types of trees.

{{< svg src="structure.svg" caption="The setup this proposal studies, on an illustrative sentence and tree that come from no dataset. The structural constraint defines which types of trees the rationalization system can extract as a rationale." >}}
