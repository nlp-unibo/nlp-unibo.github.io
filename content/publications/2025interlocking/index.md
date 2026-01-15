---
title: "Interlocking-free Selective Rationalization Through Genetic-based Learning" 
date: 2025-08-01
tags: ["selective rationalization", "highlights", "XAI", "genetic algorithms", "select-then-predict", "text classification"]
author: ["Federico Ruggeri","Gaetano Signorelli"]
description: "We present GenSPP, a selective rationalization framework that eliminates interlocking via genetic-based search" 
summary: "We present GenSPP, a selective rationalization framework that eliminates interlocking via genetic-based search" 
cover:
    image: "paper.png"
    alt: "Interlocking-free Selective Rationalization Through Genetic-based Learning"
    relative: true
editPost:
    URL: "https://github.com/federicoruggeri/hugo-website"
    Text: "Association for Computational Linguistics"

---

---

##### Download

+ [Paper](paper.pdf)
+ [Code and data](https://github.com/nlp-unibo/gen-spp)

---

##### Abstract

A popular end-to-end architecture for selective rationalization is the select-then-predict pipeline, comprising a generator to extract highlights fed to a predictor. Such a cooperative system suffers from suboptimal equilibrium minima due to the dominance of one of the two modules, a phenomenon known as interlocking. While several contributions aimed at addressing interlocking, they only mitigate its effect, often by introducing feature-based heuristics, sampling, and ad-hoc regularizations. We present GenSPP, the first interlocking-free architecture for selective rationalization that does not require any learning overhead, as the above-mentioned. GenSPP avoids interlocking by performing disjoint training of the generator and predictor via genetic global search. Experiments on a synthetic and a real-world benchmark show that our model outperforms several state-of-the-art competitors.

---

##### Citation

Federico Ruggeri and Gaetano Signorelli. 2025. Interlocking-free Selective Rationalization Through Genetic-based Learning. In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 1175–1191, Vienna, Austria. Association for Computational Linguistics.

```latex
@inproceedings{ruggeri-signorelli-2025-interlocking,
    title = "Interlocking-free Selective Rationalization Through Genetic-based Learning",
    author = "Ruggeri, Federico  and
      Signorelli, Gaetano",
    editor = "Che, Wanxiang  and
      Nabende, Joyce  and
      Shutova, Ekaterina  and
      Pilehvar, Mohammad Taher",
    booktitle = "Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = jul,
    year = "2025",
    address = "Vienna, Austria",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.acl-long.59/",
    doi = "10.18653/v1/2025.acl-long.59",
    pages = "1175--1191",
    ISBN = "979-8-89176-251-0",
    abstract = "A popular end-to-end architecture for selective rationalization is the select-then-predict pipeline, comprising a generator to extract highlights fed to a predictor. Such a cooperative system suffers from suboptimal equilibrium minima due to the dominance of one of the two modules, a phenomenon known as interlocking. While several contributions aimed at addressing interlocking, they only mitigate its effect, often by introducing feature-based heuristics, sampling, and ad-hoc regularizations. We present GenSPP, the first interlocking-free architecture for selective rationalization that does not require any learning overhead, as the above-mentioned. GenSPP avoids interlocking by performing disjoint training of the generator and predictor via genetic global search. Experiments on a synthetic and a real-world benchmark show that our model outperforms several state-of-the-art competitors."
}
```
