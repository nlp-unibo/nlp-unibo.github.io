---
title: Assessing the Reasoning Capabilities of LLMs in the context of Evidence-based
  Claim Verification

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- John Dougrez-Lewis
- Mahmud Elahi Akhter
- Federico Ruggeri
- Sebastian Löbbers
- Yulan He
- Maria Liakata

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2025-07-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2026-02-27T15:55:53.553281Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- paper-conference

# Publication name and optional abbreviated publication name.
publication: '*Findings of the Association for Computational Linguistics: ACL 2025*'
publication_short: ''

doi: 10.18653/v1/2025.findings-acl.1059

abstract: Although LLMs have shown great performance on Mathematics and Coding related
  reasoning tasks, the reasoning capabilities of LLMs regarding other forms of reasoning
  are still an open problem. Here, we examine the issue of reasoning from the perspective
  of claim verification. We propose a framework designed to break down any claim paired
  with evidence into atomic reasoning types that are necessary for verification. We
  use this framework to create RECV, the first claim verification benchmark, incorporating
  real-world claims, to assess the deductive and abductive reasoning capabilities
  of LLMs. The benchmark comprises of three datasets, covering reasoning problems
  of increasing complexity. We evaluate three state of-the-art proprietary LLMs under
  multiple prompt settings. Our results show that while LLMs can address deductive
  reasoning problems, they consistently fail in cases of abductive reasoning. Moreover,
  we observe that enhancing LLMs with rationale generation is not always beneficial.
  Nonetheless, we find that generated rationales are semantically similar to those
  provided by humans, especially in deductive reasoning cases.

# Summary. An optional shortened abstract.
summary: RECV, a benchmark of real-world claims labeled by reasoning type, shows that LLMs verify claims by deduction well but fail when abduction is needed.

tags:
- claim verification
- fact-checking
- rationale generation
- abductive reasoning
- deductive reasoning
- benchmark

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
  caption: 'The RECV framework breaks down claim verification into a reasoning task, a reasoning process, and an atomic reasoning type, here abduction (Figure 1 of the paper).'
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
  url: https://aclanthology.org/2025.findings-acl.1059/
categories:
  - Conference
aliases:
  - /publication_conferences/dougrez-lewis-etal-2025-assessing/
topics: [llm-reasoning, fact-checking, benchmark]
---

## Research setting

Claim verification decides whether a claim is true, given some evidence.
A claim is a statement that has to be checked, such as a rumour circulating on social media.
The evidence is a piece of text, here taken from Wikipedia or from news articles, that can confirm or contradict the claim.
The verdict, called the veracity, is either supported or refuted, and a rationale is a short text that explains how the evidence leads to the verdict.

{{< figure src="task.png" caption="Top: an annotator reads a claim with its evidence and veracity, writes a rationale, and names the reasoning type. Bottom: a large language model (LLM) reads the claim and the evidence and returns a veracity, optionally with a rationale (Figure A2 of the paper)." >}}

The paper names two ways to reach a verdict.
In **deduction**, the conclusion follows directly from the evidence, which states what the claim says or contradicts it.
In **abduction**, the evidence is partial, so the verdict rests on the most plausible of several hypotheses.
That hypothesis could be wrong.

## Motivation

LLMs score well on reasoning tests in mathematics and coding, but whether they reason in other settings is still an open question.
Fact-checking is a high-stakes setting where this question matters, because a verifier must give both a correct verdict and a sound rationale.
The most prominent reasoning datasets also leave implicit which kind of reasoning each problem needs.
No claim verification benchmark labeled each claim with the reasoning type required to verify it.

{{< gap caption="How RECV relates to the claim verification work discussed in the paper (Section 9). Not stated means the paper does not say." >}}
label: Work
columns: [Real-world claims and evidence, Evidence given with the claim, Reasoning mode not named in the prompt, Framework of atomic reasoning types]
rows:
  - name: Claims only (Hu et al., 2023b)
    cells: [Not stated, false, Not stated, Not stated]
  - name: Fact verification benchmarks (Aly et al., 2023; Tang et al., 2024; Strong et al., 2024)
    cells: [false, Not stated, Not stated, false]
  - name: Logical reasoning evaluation (Xu et al., 2025)
    cells: [false, Not stated, false, false]
  - name: This paper (RECV)
    ours: true
    cells: [true, true, true, true]
{{< /gap >}}

> **Objective.** Measure how well LLMs verify real-world claims when the evidence calls for deductive or for abductive reasoning, and check whether asking them for a rationale helps.

## Approach

The paper first defines a framework with three layers.
The reasoning task is the overall problem, the reasoning process is one step or several, and an atomic reasoning type is the inference used at each step.
A preliminary study on 90 hand-picked claims found that every claim needed either deduction or abduction, so RECV focuses on these two types.
The authors then sampled 500 claim-evidence pairs from each of three existing datasets, using text-similarity thresholds so that abductive pairs would not be drowned out.
Nine PhD students in Computer Science, three per dataset, labeled each pair as deductive or abductive.

{{< pipeline caption="How RECV was built and used (Sections 4 to 6 of the paper)." >}}
- title: Layers
  text: A framework of task, process, and atomic reasoning type.
  icon: layer-group
- title: Study
  text: A preliminary study of 90 claims finds only deduction and abduction.
  icon: search
- title: Sampling
  text: Similarity thresholds pick 500 pairs per dataset.
  icon: filter
- title: Labels
  text: Three annotators per dataset label the reasoning type.
  icon: user-edit
- title: LLM evaluation
  text: Three LLMs predict the veracity, with or without a rationale.
  icon: robot
  highlight: true
{{< /pipeline >}}

| Dataset | Claims and evidence from | Pairs | Abductive pairs |
|---|---|---|---|
| VitaminC | Wikipedia | 500 | 29 (5.8%) |
| CLIMATE-FEVER | Online claims and Wikipedia | 500 | 102 (20.4%) |
| PHEMEPlus | Social media rumours and news articles | 500 | 36 (7.2%) |

*The three RECV datasets, in order of increasing complexity. Source: Table 1 and Section 5 of the paper.*

Three proprietary LLMs are tested: Claude V3 Sonnet, GPT-4, and GPT-4o.
In the No-Exp setting, a model gives only the veracity; in the Exp setting, it first writes a rationale and then gives the veracity.
Both settings use zero-shot prompts (ZS), without worked examples.
Both also use manual chain-of-thought prompts (M-CoT), with worked step-by-step examples.
The Exp setting adds zero-shot chain-of-thought prompts (ZS CoT).

## Results

The paper scores veracity prediction with macro-F1, from 0 to 1.
It also reports the error rate: the percentage of deductive, or of abductive, pairs whose veracity the model gets wrong.
It also compares the generated rationales with human ones on 100 pairs per dataset.

{{< numbers >}}
- value: "48.58%"
  label: average error rate on abductive pairs of CLIMATE-FEVER, against 15.58% on deductive ones
- value: "32%"
  label: average error rate on abductive pairs of VitaminC, the simplest dataset, against 10.31% on deductive ones
- value: "14.76%"
  label: average performance drop on abductive pairs of CLIMATE-FEVER when models write a rationale first
{{< /numbers >}}

{{< bars caption="Average error rate across all models and prompt settings. Source: Section 6.1 of the paper." >}}
metric: Error rate (%) by dataset and reasoning type
unit: "%"
min: 0
max: 60
lower_is_better: true
bars:
  - label: VitaminC, deductive
    value: "10.31"
  - label: VitaminC, abductive
    value: "32"
  - label: CLIMATE-FEVER, deductive
    value: "15.58"
  - label: CLIMATE-FEVER, abductive
    value: "48.58"
  - label: PHEMEPlus, deductive
    value: "20.06"
  - label: PHEMEPlus, abductive
    value: "44.68"
{{< /bars >}}

| Model and setting | VitaminC F1 | CLIMATE-FEVER F1 | PHEMEPlus F1 |
|---|---|---|---|
| Claude ZS No-Exp | 0.85 | 0.80 | 0.73 |
| Claude ZS Exp | 0.89 | 0.74 | 0.74 |
| GPT-4 ZS No-Exp | 0.86 | 0.87 | 0.69 |
| GPT-4 ZS Exp | 0.88 | 0.78 | 0.73 |
| GPT-4o ZS No-Exp | 0.88 | 0.84 | 0.72 |
| GPT-4o ZS Exp | 0.89 | 0.79 | 0.74 |

*Veracity macro-F1 with zero-shot prompts, without (No-Exp) and with (Exp) a rationale. Source: Table 2 of the paper.*

On every dataset, abductive pairs are much harder than deductive ones: the gap is about three times on average.
Writing a rationale first raises macro-F1 on VitaminC but lowers it on CLIMATE-FEVER, so its effect depends on the dataset and the model.
Against human rationales, the generated ones score from 0.81 to 0.94 on evidence appropriateness and factual consistency.
They match human rationales better when the verdict is correct.
For abductive pairs, models tend to write firm assertions instead of hedged ones, and they often attend to only part of the claim or of the evidence.

## Takeaways

{{< takeaways >}}
- title: Deduction works, abduction does not.
  text: All three LLMs verify claims well when the evidence states the answer, and they fail far more often when the verdict rests on a plausible hypothesis.
- title: A rationale is not a free gain.
  text: Asking for a rationale or a chain of thought helps on simple claims and hurts on complex ones, so no prompt strategy wins everywhere.
- title: Labeling the reasoning type exposes the weakness.
  text: RECV gives 1,500 real-world claim-evidence pairs labeled by reasoning type, which shows where LLM reasoning breaks rather than only how often.
{{< /takeaways >}}
