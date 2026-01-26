---
title: "Research Proposals"
date: 2026-01-23
tags: ["Research","Proposals", "Argument Mining","Legal Analytics","Knowledge Graphs and LLMs", "UKI", "Interpretability"]
author: "LT-Lab"
description: "Research proposals of our interest." 
summary: "Research proposals of our interest." 
cover:
    image: "proposals.jpg"
    alt: "Research Proposals"
    relative: true
showToc: true
disableAnchoredHeadings: false

---


## Argumentation Mining

One of our main research interests is Argument/Argumentation Mining (AM). 
It can be informally described as the problem of automatically detecting and extracting arguments from the text. 
Arguments are usually represented as a combination of a premise (a fact) that supports a subjective conclusion (opinion, claim). 
Argumentation Mining touches a wide variety of well-known NLP tasks, spanning from sentiment analysis, stance detection to summarization and dialogue systems.


### - Multimodal Argument Mining -

**Description:**\
Make use of speech information (e.g. prosody) to enhance the set of features that can be used to detect arguments. 
Speech can either be represented by means of ad-hoc feature extraction methods (e.g. MFCC) or via end-to-end architectures. 
Few existing corpora both offer argument annotation layers and speech data regarding a given text document.

**Contact:** [Eleonora Mancini](mailto:e.mancini@unibo.it), [Federico Ruggeri](mailto:federico.ruggeri6@unibo.it)

**References:** 

**MAMKit: A Comprehensive Multimodal Argument Mining Toolkit.**\
Eleonora Mancini, Federico Ruggeri, Stefano Colamonaco, Andrea Zecca, Samuele Marro, and Paolo Torroni. 2024.\
In Proceedings of the 11th Workshop on Argument Mining (ArgMining 2024), pages 69–82, Bangkok, Thailand. Association for Computational Linguistics.\
[DOI](https://doi.org/10.18653/v1/2024.argmining-1.7)
| [PDF](https://aclanthology.org/2024.argmining-1.7.pdf)

**Multimodal Fallacy Classification in Political Debates**\
Eleonora Mancini, Federico Ruggeri, Paolo Torroni\
18th Conference of the European Chapter of the Association for Computational Linguistics (EACL), pp. 170–178, 2024\
[DOI](https://doi.org/10.18653/v1/2024.eacl-short.16)
| [PDF](https://aclanthology.org/2024.eacl-short.16.pdf)

**Multimodal Argument Mining: A Case Study in Political Debates**\
Eleonora Mancini, Federico Ruggeri, Andrea Galassi, and Paolo Torroni.\
In Proceedings of the 9th Workshop on Argument Mining, pages 158–170, Online and in Gyeongju, Republic of Korea. International Conference on Computational Linguistics, 2022.\
[PDF](https://aclanthology.org/2022.argmining-1.15.pdf)
| [Anthology](https://aclanthology.org/2022.argmining-1.15)


### - Hate Speech Detection with Argumentative Reasoning -

**Description:**\
Hate speech often lies on implicit content and subtle reasoning nuances. 
Our idea is to apply argumentative reasoning to hate speech to make implicit content explicit in order to define more interpretable and user-friendly hate speech detection systems.

**Contact:** [Federico Ruggeri](mailto:federico.ruggeri6@unibo.it), [Arianna Muti](mailto:arianna.muti@unibocconi.it)

**References:**

**Language is Scary when Over-Analyzed: Unpacking Implied Misogynistic Reasoning with Argumentation Theory-Driven Prompts**\
Arianna Muti, Federico Ruggeri, Khalid Al-Khatib, Alberto Barrón-Cedeño, Tommaso Caselli\
Conference on Empirical Methods in Natural Language Processing (EMNLP), pp. 21091–21107, 2024\
[DOI](https://doi.org/10.18653/v1/2024.emnlp-main.1174)
| [PDF](https://aclanthology.org/2024.emnlp-main.1174.pdf)

**PejorativITy: Disambiguating Pejorative Epithets to Improve Misogyny Detection in Italian Tweets**\
Arianna Muti, Federico Ruggeri, Cagri Toraman, Lorenzo Musetti, Samuel Algherini, Silvia Ronchi, Gianmarco Saretto, Caterina Zapparoli, Alberto Barrón-Cedeño.\
In Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024), pages 12700–12711, Torino, Italia. ELRA and ICCL.\
[PDF](https://aclanthology.org/2024.lrec-main.1112.pdf)
| [Anthology](https://aclanthology.org/2024.lrec-main.1112)

------

## Legal Analytics

The domain of legal documents is one of those that would benefit the most from a wide development and application of NLP tools. 
At the same time, it typically requires a human with a high level of specialization and background knowledge to perform tasks in this context, which are difficult to transfer to an automatic tool.
In this context, we are involved in multiple projects (see CLAUDETTE, ADELE, LAILA, POLINE, PRIMA on the [Projects page](/projects)), which address tasks such as: argument mining, summarization, outcome prediction, detection of unfair clauses, information extraction, and cross-lingual knowledge transfer.
Our purpose is to research and develop tools that can meaningfully impact the community. 
We are in close contact with teams of legal experts who can provide their expertise, and we have access to reserved datasets that can be used to develop automatic tools.

### - Transformers and LLMs for the detection and classification of unfair clauses -

**Description:**  
For several years, we have been working on tools for the automatic detection of unfair clauses in Terms of Services and Privacy Policies documents in the English language (see CLAUDETTE and PRIMA [Projects page](\projects)).
We have already conducted several studies on this topic, and we are interested in applying new effective methods and techniques. 
Right now, we are focused on LLMs, but we are also interested in alternative techniques.

**Contact:** [Andrea Galassi](mailto:galassi@unibo.it), [Marco Lippi](mailto:marco.lippi@unifi.it)

### - Argument Mining on Legal Datasets -

**Description:**\
Argumentation in legal documents is typically well-structured and follows specific domain rules. 
We are interested in applying both the most recent NLP techniques and also hybrid techniques that can leverage the domain knowledge.

**Contact:** [Andrea Galassi](mailto:a.galassi@unibo.it), [Marco Lippi](mailto:marco.lippi@unifi.it)

-----

## Knowledge Graphs and LLMs

A Knowledge Graph is a graph structure used to represent the Knowledge contained in a Knowledge Base. 
In this representation, real world entities (e.g. objects, facts, events) are represented as nodes and their relationships as edges.
Knowledge Graphs provide for a compact, usable and human-readable world representation, they are however of discrete nature (hard to work with deep learning). 
Moreover, KGs are subject to a number of challenges (e.g. entity alignment, ontologies mismatches, etc.) that renders them hard to work with especially during evaluation.
Investigating methods to integrate KGs and LLMs, especially in the field of NLP and from a computational linguistic point of view could potentially enhance LLMs capabilities in lacking fields such as reasoning and maintaining consistency.

### - Knowledge Extraction -

**Description:**\
Given a text in natural language extract a Knowledge Graph using Language Models. 
The key point for this project is to extract relevant information from text and produce a valid (and useful) knowledge base. 
Open problems: integration with ontologies, new concepts, unknown concepts.

**Contact:** [Gianmarco Pappacoda](mailto:gianmarco.pappacoda@unibo.it)

### - Knowledge Injection -

**Description:**\
Given a Knowledge Graph and a Language Models, explore methods for enhancing the Language Model's responses with factual knowledge contained in the Knowledge Graph. 
Possible applications: question answering and information retrieval systems.

**Contact:** [Gianmarco Pappacoda](mailto:gianmarco.pappacoda@unibo.it)
 
### - Ontology learning -

**Description:**\
Given a text and a Language Model, learn the corresponding ontology describing entities and relationships.

**Contact:** [Gianmarco Pappacoda](mailto:gianmarco.pappacoda@unibo.it)

## Unstructured Knowledge Integration

We are interested in developing deep learning models that are capable of employing knowledge in the form of natural language. 
Such knowledge is easy to interpret and to define (compared to structured representations like syntactic trees, knowledge graphs and symbolic rules). 
Unstructured knowledge increases the interpretability of models and goes in the direction of defining a realistic type of artificial intelligence. 
However, properly integrating this type of information is particularly challenging due to its inherent ambiguity and variability.

### - Text Classification with Guidelines Only -

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

### - Multi-cultural Abusive and Hate Speech Detection -

**Description:**\
What is attributable as abusive or hate speech depends on the given socio-cultural context. 
The same text might be reputed offensive by a certain culture, allowed by another, and, in the most extreme case, legally prosecutable by a third one. 
Our aim is to evaluate how machine learning model are affected by different definitions of abusive and hate speech to promote awareness in developing accurate abusive speech detection systems.

**Contact:** [Federico Ruggeri](mailto:federico.ruggeri6@unibo.it), [Katerina Korre](mailto:k.korre@athenarc.gr), [Arianna Muti](mailto:arianna.muti@unibocconi.it)

**References:**

**Untangling Hate Speech Definitions: A Semantic Componential Analysis Across Cultures and Domains.**\
Katerina Korre, Arianna Muti, Federico Ruggeri, and Alberto Barrón-Cedeño. 2025.\
In Findings of the Association for Computational Linguistics: NAACL 2025, pages 3184–3198, Albuquerque, New Mexico. Association for Computational Linguistics.\
[DOI](https://doi.org/10.18653/v1/2025.findings-naacl.175)
| [PDF](https://aclanthology.org/2025.findings-naacl.175.pdf)

-----

## Interpretability

We are interested in developing interpretable models. An interpretable model exposes means for identifying the process that leads from an input to a prediction. 
We are mainly focused on interpretability by design in text classification.

Current topics of interest:

**Selective Rationalization:**\
The process of learning by providing highlights as explanations is denoted as selective rationalization. 
Highlights are a subset of input texts meant to be interpretable by a user and faithfully describe the inference process of a classification model. 
A popular architecture for selective rationalization is the Select-then-Predict Pipeline (SPP): a generator selects the rationale to be fed to a predictor. 
It has been shown that SPP suffers from local minima derived by suboptimal interplay between the generator and predictor, a phenomenon known as interlocking.

**Knowledge Extraction:**\
The process of extracting interpretable knowledge from data-driven processes. 
Our aim is to distill common knowledge from several examples when addressing a downstream task.

### - Mixture of Experts for Rationalization -

**Description:**\
Mixture of Experts (MoE) is a technique whereby several models are trained on the same data, each specializing in a certain subset. 
MoE have been shown to be successful in a variety of applications and their original formulation dates back early 2000s. 
The idea is to understand whether we can develop a MoE model for selective rationalization to address interlocking.

**Contact:** [Federico Ruggeri](mailto:federico.ruggeri6@unibo.it)

**References:**

**A Survey on Mixture of Experts in Large Language Models**\
W. Cai, J. Jiang, F. Wang, J. Tang, S. Kim and J. Huang.\
In IEEE Transactions on Knowledge and Data Engineering, vol. 37, no. 7, pp. 3896-3915, July 2025.\
[DOI](https://doi.org/10.1109/TKDE.2025.3554028)

### - Rationalization via LLMs -

**Description:**\
LLMs are ubiquitous in NLP. Our aim is to evaluate LLM capabilities in performing selective rationalization via prompting. 
How do they compare w.r.t. traditional SPP models?

**Contact:** [Federico Ruggeri](mailto:federico.ruggeri6@unibo.it)

**References:**

**Towards Faithful Explanations: Boosting Rationalization with Shortcuts Discovery**\
Linan Yue, Qi Liu, Yichao Du, Li Wang, Weibo Gao, Yanqing An.\
The Twelfth International Conference on Learning Representations, 2024.\
[PDF](https://openreview.net/pdf?id=uGtfk2OphU)

**Learning Robust Rationales for Model Explainability: A Guidance-Based Approach**\
S Hu, K Yu.\
Proceedings of the AAAI Conference on Artificial Intelligence, 2024.\
[DOI](https://doi.org/10.1609/aaai.v38i16.29783)
| [PDF](https://ojs.aaai.org/index.php/AAAI/article/view/29783/31352)

### - Structured Rationalization via Tree kernel methods -

**Description:**\
There are several techniques for transforming text into abstract structured content (AMR graphs, Parse trees, etc...). 
We are interested in applying rationalization in these contexts by also enforcing some structural constraints depending on the given scenario of application.
The constraints describe which type of allowed structured the rationalization system can extract. 
In the case of tree kernels, these structures are different types of trees.

**Contact:** [Federico Ruggeri](mailto:federico.ruggeri6@unibo.it)

**References:**

**Tree-constrained Graph Neural Networks for Argument Mining**\
Federico Ruggeri, Marco Lippi, Paolo Torroni\
September 2021\
[PDF](https://arxiv.org/abs/2110.00124)

### - Knowledge Extraction from Rationalization -

**Description:**\
Rationalization is a type of example-specific explanation.
However, samples belonging to the same class might share similar rationales.
The idea is to define ways to go from a local explanation (i.e., rationalization) to a global explanation (i.e., knowledge base) by aggregating and summarizing extracted rationales. 
This can be done with LLMs (e.g., prompting techniques) or other solutions.

**Contact:** [Federico Ruggeri](mailto:federico.ruggeri6@unibo.it)

**References:**

**A Game Theoretic Approach to Class-wise Selective Rationalization**\
Shiyu Chang, Yang Zhang, Mo Yu, Tommi S. Jaakkola.
33rd Conference on Neural Information Processing Systems (NeurIPS), Vancouver, Canada, 2019.\
[PDF](https://papers.neurips.cc/paper_files/paper/2019/file/5ad742cd15633b26fdce1b80f7b39f7c-Paper.pdf)
