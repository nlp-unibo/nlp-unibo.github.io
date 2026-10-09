---
title: 'Unfair clause detection in terms of service across multiple languages'

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- Andrea Galassi
- Francesca Lagioia
- Agnieszka Jabłonowska
- Marco Lippi

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2024-04-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2026-03-02T12:28:22.071408Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- article-journal

# Publication name and optional abbreviated publication name.
publication: '*Artificial Intelligence and Law*'
publication_short: ''

doi: 10.1007/s10506-024-09398-7

abstract: 'Most of the existing natural language processing systems for legal texts
  are developed for the English language. Nevertheless, there are several application
  domains where multiple versions of the same documents are provided in different
  languages, especially inside the European Union. One notable example is given by
  Terms of Service (ToS). In this paper, we compare different approaches to the task
  of detecting potential unfair clauses in ToS across multiple languages. In particular,
  after developing an annotated corpus and a machine learning classifier for English,
  we consider and compare several strategies to extend the system to other languages:
  building a novel corpus and training a novel machine learning system for each language,
  from scratch; projecting annotations across documents in different languages, to
  avoid the creation of novel corpora; translating training documents while keeping
  the original annotations; translating queries at prediction time and relying on
  the English system only. An extended experimental evaluation conducted on a large,
  original dataset indicates that the time-consuming task of re-building a novel annotated
  corpus for each language can often be avoided with no significant degradation in
  terms of performance.'

# Summary. An optional shortened abstract.
summary: 'With good machine translation, an English unfair-clause detector for Terms of Service matches detectors trained on new German, Italian, and Polish corpora.'

tags:
- multilingualism
- terms of service
- unfair clause detection
- machine translation
- annotation projection
- consumer protection

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
  caption: 'The four tested strategies for extending the unfair clause detector to a new language, exemplified for German (Figure 1 of the paper, CC BY 4.0).'
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
  url: https://doi.org/10.1007/s10506-024-09398-7
categories:
  - Highlight
  - Journal
aliases:
  - /publication_highlights/10-1007-s-10506-024-09398-7/
topics: [legal]
---

## Research setting

Terms of Service (ToS) are the contracts that online services ask consumers to accept.
Some of their clauses may be unfair to consumers under European consumer law, for example a clause that limits the liability of the provider.
Unfair clause detection is the task of finding these clauses automatically, one sentence at a time.
Legal experts give each relevant clause one of nine categories, such as choice of law (`law`) or jurisdiction (`j`).
They also give it a level: 1 for clearly fair, 2 for potentially unfair, and 3 for clearly unfair.

{{< annotate caption="A real annotated clause from the English Klarna ToS, quoted in Appendix A of the paper. The first sentence is a potentially unfair choice of law (law2) and a clearly unfair jurisdiction clause (j3). The second sentence is a clearly fair jurisdiction clause (j1)." >}}
labels: ["Unfair (law2, j3)", "Fair (j1)"]
segments:
  - text: "This Agreement is governed by the laws of England and Wales and is subject to the exclusive jurisdiction of courts of England and Wales."
    label: "Unfair (law2, j3)"
  - text: "If you are a resident of Northern Ireland you may also bring proceedings in Northern Ireland, and if you are a resident of Scotland, you may also bring proceedings in Scotland."
    label: "Fair (j1)"
{{< /annotate >}}

CLAUDETTE is such a detector for English, and it labels a sentence as positive when the experts marked it as unfair or potentially unfair.

## Motivation

Most legal language technology is built for English.
The European Union works in 24 official languages, and many ToS exist in several language versions.
Annotating a new corpus for every language takes time and legal experts who are native speakers of that language.
The language versions of one contract also differ: some are translations of the English text, while others add clauses for one country.
For example, the Italian Klarna ToS replaces the clauses above with Italian law and the court of the consumer's home, which the experts labeled as clearly fair.

{{< gap caption="How the paper relates to the work it discusses in Section 2. Columns list the properties that the paper uses to position itself." >}}
label: Work
columns: [Legal documents, Unfair clauses in ToS, Annotation projection, Machine translation as a strategy, Several target languages]
rows:
  - name: MULTI-EURLEX (Chalkidis et al., 2021)
    cells: [true, false, false, false, true]
  - name: Annotation projection for ToS (Galassi et al., 2020)
    cells: [true, true, true, false, false]
  - name: Machine translation vs. new models (Isbister et al., 2021)
    cells: [false, false, false, true, true]
  - name: This paper
    ours: true
    cells: [true, true, true, true, true]
{{< /gap >}}

> **Objective.** Find out whether an English unfair clause detector can be extended to other languages without annotating a new corpus for each one. The paper compares four strategies on German, Italian, and Polish.

## Approach

The authors first built a parallel corpus of the same 50 ToS in English, German, Italian, and Polish.
Legal experts annotated all 200 documents.
They then compared four strategies to obtain a detector for a target language, shown in the figure at the top of this page.
Annotation projection copies the labels of each English sentence onto the matching sentence of the target-language version of the same contract.
Machine translation means an off-the-shelf automatic translation tool.

{{< stages caption="The four strategies (Section 4, Figure 1, and Table 2 of the paper). Each tab shows which resources a strategy needs, and whether a classifier is trained for the target language." >}}
flow: [English corpus, Machine translation, Target-language corpus, Classifier]
icons:
  evolved: user-edit
  frozen: lock
labels:
  evolved: New labels
  frozen: Used as is
legend:
  evolved: New annotation by legal experts
  trained: Trained for the target language
  frozen: Used as is, no training
  data: Existing data
stages:
  - title: 1. New corpus
    text: Legal experts annotate a new corpus in the target language, and a new classifier is trained on it. The English corpus and the English system are not used.
    states: {Target-language corpus: evolved, Classifier: trained}
  - title: 2. Projection
    text: The labels of the English corpus are projected onto the original target-language versions of the same contracts. Sentences are matched with sentence embeddings and dynamic time warping. A new classifier is trained on the projected labels.
    states: {English corpus: data, Machine translation: frozen, Target-language corpus: data, Classifier: trained}
  - title: 3. Translate training set
    text: The English training documents are translated into the target language and keep their original labels. A new classifier is trained on the translated documents.
    states: {English corpus: data, Machine translation: frozen, Target-language corpus: data, Classifier: trained}
  - title: 4. Translate queries
    text: No new classifier is trained. At prediction time, each target-language sentence is translated into English and classified by the English system.
    states: {English corpus: data, Machine translation: frozen, Target-language corpus: data, Classifier: frozen}
{{< /stages >}}

All strategies use the same classifier, a linear support vector machine (SVM) on word unigrams and bigrams.
It beat sentence embeddings from ELMo and BERT in a preliminary test (Table 3 of the paper).
Three translation tools of different quality are compared: Google Translate, Opus-MT, and the older statistical system Apache Joshua.

## Results

Each strategy was tested on the German, Italian, and Polish documents with 5-fold cross-validation over documents.
Precision is the share of flagged sentences that are truly unfair, and recall is the share of unfair sentences that are flagged.
The measure is F1, from 0 to 1, which balances the two and is averaged over the five folds.

{{< numbers >}}
- value: "0.677"
  label: F1 on German when queries are translated with Google Translate, against 0.638 with a new German corpus
- value: "0.662"
  label: F1 on Italian when queries are translated with Opus-MT, against 0.621 with a new Italian corpus
- value: "0.645"
  label: F1 on Polish when queries are translated with Google Translate, against 0.630 with a new Polish corpus
{{< /numbers >}}

{{< bars caption="F1 of each strategy on German. G is Google Translate, O is Opus-MT, and J is Apache Joshua. Source: Table 4 of the paper." >}}
metric: F1 on German ToS
unit: ""
min: 0
max: 1
bars:
  - label: 1. New corpus
    value: "0.638"
  - label: 2. Projection
    value: "0.620"
  - label: 3. Translate training set (G)
    value: "0.620"
  - label: 4. Translate queries (G)
    value: "0.677"
  - label: 4. Translate queries (O)
    value: "0.676"
  - label: 4. Translate queries (J)
    value: "0.538"
{{< /bars >}}

| Strategy | German F1 | Italian F1 | Polish F1 |
|---|---|---|---|
| 1. New corpus | 0.638 | 0.621 | 0.630 |
| 2. Projection | 0.620 | 0.604 | 0.619 |
| 3. Translate training set (G) | 0.620 | 0.612 | 0.608 |
| 4. Translate queries (G) | **0.677** | 0.644 | **0.645** |
| 4. Translate queries (O) | 0.676 | **0.662** | 0.575 |
| 4. Translate queries (J) | 0.538 | 0.535 | 0.509 |

*F1 of every strategy in each language. Source: Tables 4, 5, and 6 of the paper.*

With Google Translate, translating the queries scored a higher F1 than a new corpus in all three languages.
With Opus-MT, it did so in German and Italian but not in Polish.
The gain was statistically significant (paired t-test, p < 0.05) for German with both tools and for Italian with Opus-MT.
With the lower-quality Joshua translations, F1 dropped, and a new corpus was significantly better in all three languages.
Projection was only slightly below a new corpus, with a significant gap for German only, and its loss came mostly from precision.
Projection and training set translation performed alike in every language.

## Takeaways

{{< takeaways >}}
- title: A new corpus per language is often not needed.
  text: An English detector with Google Translate for the queries scored a higher F1 than detectors trained on new German, Italian, and Polish corpora.
- title: Translation quality decides the outcome.
  text: With the older Joshua system, F1 fell to between 0.509 and 0.538, and annotating a new corpus became the better choice.
- title: Projection and translation are cheaper fallbacks.
  text: Projecting labels or translating the training set lost little F1 against a new corpus, and the authors release their four-language corpus and code for research.
{{< /takeaways >}}
