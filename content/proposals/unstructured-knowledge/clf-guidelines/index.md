---
title: Text Classification with Guidelines Only
draft: true
date: 2026-03-02
summary: Train text classifiers from annotation guidelines alone, without class labels.
brief: Annotators label data by following guidelines, while models learn the same mapping from labels alone, so they can fit any mapping that matches the data. This proposal gives the guidelines directly to models, without access to class labels during training.
contacts:
- federico-ruggeri
tags:
- text classification
- annotation guidelines
- large language models
aliases:
- /proposals_uki/clf_guidelines/
- /proposals/unstructured-knowledge/clf_guidelines/
---

## Context

The standard way to train a machine learning model is to give it an annotated dataset: data paired with class labels.
Annotators build this dataset after training on annotation guidelines, the rules that define how to assign the classes.
They label the data with classes from a given class set.
The model learns from the labels alone, without the guidelines, so it can learn any mapping from data to classes that fits the given data.

## Objective

This proposal gives the annotation guidelines directly to the model.
During training, the model receives the guidelines and unlabeled data, but no class labels.

{{< svg src="settings.svg" caption="The two settings this proposal compares. In standard training, only the annotators learn from the guidelines; in guidelines-only training, the model receives the guidelines and no class labels." >}}
