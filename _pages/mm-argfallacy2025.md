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


We use **MM-USED-fallacy** and release a version of the dataset specifically designed for argumentative fallacy detection.   This dataset includes 1,278 sentences from [Haddadan et al.'s (2019)](https://aclanthology.org/P19-1463.pdf) dataset on US presidential elections.  Each sentence is labeled with one of six argumentative fallacy categories, as introduced by [Goffredo et al. (2022)](https://www.ijcai.org/proceedings/2022/575).  

Inspired by observations from [Goffredo et al. (2022)](https://www.ijcai.org/proceedings/2022/575) on the benefits of leveraging multiple argument mining tasks for fallacy detection and classification, we also provide additional datasets to encourage multi-task learning. A summary is provided in the table below:  

---

| **Dataset**       | **Description**                                                                                                                                                                          | **Size**       |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|
|**MM-USED-fallacy** | A multimodal extension of USElecDeb60to20 dataset, covering US presidential debates (1960-2020). Inlcludes labels for argumentative fallacy detection and argumentative fallacy classification. | 1,278 samples (updated version)| 
| **MM-USED**        | A multimodal extension of the USElecDeb60to16 dataset, covering US presidential debates (1960–2016). Includes labels for argumentative sentence detection and component classification.   | 23,505 sentences (updated version)|
| **UKDebates**      | 386 sentences and audio samples from the 2015 UK Prime Ministerial elections. Sentences are labeled for argumentative sentence detection: containing or not containing a claim.           | 386 sentences  |
| **M-Arg**          | A multimodal dataset for argumentative relation classification from the 2020 US Presidential elections. Sentences are labeled as attacking, supporting, or unrelated to another sentence. | 4,104 pairs    |


---

All datasets will be available through [MAMKit](https://nlp-unibo.github.io/mamkit/).  

Since many multimodal datasets cannot release audio samples due to copyright restrictions, MAMKit provides an interface to dynamically build datasets and promote reproducible research.  

Datasets are formatted as `torch.Dataset` objects, containing input values (text, audio, or both) and corresponding task-specific labels. More details about data formats and dataset building are available in MAMKit's documentation.  ## Retrieving the Data through MAMKit

To retrieve the datasets through MAMKit, you can use the following code interface:

```python
from mamkit.data.datasets import MMUSEDFallacy, USEDFallacy, UKDebates, MArg
import logging
from pathlib import Path

def loading_data_example():
    base_data_path = Path(__file__).parent.parent.resolve().joinpath('data')

    # MM-USED-fallacy dataset
    mm_used_fallacy_loader = MMUSEDFallacy(
        task_name='afc', # Choose between 'afc' or 'afd'               
        input_mode=InputMode.TEXT_AUDIO, # Choose between TEXT_ONLY, AUDIO_ONLY, or TEXT_AUDIO
        base_data_path=base_data_path
    )

    # MM-USED dataset
    mm_used_loader = MMUSED(
        task_name='asd',#Choose between 'asd' or 'acc'  
        input_mode=InputMode.TEXT_AUDIO, # Choose between TEXT_ONLY, AUDIO_ONLY, or TEXT_AUDIO
        base_data_path=base_data_path
    )

    # UKDebates dataset
    uk_debates_loader = UKDebates(
        task_name='asd', 
        input_mode=InputMode.TEXT_AUDIO, # Choose between TEXT_ONLY, AUDIO_ONLY, or TEXT_AUDIO
        base_data_path=base_data_path
    )

    # M-Arg dataset
    m_arg_loader = MArg(
        task_name='arc',
        input_mode=InputMode.TEXT_AUDIO, # Choose between TEXT_ONLY, AUDIO_ONLY, or TEXT_AUDIO
        base_data_path=base_data_path
    )
```

Each loader is initialized with the appropriate task name (`afc` for argumentative fallacy classification, `asd` for argumentative sentence detection, and 'arc' for argumentative relation classification), input mode (InputMode.TEXT_ONLY, InputMode.AUDIO_ONLY, or InputMode.TEXT_AUDIO), and the base data path.

Ensure that you have MAMKit installed and properly configured in your environment to use these loaders.

For more details, refer to the MAMKit [GitHub repository](https://nlp-unibo.github.io/mamkit/) and [website](https://nlp-unibo.github.io/mamkit/) . 


### References

- **MM-USED-fallacy**: [Mancini et al. (2024)](https://aclanthology.org/2024.eacl-short.16.pdf). The version provided through MAMKit includes updated samples, with refinements in the alignment process. This results in a different number of samples compared to the original dataset.
- **MM-USED**: [Mancini et al. (2022)](https://aclanthology.org/2022.argmining-1.15.pdf). The version provided through MAMKit includes updated samples, with refinements in the alignment process. This results in a different number of samples compared to the original dataset.
- **UK-Debates**: [Lippi and Torroni (2016)](https://ojs.aaai.org/index.php/AAAI/article/view/10384).
- **M-Arg**: [Mestre et al. (2021)](https://aclanthology.org/2021.argmining-1.8.pdf).

**Note**: By "updated version," we mean that the datasets have undergone a refinement in the alignment process, which has resulted in adjustments to the number of samples included compared to the original versions published in the referenced papers.

# Evaluation 
For argumentative fallacy detection, we will compute the binary F1-score on predicted sentence-level labels. 
For argumentative fallacy classification, we will compute the macro F1-score on predicted sentence-level labels.
Metrics will be computed on the hidden test set to determine the best system for each sub-task and input mode.

# Key Dates (Anywhere on Earth)

- **Release of Training Data**: February 25th
- **Release of Test Set**: March 24th
- **Evaluation Start**: April 14th
- **Evaluation End**: April 25th
- **Paper Submission Due**: May 15th
- **Workshop**: July 31st

# Submission 
Will be updated soon. 



# Task Organizers 

<div class="row row-cols-2 projects pt-3 pb-3">
  {% include people_horizontal.html name="Eleonora Mancini" affiliation="Language Technologies Lab, University of Bologna, Italy" url="https://helemanc.github.io/" img="/assets/img/people/eleonora_mancini.jpeg" %}
  {% include people_horizontal.html name="Federico Ruggeri" affiliation="Language Technologies Lab, University of Bologna, Italy" url="https://www.unibo.it/sitoweb/federico.ruggeri6" img="/assets/img/people/fede.png" %}
  {% include people_horizontal.html name="Paolo Torroni" affiliation="Language Technologies Lab, University of Bologna, Italy" url="https://www.unibo.it/sitoweb/p.torroni/en" img="/assets/img/people/paolo.png" %}
  {% include people_horizontal.html name="Serena Villata" affiliation="Inria-I3S WIMMICS Laboratoire I3S, CNRS, Sophia Antipolis, France" url="https://webusers.i3s.unice.fr/~villata/Home.html" img="assets/img/people/serena_villata.jpg" %}
</div>



# Contacts
**[Join the MM-ArgFallacy2025 Slack Channel!](https://join.slack.com/t/mm-argfallacy2025/shared_invite/zt-2yjct5udc-vbuGSsSelR5FMiopSne~wQ)**