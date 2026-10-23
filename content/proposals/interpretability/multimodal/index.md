---
title: Multimodal Rationalization
date: 2026-10-23
summary: Extend the Select-then-Predict Pipeline to speech, so that a model explains each prediction with highlights of both the audio and its transcript.
brief: Selective rationalization explains a prediction with highlights of the input text. Many tasks, such as the analysis of debates, also come with the audio of the speech. This proposal extends the Select-then-Predict Pipeline to audio and text. The highlights of the two modalities can overlap or complement each other, and this comparison shows what each modality adds to the explanation.
contacts:
- federico-ruggeri
tags:
- interpretability
- selective rationalization
- multimodal
- audio
---

## Context

Selective rationalization trains a model to explain each prediction with highlights of its input, called rationales.
In the Select-then-Predict Pipeline (SPP), a generator selects the rationale and a predictor classifies the rationale only.
The SPP is typically applied to text alone.
Many tasks, such as argument mining in political debates, also come with the audio of the speech.
The audio carries cues that the transcript loses, such as tone, emphasis, and pauses.

## Objective

This proposal extends the SPP to audio and text, with one rationale for each modality.
The two rationales can overlap, when both modalities highlight the same words.
They can also complement each other, when one modality highlights evidence that the other lacks.
Comparing the two rationales shows what each modality adds to the explanation, so multimodality also serves interpretability.

{{< svg src="schema.svg" caption="The SPP on text and audio, on an illustrative sentence that comes from no dataset. The generator selects one rationale per modality: the rationales overlap on one word and complement each other on two others. The predictor classifies both rationales." >}}
