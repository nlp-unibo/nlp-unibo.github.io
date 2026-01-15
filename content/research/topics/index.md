---
title: "Research Topics"
date: 2025-01-01
tags: ["Research", "Research Topics"]
author: "Federico Ruggeri"
description: "Academic research topics." 
summary: "Academic research topics.." 
cover:
    image: "topics.jpg"
    alt: "Research Topics"
    relative: true
showToc: true
disableAnchoredHeadings: false

---

## Useful Links

+ [Research Topics](https://site.unibo.it/nlp/en/teaching/project-topics)

## Argumentation Mining

One of our main research interests is Argument/Argumentation Mining (AM). It can be informally described as the problem of automatically detecting and extracting arguments from the text. Arguments are usually represented as a combination of a premise (a fact) that supports a subjective conclusion (opinion, claim). Argumentation Mining touches a wide variety of well-known NLP tasks, spanning from sentiment analysis, stance detection to summarization and dialogue systems.

### Multimodal Argument Mining

**Description:** Make use of speech information (e.g. prosody) to enhance the set of features that can be used to detect arguments. Speech can either be represented by means of ad-hoc feature extraction methods (e.g. MFCC) or via end-to-end architectures. Few existing corpora both offer argument annotation layers and speech data regarding a given text document.

**Contact:** [Eleonora Mancini](mailto:e.mancini@unibo.it), [Federico Ruggeri](mailto:federico.ruggeri6@unibo.it)

**References:** 
- Eleonora Mancini, Federico Ruggeri, Stefano Colamonaco, Andrea Zecca, Samuele Marro, Paolo Torroni. 2024. MAMKit: A Comprehensive Multimodal Argument Mining Toolkit. In Proceedings of the 11th Workshop on Argument Mining (ArgMining 2024), pages 69–82, Bangkok, Thailand. Association for Computational Linguistics.
- Eleonora Mancini, Federico Ruggeri, Paolo Torroni. 2024. Multimodal Fallacy Classification in Political Debates. In Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics (Volume 2: Short Papers).
- Eleonora Mancini, Federico Ruggeri, Andrea Galassi, and Paolo Torroni. 2022. Multimodal Argument Mining: A Case Study in Political Debates. In Proceedings of the 9th Workshop on Argument Mining, pages 158–170, Online and in Gyeongju, Republic of Korea. International Conference on Computational Linguistics.

### Hate Speech Detection with Argumentative Reasoning

**Description:** Hate speech often lies on implicit content and subtle reasoning nuances. Our idea is to apply argumentative reasoning to hate speech to make implicit content explicit in order to define more interpretable and user-friendly hate speech detection systems.

**Contact:** [Federico Ruggeri](mailto:federico.ruggeri6@unibo.it), [Arianna Muti](mailto:arianna.muti@unibocconi.it)

**References**:
- Arianna Muti, Federico Ruggeri, Khalid Al-Khatib, Alberto Barrón-Cedeño, Tommaso Caselli. 2024. Language is Scary when Over-Analyzed: Unpacking Implied Misogynistic Reasoning with Argumentation Theory-Driven Prompts. The 2024 Conference on Empirical Methods in Natural Language Processing. 
- Arianna Muti, Federico Ruggeri, Cagri Toraman, Lorenzo Musetti, Samuel Algherini, Silvia Ronchi, Gianmarco Saretto, Caterina Zapparoli, Alberto Barrón-Cedeño. 2024. PejorativITy: Disambiguating Pejorative Epithets to Improve Misogyny Detection in Italian Tweets. In Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024), pages 12700–12711, Torino, Italia. ELRA and ICCL.

## Unstructured Knowledge Integration
We are interested in developing deep learning models that are capable of employing knowledge in the form of natural language. Such knowledge is easy to interpret and to define (compared to structured representations like syntactic trees, knowledge graphs and symbolic rules). Unstructured knowledge increases the interpretability of models and goes in the direction of defining a realistic type of artificial intelligence. However, properly integrating this type of information is particularly challenging due to its inherent ambiguity and variability.

### Text Classification with Guidelines Only

**Description:** The standard approach for training a machine learning model on a task is to provide an annotated dataset (X, Y). The dataset is built by providing unlabeled data X to a group of annotators previously trained on a set of annotation guidelines G. Annotators label data X via a given class set C.
The main issue of this approach is that annotators define the mapping from data X to the class set C via the guidelines G, while machine learning models are trained to learn the same mapping without guidelines G. Consequently, these models can learn any kind of mapping from X to C that better fits given data. Our idea is to directly provide guidelines G to models without any access to class labels during training.

**Contact:** [Federico Ruggeri](mailto:federico.ruggeri6@unibo.it)

**References:**
- Federico Ruggeri, Eleonora Misino, Arianna Muti, Katerina Korre, Paolo Torroni, Alberto Barrón-Cedeño. 2024. Let Guidelines Guide You: A Prescriptive Guideline-Centered Data Annotation Methodology. ArXiv Pre-print.

## Multi-cultural Abusive and Hate Speech Detection

**Description:** What is attributable as abusive or hate speech depends on the given socio-cultural context. The same text might be reputed offensive by a certain culture, allowed by another, and, in the most extreme case, legally prosecutable by a third one. Our aim is to evaluate how machine learning model are affected by different definitions of abusive and hate speech to promote awareness in developing accurate abusive speech detection systems.

**Contact:** [Federico Ruggeri](mailto:federico.ruggeri6@unibo.it), [Katerina Korre](k.korre@athenarc.gr), [Arianna Muti](mailto:arianna.muti@unibocconi.it)

**References:**
- Katerina Korre, Arianna Muti, Federico Ruggeri, Alberto Barrón-Cedeño. 2025. Untangling Hate Speech Definitions: A Semantic Componential Analysis Across Cultures and Domains. NAACL Findings.

## Interpretability
We are interested in developing interpretable models. An interpretable model exposes means for identifying the process that leads from an input to a prediction. We are mainly focused on interpretability by design in text classification.

**Current topics of interest:**

- **Selective Rationalization:** The process of learning by providing highlights as explanations is denoted as selective rationalization. Highlights are a subset of input texts meant to be interpretable by a user and faithfully describe the inference process of a classification model. A popular architecture for selective rationalization is the Select-then-Predict Pipeline (SPP): a generator selects the rationale to be fed to a predictor. It has been shown that SPP suffers from local minima derived by sub-optimal interplay between the generator and predictor, a phenomenon known as interlocking.

- **Knowledge Extraction:** The process of extracting interpretable knowledge from data-driven processes. Our aim is to distill a common knowledge from several examples when addressing a downstream task.

### Mixture of Experts for Rationalization

**Description:** Mixture of Experts (MoE) is a technique whereby several models are trained on the same data, each specializing in a certain subset. MoE have been shown to be successful in a variety of applications and their original formulation dates back early 2000s. The idea is to understand whether we can develop a MoE model for selective rationalization to address interlocking.

**Contact:** [Federico Ruggeri](mailto:federico.ruggeri6@unibo.it)

**References:**
- Weilin Cai, Juyong Jiang, Fan Wang, Jing Tang, Sunghun Kim, Jiayi Huang. 2024. A Survey on Mixture of Experts. ArXiv Pre-print.

### Rationalization via LLMs

**Description:** LLMs are ubiquitous in NLP. Our aim is to evaluate LLM capabilities in performing selective rationalization via prompting. How do they compare w.r.t. traditional SPP models?

**Contact:** [Federico Ruggeri](mailto:federico.ruggeri6@unibo.it)

**References:**
- Linan Yue, Qi Liu, Yichao Du, Li Wang, Weibo Gao, Yanqing An. 2024. Towards Faithful Explanations: Boosting Rationalization with Shortcuts Discovery. The Twelfth International Conference on Learning Representations.
- S Hu, K Yu. 2024. Learning Robust Rationales for Model Explainability: A Guidance-Based Approach. Proceedings of the AAAI Conference on Artificial Intelligence.

### Structured Rationalization via Tree kernel methods

**Description:** There are several techniques for transforming text into abstract structured content (AMR graphs, Parse trees, etc...). We are interested in applying rationalization in these contexts by also enforcing some structural constraints depending on the given scenario of application. The constraints describe which type of allowed structured the rationalization system can extract. In the case of tree kernels, these structures are different types of trees.

**Contact:** [Federico Ruggeri](mailto:federico.ruggeri6@unibo.it)

**References:**
- Federico Ruggeri, Marco Lippi, Paolo Torroni. 2021. Tree-constrained graph neural networks for argument mining. ArXiv Pre-print.

### Knowledge Extraction from Rationalization

**Description:** Rationalization is a type of example-specific explanation. However, samples belonging to the same class might share similar rationales. The idea is to define ways to go from a local explanation (i.e., rationalization) to a global explanation (i.e., knowledge base) by aggregating and summarizing extracted rationales. This can be done with LLMs (e.g., prompting techniques) or other solutions.

**Contact:** [Federico Ruggeri](mailto:federico.ruggeri6@unibo.it)

**References:**
Shiyu Chang, Yang Zhang, Mo Yu, Tommi S. Jaakkola. 2019. A Game Theoretic Approach to Class-wise Selective Rationalization. 33rd Conference on Neural Information Processing Systems (NeurIPS 2019), Vancouver, Canada. 