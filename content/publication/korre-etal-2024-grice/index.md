---
title: 'A Grice-ful Examination of Offensive Language: Using NLP Methods to Assess
  the Co-operative Principle'

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- Katerina Korre
- Federico Ruggeri
- Alberto Barrón-Cedeño

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2024-10-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2026-02-27T15:55:09.433254Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- paper-conference

# Publication name and optional abbreviated publication name.
publication: '*Proceedings of the First LUHME Workshop*'
publication_short: ''

doi: ''

abstract: 'Natural Language Processing (NLP) can provide tools for analyzing specific
  intricate language phenomena, such as offensiveness in language. In this study,
  we employ methods from pragmatics, more specifically Gricean theory, as well as
  NLP techniques, to analyze instances of online offensive language. We present a
  comparative analysis between offensive and non-offensive instances with regard to
  the degree to which the 4 Gricean Maxims (Quality, Quantity, Manner, and Relevance)
  are flouted or violated. To facilitate our analysis, we employ NLP tools to filter
  the instances and proceed to a more thorough qualitative analysis. Our findings
  reveal that offensive and non-offensive speech do not differ significantly when
  we evaluate with metrics that correspond to the Gricean Maxims, apart from some
  aspects of the Maxim of Quality and the Maxim of Manner. Through this paper, we
  advocate for a turn towards mixed approaches to linguistic topics by also paving
  the way for a modernization of discourse analysis and natural language understanding
  that encompasses computational methods. Warning: This paper contains offensive language
  that might be triggering for some individuals.'

# Summary. An optional shortened abstract.
summary: 'Four Gricean Maxims become NLP metrics: offensive Reddit comments break them about as often as safe ones, except through profanity and untruthful claims.'

tags:
- gricean maxims
- pragmatics
- offensive language
- discourse analysis
- cooperative principle
topics: [dialogue]

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
  caption: 'Share of offensive and safe ToxiChat comments that contain profanity: 53.8% against 16.4% (Figure 5 of the paper).'
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
  url: https://aclanthology.org/2024.luhme-1.2/
categories:
  - Workshop
aliases:
  - /publication_workshops/korre-etal-2024-grice/
---

## Research setting

Pragmatics studies how people mean more than their words say.
In this field, the philosopher H. P. Grice described the cooperative principle: in a conversation, each contribution should serve the shared purpose of the exchange.
He broke the principle down into four maxims, listed below.

| Maxim | What it asks of a speaker |
|---|---|
| Quality | Do not say what you believe to be false, or what you lack evidence for. |
| Quantity | Be as informative as required, and not more. |
| Relevance | Be relevant. |
| Manner | Avoid obscurity and ambiguity. Be brief and orderly. |

*The four Gricean Maxims. Source: Table 1 of the paper.*

A speaker who breaks a maxim by accident violates it.
A speaker who breaks it on purpose, for a rhetorical or humorous effect, flouts it.
The paper asks whether offensive comments in online conversations break the maxims more often than safe ones.
Its data is ToxiChat, a set of Reddit threads in which each turn (one message in the thread) is labeled as offensive or safe.

{{< annotate caption="A three-turn thread from ToxiChat with its offensiveness labels (Table 4 of the paper)." >}}
labels: [Safe, Offensive]
segments:
  - text: "Title: [Question] Why do Libertarians get so much flack from the rest of reddit Like seriously I was downvoted when I said \"Libertarian is a good one\" on a post about third party voting."
    label: Safe
  - text: "Because the rest of reddit are unironically communists."
    label: Offensive
  - text: "Bullshit most are democrats"
    label: Offensive
{{< /annotate >}}

## Motivation

Natural Language Processing (NLP) usually treats offensive language as a detection task: a model labels each message as offensive or not.
This view says little about how an offensive conversation works.
Studies that apply the Gricean Maxims to hate speech read the texts by hand.
Studies that turn the maxims into metrics do not look at offensive language.

{{< gap caption="How the paper relates to the prior work it discusses (Sections 1 and 3)." >}}
label: Approach
columns: [Uses the Gricean Maxims, Measures them with NLP tools, Studies offensive language]
rows:
  - name: Sarcasm in hate speech on Instagram (Pasa et al., 2021)
    cells: [true, false, true]
  - name: Dialog evaluation by user survey (Jwalapuram, 2017)
    cells: [true, false, false]
  - name: Maxims as metrics (Freihat et al., 2018; Tewari et al., 2020; Ge et al., 2023)
    cells: [true, true, false]
  - name: Speech acts in hate speech (Hidayati and Arifuddin, 2021)
    cells: [false, false, true]
  - name: Speech-act-guided toxic stance detection (Upadhyaya et al., 2023)
    cells: [false, true, true]
  - name: This paper
    ours: true
    cells: [true, true, true]
{{< /gap >}}

> **Objective.** Translate each Gricean Maxim into an NLP metric, compare offensive and safe comments with these metrics, and use them to pick examples for a close qualitative reading.

## Approach

Each maxim gets its own NLP tool, which scores every human turn of ToxiChat.
The paper then compares the scores of offensive and safe turns.
Lastly, it filters the offensive turns by these scores and reads selected examples by hand, as in traditional discourse analysis.

{{< pipeline caption="The analysis pipeline of the paper (Section 4). Only the human turns of the ToxiChat training set are used; the bot turns are left out." >}}
- title: ToxiChat turns
  text: Reddit threads, each turn labeled offensive or safe.
  icon: comments
- title: One metric per maxim
  text: Each turn gets four maxim scores.
  icon: ruler
  highlight: true
  branches:
    - title: Quality
      text: Deception classifier
    - title: Quantity
      text: Syntactic cohesion
    - title: Relevance
      text: Embedding similarity
    - title: Manner
      text: Ambiguity, readability, profanity
- title: Compare classes
  text: Offensive turns against safe turns, maxim by maxim.
  icon: balance-scale
- title: Close reading
  text: Selected offensive examples analyzed by hand.
  icon: search
{{< /pipeline >}}

| Maxim | Tool | Signal of a broken maxim |
|---|---|---|
| Quality | A BERT text classifier trained to detect deceptive hotel reviews (1,600 reviews about 20 hotels), with a macro-F1 of 0.926 ± 0.021 on its test set | The turn is predicted as untrue |
| Quantity | Informativeness from syntactic cohesion, scored from 0 to 1 | Below 0.25 (under-informative) or above 0.75 (over-informative) |
| Relevance | Cosine similarity of BERT embeddings between a reply, the thread title, and the previous reply | The reply is judged not relevant |
| Manner | Lexical ambiguity from WordNet word senses, Flesch readability (higher is easier), and a profanity word list | High ambiguity, low readability, or profanity |

*Maxim metrics. Source: Section 4.1 of the paper.*

## Results

The paper scores the human turns of the ToxiChat training set and compares, for each maxim, the share of offensive and safe turns that break it.

{{< numbers >}}
- value: "53.8%"
  label: of offensive turns contain profanity, against 16.4% of safe turns
- value: "40%"
  label: of offensive turns are predicted as untrue, against 30% of safe turns
- value: "95.37%"
  label: of offensive turns are optimally informative, against 95.79% of safe turns
{{< /numbers >}}

| Measure | Offensive | Safe |
|---|---|---|
| Quality: predicted untrue | 371 (40%) | 673 (30%) |
| Quantity: optimally informative | 886 (95.37%) | 2186 (95.79%) |
| Quantity: over-informative | 21 (2.26%) | 50 (2.19%) |
| Quantity: under-informative | 22 (2.37%) | 46 (2.02%) |
| Manner: contains profanity | 53.8% | 16.4% |

*Main results per maxim. Source: Tables 5 and 6 and Figure 5 of the paper.*

{{< figure src="relevance.png" caption="Most replies are relevant in both classes, and irrelevant replies are more frequent among safe turns (Figure 2 of the paper)." >}}

Offensive and safe turns score almost the same on Quantity and Relevance.
Ambiguity and readability are also similar in the two classes.
The clear difference is profanity, a break of the Maxim of Manner, which is much more frequent in offensive turns.
Untrue statements, a break of the Maxim of Quality, are also more frequent in offensive turns.
In the close reading, the authors disagree with the Relevance metric on both examples they chose.
The metrics can therefore err on single turns.

## Takeaways

{{< takeaways >}}
- title: Offensive and safe turns mostly break the maxims alike.
  text: Offensive turns are as informative and as relevant as safe ones. They differ in profanity, which breaks the Maxim of Manner, and partly in truthfulness.
- title: NLP metrics can filter data for linguists.
  text: Scores on each maxim make it fast to find the examples worth a close reading. Discourse analysis thus becomes semi-automatic.
- title: The metrics need human checks.
  text: The close reading found likely errors of the Relevance metric. The paper calls for testing the metrics in other settings and with human experts.
{{< /takeaways >}}
