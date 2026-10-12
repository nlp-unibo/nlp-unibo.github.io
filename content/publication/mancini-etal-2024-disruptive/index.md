---
title: Disruptive situation detection on public transport through speech emotion recognition

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- Eleonora Mancini
- Andrea Galassi
- Federico Ruggeri
- Paolo Torroni

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2024-01-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2026-02-27T15:55:53.506864Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- article-journal

# Publication name and optional abbreviated publication name.
publication: '*Intelligent Systems with Applications*'
publication_short: ''

doi: 10.1016/j.iswa.2023.200305

abstract: Disruptive situations are emotionally-charged events diverging from ordinary
  behavior, like people fighting or screaming. Public transports are one type of social
  environment where disruptive situation may occur, and their timely detection may
  bring significant improvements to people's safety. Current approaches to disruptive
  situation detection, typically based on CCTVs, do not take the emotional dimension
  into account. Conversely, we propose to frame such a problem as a speech emotion
  recognition task. To validate our hypotheses, we carry out an extensive experimental
  study focusing on the development of a model characterized by speaker/gender independence,
  robustness to noise, and robustness against multiple voices. We investigate a variety
  of audio features, classifiers, datasets, and data augmentation methods in an effort
  to define effective ways to address this under-investigated yet socially significant
  problem. Our experiments show that the proposed systems attain an F1 score of over
  90% on the disruptive class, even when introducing noisy elements such as environmental
  noise or multiple overlapping voices. This robust performance is achieved with datasets
  characterized by speaker variability, gender diversity, and varying number of samples.
  Such promising results indicate that framing disruptive situation detection as a
  speech emotion recognition task could pave the way to the adoption of new types
  of intelligent systems with a positive impact on public safety.

# Summary. An optional shortened abstract.
summary: Detecting disruptive situations on public transport by recognizing anger, fear, sadness, and disgust in speech, with small models that stay accurate in noise.
# Caption of card.svg, the teaser of the page
card_caption: "Speech features of a passenger recording, with train noise added during training, feed a classifier that flags disruptive situations. Schema drawn from the paper."

tags:
- speech emotion recognition
- affective computing
- natural language processing
- machine learning
- data augmentation
- public transport

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
  caption: "The convolutional neural network used as one of the two classifiers: two convolution and pooling blocks, then two dense layers (Figure 1 of the paper, CC BY 4.0)."
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
  url: https://www.sciencedirect.com/science/article/pii/S2667305323001308
categories:
  - Journal
aliases:
  - /publication_journals/mancini-etal-2024-disruptive/
topics: [speech, sentiment]
# Key in data/venues.yaml, whose rank decides the Highlights carousel
venue_key: iswa
# Research focus topics, as <area>/<key> of content/research/<area>/index.md
focus: [speech/applications]
---

## Research setting

A disruptive situation is an emotionally charged event, such as people fighting or screaming, and detecting it in time on public transport can make passengers safer.
The paper treats detection as speech emotion recognition (SER), where a model labels a short speech recording as disruptive (D) or non-disruptive (ND) from the emotion it expresses.
The model reads two kinds of audio features.
Mel-Frequency Cepstral Coefficients (MFCCs) summarize the sound spectrum frame by frame, and Root-Mean-Square Energy (RMSE) measures loudness.
Training and test data come from four acted English datasets (RAVDESS, TESS, SAVEE, and CREMA-D), in which actors speak with a given emotion.

{{< svg src="task.svg" caption="Disruptive situation detection framed as binary speech emotion recognition. Schema drawn from the paper's definitions (Section 4.1.2); the emotion-to-class mapping is the paper's." >}}

## Motivation

The main earlier work on public transport framed the problem as detecting screams and shouted speech.
Yet disruption is not always loud: a passenger can be threatened quietly or be paralyzed by fear.
A real system also has to work in a noisy train, with several people speaking at once, and for speakers of any gender.
Lastly, many SER studies split data at random.
The same actor can then appear in training and test, which makes results look better than they are.

{{< gap caption="How the paper relates to the related work it discusses (Sections 1, 2, and 4.1 of the paper)." >}}
label: Approach
columns: [Public transport setting, Emotion-based detection, Actor- and gender-independent splits, Domain-specific noise]
rows:
  - name: Scream and shouted speech detection (Laffitte et al., 2016)
    cells: [true, false, "not discussed", "not discussed"]
  - name: SER with random data splits (Padi et al., 2020; de Pinto et al., 2020; Patel et al., 2022)
    cells: [false, true, false, "not discussed"]
  - name: SER with leave-one-speaker-out or gender splits (Bitouk et al., 2010; Fu et al., 2020; Zhu et al., 2017)
    cells: [false, true, "partial", "not discussed"]
  - name: SER with white-noise augmentation (An and Ruan, 2021)
    cells: [false, true, "not discussed", "partial"]
  - name: This paper
    ours: true
    cells: [true, true, true, true]
{{< /gap >}}

> **Objective.** Test whether disruptive situation detection can be framed as speech emotion recognition, with a model that is independent of speaker and gender, robust to noise, and robust to multiple overlapping voices.

## Approach

The paper prepares the four datasets so that the evaluation is fair, then trains two lightweight classifiers on them.
Each actor appears in only one split, and splits balance male and female actors when the dataset allows it.
To mimic a train, the training audio is mixed with three real noise recordings.
They capture the inside of a train, a freight train with squeaky wheels, and a small crowd of children playing.
The two classifiers are a support vector machine (SVM) and a small convolutional neural network (CNN), both cheap enough for edge devices.
The paper tests 64 combinations of 4 feature sets, 2 classifiers, and 8 training sets (each dataset with and without noise).

{{< pipeline caption="The method of the paper, from raw recordings to a disruptive or non-disruptive label (Sections 4.1 and 4.2)." >}}
- title: Two classes
  text: Map each emotion to disruptive or non-disruptive.
  icon: tags
- title: Fair splits
  text: Each actor in one split, genders balanced.
  icon: users
  highlight: true
- title: Train noise
  text: Overlay train or crowd noise, 2 dB below the voice.
  icon: train
  highlight: true
- title: Features
  text: 5-second clips at 16 kHz, 12 or 25 MFCCs, optional RMSE.
  icon: wave-square
- title: Classifier
  text: SVM or CNN, also combined in an ensemble.
  icon: project-diagram
{{< /pipeline >}}

## Results

The main metric is the F1 score on the disruptive class, which is high only when the model finds disruptive recordings without raising many false alarms.
Models are tested on the clean test split of each dataset.
RAVDESS, the reference dataset with 12 actresses and 12 actors, also gets noisy, single-gender, and overlapping-voice test sets.

{{< numbers >}}
- value: "0.91"
  label: F1 (D) of the best CNN on the clean RAVDESS test set
- value: "0.87"
  label: F1 (D) on noisy RAVDESS when the CNN is trained with noise
- value: "0.92"
  label: F1 (D) of an ensemble that averages three models' probabilities
{{< /numbers >}}

| Dataset | Best CNN F1 (D) | Best SVM F1 (D) |
|---|---|---|
| RAVDESS | 0.91 (+0.21) | 0.75 (+0.05) |
| TESS | 0.77 (+0.04) | 0.73 (+0.00) |
| SAVEE | 0.67 (+0.00) | 0.62 (-0.05) |
| CREMA-D | 0.92 (+0.03) | 0.89 (+0.00) |

*Best F1 score on the disruptive class on each clean test set, with the gain over a majority baseline, which always predicts the most frequent class, in parentheses. Source: Table 4 of the paper.*

{{< bars caption="F1 (D) on the noise-corrupted RAVDESS test set for models trained on RAVDESS, with 25 MFCCs. Source: Table 6 of the paper." >}}
metric: F1 on the disruptive class, noisy RAVDESS test set
unit: ""
min: 0
max: 1
bars:
  - label: CNN
    value: "0.73"
  - label: CNN + noise augmentation
    value: "0.87"
  - label: CNN + RMSE
    value: "0.76"
  - label: SVM
    value: "0.70"
  - label: SVM + noise augmentation
    value: "0.67"
  - label: SVM + RMSE + noise augmentation
    value: "0.66"
{{< /bars >}}

CNNs give the best results on all four datasets.
On RAVDESS they beat the majority baseline by 0.21 F1 (D), while TESS, SAVEE, and CREMA-D remain hard.
On clean test data, noise augmentation has almost no effect.
On the noisy test set, it limits the CNN loss to 4 F1 points, against up to 17 points without it.
The best RAVDESS CNN scores 0.94 on male-only and 0.89 on female-only test sets (Table 5), which suggests gender independence.
With 2, 5, and 10 overlapping voices, RAVDESS models keep an F1 (D) of 0.89, 0.83, and 0.92, against 0.91 on single files (Table 7).

## Takeaways

{{< takeaways >}}
- title: Disruption can be heard as emotion.
  text: Framed as binary speech emotion recognition, a small CNN reaches an F1 of 0.91 on the disruptive class of RAVDESS, with actors never shared between training and test.
- title: Train with the noise you expect.
  text: Mixing real train and crowd noise into the training audio keeps the CNN at 0.87 F1 on a noisy test set, against 0.73 without it.
- title: Small models, open questions.
  text: The models are light enough for edge devices. They were trained on acted English speech and not tested in real deployments, so a real-world dataset is the next step.
{{< /takeaways >}}
