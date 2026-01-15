---
title: "Untangling Hate Speech Definitions: A Semantic Componential Analysis Across Cultures and Domains" 
date: 2025-04-29
tags: ["hate speech definitions", "cross-domain analysis", "cross-cultural analysis"]
author: ["Katerina Korre", "Arianna Muti", "Federico Ruggeri", "Alberto Barrón-Cedeño"]
description: "We propose a Semantic Componential Analysis (SCA) framework for a cross-cultural and cross-domain analysis of hate speech definitions." 
summary: "We propose a Semantic Componential Analysis (SCA) framework for a cross-cultural and cross-domain analysis of hate speech definitions." 
cover:
    image: "paper.png"
    alt: "Untangling Hate Speech Definitions: A Semantic Componential Analysis Across Cultures and Domains"
    relative: true
editPost:
    URL: "https://github.com/federicoruggeri/hugo-website"
    Text: "Association for Computational Linguistics"

---

---

##### Download

+ [Paper](paper.pdf)
+ [Code and data](https://github.com/katkorre/SCA-of-Hate-Speech)

---

##### Abstract

Hate speech relies heavily on cultural influences, leading to varying individual interpretations. For that reason, we propose a Semantic Componential Analysis (SCA) framework for a cross-cultural and cross-domain analysis of hate speech definitions. We create the first dataset of hate speech definitions encompassing 493 definitions from more than 100 cultures, drawn from five key domains: online dictionaries, academic research, Wikipedia, legal texts, and online platforms. By decomposing these definitions into semantic components,our analysis reveals significant variation across definitions, yet many domains borrow definitions from one another without taking into account the target culture. We conduct zero-shot model experiments using our proposed dataset, employing three popular open-sourced LLMs to understand the impact of different definitions on hate speech detection. Our findings indicate that LLMs are sensitive to definitions: responses for hate speech detection change according to the complexity of definitions used in the prompt.

---

##### Citation

Katerina Korre, Arianna Muti, Federico Ruggeri, and Alberto Barrón-Cedeño. 2025. Untangling Hate Speech Definitions: A Semantic Componential Analysis Across Cultures and Domains. In Findings of the Association for Computational Linguistics: NAACL 2025, pages 3184–3198, Albuquerque, New Mexico. Association for Computational Linguistics.

```latex
@inproceedings{korre-etal-2025-untangling,
    title = "Untangling Hate Speech Definitions: A Semantic Componential Analysis Across Cultures and Domains",
    author = "Korre, Katerina  and
      Muti, Arianna  and
      Ruggeri, Federico  and
      Barr{\'o}n-Cede{\~n}o, Alberto",
    editor = "Chiruzzo, Luis  and
      Ritter, Alan  and
      Wang, Lu",
    booktitle = "Findings of the Association for Computational Linguistics: NAACL 2025",
    month = apr,
    year = "2025",
    address = "Albuquerque, New Mexico",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.findings-naacl.175/",
    doi = "10.18653/v1/2025.findings-naacl.175",
    pages = "3184--3198",
    ISBN = "979-8-89176-195-7",
    abstract = "Hate speech relies heavily on cultural influences, leading to varying individual interpretations. For that reason, we propose a Semantic Componential Analysis (SCA) framework for a cross-cultural and cross-domain analysis of hate speech definitions. We create the first dataset of hate speech definitions encompassing 493 definitions from more than 100 cultures, drawn from five key domains: online dictionaries, academic research, Wikipedia, legal texts, and online platforms. By decomposing these definitions into semantic components,our analysis reveals significant variation across definitions, yet many domains borrow definitions from one another without taking into account the target culture. We conduct zero-shot model experiments using our proposed dataset, employing three popular open-sourced LLMs to understand the impact of different definitions on hate speech detection. Our findings indicate that LLMs are sensitive to definitions: responses for hate speech detection change according to the complexity of definitions used in the prompt."
}
```
