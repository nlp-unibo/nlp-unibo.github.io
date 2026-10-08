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

Selective rationalization is the process of learning by providing highlights as explanations. Highlights, called rationales, are a subset of the input text meant to be interpretable by a user and to describe faithfully the inference process of a classification model.
Several techniques transform text into abstract structured content, such as abstract meaning representation (AMR) graphs and parse trees.

## Objective

Apply rationalization to structured content, and enforce structural constraints that depend on the application scenario.
The constraints describe which types of structures the rationalization system can extract.
A tree kernel is a function that measures the similarity between two trees; in the case of tree kernels, the allowed structures are different types of trees.

## References

**Tree-constrained Graph Neural Networks for Argument Mining**\
Federico Ruggeri, Marco Lippi, Paolo Torroni\
September 2021\
[PDF](https://arxiv.org/abs/2110.00124)
