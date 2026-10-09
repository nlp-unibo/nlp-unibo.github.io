---
title: Investigating the effectiveness of explainability methods in Parkinson’s detection
  from speech

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- Eleonora Mancini
- Francesco Paissan
- Paolo Torroni
- Mirco Ravanelli
- Cem Subakan

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2025-01-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2026-03-02T12:28:22.201249Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- paper-conference

# Publication name and optional abbreviated publication name.
publication: '*2025 IEEE International Conference on Acoustics, Speech, and Signal
  Processing Workshops (ICASSPW)*'
publication_short: ''

doi: 10.1109/icasspw65056.2025.11011035

abstract: "Speech impairments in Parkinson’s disease (PD) provide significant early indicators for diagnosis. While models for speech-based PD detection have shown strong performance, their interpretability remains underexplored. This study systematically evaluates several explainability methods to identify PD-specific speech features, aiming to support the development of accurate, interpretable models for clinical decision-making in PD diagnosis and monitoring. Our methodology involves (i) obtaining attributions and saliency maps using mainstream interpretability techniques, (ii) quantitatively evaluating the faithfulness of these maps and their combinations obtained via union and intersection through a range of established metrics, and (iii) assessing the information conveyed by the saliency maps for PD detection from an auxiliary classifier. Our results reveal that, while explanations are aligned with the classifier, they often fail to provide valuable information for domain experts."

# Summary. An optional shortened abstract.
summary: A systematic test of six explanation methods for a speech-based Parkinson's detector, showing faithful explanations that domain experts still cannot easily read.

tags:
- explainability
- parkinson's disease
- saliency maps
- speech
- faithfulness

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
  caption: "The three-step evaluation: saliency maps from six explanation methods, faithfulness metrics, and a classifier trained on the maps (schema drawn for this page from Section III of the paper)."
  focal_point: ''
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects: ['internal-project']` links to `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []
categories:
  - Workshop
aliases:
  - /publication_conferences/mancini-2025-investigating/
topics: [interpretability, speech, biomedical]
---

## Research setting

Parkinson's disease (PD) is a progressive disorder of the nervous system, and speech problems often appear in its early stages.
Speech analysis is non-invasive and cheap, so models that detect PD from a voice recording are a promising aid to diagnosis.
These models are accurate, but they do not say why they label a person as PD or healthy control (HC).
This paper studies post-hoc explanation methods, which leave a trained detector unchanged and return a saliency map.
A saliency map gives a score to each cell of the spectrogram, a time and frequency picture of the sound, and so shows which parts drove the label.

{{< svg src="setting.svg" caption="The task. The detector stays fixed, and an explanation method marks the spectrogram cells behind its decision. Illustrative schema drawn for this page from the definitions in Section III of the paper." >}}

Terms used on this page:

- **Gradient-based methods** build the map from how the detector's output changes with each input cell. The paper tests Saliency, SmoothGrad, Integrated Gradients, Guided GradCAM, Guided Backprop, and Gradient SHAP.
- **Faithfulness** means that the map agrees with the detector: keeping the marked cells should keep the decision, and removing them should change it.
- **IoU** (intersection over union) measures how much two saliency maps overlap, from 0 (no shared cells) to 1 (identical maps).

## Motivation

Most work on speech-based PD detection reports accuracy and pays little attention to interpretability.
Some studies show GradCAM or EigenCAM maps, but they do not check them with numbers.
Studies that use SHAP explain features such as MFCCs (a compact summary of the sound spectrum), which do not map directly to what a clinician hears.

{{< gap caption="How the paper positions itself against the PD detection work it discusses (Section II of the paper)." >}}
label: Study
columns: [Explains the decision, Quantitative check of the explanations, Several methods compared]
rows:
  - name: CNNs on spectrograms (Sonawane and Sharma, 2021; Rios-Urrego et al., 2022)
    cells: [false, false, false]
  - name: GradCAM or EigenCAM maps for PD detection
    cells: [true, false, "not discussed"]
  - name: SHAP on MFCC features (Maffia et al., 2023)
    cells: [true, "not discussed", false]
  - name: This paper
    ours: true
    cells: [true, true, true]
{{< /gap >}}

> **Objective.** Evaluate several mainstream explanation methods for a speech-based PD detector in a systematic way, and find out whether their saliency maps highlight speech features that are specific to PD.

## Approach

The detector is HuBERT, a speech model pre-trained without labels and fine-tuned to tell PD from HC.
HuBERT reads the raw waveform, so the authors compute the explanations on the spectrogram and turn it back into a waveform before it enters the detector.
Each saliency map is then scored with faithfulness metrics, alone and combined with a second map by intersection or union.
Then a new classifier, CNN14, learns to separate PD from HC using only the saliency maps.
Selective metrics scale its accuracy and F1 score by one minus the mean value of the map, so a map that marks the whole input scores lower.

{{< stages caption="The evaluation protocol, from the detector to the classifier trained on its explanations (Section III of the paper)." >}}
flow: [Speech, HuBERT detector, Saliency maps, Metrics, CNN14 classifier]
stages:
  - title: 1. Explain the detector
    text: HuBERT is trained on the PD task and then kept fixed. Six explanation methods compute a saliency map for each test recording.
    states: {Speech: data, HuBERT detector: frozen, Saliency maps: data}
  - title: 2. Score the maps
    text: Metrics check whether masking the input with each map keeps or removes the decision of the fixed detector. Pairs of maps are also combined by intersection and union.
    states: {Speech: data, HuBERT detector: frozen, Saliency maps: data, Metrics: data}
  - title: 3. Learn from the maps
    text: CNN14 is trained on the saliency maps alone, to test how much PD information they carry.
    states: {Saliency maps: data, CNN14 classifier: trained}
{{< /stages >}}

## Results

The data is s-PC-GITA, Spanish recordings of 50 people with PD and 50 healthy controls, with results averaged over 10 folds.
The HuBERT detector reaches 81.32% accuracy and 81.03% F1 score.
Average Increase (AI) is the share of samples where the detector grows more confident on the explanation, and Average Decrease (AD) is the drop in confidence once the input is masked.
The other faithfulness metrics are Average Gain (AG), Faithfulness (FF), and input fidelity (Fid-In), while Sparseness (SPS) and Complexity (COMP) measure how concise a map is.

{{< numbers >}}
- value: "0.89"
  label: accuracy of CNN14 trained on Integrated Gradients maps
- value: "0.82"
  label: accuracy of CNN14 trained on the original spectrograms
- value: "ρ = -0.92"
  label: correlation between AD and IoU for intersected maps
{{< /numbers >}}

| Method | AI ↑ | AD ↓ | FF ↑ | Fid-In ↑ | SPS ↑ | COMP ↓ |
|---|---|---|---|---|---|---|
| Saliency | 74.66 | 1.80 | 0.004 | 82.82 | 0.69 | 11.98 |
| SmoothGrad | 75.10 | 1.85 | 0.004 | 81.89 | 0.50 | 12.51 |
| Guided GradCAM | 64.99 | 5.24 | 0.001 | **82.85** | **0.83** | **10.69** |
| Guided Backprop | 75.21 | 1.62 | 0.005 | 82.67 | 0.70 | 11.94 |
| Integrated Gradients | **78.83** | **1.22** | **0.013** | 81.93 | 0.77 | 11.69 |
| Gradient SHAP | 76.55 | 2.26 | 0.004 | 81.93 | 0.69 | 11.99 |

*Mean over 10 folds on s-PC-GITA; arrows show the better direction and bold marks the best value (Table I of the paper, which also reports AG and standard deviations).*

{{< bars caption="Accuracy of the CNN14 classifier trained on each method's saliency maps, against training on the original spectrograms; whiskers show one standard deviation. Source: Table III of the paper." >}}
metric: Accuracy of CNN14 (PD vs HC)
unit: ""
min: 0
max: 1
bars:
  - label: Original spectrograms
    value: "0.82"
    err: "0.12"
  - label: Guided GradCAM maps
    value: "0.78"
    err: "0.09"
  - label: Gradient SHAP maps
    value: "0.84"
    err: "0.13"
  - label: SmoothGrad maps
    value: "0.86"
    err: "0.11"
  - label: Saliency maps
    value: "0.87"
    err: "0.12"
  - label: Guided Backprop maps
    value: "0.87"
    err: "0.10"
  - label: Integrated Gradients maps
    value: "0.89"
    err: "0.08"
{{< /bars >}}

All six methods give comparable faithfulness, and the large spread across folds follows the spread of the detector itself.
Integrated Gradients is best on AI, AD, AG, and FF, while Guided GradCAM gives the most concise maps.
When two maps are intersected, a larger overlap goes with better scores: FF rises with IoU (ρ = 0.89) and AD falls (ρ = -0.92).
In most cases, a classifier trained on the maps beats one trained on the original spectrograms, and Integrated Gradients also has the highest selective accuracy, 0.88.
Still, the maps tend to focus on high-frequency regions and are not easy for people to interpret.

## Takeaways

{{< takeaways >}}
- title: Explanations follow the detector.
  text: All six methods produce saliency maps that agree with the HuBERT detector, and Integrated Gradients scores best on most faithfulness metrics.
- title: Maps carry PD information.
  text: A classifier trained only on Integrated Gradients maps reaches 0.89 accuracy, above the 0.82 it reaches on the original spectrograms.
- title: Faithful is not readable.
  text: The maps remain hard for domain experts to interpret. The authors suggest phoneme-level maps, links to known speech biomarkers, or listenable explanations as next steps.
{{< /takeaways >}}
