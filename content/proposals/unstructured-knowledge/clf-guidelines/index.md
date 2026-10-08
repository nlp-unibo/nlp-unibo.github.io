---
title: Text Classification with Guidelines Only
date: 2026-03-02
summary: Train text classifiers from annotation guidelines alone, without class labels.
brief: Annotators label data by following guidelines, while models learn the same mapping from labels alone, so they can fit any mapping that matches the data. This proposal gives the guidelines directly to models, without access to class labels during training.
contacts:
- federico-ruggeri
tags:
- text classification
- annotation guidelines
- large language models
math: true
aliases:
- /proposals_uki/clf_guidelines/
- /proposals/unstructured-knowledge/clf_guidelines/
---

## Context

The standard approach for training a machine learning model on a task is to provide an annotated dataset $(\mathcal{X}, \mathcal{Y})$.
The dataset is built by providing unlabeled data $\mathcal{X}$ to a group of annotators previously trained on a set of annotation guidelines $\mathcal{G}$.
Annotators label data $\mathcal{X}$ via a given class set $\mathcal{C}$.

## Problem

Annotators define the mapping from data $\mathcal{X}$ to the class set $\mathcal{C}$ via the guidelines $\mathcal{G}$.
Machine learning models, instead, are trained to learn the same mapping without the guidelines $\mathcal{G}$.
Consequently, these models can learn any mapping from $\mathcal{X}$ to $\mathcal{C}$ that better fits the given data.

## Objective

Directly provide the guidelines $\mathcal{G}$ to models, without any access to class labels during training.

## References

**Let Guidelines Guide You: A Prescriptive Guideline-Centered Data Annotation Methodology**\
Federico Ruggeri, Eleonora Misino, Arianna Muti, Katerina Korre, Paolo Torroni, Alberto Barrón-Cedeño\
September 2024\
[PDF](https://arxiv.org/abs/2406.14099)
