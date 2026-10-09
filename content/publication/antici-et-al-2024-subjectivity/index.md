---
title: A Corpus for Sentence-Level Subjectivity Detection on English News Articles

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- Francesco Antici
- Federico Ruggeri
- Andrea Galassi
- Katerina Korre
- Arianna Muti
- Alessandra Bardi
- Alice Fedotova
- Alberto Barrón-Cedeño

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2024-05-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2026-02-27T15:55:53.534986Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- paper-conference

# Publication name and optional abbreviated publication name.
publication: '*Proceedings of the 2024 Joint International Conference on Computational
  Linguistics, Language Resources and Evaluation (LREC-COLING 2024)*'
publication_short: ''

doi: 10.63317/38y82q5xd7db

abstract: We develop novel annotation guidelines for sentence-level subjectivity detection,
  which are not limited to language-specific cues. We use our guidelines to collect
  NewsSD-ENG, a corpus of 638 objective and 411 subjective sentences extracted from
  English news articles on controversial topics. Our corpus paves the way for subjectivity
  detection in English and across other languages without relying on language-specific
  tools, such as lexicons or machine translation. We evaluate state-of-the-art multilingual
  transformer-based models on the task in mono-, multi-, and cross-language settings.
  For this purpose, we re-annotate an existing Italian corpus. We observe that models
  trained in the multilingual setting achieve the best performance on the task.

# Summary. An optional shortened abstract.
summary: NewsSD-ENG is an English news corpus for sentence-level subjectivity detection, labeled with guidelines that rely on no language-specific tools.

tags:
- subjectivity detection
- student publication
- corpus
- news articles
- annotation guidelines
- multilingual

# Display this page in a list of Featured pages?
featured: false

# Links
url_pdf: ''
url_code: 'https://github.com/nlp-unibo/newssd-eng'
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
  caption: "NewsSD-ENG labels each sentence of English news articles as objective or subjective, shown on two example sentences with the corpus size, agreement, and best result (drawn for this page from Sections 3 and 5 and Tables 4 and 8 of the paper)."
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
  url: https://aclanthology.org/2024.lrec-main.25
categories:
  - Conference
aliases:
  - /publication_conferences/antici-et-al-2024-subjectivity/
topics: [benchmark, fact-checking]
---

## Research setting

Subjectivity detection decides whether a sentence states facts or carries the opinion of its author.
The paper defines a sentence as subjective when its content is based on or influenced by personal feelings, tastes, or opinions, and as objective otherwise.
It supports tasks such as sentiment analysis, bias detection, and fact-checking, where opinions must be separated from facts that can be checked.
Training a classifier for this task needs a corpus: a collection of sentences labeled by human annotators who follow written annotation guidelines.

{{< svg src="setting.svg" caption="The task on two example sentences from the annotation guidelines (Table 8 of the paper). A model reads one sentence at a time and returns OBJ (objective) or SUBJ (subjective)." >}}

Two terms recur on this page:

- **Inter-annotator agreement (IAA)** measures how consistently annotators label the same sentences. The paper uses Krippendorff's alpha, where 1 means perfect agreement and 0 means agreement no better than chance.
- **Macro-F1** is the F1 score (the balance of precision and recall) computed for each class and then averaged, so objective and subjective sentences count equally. It ranges from 0 to 1, and higher is better.

## Motivation

Perceiving subjectivity is hard even for experts.
It depends on interpretation, background knowledge, and personal bias.
The standard way to build corpora spots subjective words from a lexicon, a fixed list of opinion words for one language and domain.
Moving such resources to another language needs extra tools such as machine translation.
Guideline-based alternatives exist, but they struggle with ambiguous sentences and annotator bias.

{{< gap caption="How the paper positions itself against the related work it discusses (Sections 1 and 6 of the paper)." >}}
label: Approach
columns: [No lexicons or machine translation, Disagreements discussed and resolved, Sentence level, Hand-labeled corpora in two languages]
rows:
  - name: Lexicon-based corpus creation (Riloff and Wiebe, 2003; Wiebe and Riloff, 2005)
    cells: [false, "not discussed", true, false]
  - name: Evidentiality-based annotation (Wiebe et al., 1999b)
    cells: ["not discussed", "certainty rating instead", true, false]
  - name: Multilingual detection through translation (Banea et al.)
    cells: [false, "not discussed", "not discussed", false]
  - name: This paper (NewsSD-ENG)
    ours: true
    cells: [true, true, true, true]
{{< /gap >}}

> **Objective.** Write annotation guidelines for sentence-level subjectivity that do not depend on language-specific cues. Use them to build an English news corpus, and test whether they carry over to Italian.

## Approach

The authors follow the prescriptive paradigm: annotators share one written belief about what counts as subjective, and every disagreement leads to a discussion and a clearer rule.
Seven annotators with near-native English and a linguistics or computing background label the sentences.
The articles come from 8 British news outlets and cover controversial political affairs, such as law, civil rights, and economics.
The guidelines start from those of SubjectivITA, an earlier Italian news corpus, and are refined in two pilot studies.

{{< pipeline caption="How the guidelines were built (Section 2 of the paper)." >}}
- title: Starting guidelines
  text: Adapted from the Italian SubjectivITA guidelines.
  icon: book
- title: First pilot
  text: 270 sentences, IAA 0.40, edge cases discussed.
  icon: users
- title: Second pilot
  text: With article context, IAA 0.38. Without it, 0.53.
  icon: balance-scale
- title: Final guidelines
  text: Isolated sentences, five subjective cases, clear objective cases.
  icon: clipboard-check
  highlight: true
{{< /pipeline >}}

A sentence is subjective when its author expresses an explicit opinion, uses sarcasm or irony, exhorts, uses discriminating or downgrading words, or uses rhetorical figures to convey an opinion.
Opinions of a third party, such as quotes, are objective.
The author's own stated emotions are objective too, since the author is a reliable source about their own feelings.
Annotators see each sentence alone, because article context made them label ambiguous sentences as subjective more often and increased their workload.

{{< pipeline caption="The three-stage annotation of the final corpus (Section 3 of the paper)." >}}
- title: Two annotators
  text: Each sentence is labeled independently by two annotators.
  icon: user-edit
- title: Discussion
  text: The pair discusses ambiguous sentences to agree.
  icon: comments
- title: Third annotator
  text: Breaks the tie in the remaining cases.
  icon: gavel
  highlight: true
{{< /pipeline >}}

To test whether the guidelines carry over to other languages, the authors re-annotate quotes and emotions in SubjectivITA with the same criteria, creating NewsSD-ITA.
They then train classifiers in three settings:

| Setting | Training data | Test data |
|---|---|---|
| Monolingual | One language (en→en or it→it) | Same language |
| Multilingual | English and Italian together (en+it) | English or Italian |
| Cross-lingual | One language only | The other language, with no training examples in it |

## Results

The authors first measure corpus quality with IAA, and then compare classifiers by macro-F1 on the test sets of NewsSD-ENG (English) and NewsSD-ITA (Italian), averaged over three seed runs.
Two classifiers use tf-idf word features: a support vector machine (SVM) and a logistic regressor (LR).
Two are multilingual transformers: M-BERT and M-SBERT.
A random and a majority-class baseline complete the comparison.

NewsSD-ENG holds 1,049 sentences from 23 articles: 638 objective and 411 subjective.

{{< numbers >}}
- value: "0.83"
  label: IAA after the pair discussion, up from 0.51 after independent labeling
- value: "-0.21"
  label: average IAA of a lexicon-based tool (TextBlob) with the annotators
- value: "0.80"
  label: macro-F1 of M-BERT on English when trained on English and Italian, against 0.75 on English alone
{{< /numbers >}}

{{< bars caption="Macro-F1 of the two transformers on the NewsSD-ENG test set in each setting. Source: Table 4 of the paper (average over three seed runs)." >}}
metric: Macro-F1 on the English test set
unit: ""
min: 0
max: 1
bars:
  - label: M-SBERT, monolingual
    value: "0.69"
  - label: M-SBERT, multilingual
    value: "0.71"
  - label: M-SBERT, cross-lingual
    value: "0.67"
  - label: M-BERT, monolingual
    value: "0.75"
  - label: M-BERT, multilingual
    value: "0.80"
  - label: M-BERT, cross-lingual
    value: "0.60"
{{< /bars >}}

| Model | Setting | English macro-F1 | English SUBJ F1 | Italian macro-F1 | Italian SUBJ F1 |
|---|---|---|---|---|---|
| Majority baseline | Monolingual | 0.33 | 0.00 | 0.42 | 0.00 |
| Random baseline | Monolingual | 0.50 | 0.50 | 0.47 | 0.36 |
| SVM | Monolingual | 0.44 | 0.24 | 0.59 | 0.34 |
| LR | Monolingual | 0.55 | 0.48 | 0.60 | 0.42 |
| M-SBERT | Monolingual | 0.69 | 0.69 | 0.69 | 0.56 |
| M-BERT | Monolingual | 0.75 | 0.71 | 0.74 | 0.59 |
| SVM | Multilingual | 0.49 | 0.34 | 0.60 | 0.35 |
| LR | Multilingual | 0.64 | 0.65 | 0.61 | 0.42 |
| M-SBERT | Multilingual | 0.71 | 0.76 | 0.69 | 0.56 |
| **M-BERT** | **Multilingual** | **0.80** | **0.80** | **0.77** | **0.66** |
| M-SBERT | Cross-lingual | 0.67 | 0.74 | 0.66 | 0.49 |
| M-BERT | Cross-lingual | 0.60 | 0.46 | 0.65 | 0.46 |

*Macro-F1 and F1 on the subjective class (SUBJ). Source: Table 4 of the paper.*

The annotation reaches near-perfect agreement after discussion, and a third annotator was needed for fewer than 10% of the sentences.
The lexicon-based tool disagrees with the annotators, which suggests that lexicons do not suit this task.
Training on English and Italian together never lowers performance and helps M-BERT most: macro-F1 rises by 5 points on English and 3 points on Italian.
In the cross-lingual setting, M-SBERT stays close to its monolingual scores, while M-BERT loses performance.

## Takeaways

{{< takeaways >}}
- title: A careful corpus for English news.
  text: NewsSD-ENG labels 1,049 news sentences with guidelines refined through pilot studies and discussion, reaching an IAA of 0.83.
- title: The guidelines travel across languages.
  text: They rely on no lexicon or translation, and the matching Italian corpus can be added to training without any loss.
- title: Mixing languages helps.
  text: Multilingual training gives the best macro-F1 on both test sets, 0.80 on English and 0.77 on Italian with M-BERT.
{{< /takeaways >}}
