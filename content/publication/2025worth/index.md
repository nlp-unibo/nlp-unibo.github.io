---
title: "Is It Worth Using LLMs for Unfair Clause Detection in Terms of Service?"

authors:
- Marco Panarelli
- Andrea Galassi
- Francesca Lagioia
- Rūta Liepiņa
- Marco Lippi
- Przemysław Pałka
- Giovanni Sartor

date: "2025-01-01"
doi: "10.1145/3769126.3769218"

# Schedule page publish date (NOT publication's date).
publishDate: "2025-01-01"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["paper-conference"]

# Publication name and optional abbreviated publication name.
publication: "20th International Conference on Artificial Intelligence and Law (ICAIL)"
publication_short: "20th International Conference on Artificial Intelligence and Law (ICAIL)"

url_pdf: 'https://dl.acm.org/doi/pdf/10.1145/3769126.3769218'

abstract: 'Unfair clause detection is an extremely useful AI application for consumer protection. Artificial intelligence has recently been successful in building systems capable to automatically detect unfair clauses in Terms of Service, and also to identify their unfairness categories. Since Large Language Models (LLMs) are nowadays bringing a revolution to the field of artificial intelligence, and in particular to natural language processing and understanding, in this paper we compare several different prompt strategies for LLMs with more traditional BERT-based fine-tuned models. Our extensive experimental evaluation aims to investigate whether it is worth using LLMs also for this challenging domain-specific task.'
# Summary. An optional shortened abstract.
summary: 'Seven large language models, prompted in three ways, face fine-tuned classifiers at spotting unfair clauses in Terms of Service, and the fine-tuned classifiers still win.'

image:
  caption: 'Illustrative schema built from the paper''s definitions: Terms of Service sentences classified into nine unfairness categories by prompted large language models (three prompt strategies) and by supervised baselines.'
  focal_point: ''
  preview_only: false

tags:
- legal
- LLMs
- unfair clause detection
- student publication
- terms of service
- prompting

featured: false

award: '"Peter Jackson" Award for Best Innovative Application Paper'

categories:
  - Highlight
  - Conference
aliases:
  - /publication_highlights/2025worth/
topics: [legal, llms]
---

## Research setting

Online platforms ask users to accept Terms of Service (ToS), contracts that the provider writes alone and that often contain clauses unfair under EU consumer law.
Unfair clause detection checks each ToS sentence against nine unfairness categories, and a sentence unfair for no category counts as fair.
Large language models (LLMs) are general text generators that solve a task from written instructions, called a prompt.
Fine-tuned classifiers, such as BERT-based models, instead learn the task from annotated sentences.

{{< svg src="task.svg" caption="The task on a real sentence from the paper (9GAG ToS, Section 5.5). The paper discusses it as a privacy included clause. The nine categories come from Section 3 of the paper." >}}

## Motivation

Fine-tuned classifiers detect unfair clauses well, but they need a large annotated training set, which takes much work to build and can age as providers change their wording.
LLMs can solve a task from a prompt alone, with no examples (zero-shot) or a few examples (few-shot), so they could avoid that cost.
The best LLMs, however, are often large, costly to run, or available only on payment.
It was unclear whether smaller, open, free LLMs are good enough for this domain-specific legal task.

{{< gap caption="How the paper relates to the work it discusses (Section 2.2). Partial: proprietary GPT models next to the open Llama-2 for privacy policies; zero-shot and few-shot settings only for ChatGPT." >}}
label: Approach
columns: [Unfair clauses in ToS, No large training set, Free open models, Several prompt strategies]
rows:
  - name: Supervised classifiers (Lippi et al., 2019; Guarino et al., 2021)
    cells: [true, false, true, false]
  - name: LLMs on privacy policies (Tang et al., 2023; Rodriguez et al., 2024)
    cells: [false, true, "partial", true]
  - name: ChatGPT on the LexGLUE ToS task (Chalkidis, 2023)
    cells: [true, true, false, "partial"]
  - name: This paper
    ours: true
    cells: [true, true, true, true]
{{< /gap >}}

> **Objective.** Find out whether and to what extent LLMs can detect unfair clauses in ToS, and whether they are worth using instead of fine-tuned transformer classifiers.

## Approach

The paper tests seven instruction-tuned LLMs from 7 to 32 billion parameters: five small ones (Llama3-8B, Mistral-7B, Law-Chat, Nemo-12B, Phi3-14B) and two larger ones (Codestral-22B, Qwen-32B).
The LLMs are never trained: they only receive prompts built from the definitions of the nine categories in the annotation guidelines.
Three prompt strategies split the work differently, and few-shot prompts add 8 hand-picked unfair clauses per category, either long or short sentences.
Eight supervised baselines take the same task: a linear support vector machine (SVM) and seven pre-trained transformers, fine-tuned on the training split.

{{< stages caption="The three prompt strategies and the supervised baselines (Sections 4 and 5.1 of the paper)." >}}
flow: [ToS sentence, Prompt, LLM, Classifier, Categories]
legend:
  frozen: Used as is, never trained
  trained: Fine-tuned on annotated sentences
stages:
  - title: 1. Single-prompt
    text: One prompt holds the task, all nine category definitions, and the output format. The LLM returns the list of categories for which the sentence is unfair. Zero-shot only, since examples for nine categories would make the prompt too long.
    states: {ToS sentence: data, Prompt: data, LLM: frozen, Categories: data}
  - title: 2. Multi-prompt
    text: Nine separate prompts, one per category, each asking for a yes or no answer. This turns the task into nine binary decisions and works zero-shot or few-shot.
    states: {ToS sentence: data, Prompt: data, LLM: frozen, Categories: data}
  - title: 3. Pipeline, step 1
    text: "Category identification: for each category, a zero-shot prompt asks whether the sentence talks about that subject at all. If every answer is no, the sentence is fair."
    states: {ToS sentence: data, Prompt: data, LLM: frozen, Categories: data}
  - title: 4. Pipeline, step 2
    text: "Unfairness assessment: for each category found in step 1, a few-shot prompt asks whether the sentence is unfair under that category's conditions. The pipeline uses 9 to 18 prompts per sentence."
    states: {ToS sentence: data, Prompt: data, LLM: frozen, Categories: data}
  - title: 5. Supervised baselines
    text: The SVM reads word n-gram features, and the transformers (such as Legal-BERT and DeBERTa) are fine-tuned for up to 20 epochs on the training documents.
    states: {ToS sentence: data, Classifier: trained, Categories: data}
{{< /stages >}}

## Results

All models are tested on the CLAUDETTE corpus: 142 English ToS with 37,895 sentences, of which 3,049 are labeled unfair for at least one category, split into 85 training, 35 validation, and 22 test documents.
The paper reports two scores, shown here from 0 to 100:

- **Micro-F1** pools all decisions, so the many fair sentences dominate it.
- **Macro-F1** averages the F1 score over categories, so rare categories weigh as much as frequent ones.

{{< numbers >}}
- value: "77.9"
  label: test macro-F1 of Custom-LegalBERT, the best fine-tuned classifier
- value: "72"
  label: test macro-F1 of Qwen-32B with the pipeline, the best LLM
- value: "~1000x"
  label: faster inference for the fine-tuned transformers than for the LLMs
{{< /numbers >}}

{{< bars caption="Test macro-F1 of each model in its best setting. Source: Tables 3 and 4 of the paper (the paper gives LLM scores from 0 to 1, multiplied here by 100)." >}}
metric: Macro-F1 on the CLAUDETTE test split
unit: ""
min: 0
max: 100
bars:
  - label: Custom-LegalBERT (fine-tuned)
    value: "77.9"
  - label: DeBERTa-base (fine-tuned)
    value: "77.8"
  - label: Qwen-32B (pipeline)
    value: "72"
  - label: Nemo-12B (pipeline)
    value: "62"
  - label: TF-IDF + SVM
    value: "61.0"
  - label: Llama3-8B (pipeline)
    value: "58"
  - label: Phi3-14B (pipeline)
    value: "57"
  - label: Codestral-22B (pipeline)
    value: "47"
  - label: Law-Chat (multi-prompt, few-shot)
    value: "43"
  - label: Mistral-7B (pipeline)
    value: "29"
{{< /bars >}}

| Model | Single | Multi, zero-shot | Multi, few-shot | Pipeline |
|---|---|---|---|---|
| Llama3-8B | 37 | 47 | 40 | **58** |
| Mistral-7B | 23 | 16 | 24 | **29** |
| Law-Chat | 9 | 39 | **43** | 22 |
| Nemo-12B | 39 | 26 | 15 | **62** |
| Phi3-14B | 33 | 41 | 52 | **57** |
| Codestral-22B | 19 | 21 | 26 | **47** |
| Qwen-32B | 49 | 61 | 61 | **72** |

*Test macro-F1 of each LLM per prompt strategy (single-prompt, multi-prompt, pipeline), multiplied by 100; for few-shot settings, the better of long and short examples. Best strategy per model in bold. Source: Table 4 of the paper.*

Every LLM scores below the fine-tuned transformers, which also classify a clause in 1 to 2 milliseconds, against at least about 1 second for an LLM.
The pipeline gives the best macro-F1 for six of the seven LLMs.
The paper observes that LLMs tend to flag sentences unrelated to any category as unfair, and the first pipeline step filters those out.
Model size matters more than example length: Qwen-32B, even with 4-bit weights, comes close to the baselines and matches or beats them on choice of law and privacy included.

## Takeaways

{{< takeaways >}}
- title: Fine-tuned classifiers are still worth it.
  text: When annotated data exist, BERT-based classifiers detect and classify unfair clauses better than every tested LLM, and run about 1000 times faster.
- title: Split the question for LLMs.
  text: Asking first whether a sentence is about a category, and only then whether it is unfair, gave the best results for most LLMs.
- title: Small LLMs miss legal context.
  text: They flag procedural descriptions as unfair and struggle with clauses whose unfairness spans several sentences. Larger models such as Qwen-32B come much closer.
{{< /takeaways >}}
