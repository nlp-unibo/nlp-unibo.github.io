---
title: "A Corpus for Sentence-Level Subjectivity Detection on English News Articles" 
date: 2024-05-01
tags: ["Natural language processing", "benchmark", 'subjectivity detection', 'corpus', 'english', 'fact-checking']
author: ["Francesco Antici", "Federico Ruggeri", "Andrea Galassi", "Katerina Korre", "Arianna Muti", "Alessandra Bardi", "Alice Fedotova", "Alberto Barrón-Cedeño"]
description: "We develop novel annotation guidelines for sentence-level subjectivity detection, which are not limited to language-specific cues." 
summary: "We develop novel annotation guidelines for sentence-level subjectivity detection, which are not limited to language-specific cues." 
cover:
    image: "paper.jpg"
    alt: "A Corpus for Sentence-Level Subjectivity Detection on English News Articles"
    relative: true
editPost:
    URL: "https://github.com/federicoruggeri/hugo-website"
    Text: "Association for Computational Linguistics"

---

---

##### Download

+ [Paper](paper.pdf)
+ [Code and data](https://github.com/nlp-unibo/newssd-eng)

---

##### Abstract

We develop novel annotation guidelines for sentence-level subjectivity detection, which are not limited to language-specific cues. We use our guidelines to collect NewsSD-ENG, a corpus of 638 objective and 411 subjective sentences extracted from English news articles on controversial topics. Our corpus paves the way for subjectivity detection in English and across other languages without relying on language-specific tools, such as lexicons or machine translation. We evaluate state-of-the-art multilingual transformer-based models on the task in mono-, multi-, and cross-language settings. For this purpose, we re-annotate an existing Italian corpus. We observe that models trained in the multilingual setting achieve the best performance on the task.

---

##### Citation

Francesco Antici, Federico Ruggeri, Andrea Galassi, Katerina Korre, Arianna Muti, Alessandra Bardi, Alice Fedotova, and Alberto Barrón-Cedeño. 2024. A Corpus for Sentence-Level Subjectivity Detection on English News Articles. In Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024), pages 273–285, Torino, Italia. ELRA and ICCL.

```latex
@inproceedings{antici-etal-2024-corpus,
    title = "A Corpus for Sentence-Level Subjectivity Detection on {E}nglish News Articles",
    author = "Antici, Francesco  and
      Ruggeri, Federico  and
      Galassi, Andrea  and
      Korre, Katerina  and
      Muti, Arianna  and
      Bardi, Alessandra  and
      Fedotova, Alice  and
      Barr{\'o}n-Cede{\~n}o, Alberto",
    editor = "Calzolari, Nicoletta  and
      Kan, Min-Yen  and
      Hoste, Veronique  and
      Lenci, Alessandro  and
      Sakti, Sakriani  and
      Xue, Nianwen",
    booktitle = "Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024)",
    month = may,
    year = "2024",
    address = "Torino, Italia",
    publisher = "ELRA and ICCL",
    url = "https://aclanthology.org/2024.lrec-main.25/",
    pages = "273--285",
    abstract = "We develop novel annotation guidelines for sentence-level subjectivity detection, which are not limited to language-specific cues. We use our guidelines to collect NewsSD-ENG, a corpus of 638 objective and 411 subjective sentences extracted from English news articles on controversial topics. Our corpus paves the way for subjectivity detection in English and across other languages without relying on language-specific tools, such as lexicons or machine translation. We evaluate state-of-the-art multilingual transformer-based models on the task in mono-, multi-, and cross-language settings. For this purpose, we re-annotate an existing Italian corpus. We observe that models trained in the multilingual setting achieve the best performance on the task."
}
```
