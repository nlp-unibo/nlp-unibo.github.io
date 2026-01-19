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

<p float="left">
  <img src="content/organization/2025argfallacy/argfallacy.webp" width="33%" />
  <img src="content/organization/2025argfallacy/argfallacy.webp" width="33%" />
  <img src="content/organization/2025argfallacy/argfallacy.webp" width="33%" />
</p>

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
from mamkit.data.datasets import MMUSEDFallacy, MMUSED, UKDebates, MArg, InputMode

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

For more details, refer to the MAMKit [GitHub repository](https://github.com/nlp-unibo/mamkit) and [website](https://nlp-unibo.github.io/mamkit/) . 

## Test Set Access 🔍

The test set for **mm-argfallacy-2025** is now available! To use it, please:

1. Create a fresh environment  
2. Clone the repository and install the requirements:

```bash
git clone git@github.com:nlp-unibo/mamkit.git
cd mamkit
pip install -r requirements.txt
pip install --editable .
```

<ol start="3"> <li>Access MAMKit in your Python code:</li> </ol> 

```python
import mamkit
```

Then, retrieve the data using the following code:

### For **Fallacy Classification** (`afc`):
```python
from mamkit.data.datasets import MMUSEDFallacy, InputMode
from pathlib import Path

def loading_data_example():
    base_data_path = Path(__file__).parent.parent.resolve().joinpath('data')
    loader = MMUSEDFallacy(
        task_name='afc',
        input_mode=InputMode.TEXT_ONLY,  # or TEXT_AUDIO or AUDIO_ONLY
        base_data_path=base_data_path
    )
    split_info = loader.get_splits('mm-argfallacy-2025')
```

### For **Fallacy Detection** (`afd`):
```python
from mamkit.data.datasets import MMUSEDFallacy, InputMode
from pathlib import Path

def loading_data_example():
    base_data_path = Path(__file__).parent.parent.resolve().joinpath('data')
    loader = MMUSEDFallacy(
        task_name='afd',
        input_mode=InputMode.TEXT_ONLY,  # or TEXT_AUDIO or AUDIO_ONLY
        base_data_path=base_data_path
    )
    split_info = loader.get_splits('mm-argfallacy-2025')
```

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

Evaluation will be performed via the [CodaLab platform](https://codalab.lisn.upsaclay.fr/competitions/22739).  
On CodaLab, participants will find the leaderboard, along with the results of the provided baselines.  
Submission guidelines can be found under the *Evaluation* section of the CodaLab competition page.

🚨 **Important**: In the evaluation website, you will also find a link to a **mandatory participation survey**.  
Filling out this survey is required in order to participate in the task.  
We also provide the survey link here for convenience: [https://tinyurl.com/limesurvey-argfallacy](https://tinyurl.com/limesurvey-argfallacy)  

### Baseline Results on Test Set

#### Argumentative Fallacy Classification (AFC) – Macro F1-score

---

| Input Modality | Model                            | F1-Score |
|----------------|----------------------------------|----------|
| Text-only      | BiLSTM w/ GloVe                  | 47.21    |
| Text-only      | RoBERTa                          | 39.25    |
| Audio-only     | BiLSTM w/ MFCCs                  | 15.82    |
| Audio-only     | WavLM                            | 6.43     |
| Text + Audio   | BiLSTM (GloVe + MFCCs)           | 21.91    |
| Text + Audio   | MM-RoBERTa + WavLM               | 38.16    |

---

#### Argumentative Fallacy Detection (AFD) – Binary F1-score

---

| Input Modality | Model                            | F1-Score |
|----------------|----------------------------------|----------|
| Text-only      | BiLSTM w/ GloVe                  | 24.62    |
| Text-only      | RoBERTa                          | 27.70    |
| Audio-only     | BiLSTM w/ MFCCs                  | 0.00     |
| Audio-only     | WavLM                            | 0.00     |
| Text + Audio   | BiLSTM (GloVe + MFCCs)           | 23.37    |
| Text + Audio   | MM-RoBERTa + WavLM               | 28.48    |

---


# Submission

All evaluated submissions are required to commit to submitting a system description paper. You can choose between two options:

- **Non-Archival Paper**:  
  A 2-page paper describing your system, with unlimited pages for appendices and bibliography. These papers will *not* be published in the workshop proceedings, but your system will be mentioned in the Overview Paper of the shared task, upon acceptance.

- **Archival Paper**:  
  A 4-page paper describing your system, also with unlimited pages for appendices and bibliography. These papers *will* be published in the official ACL workshop proceedings and must be presented at the workshop (poster or oral session).  
  ⚠️ *In accordance with ACL policy, at least one team member must register for the workshop in order to present an archival paper if aaccepted to be published at the ACL proceedings.*

All papers must use the official [ACL style templates](https://github.com/acl-org/acl-style-files), available in both LaTeX and Word. We strongly recommend using the official [Overleaf template](https://www.overleaf.com/project/5f64f1fb97c4c50001b60549) for convenience.

We have sent an email to each team with all the details regarding the system description paper submission for MM-ArgFallacy2025. Please check your inbox (and spam folder just in case).

- 🗓️ **Submissions open**: May 1st, 2025 (the day after the end of the evaluation period)  
- 🗓️ **Submissions close**: May 15th, 2025 
- 📢 **Notification of acceptance**: May 20th, 2025  
- 📝 **Camera-ready deadline**: May 25th, 2025  

**Important notes**:
- All accepted **archival papers** will be presented during the workshop’s poster session and require at least one registered author.  
- **Non-archival papers** do *not* require registration and are not presented at the workshop, but their systems will be acknowledged in the Overview Paper.

We look forward to receiving your submissions!

## 🏆 Leaderboard – Shared Task Results 

### `AFC Task – Argumentative Fallacy Classification`

#### 📝 Text-only


| Rank | Team                  | F1-Macro |
|------|------------------------|----------|
| 1    | Team NUST              | 0.4856   |
| 2    | Baseline BiLSTM        | 0.4721   |
| 3    | alessiopittiglio       | 0.4444   |
| 4    | Baseline RoBERTa       | 0.3925   |
| 5    | Team CASS              | 0.1432   |

#### 🔊 Audio-only


| Rank | Team                      | F1-Macro |
|------|---------------------------|----------|
| 1    | alessiopittiglio           | 0.3559   |
| 2    | Team NUST                  | 0.1588   |
| 3    | Baseline BiLSTM + MFCCs    | 0.1582   |
| 4    | Team CASS                  | 0.0864   |
| 5    | Baseline WavLM             | 0.0643   |

#### 🔁 Text-Audio


| Rank | Team                              | F1-Macro |
|------|-----------------------------------|----------|
| 1    | Team NUST                          | 0.4611   |
| 2    | alessiopittiglio                   | 0.4403   |
| 3    | Baseline RoBERTa + WavLM           | 0.3816   |
| 4    | Baseline BiLSTM + MFCCs            | 0.2191   |
| 5    | Team CASS                          | 0.1432   |

---

### `AFD Task – Argumentative Fallacy Detection`

#### 📝 Text-only


| Rank | Team                        | F1-Macro |
|------|-----------------------------|----------|
| 1    | Baseline RoBERTa            | 0.2770   |
| 2    | Ambali_Yashovardhan         | 0.2534   |
| 3    | Baseline BiLSTM             | 0.2462   |
| 4    | Team EvaAdriana             | 0.2195   |

#### 🔊 Audio-only


| Rank | Team                        | F1-Macro |
|------|-----------------------------|----------|
| 1    | Ambali_Yashovardhan         | 0.2095   |
| 2    | Team EvaAdriana             | 0.1690   |
| 3    | Baseline BiLSTM + MFCCs     | 0.0000   |
| 4    | Baseline WavLM              | 0.0000   |

#### 🔁 Text-Audio


| Rank | Team                              | F1-Macro |
|------|-----------------------------------|----------|
| 1    | Baseline RoBERTa + WavLM          | 0.2848   |
| 2    | Baseline BiLSTM + MFCCs           | 0.2337   |
| 3    | Ambali_Yashovardhan               | 0.2244   |
| 4    | Team EvaAdriana                   | 0.1931   |


# Key Dates (Anywhere on Earth)

- **Release of Training Data**: February 25th
- **Release of Test Set**: ~~March 24th~~ → April 7th
- **Evaluation Start**: ~~April 14th~~ → April 21st
- **Evaluation End**: ~~April 25th~~ → April 30th
- **Paper Submissions Open**: May 1st
- **Paper Submission Close**: May 15th
- **Notification of acceptance**: May 20th
- **Camera-ready Due**: May 25th  
- **Workshop**: July 31st





# Task Organizers 

<div class="row row-cols-2 projects pt-3 pb-3">
  {% include static/people_horizontal.html name="Eleonora Mancini" affiliation="Language Technologies Lab, University of Bologna, Italy" url="https://helemanc.github.io/" img="/assets/img/people/eleonora_mancini.jpeg" %}
  {% include static/people_horizontal.html name="Federico Ruggeri" affiliation="Language Technologies Lab, University of Bologna, Italy" url="https://www.unibo.it/sitoweb/federico.ruggeri6" img="/assets/img/people/fede.png" %}
  {% include static/people_horizontal.html name="Paolo Torroni" affiliation="Language Technologies Lab, University of Bologna, Italy" url="https://www.unibo.it/sitoweb/p.torroni/en" img="/assets/img/people/paolo.png" %}
  {% include static/people_horizontal.html name="Serena Villata" affiliation="Inria-I3S WIMMICS Laboratoire I3S, CNRS, Sophia Antipolis, France" url="https://webusers.i3s.unice.fr/~villata/Home.html" img="assets/img/people/serena_villata.jpg" %}
</div>



# Contacts
**[Join the MM-ArgFallacy2025 Slack Channel!](https://join.slack.com/t/mm-argfallacy2025/shared_invite/zt-2yjct5udc-vbuGSsSelR5FMiopSne~wQ)**

# Cite

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

# Credits

<div style="display:flex; justify-content: space-around;">
<div class="content-wrap about_content">
    <p>
        This shared task is partially supported by the project European Commission's NextGeneration EU programme, PNRR -- M4C2 -- Investimento 1.3, Partenariato Esteso, PE00000013 - FAIR - Future Artificial Intelligence Research'' -- Spoke 8 Pervasive AI’’.
    </p>
</div>

<div class="card-img col-sm-4">
  <img src="content/organization/2025argfallacy/eulogo.svg" class="img-fluid rounded z-depth-1" width="650px" height="90px" />
</div>
</div>

