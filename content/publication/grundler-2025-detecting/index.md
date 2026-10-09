---
title: Detecting Vague Clauses in Italian Privacy Policies Using Transformers, LLMs,
  and Cross-Lingual Techniques

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- Giulia Grundler
- Mariaceleste Musicco
- Andrea Galassi
- Francesca Lagioia
- Rūta Liepiņa
- Giorgio Resta
- Sara Roccu
- Giovanni Sartor
- Paolo Torroni

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2025-01-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2026-03-02T12:28:22.131021Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- paper-conference

# Publication name and optional abbreviated publication name.
publication: '*ECAI 2025*'
publication_short: ''

doi: 10.3233/faia251362

abstract: "Privacy policies often fall short of providing a comprehensive account of how\
  \ personal data is used, thus failing to comply with GDPR requirements. By doing\
  \ so, they hamper the users’ ability to make informed decisions about using services\
  \ while ensuring that their data is used properly and fairly. This calls for automatic\
  \ tools that can effectively identify potentially unlawful policies. Here we present\
  \ a new corpus of Italian privacy policies, with clauses labelled by experts in data\
  \ protection law, to indicate the level of comprehensiveness of information. We focus\
  \ on the categories of data processed, classifying each clause as either sufficiently\
  \ or insufficiently informative (“vague”). We perform 6 different classification\
  \ and detection tasks, comparing the performance of BERT-based models and generative\
  \ Large Language Models. Addressing multilingualism is crucial in the EU, whose 24\
  \ spoken languages are an integral part of its cultural heritage. Consequentely,\
  \ we also perform cross-language experiments to evaluate whether a pre-existing\
  \ English corpus or classifiers can be leveraged for Italian and, vice versa, whether\
  \ our corpus is informative enough to generalize to other languages."

# Summary. An optional shortened abstract.
summary: A new corpus of 30 Italian privacy policies shows that BERT models beat LLMs at flagging vague data clauses and that resources transfer across languages.

tags:
- privacy policies
- gdpr
- vagueness
- cross-lingual transfer
- italian
- large language models

# Display this page in a list of Featured pages?
featured: false

# Links
url_pdf: ''
url_code: 'https://github.com/nlp-unibo/Privacy-Policies-Compliance'
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
  caption: 'The same annotated clauses in the English corpus (left) and the new Italian corpus (right), from LinkedIn and TikTok policies (Figure 1 of the paper).'
  focal_point: ''
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects: ['internal-project']` links to `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []
award: 'Honorable Mention in the Best Paper Award Consideration'

categories:
  - Conference
aliases:
  - /publication_conferences/grundler-2025-detecting/
topics: [privacy, legal, llms]
---

## Research setting

In the European Union, the General Data Protection Regulation (GDPR) requires a privacy policy to tell users which personal data a service processes.
The paper studies the clauses of a policy that describe these categories of data, called CAT clauses.
A legal expert labels each CAT clause as sufficiently informative, when the data are described in full, or insufficiently informative, also called vague, in all other cases.

The label follows from three annotated elements.
A Category is the term that names the data, such as "geolocation data".
A Specification is an optional list introduced by words such as "such as" or "namely", and each item of the list is a Subcategory, such as "GPS information".
Each element is either Open, when it is vague or open-ended, or Closed, when it is concrete or exhaustive.

{{< annotate caption="An insufficiently informative clause from the TikTok policy (Figure 1 of the paper). The Category is Open and the list is open-ended, so the clause is vague even though its two Subcategories are Closed. The Specification element spans the whole list; only its opening words are marked here." >}}
labels: [Open category, Open specification, Closed subcategory]
segments:
  - text: "We receive"
  - text: "information about you"
    label: Open category
  - text: "from merchants as well as payment and transaction fulfillment providers,"
  - text: "such as"
    label: Open specification
  - text: "payment confirmation details,"
    label: Closed subcategory
  - text: "and"
  - text: "information about the delivery of products you have purchased"
    label: Closed subcategory
  - text: "through our shopping features."
{{< /annotate >}}

| Category | Specification | Subcategories | Label |
|---|---|---|---|
| Closed | none | none | Sufficient |
| Closed | any | any | Sufficient |
| Open | Closed | Closed | Sufficient |
| Open | none | none | Insufficient |
| Open | Open | any | Insufficient |
| Open | Closed | Open | Insufficient |

*The six rules that label a clause as sufficiently or insufficiently informative. "Any" means Open or Closed. Source: Table 2 of the paper.*

## Motivation

Empirical studies show that many privacy policies still fall short of the GDPR, and vague descriptions of data leave users unable to know what is collected about them.
Automatic tools could flag such clauses, but previous work on insufficiently informative clauses covers English documents only.
The EU has 24 official languages, and annotated legal corpora are scarce in many of them.
So it matters whether a resource built for one language can serve another.

{{< gap caption="How the paper relates to the prior work it discusses (Section 2 of the paper)." >}}
label: Work
columns: [Italian privacy policies, Insufficiently informative clauses, Cross-lingual transfer]
rows:
  - name: Vague terms (Lebanoff and Liu, 2018; Malik et al., 2023)
    cells: [false, "partial", false]
  - name: Vague data clauses in English (Grundler et al., 2024)
    cells: [false, true, false]
  - name: Cross-lingual legal NLP (Chalkidis et al., 2021; Galassi et al., 2024)
    cells: [false, false, true]
  - name: This paper
    ours: true
    cells: [true, true, true]
{{< /gap >}}

> **Objective.** Find the most effective way to detect insufficiently informative clauses in Italian, and test whether annotated data can be transferred between English and Italian in both directions.

## Approach

The authors build the first Italian corpus for this task: 30 privacy policies of the same online platforms as the 30 English policies of Grundler et al. (2024).
A legal expert, an Italian native speaker trained on the English corpus, annotated it.
In the last training round on English policies, the expert agreed with the English gold labels with a Cohen's κ of 0.77 on the label.
The corpus has 5,862 sentences and 875 CAT clauses, of which 220 are sufficiently informative.

| Task | Input | Output |
|---|---|---|
| CAT classification | A sentence | CAT or not |
| Informativeness classification | A CAT clause | Sufficiently or insufficiently informative |
| Category and Subcategory detection | A CAT clause | The spans of Categories and Subcategories |
| Specification detection | A CAT clause | The spans of Specifications |
| Type classification | A Category or Subcategory | Open or Closed |
| Kind classification | A Category or Subcategory | One of 30 kinds of data, such as payment |

*The six tasks, each solved independently (Section 4.1 of the paper).*

Two families of models solve each task.
Four BERT models (three Italian models and one multilingual model) are fine-tuned on the Italian training split.
Two large language models (LLMs), Gemini 2.0 Flash and Llama-3.1-8B-Instruct, answer from a prompt.
The prompt has no examples (zero-shot) or 15 examples (few-shot, 30 for Kind), picked at random or as the nearest neighbours of the input.
The cross-lingual experiments use no Italian training data at all.

{{< pipeline caption="Transfer from English to Italian (Section 4.3.1 of the paper). Translation uses the open-source Opus-MT models. The reverse direction applies the same idea with the Italian corpus as training data and the English test set." >}}
- title: English corpus
  text: 30 annotated English policies.
  icon: file-alt
- title: Transfer technique
  text: Three ways to reach Italian.
  icon: language
  highlight: true
  branches:
    - title: Training set translation
      text: Translate the training data, train Italian models.
    - title: Multilingual model
      text: Train a multilingual model in English.
    - title: Test set translation
      text: Translate Italian test clauses to English.
- title: Italian test set
  text: Scored on the new Italian corpus.
  icon: check-circle
{{< /pipeline >}}

## Results

Each system is scored on the Italian test split, which holds 20% of the policies, with the F1 score of each class and their average, the macro F1 (from 0 to 1, higher is better).
BERT scores are averages over three fine-tuning runs.

{{< numbers >}}
- value: "0.79"
  label: macro F1 on informativeness for Italian BERT trained on Italian data
- value: "0.80"
  label: macro F1 on informativeness with no Italian training data (DeBERTa, test set translation)
- value: "0.84"
  label: macro F1 on informativeness in English for Italian BERT trained on the Italian corpus
{{< /numbers >}}

{{< bars caption="Informativeness classification on the Italian test set. Source: Table 3 of the paper (whiskers show the standard deviation over three runs)." >}}
metric: Macro F1 for informativeness classification
unit: ""
min: 0
max: 1
bars:
  - label: Gemini zero-shot
    value: "0.64"
  - label: Llama zero-shot
    value: "0.64"
  - label: Llama few-shot (nearest examples)
    value: "0.71"
  - label: Gemini few-shot (nearest examples)
    value: "0.72"
  - label: Multilingual BERT trained in English
    value: "0.65"
    err: "0.109"
  - label: UmBERTo
    value: "0.78"
    err: "0.043"
  - label: Italian BERT
    value: "0.79"
    err: "0.016"
  - label: DeBERTa, test set translation
    value: "0.80"
    err: "0.005"
{{< /bars >}}

| Setting | Model | CAT | Informativeness | Type | Kind |
|---|---|---|---|---|---|
| Zero-shot | Gemini | 0.85 | 0.64 | 0.67 | **0.56** |
| Few-shot, nearest examples | Gemini | **0.86** | 0.72 | 0.76 | 0.54 |
| Fine-tuned on Italian data | Italian BERT | **0.86** | 0.79 | **0.80** | 0.44 |
| Multilingual model | BERT multilingual | 0.68 | 0.65 | 0.73 | 0.30 |
| Training set translation | UmBERTo | 0.85 | **0.80** | 0.73 | 0.32 |
| Test set translation | DeBERTa | 0.85 | **0.80** | 0.79 | 0.43 |

*Macro F1 of the four classification tasks on the Italian test set for selected systems. Source: Table 3 of the paper.*

Fine-tuned BERT models beat the LLMs on vagueness: Italian BERT reaches 0.79, against 0.72 for the best LLM.
The one exception is Kind classification, with 30 classes, where Gemini zero-shot scores best with 0.56.
In the detection tasks, Italian BERT and UmBERTo are always the best models, with up to 0.86 macro F1 for Specifications with BIO tags (Table 5 of the paper).
Translating the Italian test set and reusing English models reaches the top informativeness score of 0.80, while a multilingual model trained in English drops to 0.65.

| Training data for the English test set | Model | CAT | Informativeness | Type | Kind |
|---|---|---|---|---|---|
| Original English corpus | LEGAL-BERT | 0.86 | 0.84 | 0.80 | 0.46 |
| Italian corpus, translated to English | LEGAL-BERT | 0.86 | 0.80 | 0.78 | 0.36 |
| Italian corpus, test set translated to Italian | Italian BERT | 0.85 | 0.84 | 0.77 | 0.35 |

*Macro F1 on the English test set. Source: Table 4 of the paper.*

In the other direction, models trained on the Italian corpus match the English-trained model in three of the four classification tasks, and fall 10 points behind only on Kind classification.

## Takeaways

{{< takeaways >}}
- title: Fine-tuned BERT models beat LLMs on vagueness.
  text: Italian BERT reaches 0.79 macro F1 on informativeness, against 0.72 for the best few-shot LLM. LLMs lead only on Kind classification, which has 30 classes.
- title: English resources can serve Italian.
  text: Translating the test set and reusing English models matches training on Italian data, with no new corpus and no new training. A multilingual model trained in English transfers poorly.
- title: The Italian corpus generalizes to English.
  text: Trained on Italian data, models match the English-trained model in three of the four classification tasks. The corpus and code are public.
{{< /takeaways >}}
