---
title: Multimodal Argument Mining
date: 2026-03-02
summary: Detect arguments with speech information, such as prosody, in addition to text.
brief: This proposal adds speech information, such as prosody, to the features used to detect arguments. Speech can be represented with ad hoc features or with end-to-end architectures. Few existing corpora offer both argument annotations and the speech of the annotated text.
contacts:
- eleonora-mancini
- federico-ruggeri
tags:
- argument mining
- multimodal
- speech
aliases:
- /proposals_am/mam/
---

## Context

Argument mining is the problem of automatically detecting and extracting arguments from text. An argument usually combines a premise, a fact, that supports a subjective conclusion, a claim.
Spoken arguments also carry speech information, such as prosody, the rhythm and intonation of speech.

## Objective

Use speech information to enhance the set of features that can be used to detect arguments.

{{< pipeline caption="Illustrative flow built from the proposal's description: speech information joins the text features used to detect arguments." >}}
- title: Spoken argument
  text: Recorded speech with its transcript.
  icon: microphone-alt
- title: Features
  icon: wave-square
  highlight: true
  branches:
    - title: Text
      text: the words of the transcript
    - title: Speech
      text: prosody, with MFCC or end-to-end models
- title: Argument detection
  text: Finds premises and claims.
  icon: project-diagram
{{< /pipeline >}}

## Directions

Speech can be represented with ad hoc feature extraction methods, such as Mel-frequency cepstral coefficients (MFCC), or with end-to-end architectures.
Data is a known challenge: few existing corpora offer both argument annotation layers and the speech of the annotated text.

## References

**MAMKit: A Comprehensive Multimodal Argument Mining Toolkit.**\
Eleonora Mancini, Federico Ruggeri, Stefano Colamonaco, Andrea Zecca, Samuele Marro, and Paolo Torroni. 2024.\
In Proceedings of the 11th Workshop on Argument Mining (ArgMining 2024), pages 69–82, Bangkok, Thailand. Association for Computational Linguistics.\
[DOI](https://doi.org/10.18653/v1/2024.argmining-1.7)
| [PDF](https://aclanthology.org/2024.argmining-1.7.pdf)

**Multimodal Fallacy Classification in Political Debates**\
Eleonora Mancini, Federico Ruggeri, Paolo Torroni\
18th Conference of the European Chapter of the Association for Computational Linguistics (EACL), pp. 170–178, 2024\
[DOI](https://doi.org/10.18653/v1/2024.eacl-short.16)
| [PDF](https://aclanthology.org/2024.eacl-short.16.pdf)

**Multimodal Argument Mining: A Case Study in Political Debates**\
Eleonora Mancini, Federico Ruggeri, Andrea Galassi, and Paolo Torroni.\
In Proceedings of the 9th Workshop on Argument Mining, pages 158–170, Online and in Gyeongju, Republic of Korea. International Conference on Computational Linguistics, 2022.\
[PDF](https://aclanthology.org/2022.argmining-1.15.pdf)
| [Anthology](https://aclanthology.org/2022.argmining-1.15)
