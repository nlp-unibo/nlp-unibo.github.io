---
title: Speech Processing
date: 2026-02-27

tags:
  - speech
  - research

summary: The development of automatic tools for handling and digesting speech data, often in conjunction with other modalities like text.

# Font Awesome icon shown on the homepage research card
icon: microphone-alt
weight: 3

# Homepage research card: tagline and cover pattern (dots, graph, tokens, or wave).
tagline: Combining audio and text, from spoken arguments to clinical speech.
cover_pattern: wave

# Definition: a short answer to "What is speech processing?" under the title. Markdown, one idea per sentence.
definition: |
  Speech processing is the automatic analysis of spoken language from its audio signal, often together with a transcript of the words.
  The voice carries information that the words alone do not, such as emotion, and this information can help tasks like argument mining ([Lippi and Torroni, 2016](/publication/lippi-torroni-2016/)).
  We study what the audio adds to the text, how to explain the decisions of audio models, and how speech data are collected and documented.

# Core concepts: one block per concept, with a short text and a small schema (an SVG file in this folder, drawn with the `lt-s-*` classes).
overview:
  - icon: wave-square
    title: Audio features
    text: "A model does not use raw sound directly. It first turns the audio signal into features, such as Mel-frequency cepstral coefficients (MFCCs), which describe the spectrum of the signal. Other models use embeddings learned by a neural network such as Wav2vec."
    schema: schema-features.svg
  - icon: closed-captioning
    title: Transcripts
    text: "A speech recognizer turns the audio into text, so that text models can read it. Its errors carry over to later tasks: in one debate, claim detection on recognized text was no better than chance for one of the speakers."
    schema: schema-transcripts.svg
  - icon: layer-group
    title: Modalities
    text: "A modality is a type of input, such as text or audio. A model can read the text only, listen to the audio only, or combine both, and comparing the three settings shows what each modality contributes."
    schema: schema-modalities.svg
  - icon: search
    title: Explanations
    text: "Neural audio models are typically black boxes. Post-hoc explanation methods show which parts of the input a model relied on, for example as maps that a person can listen to."
    schema: schema-explanations.svg

# What is speech processing?: background for the views below, shown as their section introduction. Markdown, one idea per sentence.
views_title: What does the audio add?
concepts: |
  Many tasks on speech start from a transcript, a written version of what was said.
  A transcript keeps the words but loses how they were said, such as tone, rhythm, and emphasis.
  These paralinguistic cues can relate to the meaning of an argument: for example, a prosody that stresses anger can signal an appeal to emotion ([Mancini et al., 2024](/publication/mancini-etal-2024-multimodal/)).
  The examples below compare models that read the transcript alone with models that also use the audio.

# Views: interactive examples, grouped by research area.
# `type: voices` draws illustrative readings of short sentences as cue strips: each word has a duration `dur` and an optional
# `pause` after it (seconds), a `pitch` pair (start and end, 0 to 1), and a `loud` value (0 to 1). Each reading has a `gold`
# answer (`gold_label` names the row, Annotators by default), and each of `models` lists one answer per reading, with what
# the model `hears`. Captions are Markdown: link each cited paper by its name.
views:
  - key: claims
    type: voices
    group: Argumentation
    label: Claims in debates
    description: "Claim detection decides whether a sentence states a claim, an opinion or thesis that the speaker asserts. A speech recognizer writes the words without punctuation, so a statement and a question with the same words give the same transcript. The pitch of the voice tells them apart."
    caption: "Illustrative example: the sentences, cue values, and answers are constructed. No recording or model output is shown. The task follows the claim detection setting of [Lippi and Torroni (2016)](/publication/lippi-torroni-2016/), who combine text and audio features of a televised political debate."
    question: Is the sentence a claim?
    readings:
      - label: Said as a statement
        summary: "Stress on cut, and the pitch falls at the end."
        gold: "Yes"
        words:
          - {w: we, dur: 0.2, pitch: [0.45, 0.5], loud: 0.5}
          - {w: will, dur: 0.25, pitch: [0.55, 0.55], loud: 0.6}
          - {w: cut, dur: 0.35, pitch: [0.85, 0.75], loud: 0.95}
          - {w: taxes, dur: 0.5, pitch: [0.5, 0.1], loud: 0.6}
      - label: Same words, asked as a question
        summary: "No stress, and the pitch rises at the end."
        gold: "No"
        words:
          - {w: we, dur: 0.2, pitch: [0.4, 0.4], loud: 0.45}
          - {w: will, dur: 0.25, pitch: [0.4, 0.42], loud: 0.45}
          - {w: cut, dur: 0.3, pitch: [0.45, 0.5], loud: 0.5}
          - {w: taxes, dur: 0.6, pitch: [0.55, 0.95], loud: 0.6}
      - label: Other words, said firmly
        summary: "Stress on evening, a short pause, and the pitch falls at the end."
        gold: "No"
        words:
          - {w: good, dur: 0.25, pitch: [0.6, 0.55], loud: 0.7}
          - {w: evening, dur: 0.45, pitch: [0.8, 0.6], loud: 0.9, pause: 0.3}
          - {w: all, dur: 0.5, pitch: [0.5, 0.1], loud: 0.65}
    models:
      - {label: Text only, hears: "The words, without punctuation", answers: ["Yes", "Yes", "No"]}
      - {label: Audio only, hears: "Pitch, loudness, pauses, and rate", answers: ["Yes", "No", "Yes"]}
      - {label: Text and audio, hears: "Both", answers: ["Yes", "No", "No"]}
  - key: fallacies
    type: voices
    group: Argumentation
    label: Fallacies in debates
    description: "A fallacy is a deceptive, misleading, or generally invalid argument. An appeal to emotion seeks agreement by stirring feelings instead of giving reasons. A transcript keeps the words but loses the anger in the voice."
    caption: "Illustrative example: the sentences, cue values, and answers are constructed. No recording or model output is shown. The task follows the fallacy classification setting of [Mancini et al. (2024)](/publication/mancini-etal-2024-multimodal/), who pair sentences of US presidential debates with their audio."
    question: Is the sentence an appeal to emotion?
    readings:
      - label: Said calmly
        summary: "Even loudness, and the pitch stays level."
        gold: "No"
        words:
          - {w: this, dur: 0.2, pitch: [0.45, 0.45], loud: 0.5}
          - {w: plan, dur: 0.3, pitch: [0.5, 0.45], loud: 0.5}
          - {w: hurts, dur: 0.35, pitch: [0.5, 0.45], loud: 0.55}
          - {w: families, dur: 0.6, pitch: [0.45, 0.3], loud: 0.5}
      - label: Same words, said with anger
        summary: "Loud throughout, a pitch peak on hurts, and a pause for effect."
        gold: "Yes"
        words:
          - {w: this, dur: 0.2, pitch: [0.6, 0.65], loud: 0.75}
          - {w: plan, dur: 0.3, pitch: [0.7, 0.65], loud: 0.8}
          - {w: hurts, dur: 0.45, pitch: [0.95, 0.8], loud: 1.0, pause: 0.4}
          - {w: families, dur: 0.7, pitch: [0.8, 0.4], loud: 0.9}
      - label: Other words, said with anger
        summary: "Loud throughout, and a pitch peak on vote."
        gold: "No"
        words:
          - {w: we, dur: 0.2, pitch: [0.6, 0.65], loud: 0.75}
          - {w: vote, dur: 0.4, pitch: [0.95, 0.8], loud: 1.0}
          - {w: on, dur: 0.15, pitch: [0.7, 0.7], loud: 0.8}
          - {w: tuesday, dur: 0.6, pitch: [0.8, 0.4], loud: 0.9}
    models:
      - {label: Text only, hears: "The words, without punctuation", answers: ["No", "No", "No"]}
      - {label: Audio only, hears: "Pitch, loudness, pauses, and rate", answers: ["No", "Yes", "Yes"]}
      - {label: Text and audio, hears: "Both", answers: ["No", "Yes", "No"]}
  - key: depression
    type: voices
    group: Mental health
    label: Depression in speech
    description: "Depression detection predicts whether a person has depression from signals such as their speech. A transcript keeps what the person says, but not how flat or slow the voice is. The voice and the words can each carry signs that the other misses."
    caption: "Illustrative example: the sentences, cue values, and labels are constructed. The answers are not a diagnosis. No recording or model output is shown. The task follows the depression detection setting of [Nurfidausi et al. (2025)](/publication/nurfidausi-2025-trideptrimodalcomparativestudy/), who compare speech, text, and EEG."
    question: Does the speaker show signs of depression?
    gold_label: Clinical label
    readings:
      - label: Said with varied pitch
        summary: "Varied pitch and a regular pace."
        gold: "No"
        words:
          - {w: i, dur: 0.15, pitch: [0.5, 0.6], loud: 0.6}
          - {w: slept, dur: 0.35, pitch: [0.7, 0.55], loud: 0.7}
          - {w: well, dur: 0.3, pitch: [0.75, 0.5], loud: 0.7}
          - {w: today, dur: 0.5, pitch: [0.6, 0.3], loud: 0.6}
      - label: Same words, said flat and slow
        summary: "Flat pitch, low loudness, a slow pace, and a long pause."
        gold: "Yes"
        words:
          - {w: i, dur: 0.25, pitch: [0.3, 0.3], loud: 0.35}
          - {w: slept, dur: 0.5, pitch: [0.3, 0.28], loud: 0.35}
          - {w: well, dur: 0.45, pitch: [0.28, 0.28], loud: 0.3, pause: 0.8}
          - {w: today, dur: 0.7, pitch: [0.28, 0.25], loud: 0.3}
      - label: Other words, said with varied pitch
        summary: "Varied pitch and a regular pace."
        gold: "Yes"
        words:
          - {w: nothing, dur: 0.3, pitch: [0.7, 0.55], loud: 0.7}
          - {w: matters, dur: 0.3, pitch: [0.75, 0.5], loud: 0.7}
          - {w: anymore, dur: 0.45, pitch: [0.6, 0.3], loud: 0.6}
    models:
      - {label: Text only, hears: "The words, without punctuation", answers: ["No", "No", "Yes"]}
      - {label: Audio only, hears: "Pitch, loudness, pauses, and rate", answers: ["No", "Yes", "No"]}
      - {label: Text and audio, hears: "Both", answers: ["No", "Yes", "Yes"]}

# Research areas: one block per macro topic. Selecting a block enlarges it and opens its tasks beside it.
# Each task states its input and the expected output.
fields:
- key: arguments
  title: Arguments in speech
  icon: comments
  question: "Can a model find the arguments in what people say aloud?"
  summary: "Political debates are spoken, so their arguments come with the voice of the speaker. Systems detect and classify argumentative sentences from the transcript, the audio, or both."
  tasks:
  - name: Claim detection
    text: "Given a sentence, the task is to say whether it contains a claim. A claim is the conclusion of an argument, a statement that asserts an opinion or a thesis."
  - name: Argumentative sentence detection
    text: "Given a sentence, the task is to say whether it contains an argument."
  - name: Argumentative component classification
    text: "Given an argumentative sentence, the task is to say whether it contains a claim or a premise, a reason offered for a claim."
  - name: Argumentative relation classification
    text: "Given a pair of sentences, the task is to say whether the first supports the second, attacks it, or neither."
  - name: Fallacy detection and classification
    text: "Given a sentence of a debate, the task is to say whether it contains a fallacy. A second task assigns the category of the fallacy, such as ad hominem or appeal to emotion."
- key: modalities
  title: Text and audio together
  icon: layer-group
  question: "What does the audio add to the words?"
  summary: "Multimodal models combine an encoding of the text with an encoding of the audio. Comparing them with text-only and audio-only models shows what each modality contributes."
  tasks:
  - name: Audio encoding
    text: "Given an audio segment, the task is to represent it for a classifier, either with spectral features such as MFCCs or with embeddings from a pretrained network such as Wav2vec."
  - name: Modality fusion
    text: "Given an encoding of the text and an encoding of the audio of the same sentence, the task is to combine them into one input for a classifier."
  - name: Benchmarking
    text: "Given several datasets and models, the task is to compare them with the same data loading and the same evaluation, so that results are comparable."
- key: health
  title: Speech and health
  icon: heartbeat
  question: "Can speech help detect mental health and neurological disorders, and can we trust the data?"
  summary: "Conditions such as depression and Parkinson's disease can change how a person speaks. Models that detect them depend on datasets whose collection must protect the people who speak."
  tasks:
  - name: Depression detection
    text: "Given recordings of a person, possibly with other signals such as EEG, the task is to predict whether the person has major depressive disorder."
  - name: Parkinson's disease detection
    text: "Given a speech recording, the task is to distinguish people with Parkinson's disease from healthy controls."
  - name: Dataset documentation
    text: "Given a speech dataset for mental health, the task is to check whether its paper reports informed consent, privacy, accountability, and the other items of a checklist."
- key: explanations
  title: Explaining audio models
  icon: search
  question: "Which parts of a recording does a model rely on?"
  summary: "Audio classifiers rarely show why they decide. Explanation methods mark the parts of the input that a decision depends on, and their quality must be measured."
  tasks:
  - name: Post-hoc explanation
    text: "Given a trained audio classifier and an input, the task is to produce an explanation of the decision. The explanation can be a saliency map over the input or an audio signal that a person can listen to."
  - name: Faithfulness evaluation
    text: "Given an explanation, the task is to measure whether it reflects what the model actually used for its decision."
- key: applications
  title: Speech in applications
  icon: bus
  question: "Where can speech models help outside the lab?"
  summary: "Speech models also serve safety on public transport and music retrieval. These settings bring noise, overlapping voices, and limited hardware."
  tasks:
  - name: Speech emotion recognition
    text: "Given a speech recording, the task is to recognize the emotion of the speaker, such as anger or calm, as one of a set of discrete classes."
  - name: Disruptive situation detection
    text: "Given a recording from a public space, the task is to detect disruptive situations, emotionally charged events such as people fighting or screaming."
  - name: Lyrics matching
    text: "Given the audio of songs, the task is to find songs with similar lyrical content, working from the audio rather than from written lyrics."

# Our focus: the lab's topics, each with a summary, a definition paragraph, and items that are done, now, or next.
# Done items cite lab publications by their folder name in content/publication.
focus:
- key: arguments
  title: Arguments in speech
  icon: comments
  summary: "We study whether the voice of a speaker helps a machine find and classify arguments. Our data come from televised political debates."
  description: "Argument mining extracts arguments and their relations from natural language. In a political debate the arguments are spoken, so a model can use the transcript, the audio, or both. A claim is the conclusion of an argument, and a fallacy is a deceptive, misleading, or generally invalid argument. We ask whether audio features improve the detection of claims and the classification of fallacies."
  items:
  - status: done
    text: Claim detection from the audio of a political debate.
    detail: "We build a corpus from the UK leaders' debate of 2 April 2015, with 386 audio samples of three candidates labelled as containing a claim or not. Adding audio features (MFCCs) to text features improves the F1 score by around 5% for every candidate, except one when the text comes from a speech recognizer."
    cite:
    - lippi-torroni-2016
  - status: done
    text: Fallacy classification with text and audio.
    detail: "We release MM-USED-fallacy, the first corpus for multimodal fallacy classification, with 1891 text-audio pairs from 28 US presidential debates. Adding the audio to a text model improves the macro F1 score by up to 8 points for BERT and RoBERTa, while audio-only models are weak."
    cite:
    - mancini-etal-2024-multimodal
  - status: done
    text: A shared task on multimodal fallacy detection.
    detail: "MM-ArgFallacy2025 asks systems to detect and classify fallacies in sentences of US presidential debates, from the text, the audio, or both. A new test set comes from two debates of 2024. Five teams took part, and text-only systems performed best."
    cite:
    - mancini-etal-2025-overview
  - status: next
    text: Annotating fallacies while listening to the audio.
    detail: "Existing annotations were made on transcripts and only later extended to the audio. We plan annotations made with access to the audio, so that labels can reflect how an argument is spoken."
- key: modalities
  title: Text and audio together
  icon: layer-group
  summary: "We compare models that read, listen, or do both, and we release tools that make these comparisons fair."
  description: "A multimodal model combines several modalities, for example by joining an encoding of the text and an encoding of the audio before a classifier. Comparing text-only, audio-only, and text-audio settings shows what each modality adds. We ask how to encode the audio and how to fuse it with the text."
  items:
  - status: done
    text: Multimodal argument mining in political debates.
    detail: "We release MM-USElecDeb60to16, in which the transcripts of US presidential debates are aligned to their audio sentence by sentence. Embedding-based audio encodings such as Wav2vec generally beat spectral features, and text with audio is better than or on par with text alone, with small gains."
    cite:
    - mancini-etal-2022-multimodal
  - status: done
    text: MAMKit, a toolkit for multimodal argument mining.
    detail: "MAMKit is an open PyTorch toolkit that gathers 4 datasets and 6 model architectures behind one interface. Its benchmark finds that the audio helps on some tasks and not on others, possibly because the annotations were first made on transcripts."
    cite:
    - mancini-etal-2024-mamkit
  - status: next
    text: Attention-based fusion of text and audio.
    detail: "Combining the two modalities is not trivial, since some models end up relying on one modality only. We plan fusion methods based on attention."
- key: health
  title: Speech and health
  icon: heartbeat
  summary: "We study speech as a signal of mental health and neurological disorders, and how speech datasets in this domain are collected and documented."
  description: "Mental health and neurological disorders, such as depression and Parkinson's disease, can change how a person speaks. Speech datasets in this domain come from vulnerable people, and their limitations and biases affect how far the models built on them can be trusted. We ask how to document these datasets responsibly and which modalities help detection."
  items:
  - status: done
    text: Responsible speech datasets for mental health.
    detail: "We define a checklist for speech datasets on mental health and neurological disorders, covering informed consent, data security, privacy, accountability, fairness, data quality, and discourse genre. Checking 36 dataset papers against it shows that data security, privacy, and maintainability are rarely reported."
    cite:
    - mancini-etal-2025-promoting-datasets
  - status: done
    text: Depression detection from speech, text, and EEG.
    detail: "On the MODMA dataset, speech is the most informative single modality. Combining speech, text, and EEG gives the best macro F1 score, 0.864. With 38 subjects, no difference between configurations is statistically significant."
    cite:
    - nurfidausi-2025-trideptrimodalcomparativestudy
  - status: now
    text: Interpretable speech models for clinical data.
    detail: "We evaluate interpretable speech techniques on clinical data, such as speech from people with depression."
- key: explanations
  title: Explaining audio models
  icon: search
  summary: "We study how to explain the decisions of audio classifiers in a form that people can check, including by listening."
  description: "Neural networks are typically black boxes, so their decision mechanisms remain opaque. Post-hoc explanation methods produce an explanation after training, such as a saliency map that marks the parts of the input a model relied on. An explanation is faithful when it reflects what the model actually used. We ask how to make explanations faithful and useful for people, including domain experts."
  items:
  - status: done
    text: "LMAC-TD: explanations that can be heard."
    detail: "LMAC-TD trains a decoder that produces explanations directly as audio, building on Listenable Maps for Audio Classifiers (L-MAC). In a user study with 19 participants, its explanations receive higher mean opinion scores than those of the baselines, while their faithfulness stays better than or comparable to that of L-MAC."
    cite:
    - "10890448"
  - status: done
    text: Explanations for Parkinson's disease detection from speech.
    detail: "We evaluate several explanation methods for models that detect Parkinson's disease from speech, measuring the faithfulness of their saliency maps and of their unions and intersections. The explanations agree with the classifier but often fail to give useful information to domain experts."
    cite:
    - mancini-2025-investigating
  - status: now
    text: Discrete audio tokens to analyse audio inputs.
    detail: "Audio tokens are the result of a discretization of the audio signal into units. We study them as interpretable features to better analyse audio inputs."
- key: applications
  title: Speech in applications
  icon: bus
  summary: "We apply speech technologies to safety on public transport and to music retrieval."
  description: "Outside the lab, speech comes with noise, several voices, and limited hardware. Speech emotion recognition labels a recording with an emotion, such as anger or calm. Lyrics matching finds songs whose lyrics are similar in theme, meaning, or structure. We ask how speech models hold up in these settings."
  items:
  - status: done
    text: Detecting disruptive situations on public transport.
    detail: "We frame the detection of disruptive situations, such as people fighting or screaming, as speech emotion recognition, with anger, sadness, fear, and disgust as disruptive emotions. Small models for edge devices reach an F1 score above 0.90 on the disruptive class. A model trained with added transport noise loses at most 4 F1 points on noisy recordings."
    cite:
    - mancini-etal-2024-disruptive
  - status: done
    text: "WEALY: lyrics matching with Whisper embeddings."
    detail: "WEALY is a fully reproducible pipeline that uses the decoder embeddings of Whisper to match songs by their lyrics from the audio. It performs comparably to state-of-the-art methods that lack reproducibility. Combined with an audio content model, it also improves the identification of different versions of a song."
    cite:
    - mancini-2026-leveragingwhisperembeddingsaudiobased
---
