---
title: "A Dataset of Argumentative Dialogues on Scientific Papers" 
date: 2023-07-01
tags: ["natural language processing", "corpus", "benchmark", "argument mining", "dialogues", "scientific papers"]
author: ["Federico Ruggeri", "Mohsen Mesgar", "Iryna Gurevych"]
description: "We introduce ArgSciChat, a dataset of 41 argumentative dialogues between scientists on 20 NLP papers." 
summary: "We introduce ArgSciChat, a dataset of 41 argumentative dialogues between scientists on 20 NLP papers." 
cover:
    image: "paper.png"
    alt: "A Dataset of Argumentative Dialogues on Scientific Papers"
    relative: true
editPost:
    URL: "https://github.com/federicoruggeri/hugo-website"
    Text: "Association for Computational Linguistics"

---

---

##### Download

+ [Paper](paper.pdf)
+ [Code and data](https://github.com/UKPLab/acl2023-argscichat)

---

##### Abstract

With recent advances in question-answering models, various datasets have been collected to improve and study the effectiveness of these models on scientific texts. Questions and answers in these datasets explore a scientific paper by seeking factual information from the paper’s content. However, these datasets do not tackle the argumentative content of scientific papers, which is of huge importance in persuasiveness of a scientific discussion. We introduce ArgSciChat, a dataset of 41 argumentative dialogues between scientists on 20 NLP papers. The unique property of our dataset is that it includes both exploratory and argumentative questions and answers in a dialogue discourse on a scientific paper. Moreover, the size of ArgSciChat demonstrates the difficulties in collecting dialogues for specialized domains. Thus, our dataset is a challenging resource to evaluate dialogue agents in low-resource domains, in which collecting training data is costly. We annotate all sentences of dialogues in ArgSciChat and analyze them extensively. The results confirm that dialogues in ArgSciChat include exploratory and argumentative interactions. Furthermore, we use our dataset to fine-tune and evaluate a pre-trained document-grounded dialogue agent. The agent achieves a low performance on our dataset, motivating a need for dialogue agents with a capability to reason and argue about their answers. We publicly release ArgSciChat.

---

##### Citation

Federico Ruggeri, Mohsen Mesgar, and Iryna Gurevych. 2023. A Dataset of Argumentative Dialogues on Scientific Papers. In Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 7684–7699, Toronto, Canada. Association for Computational Linguistics.

```latex
@inproceedings{ruggeri-etal-2023-dataset,
    title = "A Dataset of Argumentative Dialogues on Scientific Papers",
    author = "Ruggeri, Federico  and
      Mesgar, Mohsen  and
      Gurevych, Iryna",
    editor = "Rogers, Anna  and
      Boyd-Graber, Jordan  and
      Okazaki, Naoaki",
    booktitle = "Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = jul,
    year = "2023",
    address = "Toronto, Canada",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.acl-long.425/",
    doi = "10.18653/v1/2023.acl-long.425",
    pages = "7684--7699",
    abstract = "With recent advances in question-answering models, various datasets have been collected to improve and study the effectiveness of these models on scientific texts. Questions and answers in these datasets explore a scientific paper by seeking factual information from the paper{'}s content. However, these datasets do not tackle the argumentative content of scientific papers, which is of huge importance in persuasiveness of a scientific discussion. We introduce ArgSciChat, a dataset of 41 argumentative dialogues between scientists on 20 NLP papers. The unique property of our dataset is that it includes both exploratory and argumentative questions and answers in a dialogue discourse on a scientific paper. Moreover, the size of ArgSciChat demonstrates the difficulties in collecting dialogues for specialized domains. Thus, our dataset is a challenging resource to evaluate dialogue agents in low-resource domains, in which collecting training data is costly. We annotate all sentences of dialogues in ArgSciChat and analyze them extensively. The results confirm that dialogues in ArgSciChat include exploratory and argumentative interactions. Furthermore, we use our dataset to fine-tune and evaluate a pre-trained document-grounded dialogue agent. The agent achieves a low performance on our dataset, motivating a need for dialogue agents with a capability to reason and argue about their answers. We publicly release ArgSciChat."
}
```
