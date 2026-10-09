---
title: Generation and Evaluation of English Grammar Multiple-Choice Cloze Exercises

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- nicolo-donati
- Matteo Periani
- Paolo Di Natale
- Giuseppe Savino
- Paolo Torroni

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2024-12-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2026-03-02T12:28:22.214596Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- paper-conference

# Publication name and optional abbreviated publication name.
publication: '*Proceedings of the Tenth Italian Conference on Computational Linguistics
  (CLiC-it 2024)*'
publication_short: ''

doi: ''

abstract: English grammar Multiple-Choice Cloze (MCC) exercises are crucial for improving
  learners' grammatical proficiency and comprehension skills. However, creating these
  exercises is labour-intensive and requires expert knowledge. Effective MCC exercises
  must be contextually relevant and engaging, incorporating distractors — plausible but incorrect alternatives — to balance difficulty and maintain learner motivation.
  Despite the increasing interest in utilizing large language models (LLMs) in education,
  their application in generating English grammar MCC exercises is still limited.
  Previous methods typically impose constraints on LLMs, producing grammatically correct
  yet uncreative results. This paper explores the potential of LLMs to independently
  generate diverse and contextually relevant MCC exercises without predefined limitations.
  We hypothesize that LLMs can craft self-contained sentences that foster learner's
  communicative competence. Our analysis of existing MCC exercise datasets revealed
  issues of diversity, completeness, and correctness. Furthermore, we address the lack
  of a standardized automatic metric for evaluating the quality of generated exercises.
  Our contributions include developing an LLM-based solution for generating MCC exercises,
  curating a comprehensive dataset spanning 19 grammar topics, and proposing an automatic
  metric validated against human expert evaluations. This work aims to advance the automatic
  generation of English grammar MCC exercises, enhancing both their quality and creativity.

# Summary. An optional shortened abstract.
summary: A fine-tuned Llama 3 writes English grammar multiple-choice exercises without predefined constraints, and a rule-based check of their structure agrees with a human expert.

tags:
- large language models
- multiple-choice cloze
- distractor generation
- language learning
- evaluation metric
- education

# Display this page in a list of Featured pages?
featured: false

# Links
url_pdf: ''
url_code: 'https://github.com/ZanichelliEditore/english-grammar-multiple-choice-generation'
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

# Publication image
# Add an image named `featured.jpg/png` to your page's folder then add a caption below.
image:
  caption: 'A grammar multiple-choice cloze exercise and the prompt that asks for it, from the fine-tuning dataset (Listing 2 of the paper), drawn for this page.'
  focal_point: ''
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects: ['internal-project']` links to `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []
links:
- name: URL
  url: https://aclanthology.org/2024.clicit-1.39/
categories:
  - Conference
aliases:
  - /publication_conferences/donati-etal-2024-generation/
topics: [llms, industry]
---

## Research setting

Language teachers use multiple-choice cloze (MCC) exercises to train grammar.
An MCC exercise has a body, a sentence with a gap; a key, the correct answer for the gap; and distractors, plausible but incorrect alternatives.
Good distractors are homogeneous (same syntactic category as the key), plausible, and unambiguous (none of them could replace the key).
Writing many such exercises by hand takes time and expert knowledge, so the paper asks a large language model (LLM) to write them.

{{< annotate caption="An MCC exercise on comparisons from the fine-tuning dataset (Listing 2 of the paper), shown with its key filled in. The learner sees a gap in place of the key and chooses among better, best, good, and well; the last three are the distractors." >}}
labels: [Key]
segments:
  - text: "Thanks to high technology, doctors can"
  - text: "better"
    label: Key
  - text: "assess patients’ conditions."
{{< /annotate >}}

## Motivation

Most earlier systems take sentences from existing texts and place the gap with fixed rules, such as the first verb or an adjective.
Systems that write new sentences still constrain the model, for example with a fixed part-of-speech (POS) sequence, and their output tends to lack creativity.
The only English MCC dataset, SC-Ques, has limited diversity, underrepresented topics, and frequent mistakes.
Lastly, the field has no agreed automatic metric for the quality of a generated exercise.

{{< gap caption="How the paper relates to the prior work it discusses (Sections 1 and 3)." >}}
label: Approach
columns: [Writes its own sentences, No fixed gap rule or POS sequence]
rows:
  - name: Rule-based pipelines (Sumita et al.; Lin et al.)
    cells: [false, false]
  - name: Gap detection with conditional random fields (Goto et al.)
    cells: [false, true]
  - name: Neural gap prediction (Bitew et al.; Matsumori et al.)
    cells: [false, true]
  - name: Generation from a POS sequence, keyword, and topic (Chomphooyod et al.)
    cells: [true, false]
  - name: This paper
    ours: true
    cells: [true, true]
{{< /gap >}}

> **Objective.** Find out how well an LLM can write accurate English grammar MCC exercises without predefined constraints or POS sequences, and measure their quality with an automatic metric checked against a human expert.

## Approach

The base Llama 3 model, given a detailed prompt, struggled with some grammar topics and wrote poor distractors.
The authors therefore fine-tuned it on a cleaned dataset of exercises, built from SC-Ques in the steps below.

{{< pipeline caption="Building the fine-tuning dataset (Section 5 of the paper). After the removal of similar exercises, 30% of the original data was left." >}}
- title: SC-Ques
  text: About 300k English sentence completion exercises written by teachers.
  icon: database
- title: Cleaning
  text: Drop items with several gaps, fewer than two distractors, or noise.
  icon: broom
- title: Topics
  text: A rule-based Pattern Matcher links each key to one of 19 grammar topics.
  icon: tags
  highlight: true
- title: Filtering
  text: Remove similar exercises per topic and cap how often one key appears.
  icon: clone
- title: Balancing
  text: Add synthetic WH-question exercises written with GPT-4.
  icon: balance-scale
{{< /pipeline >}}

Each training example pairs a grammar topic and a number of distractors with an exercise in JSON: the full sentence, the sentence with the gap, the key, and the distractors.
Two metrics then score the output.
Structural compliance (SC) is a rule-based check of the exercise form.
The gap must sit in the intended place, the key must have the right grammatical form, and every distractor must be homogeneous with the key.
Self-BLEU measures how much the exercises of one topic repeat each other's word sequences (2 to 5 words long); lower means more diverse.

{{< stages caption="Training, generation, and checking (Sections 6 to 8 of the paper)." >}}
flow: [Grammar topic, Llama 3 weights, LoRA adapters, Exercise, Structural check]
legend:
  trained: Trained with gradients
  frozen: Kept fixed
stages:
  - title: 1. Fine-tune
    text: Llama 3 8B Instruct is quantized to 4-bit precision and kept frozen. Small low-rank (LoRA) adapters on its attention layers learn to write the exercise for a given topic, for 3 epochs, in two hours on one GPU.
    states: {Grammar topic: data, Llama 3 weights: frozen, LoRA adapters: trained, Exercise: data}
  - title: 2. Generate
    text: For each of the 19 topics, the model writes 50 exercises with one distractor each, sampling at temperature 0.7.
    states: {Grammar topic: data, Llama 3 weights: frozen, LoRA adapters: frozen, Exercise: data}
  - title: 3. Check
    text: "The structural check tests the gap and key (pertinence) and the distractor (homogeneity). For inflectional topics, the distractor must share the key's lemma; for free morpheme topics, whose options form a small closed set, it must come from a list of admitted words."
    states: {Exercise: data, Structural check: frozen}
{{< /stages >}}

## Results

The 950 generated exercises were scored with the automatic metrics and reviewed by a computational linguist with a background in language teaching.
The expert judged each exercise correct (EC) only if it was plausible, unambiguous, coherent with common sense, and acceptable (free of stereotypes and inappropriate content).
The expert also judged structural compliance, which serves as the gold reference for the automatic check (SC<sub>A</sub>).

{{< numbers >}}
- value: "79%"
  label: of the 950 exercises judged ready for learners by the expert
- value: "95%"
  label: F1 of the automatic structural check against the expert (precision 98%, recall 91%)
- value: "0.07"
  label: average self-BLEU, a sign of low repetition
{{< /numbers >}}

{{< bars caption="Share of exercises judged correct by the expert, per grammar topic. Source: Table 1 of the paper (50 exercises per topic)." >}}
metric: Exercise correctness (EC) per grammar topic
unit: ""
min: 0
max: 1
bars:
  - label: articles
    value: "0.74"
  - label: comparison adjectives
    value: "0.72"
  - label: conditional statements
    value: "0.66"
  - label: future simple
    value: "0.90"
  - label: modal verbs
    value: "0.70"
  - label: infinitive and gerund verbs
    value: "0.86"
  - label: passive tenses
    value: "0.74"
  - label: past continuous
    value: "0.88"
  - label: past perfect
    value: "0.82"
  - label: past simple
    value: "0.82"
  - label: personal pronouns
    value: "0.74"
  - label: possessive adjectives
    value: "0.72"
  - label: prepositions
    value: "0.72"
  - label: present continuous
    value: "0.88"
  - label: present perfect
    value: "0.84"
  - label: present simple
    value: "0.86"
  - label: quantifiers
    value: "0.84"
  - label: relative clauses
    value: "0.74"
  - label: WH- question
    value: "0.90"
{{< /bars >}}

| Average over the 19 topics | Value |
|---|---|
| Structural compliance, automatic check (SC<sub>A</sub>) | 0.85 |
| Structural compliance, expert (SC<sub>H</sub>) | 0.92 |
| Self-BLEU (lower is better) | 0.07 |
| Exercise correctness, expert (EC) | 0.79 |
| Wrong exercises that break common sense | 0.75 |
| Wrong exercises with an ambiguous distractor | 0.19 |
| Wrong exercises that are not acceptable | 0.05 |
| Wrong exercises that are not plausible | 0.01 |

*Averages from Table 1 (first four rows) and from the error analysis on wrong exercises in Table 2 of the paper.*

Most generated exercises are well formed and varied, and the automatic check agrees closely with the expert.
By the structural scores, the model does better on free morpheme topics, where keys and distractors come from a small set of words.
On verb tense topics, the Pattern Matcher sometimes mislabels verbs, so the check can wrongly reject an exercise.
Among the wrong exercises, a sentence that makes no sense is the most frequent error, and an ambiguous distractor is the second.
Biased or trivial exercises are almost absent.

## Takeaways

{{< takeaways >}}
- title: A fine-tuned LLM writes usable grammar exercises.
  text: Without predefined constraints or POS sequences, 79% of the generated exercises met every requirement for classroom use. The authors found that high-quality fine-tuning data was a key factor.
- title: Structure can be checked automatically.
  text: The rule-based structural check reached 95% F1 against the expert, so it can screen exercises before a human review.
- title: Meaning is the open problem.
  text: Most wrong exercises had a sentence that breaks common sense, and some distractors could replace the key, especially for verb tenses.
{{< /takeaways >}}
