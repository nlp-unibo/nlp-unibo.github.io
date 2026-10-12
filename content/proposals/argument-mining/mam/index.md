---
title: Multimodal Argument Mining
date: 2026-03-02
summary: Detect arguments with speech information, such as prosody, in addition to text.
brief: This proposal adds speech information, such as prosody, to the features used to detect arguments. Speech can be represented with ad hoc features or with end-to-end architectures. Few existing corpora offer both argument annotations and the speech of the annotated text.
contacts:
- eleonora-mancini
- federico-ruggeri
tags:
- argument mining
- multimodal
- speech
aliases:
- /proposals_am/mam/
---

## Context

Argument mining automatically detects and extracts arguments from text.
An argument usually combines a premise and a claim.
The premise is a fact, and it supports the claim, a subjective conclusion.
Spoken arguments also carry speech information, such as prosody, which is the rhythm and intonation of speech.
A spoken argument comes as recorded speech together with its transcript, the written words of that speech.

## Objective

This proposal aims to detect arguments with speech information in addition to text.
Speech information enhances the set of features used to find premises and claims.

{{< svg src="features.svg" caption="Text features from the transcript and speech features from the recorded speech of one spoken argument both feed argument detection, which finds premises and claims." >}}
