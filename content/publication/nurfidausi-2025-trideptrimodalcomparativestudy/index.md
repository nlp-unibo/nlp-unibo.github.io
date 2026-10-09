---
title: 'TRI-DEP: A Trimodal Comparative Study for Depression Detection Using Speech,
  Text, and EEG'

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- Annisaa Fitri Nurfidausi
- Eleonora Mancini
- Paolo Torroni

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2025-10-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2026-03-02T12:28:22.224084Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- article

# Publication name and optional abbreviated publication name.
publication: ''
publication_short: ''

doi: ''

abstract: Depression is a widespread mental health disorder, yet its automatic detection remains challenging. Prior work has explored unimodal and multimodal approaches, with multimodal systems showing promise by leveraging complementary signals. However, existing studies are limited in scope, lack systematic comparisons of features, and suffer from inconsistent evaluation protocols. We address these gaps by systematically exploring feature representations and modelling strategies across EEG, together with speech and text. We evaluate handcrafted features versus pre-trained embeddings, assess the effectiveness of different neural encoders, compare unimodal, bimodal, and trimodal configurations, and analyse fusion strategies with attention to the role of EEG. Consistent subject-independent splits are applied to ensure robust, reproducible benchmarking. Our results show that (i) the combination of EEG, speech and text modalities enhances multimodal detection, (ii) pretrained embeddings outperform handcrafted features, and (iii) carefully designed trimodal models achieve state-of-the-art performance. Our work lays the groundwork for future research in multimodal depression detection.

# Summary. An optional shortened abstract.
summary: A fair, reproducible benchmark of EEG, speech, and interview text for depression detection, showing that fusing all three signals works best.
card_summary: A reproducible benchmark showing that combining EEG, speech, and text improves depression detection.

topics: [multimodal, speech, benchmark, reproducibility]

tags:
- speech
- multimodality
- depression detection
- EEG
- late fusion
- pretrained embeddings

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
  caption: "The TRI-DEP framework: the best EEG, speech, and text pipelines are fused at the decision level (Figure 1 of the paper)."
  focal_point: ''
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects: ['internal-project']` links to `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []
links:
- name: arXiv
  url: https://arxiv.org/abs/2510.14922
categories:
  - Preprint
aliases:
  - /publication_preprints/nurfidausi-2025-trideptrimodalcomparativestudy/
---

## Research setting

Automatic depression detection trains a model to tell people with Major Depressive Disorder (MDD) apart from healthy controls (HC), to support clinical decisions and telemedicine.
A clinical session offers several signals at once, because human expression spans speech, language, and neural activity.
This study uses the public MODMA dataset, which pairs a 5-minute resting-state EEG recording with the audio of a structured clinical interview for each person.
The authors keep the 38 subjects who have both recordings.

{{< pipeline caption="The task: three signals from one person go in, and one label (MDD or healthy control) comes out." >}}
- title: Three signals per subject
  text: Each signal captures a different side of the person.
  icon: wave-square
  branches:
    - title: EEG
      text: Electrical brain activity at rest, 128 channels
    - title: Speech
      text: Audio of 29 interview answers
    - title: Text
      text: Automatic transcripts of those answers
- title: Classifier
  text: Learns depression cues from the signals.
  icon: project-diagram
- title: Label
  text: MDD or healthy control.
  icon: tag
{{< /pipeline >}}

Terms used on this page:

- **Handcrafted features** are measurements designed by experts, such as spectral power for EEG or MFCCs (a standard description of the sound spectrum) and prosody for speech.
- **Pretrained embeddings** are vectors produced by large models trained beforehand on other data, such as HuBERT for speech, MacBERT for text, and the brain-signal models LaBraM and CBraMod for EEG.
- **Late fusion** trains one model per signal and combines only their final predictions.
- **Subject-level split** means that all recordings of a person go either to training or to testing, never to both.
- **Macro-F1** is the F1 score (the balance of precision and recall) computed for each class and then averaged, so both classes count equally. It ranges from 0 to 1, and higher is better.

## Motivation

Most prior systems combine only two signals, and most of them leave out text.
Few compare handcrafted features with pretrained embeddings, and fusion strategies are rarely explored.
Many studies also do not say how they split the data, and a segment-level split can place recordings of the same person in both training and test sets, which inflates scores.

{{< gap caption="How the paper positions itself against the related work it discusses (Introduction and Section 2.1 of the paper)." >}}
label: Study
columns: [EEG + speech + text, Handcrafted vs pretrained features, Several fusion strategies, Clear subject-level splits]
rows:
  - name: EEG and speech with image models (Yousufi et al.; Qayyum et al.)
    cells: [false, "not discussed", "not discussed", false]
  - name: Speech and text comparative analysis (Daly et al.)
    cells: [false, "not discussed", true, "not discussed"]
  - name: Trimodal GAT-CNN-MPNet (He et al., 2024)
    cells: [true, false, "basic only", false]
  - name: This paper (TRI-DEP)
    ours: true
    cells: [true, true, true, true]
{{< /gap >}}

> **Objective.** Build a reproducible benchmark for depression detection from EEG, speech, and text. Find out which features, models, and fusion strategies work best, and what EEG adds.

## Approach

MODMA has no transcripts, so the authors transcribe the interviews automatically with WhisperX.
For each signal, they compare handcrafted features with pretrained embeddings and train several small neural classifiers on top.
They keep the best feature and classifier pair per signal and combine the three predictions with weighted averaging, Bayesian fusion, or majority voting.
Fusion weights are chosen by grid search.
Every experiment uses the same stratified 5-fold subject-level splits, which the authors release.

{{< stages caption="The benchmark protocol, run on the same five subject-level folds." >}}
flow: [Signals, Features, Classifier, Prediction, Fusion]
legend:
  evolved: Weights set by grid search
stages:
  - title: 1. Extract features
    text: Each signal is cut into segments and turned into handcrafted features or pretrained embeddings.
    states: {Signals: data, Features: data}
  - title: 2. Train one classifier per signal
    text: A separate classifier (CNN, LSTM, or GRU based) learns to predict the label from each signal's features.
    states: {Signals: data, Features: data, Classifier: trained, Prediction: data}
  - title: 3. Fuse the best predictions
    text: The best classifier per signal is kept fixed, and its predictions are combined with fusion weights found by grid search.
    states: {Signals: data, Features: data, Classifier: frozen, Prediction: data, Fusion: evolved}
{{< /stages >}}

{{< pipeline caption="The final framework: the best model for each signal, fused at the decision level." >}}
- title: Inputs
  text: EEG, speech, and WhisperX text.
  icon: brain
- title: Per-signal models
  text: Best features and classifier for each signal.
  icon: wave-square
  branches:
    - title: EEG
      text: CBraMod and a CNN
    - title: Speech
      text: HuBERT and a CNN with a BiGRU
    - title: Text
      text: MacBERT and an LSTM
- title: Late fusion
  text: Combines the three outputs.
  icon: layer-group
  highlight: true
{{< /pipeline >}}

## Results

The authors measure macro-F1 on the 38 MODMA subjects, as the mean and standard deviation over the 5 subject-level folds.
As baselines, they re-run two published EEG and speech image models (ViT and DenseNet-121) on the same splits, so these scores are not directly comparable to the original papers.

{{< numbers >}}
- value: "0.864"
  label: macro-F1 when fusing EEG, speech, and text
- value: "0.809"
  label: macro-F1 of the best single signal (speech)
- value: "0.586"
  label: macro-F1 of the best re-run baseline
{{< /numbers >}}

{{< bars caption="Best configuration per setting, macro-F1 averaged over 5 subject-level folds; whiskers show one standard deviation. Source: Tables 3 and 4 of the paper." >}}
metric: Macro-F1 (mean over 5 folds)
unit: ""
min: 0
max: 1
bars:
  - label: ViT baseline (EEG + speech)
    value: "0.560"
    err: "0.190"
  - label: DenseNet-121 baseline (EEG + speech)
    value: "0.586"
    err: "0.240"
  - label: EEG only (CBraMod + CNN)
    value: "0.446"
    err: "0.106"
    ours: true
  - label: Text only (MacBERT + LSTM)
    value: "0.784"
    err: "0.114"
    ours: true
  - label: Speech only (HuBERT)
    value: "0.809"
    err: "0.081"
    ours: true
  - label: Speech + text, weighted averaging
    value: "0.839"
    err: "0.059"
    ours: true
  - label: EEG + speech + text, weighted averaging
    value: "0.864"
    err: "0.095"
    ours: true
{{< /bars >}}

| Signal | Best handcrafted features | Best pretrained embeddings |
|---|---|---|
| EEG | 0.418 (statistical, spectral, entropy) | 0.446 (CBraMod) |
| Speech | 0.655 (prosody + MFCCs) | 0.809 (Chinese HuBERT) |

*Macro-F1, mean over 5 folds (Table 3 of the paper). Text was tested with pretrained embeddings only.*

Speech is the strongest single signal, text comes close, and EEG alone stays below 0.5 macro-F1.
Pretrained embeddings beat handcrafted features, most clearly for speech.
Fusing all three signals gives the best score, 0.864 macro-F1 with both weighted averaging and Bayesian fusion, about 5.5 points above speech alone.
With only 38 subjects and 5 folds, no pairwise difference is statistically significant at α = 0.05, so the gains show a consistent direction rather than a proven effect.

## Takeaways

{{< takeaways >}}
- title: Three signals beat one.
  text: Trimodal late fusion reaches 0.864 macro-F1, the best result in the study. EEG is weak alone but adds complementary information when combined with speech and text.
- title: Pretrained embeddings win.
  text: Embeddings from pretrained models outperform handcrafted features. Speech embeddings from Chinese HuBERT give the strongest single signal.
- title: Fair splits matter.
  text: Published image-model baselines, re-run on the same subject-level splits, reach only 0.560 and 0.586 macro-F1. The released splits and code make future comparisons reproducible.
{{< /takeaways >}}
