---
title: 'MAMKit: A Comprehensive Multimodal Argument Mining Toolkit'

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- Eleonora Mancini
- Federico Ruggeri
- Stefano Colamonaco
- Andrea Zecca
- Samuele Marro
- Paolo Torroni

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2024-08-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2026-02-27T15:55:09.413350Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- paper-conference

# Publication name and optional abbreviated publication name.
publication: '*Proceedings of the 11th Workshop on Argument Mining (ArgMining 2024)*'
publication_short: ''

doi: 10.18653/v1/2024.argmining-1.7

abstract: Multimodal Argument Mining (MAM) is a recent area of research aiming to
  extend argument analysis and improve discourse understanding by incorporating multiple
  modalities. Initial results confirm the importance of paralinguistic cues in this
  field. However, the research community still lacks a comprehensive platform where
  results can be easily reproduced, and methods and models can be stored, compared,
  and tested against a variety of benchmarks. To address these challenges, we propose
  MAMKit, an open, publicly available, PyTorch toolkit that consolidates datasets
  and models, providing a standardized platform for experimentation. MAMKit also includes
  some new baselines, designed to stimulate research on text and audio encoding and
  fusion for MAM tasks. Our initial results with MAMKit indicate that advancements
  in MAM require novel annotation processes to encompass auditory cues effectively.

# Summary. An optional shortened abstract.
summary: MAMKit is an open PyTorch toolkit that puts multimodal argument mining datasets and models behind one interface, so results become easy to reproduce.

tags:
- toolkit
- MAMKit
- argument mining
- multimodal
- student publication
- audio

# Display this page in a list of Featured pages?
featured: false

# Links
url_pdf: ''
url_code: 'https://github.com/nlp-unibo/mamkit'
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
  caption: 'The five packages of MAMKit: data, models, modules, configs, and utility (Figure 1 of the paper).'
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
  url: https://aclanthology.org/2024.argmining-1.7
categories:
  - Workshop
aliases:
  - /publication_workshops/mancini-etal-2024-mamkit/
topics: [argument-mining, multimodal, toolkit, speech]
---

## Research setting

Argument mining is the automatic analysis of arguments in text, such as finding claims, the premises that support them, and the relations between them.
Political debates are a natural source of arguments, and they are spoken: the voice of a speaker carries paralinguistic cues, such as tone and pauses, that a transcript loses.
Multimodal argument mining (MAM) studies arguments from both the text and the audio of each sentence.
The paper covers four MAM tasks:

- **Argumentative sentence detection (ASD)** decides whether a sentence contains an argument or a component, such as a claim.
- **Argumentative component classification (ACC)** labels an argumentative sentence as a claim or a premise.
- **Argumentative relation classification (ARC)** labels a pair of sentences as support, attack, or no relation.
- **Argumentative fallacy classification (AFC)** assigns a sentence already known to be a fallacy, a flawed argument, to one category of a fallacy taxonomy.

{{< pipeline caption="The MAM setting of the paper (Sections 3.3 to 3.5). Each debate sentence comes with its audio snippet. A model reads both and predicts the label of one task." >}}
- title: Debate
  text: Transcripts and audio recordings of political debates.
  icon: microphone
- title: Aligned sentence
  text: Each sentence is paired with its audio snippet.
  icon: align-left
  branches:
    - title: Text
      text: Sentence transcript
    - title: Audio
      text: Speech snippet
- title: Multimodal model
  text: Encodes and fuses text and audio.
  icon: project-diagram
  highlight: true
- title: Task label
  text: One of the four tasks.
  icon: tag
  branches:
    - title: ASD, ACC
      text: Sentence labels
    - title: ARC
      text: Pair labels
    - title: AFC
      text: Fallacy category
{{< /pipeline >}}

## Motivation

Early MAM results suggest that the audio of a speaker helps argument analysis.
However, MAM datasets and models are spread across different sites and repositories, each with its own way of loading and rebuilding them.
This makes a fair comparison between models hard, and it slows the evaluation of new ones.
Toolkits with a shared interface exist for other areas of AI, but none supports argument mining.
Past MAM models also mostly merged unimodal models in a standard way and left recent audio encoders and fusion methods unexplored.

{{< gap caption="How MAMKit relates to the prior work discussed in the paper (Sections 1 and 2)." >}}
label: Resource
columns: [Built for argument mining, Shared interface for datasets and models, Recent audio encoders and fusion methods]
rows:
  - name: Earlier MAM models and datasets, each in its own repository
    cells: [true, false, false]
  - name: Language-vision libraries (LAVIS, MMF, X-modaler, UniLM)
    cells: [false, true, Other modalities]
  - name: Multimodal and audio tools (TorchMultimodal, ViLMedic, pyannote, Muskits)
    cells: [false, true, Other tasks]
  - name: Task-specific NLP libraries (LogiTorch, TextBox 2.0, DeepPavlov, and others)
    cells: [false, true, Text only]
  - name: This paper (MAMKit)
    ours: true
    cells: [true, true, true]
{{< /gap >}}

> **Objective.** Give MAM researchers one open, standardized platform where datasets and models can be loaded, compared, and reproduced, and use it to test new audio encoders and fusion methods.

## Approach

MAMKit is an open-source PyTorch toolkit organized in five packages, shown in the figure at the top of this page.
The data package loads, splits, and preprocesses each dataset for text-only, audio-only, or text-audio input.
The models and modules packages define the models and their shared layers.
The configs package stores the exact settings of published experiments, so a user can rebuild a model and its data processing from a single configuration key.
The utility package wraps every model for training and evaluation with PyTorch Lightning.

Every model in MAMKit follows the same structure: a text module, an audio module, a fusion layer that merges the two, and a classification head for the task.
Early fusion merges the two modalities near the input, while late fusion merges the outputs of two separate unimodal branches.

{{< pipeline caption="The structure shared by all MAMKit models (Section 3.3 and Table 1 of the paper). Wav2Vec 2.0, HuBERT, and WavLM are pre-trained speech models. MFCCs are classic hand-crafted audio features." >}}
- title: Text module
  text: GloVe with a BiLSTM, BERT, or RoBERTa.
  icon: file-alt
- title: Audio module
  text: Speech features, then a BiLSTM or a transformer.
  icon: wave-square
  branches:
    - title: Features
      text: Wav2Vec 2.0, HuBERT, WavLM, or MFCCs
- title: Fusion layer
  text: Merges text and audio.
  icon: compress-arrows-alt
  highlight: true
  branches:
    - title: Concat
      text: Concatenation, early or late
    - title: Average
      text: Late
    - title: Crossmodal attention
      text: One modality attends to the other
- title: Classification head
  text: Predicts the task label.
  icon: tag
{{< /pipeline >}}

MAMKit includes three models from earlier MAM work and three new ones.

| Model | Origin | Text module | Audio module | Fusion |
|---|---|---|---|---|
| BiLSTM | Earlier work | GloVe + BiLSTM | Wav2Vec 2.0 or MFCCs + BiLSTM | Concatenation, late |
| MM-BERT | Earlier work | BERT | Wav2Vec 2.0, HuBERT, or WavLM + BiLSTM | Concatenation, late |
| MM-RoBERTa | Earlier work | RoBERTa | Wav2Vec 2.0, HuBERT, or WavLM + BiLSTM | Concatenation, late |
| **CSA** | This paper | BERT | Wav2Vec 2.0, HuBERT, or WavLM + transformer | Concatenation, early |
| **Ensemble** | This paper | BERT | Wav2Vec 2.0, HuBERT, or WavLM + transformer | Average, late |
| **Mul-TA** | This paper | BERT | Wav2Vec 2.0, HuBERT, or WavLM + transformer | Crossmodal attention |

*Models available in MAMKit. Source: Table 1 of the paper.*

- **CSA** joins the text and audio sequences into one sequence and applies self-attention. Audio sequences are often about ten times longer than text, so CSA rescales the attention scores to give text and audio the same total weight.
- **Ensemble** trains a text-only and an audio-only model and averages their predicted probabilities with a learned weight. The weight is bounded between 0.3 and 0.7, so the ensemble cannot ignore either modality.
- **Mul-TA** adapts a multimodal transformer to text and audio. In each crossmodal attention layer, one modality queries the other, so the two sequences need no alignment.

{{< figure src="csa.png" caption="The CSA model joins text and audio embeddings into one sequence for a transformer with rescaled attention (Figure 2 of the paper)." >}}

## Results

The paper evaluates every MAMKit model on every supported task and dataset:

- **UKDebates** has 386 sentences from a 2015 UK Prime Ministerial election debate, labeled as containing a claim or not (ASD).
- **M-Argγ** has 2,443 sentence pairs from the 2020 US presidential debates, kept for their high annotator agreement and labeled for relations (ARC).
- **MM-USED** has 26,781 sentences from 39 US presidential debates, from 1960 to 2016, labeled for detection (ASD) and for claims and premises (ACC). It is the largest MAM resource to date.
- **MM-USED-fallacy** has 1,891 sentences labeled with six fallacy categories (AFC).

The metric is macro F1, the F1 score averaged over classes, except on UKDebates, where it is the binary F1 of the claim class.
Scores range from 0 to 1, and higher is better.
Each score is the best configuration of a model, averaged over repeated runs.

{{< numbers >}}
- value: ".697"
  label: macro F1 of Mul-TA on MM-USED (ACC), against .679 for its text-only module
- value: ".657"
  label: macro F1 of an audio-only BiLSTM on MM-USED-fallacy (AFC), the best of all models
- value: ".692"
  label: binary F1 of text-only RoBERTa on UKDebates (ASD), above every text-audio model
{{< /numbers >}}

{{< bars caption="Fallacy classification, the only task where audio-only models lead. Source: Table 2 of the paper (mean and standard deviation over runs)." >}}
metric: Macro F1 on MM-USED-fallacy (AFC)
unit: ""
min: 0
max: 1
bars:
  - label: BiLSTM, text only
    value: ".525"
    err: ".113"
  - label: BERT, text only
    value: ".594"
    err: ".122"
  - label: RoBERTa, text only
    value: ".615"
    err: ".097"
  - label: BiLSTM, audio only
    value: ".657"
    err: ".000"
  - label: Transformer, audio only
    value: ".629"
    err: ".162"
  - label: BiLSTM, text and audio
    value: ".572"
    err: ".099"
  - label: MM-BERT
    value: ".599"
    err: ".128"
  - label: MM-RoBERTa
    value: ".624"
    err: ".074"
  - label: CSA
    value: ".582"
    err: ".114"
    ours: true
  - label: Ensemble
    value: ".612"
    err: ".134"
    ours: true
  - label: Mul-TA
    value: ".605"
    err: ".110"
    ours: true
{{< /bars >}}

| Model | Input | UKDebates (ASD) | M-Argγ (ARC) | MM-USED (ASD) | MM-USED (ACC) | MM-USED-fallacy (AFC) |
|---|---|---|---|---|---|---|
| BiLSTM | Text | .552 | .120 | .811 | .663 | .525 |
| BERT | Text | .654 | .132 | .824 | .679 | .594 |
| RoBERTa | Text | **.692** | .172 | .839 | .680 | .615 |
| BiLSTM | Audio | .393 | .024 | .774 | .596 | **.657** |
| Transformer | Audio | .455 | .000 | .771 | .526 | .629 |
| BiLSTM | Both | .533 | .084 | .815 | .667 | .572 |
| MM-BERT | Both | .662 | .160 | **.841** | .680 | .599 |
| MM-RoBERTa | Both | .687 | **.178** | .837 | .678 | .624 |
| CSA (this paper) | Both | .663 | .160 | .833 | .693 | .582 |
| Ensemble (this paper) | Both | .586 | .011 | .826 | .681 | .612 |
| Mul-TA (this paper) | Both | .616 | .098 | .837 | **.697** | .605 |

*Best score of each model on each task. Input is text, audio, or both. Source: Table 2 of the paper.*

On UKDebates, adding audio brings no benefit: text-audio models score the same as or below their text-only modules.
On M-Argγ, audio-only models fail to learn the task, and only MM-BERT and CSA score slightly above their text-only modules.
On MM-USED, audio-only models come close to text-only ones, but text-audio models improve on their text modules by at most 1.8 points on a 0 to 100 scale.
On MM-USED-fallacy, audio-only models lead, and text-audio models fall between text-only and audio-only ones.
The paper suggests one cause: every dataset was first annotated on transcripts and only later aligned to audio, so the labels do not reflect acoustic cues.

## Takeaways

{{< takeaways >}}
- title: MAM now has a shared platform.
  text: MAMKit offers 4 datasets and 6 models behind one interface, and it rebuilds published experiments from a configuration key.
- title: New audio encoders and fusion methods gave small gains.
  text: The three new models did not bring the improvement the authors hoped for, and text-only models remain strong baselines.
- title: Annotation should start from the audio.
  text: Labels made on transcripts miss auditory cues, so progress in MAM needs annotation processes that include them.
{{< /takeaways >}}
