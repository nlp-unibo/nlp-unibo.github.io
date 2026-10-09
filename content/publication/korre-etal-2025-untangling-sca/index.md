---
title: 'Untangling Hate Speech Definitions: A Semantic Componential Analysis Across
  Cultures and Domains'

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- Katerina Korre
- Arianna Muti
- Federico Ruggeri
- Alberto Barrón-Cedeño

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2025-04-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2026-02-27T15:55:53.544293Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- paper-conference

# Publication name and optional abbreviated publication name.
publication: '*Findings of the Association for Computational Linguistics: NAACL 2025*'
publication_short: ''

doi: 10.18653/v1/2025.findings-naacl.175

abstract: 'Hate speech relies heavily on cultural influences, leading to varying individual
  interpretations. For that reason, we propose a Semantic Componential Analysis (SCA)
  framework for a cross-cultural and cross-domain analysis of hate speech definitions.
  We create the first dataset of hate speech definitions encompassing 493 definitions
  from more than 100 cultures, drawn from five key domains: online dictionaries, academic
  research, Wikipedia, legal texts, and online platforms. By decomposing these definitions
  into semantic components, our analysis reveals significant variation across definitions,
  yet many domains borrow definitions from one another without taking into account
  the target culture. We conduct zero-shot model experiments using our proposed dataset,
  employing three popular open-sourced LLMs to understand the impact of different
  definitions on hate speech detection. Our findings indicate that LLMs are sensitive
  to definitions: responses for hate speech detection change according to the complexity
  of definitions used in the prompt.'

# Summary. An optional shortened abstract.
summary: HateDefCon breaks 493 hate speech definitions from five domains into semantic components and shows LLM hate speech detection changes with the definition in the prompt.

tags:
- hate speech
- definitions
- semantic componential analysis
- cross-cultural analysis
- dataset
- prompting

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
  caption: 'The component hierarchy of HateDefCon: what a definition says about the target, the intent or purpose, and the act or means of hate speech (Figure 2 of the paper).'
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
  url: https://aclanthology.org/2025.findings-naacl.175/
categories:
  - Conference
aliases:
  - /publication_conferences/korre-etal-2025-untangling-sca/
topics: [benchmark, llms]
---

## Research setting

Hate speech detection is the task of deciding whether a text, such as a social media post, contains hate speech.
Datasets and models for this task rest on a definition of hate speech.
No definition is universally accepted, and what counts as hate depends on culture.
The paper reads each definition as a set of definitional components: the elements that a definition uses to say what hate speech is.
Components fall under three parent categories: the target (who is attacked), the intent or purpose, and the act or means.

{{< annotate caption="A hate speech definition from the paper and the components that annotators mark in it (Figure 1 of the paper)." >}}
labels: [Intent/purpose, Target]
segments:
  - text: "Hate speech denotes speech intended to"
  - text: "degrade"
    label: Intent/purpose
  - text: "groups of people on the basis of their"
  - text: "race,"
    label: Target
  - text: "gender,"
    label: Target
  - text: "age,"
    label: Target
  - text: "color."
    label: Target
{{< /annotate >}}

Definitions come from several domains, the contexts where they emerge: laws, Wikipedia, online dictionaries, research papers, and the conduct policies of online platforms.
A large language model (LLM) can detect hate speech zero-shot: it receives a definition and a text in the prompt and answers without any task-specific training.

## Motivation

Two definitions with different components can give a text two different labels.
Suppose only one of them lists political opinion as a target.
A post that attacks a political group is then hate under the first and not hate under the second.
Most NLP research works on English data, so the cultural side of definitions is often overlooked.
Prior work compares labels of harmful language or proposes criteria for writing definitions.
None of it breaks hate speech definitions themselves into components.

{{< gap caption="How the paper relates to the prior work it discusses (Section 2)." >}}
label: Approach
columns: [Studies hate speech definitions, Breaks definitions into components, Compares definitions across domains and cultures, Tests the effect of definitions on LLMs]
rows:
  - name: Formal concept analysis and conceptual primitives (Kamphuis and Sarbo, 1998; Cambria et al., 2016)
    cells: [false, true, false, false]
  - name: Harmful language categories (Fortuna et al., 2020)
    cells: [false, false, false, false]
  - name: Review of abusive, offensive, toxic, and uncivil (Pachinger et al., 2023)
    cells: [false, false, "partial", false]
  - name: Modular hate speech criteria (Khurana et al., 2022)
    cells: [true, "partial", false, false]
  - name: This paper (SCA and HateDefCon)
    ours: true
    cells: [true, true, true, true]
{{< /gap >}}

> **Objective.** Build a dataset of hate speech definitions annotated with their components, compare the definitions across domains and cultures, and test how the definition in the prompt changes LLM hate speech detection.

## Approach

Semantic Componential Analysis (SCA) is a technique from linguistics that describes a meaning by the components that are present or absent in it.
The paper applies SCA to 493 hate speech definitions from more than 100 cultures and builds the HateDefCon dataset.
Keyword extraction proposes an initial list of components.
Three annotators then mark each component of each definition as present or absent, with an average agreement (Cohen's kappa) of 0.64.
The result is the component hierarchy shown at the top of this page.

{{< figure src="pipeline.png" caption="The HateDefCon pipeline. Definitions come from five domains, keyword extraction proposes components, and annotators mark the components present in each definition (Figure 1 of the paper)." >}}

| Domain | Definitions | Cultures |
|---|---|---|
| Platform policies | 278 | Each culture appears once per platform |
| Laws | 116 | Each culture appears once |
| Wikipedia | 49 | Each culture appears once |
| Research papers | 29 | English 13, German 3, Arabic 2, Indonesian 2, the rest once |
| Dictionaries | 21 | English 7, Italian 5, the rest once |
| **Total** | **493** | |

*Definitions and their cultures per domain in HateDefCon. Source: Table 1 of the paper.*

To test the effect of definitions, the paper prompts three open LLMs (Llama3, Mistral2, and Phi3-mini) with a definition and a post, and asks for a yes or no answer.

{{< pipeline caption="The zero-shot experiment: only the definition in the prompt changes between runs (Sections 6 and 7 and Appendix G of the paper)." >}}
- title: Definition
  text: One definition from HateDefCon, swapped between runs.
  icon: book
  highlight: true
- title: Post
  text: A social media post to classify.
  icon: comment
- title: LLM
  text: Llama3, Mistral2, or Phi3-mini, temperature zero.
  icon: robot
- title: Answer
  text: Yes or no, compared with the gold label.
  icon: check
{{< /pipeline >}}

## Results

The definition analysis compares domains, cultures, and components.
The LLM experiment uses 500 posts from the Gab Hate Corpus, 250 hate and 250 not hate.
It measures the F1 score of the binary task, from 0 to 1, where higher is better.
It compares three definitions.
Dghc is the definition used to annotate the corpus.
Dwiki is a long and detailed definition from the Macedonian Wikipedia.
Ddict is a short general definition from the Merriam-Webster dictionary.

{{< numbers >}}
- value: "17 of 30"
  label: research papers borrow their definition from other papers, laws, or platform policies
- value: "0.78"
  label: F1 of Llama3 with Dwiki, against 0.67 with Dghc
- value: "5%"
  label: of posts that Llama3 refuses to answer with Ddict, against 1% with Dwiki
{{< /numbers >}}

| Model | Dghc | Dwiki | Ddict |
|---|---|---|---|
| Llama3 | 0.67 | **0.78** | 0.70 |
| Mistral2 | 0.56 | 0.53 | 0.58 |
| Phi3-mini | 0.60 | 0.58 | 0.58 |

*F1 score for binary hate speech detection with each definition in the prompt. Source: Table 3 of the paper.*

Definitions vary widely in their components, and the most frequent target components are religion, race, ethnicity, and nationality.
Only laws refer to a specific culture.
Platform policies repeat one text translated into many languages, and Wikipedia often relies on the Cambridge Dictionary.
The LLMs react to the definition in different ways: Llama3 gains with the detailed Dwiki, while Mistral2 shows the reverse tendency.
With Dwiki, Llama3 also finds more attacks on individuals and on political views, which the other two definitions miss.

The paper also prompts Llama3 with definitions tied to Levantine Arabic, a language spoken in Syria, Jordan, and Israel among other countries.

{{< bars caption="Llama3 F1 score with the definition of a Levantine hate speech dataset and with the hate speech laws of three countries where Levantine Arabic is spoken. Source: Section 7 of the paper." >}}
metric: F1 score of Llama3
unit: ""
min: 0
max: 1
bars:
  - label: Levantine dataset
    value: "0.32"
  - label: Israel law
    value: "0.74"
  - label: Syria law
    value: "0.74"
  - label: Jordan law
    value: "0.67"
{{< /bars >}}

The Syrian law names only one target component, race, and still gives the best score together with the Israeli law.
The paper concludes that the models carry their own biases and rely on their internal knowledge as well as on the definition.

## Takeaways

{{< takeaways >}}
- title: Hate speech definitions differ in their components.
  text: Breaking 493 definitions into target, intent or purpose, and act or means shows wide variation, from general definitions to highly specific ones.
- title: Definitions travel without their culture.
  text: Domains borrow definitions from one another, and only laws refer to a specific culture. The paper asks that a definition fit the language and the target culture of the task.
- title: The definition in the prompt changes LLM answers.
  text: F1 scores and refusals move with the definition, in different directions for different models, so the definition should be chosen together with the model and the task.
{{< /takeaways >}}
