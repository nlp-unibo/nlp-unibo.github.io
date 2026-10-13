---
title: "Cross-Cultural Idiom Understanding in Large Language Models"
date: 2026-10-13
# One sentence of about 18 words, shown on the card
summary: "Test whether large language models grasp the meaning of idioms across languages and cultures, using only existing datasets."
# Two to four sentences, at most 70 words, shown on the opened card
brief: "An idiom is an expression whose meaning does not follow from its words. This proposal tests whether large language models grasp idioms across languages, without new annotation. A student would group idioms from existing datasets into shared idioms, idioms with the same meaning but a different image, and culture-specific idioms, and then compare models on each group."
contacts:
  - federico-ruggeri
  - katerina-korre
tags:
  - idioms
  - large language models
  - multilingual
  - cross-cultural analysis
---

## Context

An idiom is an expression whose meaning does not follow from its words, such as "break a leg".
Large language models (LLMs) are neural models trained on large text collections, and they often read idioms literally.

Idioms also vary across cultures.
Some idioms are shared across languages, with the same image and meaning.
Others keep the meaning but change the image: the Italian "in bocca al lupo" and the English "break a leg" both wish good luck.
Others belong to one culture only.
Existing datasets, including SemEval shared tasks, already pair idioms with their meanings in many languages.

## Objective

This proposal tests whether LLMs grasp shared, image-different, and culture-specific idioms, without new annotation.
The student builds the three groups from existing datasets and compares models across languages.
