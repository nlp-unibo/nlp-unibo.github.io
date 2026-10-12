---
title: Argument Mining on Legal Datasets
date: 2026-03-02
summary: Mine the well-structured arguments of legal documents with recent and hybrid NLP techniques.
brief: Argumentation in legal documents is typically well-structured and follows specific domain rules. This proposal applies both the most recent NLP techniques and hybrid techniques that can leverage domain knowledge.
contacts:
- andrea-galassi
- marco-lippi
tags:
- legal analytics
- argument mining
- benchmarks
aliases:
- /proposals_legal/am/
---

## Context

Legal documents are among the domains that would benefit most from natural language processing (NLP), the field that builds tools to analyze text automatically.
Tasks in this domain usually require a specialist with background knowledge, and they are hard to transfer to an automatic tool.
Argument mining is the task of detecting and extracting arguments from text automatically.
An argument usually combines a premise and a claim.
The premise is a fact, and it supports the claim, a subjective conclusion.

## Objective

Arguments in legal documents are usually well-structured and follow specific domain rules.
This proposal applies the most recent NLP techniques, and hybrid techniques that can use domain knowledge, to argument mining on legal documents.

{{< svg src="argument.svg" caption="Argument mining on an illustrative sentence that comes from no legal document. The premise is a fact, and the claim is the subjective conclusion it supports." >}}
