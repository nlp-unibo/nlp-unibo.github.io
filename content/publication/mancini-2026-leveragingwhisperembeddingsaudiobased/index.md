---
title: Leveraging Whisper Embeddings for Audio-based Lyrics Matching

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- Eleonora Mancini
- Joan Serrà
- Paolo Torroni
- Yuki Mitsufuji

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2026-05-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2026-03-02T12:28:22.228519Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- paper-conference

# Publication name and optional abbreviated publication name.
publication: '*ICASSP 2026 - 2026 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)*'
publication_short: ''

doi: 10.1109/icassp55912.2026.11461231

abstract: 'Audio-based lyrics matching can be an appealing alternative to other content-based retrieval approaches, but existing methods often suffer from limited reproducibility and inconsistent baselines. In this work, we introduce WEALY, a fully reproducible pipeline that leverages Whisper decoder embeddings for lyrics matching tasks. WEALY establishes robust and transparent baselines, while also exploring multimodal extensions that integrate textual and acoustic features. Through extensive experiments on standard datasets, we demonstrate that WEALY achieves a performance comparable to state-of-the-art methods that lack reproducibility. In addition, we provide ablation studies and analyses on language robustness, loss functions, and embedding strategies. This work contributes a reliable benchmark for future research, and underscores the potential of speech technologies for music information retrieval tasks.'

# Summary. An optional shortened abstract.
summary: WEALY matches songs by their lyrics straight from the audio, using Whisper speech embeddings, and offers a reproducible baseline across three public datasets.

tags:
- lyrics matching
- whisper
- musical version identification
- contrastive learning
- music information retrieval

# Display this page in a list of Featured pages?
featured: false

# Links
url_pdf: ''
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

# Publication image
# Add an image named `featured.jpg/png` to your page's folder then add a caption below.
image:
  caption: "The WEALY pipeline: a frozen Whisper model turns the song audio into lyrics-aware latents, and a trained transformer encoder maps them to one embedding per song (Figure 1 of the paper, arXiv version, CC BY)."
  focal_point: ''
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects: ['internal-project']` links to `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []
links:
- name: arXiv
  url: https://arxiv.org/abs/2510.08176
categories:
  - Conference
aliases:
  - /publication_preprints/mancini-2026-leveragingwhisperembeddingsaudiobased/
topics: [information-retrieval, speech, multimodal, reproducibility]
---

## Research setting

Audio-based lyrics matching finds songs whose lyrics are similar, using only the song audio.
It can support copyright protection, music discovery, and songwriters who want to avoid unintentional plagiarism.
Datasets of matched lyrics are scarce, so the paper evaluates on musical version identification (MVI).
In MVI, a system receives a song and must find its other versions, such as covers, in a large collection.
Versions of one song usually share their lyrics, so they give similarity labels without curated lyric texts.

{{< pipeline caption="The retrieval task used for evaluation: a query song goes in, and a ranked list of candidate songs comes out." >}}
- title: Query song
  text: Raw audio only, no lyrics text.
  icon: music
- title: Song embedding
  text: One vector that describes the lyrics.
  icon: wave-square
  highlight: true
- title: Compare with collection
  text: Similarity with every candidate song.
  icon: search
- title: Ranked list
  text: Versions of the query should come first.
  icon: list-ol
{{< /pipeline >}}

Terms used on this page:

- **Whisper** is a large speech recognition model that turns speech into text. Its decoder writes the text one word piece at a time.
- **Whisper embeddings** (or latents) are the internal vectors of the decoder just before it picks each word piece. They describe what is being sung without writing it down.
- **Contrastive learning** trains a model to place versions of the same song close together and different songs far apart.
- **Mean average precision (MAP)** scores a ranked list by how high the true versions of each query appear, averaged over all queries. It ranges from 0 to 1, and higher is better.

## Motivation

Lyrics text is often unavailable, incomplete, or restricted by copyright, and transcription of singing makes errors.
Early lyrics-based systems depend on transcripts or external lyrics databases.
Recent systems use Whisper inside complex pipelines that combine source separation, transcriptions, and several embeddings.
These pipelines offer limited transparency and reproducibility.
Prior work is also evaluated on limited datasets, so the field has no robust benchmark.

{{< gap caption="How the paper positions itself against the related work it discusses (Introduction and Section 2 of the paper)." >}}
label: Approach
columns: [Works without transcripts, Transparent and reproducible, Several datasets]
rows:
  - name: Text-based (Knees et al., 2005; Patra et al., 2017)
    cells: [false, "not discussed", "not discussed"]
  - name: Transcript or lyrics database (Correya et al., 2018; Vaglio et al., 2021)
    cells: [false, "not discussed", "not discussed"]
  - name: Whisper-based (Balluff et al., 2024; Du et al., 2024)
    cells: [false, false, "not discussed"]
  - name: This paper (WEALY)
    ours: true
    cells: [true, true, true]
{{< /gap >}}

> **Objective.** Build a fully reproducible, end-to-end pipeline that matches songs by their lyrics directly from audio, and set transparent baselines for it on several public datasets.

## Approach

WEALY (Whisper Embeddings for Audio-based LYrics matching) works in two stages.
First, a frozen Whisper model listens to the song in 30-second chunks and keeps its decoder embeddings, without producing a transcript.
Second, a transformer encoder reads a random window of 1500 of these embeddings, pools them over time, and projects them to one 512-dimensional song embedding.
Only the encoder is trained, with a contrastive loss on pairs of versions of the same song.
At test time, each song is cut into overlapping windows, and two songs are as similar as their best-matching pair of windows.

{{< stages caption="The two stages of WEALY: what is frozen and what is trained (Section 3 and Figure 1 of the paper)." >}}
flow: [Song audio, Whisper, Latents, Encoder, Output]
stages:
  - title: 1. Feature extraction
    text: The song is resampled to 16 kHz mono and cut to at most 5 minutes. Frozen Whisper decodes it chunk by chunk, and the decoder states are kept as lyrics-aware latents.
    states: {Song audio: data, Whisper: frozen, Latents: data}
  - title: 2. Feature adaptation
    text: A transformer encoder with 4 blocks turns a window of latents into the output, one song embedding. It learns with a contrastive loss that pulls versions of the same song together.
    states: {Song audio: data, Whisper: frozen, Latents: data, Encoder: trained, Output: data}
{{< /stages >}}

The paper also tests a multimodal extension.
It adds the WEALY distance between two songs to the distance from CLEWS, an existing audio-content model for version identification, so lyrics and sound are combined at the distance level.

## Results

The authors measure MAP for version identification on three public datasets: DiscogsVI-YT (DVI), SHS100k-v2 (SHS), and LyricCovers2.0 (LYC).
LYC covers 80 languages.
They compare WEALY with baselines that transcribe the lyrics with Whisper and then compare the texts, and with raw Whisper embeddings averaged over time without training.

{{< numbers >}}
- value: "0.692"
  label: MAP of WEALY on LYC
- value: "0.573"
  label: MAP of the best transcription baseline on LYC
- value: "0.912"
  label: MAP on SHS when WEALY is fused with CLEWS
{{< /numbers >}}

| Method | DVI | SHS | LYC |
|---|---|---|---|
| Random | 0.001 | 0.003 | 0.002 |
| TF-IDF on transcripts, cosine | 0.272 | 0.503 | 0.537 |
| TF-IDF on transcripts, Lucene | 0.242 | 0.457 | 0.486 |
| Sentence-BERT on transcripts, cosine | 0.294 | 0.508 | 0.573 |
| Sentence-BERT on transcripts, trained transformer | N/A | 0.480 | 0.516 |
| Averaged Whisper embeddings, no training | 0.166 | 0.297 | 0.322 |
| **WEALY (this work)** | **0.328** | **0.640** | **0.692** |
| Oracle upper bound (versions with valid lyrics) | 0.967 | 0.956 | 0.954 |

*MAP on the test sets (Table 1 of the paper). The oracle gives a perfect match to every version with usable lyrics, so it bounds what a lyrics-only method can reach.*

WEALY beats every transcription-based baseline on all three datasets.
Averaged Whisper embeddings without training score lowest, so the trained encoder is needed.
In the ablation on SHS, the contrastive loss matters most: a triplet loss drops MAP from 0.640 to 0.548.
Forcing Whisper to decode every song as English drops MAP to 0.578, so the multilingual cues in the embeddings help retrieval.

{{< bars caption="Version identification on SHS, MAP on the test set; whiskers show the reported ± value. Source: Table 3 of the paper." >}}
metric: MAP on SHS
unit: ""
min: 0
max: 1
bars:
  - label: ByteCover1/2 (audio content)
    value: "0.813"
    err: "0.006"
  - label: ByteCover3.5 (audio content)
    value: "0.857"
  - label: CLEWS (audio content)
    value: "0.876"
    err: "0.005"
  - label: WEALY + CLEWS (lyrics and audio)
    value: "0.912"
    err: "0.004"
    ours: true
{{< /bars >}}

Alone, WEALY stays below the strongest audio-content models for version identification.
Added to CLEWS with a simple sum of distances, it gives the best MAP, so lyrics and sound carry complementary information.

## Takeaways

{{< takeaways >}}
- title: No transcript needed.
  text: Whisper decoder embeddings, taken straight from the audio, beat pipelines that first transcribe the lyrics and then compare the texts, on all three datasets.
- title: A reproducible baseline.
  text: WEALY sets transparent results on three public datasets, and the authors release the code and the model checkpoints.
- title: Lyrics complement sound.
  text: A simple distance-level fusion of WEALY with the audio model CLEWS raises MAP on SHS from 0.876 to 0.912.
{{< /takeaways >}}
