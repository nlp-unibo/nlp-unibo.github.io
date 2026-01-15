---
title: "PejorativITy: Disambiguating Pejorative Epithets to Improve Misogyny Detection in Italian Tweets" 
date: 2024-05-01
tags: ["Natural language processing", "corpus", "pejorative epithets", "word sense disambiguation", "misogyny", "italian"]
author: ["Arianna Muti", "Federico Ruggeri", "Cagri Toraman", "Alberto Barrón-Cedeño", "Samuel Algherini", "Lorenzo Musetti", "Silvia Ronchi", "Gianmarco Saretto", "Caterina Zapparoli"]
description: "We present PejorativITy, a novel corpus of 1,200 manually annotated Italian tweets for pejorative language at the word level and misogyny at the sentence level. " 
summary: "We present PejorativITy, a novel corpus of 1,200 manually annotated Italian tweets for pejorative language at the word level and misogyny at the sentence level. " 
cover:
    image: "paper.png"
    alt: "PejorativITy: Disambiguating Pejorative Epithets to Improve Misogyny Detection in Italian Tweets"
    relative: true
editPost:
    URL: "https://github.com/federicoruggeri/hugo-website"
    Text: "Association for Computational Linguistics"

---

---

##### Download

+ [Paper](paper.pdf)
+ [Code and data](https://github.com/arimuti/PejorativITy)

---

##### Abstract

Misogyny is often expressed through figurative language. Some neutral words can assume a negative connotation when functioning as pejorative epithets. Disambiguating the meaning of such terms might help the detection of misogyny. In order to address such task, we present PejorativITy, a novel corpus of 1,200 manually annotated Italian tweets for pejorative language at the word level and misogyny at the sentence level. We evaluate the impact of injecting information about disambiguated words into a model targeting misogyny detection. In particular, we explore two different approaches for injection: concatenation of pejorative information and substitution of ambiguous words with univocal terms. Our experimental results, both on our corpus and on two popular benchmarks on Italian tweets, show that both approaches lead to a major classification improvement, indicating that word sense disambiguation is a promising preliminary step for misogyny detection. Furthermore, we investigate LLMs’ understanding of pejorative epithets by means of contextual word embeddings analysis and prompting.

---

##### Citation

Arianna Muti, Federico Ruggeri, Cagri Toraman, Alberto Barrón-Cedeño, Samuel Algherini, Lorenzo Musetti, Silvia Ronchi, Gianmarco Saretto, and Caterina Zapparoli. 2024. PejorativITy: Disambiguating Pejorative Epithets to Improve Misogyny Detection in Italian Tweets. In Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024), pages 12700–12711, Torino, Italia. ELRA and ICCL.

```latex
@inproceedings{muti-etal-2024-pejorativity,
    title = "{P}ejorativ{IT}y: Disambiguating Pejorative Epithets to Improve Misogyny Detection in {I}talian Tweets",
    author = "Muti, Arianna  and
      Ruggeri, Federico  and
      Toraman, Cagri  and
      Barr{\'o}n-Cede{\~n}o, Alberto  and
      Algherini, Samuel  and
      Musetti, Lorenzo  and
      Ronchi, Silvia  and
      Saretto, Gianmarco  and
      Zapparoli, Caterina",
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
    url = "https://aclanthology.org/2024.lrec-main.1112/",
    pages = "12700--12711",
    abstract = "Misogyny is often expressed through figurative language. Some neutral words can assume a negative connotation when functioning as pejorative epithets. Disambiguating the meaning of such terms might help the detection of misogyny. In order to address such task, we present PejorativITy, a novel corpus of 1,200 manually annotated Italian tweets for pejorative language at the word level and misogyny at the sentence level. We evaluate the impact of injecting information about disambiguated words into a model targeting misogyny detection. In particular, we explore two different approaches for injection: concatenation of pejorative information and substitution of ambiguous words with univocal terms. Our experimental results, both on our corpus and on two popular benchmarks on Italian tweets, show that both approaches lead to a major classification improvement, indicating that word sense disambiguation is a promising preliminary step for misogyny detection. Furthermore, we investigate LLMs' understanding of pejorative epithets by means of contextual word embeddings analysis and prompting."
}
```
