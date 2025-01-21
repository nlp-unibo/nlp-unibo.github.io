---
layout: page
title: MM-ArgFallacy2025 
permalink: /mm-argfallacy/2025/
description: 
nav: false
#nav_order: 8
related_publications: false
---
<!-- pages/parkinsons-speech-xai.md -->


Multimodal Argumentative Fallacy Detection and Classification on Political Debates Shared Task.

Co-located with The [12th Workshop on Argument Mining](https://argmining-org.github.io/2025/) in Vienna, Austria.


# Overview
This shared task focuses on detecting and classifying fallacies in **political debates** by integrating text and audio data. Participants will tackle two sub-tasks:  
- **Argumentative Fallacy Detection**  
- **Argumentative Fallacy Classification**  

We offer three input settings:  
- **Text-only:** Analyze textual arguments.  
- **Audio-only:** Explore paralinguistic features.  
- **Text + Audio:** Combine both for a multimodal perspective.  

Join us to advance multimodal argument mining and uncover new insights into human reasoning! 💬


# Tasks 

**Task A**

- **Input**: a sentence, in the form of text or audio or both, extracted from a political debate. 
- **Task**: to determine whether the input contains an argumentative fallacy.

**Task B**
- **Input**: a sentence, in the form of text or audio or both, extracted from a political debate, containing a fallacy. 
- **Task**: to determine the type of fallacy contained in the input, according to the classification introduced by [Goffredo et al. (2022)](https://www.ijcai.org/proceedings/2022/575). We only refer to macro categories.

-----------------------------------

For each sub-task, participants can leverage the debate context of a given input: all its previous sentences and corresponding aligned audio samples.  For instance, consider the **text-only** input mode.  Given a sentence from a political debate at index *i*, participants can use sentences with indexes from *0* to *i - 1*, where *0* denotes the first sentence in the debate.  

------------------------------------


# Data 


We use **MM-USED-fallacy** and release a version of the dataset specifically designed for argumentative fallacy detection.   This dataset includes 1,891 sentences from [Haddadan et al.'s (2019)](https://aclanthology.org/P19-1463.pdf) dataset on US presidential elections.  Each sentence is labeled with one of six argumentative fallacy categories, as introduced by [Goffredo et al. (2022)](https://www.ijcai.org/proceedings/2022/575).  

Inspired by observations from [Goffredo et al. (2022)](https://www.ijcai.org/proceedings/2022/575) on the benefits of leveraging multiple argument mining tasks for fallacy detection and classification, we also provide additional datasets to encourage multi-task learning. A summary is provided in the table below:  

For argumentative fallacy detection, we will compute the binary F1-score on predicted sentence-level labels. 
For argumentative fallacy classification, we will compute the macro F1-score on predicted sentence-level labels.
Metrics will be computed on the hidden test set to determine the best system for each sub-task and input mode.

---

| **Dataset**       | **Description**                                                                                                                                                                          | **Size**       |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|
| **UKDebates**      | 386 sentences and audio samples from the 2015 UK Prime Ministerial elections. Sentences are labeled for argumentative sentence detection: containing or not containing a claim.           | 386 sentences  |
| **M-Arg**          | A multimodal dataset for argumentative relation classification from the 2020 US Presidential elections. Sentences are labeled as attacking, supporting, or unrelated to another sentence. | 4,104 pairs    |
| **MM-USED**        | A multimodal extension of the USElecDeb60to16 dataset, covering US presidential debates (1960–2016). Includes labels for argumentative sentence detection and component classification.   | 26,781 sentences |

---

All datasets will be available through [MAMKit](https://nlp-unibo.github.io/mamkit/).  

Since many multimodal datasets cannot release audio samples due to copyright restrictions, MAMKit provides an interface to dynamically build datasets and promote reproducible research.  

Datasets are formatted as `torch.Dataset` objects, containing input values (text, audio, or both) and corresponding task-specific labels. More details about data formats and dataset building are available in MAMKit's documentation.  

# Evaluation 
For argumentative fallacy detection, we will compute the binary F1-score on predicted sentence-level labels. 
For argumentative fallacy classification, we will compute the macro F1-score on predicted sentence-level labels.
Metrics will be computed on the hidden test set to determine the best system for each sub-task and input mode.

# Key Dates (Anywhere on Earth)
Will be updated soon. 

# Submission 
We be updated soon. 



# Task Organizers 

<div class="row row-cols-2 projects pt-3 pb-3">
  {% include people_horizontal.html name="Eleonora Mancini" affiliation="Language Technologies Lab, University of Bologna, Italy" url="https://helemanc.github.io/" img="/assets/img/people/eleonora_mancini.jpeg" %}
  {% include people_horizontal.html name="Federico Ruggeri" affiliation="Language Technologies Lab, University of Bologna, Italy" url="https://www.unibo.it/sitoweb/federico.ruggeri6" img="/assets/img/people/fede.png" %}
  {% include people_horizontal.html name="Paolo Torroni" affiliation="Language Technologies Lab, University of Bologna, Italy" url="https://www.unibo.it/sitoweb/p.torroni/en" img="/assets/img/people/paolo.png" %}
  {% include people_horizontal.html name="Serena Villata" affiliation="Inria-I3S WIMMICS Laboratoire I3S, CNRS, Sophia Antipolis, France" url="https://webusers.i3s.unice.fr/~villata/Home.html" img="assets/img/people/serena_villata.jpg" %}
</div>



# Contacts
**[Join the MM-ArgFallacy2025 Slack Channel!](https://join.slack.com/t/mm-argfallacy2025/shared_invite/zt-2yjct5udc-vbuGSsSelR5FMiopSne~wQ)**