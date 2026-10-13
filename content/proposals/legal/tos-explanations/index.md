---
title: Explaining Unfair Clauses in Terms of Service
date: 2026-10-13
summary: Generate legal explanations of why a clause in a digital contract is fair or unfair, with large language models.
brief: Privacy policies and terms of service often contain clauses that are unfair to customers or do not fully meet the GDPR. This proposal uses large language models to explain whether a clause can be considered fair, either by classifying the clause or by motivating a label given by a person or another system. It measures how the type of information and the technique change the explanations.
contacts:
- andrea-galassi
- giulia-grundler
- francesca-lagioia
tags:
- terms of service
- legal explanations
- large language models
---

## Context

Privacy policies and terms of service often contain clauses that are unfair to customers or do not fully meet the General Data Protection Regulation (GDPR).
These documents are long and technical, so their analysis is complex and slow.
Artificial intelligence can help users understand them and make informed decisions.

## Objective

This proposal uses large language models to generate legal explanations of whether a clause in a digital contract can be considered fair.
The model may classify the clause itself or motivate a label assigned by a person or another system.
The thesis evaluates the impact of the available information, such as guidelines or other contracts, and of the technique, such as retrieval-augmented generation or few-shot learning.

{{< svg src="explanation.svg" caption="The explanation task on the illustrative clause of the unfair clause detection proposal, built from the description of the proposal." >}}
