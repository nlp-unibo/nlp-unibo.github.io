---
title: Legal Argument Generation with LLMs
date: 2026-10-13
summary: Evaluate whether large language models can generate the conclusion or a missing step of a legal argumentative chain.
brief: A legal argument is a chain of reasoning steps that leads to a conclusion. This proposal evaluates how well large language models generate parts of such a chain, from the final conclusion to a missing intermediate step. The model may draw on related arguments or similar documents, given as demonstrations or retrieved with retrieval-augmented generation.
contacts:
- andrea-galassi
- giulia-grundler
- francesca-lagioia
tags:
- legal argument mining
- argument generation
- large language models
---

## Context

Legal argument mining identifies, extracts, and reconstructs the arguments of judicial texts automatically.
It can reduce manual analysis and support legal research, document retrieval, summarization, and outcome prediction.
In a judicial text, an argument is a chain of reasoning steps that leads to a conclusion.

## Objective

This proposal evaluates the ability of large language models to generate parts of an argumentative chain: the final conclusion or any missing intermediate step.
The model may rely on related arguments or similar documents, given as demonstrations or retrieved with retrieval-augmented generation (RAG).

{{< svg src="chain.svg" caption="Generation of a missing step in an illustrative argumentative chain, built from the description of the proposal." >}}
