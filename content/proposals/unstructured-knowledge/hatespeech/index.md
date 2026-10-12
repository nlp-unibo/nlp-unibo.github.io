---
title: Multi-cultural Abusive and Hate Speech Detection
date: 2026-03-02
summary: Measure how different definitions of abusive and hate speech affect detection models.
brief: What counts as abusive or hate speech depends on the socio-cultural context. This proposal evaluates how machine learning models are affected by different definitions, to promote awareness in developing accurate abusive speech detection systems.
contacts:
- federico-ruggeri
- katerina-korre
- arianna-muti
tags:
- hate speech
- abusive language
- multi-cultural
- definitions
aliases:
- /proposals_uki/hatespeech/
---

## Context

What counts as abusive or hate speech depends on the socio-cultural context: the culture, norms, and laws of the people who read a text.
The same text might be deemed offensive in one culture, allowed in another, and legally prosecutable in a third.
A detection model is a machine learning model that flags a text as abusive or hate speech.
It learns from labeled examples.

## Objective

This proposal evaluates how different definitions of abusive and hate speech affect detection models.
The aim is to promote awareness when developing accurate detection models.

{{< svg src="definitions.svg" caption="One text judged in three socio-cultural contexts, each with its own definition of abusive and hate speech. Cultures A, B, and C are placeholders, not real cultures." >}}
