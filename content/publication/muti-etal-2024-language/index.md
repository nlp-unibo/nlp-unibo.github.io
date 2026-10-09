---
title: 'Language is Scary when Over-Analyzed: Unpacking Implied Misogynistic Reasoning
  with Argumentation Theory-Driven Prompts'

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- Arianna Muti
- Federico Ruggeri
- Khalid Al Khatib
- Alberto Barrón-Cedeño
- Tommaso Caselli

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2024-11-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2026-02-27T15:55:53.516636Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- paper-conference

# Publication name and optional abbreviated publication name.
publication: '*Proceedings of the 2024 Conference on Empirical Methods in Natural
  Language Processing*'
publication_short: ''

doi: 10.18653/v1/2024.emnlp-main.1174

abstract: We propose misogyny detection as an Argumentative Reasoning task and we
  investigate the capacity of large language models (LLMs) to understand the implicit
  reasoning used to convey misogyny in both Italian and English. The central aim is
  to generate the missing reasoning link between a message and the implied meanings
  encoding the misogyny. Our study uses argumentation theory as a foundation to form
  a collection of prompts in both zero-shot and few-shot settings. These prompts integrate
  different techniques, including chain-of-thought reasoning and augmented knowledge.
  Our findings show that LLMs fall short on reasoning capabilities about misogynistic
  comments and that they mostly rely on their implicit knowledge derived from internalized
  common stereotypes about women to generate implied assumptions, rather than on inductive
  reasoning.

# Summary. An optional shortened abstract.
summary: Prompting LLMs to rebuild the hidden reasoning of implicit misogyny shows that they often reach the right label for the wrong reasons.

tags: [misogyny, implicit hate speech, argumentative reasoning, toulmin, prompting, italian]

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
  caption: "A large language model reconstructs the warrant that links an implicit misogynous message to its claim (Figure 2 of the paper)."
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
  url: https://aclanthology.org/2024.emnlp-main.1174
categories:
  - Conference
aliases:
  - /publication_conferences/muti-etal-2024-language/
topics: [llm-reasoning, llms, argument-mining]
---

## Research setting

Misogyny detection is a task of hate speech detection: a model reads a social media message and decides whether it is misogynous.
Many misogynous messages are implicit. They contain no slur and no insult, and their hate lies in an unstated assumption about women, called an implied assumption.
Classifiers trained mostly on explicit hate tend to miss these messages, as the example below shows.

{{< figure src="example.png" caption="An existing hate speech classifier (bert-hateXplain) flags the explicit message but misses the implicit one (Figure 1 of the paper). Its implied assumptions are that women are not as capable as men and should be told what to do." >}}

The paper reads such messages as arguments, following the argument model of Toulmin.
In this model, the claim is what the message states, and the warrant is the unstated link that makes the claim acceptable.
A large language model (LLM) is a general text model that follows written instructions, called prompts.
In the zero-shot setting the prompt gives only the instructions, and in the few-shot setting it also gives a few solved examples.

## Motivation

Most work on hate speech has focused on explicit messages.
Some English datasets pair implicit hateful messages with human-written implied statements, but few efforts generate these statements automatically.
No study had evaluated whether widely used LLMs can reason their way to good implied assumptions, and Italian had no dataset for implicit misogyny.

{{< gap caption="How the paper relates to the prior work it discusses (Sections 1 and 2 of the paper)." >}}
label: Line of work
columns: [Targets implicit hate, Generates implied assumptions automatically, Argumentative reasoning framing]
rows:
  - name: Explicit hate speech datasets and systems
    cells: [false, false, false]
  - name: Implicit hate datasets with implied statements (Sap et al., 2020; ElSherief et al., 2021)
    cells: [true, Human-written only, false]
  - name: Concept-based explanation generation (Ji et al., 2020; Yang et al., 2023)
    cells: ["partial", true, false]
  - name: LLMs on argumentative tasks (Wachsmuth et al., 2024; Chen et al., 2023; Gorur et al., 2024)
    cells: [false, false, true]
  - name: This paper
    ours: true
    cells: [true, true, true]
{{< /gap >}}

> **Objective.** Frame implicit misogyny detection as an argumentative reasoning task, and test whether LLMs can generate the missing warrant of a message and use it to classify the message, in English and Italian.

## Approach

The paper prompts the LLM to write out the hidden reasoning before it gives its label.
In the Toulmin setting, the LLM states the claim and the warrant, and then decides whether the message is misogynous based on the warrant.
In the Assumption setting, the LLM writes the implied assumptions directly, without a claim, and then classifies.
The Toulmin prompts ask for the reasoning step by step, a technique called chain-of-thought prompting.
In both settings the generated text then informs the decision, a technique called knowledge-augmented prompting.

{{< pipeline caption="The Toulmin setting on the example of Figure 2 of the paper. The Assumption setting skips the claim and asks for the implied assumptions directly." >}}
- title: Message
  text: Women football commentators annoy me so much.
  icon: comment
- title: Claim
  text: Women football commentators are annoying.
  icon: quote-right
- title: Warrant
  text: The LLM writes the hidden link. Women do not understand sport.
  icon: link
  highlight: true
- title: Label
  text: Misogynous, decided from the warrant.
  icon: tag
{{< /pipeline >}}

Each setting runs zero-shot and few-shot, with prompts in English and in Italian.
Two instruction-tuned LLMs are tested: Llama3-8B and Mistral-7B-v02.
The baselines are fine-tuned classifiers (bert-hateXplain for English, ALBERTo for Italian) and the same LLMs asked for a label with no reasoning.

## Results

The experiments use two datasets of implicit misogyny.
ImplicIT-Mis is a new Italian dataset of 1,120 Facebook comments, all misogynous, where 150 comments carry 225 human-written implied assumptions.
SBIC+ has 2,409 English messages from two existing corpora, each with human-written warrants.
Because every message is misogynous, classification is measured by recall, the share of messages labeled misogynous, from 0 to 1.
The generated warrants were also checked by hand on 300 messages, 150 per language, for the best model in each language.

{{< numbers >}}
- value: "0.725"
  label: recall of Llama3-8B few-shot with Toulmin warrants on ImplicIT-Mis, against 0.480 with implied assumptions
- value: "68% / 50%"
  label: of generated implied assumptions are wrong, in Italian and in English
- value: "All"
  label: correct Italian labels in the manual check were reached for the wrong reasons
{{< /numbers >}}

{{< bars caption="Classification recall on the Italian ImplicIT-Mis dataset with few-shot prompts and the fine-tuned baseline. Source: Table 1 of the paper." >}}
metric: Recall on ImplicIT-Mis
unit: ""
min: 0
max: 1
bars:
  - label: ALBERTo (fine-tuned)
    value: "0.380"
  - label: Llama3-8B, label only
    value: "0.738"
  - label: Llama3-8B, Assumption
    value: "0.480"
    ours: true
  - label: Llama3-8B, Toulmin
    value: "0.725"
    ours: true
  - label: Mistral-7B-v02, label only
    value: "0.259"
  - label: Mistral-7B-v02, Assumption
    value: "0.461"
    ours: true
  - label: Mistral-7B-v02, Toulmin
    value: "0.556"
    ours: true
{{< /bars >}}

| Setting | Model | ImplicIT-Mis (IT) | SBIC+ (EN) |
|---|---|---|---|
| Fine-tuned | bert-hateXplain / ALBERTo | 0.380 | 0.342 |
| Zero-shot, label only | Llama3-8B | 0.588 | 0.609 |
| Few-shot, label only | Llama3-8B | **0.738** | **0.719** |
| Few-shot, Assumption | Llama3-8B | 0.480 | 0.616 |
| Few-shot, Assumption | Mistral-7B-v02 | 0.461 | 0.685 |
| Zero-shot, Toulmin | Llama3-8B | 0.557 | 0.452 |
| Few-shot, Toulmin | Llama3-8B | 0.725 | 0.594 |
| Few-shot, Toulmin | Mistral-7B-v02 | 0.556 | 0.604 |

*Classification recall, selected rows. ALBERTo is the Italian baseline and bert-hateXplain the English one. Source: Table 1 of the paper.*

LLMs generally beat the fine-tuned classifiers, and Llama3-8B with a plain few-shot prompt gives the best recall in both languages.
In Italian, the Toulmin warrant comes close to that best score and gains 24 points over implied assumptions in the few-shot setting, while in English the warrant-based prompt falls behind.
The manual check shows that a correct label does not mean a correct explanation.
Only 35% of the Italian warrants were correct, and about half of the English implied assumptions were wrong.
The most frequent errors were wrong inferences, missing knowledge of the people a message refers to, figurative language, and sarcasm.

| Error in the generated warrant | Italian | English |
|---|---|---|
| Wrong inference | 42 | 34 |
| Lack of reference | 17 | 0 |
| Metaphorical and figurative language | 14 | 1 |
| Opposite intention | 12 | 9 |
| Wrong translation | 10 | N/A |
| Denial of misogyny | 3 | 4 |
| Sarcasm or irony | 2 | 26 |

*Error categories in the manually checked samples. Source: Table 3 of the paper.*

## Takeaways

{{< takeaways >}}
- title: A right label is not right reasoning.
  text: In the Italian manual check, every correctly classified message came with a wrong warrant, so classification scores cannot certify the explanation.
- title: LLMs lean on stereotypes, not inference.
  text: The models fill the gap with common stereotypes about women and with spurious correlations. They fail on metaphors, sarcasm, and references to people they do not know.
- title: Warrants help in Italian, not in English.
  text: Toulmin prompts raised Italian few-shot recall by 24 points over implied assumptions. The paper suggests checking the generated warrants with humans in the loop before using them.
{{< /takeaways >}}
