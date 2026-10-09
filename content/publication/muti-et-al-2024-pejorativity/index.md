---
title: 'PejorativITy: Disambiguating Pejorative Epithets to Improve Misogyny Detection
  in Italian Tweets'

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- Arianna Muti
- Federico Ruggeri
- Cagri Toraman
- Alberto Barrón-Cedeño
- Samuel Algherini
- Lorenzo Musetti
- Silvia Ronchi
- Gianmarco Saretto
- Caterina Zapparoli

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2024-05-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2026-02-27T15:55:53.539577Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- paper-conference

# Publication name and optional abbreviated publication name.
publication: '*Proceedings of the 2024 Joint International Conference on Computational
  Linguistics, Language Resources and Evaluation (LREC-COLING 2024)*'
publication_short: ''

doi: 10.63317/3gjo4kk28fq8

abstract: 'Misogyny is often expressed through figurative language. Some neutral words
  can assume a negative connotation when functioning as pejorative epithets. Disambiguating
  the meaning of such terms might help the detection of misogyny. In order to address
  such task, we present PejorativITy, a novel corpus of 1,200 manually annotated Italian
  tweets for pejorative language at the word level and misogyny at the sentence level.
  We evaluate the impact of injecting information about disambiguated words into a
  model targeting misogyny detection. In particular, we explore two different approaches
  for injection: concatenation of pejorative information and substitution of ambiguous
  words with univocal terms. Our experimental results, both on our corpus and on two
  popular benchmarks on Italian tweets, show that both approaches lead to a major
  classification improvement, indicating that word sense disambiguation is a promising
  preliminary step for misogyny detection. Furthermore, we investigate LLMs'' understanding
  of pejorative epithets by means of contextual word embeddings analysis and prompting.'

# Summary. An optional shortened abstract.
summary: PejorativITy labels Italian tweets for pejorative words and misogyny, and shows that telling insults from neutral senses first improves misogyny detection.

tags:
- misogyny detection
- pejorative language
- word sense disambiguation
- italian tweets
- hate speech

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
  caption: 'The pipeline: a first model decides whether a potentially pejorative word is used as an insult, and its answer is added to the tweet (CONCAT) or replaces the word with an unambiguous anchor (SUBST) before misogyny detection. Schema drawn for this page from Figure 1 and Section 5 of the paper.'
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
  url: https://aclanthology.org/2024.lrec-main.1112
categories:
  - Conference
aliases:
  - /publication_conferences/muti-et-al-2024-pejorativity/
topics: [benchmark, fairness, llms]
---

## Research setting

Misogyny detection is a text classification task: a model reads a social media post and decides whether it expresses hate toward women.
Misogyny is often figurative, and many neutral words become insults when they are aimed at a woman.
The paper calls such words pejorative epithets: a word with a primary neutral meaning and a second, negative one.
In Italian, balena means whale, but it can also insult a woman as fat.
Only the context of the tweet tells the two senses apart.

{{< svg src="senses.svg" caption="One lexicon word, two senses. An anchor is a word with a single meaning that stands for one sense. Example from Table 1 of the paper (balena has a second neutral anchor, balenare, to flash)." >}}

Word sense disambiguation is the task of picking the right sense of a word in its context.
Here it is a binary decision: is this word, in this tweet, used in a pejorative or in a neutral way?

## Motivation

When a word such as balena appears with its insulting sense in the training data, misogyny classifiers tend to flag every tweet that contains it.
A tweet about a real whale then becomes a false positive, that is, a non-misogynous tweet labeled as misogynous.
Earlier work studied pejorative words or misogyny, but it never used the sense of a word to help misogyny detection.

{{< gap caption="How PejorativITy relates to the prior work discussed in the paper (Sections 1, 2, and 5)." >}}
label: Work
columns: [Italian data, Word-level labels for ambiguous words, Targets neutral words used as insults, Word sense informs misogyny detection]
rows:
  - name: Pejorative lexicon and tweets (Dinu et al., 2021)
    cells: ["partial", true, true, false]
  - name: SWAD swear word dataset (Pamungkas et al., 2023)
    cells: [false, false, false, false]
  - name: AMI misogyny datasets (Fersini et al., 2018, 2020)
    cells: [true, false, "not addressed", false]
  - name: This paper (PejorativITy)
    ours: true
    cells: [true, true, true, true]
{{< /gap >}}

> **Objective.** Find out which epithets are used against women in Italian tweets, test whether disambiguating them lowers the error rate of misogyny detection, and check whether language models can tell the two senses apart from context.

## Approach

The authors first built a lexicon of 24 Italian words that tweets use with both a neutral and a pejorative sense, each with its neutral and pejorative anchors.
They then collected 50 tweets per word, from December 2022 to February 2023, and an expert annotator labeled each tweet for misogyny and each lexicon word for pejorativity.
On this corpus, called PejorativITy, a first AlBERTo model (a BERT model pre-trained on Italian tweets), named model_pej, learns to label the lexicon word as pejorative or neutral.
Its answer then enriches the tweet before a second AlBERTo model, named model_mis, classifies misogyny.

{{< pipeline caption="The PejorativITy pipeline (Sections 3 to 5 and Figure 1 of the paper)." >}}
- title: Corpus
  text: 1,200 tweets with 24 ambiguous words, labeled for pejorativity and misogyny.
  icon: user-edit
- title: model_pej
  text: Labels the lexicon word as pejorative or neutral.
  icon: search
  highlight: true
- title: Inject the sense
  text: Two ways to add the answer to the tweet.
  icon: plus-square
  highlight: true
  branches:
    - title: CONCAT
      text: append the label
    - title: SUBST
      text: swap in the anchor
- title: model_mis
  text: Classifies the enriched tweet as misogynous or not.
  icon: balance-scale
{{< /pipeline >}}

| Class | Training | Test | Total |
|---|---|---|---|
| Misogynous | 369 | 28 | 397 |
| of which with a pejorative word | 363 | 28 | 391 |
| Non-misogynous | 735 | 68 | 803 |
| of which with a pejorative word | 172 | 18 | 190 |

*The PejorativITy corpus (Table 3 of the paper). Some non-misogynous tweets use the word pejoratively, for example in reported speech or against men.*

## Results

The models are scored with macro-F1, the F1 score averaged over the two classes, from 0 to 1 and averaged over three runs.
Misogyny detection is tested on the PejorativITy test set (96 tweets) and on the test sets of AMI-2018 and AMI-2020 (1,000 tweets each), the two Italian misogyny benchmarks.
The AMI tweets have no pejorativity labels, so model_pej predicts them.
Each approach is compared with a baseline: AlBERTo fine-tuned on the original tweets.

{{< numbers >}}
- value: "0.82"
  label: macro-F1 of model_pej in telling pejorative from neutral uses
- value: "+9 points"
  label: misogyny macro-F1 on PejorativITy with SUBST, from 0.68 to 0.77
- value: "25 → 16"
  label: false positives on the PejorativITy test set with CONCAT
{{< /numbers >}}

{{< bars caption="Misogyny detection on the PejorativITy test set. The gold rows use the annotators' pejorativity labels instead of model_pej predictions, an upper bound for the pipeline. Source: Table 5 of the paper." >}}
metric: Macro-F1 on PejorativITy
unit: ""
min: 0
max: 1
bars:
  - label: Baseline
    value: "0.68"
  - label: CONCAT, predicted
    value: "0.75"
    ours: true
  - label: SUBST, predicted
    value: "0.77"
    ours: true
  - label: CONCAT, gold
    value: "0.83"
    ours: true
  - label: SUBST, gold
    value: "0.87"
    ours: true
{{< /bars >}}

| Test set | Baseline | CONCAT | SUBST |
|---|---|---|---|
| AMI-2018, tweets with a lexicon word (34) | 0.79 | **0.82** | 0.79 |
| AMI-2018, whole test set | 0.86 | 0.86 | 0.86 |
| AMI-2020, tweets with a lexicon word (192) | 0.77 | **0.81** | 0.77 |
| AMI-2020, whole test set | 0.82 | **0.83** | 0.82 |

*Macro-F1 on the AMI benchmarks. Source: Table 7 of the paper.*

Both ways of injecting the word sense improve misogyny detection on PejorativITy, and with gold labels the gain reaches +19 points.
On the AMI tweets that contain a lexicon word, CONCAT gains 3 points on AMI-2018 and 4 points on AMI-2020.
SUBST brings no gain there, possibly because some anchors fit the tweet poorly.
The whole AMI test sets barely change, since few of their tweets contain a lexicon word.

Fine-tuning also moves the AlBERTo representation of a lexicon word toward the anchor of its sense (Section 7).
The average cosine similarity with pejorative anchors becomes 0.39 in pejorative tweets and 0.20 in neutral ones, against 0.34 and 0.29 before fine-tuning.
Among three open LLMs prompted without examples, Mistral 7B explained the sense of lexicon words best (Section 8).
It still missed some pejorative uses and reported speech, and the two LLaMA-based models mostly answered that the word means itself.

## Takeaways

{{< takeaways >}}
- title: A new Italian resource.
  text: PejorativITy pairs 1,200 Italian tweets with word-level pejorativity labels and sentence-level misogyny labels, built from a lexicon of 24 ambiguous epithets.
- title: Disambiguation helps misogyny detection.
  text: Adding the sense of the epithet raised macro-F1 on PejorativITy from 0.68 to 0.77 and cut false positives, and better sense labels would raise it further.
- title: Open models still miss the insult.
  text: Fine-tuning teaches AlBERTo the two senses, while the prompted open LLMs struggled with pejorative uses and reported speech.
{{< /takeaways >}}
