---
title: Overview of MM-ArgFallacy2025 on Multimodal Argumentative Fallacy Detection
  and Classification in Political Debates

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- Eleonora Mancini
- Federico Ruggeri
- Serena Villata
- Paolo Torroni

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2025-07-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2026-02-27T15:55:09.465450Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- paper-conference

# Publication name and optional abbreviated publication name.
publication: '*Proceedings of the 12th Argument mining Workshop*'
publication_short: ''

doi: 10.18653/v1/2025.argmining-1.35

abstract: 'We present an overview of the MM-ArgFallacy2025 shared task on Multimodal
  Argumentative Fallacy Detection and Classification in Political Debates, co-located
  with the 12th Workshop on Argument Mining at ACL 2025. The task focuses on identifying
  and classifying argumentative fallacies across three input modes: text-only, audio-only,
  and multimodal (text+audio), offering both binary detection (AFD) and multi-class
  classification (AFC) subtasks. The dataset comprises 18,925 instances for AFD and
  3,388 instances for AFC, from the MM-USED-Fallacy corpus on U.S. presidential debates,
  annotated for six fallacy types: Ad Hominem, Appeal to Authority, Appeal to Emotion,
  False Cause, Slippery Slope, and Slogan. A total of 5 teams participated: 3 on classification
  and 2 on detection. Participants employed transformer-based models, particularly
  RoBERTa variants, with strategies including prompt-guided data augmentation, context
  integration, specialised loss functions, and various fusion techniques. Audio processing
  ranged from MFCC features to state-of-the-art speech models. Results demonstrated
  textual modality dominance, with best text-only performance reaching 0.4856 F1-score
  for classification and 0.34 for detection. Audio-only approaches underperformed
  relative to text but showed improvements over previous work, while multimodal fusion
  showed limited improvements. This task establishes important baselines for multimodal
  fallacy analysis in political discourse, contributing to computational argumentation
  and misinformation detection capabilities.'

# Summary. An optional shortened abstract.
summary: 'MM-ArgFallacy2025 benchmarks fallacy detection and classification in U.S. presidential debates from text, audio, or both, and finds that text-based systems still score highest.'

tags:
- fallacy detection
- fallacy classification
- political debates
- multimodal argument mining
- shared task

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
  caption: "The MM-ArgFallacy2025 shared task: detect and classify fallacies in debate sentences from text, audio, or both. Schema drawn from the paper's task definition and examples (Section 3 and Table 1)."
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
  url: https://aclanthology.org/2025.argmining-1.35/
categories:
  - Workshop
aliases:
  - /publication_workshops/mancini-etal-2025-overview/
topics: [argument-mining, multimodal, speech, benchmark]
---

## Research setting

Argument mining is the automatic extraction of arguments from discourse.
Multimodal argument mining (MAM) adds the audio of the speech to the text, because paralinguistic features, such as how a sentence is spoken, carry cues that text alone misses.
A fallacy is an argument with a flaw in its reasoning, and political debates contain many of them.
MM-ArgFallacy2025 is a shared task, a public challenge where teams build systems for the same task and are ranked on the same hidden data.
It has two subtasks on sentences from U.S. presidential debates: argumentative fallacy detection (AFD) and argumentative fallacy classification (AFC).

{{< svg src="task.svg" caption="The two subtasks on a real annotated example labeled Ad Hominem (Table 1 of the paper). Each sentence comes as text only, audio only, or text with its aligned audio. Systems may also use the previous sentences of the debate as context. Schema drawn from the paper's task definition (Section 3)." >}}

## Motivation

Detecting and classifying fallacies can help to analyse behaviour in dialogue, to stop misinformation in fact-checking systems, and to evaluate the reasoning of generative models.
The voice may help, since paralinguistic features can be associated with specific fallacy types.
MAM has mainly addressed finding arguments, labeling their parts, and linking them, where audio has proved effective.
Fallacy detection and classification with audio are still underexplored.

{{< gap caption="How the shared task relates to the debate datasets the paper discusses (Sections 2 and 4 and Table 2 of the paper)." >}}
label: Resource
columns: [Audio aligned with text, Fallacy labels, Secret test set from new debates]
rows:
  - name: UKDebates (Lippi and Torroni, 2016)
    cells: [true, false, false]
  - name: M-Arg (Mestre et al., 2021)
    cells: [true, false, false]
  - name: MM-USED (Mancini et al., 2022)
    cells: [true, false, false]
  - name: Fallacies in debates (Goffredo et al., 2022)
    cells: [false, true, false]
  - name: MM-USED-fallacy (Mancini et al., 2024)
    cells: [true, true, false]
  - name: This paper (MM-ArgFallacy2025)
    ours: true
    cells: [true, true, true]
{{< /gap >}}

> **Objective.** Provide a common platform to develop and evaluate systems that detect and classify fallacies in political debates from text, audio, or both, and report what the participating systems reveal.

## Approach

The organizers released MM-USED-fallacy for training, with sentences and aligned audio from past U.S. presidential debates.
It holds 18,925 instances for detection and 3,388 for classification.
Three supplementary debate datasets, labeled for other argument mining tasks, were also offered for training on several related tasks at once.

For the secret test set, the organizers took two 2024 presidential debates: Trump against Biden and Trump against Harris.
They aligned the transcripts to the audio with WhisperX, a speech recognition model.
Two annotators with argument mining expertise labeled the fallacies with the guidelines of the training data.
Their agreement, measured as Cohen's kappa, is 0.4787 for detection and 0.4954 for classification, both moderate.

{{< pipeline caption="How the shared task was built and scored (Sections 4 and 5 of the paper)." >}}
- title: Training data
  text: MM-USED-fallacy, past presidential debates with aligned audio.
  icon: database
- title: New debates
  text: Two 2024 debates, transcripts aligned to audio.
  icon: microphone
- title: Annotation
  text: Two annotators label fallacies and their types.
  icon: user-edit
  highlight: true
- title: Evaluation
  text: Team runs scored on the secret test set.
  icon: chart-bar
{{< /pipeline >}}

| Fallacy type | Test instances |
|---|---|
| Appeal to Emotion | 142 |
| Ad Hominem | 46 |
| Appeal to Authority | 16 |
| False Cause | 16 |
| Slogan | 9 |
| Slippery Slope | 0 |
| **Total fallacious** | **229** |

*The secret test set for classification (Table 3 of the paper). For detection, the test set holds 229 fallacies and 1,946 non-fallacious sentences.*

The organizers ran two baselines in every input mode.
The first is a BiLSTM, a recurrent network, that reads GloVe word embeddings and MFCCs, standard acoustic features.
The second is a transformer model that uses RoBERTa for text and WavLM for audio.

## Results

Five teams took part, three in classification and two in detection, with 25 valid runs in total.
Every system is scored with F1, which combines precision and recall into a value from 0 to 1.
Detection uses binary F1.
Classification uses macro F1, the average F1 over fallacy types, so rare types weigh as much as frequent ones.

{{< numbers >}}
- value: "0.4856"
  label: best classification macro F1, text only (Team NUST)
- value: "0.3559"
  label: best classification macro F1, audio only (Team AlessioPittiglio)
- value: "0.4611"
  label: best classification macro F1, text and audio (Team NUST)
{{< /numbers >}}

{{< bars caption="Fallacy classification with text only. Source: Table 4 of the paper." >}}
metric: Macro F1 on the secret test set, text only
unit: ""
min: 0
max: 1
bars:
  - label: Team NUST
    value: "0.4856"
  - label: Baseline BiLSTM
    value: "0.4721"
  - label: Team AlessioPittiglio
    value: "0.4444"
  - label: Baseline Transformer
    value: "0.3925"
  - label: Team CASS
    value: "0.1432"
{{< /bars >}}

| System | Text | Audio | Both |
|---|---|---|---|
| **Classification (macro F1)** | | | |
| Team NUST | 0.4856 | 0.1588 | 0.4611 |
| Team AlessioPittiglio | 0.4444 | 0.3559 | 0.4403 |
| Team CASS | 0.1432 | 0.0864 | 0.1432 |
| Baseline BiLSTM | 0.4721 | 0.1582 | 0.2191 |
| Baseline Transformer | 0.3925 | 0.0643 | 0.3816 |
| **Detection (binary F1)** | | | |
| Team Ambali_Yashovardhan | 0.2534 | 0.2095 | 0.2244 |
| Team EvaAdriana | 0.2195 | 0.1690 | 0.1931 |
| Baseline BiLSTM | 0.2462 | 0.0000 | 0.2337 |
| Baseline Transformer | 0.2770 | 0.0000 | 0.2848 |

*All results by input mode, where Both means text with its aligned audio. Source: Table 4 of the paper.*

Text alone gives the best classification scores.
Only Team NUST beats both baselines with text, which shows that even a simple BiLSTM is a strong competitor.
Audio alone stays well below text, although the best audio-only run improves over earlier work.
Adding audio to text does not beat the best text-only score in classification.
In detection, the transformer baseline ranks first with text and with text and audio.
Most teams used transformer models, mainly RoBERTa variants.
Team NUST countered the rarity of some fallacy types by generating extra training examples with GPT-4.

## Takeaways

{{< takeaways >}}
- title: Text carries most of the signal.
  text: Text-only systems gave the best classification scores, and adding audio brought at most small gains. Transformer models, particularly RoBERTa variants, proved the most effective.
- title: Audio needs better fusion.
  text: Audio-only scores improved over earlier work but stay below text. The paper argues that simple fusion, which joins the text and audio outputs only at the end, misses how words and voice interact. It calls for models that learn both modalities jointly.
- title: Data scale and imbalance limit the task.
  text: Only 9.2% of detection sentences are fallacious, Appeal to Emotion makes up 59% of fallacies, and Slippery Slope is absent from the test set. Larger and more balanced data across more debates is the next step.
{{< /takeaways >}}
