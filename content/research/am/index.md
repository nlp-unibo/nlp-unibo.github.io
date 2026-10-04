---
title: Argument Mining
date: 2026-02-27

tags:
  - argument mining
  - research
  
summary: The automatic extraction and identification of argumentative structures from text. Such argumentative structures include the premise, conclusions, the argument scheme and the relationship between arguments.

# Font Awesome icon shown on the homepage research card
icon: comments
weight: 1

# Homepage research map: tagline, cover pattern (dots, graph, tokens, or wave), own topic, and shared threads.
# Topic and thread keys come from data/topics.yaml.
tagline: Finding claims, premises, and fallacies in text, dialogue, and speech.
cover_pattern: graph
topic: argument-mining
threads:
  - argument-mining
  - interpretability
  - multimodal
  - benchmark
  - llm-reasoning

# Research map: an overview graph of subareas, then one detail panel per subarea.
# Columns run left to right in the overview. Each block is one node.
# `key` names the node, `summary` is the short text shown on hover (one or two sentences),
# and `links` lists the keys of related nodes; a link is declared once and drawn both ways.
# `status` is done (published), now (current work), or next (where we are heading).
# `cite` lists publication folder names; each renders as "Surname et al., Year" and links to the paper.
# `topics` are keys of data/topics.yaml, shown as colored tags.
map:
  - column: Finding arguments
    blocks:
      - key: speech
        title: Speech and debates
        summary: Arguments are also spoken. We study what the voice of a speaker adds to the words.
        topics: [multimodal, speech]
        links: [components, fallacies]
        items:
          - status: done
            text: Claim detection from the audio of political debates.
            cite: [lippi-torroni-2016, mancini-etal-2022-multimodal]
          - status: done
            text: An open toolkit for multimodal argument mining.
            cite: [mancini-etal-2024-mamkit]
          - status: now
            text: Measuring what audio adds to text, task by task.
      - key: components
        title: Components and relations
        summary: The core task. We find claims and premises in text and the relations that link them.
        topics: [argument-mining]
        links: [dialogues, domains, fallacies, interpretability]
        items:
          - status: done
            text: Surveys that framed argument mining as a machine learning problem.
            cite: [10-1007-978-3-319-28460-6-10, 10-1145-2850417]
          - status: done
            text: Claim detection that works across topics, served as a public tool.
            cite: [lippi-2015-context, lippi-2016292]
          - status: done
            text: Neural-symbolic, graph, and multi-task models of argument structure.
            cite: [10-3389-fdata-2019-00052, galassi-2021-investigating, ruggeri-etal-2021-tree-constrained, 10122594]
      - key: dialogues
        title: Dialogues
        summary: Arguments exchanged between people and systems. We build dialogue systems and datasets.
        topics: [benchmark]
        links: [guided]
        items:
          - status: done
            text: Dialogue systems that reason with arguments.
            cite: [10-1007-978-3-030-89391-0-27, fazzinga-2022200113]
          - status: done
            text: A dataset of argumentative dialogues on scientific papers.
            cite: [ruggeri-etal-2023-dataset]
          - status: next
            text: Moving argumentative dialogue from benchmarks to tools that people use.
  - column: Assessing and explaining
    blocks:
      - key: fallacies
        title: Fallacies
        summary: Arguments that look valid but are not. Spotting them requires reasoning.
        topics: [multimodal, llm-reasoning]
        links: [reasoning]
        items:
          - status: done
            text: The first corpus of fallacies in debate audio and text.
            cite: [mancini-etal-2024-multimodal]
          - status: done
            text: A shared task on multimodal fallacy detection.
            cite: [mancini-etal-2025-overview]
          - status: next
            text: Linking each fallacy type to the reasoning it requires.
      - key: interpretability
        title: Interpretability
        summary: Models that show why they decide. We extract the parts of an input that justify a prediction.
        topics: [interpretability]
        links: [reasoning]
        items:
          - status: done
            text: Models that explain their output with natural language knowledge.
            cite: [ruggeri-etal-2024-combining]
          - status: done
            text: Highlights that justify a prediction, learned end to end.
            cite: [ruggeri-signorelli-2025-interlocking]
          - status: now
            text: Finding which textual patterns characterise each argument component.
      - key: domains
        title: Specialised domains
        summary: Argument mining where experts need it, from clinical trials to court decisions.
        topics: [legal]
        links: []
        items:
          - status: done
            text: Arguments in clinical trials and COVID-19 literature.
            cite: [mayer-2018-argument, lippi-etal-2022-amica, brambilla-etal-2022-argument-covid]
          - status: done
            text: Arguments and their structure in court decisions.
            cite: [grundler-etal-2022-cjeu-arguments, 10-1145-3594536-3595174, grundler-etal-2024-amelia]
          - status: now
            text: Adapting LLMs to legal argument mining from a few examples.
            cite: [alfieri-2025-dynamic]
  - column: Argumentation for LLMs
    blocks:
      - key: reasoning
        title: Reasoning assessment
        summary: Argumentation as a lens on LLMs. We test whether models follow the reasoning behind a text.
        topics: [llm-reasoning]
        links: [guided]
        items:
          - status: done
            text: Reconstructing the implied reasoning behind misogynistic messages.
            cite: [muti-etal-2024-language]
          - status: done
            text: Breaking claim verification into atomic reasoning types.
            cite: [dougrez-lewis-etal-2025-assessing]
          - status: now
            text: Using argument mining tasks to probe how LLMs reason.
      - key: guided
        title: Argumentation-guided LLMs
        summary: Our vision. Argumentation that evaluates, checks, and steers LLM reasoning.
        topics: [llm-reasoning, interpretability]
        links: []
        items:
          - status: next
            text: Benchmarks centred on argumentation to evaluate LLM reasoning.
          - status: next
            text: Hybrid systems where symbolic argumentation checks LLM coherence.
          - status: next
            text: Prompting with argumentation to make LLM answers consistent.
---

Argument mining is the automatic extraction of arguments from text and speech.
An argument links a claim, the statement under discussion, to premises, the reasons that support or attack it.
We also use argumentation to assess how large language models (LLMs) reason.
The map below links our research subareas. Select one to see what we have done, what we work on now, and where we are heading.
