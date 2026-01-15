---
title: "Overview of MM-ArgFallacy2025 on Multimodal Argumentative Fallacy Detection and Classification in Political Debates" 
date: 2025-07-01
tags: ["natural language processing", "shared task", "arg-fallacy", "argument mining", "fallacy classification", "fallacy detection", "political debates", "multimodal"]
author: ["Eleonora Mancini", "Federico Ruggeri", "Serena Villata", "Paolo Torroni"]
description: "We present an overview of the MM-ArgFallacy2025 shared task on Multimodal Argumentative Fallacy Detection and Classification in Political Debates, co-located with the 12th Workshop on Argument Mining at ACL 2025." 
summary: "We present an overview of the MM-ArgFallacy2025 shared task on Multimodal Argumentative Fallacy Detection and Classification in Political Debates, co-located with the 12th Workshop on Argument Mining at ACL 2025." 
cover:
    image: "paper.png"
    alt: "Overview of MM-ArgFallacy2025 on Multimodal Argumentative Fallacy Detection and Classification in Political Debates"
    relative: true
editPost:
    URL: "https://github.com/federicoruggeri/hugo-website"
    Text: "CLEF"

---

---

##### Resources

+ [CheckThat! 2025](https://nlp-unibo.github.io/mm-argfallacy/2025/)
+ [Paper](paper.pdf)

---

##### Abstract

We present an overview of the MM-ArgFallacy2025 shared task on Multimodal Argumentative Fallacy Detection and Classification in Political Debates, co-located with the 12th Workshop on Argument Mining at ACL 2025. The task focuses on identifying and classifying argumentative fallacies across three input modes: text-only, audio-only, and multimodal (text+audio), offering both binary detection (AFD) and multi-class classification (AFC) subtasks. The dataset comprises 18,925 instances for AFD and 3,388 instances for AFC, from the MM-USED-Fallacy corpus on U.S. presidential debates, annotated for six fallacy types: Ad Hominem, Appeal to Authority, Appeal to Emotion, False Cause, Slippery Slope, and Slogan. A total of 5 teams participated: 3 on classification and 2 on detection. Participants employed transformer-based models, particularly RoBERTa variants, with strategies including prompt-guided data augmentation, context integration, specialised loss functions, and various fusion techniques. Audio processing ranged from MFCC features to state-of-the-art speech models. Results demonstrated textual modality dominance, with best text-only performance reaching 0.4856 F1-score for classification and 0.34 for detection. Audio-only approaches underperformed relative to text but showed improvements over previous work, while multimodal fusion showed limited improvements. This task establishes important baselines for multimodal fallacy analysis in political discourse, contributing to computational argumentation and misinformation detection capabilities.

---

##### Citation

Eleonora Mancini, Federico Ruggeri, Serena Villata, and Paolo Torroni. 2025. Overview of MM-ArgFallacy2025 on Multimodal Argumentative Fallacy Detection and Classification in Political Debates. In Proceedings of the 12th Argument mining Workshop, pages 358–368, Vienna, Austria. Association for Computational Linguistics.


```latex
@inproceedings{mancini-etal-2025-overview,
    title = "Overview of {MM}-{A}rg{F}allacy2025 on Multimodal Argumentative Fallacy Detection and Classification in Political Debates",
    author = "Mancini, Eleonora  and
      Ruggeri, Federico  and
      Villata, Serena  and
      Torroni, Paolo",
    editor = "Chistova, Elena  and
      Cimiano, Philipp  and
      Haddadan, Shohreh  and
      Lapesa, Gabriella  and
      Ruiz-Dolz, Ramon",
    booktitle = "Proceedings of the 12th Argument mining Workshop",
    month = jul,
    year = "2025",
    address = "Vienna, Austria",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.argmining-1.35/",
    doi = "10.18653/v1/2025.argmining-1.35",
    pages = "358--368",
    ISBN = "979-8-89176-258-9",
    abstract = "We present an overview of the MM-ArgFallacy2025 shared task on Multimodal Argumentative Fallacy Detection and Classification in Political Debates, co-located with the 12th Workshop on Argument Mining at ACL 2025. The task focuses on identifying and classifying argumentative fallacies across three input modes: text-only, audio-only, and multimodal (text+audio), offering both binary detection (AFD) and multi-class classification (AFC) subtasks. The dataset comprises 18,925 instances for AFD and 3,388 instances for AFC, from the MM-USED-Fallacy corpus on U.S. presidential debates, annotated for six fallacy types: Ad Hominem, Appeal to Authority, Appeal to Emotion, False Cause, Slippery Slope, and Slogan. A total of 5 teams participated: 3 on classification and 2 on detection. Participants employed transformer-based models, particularly RoBERTa variants, with strategies including prompt-guided data augmentation, context integration, specialised loss functions, and various fusion techniques. Audio processing ranged from MFCC features to state-of-the-art speech models. Results demonstrated textual modality dominance, with best text-only performance reaching 0.4856 F1-score for classification and 0.34 for detection. Audio-only approaches underperformed relative to text but showed improvements over previous work, while multimodal fusion showed limited improvements. This task establishes important baselines for multimodal fallacy analysis in political discourse, contributing to computational argumentation and misinformation detection capabilities."
}
```
