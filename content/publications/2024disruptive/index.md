---
title: "Disruptive situation detection on public transport through speech emotion recognition" 
date: 2024-03-01
tags: ["Speech emotion recognition", "Affective computing", "Natural language processing", "Machine learning", "Data augmentation"]
author: ["Eleonora Mancini", "Andrea Galassi", "Federico Ruggeri", "Paolo Torroni"]
description: "We propose to frame disruptive situation detection as a speech emotion recognition task. To validate our hypotheses, we carry out an extensive experimental study focusing on the development of a model characterized by speaker/gender independence, robustness to noise, and robustness against multiple voices." 
summary: "We propose to frame disruptive situation detection as a speech emotion recognition task. To validate our hypotheses, we carry out an extensive experimental study focusing on the development of a model characterized by speaker/gender independence, robustness to noise, and robustness against multiple voices." 
cover:
    image: "paper.png"
    alt: "Disruptive situation detection on public transport through speech emotion recognition"
    relative: true
editPost:
    URL: "https://github.com/federicoruggeri/hugo-website"
    Text: "Intelligent Systems with Applications"

---

---

##### Download

+ [Paper](paper.pdf)
+ [Code and data](https://github.com/helemanc/ambient-intelligence)

---

##### Abstract

Disruptive situations are emotionally-charged events diverging from ordinary behavior, like people fighting or screaming. Public transports are one type of social environment where disruptive situation may occur, and their timely detection may bring significant improvements to people's safety. Current approaches to disruptive situation detection, typically based on CCTVs, do not take the emotional dimension into account. Conversely, we propose to frame such a problem as a speech emotion recognition task.
To validate our hypotheses, we carry out an extensive experimental study focusing on the development of a model characterized by speaker/gender independence, robustness to noise, and robustness against multiple voices. We investigate a variety of audio features, classifiers, datasets, and data augmentation methods in an effort to define effective ways to address this under-investigated yet socially significant problem. Our experiments show that the proposed systems attain an F1 score of over 90% on the disruptive class, even when introducing noisy elements such as environmental noise or multiple overlapping voices. This robust performance is achieved with datasets characterized by speaker variability, gender diversity, and varying number of samples. Such promising results indicate that framing disruptive situation detection as a speech emotion recognition task could pave the way to the adoption of new types of intelligent systems with a positive impact on public safety.

---

##### Citation

 Eleonora Mancini, Andrea Galassi, Federico Ruggeri, and Paolo Torroni. Disruptive situation detection on public transport through speech emotion recognition. Intelligent Systems with Applications, 21:200305, 2024.

```latex
@article{mancini-etal-2024-disruptive,
title = {Disruptive situation detection on public transport through speech emotion recognition},
journal = {Intelligent Systems with Applications},
volume = {21},
pages = {200305},
year = {2024},
issn = {2667-3053},
doi = {https://doi.org/10.1016/j.iswa.2023.200305},
url = {https://www.sciencedirect.com/science/article/pii/S2667305323001308},
author = {Eleonora Mancini and Andrea Galassi and Federico Ruggeri and Paolo Torroni},
keywords = {Speech emotion recognition, Affective computing, Natural language processing, Machine learning, Data augmentation},
abstract = {Disruptive situations are emotionally-charged events diverging from ordinary behavior, like people fighting or screaming. Public transports are one type of social environment where disruptive situation may occur, and their timely detection may bring significant improvements to people's safety. Current approaches to disruptive situation detection, typically based on CCTVs, do not take the emotional dimension into account. Conversely, we propose to frame such a problem as a speech emotion recognition task. To validate our hypotheses, we carry out an extensive experimental study focusing on the development of a model characterized by speaker/gender independence, robustness to noise, and robustness against multiple voices. We investigate a variety of audio features, classifiers, datasets, and data augmentation methods in an effort to define effective ways to address this under-investigated yet socially significant problem. Our experiments show that the proposed systems attain an F1 score of over 90\% on the disruptive class, even when introducing noisy elements such as environmental noise or multiple overlapping voices. This robust performance is achieved with datasets characterized by speaker variability, gender diversity, and varying number of samples. Such promising results indicate that framing disruptive situation detection as a speech emotion recognition task could pave the way to the adoption of new types of intelligent systems with a positive impact on public safety.}
}
```
