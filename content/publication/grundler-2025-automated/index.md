---
title: Automated Extraction of Judicial Interpretative Formulas in EU Case Law on
  VAT

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- Giulia Grundler
- Piera Santin
- Alessia Fidelangeli
- Rachele Mignone
- Federico Galli
- Andrea Galassi
- Giuseppe Contissa
- Luigi di Caro
- Paolo Torroni

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2025-01-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2026-03-02T12:28:22.126872Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- paper-conference

# Publication name and optional abbreviated publication name.
publication: '*Legal Knowledge and Information Systems*'
publication_short: ''

doi: 10.3233/faia251600

abstract: 'This paper addresses the extraction of Judicial Interpretative Formulas (JIFs) in decisions of the Court of Justice of the European Union (CJEU) on Value Added Tax (VAT). European case law includes a significant number of JIFs on this subject, which are crucial for the interpretation of VAT. However, extracting such JIFs manually is effortful, and doing that automatically has not been investigated yet in the VAT domain. Our work proposes the first pipeline method for doing so. We start by defining a set of guidelines for annotating legal texts following a principle definition of JIF. By following such guidelines, we obtain a corpus of 21 expert-labeled CJEU decisions. We keep them for validation and testing. For training, we machine-annotate 80 additional decisions using LLMs. Our experiments show that BERT-based architectures trained on such data perform comparably to LLMs.'

# Summary. An optional shortened abstract.
summary: "A pipeline trains small classifiers on LLM-labelled EU tax rulings to find the Court's interpretative paragraphs, matching the LLM on expert-labelled test data."

tags:
- judicial interpretative formulas
- court of justice of the eu
- value added tax
- llm annotation
- legal-bert
- case law

# Display this page in a list of Featured pages?
featured: false

# Links
url_pdf: ''
url_code: 'https://github.com/poline-project/jif-cjeu'
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
  caption: 'Legal experts label the evaluation rulings, an LLM labels the training rulings, and a fine-tuned classifier finds Judicial Interpretative Formulas. Illustrative schema built from Sections 2 and 3 of the paper.'
  focal_point: ''
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects: ['internal-project']` links to `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []
categories:
  - Conference
aliases:
  - /publication_conferences/grundler-2025-automated/
topics: [legal, knowledge-extraction, llms]
---

## Research setting

The Court of Justice of the European Union (CJEU) interprets EU law for the courts of the member states.
A national court can send it a question, and the CJEU answers with a decision called a preliminary ruling.
In its answers, the Court writes general interpretative statements that later rulings cite again and again: the paper calls them Judicial Interpretative Formulas (JIFs).
JIFs are especially important in value added tax (VAT), where EU rules leave some aspects to national choice and CJEU rulings have shaped much of the law.

{{< svg src="task.svg" caption="The task, as defined by the paper's annotation guidelines (Section 2). Only the part of the ruling that holds the Court's answer is read. Each numbered paragraph gets one label. The paragraph descriptions are illustrative, built from the four kinds of statement that make a paragraph a JIF." >}}

The task is paragraph classification: a paragraph is a JIF when it contains at least one of the four kinds of statement shown above, and not a JIF otherwise.

## Motivation

Finding JIFs by hand is slow work for legal experts, and no automatic method existed for VAT case law.
Prior work on extracting legal principles has two weak points.
Methods that learn from data need many examples labelled by experts, which are costly.
Methods that prompt a large language model (LLM), a general text generator driven by instructions, often lack the stability, transparency, and reproducibility that legal work requires.

{{< gap caption="How the paper positions its pipeline against prior work on extracting legal principles (Section 1 of the paper)." >}}
label: Approach
columns: [No costly expert labels for training, Stable and reproducible at deployment, Applied to CJEU VAT rulings]
rows:
  - name: Machine learning on expert labels (Shulayeva et al., 2017; Valvoda and Ray, 2017)
    cells: [false, true, false]
  - name: Prompting an LLM (Molinari et al., 2024)
    cells: [true, false, false]
  - name: This paper (hybrid pipeline)
    ours: true
    cells: [true, true, true]
{{< /gap >}}

> **Objective.** Build and evaluate a pipeline that extracts JIFs from CJEU rulings on VAT, using an LLM to label training data and a smaller, task-specific classifier to do the extraction.

## Approach

Two legal experts wrote annotation guidelines and refined them on real rulings until no ambiguities remained.
With the final guidelines, they labelled rulings independently and agreed almost perfectly.
In total, experts labelled 21 rulings, which are kept for validation and testing only.
This way, no model is ever evaluated on machine labels.
An LLM, prompted with the guidelines, labelled 80 more rulings for training.
Classifiers based on BERT, a family of compact language models that are fine-tuned (further trained) for one task, then learn from these machine labels.

{{< pipeline caption="The extraction pipeline (Sections 2 and 3 of the paper). The last step trains a dedicated classifier on labels produced by an LLM instead of by experts." >}}
- title: Guidelines
  text: Experts define what a JIF is, with examples.
  icon: book
- title: Expert labels
  text: 21 rulings for validation and testing.
  icon: user-edit
- title: LLM labels
  text: DeepSeek-R1 labels 80 rulings for training.
  icon: robot
- title: Classifier
  text: Fine-tuned on the LLM labels, it labels every paragraph as JIF or not JIF.
  icon: cogs
  highlight: true
{{< /pipeline >}}

| Split | Rulings | Labels | JIF | Not JIF |
|---|---|---|---|---|
| Train | 80 | LLM | 1015 | 1037 |
| Validation | 11 | Experts | 147 | 164 |
| Test | 10 | Experts | 142 | 164 |

*The corpus, with paragraph counts per class. Source: Table 3 of the paper. Splits are made by ruling, so the paragraphs of one ruling never end up in two splits.*

## Results

Each model labels the paragraphs of the 10 test rulings, and its labels are compared with the expert labels.
Precision is the share of predicted JIFs that are real JIFs.
Recall is the share of real JIFs that the model finds.
F1 combines the two, and macro F1 averages F1 over the two classes, JIF and not JIF.
Agreement between the two experts is measured with Cohen's kappa, where 1 means full agreement.

The three BERT-based models are DistilRoBERTa, DeBERTa, and LEGAL-BERT, a BERT model pre-trained on legal text.
A simpler classifier, LinearSVC on word statistics (TF-IDF), is also trained on the LLM labels.

DeepSeek-R1 labelled the training data because it had the best F1 against the experts on the validation split.
It scored 0.807, against 0.785 for Claude-3.7-sonnet and 0.727 for Gemini-1.5-pro.
It also runs on the test split as a reference, next to a random baseline and a majority baseline that always predicts not JIF.
Each BERT-based model is trained three times with different random seeds, and its scores are averaged.
LinearSVC is deterministic, so it needs no repeated runs.

{{< numbers >}}
- value: "0.96"
  label: Cohen's kappa between the two experts, on two rulings labelled independently with the final guidelines
- value: "0.76"
  label: macro F1 of LEGAL-BERT and DistilRoBERTa, against 0.75 for DeepSeek-R1
- value: "0.008"
  label: standard deviation of LEGAL-BERT over three seed runs, the lowest of the BERT-based models
{{< /numbers >}}

{{< bars caption="Paragraph classification on the test split. Source: Table 4 of the paper. Whiskers show the standard deviation over three seed runs." >}}
metric: Macro F1 on the test split
unit: ""
min: 0
max: 1
bars:
  - label: Majority baseline
    value: "0.35"
  - label: Random baseline
    value: "0.49"
  - label: DeepSeek-R1
    value: "0.75"
  - label: LinearSVC
    value: "0.72"
    ours: true
  - label: LEGAL-BERT
    value: "0.76"
    err: "0.008"
    ours: true
  - label: DistilRoBERTa
    value: "0.76"
    err: "0.020"
    ours: true
  - label: DeBERTa
    value: "0.74"
    err: "0.012"
    ours: true
{{< /bars >}}

| Model | JIF precision | JIF recall | JIF F1 |
|---|---|---|---|
| DeepSeek-R1 | 0.73 | 0.73 | 0.74 |
| LinearSVC | 0.68 | 0.75 | 0.71 |
| **LEGAL-BERT** | 0.73 | 0.80 | **0.76** |
| DistilRoBERTa | **0.75** | 0.75 | 0.75 |
| DeBERTa | 0.69 | **0.82** | 0.75 |

*Scores on the JIF class. Source: Table 4 of the paper.*

Classifiers trained only on machine labels perform on par with the LLM that produced those labels, and two of them slightly beat it.
Like the LLM, they tend to find more JIFs than they should rather than miss them, which the paper suggests may come from learning DeepSeek-R1's labels.
Their scores vary little across seed runs.
LinearSVC is not far behind, which suggests that word choice is a strong cue for JIFs.

## Takeaways

{{< takeaways >}}
- title: LLM labels can train a legal classifier.
  text: Classifiers trained on 80 rulings labelled by an LLM perform on par with that LLM, so experts label only the rulings used for validation and testing.
- title: A small model brings stability.
  text: A dedicated classifier is more transparent and reproducible than prompting an LLM, and its scores change little across training runs.
- title: Recall matters to legal users.
  text: LEGAL-BERT, the model the paper prefers, reaches a JIF recall of 0.80, close to the best. Users can drop a few extra paragraphs, but cannot know that a key JIF is missing.
{{< /takeaways >}}
