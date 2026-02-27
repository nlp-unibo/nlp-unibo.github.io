---
title: Legal Analytics
date: 2026-02-27

tags:
  - legal
  - legal analytics
  - research

summary: The process of automatically understanding and extracting legal knowledge from legal documents.

---

### Argumentation and Argument Schema 

We have defined legal arguments and developed benchmarks for training machine learning in automatically identifying them.
Legal arguments are relevant to several legal tasks (e.g., judgement prediction) as they encode important decisions and opinions that are tailored to a given problem.
Moreover, legal experts are interested in assessing if there are some recurring patterns concerning legal arguments.
For instance, do similar documents convey similar legal arguments?
Can we compare documents based on their arguments? 

### Judgement Prediction 

The automatic prediction of the judge's decision.
We have developed benchmarks and assessed standard and transformer-based models on this task. 

### Interpretability 

We have explored memory-augmented neural networks and decision trees to define more interpretable models, encouraging user trustworthiness based on explanations in addition to model efficiency. 

### Unfair Clause Detection 

The automatic  identification and classification of unfair clauses.
We have developed benchmarks on this topic. 

### Summarization 

Can machine learning models summarize legal documents based on certain guidelines?
Are the developed summaries useful to legal experts? 

### Cross-linguality

We have developed some methods to project labels from similar documents written in different languages. 

### Information Retrieval 

The automatic retrieval of legal documents and knowledge based on a similarity metric.
This also link to the argumentation topic if we use arguments (either quantitatively or qualitatively) to compare and rank retrieved documents. 