---
title: "Argumentation Structure Prediction in CJEU Decisions on Fiscal State Aid" 
date: 2023-09-07
tags: ["natural language processing", "legal", "CJEU", "Argument Mining", "structure prediction"]
author: ["Piera Santin", "Giulia Grundler", "Andrea Galassi", "Federico Galli", "Francesca Lagioia", "Elena Palmieri", "Federico Ruggeri", "Giovanni Sartor", "Paolo Torroni"]
description: "We study how propositions are combined inhigher-level structures and how the relations between propositionscan be predicted by NLP models." 
summary: "We study how propositions are combined inhigher-level structures and how the relations between propositionscan be predicted by NLP models." 
cover:
    image: "paper.png"
    alt: "Argumentation Structure Prediction in CJEU Decisions on Fiscal State Aid"
    relative: true
editPost:
    URL: "https://github.com/federicoruggeri/hugo-website"
    Text: "International Conference on Artificial Intelligence and Law"

---

---

##### Download

+ [Paper](paper.pdf)
+ [Code and data](https://github.com/adele-project/demosthenes)

---

##### Abstract

Argument structure prediction aims to identify the relations between arguments or between parts of arguments. It is a crucial task in legal argument mining, where it could help identifying motivations behind judgments or even fallacies or inconsistencies. It is also a very challenging task, which is relatively underdeveloped compared to other argument mining tasks, owing to a number of reasons including a low availability of datasets and a high complexity of the reasoning involved. In this work, we address argumentative link prediction in decisions by Court of Justice of the European Union on fiscal state aid. We study how propositions are combined in higher-level structures and how the relations between propositions can be predicted by NLP models. To this end, we present a novel annotation scheme and use it to extend a dataset from literature with an additional annotation layer. We use our new dataset to run an empirical study, where we compare two architectures and explore different combinations of hyperparameters and training regimes. Our results indicate that an ensemble of residual networks yields the best results.

---

##### Citation

Piera Santin, Giulia Grundler, Andrea Galassi, Federico Galli, Francesca Lagioia, Elena Palmieri, Federico Ruggeri, Giovanni Sartor, and Paolo Torroni. Argumentation structure prediction in cjeu decisions on fiscal state aid. In Proceedings of the Nineteenth International Conference on Artificial Intelligence and Law, ICAIL ’23, page 247–256, New York, NY, USA, 2023. Association for Computing Machinery. 

```latex
@inproceedings{santin-etal-2023-argumentation-cjeu,
author = {Santin, Piera and Grundler, Giulia and Galassi, Andrea and Galli, Federico and Lagioia, Francesca and Palmieri, Elena and Ruggeri, Federico and Sartor, Giovanni and Torroni, Paolo},
title = {Argumentation Structure Prediction in CJEU Decisions on Fiscal State Aid},
year = {2023},
isbn = {9798400701979},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3594536.3595174},
doi = {10.1145/3594536.3595174},
abstract = {Argument structure prediction aims to identify the relations between arguments or between parts of arguments. It is a crucial task in legal argument mining, where it could help identifying motivations behind judgments or even fallacies or inconsistencies. It is also a very challenging task, which is relatively underdeveloped compared to other argument mining tasks, owing to a number of reasons including a low availability of datasets and a high complexity of the reasoning involved. In this work, we address argumentative link prediction in decisions by Court of Justice of the European Union on fiscal state aid. We study how propositions are combined in higher-level structures and how the relations between propositions can be predicted by NLP models. To this end, we present a novel annotation scheme and use it to extend a dataset from literature with an additional annotation layer. We use our new dataset to run an empirical study, where we compare two architectures and explore different combinations of hyperparameters and training regimes. Our results indicate that an ensemble of residual networks yields the best results.},
booktitle = {Proceedings of the Nineteenth International Conference on Artificial Intelligence and Law},
pages = {247–256},
numpages = {10},
keywords = {Link Prediction, CJEU decisions, Argument Mining, Legal Argument},
location = {Braga, Portugal},
series = {ICAIL '23}
}
```
