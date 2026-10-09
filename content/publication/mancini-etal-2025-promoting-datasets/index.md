---
title: Promoting the Responsible Development of Speech Datasets for Mental Health
  and Neurological Disorders Research

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- Eleonora Mancini
- Ana Tanevska
- Andrea Galassi
- Alessio Galatolo
- Federico Ruggeri
- Paolo Torroni

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2025-01-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2026-02-27T15:55:53.521228Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- article-journal

# Publication name and optional abbreviated publication name.
publication: '*Journal of Artificial Intelligence Research*'
publication_short: ''

doi: 10.1613/JAIR.1.16406

abstract: 'Current research in machine learning and artificial intelligence is largely centered on modeling and performance evaluation, less so on data collection. However, recent research demonstrated that limitations and biases in data may negatively impact trustworthiness and reliability. These aspects are particularly impactful on sensitive domains such as mental health and neurological disorders, where speech data are used to develop AI applications for patients and healthcare providers. In this paper, we chart the landscape of available speech datasets for this domain, to highlight possible pitfalls and opportunities for improvement and promote fairness and diversity. We present a comprehensive list of desiderata for building speech datasets for mental health and neurological disorders and distill it into an actionable checklist focused on ethical concerns to foster more responsible research.'

# Summary. An optional shortened abstract.
summary: 'A checklist for responsible speech datasets on mental health and neurological disorders shows that 36 dataset papers rarely report privacy and security measures.'

tags:
- speech datasets
- mental health
- neurological disorders
- data ethics
- checklist
- survey

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
  caption: "Seven desiderata distilled into checklist items C1 to C7, used to review 36 papers on speech datasets by target issue, discourse genre and source. Illustrative schema built from the paper's definitions."
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
  url: https://doi.org/10.1613/jair.1.16406

categories:
  - Highlight
  - Journal
aliases:
  - /publication_highlights/mancini-etal-2025-promoting-datasets/
topics: [speech, biomedical, ethics]
---

## Research setting

Mental health and neurological disorders (MHND) include depression, Alzheimer's, bipolar disorder, and Parkinson's.
AI systems can help with MHND by detecting signs of a disorder in the way a person speaks.
These systems learn from speech datasets: recordings of participants, each with a label for the disorder.
The kind of speaking task that participants perform is called the discourse genre, for example a clinical interview, a reading aloud, or a speech task.
Each dataset also has a source of content: personal interaction with participants, crowdsourcing through online platforms, or media already available online.

{{< svg src="lifecycle.svg" caption="How a speech dataset for MHND is built, with DAIC-WoZ, the case study of Section 2 of the paper, as the example. Schema drawn from the paper's description." >}}

## Motivation

Machine learning research focuses on models more than on how data are collected, yet biased or poorly documented data can make a system unreliable.
In MHND, the data come from people with a disorder, who may share sensitive content when they speak freely.
The paper shows the risk on DAIC-WoZ, one of the most used depression datasets.
Its classes are imbalanced (65% negative, 35% positive).
Its paper does not state how the PHQ-8 score maps to the binary label.
There is also no way to report or fix its known errors.

{{< gap caption="How the paper relates to the related work it discusses (Section 3 of the paper)." >}}
label: Related work
columns: [Targets MHND, Speech data, Dataset guidance]
rows:
  - name: Mental health ethics (Fadda et al., 2022, and others)
    cells: [true, false, "partial"]
  - name: General datasheets and checklists (Gebru et al., 2021, and others)
    cells: [false, false, true]
  - name: Healthcare datasets (Rostamzadeh et al., 2022)
    cells: ["partial", false, true]
  - name: Speech technology (Papakyriakopoulos et al., 2023, and others)
    cells: [false, true, true]
  - name: Aphasia speech data (Westerhout and Monachesi, 2006)
    cells: ["partial", true, "partial"]
  - name: This paper
    ours: true
    cells: [true, true, true]
{{< /gap >}}

> **Objective.** Define what a responsible speech dataset for MHND should offer, turn it into an actionable checklist, and use the checklist to review the existing datasets.

## Approach

The paper first lists seven desiderata, the properties that a responsible MHND speech dataset should have.
It then turns each desideratum into checklist items, labeled C1 to C7, that state what a dataset paper should report.
It applies the checklist to 36 peer-reviewed papers, each releasing a public speech dataset recorded from people with an MHND.
The analysis groups the datasets by target issue (the disorder), by discourse genre, and by source of content.

{{< pipeline caption="The method of the paper, from the case study to the survey (Sections 2, 4, 5, and 6)." >}}
- title: Case study
  text: Issues found in the DAIC-WoZ depression dataset.
  icon: search
- title: Desiderata
  text: Seven properties of a responsible MHND speech dataset.
  icon: list-ul
- title: Checklist
  text: Items C1 to C7 that a dataset paper should report.
  icon: tasks
  highlight: true
- title: Survey
  text: 36 dataset papers checked, by disorder, genre, and source.
  icon: table
{{< /pipeline >}}

| Desideratum | What the checklist asks the paper to report |
|---|---|
| C1 Informed consent | Consent details shared with participants |
| C2 Data storage and security | Storage and security measures |
| C3 Data privacy | Anonymization and removal of personal information |
| C4 Accountability | Approval by an ethical board |
| C5 Fairness, bias, and diversity | Speakers by class, age, gender/sex, education, language, and ethnicity; bias awareness; diversity collection measures |
| C6 Data quality, validation, and maintainability | Recording settings; versioning and issue reporting; domain experts in the loop; diagnostic criteria |
| C7 Discourse genre | The genres performed and why they were chosen |

*The seven desiderata and their checklist items (Sections 4 and 5.2 of the paper). C5 and C6 also have items for Parkinson's and Alzheimer's datasets only.*

## Results

The survey counts how many of the 36 dataset papers report each checklist item.
The papers cover eight target issues, with depression the most frequent (17 datasets).

{{< numbers >}}
- value: "20 / 36"
  label: papers report informed consent (C1)
- value: "9 / 36"
  label: papers report storage and security measures (C2)
- value: "2 / 36"
  label: papers report the ethnicity of the speakers (C5-f)
{{< /numbers >}}

{{< bars caption="Papers that report each checklist item, out of 36. Source: Table 1 of the paper. Items C5-g (Parkinson's only) and C6-e (Alzheimer's only) are left out." >}}
metric: Papers that report the item
unit: ""
min: 0
max: 36
bars:
  - label: C1 Informed consent
    value: "20"
  - label: C2 Storage and security
    value: "9"
  - label: C3 Privacy
    value: "10"
  - label: C4 Ethical approval
    value: "21"
  - label: C5-a Speakers by class
    value: "28"
  - label: C5-b Age
    value: "25"
  - label: C5-c Gender/sex
    value: "23"
  - label: C5-d Education
    value: "12"
  - label: C5-e Language
    value: "24"
  - label: C5-f Ethnicity
    value: "2"
  - label: C5-h Bias awareness
    value: "13"
  - label: C5-i Diversity measures
    value: "7"
  - label: C6-a Recording settings
    value: "12"
  - label: C6-b Maintainability
    value: "8"
  - label: C6-c Domain experts
    value: "17"
  - label: C6-d Diagnostic criteria
    value: "8"
  - label: C7-a Discourse genre
    value: "28"
  - label: C7-b Genre motivation
    value: "17"
{{< /bars >}}

| Item | Crowdsourcing (5 datasets) | Online media (2 datasets) |
|---|---|---|
| C1 Informed consent | 3 | 0 |
| C2 Storage and security | 3 | 0 |
| C4 Ethical approval | 3 | 0 |
| C5-i Diversity measures | 5 | 0 |
| C6-a Recording settings | 0 | 0 |

*Datasets that report each item, by source of content. Source: Table 4 of the paper.*

Most papers describe their speakers and the discourse genre, so the community is aware that speaker distributions matter.
About half do not report informed consent or ethical approval.
Storage, privacy, and maintainability are reported even less.
The gaps also depend on the source of content.
All crowdsourced datasets report diversity measures, but none reports recording settings.
The datasets built from online media report no consent, security, or ethical approval.

## Takeaways

{{< takeaways >}}
- title: Ethics is often missing from the paper.
  text: About half of the dataset papers do not report informed consent or ethical approval, and fewer report storage, security, or privacy measures.
- title: How data are gathered shapes the gaps.
  text: Crowdsourcing and online media make some items hard to meet, such as recording settings or the consent of the people in the media.
- title: The checklist is a tool for both sides.
  text: Dataset creators can follow it when they design and maintain a dataset, and dataset users can check it before they rely on one.
{{< /takeaways >}}
