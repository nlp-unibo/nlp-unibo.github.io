---
title: "Let Guidelines Guide You: A Prescriptive Guideline-Centered Data Annotation Methodology"

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- Federico Ruggeri
- Eleonora Misino
- Arianna Muti
- Katerina Korre
- Paolo Torroni
- Alberto Barrón-Cedeño

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2026-09-18'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2026-03-02T16:18:34.217207Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- article-journal

# Publication name and optional abbreviated publication name.
publication: '*Transactions of the Association for Computational Linguistics (TACL)*'
publication_short: ''

doi: 10.1162/tacl.a.804

abstract: We introduce Guideline-Centered Annotation Methodology (GCAM), a novel methodology designed to report the annotation guidelines associated with each data instance. GCAM addresses four key limitations of the standard application of the prescriptive annotation methodology by reducing the information loss during annotation, ensuring adherence to guidelines, and enabling the efficient reuse of annotated data across multiple tasks that rely on the same guidelines. We evaluate GCAM with a focus on text classification tasks through (i) a human annotation study and (ii) an experimental evaluation with several machine learning models. Our results highlight the advantages of GCAM from multiple perspectives, guaranteeing a transparent evaluation of the successful application of the prescriptive paradigm and enabling a fine-grained model error analysis.
# Summary. An optional shortened abstract.
summary: GCAM has annotators report which guidelines apply to each text instead of a label, so adherence becomes checkable and one annotation serves many tasks.

tags:
- data annotation
- annotation guidelines
- prescriptive paradigm
- text classification
- inter-annotator agreement
topics: [reproducibility, interpretability, llms]

# Display this page in a list of Featured pages?
featured: false

# Links
url_pdf: 'https://direct.mit.edu/tacl/article-pdf/doi/10.1162/TACL.a.804/2629452/tacl.a.804.pdf'
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
  caption: "In standard annotation (SAM) the annotator maps a text to a label, while in GCAM the annotator maps it to guidelines and fixed functions map those guidelines to any class set (Figure 1 of the paper)."
  focal_point: ''
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects: ['internal-project']` links to `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []
links:
- name: arXiv preprint
  url: https://arxiv.org/abs/2406.14099
categories:
  - Highlight
  - Journal
aliases:
  - /publication_highlights/ruggeri-et-al-2026-gcam/
---

## Research setting

*Content warning: this page contains an example of offensive content from the paper.*

Many datasets for text classification are labeled by human annotators who follow written annotation guidelines.
A guideline is one textual criterion, such as "The entry derogates women by comparing them to non-human entities".
A class set is the list of labels of a task, such as `sexist` and `non-sexist`.
In the prescriptive paradigm, all annotators must apply one shared set of guidelines, and the standard annotation methodology (SAM) asks them to record only a class label for each text.

{{< figure src="setting.png" caption="(a) A guideline set and a class set for sexism detection. (b) In SAM, the annotator knows how guidelines map to classes and records only the label. (c) In GCAM, the annotator sees only the guidelines and records which ones apply; a fixed mapping then gives the label (panels a to c of Figure 1 of the paper)." >}}

## Motivation

When only the label is recorded, nobody knows which guideline the annotator used, or whether they used one at all.
Agreement between annotators is then measured on labels only, which can hide disagreement on the guidelines.
The labels are also tied to one class set, so a new formulation of the task needs a new round of human annotation.
Finally, models never see the guidelines, so it is unclear whether they learn the task that the guidelines describe.

{{< gap caption="How GCAM relates to the annotation methods discussed in the paper (Sections 1, 2 and 4)." >}}
label: Annotation method
columns: [Records the guidelines used for each text, Annotators do not see the class set, Reuse with a new class set without new annotation, Annotators report one kind of annotation only]
rows:
  - name: Standard annotation, SAM (Rottger et al., 2022)
    cells: [false, false, false, true]
  - name: Guidelines plus labels (Jikeli et al., 2023)
    cells: [true, false, false, false]
  - name: This paper (GCAM)
    ours: true
    cells: [true, true, true, true]
{{< /gap >}}

> **Objective.** Define an annotation methodology in which annotators report the guidelines that apply to each text instead of a class label, and compare it with standard annotation in a human study and in experiments with machine learning models.

## Approach

The Guideline-Centered Annotation Methodology (GCAM) splits annotation into two stages.
First, annotators see only the guidelines and select the subset of guidelines that applies to each text.
They never see the class set, so their choice must rest on the guidelines.
Second, a class grounding function, fixed by design and hidden from annotators, maps the selected guidelines to class labels.
Swapping this function gives labels for another class set from the same human annotation.

{{< stages caption="The two stages of GCAM and the reuse of its annotations (Section 3 and Figure 1 of the paper)." >}}
flow: [Input, Annotator, Selected, Grounding, Labels]
icons:
  trained: user-edit
  evolved: exchange-alt
  frozen: lock
labels:
  trained: Human work
  frozen: Fixed
  evolved: Swapped
legend:
  trained: Human work
  frozen: Fixed by design, not shown to annotators
  evolved: Swapped for a new class set
stages:
  - title: 1. Annotate with guidelines
    text: The input is a text and the guideline set, with no class set. The annotator reports the selected guidelines that apply. "Women are evil" gets guideline g1.
    states: {Input: data, Annotator: trained, Selected: data}
  - title: 2. Ground to classes
    text: The class grounding function maps each selected guideline to a class, with no annotator involved. Guideline g1 maps to sexist.
    states: {Selected: data, Grounding: frozen, Labels: data}
  - title: 3. Reuse for another task
    text: A different grounding function maps the same guidelines to another class set, for example animosity, threats, and derogation. No new human annotation is needed.
    states: {Selected: data, Grounding: evolved, Labels: data}
{{< /stages >}}

The paper tests GCAM in two ways.
In a human study, four annotators label 200 news sentences as subjective or objective with 12 guidelines, split in two batches of 100: one pair uses SAM and the other uses GCAM.
In model experiments, encoder models and three open LLMs (Mistral, Llama, Phi) are trained or prompted to predict labels or guidelines on two datasets that record both: ToS-100 (unfair clauses in Terms of Service, five unfairness categories) and EDOS (online sexism).

## Results

The human study measures inter-annotator agreement with Krippendorff's alpha, on labels for both pairs and on selected guidelines for the GCAM pair, and the annotation time per batch.
The model experiments report macro-F1, the average F1 score over classes, on labels and on guidelines, as the mean of 10 seed runs for encoders.

{{< numbers >}}
- value: "66 of 115"
  label: guideline disagreements between GCAM annotators that still agree on the label
- value: "~150 min"
  label: per batch of 100 sentences with GCAM, against ~60 min with SAM
- value: "80.14"
  label: macro-F1 on ToS-A for the guideline-trained encoder, against 71.61 with labels only
{{< /numbers >}}

{{< bars caption="Inter-annotator agreement on all 200 sentences of the human study (Appendix B of the paper)." >}}
metric: Krippendorff's alpha, as reported in the paper
unit: ""
min: 0
max: 100
bars:
  - label: SAM, class labels
    value: "57.90"
  - label: GCAM, class labels
    value: "50.97"
    ours: true
  - label: GCAM, guidelines
    value: "33.93"
    ours: true
{{< /bars >}}

Agreement on labels is comparable for the two methods (54.00 and 62.00 for SAM, 48.18 and 54.00 for GCAM, on the two batches).
Agreement on guidelines is much lower (29.28 and 38.74), so agreeing on a broad set of guidelines is notably harder.
GCAM makes this visible: 66 of the 115 disagreements (about 57%) agree on the label while reporting different guidelines, so a high label agreement can hide different reasons.
The price is time, since reporting guidelines takes longer than reporting labels.

| Dataset | Binary (SAM), labels | Fine-grained (GCAM), labels | Text-based (GCAM), labels | Fine-grained (GCAM), guidelines | Text-based (GCAM), guidelines |
|---|---|---|---|---|---|
| ToS-A | 71.61 | 65.31 | **80.14** <sup>∗, ∗∗</sup> | 18.33 | **37.49** <sup>∗∗</sup> |
| ToS-CH | 87.96 | 83.61 | **90.23** <sup>ns, ∗∗</sup> | 34.58 | **44.92** <sup>∗∗</sup> |
| ToS-CR | **79.02** | 67.85 | 78.14 <sup>ns, ∗∗</sup> | 17.37 | **27.21** <sup>∗∗</sup> |
| ToS-LTD | 75.87 | 73.70 | **80.39** <sup>∗∗, ∗∗</sup> | 19.87 | **21.49** <sup>ns</sup> |
| ToS-TER | **86.86** | 78.80 | 84.57 <sup>ns, ∗</sup> | 10.16 | **20.04** <sup>∗∗</sup> |
| EDOS | **81.74** | 71.67 | 79.87 <sup>∗, ∗∗</sup> | **27.09** | 22.97 <sup>∗∗</sup> |

*Macro-F1 of encoder models (LegalBERT on ToS-100, RoBERTaHate on EDOS), mean of 10 seed runs (Table 2 of the paper, left part). Binary predicts labels, Fine-grained treats each guideline as a class, Text-based reads each guideline text next to the input. Best values in bold, as in the paper. Superscripts give the Wilcoxon significance of Text-based against Binary and Fine-grained on labels, and against Fine-grained on guidelines: ns for not significant, ∗ for p ≤ 0.05, ∗∗ for p ≤ 0.01.*

On labels, the Text-based encoder significantly outperforms the label-only Binary model on ToS-A and ToS-LTD, shows no significant difference on ToS-CH, ToS-CR, and ToS-TER, and is significantly below it on EDOS (79.87 against 81.74).
It significantly outperforms Fine-grained on labels on every dataset, which shows the value of the guideline text.
On guidelines, it significantly outperforms Fine-grained on four of the five ToS targets, shows no significant difference on ToS-LTD, and is significantly below it on EDOS (22.97 against 27.09).
Guidelines also refine error analysis: for the Text-based model on EDOS, 423 test predictions have the right label for the wrong guideline, a case SAM counts as correct (Figure 2 of the paper).
Prompted zero-shot, the LLMs lose much of their performance when asked for guidelines, and in EDOS 60 to 71% of their predictions get both guideline and label wrong (Section 6.3).

## Takeaways

{{< takeaways >}}
- title: Record the reason, not only the label.
  text: When annotators report guidelines, one can check whether they followed them and see why they disagree, even when their labels match.
- title: Annotate once, reuse for many tasks.
  text: Labels come from a separate fixed mapping, so the same guideline annotations produce labels for several class sets without new human work.
- title: Guidelines help models and their evaluation.
  text: Encoders trained with guideline text perform as well as label-only training, and guideline errors separate right answers from right answers for the wrong reason.
{{< /takeaways >}}
