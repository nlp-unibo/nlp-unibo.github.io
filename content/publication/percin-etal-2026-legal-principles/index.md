---
title: Automatic extraction and collection of legal principles from CJEU decisions on Fiscal State Aid
authors:
- Sezen Perçin
- Rūta Liepiņa
- Andrea Galassi
- Francesca Lagioia
- Federico Ruggeri
- Piera Santin
- Giovanni Sartor
- Paolo Torroni
author_notes: []
date: '2026-06-22'
publishDate: '2026-10-13'
publication_types:
- article-journal
publication: Artificial Intelligence and Law
publication_short: ''
venue_key: ai-and-law
doi: 10.1007/s10506-026-09526-5
abstract: Legal principles stated in judicial decisions are a key reference for judges and legal professionals. However, typically,
  decisions are long and complex documents. The automatic extraction of legal principles therein may thus be beneficial to
  many. Unfortunately, this is an under-investigated task for which few resources and implementations exist, especially with
  regard to EU law. To promote research in this domain, we develop a novel corpus of 64 judicial decisions on Fiscal State
  Aid by the CJEU (the Court of Justice of the European Union), in which legal principles are identified and tagged. With
  this new resource, we conduct extensive experimentation to identify the best combinations of representation methods, classifiers
  and data augmentation methods for the task at hand, obtaining an F1 score of 0.72. Additionally, we consider the collections
  of legal principles obtained by running the extractive task and collating the output paragraphs together. We show, through
  the use of lexical metrics and human evaluation, that the quality of generated collections is comparable to that of expert-made
  ones.
summary: A corpus of 64 CJEU decisions on Fiscal State Aid supports extracting legal principles, and the collections built
  automatically are comparable to expert-made ones.
card_summary: ''
card_caption: 'From a CJEU decision to a collection of legal principles: each paragraph is classified on its own, and the
  positive paragraphs are collated in document order. Drawn from Sections 5 and 7 of the paper.'
tags:
- CJEU decisions
- legal principles
- annotated corpus
- data augmentation
- text classification
featured: false
url_pdf: ''
url_code: https://github.com/nlp-unibo/legal-principles-cjeu
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''
image:
  caption: ''
  focal_point: ''
  preview_only: false
projects: []
categories:
- Journal
affiliations: []
topics:
- legal
- knowledge-extraction
focus: []
---

## Research setting

The Court of Justice of the European Union (CJEU) interprets and applies EU law, and its decisions guide judges and lawyers in later cases.
Fiscal State Aid is the area of EU law on national tax measures that give some companies an undue advantage, and it was developed through CJEU decisions.
A legal principle is a criterion stated by the judges, such as how a rule must be interpreted, excluding literal citations of legislation.
In CJEU decisions, each principle is usually contained in a single paragraph, so the task is a binary classification of paragraphs: does this paragraph state a legal principle or not?

{{< annotate caption="Two paragraphs quoted from Section 4.2 of the paper. The first, from Case C-656/15 P (para. 43), states a legal principle and contains two of the word patterns that the annotation guidelines list as indicators. The second, from Case C-83/98 P (para. 24), only reports the argument of a party, which the opening words signal, so it is not a principle." >}}
labels: [Legal principle, Indicator, Party argument]
segments:
  - text: "As regards that condition, that the advantage must be granted directly or indirectly through State resources,"
    label: Legal principle
  - text: "it must be recalled that"
    label: Indicator
  - text: "measures not involving a transfer of State resources may fall within the concept of “aid”,"
    label: Legal principle
  - text: "within the meaning of"
    label: Indicator
  - text: "Article 107(1) TFEU."
    label: Legal principle
  - text: "According to the appellant,"
    label: Indicator
  - text: "the particular nature of the review of State aid means that, when the court carrying out the review is called on to assess the facts of the case in the light of legal criteria, it must limit itself to satisfying itself that there is no manifest error of assessment."
    label: Party argument
{{< /annotate >}}

## Motivation

CJEU decisions are long and complex, so finding their principles by hand takes time and legal expertise.
Collections of extracted principles could help summarize decisions and retrieve precedents based on the same principles.
Earlier studies classified legal principles in common law cases, but no empirical work had addressed the CJEU.
The only annotated corpus of CJEU decisions on Fiscal State Aid was built for argument structure, not for principles.

{{< gap caption="How the paper relates to the work it discusses in Section 2. Columns list the properties that the paper uses to position itself." >}}
label: Work
columns: [Decisions, What is annotated, CJEU decisions, Collections of principles judged by experts]
rows:
  - name: Shulayeva et al. (2017)
    cells: [50 common law reports, Facts and legal principles, false, false]
  - name: Valvoda and Ray (2017)
    cells: [A well-cited case and the cases citing it, Binding and non-binding principles, false, false]
  - name: Demosthenes corpus (Grundler et al., 2022)
    cells: [40 CJEU decisions on Fiscal State Aid, Argument structure, true, false]
  - name: This paper
    ours: true
    cells: [64 CJEU decisions on Fiscal State Aid, Legal principles, true, true]
{{< /gap >}}

> **Objective.** Build an annotated corpus of CJEU decisions on Fiscal State Aid, find the best way to extract their legal principles automatically, and test whether the extracted paragraphs form collections that experts accept as real.

## Approach

The corpus holds all 64 decisions of the CJEU on Fiscal State Aid adopted between 1992 and 2022. Two legal experts with a PhD in Law annotated them.
On 124 principles annotated by both, their agreement was Cohen's κ = 0.87, where 1 is perfect agreement.
Only 614 paragraphs state a principle, against 8,977 that do not (Table 1), so the authors rebalance the training data.
Oversampling repeats each principle paragraph 12 to 13 times. Data augmentation creates about 5,000 new principle paragraphs by replacing 10% or 40% of their words with related words.
An encoder then turns each paragraph into a vector. A classifier, such as a support vector machine (SVM), learns to separate principles from other paragraphs.

{{< pipeline caption="How the 72 classifiers are trained on the paragraphs of the 38 training decisions (Section 5 and Figure 1 of the paper). Every combination of training set, encoder, and classifier is tried." >}}
- title: 8 training sets
  text: Original, oversampled, and six augmented.
  icon: clone
  highlight: true
  branches:
    - title: AugGV
      text: GloVe neighbor
    - title: AugLB
      text: LEGAL-BERT guess
    - title: AugWN+GV
      text: WordNet and GloVe
- title: 3 encoders
  text: Paragraph to vector.
  icon: project-diagram
  branches:
    - title: BERT
      text: general
    - title: LEGAL-BERT
      text: legal text
    - title: Sentence-BERT
      text: similarity
- title: 3 classifiers
  text: SVM, logistic regression, feed-forward network.
  icon: balance-scale
- title: 72 models
  text: Compared with 11 baselines and 3 LLMs.
  icon: check-double
{{< /pipeline >}}

{{< annotate caption="A paragraph augmented with AugGV, replacing 10% of the words, as printed in Figure 3 of the paper. AugGV replaces a word with the word closest to it in GloVe word embeddings. The original words were public, favourable, position, and amounts. The augmented paragraph keeps the label of the original." >}}
labels: [Replaced]
segments:
  - text: "Accordingly, although a measure by which the"
  - text: "office"
    label: Replaced
  - text: "authorities grant certain undertakings"
  - text: "favorable"
    label: Replaced
  - text: "tax treatment, which, although not involving the transfer of state resources, places the recipients in a more favourable financial"
  - text: "right"
    label: Replaced
  - text: "than other taxpayers,"
  - text: "quantities"
    label: Replaced
  - text: "to state aid within the meaning of article 107(1) tfeu, that is not the position as regards advantages resulting from a general measure applicable without distinction to all economic operators, which do not constitute state aid within the meaning of that provision (judgment in p, eu:c:2013:525, paragraph 18)."
{{< /annotate >}}

The baselines include random guessing, classifiers on word counts (tf-idf), and a similarity threshold to the known principles.
The three large language models (LLMs), Mistralv3, Llama3, and Phi3-mini, answer YES or NO for each paragraph from a prompt that defines a legal principle, with no examples (zero-shot).
Lastly, the paragraphs that the best classifier flags in a decision are collated in document order into a collection of principles, as in the schema at the top of this page.

## Results

All models were tested on 13 held-out decisions with 113 principle paragraphs and 1,805 other paragraphs (Table 1).
Precision is the share of flagged paragraphs that state a principle, recall is the share of principles that are flagged, and F1, from 0 to 1, balances the two.

{{< numbers >}}
- value: "0.72"
  label: F1 of BERT + SVM + AugGV (Table 6)
- value: "0.54"
  label: F1 of the best baseline, tf-idf (Table 3)
- value: "0.34"
  label: F1 of the best zero-shot LLM, Llama3 (Table 4)
{{< /numbers >}}

{{< bars caption="F1 on the test set (higher is better) for the best system of each kind. Source: Tables 3, 4, and 6 of the paper." >}}
metric: F1 on the principle class
unit: ""
min: 0
max: 1
bars:
  - label: Random, uniform
    value: "0.10"
  - label: Llama3, zero-shot
    value: "0.34"
  - label: Similarity to principles, BERT
    value: "0.50"
  - label: Tf-idf + feed-forward network
    value: "0.54"
  - label: BERT + SVM, no augmentation
    value: "0.68"
    ours: true
  - label: BERT + SVM + AugGV 10%
    value: "0.72"
    ours: true
{{< /bars >}}

BERT with an SVM led the ten best combinations, with precision of 0.80 and recall of 0.65 for the best one (Table 6).
Augmentation with AugGV at 10% added 0.039 F1 over the same model without augmentation, although no augmentation method was consistently the best.
The general-purpose BERT beat LEGAL-BERT, which reached higher recall but lower precision (Table 5).
The zero-shot LLMs flagged most paragraphs as principles: Mistralv3 reached a recall of 1.00 with a precision of 0.10 (Table 4).
The paper reports no significance tests.

The generated collections were compared with the expert-made collection of each test decision.
ROUGE measures word overlap between two texts, here as F1 averaged over the 13 test decisions.

| Collections | ROUGE‑1 | ROUGE‑2 | ROUGE‑L |
|---|---|---|---|
| This work (BERT + SVM + AugGV) | **0.73** | **0.69** | **0.67** |
| Llama3, zero-shot | 0.42 | 0.38 | 0.35 |
| Random paragraphs | 0.08 | 0.07 | 0.07 |

*F1 of each ROUGE variant, averaged over the test decisions (higher is better). Source: Table 7 of the paper.*

Two other legal experts then tried to tell generated collections from expert-made ones, for the 26 validation and test decisions.
Seeing one collection at a time, they spotted generated collections with an average F1 of 0.40 (precision 0.56, recall 0.31), so most generated collections passed as original.
Seeing both versions side by side, they reached an F1 of 0.66 (precision 0.73, recall 0.62).
Their error analysis found false positives on paragraphs about facts or appeal procedure, and false negatives where facts and principles are intertwined.

## Takeaways

{{< takeaways >}}
- title: A first corpus of principles in CJEU decisions.
  text: Experts marked 614 principle paragraphs in 64 decisions on Fiscal State Aid, with an agreement of 0.87 (Cohen's κ). The authors release the corpus and code.
- title: Small trained classifiers beat zero-shot LLMs.
  text: BERT with an SVM and AugGV augmentation reached an F1 of 0.72, against 0.34 for the best zero-shot LLM.
- title: Generated collections pass a first expert check.
  text: Experts shown one collection at a time spotted generated ones with an F1 of only 0.40. The paper names classifying each paragraph without its context as a possible limit.
{{< /takeaways >}}
