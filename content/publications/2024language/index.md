---
title: "Language is Scary when Over-Analyzed: Unpacking Implied Misogynistic Reasoning with Argumentation Theory-Driven Prompts" 
date: 2025-08-01
tags: ["misogyny detection", "argument mining", "natural language inference", "reasoning", "large language models"]
author: ["Arianna Muti", "Federico Ruggeri", "Khalid Al Khatib", "Alberto Barrón-Cedeño", "Tommaso Caselli"]
description: "We propose the task of implicit misogyny detection as an Argumentative Reasoning task, by assessing the quality of LLMs in generating the warrants which require reasoning skills in order to be extracted." 
summary: "We propose the task of implicit misogyny detection as an Argumentative Reasoning task, by assessing the quality of LLMs in generating the warrants which require reasoning skills in order to be extracted." 
cover:
    image: "paper.png"
    alt: "Language is Scary when Over-Analyzed: Unpacking Implied Misogynistic Reasoning with Argumentation Theory-Driven Prompt"
    relative: true
editPost:
    URL: "https://github.com/federicoruggeri/hugo-website"
    Text: "Association for Computational Linguistics"

---

---

##### Download

+ [Paper](paper.pdf)
+ [Code and data](https://github.com/arimuti/Argument-Reasoning-for-Implicit-Misogyny)

---

##### Abstract

We propose misogyny detection as an Argumentative Reasoning task and we investigate the capacity of large language models (LLMs) to understand the implicit reasoning used to convey misogyny in both Italian and English. The central aim is to generate the missing reasoning link between a message and the implied meanings encoding the misogyny. Our study uses argumentation theory as a foundation to form a collection of prompts in both zero-shot and few-shot settings. These prompts integrate different techniques, including chain-of-thought reasoning and augmented knowledge. Our findings show that LLMs fall short on reasoning capabilities about misogynistic comments and that they mostly rely on their implicit knowledge derived from internalized common stereotypes about women to generate implied assumptions, rather than on inductive reasoning.

---

##### Citation

Arianna Muti, Federico Ruggeri, Khalid Al Khatib, Alberto Barrón-Cedeño, and Tommaso Caselli. 2024. Language is Scary when Over-Analyzed: Unpacking Implied Misogynistic Reasoning with Argumentation Theory-Driven Prompts. In Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing, pages 21091–21107, Miami, Florida, USA. Association for Computational Linguistics.

```latex
@inproceedings{muti-etal-2024-language,
    title = "Language is Scary when Over-Analyzed: Unpacking Implied Misogynistic Reasoning with Argumentation Theory-Driven Prompts",
    author = "Muti, Arianna  and
      Ruggeri, Federico  and
      Khatib, Khalid Al  and
      Barr{\'o}n-Cede{\~n}o, Alberto  and
      Caselli, Tommaso",
    editor = "Al-Onaizan, Yaser  and
      Bansal, Mohit  and
      Chen, Yun-Nung",
    booktitle = "Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing",
    month = nov,
    year = "2024",
    address = "Miami, Florida, USA",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2024.emnlp-main.1174/",
    doi = "10.18653/v1/2024.emnlp-main.1174",
    pages = "21091--21107",
    abstract = "We propose misogyny detection as an Argumentative Reasoning task and we investigate the capacity of large language models (LLMs) to understand the implicit reasoning used to convey misogyny in both Italian and English. The central aim is to generate the missing reasoning link between a message and the implied meanings encoding the misogyny. Our study uses argumentation theory as a foundation to form a collection of prompts in both zero-shot and few-shot settings. These prompts integrate different techniques, including chain-of-thought reasoning and augmented knowledge. Our findings show that LLMs fall short on reasoning capabilities about misogynistic comments and that they mostly rely on their implicit knowledge derived from internalized common stereotypes about women to generate implied assumptions, rather than on inductive reasoning."
}
```
