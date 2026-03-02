---
title: Text Classification with Guidelines Only
date: 2026-03-02

tags: ["text classification", "uki", "LLMs", "guidelines-only", 'GCAM']

summary: "Train classifiers with guidelines only, without the need of classification labels during training"

---

**Description:**\
The standard approach for training a machine learning model on a task is to provide an annotated dataset $(\mathcal{X}, \mathcal{Y})$.
The dataset is built by providing unlabeled data $\mathcal{X}$ to a group of annotators previously trained on a set of annotation guidelines $\mathcal{G}$.
Annotators label data $\mathcal{X}$ via a given class set $\mathcal{C}$.
The main issue of this approach is that annotators define the mapping from data $\mathcal{X}$ to the class set $\mathcal{C}$ via the guidelines $\mathcal{G}$, while machine learning models are trained to learn the same mapping without guidelines $\mathcal{G}$.
Consequently, these models can learn any kind of mapping from $\mathcal{X}$ to $\mathcal{C}$ that better fits given data.
Our idea is to directly provide guidelines $\mathcal{G}$ to models without any access to class labels during training.

**Contact:** [Federico Ruggeri](mailto:federico.ruggeri6@unibo.it)

**References:**

**Let Guidelines Guide You: A Prescriptive Guideline-Centered Data Annotation Methodology**\
Federico Ruggeri, Eleonora Misino, Arianna Muti, Katerina Korre, Paolo Torroni, Alberto Barrón-Cedeño\
September 2024\
[PDF](https://arxiv.org/abs/2406.14099)