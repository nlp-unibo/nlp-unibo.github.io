---
title: The Alignment Bottleneck in Decomposition-Based Claim Verification
authors:
- Mahmud Elahi Akhter
- Federico Ruggeri
- Iman Munire Bilal
- Rob Procter
- Maria Liakata
author_notes: []
date: '2026-09-01'
publishDate: '2026-10-13'
publication_types:
- paper-conference
publication: Proceedings of the Thirty-Fifth International Joint Conference on Artificial Intelligence (IJCAI-26)
publication_short: ''
venue_key: ijcai
doi: 10.24963/ijcai.2026/608
abstract: 'Structured claim decomposition is often proposed as a solution for verifying complex, multi-faceted claims, yet
  empirical results have been inconsistent. We argue that these inconsistencies stem from two overlooked bottlenecks: evidence
  alignment and sub-claim error profiles. To better understand these factors, we introduce a new dataset of real-world complex
  claims, featuring temporally bounded evidence and human-annotated sub-claim evidence spans. We evaluate decomposition under
  two evidence alignment setups: Sub-claim Aligned Evidence (SAE) and Repeated Claim-level Evidence (SRE). Our results reveal
  that decomposition brings significant performance improvement only when evidence is granular and strictly aligned. By contrast,
  standard setups that rely on repeated claim-level evidence (SRE) fail to improve and often degrade performance as shown
  across different datasets and domains (PHEMEPlus, MMM-Fact, COVID-Fact). Furthermore, we demonstrate that in the presence
  of noisy sub-claim labels, the nature of the error ends up determining downstream robustness. We find that conservative
  "abstention" significantly reduces error propagation compared to aggressive but incorrect predictions. These findings suggest
  that future claim decomposition frameworks must prioritize precise evidence synthesis and calibrate the label bias of sub-claim
  verification models.'
summary: Splitting a complex claim into sub-claims helps verification only when each sub-claim gets its own aligned evidence;
  repeating claim-level evidence fails to improve it.
card_summary: ''
card_caption: 'The two evidence setups on the example claim of the paper: SAE pairs each sub-claim with its own evidence span,
  SRE repeats the claim evidence. After Figure 1 of the paper.'
tags:
- claim verification
- claim decomposition
- fact-checking
- large language models
featured: false
url_pdf: https://www.ijcai.org/proceedings/2026/0608.pdf
url_code: ''
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
- Conference
affiliations: []
topics:
- fact-checking
- llm-reasoning
focus: []
---

## Research setting

Claim verification decides whether a claim is true or false, given evidence such as news articles.
A complex claim packs several facts into one text, like the tweet in the figure above.
Claim decomposition splits a complex claim into sub-claims, and each sub-claim holds one fact.
Each sub-claim gets a veracity label: true (T), false (F), or unverified (U).
A model then combines the sub-claims and their labels into one verdict for the whole claim.

{{< pipeline caption="Decomposition-based claim verification, the pipeline that the paper studies (Sections 1 and 4 of the paper)." >}}
- title: Claim
  text: A tweet that states several facts.
  icon: comment
- title: Decompose
  text: The claim is split into one-fact sub-claims.
  icon: cut
- title: Verify sub-claims
  text: Each sub-claim gets T, F, or U from evidence.
  icon: search
- title: Verdict
  text: A model combines sub-claims and labels into true or false.
  icon: gavel
{{< /pipeline >}}

The evidence for each sub-claim can come in two forms.
In claim-level evidence, every sub-claim sees the same evidence collected for the whole claim.
In aligned evidence, each sub-claim sees its own evidence span, the few sentences that justify its label.

## Motivation

Studies that test decomposition for fact-checking report conflicting results.
Some find it unnecessary for LLMs, while others find that its effect depends on the decomposition method.
The paper argues that two overlooked factors explain the conflict: how evidence is aligned with each sub-claim, and whether the sub-claim labels are reliable.
Testing these factors needs real-world complex claims with evidence annotated for each sub-claim.

{{< gap caption="How the paper relates to the decomposition studies and datasets it discusses (Sections 2 and 3.3 of the paper)." >}}
label: Work
columns: [Real-world complex claims, Human evidence per sub-claim, Time-bounded evidence]
rows:
  - name: Decomposition study (Hu et al., 2024)
    cells: [false, "Automatic", false]
  - name: ClaimDecomp (Chen et al., 2022)
    cells: [true, "Per claim, by journalists", false]
  - name: WiCE (Kamoi et al., 2023)
    cells: ["Wikipedia", true, false]
  - name: This paper
    ours: true
    cells: [true, true, true]
{{< /gap >}}

> **Objective.** Build a dataset of real-world complex claims with human-annotated evidence for each sub-claim, and measure when decomposition helps claim verification as evidence alignment and sub-claim label quality change.

## Approach

The paper first builds a dataset of complex claims from PHEME, a collection of rumours posted on Twitter during five breaking news events.
It has 399 complex claims and 1169 sub-claims, with an agreement (Bennett's S) of 0.81 on 300 double-annotated sub-claims.

{{< pipeline caption="How the dataset is built (Section 3 of the paper)." >}}
- title: Filter
  text: Keep 423 PHEME claims with several verbs and sentences.
  icon: filter
- title: Decompose
  text: gpt-3.5-turbo-instruct splits them; sub-claims are checked by hand.
  icon: cut
- title: Link evidence
  text: News articles from within 2 days of each event.
  icon: newspaper
- title: Annotate
  text: Label each sub-claim T, F, or U and mark its evidence span.
  icon: user-edit
  highlight: true
{{< /pipeline >}}

The paper then gives one claim verifier, Qwen3-14B prompted zero-shot, different inputs, always together with the claim.
Each tab shows one setup and the inputs it receives.

{{< stages caption="The claim verification setups of the paper. Oracle setups receive the gold sub-claim labels, Ablation setups receive no sub-claim labels, and Noisy setups receive predicted ones (Section 4 and Figure 1 of the paper)." >}}
flow: [Sub-claims, Labels, Claim evidence, Aligned spans, Verifier]
icons:
  frozen: comment-dots
  evolved: robot
labels:
  frozen: Zero-shot
  evolved: Predicted
legend:
  frozen: Prompted zero-shot, not trained
  evolved: Predicted by a sub-claim model
stages:
  - title: Vanilla
    text: The baseline. The verifier sees only the claim and its claim-level evidence, with no decomposition.
    states: {Claim evidence: data, Verifier: frozen}
  - title: Oracle SRE
    text: Sub-claims with Repeated claim-level Evidence. The same claim evidence is repeated after each sub-claim, together with its gold label.
    states: {Sub-claims: data, Labels: data, Claim evidence: data, Verifier: frozen}
  - title: Oracle SAE
    text: Sub-claims with Aligned Evidence. Each sub-claim comes with its own annotated evidence span and its gold label.
    states: {Sub-claims: data, Labels: data, Aligned spans: data, Verifier: frozen}
  - title: Ablation SRE
    text: Oracle SRE without sub-claim labels. This is the only setup possible on MMM-Fact and COVID-Fact, which have no annotated sub-claim evidence.
    states: {Sub-claims: data, Claim evidence: data, Verifier: frozen}
  - title: Ablation SAE
    text: Oracle SAE without sub-claim labels. The verifier must judge the sub-claims from their aligned spans alone.
    states: {Sub-claims: data, Aligned spans: data, Verifier: frozen}
  - title: Noisy SAE and SRE
    text: The gold labels are replaced by labels predicted by a graph neural network (GNN) or by Qwen3-14B, which read each sub-claim with the claim-level evidence. The tab shows Noisy SAE; Noisy SRE uses claim evidence instead of aligned spans.
    states: {Sub-claims: data, Labels: evolved, Aligned spans: data, Verifier: frozen}
{{< /stages >}}

## Results

Claim verification is measured with macro-F1, the F1 score averaged over the true and false classes, and with balanced accuracy, the accuracy averaged over classes.
Scores are the mean of three runs (six for ablations), and gains over Vanilla are tested with a paired bootstrap and McNemar's test.

{{< numbers >}}
- value: "+0.0625"
  label: macro-F1 over Vanilla with Oracle SAE, PHEMEPlus
- value: "−0.0672"
  label: macro-F1 against Vanilla with Ablation SRE, MMM-Fact
- value: "0.4335"
  label: macro-F1 of Qwen Noisy SRE, PHEMEPlus
{{< /numbers >}}

{{< bars caption="Claim verification on the PHEMEPlus claims of the new dataset, mean ± standard deviation over runs. Source: Tables 2 and 3 of the paper." >}}
metric: Macro-F1 on PHEMEPlus
unit: ""
min: 0
max: 0.7
bars:
  - label: Vanilla
    value: "0.5643"
    err: "0.0091"
  - label: Oracle SRE
    value: "0.5872"
    err: "0.0127"
  - label: Oracle SAE
    value: "0.6268"
    err: "0.0098"
  - label: Ablation SRE
    value: "0.5808"
    err: "0.0064"
  - label: Ablation SAE
    value: "0.5485"
    err: "0.0052"
{{< /bars >}}

Only aligned evidence with gold labels (Oracle SAE) gives a significant gain over Vanilla: +0.0625 macro-F1 and +0.0486 balanced accuracy, both with bootstrap p = 0.0000 (Table 2).
Repeated claim evidence (Oracle SRE) gives +0.0229 macro-F1, with bootstrap p = 0.124 and McNemar p = 0.0227.
Aligned spans without labels (Ablation SAE) lose 0.0783 macro-F1 against Oracle SAE (Table 3), so granular evidence helps only with correct sub-claim labels.

| Dataset | Vanilla | Ablation SRE | Δ | p |
|---|---|---|---|---|
| COVID-Fact | **0.7365** ± 0.0248 | 0.7252 ± 0.0161 | −0.0113 | 0.549 |
| MMM-Fact | **0.7550** ± 0.0069 | 0.6878 ± 0.0064 | −0.0672 | 0.0000 |

*Macro-F1 of claim verification without sub-claim labels on two other fact-checking datasets. COVID-Fact has health claims with one evidence source each, and MMM-Fact covers several domains with 6 to 10 evidence sources per claim. Δ is the change against Vanilla, and p is the paired bootstrap p-value. Best values in bold, as in the paper. Source: Table 2 of the paper.*

On other domains, decomposition with repeated claim evidence does not help.
On COVID-Fact the drop is not significant, while on MMM-Fact it is significant, also under McNemar's test (p = 0.0000).

{{< bars caption="Claim verification on PHEMEPlus when gold sub-claim labels are replaced by labels predicted by Qwen3-14B or a GNN, mean ± standard deviation over runs. Source: Table 3 of the paper." >}}
metric: Macro-F1 on PHEMEPlus
unit: ""
min: 0
max: 0.8
bars:
  - label: Oracle SAE (gold labels)
    value: "0.6268"
    err: "0.0098"
  - label: Qwen Noisy SAE
    value: "0.5964"
    err: "0.0360"
  - label: GNN Noisy SAE
    value: "0.5839"
    err: "0.1202"
  - label: Qwen Noisy SRE
    value: "0.4335"
    err: "0.0439"
  - label: GNN Noisy SRE
    value: "0.4416"
    err: "0.0489"
{{< /bars >}}

Predicted labels lower performance in every setup.
With aligned spans the drop is moderate (−0.0304 macro-F1 for Qwen Noisy SAE), while with repeated claim evidence both models fall to about 0.44.

As sub-claim predictors, Qwen3-14B reaches 56.94% macro-F1 and the GNN 45.79% (Table 4), but they also make different errors (Table 5).
The GNN abstains with U on 35.0% of sub-claims against 15.8%, and its refutation recall, the share of false sub-claims it finds, is .04 against .31.
The paper reads this abstention as a safety mechanism with aligned evidence, and concludes that sub-claim macro-F1 alone is a poor predictor of downstream success.

## Takeaways

{{< takeaways >}}
- title: Decomposition needs aligned evidence.
  text: Sub-claims with their own evidence spans and gold labels give a significant gain of +0.0625 macro-F1 over verifying the whole claim at once.
- title: Repeated claim evidence does not help.
  text: Pairing each sub-claim with the same claim evidence brings no significant gain on PHEMEPlus and lowers macro-F1 on MMM-Fact by 0.0672.
- title: The kind of sub-claim error matters.
  text: Noisy labels hurt much less with aligned spans, and a model that abstains with Unverified behaves differently from one that commits to wrong labels.
{{< /takeaways >}}
