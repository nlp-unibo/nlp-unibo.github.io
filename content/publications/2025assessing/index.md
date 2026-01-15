---
title: "Assessing the Reasoning Capabilities of LLMs in the context of Evidence-based Claim Verification" 
date: 2025-08-01
tags: ["Reasoning evaluation", "LLM evaluation and benchmarking", "Data resources", "Claim verification and fact checking"]
author: ["John Dougrez-Lewis", "Mahmud Elahi Akhter", "Federico Ruggeri", "Sebastian Löbbers", "Yulan He", "Maria Liakata"]
description: "We present GenSPP, a selective rationalization framework that eliminates interlocking via genetic-based search" 
summary: "Evaluation of LLMs in context of Evidence-based Claim verification to show that LLMs fail at abductive reasoning and CoT methods performance are task complexity and data domain dependant." 
cover:
    image: "paper.png"
    alt: "Assessing the Reasoning Capabilities of LLMs in the context of Evidence-based Claim Verification"
    relative: true
editPost:
    URL: "https://github.com/federicoruggeri/hugo-website"
    Text: "Association for Computational Linguistics"

---

---

##### Download

+ [Paper](paper.pdf)

---

##### Abstract

Although LLMs have shown great performance on Mathematics and Coding related reasoning tasks, the reasoning capabilities of LLMs regarding other forms of reasoning are still an open problem. Here, we examine the issue of reasoning from the perspective of claim verification. We propose a framework designed to break down any claim paired with evidence into atomic reasoning types that are necessary for verification. We use this framework to create RECV, the first claim verification benchmark, incorporating real-world claims, to assess the deductive and abductive reasoning capabilities of LLMs. The benchmark comprises of three datasets, covering reasoning problems of in creasing complexity. We evaluate three state of-the-art proprietary LLMs under multiple prompt settings. Our results show that while LLMs can address deductive reasoning prob lems, they consistently fail in cases of abductive reasoning. Moreover, we observe that enhancing LLMs with rationale generation is not always beneficial. Nonetheless, we find that generated rationales are semantically similar to those provided by humans, especially in deduc tive reasoning cases.

---

##### Citation

John Dougrez-Lewis, Mahmud Elahi Akhter, Federico Ruggeri, Sebastian Löbbers, Yulan He, and Maria Liakata. 2025. Assessing the Reasoning Capabilities of LLMs in the context of Evidence-based Claim Verification. In Findings of the Association for Computational Linguistics: ACL 2025, pages 20604–20628, Vienna, Austria. Association for Computational Linguistics.

```latex
@inproceedings{dougrez-lewis-etal-2025-assessing,
    title = "Assessing the Reasoning Capabilities of {LLM}s in the context of Evidence-based Claim Verification",
    author = {Dougrez-Lewis, John  and
      Akhter, Mahmud Elahi  and
      Ruggeri, Federico  and
      L{\"o}bbers, Sebastian  and
      He, Yulan  and
      Liakata, Maria},
    editor = "Che, Wanxiang  and
      Nabende, Joyce  and
      Shutova, Ekaterina  and
      Pilehvar, Mohammad Taher",
    booktitle = "Findings of the Association for Computational Linguistics: ACL 2025",
    month = jul,
    year = "2025",
    address = "Vienna, Austria",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.findings-acl.1059/",
    doi = "10.18653/v1/2025.findings-acl.1059",
    pages = "20604--20628",
    ISBN = "979-8-89176-256-5",
    abstract = "Although LLMs have shown great performance on Mathematics and Coding related reasoning tasks, the reasoning capabilities of LLMs regarding other forms of reasoning are still an open problem. Here, we examine the issue of reasoning from the perspective of claim verification. We propose a framework designed to break down any claim paired with evidence into atomic reasoning types that are necessary for verification. We use this framework to create RECV, the first claim verification benchmark, incorporating real-world claims, to assess the deductive and abductive reasoning capabilities of LLMs. The benchmark comprises of three datasets, covering reasoning problems of in creasing complexity. We evaluate three state of-the-art proprietary LLMs under multiple prompt settings. Our results show that while LLMs can address deductive reasoning prob lems, they consistently fail in cases of abductive reasoning. Moreover, we observe that enhancing LLMs with rationale generation is not always beneficial. Nonetheless, we find that generated rationales are semantically similar to those provided by humans, especially in deduc tive reasoning cases."
}
```
