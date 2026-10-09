---
title: Multimodal Fallacy Classification in Political Debates

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- Eleonora Mancini
- Federico Ruggeri
- Paolo Torroni

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2024-03-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2026-02-27T15:55:53.530491Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- paper-conference

# Publication name and optional abbreviated publication name.
publication: '*Proceedings of the 18th Conference of the European Chapter of the Association
  for Computational Linguistics (Volume 2: Short Papers)*'
publication_short: ''

doi: 10.18653/v1/2024.eacl-short.16

abstract: Recent advances in NLP suggest that some tasks, such as argument detection
  and relation classification, are better framed in a multimodal perspective. We propose
  multimodal argument mining for argumentative fallacy classification in political
  debates. To this end, we release the first corpus for multimodal fallacy classification.
  Our experiments show that the integration of the audio modality leads to superior
  classification performance. Our findings confirm that framing fallacy classification
  as a multimodal task is essential to capture paralinguistic aspects of fallacious
  arguments.

# Summary. An optional shortened abstract.
summary: Releases the first corpus pairing political debate text with audio for classifying six fallacy types, and shows that adding audio improves classification for several models.

tags:
- multimodal argument mining
- fallacy classification
- political debates
- audio
- corpus

# Display this page in a list of Featured pages?
featured: false

# Links
url_pdf: ''
url_code: ''
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
  caption: "The multimodal architecture used in the experiments: a text module and an audio module encode the input, their outputs are concatenated, and a classification module predicts the fallacy category (Figure 1 of the paper, CC BY 4.0)."
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
  url: https://aclanthology.org/2024.eacl-short.16
categories:
  - Highlight
  - Conference
aliases:
  - /publication_highlights/mancini-etal-2024-multimodal/
topics: [argument-mining, multimodal, speech, benchmark]
---

## Research setting

Argument mining is the automatic analysis of arguments in text, such as finding claims and the reasons that support them.
A fallacy is a deceptive, misleading, or invalid argument, and fallacy classification assigns each fallacious passage to a fallacy category.
Most argument mining work reads only the words.
Spoken debates also carry paralinguistic cues, such as accent, rhythm, and tone of voice.
This paper treats fallacy classification in US presidential debates as a multimodal task, where each fallacy comes with its text and its audio clip.

{{< pipeline caption="The task: a fallacious passage from a debate, as text and as audio, goes in, and one of six fallacy categories comes out." >}}
- title: Debate passage
  text: One passage, in two modalities.
  icon: comments
  branches:
    - title: Text
      text: Transcript sentences
    - title: Audio
      text: The matching recording
- title: Classifier
  text: Combines what both modalities say.
  icon: project-diagram
  highlight: true
- title: Fallacy category
  text: One of six categories.
  icon: tag
{{< /pipeline >}}

| Fallacy category | What it does | Example from the corpus |
|---|---|---|
| Appeal to Emotion | Uses loaded language. | "the same kind of woolly thinking" |
| Appeal to Authority | Uses an expert's opinion as evidence. | "As George Will said the other day, ..." |
| Ad Hominem | Attacks the arguer instead of the position. | "Governor Carter apparently doesn't know the facts." |
| False Cause | Takes correlation for causation. | "We won the Cold War because we invested and we went forward." |
| Slippery Slope | Claims exaggerated outcomes for an action. | "And if we don't act today, the problem will be valued in the trillions." |
| Slogans | Brief, striking phrases that evoke excitement. | "We have to practice what we preach." |

*The six fallacy categories (Section 3.1 and Table 1 of the paper).*

Terms used on this page:

- A **snippet** is the annotated fallacy within a debate passage.
- A **pretrained encoder** is a large model trained beforehand on other data that turns text or audio into vectors. BERT, RoBERTa, and SBERT encode text; Wav2Vec and CLAP encode audio.
- **F1** balances precision and recall for one category. **Macro-F1** averages F1 over the six categories, so rare categories count as much as frequent ones. It ranges from 0 to 1, and higher is better.

## Motivation

Analyses of political speech link fallacies to the voice.
Accent stereotypes go with Ad Hominem, a staccato rhythm with Appeal to Authority, and an angry tone with Appeal to Emotion.
Multimodal argument mining already uses debate audio for argument detection, component classification, and relation classification.
Fallacy classification, however, had only been studied on text, and no corpus paired annotated fallacies with audio.

{{< gap caption="How the paper positions itself against the related work it discusses (Sections 1 and 2 of the paper)." >}}
label: Study
columns: [Political debates, Uses audio, Fallacy classification]
rows:
  - name: Claim detection from speech (Lippi and Torroni, 2016)
    cells: [true, true, false]
  - name: Multimodal extensions of USED (Mancini et al., 2022; Mestre et al., 2023)
    cells: [true, true, false]
  - name: Text-only fallacy classification, USED-fallacy (Goffredo et al., 2022)
    cells: [true, false, true]
  - name: This paper (MM-USED-fallacy)
    ours: true
    cells: [true, true, true]
{{< /gap >}}

> **Objective.** Build the first corpus for multimodal fallacy classification, and test whether adding audio to text improves the classification of fallacies in political debates.

## Approach

The authors start from USED-fallacy, a text corpus of US presidential debates from 1960 to 2016 with span-level fallacy annotations.
They map each annotated span to the sentences it overlaps.
Sentence-level timestamps from an earlier multimodal version of the same debates then cut the matching audio clips.
Fuzzy string matching handles small transcript differences, and misaligned samples are removed.
The result, MM-USED-fallacy, holds 1,891 text-audio pairs from 28 debates.

{{< pipeline caption="How MM-USED-fallacy is built (Section 3.2 of the paper)." >}}
- title: Spans
  text: Fallacy spans from USED-fallacy.
  icon: file-alt
- title: Sentences
  text: Label every sentence that overlaps a fallacy span.
  icon: align-left
- title: Audio
  text: Timestamps cut the clips; misaligned samples are removed.
  icon: wave-square
  highlight: true
- title: Corpus
  text: MM-USED-fallacy, 1,891 text-audio pairs from 28 debates.
  icon: database
{{< /pipeline >}}

The classifier keeps the architecture shown at the top of this page.
A text module and an audio module each encode the passage, their outputs are concatenated, and a stack of dense layers predicts the category.
The study compares three text encoders and two audio encoders, alone and in every text-audio pair.

{{< pipeline caption="The classifier and the encoders compared (Section 4 and Figure 1 of the paper)." >}}
- title: Encoders
  text: One module per modality.
  icon: wave-square
  branches:
    - title: Text module
      text: BERT, RoBERTa, or SBERT
    - title: Audio module
      text: Wav2Vec or CLAP, then a BiLSTM
- title: Concatenation
  text: Joins the two encodings.
  icon: layer-group
  highlight: true
- title: Classification module
  text: Dense layers predict the category.
  icon: tag
{{< /pipeline >}}

## Results

The authors compare text-only, audio-only, and text-audio models on 1,063 unique passage and snippet pairs, after removing duplicate snippets.
They use leave-one-out cross-validation over debates: each of the 28 runs tests on one debate and trains on the others.
Scores are macro-F1 averaged over the 28 runs, next to a majority-class baseline and a random baseline.

{{< numbers >}}
- value: "0.40"
  label: best average macro-F1, text plus audio (BERT + Wav2Vec, RoBERTa + CLAP)
- value: "0.38"
  label: best average macro-F1, text only (RoBERTa)
- value: "+8 points"
  label: gain from adding Wav2Vec audio to BERT (0.32 to 0.40)
{{< /numbers >}}

{{< bars caption="Average macro-F1 over the 28 runs; whiskers show the standard deviation reported in the paper. Source: Table 6 of the paper." >}}
metric: Average macro-F1 on MM-USED-fallacy
unit: ""
min: 0
max: 0.6
bars:
  - label: Random baseline
    value: "0.12"
    err: "0.05"
  - label: Majority baseline
    value: "0.20"
    err: "0.17"
  - label: Audio only, Wav2Vec
    value: "0.13"
    err: "0.07"
  - label: Audio only, CLAP
    value: "0.12"
    err: "0.08"
  - label: Text only, BERT
    value: "0.32"
    err: "0.13"
  - label: Text only, RoBERTa
    value: "0.38"
    err: "0.18"
  - label: Text only, SBERT
    value: "0.31"
    err: "0.18"
  - label: BERT + Wav2Vec
    value: "0.40"
    err: "0.17"
    ours: true
  - label: BERT + CLAP
    value: "0.36"
    err: "0.17"
    ours: true
  - label: RoBERTa + Wav2Vec
    value: "0.39"
    err: "0.19"
    ours: true
  - label: RoBERTa + CLAP
    value: "0.40"
    err: "0.19"
    ours: true
  - label: SBERT + Wav2Vec
    value: "0.23"
    err: "0.11"
    ours: true
  - label: SBERT + CLAP
    value: "0.24"
    err: "0.10"
    ours: true
{{< /bars >}}

| Model | Appeal to Emotion | Appeal to Authority | Ad Hominem | False Cause | Slippery Slope | Slogans |
|---|---|---|---|---|---|---|
| BERT, text only | 0.70 | 0.45 | 0.15 | 0.28 | 0.22 | 0.06 |
| BERT + Wav2Vec | 0.80 | 0.50 | 0.13 | 0.35 | 0.23 | 0.04 |
| RoBERTa, text only | 0.53 | 0.50 | 0.32 | 0.29 | 0.30 | 0.17 |
| RoBERTa + CLAP | 0.74 | 0.45 | 0.23 | 0.37 | 0.31 | 0.12 |

*F1 per fallacy category, averaged over the 28 runs (Table 6 of the paper).*

Audio alone is weak, close to the random baseline, but adding it to BERT or RoBERTa raises the average macro-F1.
The gain is statistically significant for BERT (p-value below 0.05) but not for RoBERTa, and SBERT drops when audio is added.
The gains are uneven across categories: Appeal to Emotion and False Cause improve the most, while text-only models are as good or better on Slogans, the rarest category.
Results also vary across debates, and recent debates tend to benefit more from audio.

## Takeaways

{{< takeaways >}}
- title: A first multimodal fallacy corpus.
  text: MM-USED-fallacy pairs 1,891 annotated fallacy passages from 28 US presidential debates with their audio. The corpus and code are public.
- title: Audio helps text, not alone.
  text: Adding audio raises average macro-F1 from 0.32 to 0.40 for BERT, a statistically significant gain. For RoBERTa it rises from 0.38 to 0.40, a gain that is not significant, and audio-only models stay near the random baseline.
- title: The benefit depends on the fallacy.
  text: Appeal to Emotion gains the most from audio, while Slogans do not. The annotations come from text only, so a new annotation that listens to the audio could reveal more.
{{< /takeaways >}}
