---
title: 'MARGOT: A web server for argumentation mining'

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- Marco Lippi
- Paolo Torroni

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2016-01-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2026-03-02T12:28:22.083278Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- article-journal

# Publication name and optional abbreviated publication name.
publication: '*Expert Systems with Applications*'
publication_short: ''

doi: 10.1016/j.eswa.2016.08.050

abstract: Argumentation mining is a recent challenge concerning the automatic extraction
  of arguments from unstructured textual corpora. Argumentation mining technologies
  are rapidly evolving and show a clear potential for application in diverse areas
  such as recommender systems, policy-making and the legal domain. There is a long-recognised
  need for tools that enable users to browse, visualise, search, and manipulate arguments
  and argument structures. There is, however, a lack of widely accessible tools. In
  this article we describe the technology behind MARGOT, the first online argumentation
  mining system designed to reach out to the wider community of potential users of
  these new technologies. We evaluate its performance and discuss its possible application
  in the analysis of content from various domains.

# Summary. An optional shortened abstract.
summary: 'MARGOT, the first online argumentation mining system, marks the claims and evidence in any text without being told its topic.'

tags:
- argumentation mining
- claim detection
- evidence detection
- tree kernels
- web server

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
  caption: "The MARGOT results page shows claims in bold, evidence in italics, and hides the remaining text behind [...] (Figure 4 of the paper, post-print, CC BY)."
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
  url: https://www.sciencedirect.com/science/article/pii/S0957417416304493
categories:
  - Highlight
  - Journal
aliases:
  - /publication_highlights/lippi-2016292/
topics: [argument-mining]
---

## Research setting

Argumentation mining is the automatic extraction of arguments from unstructured text, such as news, web pages, or social media.
An argument has a claim, the conclusion that someone defends, and evidence, the premises that support it.
A sentence is argumentative when it contains at least one claim or one piece of evidence.
The boundaries of a claim or of a piece of evidence are its first and last words inside the sentence.

{{< annotate caption="Two sentences from the IBM corpus, the training data of MARGOT. The first contains a claim; the second is expert evidence, a testimony by someone with authority on the topic (Section 3 of the paper)." >}}
labels: [Claim, Evidence]
segments:
  - text: "They also argue that"
  - text: "economic inequality contributes to crime."
    label: Claim
  - text: "Dr. Gary Kleck, a criminologist at Florida State University, estimated that approximately 2.5 million people used their gun in self-defense or to prevent crime each year, often by merely displaying a weapon"
    label: Evidence
{{< /annotate >}}

## Motivation

Argumentation mining could serve policy-making, recommender systems, and the legal domain, but in 2016 no tool for it was open to people outside the research field.
Existing methods solved single sub-tasks for single genres, and they relied on hand-made features tied to one genre.
Methods trained on the IBM corpus also needed the topic of the debate in advance, because that corpus labels a claim only when it is relevant to a given topic.

{{< gap caption="How MARGOT relates to the methods the paper discusses (Sections 1 to 3 of the paper)." >}}
label: System
columns: [Open to non-experts, No topic needed, Claims and evidence, Component boundaries, No genre-specific features]
rows:
  - name: Context-dependent detection (Levy et al., 2014; Rinott et al., 2015)
    cells: [false, false, true, "Claims only", false]
  - name: Cross-genre mining with SVM-HMM (Habernal & Gurevych, 2015)
    cells: [false, "Not discussed", true, true, false]
  - name: Context-independent claim detection (Lippi & Torroni, 2015)
    cells: [false, true, "Claims only", false, true]
  - name: This paper (MARGOT)
    ours: true
    cells: [true, true, true, true, true]
{{< /gap >}}

> **Objective.** Build MARGOT (Mining ARGuments frOm Text), a web server that finds claims, evidence, and their boundaries in any English text with no topic given, and test how it behaves across genres.

## Approach

MARGOT is a pipeline of three stages.
The Stanford parser first splits the text into sentences and builds the constituency parse tree of each one, a tree of its grammatical phrases.
Two classifiers then score each sentence, one for claims and one for evidence.
Last, for each argumentative sentence, a sequence labeler marks which words belong to the claim or to the evidence.
MARGOT was trained on the IBM corpus: 547 Wikipedia articles on 58 topics, with 2,294 claims and 4,690 pieces of evidence.

{{< pipeline caption="The MARGOT pipeline, from a plain text query to an HTML page with the arguments highlighted (Figure 1 and Section 4 of the paper)." >}}
- title: Input text
  text: Plain text pasted by the user.
  icon: file-alt
- title: Parsing
  text: Sentences and their parse trees.
  icon: stream
- title: Sentence scoring
  text: Tree kernel classifiers score each sentence.
  icon: filter
  highlight: true
- title: Word labels
  text: SVM-HMM marks claim and evidence words.
  icon: highlighter
  highlight: true
- title: Output page
  text: HTML page with highlights.
  icon: file-code
{{< /pipeline >}}

The classifiers are support vector machines (SVMs) with a tree kernel, a similarity that counts the fragments two parse trees share.
They also use bag-of-words, the counts of the words in the sentence.
The idea is that claims often share a structure, such as a clause after a verb like "argue" or "believe", so no genre-specific features are needed.
The boundary stage uses SVM-HMM, a sequence labeler that combines SVMs with hidden Markov models, over words, part-of-speech tags, lemmas, and named entities.

{{< figure src="method.png" caption="Parse trees of two claim sentences from the IBM corpus. Boxed nodes are the parts the two trees share, which the tree kernel counts (Figure 2 of the paper, post-print, CC BY)." >}}

## Results

On the IBM corpus, each of 39 topics is held out in turn as the test set, and scores are averaged over these topics.
Precision is the share of predicted sentences that are correct, and recall is the share of true sentences that are found.
Sentence detection reports F1, the harmonic mean of precision and recall, and AUROC, the probability that a positive sentence ranks above a negative one (1 is perfect).
Boundary detection reports HT, the share of true claims that the prediction overlaps by at least one word.
The paper then runs MARGOT on new Wikipedia pages, New York Times articles, and Reddit threads.
There it counts the share of sentences with a claim (%C) and with evidence (%E).

{{< numbers >}}
- value: "0.816"
  label: AUROC for claim sentence detection on the IBM corpus
- value: "85.9%"
  label: of true claims hit by the predicted boundaries (HT)
- value: "34.2% vs 10.0%"
  label: of sentences with a claim in controversial and non-controversial Wikipedia pages
{{< /numbers >}}

| Method | Claims, F1 | Claims, AUROC | Evidence, F1 | Evidence, AUROC |
|---|---|---|---|---|
| Random baseline | 3.1 | – | 4.9 | – |
| Bag-of-words SVM | 16.9 | 0.805 | 13.9 | 0.671 |
| Tree kernel (SSTK) | 16.6 | 0.809 | 16.1 | 0.718 |
| **Tree kernel + bag-of-words (MARGOT)** | **17.5** | **0.816** | **16.7** | **0.724** |

*Argumentative sentence detection on the IBM corpus, averaged over 39 held-out topics (Tables 1 and 2 of the paper). Less than 5% of the sentences are positive.*

F1 stays low because fewer than 5% of the sentences are positive and MARGOT does not know the topic: many of its false positives are real claims that the IBM annotators skipped as off-topic.
The tree kernel with bag-of-words gives the best F1 and AUROC for both claims and evidence.
On boundaries, MARGOT reaches an F1 of 66.6 for claims and 90.7 for evidence (Table 4).

Controversial Wikipedia pages hold far more claims than neutral ones, and New York Times articles sit in between, with 22.4% of sentences holding a claim (Tables 5 and 6).
On Reddit, the climate shift thread is richer in arguments than the New Hampshire primaries thread, with an evidence share (%E) of 0.88 against 0.48.

{{< figure src="results.png" caption="Reddit comment trees colored by the MARGOT prediction: blue for claim, red for evidence, yellow for both, gray for none (Figure 6 of the paper, post-print, CC BY)." >}}

## Takeaways

{{< takeaways >}}
- title: Argument mining for everyone.
  text: MARGOT puts claim and evidence detection behind a plain web form, so users need no background in argumentation.
- title: Sentence structure carries arguments.
  text: Tree kernels on parse trees detect claims and evidence without genre-specific features or a given topic.
- title: It generalizes, with limits.
  text: MARGOT finds more arguments where debate is expected, in Wikipedia, news, and Reddit. A truly general tool still needs training data from more genres.
{{< /takeaways >}}
