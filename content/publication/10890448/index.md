---
title: 'LMAC-TD: Producing Time Domain Explanations for Audio Classifiers'

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- Eleonora Mancini
- Francesco Paissan
- Mirco Ravanelli
- Cem Subakan

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2025-01-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2026-03-02T12:28:22.122528Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- paper-conference

# Publication name and optional abbreviated publication name.
publication: '*ICASSP 2025 - 2025 IEEE International Conference on Acoustics, Speech
  and Signal Processing (ICASSP)*'
publication_short: ''

doi: 10.1109/ICASSP49660.2025.10890448

abstract: 'Neural networks are typically black-boxes that remain opaque with regards to their decision mechanisms. Several works in the literature have proposed post-hoc explanation methods to alleviate this issue. This paper proposes LMAC-TD, a post-hoc explanation method that trains a decoder to produce explanations directly in the time domain. This methodology builds upon the foundation of L-MAC, Listenable Maps for Audio Classifiers, a method that produces faithful and listenable explanations. We incorporate SepFormer, a popular transformer-based time-domain source separation architecture. We show through a user study that LMAC-TD significantly improves the audio quality of the produced explanations while not sacrificing from faithfulness.'

# Summary. An optional shortened abstract.
summary: LMAC-TD explains an audio classifier with a listenable clip decoded directly as a waveform, which improves perceived audio quality without losing faithfulness.

tags:
- measurement
- source separation
- neural networks
- transformers
- acoustics
- decoding
- time-domain analysis
- speech processing
- neural network explanations
- explainable deep learning
- interpretability
- audio classification
- listenable explanations

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
  caption: "LMAC-TD trains a time-domain decoder, built from SepFormer, on top of a frozen audio classifier (schema drawn for this page from Section II of the paper)."
  focal_point: ''
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects: ['internal-project']` links to `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []
categories:
  - Conference
aliases:
  - /publication_conferences/10890448/
topics: [interpretability, speech]
---

## Research setting

Audio classifiers are neural networks that assign a class to a sound clip, but their decision mechanisms remain opaque.
A post-hoc explanation method leaves the trained classifier unchanged and adds a separate interpreter that points to the parts of the input behind the decision.
For audio, a listenable explanation is itself a sound: the part of the clip that drove the decision, which a person can play and hear.
A waveform is the raw sequence of audio samples, and a spectrogram is a time and frequency picture of the sound.
This paper produces the explanation in the time domain, that is, directly as a waveform instead of as a spectrogram.

{{< svg src="setting.svg" caption="The task. The classifier stays fixed, and the interpreter returns an explanation i(t) plus the masked-out rest of the clip. Schema drawn for this page from the definitions in Section II of the paper." >}}

## Motivation

Earlier listenable methods such as SLIME and AudioLIME score regions or separated sources of the input.
L2I and L-MAC (Listenable Maps for Audio Classifiers) train a decoder instead, and L-MAC drops the pre-trained NMF dictionary (a fixed set of spectral patterns) that L2I needs.
L-MAC gives faithful explanations, but it masks the magnitude STFT, a spectrogram without phase.
To turn the masked spectrogram back into sound, it reuses the phase of the input mixture, and this causes artifacts.

{{< gap caption="How the paper positions LMAC-TD against the listenable explanation methods it discusses (Section I of the paper)." >}}
label: Method
columns: [Listenable explanation, Trained decoder, No pre-trained NMF dictionary, Waveform output without the input phase]
rows:
  - name: SLIME (Mishra et al., 2017)
    cells: [true, false, "n/a", "not discussed"]
  - name: AudioLIME (Haunschmid et al., 2020)
    cells: [true, false, "n/a", "not discussed"]
  - name: L2I (Parekh et al., 2022)
    cells: [true, true, false, "not discussed"]
  - name: L-MAC (Paissan et al., 2024)
    cells: [true, true, true, false]
  - name: This paper (LMAC-TD)
    ours: true
    cells: [true, true, true, true]
{{< /gap >}}

> **Objective.** Improve the audio quality of L-MAC explanations by generating them directly in the time domain, without losing faithfulness to the classifier.

## Approach

LMAC-TD adds parts of SepFormer, a transformer model for time-domain source separation (splitting a recording into its sources), to the L-MAC interpreter.
A UNet decoder maps the classifier representations, and a SepFormer encoder maps the input waveform, to two latent maps of the same shape.
A weight α between 0 and 1 mixes the two maps, and the SepFormer MaskNet turns the mix into a mask over the encoded input.
The SepFormer decoder turns the masked input into the explanation waveform, and the inverse mask gives the masked-out rest.
A masking loss then trains the interpreter so that the frozen classifier keeps its decision on the explanation and loses it on the masked-out rest.

{{< stages caption="What is trained and what stays frozen in LMAC-TD (Section II and Figure 1 of the paper)." >}}
flow: [Input audio, Classifier, UNet decoder, SepFormer, i(t)]
stages:
  - title: 1. Read the classifier
    text: The audio goes through the frozen classifier, a CNN14 network on a Mel spectrogram, and the interpreter keeps its last four representations.
    states: {Input audio: data, Classifier: frozen}
  - title: 2. Build the mask
    text: The UNet decoder maps the representations to the SepFormer latent space, mixes them with the encoded input through α, and the MaskNet outputs a mask.
    states: {Input audio: data, Classifier: frozen, UNet decoder: trained, SepFormer: trained}
  - title: 3. Decode the waveform
    text: The SepFormer decoder turns the masked encoding into the explanation i(t), with no phase borrowed from the input.
    states: {UNet decoder: trained, SepFormer: trained, i(t): data}
  - title: 4. Check against the classifier
    text: The frozen classifier scores the explanation and the masked-out rest. The masking loss, with an ℓ1 penalty on the spectrogram of i(t) against trivial solutions, updates only the interpreter.
    states: {Classifier: frozen, UNet decoder: trained, SepFormer: trained, i(t): data}
{{< /stages >}}

## Results

The classifier is a CNN14 fine-tuned on ESC50, a dataset of environmental sounds, with added noise.
Faithfulness means how well the explanation follows this classifier.
It is measured in domain on ESC50, and out of domain on mixtures of two ESC50 clips and on clips with white noise or speech added.
Average Increase (AI) is the rise in classifier confidence on the explanation, and Average Decrease (AD) is the confidence drop once the explanation is removed.
Faithfulness (FF) and input fidelity (Fid-In) are two further scores from earlier work, and for all of them except AD higher is better.
In a user study, 19 participants rated nine audio samples from 1 to 100 for match with the predicted class and for audio quality.
The average rating is the Mean Opinion Score (MOS).

{{< numbers >}}
- value: "69.75"
  label: AI in domain for LMAC-TD (α = 0.75), against 36.25 for L-MAC
- value: "0.91"
  label: Fid-In in domain for LMAC-TD (α = 0.75), against 0.42 for L-MAC
- value: "19"
  label: participants in the listening study
{{< /numbers >}}

{{< bars caption="In-domain Average Increase on ESC50 for a selection of the methods in Table I of the paper, higher is better." >}}
metric: Average Increase (AI), in domain on ESC50
unit: ""
min: 0
max: 100
bars:
  - label: Saliency
    value: "0.00"
  - label: SHAP
    value: "0.00"
  - label: L2I
    value: "1.63"
  - label: GradCAM
    value: "8.50"
  - label: L-MAC with fine-tuning
    value: "32.37"
  - label: L-MAC
    value: "36.25"
  - label: LMAC-TD, α = 0
    value: "46.50"
    ours: true
  - label: LMAC-TD, α = 1
    value: "66.00"
    ours: true
  - label: LMAC-TD, α = 0.75
    value: "69.75"
    ours: true
{{< /bars >}}

| Setting | Method | AI ↑ | AD ↓ | FF ↑ | Fid-In ↑ |
|---|---|---|---|---|---|
| In domain | L-MAC | 36.25 | **1.15** | 0.20 | 0.42 |
| In domain | LMAC-TD, α = 0.75 | **69.75** | 2.10 | **0.42** | **0.91** |
| Two-clip mixtures | L-MAC | **60.63** | 4.82 | 0.39 | 0.81 |
| Two-clip mixtures | LMAC-TD, α = 0.75 | 59.50 | **3.42** | **0.41** | **0.87** |
| White noise added | L-MAC | **83.62** | **1.50** | 0.33 | **0.86** |
| White noise added | LMAC-TD, α = 0.75 | 63.50 | 3.06 | **0.35** | 0.83 |
| Speech added | L-MAC | **70.75** | **2.73** | 0.33 | 0.83 |
| Speech added | LMAC-TD, α = 0.75 | 62.63 | 2.95 | **0.43** | **0.90** |

*L-MAC against LMAC-TD with α = 0.75 (Tables I, II, and III of the paper). Arrows give the direction of improvement. The better value of each pair is in bold.*

In domain, LMAC-TD with α = 0.75 beats L-MAC on every faithfulness metric except AD, which stays close.
Out of domain, it keeps a higher FF in every setting, while L-MAC keeps a higher AI and, with added noise, a lower AD.
A larger α, which gives more weight to the classifier representations, generally gives more faithful explanations.
The complexity metric COMP (lower is better) is worse for LMAC-TD (10.53 against 4.71 in domain), which the authors relate to computing it on spectrograms of a waveform output.
In the user study, LMAC-TD with α = 1 and α = 0.75 obtained the highest MOS, above L-MAC and L-MAC with fine-tuning, while α = 0 was comparable to L-MAC and still above L2I.

## Takeaways

{{< takeaways >}}
- title: Explain audio with audio.
  text: Decoding the explanation directly as a waveform avoids reusing the input phase, and listeners gave the explanations with α = 1 and α = 0.75 a higher MOS than those of L-MAC.
- title: Faithfulness holds.
  text: In domain, LMAC-TD with α = 0.75 nearly doubles the Average Increase of L-MAC, and out of domain it stays comparable while keeping a higher FF.
- title: One knob for the trade-off.
  text: The weight α balances classifier representations against the raw input, and higher values generally give more faithful explanations.
{{< /takeaways >}}
