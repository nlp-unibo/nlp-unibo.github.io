---
title: Argument Mining
date: 2026-02-27

tags:
  - argument mining
  - research
  
summary: The automatic identification and extraction of arguments from text and speech. It covers argument components, such as claims and premises, the relations between them, and the argumentation schemes that arguments follow.

# Font Awesome icon shown on the homepage research card
icon: network-wired
weight: 1

# Homepage research card: tagline and cover pattern (dots, graph, tokens, or wave).
tagline: Extracting, linking, evaluating, and reasoning about arguments in text and speech.
cover_pattern: graph

# Definition: a short answer to "What is argument mining?" under the title. Markdown, one idea per sentence.
definition: |
  Argument mining automatically identifies and extracts arguments from natural language, in text and in speech.
  It finds the claims people make, the premises they offer as reasons, and the relations between them.
  Opinion mining tells what people think about a topic, while argument mining asks why they think it ([Lawrence and Reed, 2019](https://doi.org/10.1162/COLI_a_00364)).

# Core concepts: one block per concept, with a short text and a small schema (an SVG file in this folder, drawn with the `lt-s-*` classes).
overview:
  - icon: quote-right
    title: Arguments
    text: "Argument mining first separates argumentative text from the rest of a document. It then marks each argument component with its boundaries and its type. The two most common types are claims, the statements under discussion, and premises, the reasons given for or against them."
    schema: schema-arguments.svg
  - icon: project-diagram
    title: Relations
    text: "Relations, typically support and attack, connect argument components. Linking the components of a document through these relations gives an argument graph, whose nodes are components and whose edges are relations."
    schema: schema-relations.svg
  - icon: balance-scale
    title: Evaluation
    text: "An argument takes a stance on a topic, for or against it. Its quality is scored along dimensions such as clarity, relevance, and persuasiveness. Quality judgements are subjective, so annotators often disagree on them."
    schema: schema-evaluation.svg
  - icon: lightbulb
    title: Reasoning
    text: "Arguments often leave steps unstated, such as the warrant that links premises to a claim. Reasoning tasks recover these steps, identify the argumentation scheme of an argument, and recognize fallacies. An argumentation scheme is the reasoning pattern an argument follows, and a fallacy is a flaw in reasoning."
    schema: schema-reasoning.svg

# What is an argument?: background for the views below, shown as their section introduction. Markdown, one idea per sentence.
views_title: What is an argument?
concepts: |
  The literature offers several definitions of an argument.
  A common one comes from Walton, as reported by [Lippi and Torroni (2016)](/publication/10-1145-2850417/).
  In it, an argument is a set of premises, a conclusion, and an inference from the premises to the conclusion.
  Argument mining typically calls the conclusion a claim.
  A premise can support a claim or attack it, and claims on opposite sides can attack each other.

  An argument model defines the components of an argument, such as the claim and the premise, and the relations between them.
  The claim and premise model marks only these two components.
  The Toulmin model calls premises grounds and adds two more components.
  The warrant is the general rule that links the grounds to the claim, and the text can leave it unstated.
  The rebuttal states when the claim does not hold.
  The original model of [Toulmin (1958)](https://doi.org/10.1017/CBO9780511840005) adds the backing, a support for the warrant, and the qualifier, the degree of certainty of the claim.

  Each domain also names these components in its own way.
  In debate support, evidence takes the place of premises and supports a claim on a given topic.
  In clinical trial abstracts, evidence is an observed outcome of a study, and a claim is what the authors infer from it.
  In court decisions, the claim is called the conclusion, and premises are either factual or legal.
  The examples below show one argument for each model and each domain.

# Views: interactive examples of one argument each, grouped by argument model and by domain.
# `roles` fixes the role labels and their color order; a segment with `id` is a marked component, one without is plain text.
# Graph nodes show component IDs (role initials, or a role's `short`, plus a number). `implicit` adds components that the text leaves unstated, with a `node` text shown below the text in a dashed box.
# `tag` adds a type label to a component; `rows` places nodes in the graph from top to bottom.
# `edges` link components: `relation` is support, attack, or link, and `label` overrides the edge text.
# `caption` is Markdown: link each cited paper by its name.
views:
  - key: claim-premise
    group: Argument models
    label: Claim and premise
    description: The most common model. A claim is the statement being argued for, and premises are offered as reasons for it. Some annotations also mark premises that attack a claim.
    caption: "Example reported by [Sun et al. (2024)](https://aclanthology.org/2024.findings-acl.689/). Original wording preserved."
    roles:
      - {key: claim, label: Claim}
      - {key: premise, label: Premise}
    segments:
      - text: "Despite the fact that"
      - {id: p1, role: premise, text: "advertisements can be falseful and exaggerated"}
      - text: ", it is also true that"
      - {id: c, role: claim, text: "it plays an important role economically."}
      - {id: p2, role: premise, text: "They introduce new products."}
    rows: [[c], [p1, p2]]
    edges:
      - {from: p1, to: c, relation: attack}
      - {from: p2, to: c, relation: support}
  - key: toulmin
    group: Argument models
    label: Toulmin
    description: "A richer model. Grounds support a claim through a warrant, the general rule that links them, while a rebuttal states when the claim does not hold."
    caption: "Example from [Gupta et al. (2024)](https://aclanthology.org/2024.acl-long.552/), shortened. The warrant is not written in the text, so it is shown reconstructed below the text, with a dashed border."
    roles:
      - {key: claim, label: Claim}
      - {key: ground, label: Ground}
      - {key: rebuttal, label: Rebuttal}
      - {key: warrant, label: Warrant}
    segments:
      - {id: r, role: rebuttal, text: "Capital punishment is not a solution, as it cannot be ruled out that the judicial process may make mistakes."}
      - text: "[...] After all"
      - {id: g, role: ground, text: "there are criminals who enjoy 'living'"}
      - text: "in prison for its decent board [...]. Still,"
      - {id: c, role: claim, text: "the state needs the death penalty as a deterrent to horrific crimes."}
    implicit:
      - {id: w, role: warrant, node: "The death penalty deters criminals from committing horrific crimes."}
    rows: [[r, c, w], [g]]
    edges:
      - {from: g, to: c, relation: support}
      - {from: w, to: c, relation: link, label: licenses}
      - {from: r, to: c, relation: attack}
  - key: debate
    group: Domains
    label: Debates
    description: "In debate support, a system finds claims on a given topic and the evidence for them, for instance in Wikipedia articles. Claims on opposite sides attack each other."
    caption: "Example from the IBM debate corpus, shortened from Figure 1 of [Lippi and Torroni (2016)](/publication/10-1145-2850417/)."
    roles:
      - {key: claim, label: Claim}
      - {key: evidence, label: Evidence}
    segments:
      - text: "While those on the far-right think that"
      - {id: c1, role: claim, text: "immigration threatens national identity"}
      - text: "[...]. Proponents of immigration maintain that,"
      - {id: e, role: evidence, text: "according to Article 13 of the Universal Declaration of Human Rights, everyone has the right to leave or enter a country, along with movement within it."}
      - text: "[...] Some argue that"
      - {id: c2, role: claim, text: "the freedom of movement both within and between countries is a basic human right."}
      - text: "[...]"
      - {id: e2, role: evidence, text: "Immigration has been a major source of population growth and cultural change throughout much of the history of Sweden. The economic, social, and political aspects of immigration have caused controversy regarding ethnicity, economic benefits, jobs for non-immigrants, settlement patterns, impact on upward social mobility, crime, and voting behavior."}
    rows: [[c1, c2], [e2, e]]
    edges:
      - {from: e2, to: c1, relation: support}
      - {from: e, to: c2, relation: support}
      - {from: c1, to: c2, relation: attack}
      - {from: c2, to: c1, relation: attack}
  - key: clinical
    group: Domains
    label: Clinical trials
    description: "Clinical trial abstracts separate evidence, the observed outcomes of a study, from the claims the authors draw from it. Evidence is further typed, for instance as a comparison between groups or as a significance result."
    caption: "Example 1 of [Mayer, Cabrio, and Villata (2018)](https://aclanthology.org/W18-5204/), shortened. The paper marks the evidence and the claim; we added the support links and the evidence types following the definitions of the paper."
    roles:
      - {key: claim, label: Claim}
      - {key: evidence, label: Evidence}
    segments:
      - {id: e1, role: evidence, tag: Significance, text: "The diurnal intraocular pressure reduction was significant in both groups (P < 0.001)."}
      - {id: e2, role: evidence, tag: Comparative, text: "The mean intraocular pressure reduction from baseline was 32% for the latanoprost plus timolol group and 20% for the dorzolamide plus timolol group."}
      - text: "[...] This study clearly showed that"
      - {id: c, role: claim, text: "the additive diurnal intraocular pressure-lowering effect of latanoprost is superior to that of dorzolamide in patients treated with timolol."}
    rows: [[c], [e1, e2]]
    edges:
      - {from: e1, to: c, relation: support}
      - {from: e2, to: c, relation: support}
  - key: legal
    group: Domains
    label: Court decisions
    description: "Annotations of court decisions distinguish factual premises from legal premises and use relations specific to legal reasoning. A support from failure supports a conclusion because the opposing party failed to prove its point."
    caption: "Paragraphs 80 to 82 of Case C-431/14 P of the Court of Justice of the European Union, shortened, as annotated by [Santin et al. (2023)](/publication/10-1145-3594536-3595174/)."
    roles:
      - {key: conclusion, label: Conclusion}
      - {key: factual, label: "Factual premise"}
    segments:
      - text: "First, as the Commission correctly contends,"
      - {id: f1, role: factual, text: "the General Court responded in detail to the complaint relating to an alleged breach of the principle of proportionality [...]."}
      - text: "Secondly,"
      - {id: f2, role: factual, text: "the Hellenic Republic has not indicated with sufficient precision the other complaints put forward by it at first instance to which the General Court did not respond."}
      - text: "In those circumstances,"
      - {id: c, role: conclusion, text: "the second part of this ground of appeal must be rejected as, in part, unfounded and, in part, inadmissible."}
    rows: [[c], [f1, f2]]
    edges:
      - {from: f1, to: c, relation: support}
      - {from: f2, to: c, relation: support, label: support from failure}

# Research areas: one block per macro topic. Selecting a block enlarges it and opens its tasks beside it.
# Each task states its input and the expected output.
fields:
  - key: extraction
    title: Argument extraction
    icon: search
    question: Where are the arguments in a text, and what are their parts?
    summary: Extraction tasks separate argumentative text from the rest, segment it into argument components, and group arguments by the aspects they address.
    tasks:
      - name: Argumentative text detection
        text: Given a sentence or a passage, the task is to decide whether it contains an argument.
      - name: Argument component identification
        text: Given an argumentative text, the task is to mark the boundaries of each component and to label it, for instance as a claim or a premise.
      - name: Claim and evidence retrieval
        text: Given a topic and a set of documents, the task is to retrieve the claims on the topic and the evidence for each claim.
      - name: Aspect mining
        text: Given an argument, the task is to identify the aspects it addresses, such as the cost or the safety of nuclear energy. Arguments on the same aspect can then be grouped.
  - key: relations
    title: Argument relations
    icon: project-diagram
    question: How do claims and premises relate to each other?
    summary: Component identification finds claims and premises, while relation identification decides how they connect, for instance through support or attack. These relations define an argument graph over the whole document.
    tasks:
      - name: Relation identification
        text: Given two argument components, the task is to decide whether one supports or attacks the other, or whether they are unrelated.
      - name: Argument structure prediction
        text: Given a document, the task is to predict its argument graph, where components are nodes and relations are edges.
  - key: evaluation
    title: Argument evaluation
    icon: balance-scale
    question: Which side does an argument take, and how good is it?
    summary: Evaluation tasks assign properties to arguments, such as their stance on a topic or their quality.
    tasks:
      - name: Stance classification
        text: Given a topic and an argument, the task is to decide whether the argument is for or against the topic.
      - name: Argument quality assessment
        text: Given an argument, the task is to score its quality along dimensions such as clarity, relevance, and persuasiveness. A pairwise variant selects the more convincing of two arguments.
  - key: reasoning
    title: Argument reasoning
    icon: lightbulb
    question: What does an argument leave unsaid, and does its reasoning hold?
    summary: Arguments often leave some steps unstated. These tasks recover the missing steps and assess the inference.
    tasks:
      - name: Implicit argument reconstruction
        text: Given an argument with missing steps, the task is to generate the unstated premise or the warrant, the general rule that links premise and claim. This typically requires commonsense or expert knowledge.
      - name: Argumentation scheme classification
        text: Given an argument, the task is to identify its argumentation scheme, the reasoning pattern it follows, such as an argument from consequences.
      - name: Fallacy recognition
        text: Given an argument, the task is to decide whether its reasoning is flawed and, if so, which fallacy it commits.
  - key: generation
    title: Argument generation and retrieval
    icon: pen-fancy
    question: Can a system write, condense, or retrieve arguments?
    summary: Generation tasks write or condense arguments, while retrieval tasks find arguments in large collections.
    tasks:
      - name: Argument summarization
        text: Given many arguments on a topic, the task is to produce a short summary or a small set of key points.
      - name: Argument generation
        text: Given a topic or an argument, the task is to generate a new argument, potentially for the opposite stance.
      - name: Argument retrieval
        text: Given a query, the task is to retrieve relevant arguments from a large collection.
  - key: llms
    title: Argument mining and LLMs
    icon: robot
    question: What do large language models change, and what can argumentation give back?
    summary: Large language models (LLMs) are now widely applied to argument mining tasks. Argumentation, in turn, offers a way to check how these models reason.
    tasks:
      - name: LLMs for argument mining
        text: Prompting and fine-tuning allow a single model to address many tasks. Fallacy recognition and the modelling of diverse perspectives remain challenging.
      - name: Argumentation for LLMs
        text: Argumentative prompts elicit LLM reasoning, and dedicated benchmarks evaluate it. Computational argumentation, a formal way of modelling arguments and their conflicts, can verify it.

# Our focus: the lab topics, shown as a rotating carousel and, below it, one detail box per topic.
# `status` is done (Explored), now (Current), or next (Future).
# `text` is the bullet on the card, and `detail` explains it in the detail box.
# `cite` lists publication folder names; Explored objectives show them on the right of the detail box.
focus:
  - key: fallacies
    title: Argumentative fallacies
    icon: exclamation-triangle
    summary: "We study how machines can spot and name fallacies, which are flaws or errors in reasoning that can make an argument seem convincing. Spotting them takes careful reasoning, so they are a hard test for language models."
    description: "A fallacy is a flaw or error in reasoning. Examples are attacking the speaker instead of the claim (ad hominem) and warning that one small step leads to disaster (slippery slope). Fallacy detection asks whether a passage contains a fallacy, and fallacy classification asks which type it is. In political debates, how something is said can matter as much as what is said. We ask whether models can recognize fallacies from both the words and the voice of a speaker, and what reasoning each type of fallacy requires."
    items:
      - status: done
        text: "The first corpus of fallacies in debate audio and text."
        detail: "We release the first corpus for classifying fallacies from both the transcript and the audio of political debates. Our experiments show that adding the audio leads to better classification. This suggests that fallacies carry cues in tone and delivery that text alone misses."
        cite: [mancini-etal-2024-multimodal]
      - status: done
        text: "A shared task on multimodal fallacy detection."
        detail: "We organized MM-ArgFallacy2025, a shared task on detecting and classifying six fallacy types in U.S. presidential debates from text, audio, or both. Five teams took part. Text-only systems performed best, audio-only systems improved over previous work, and combining the two gave limited gains. The task sets baselines for future work on multimodal fallacy analysis."
        cite: [mancini-etal-2025-overview]
      - status: next
        text: "Linking each fallacy type to the reasoning it requires."
        detail: "We plan to describe which reasoning steps a reader needs to recognize each type of fallacy. This can show where models fail and why some fallacy types are harder than others."
  - key: multimodality
    title: Multimodality
    icon: layer-group
    summary: "Arguments are often spoken, not written. We study whether the sound of a voice helps a computer find and classify arguments better than the words alone."
    description: "Multimodality means using more than one kind of input, here the text of what people say and the audio of how they say it. Audio carries paralinguistic cues, such as tone, pitch, and pauses, that a written transcript loses. We ask whether these cues help with argument mining tasks, and for which tasks they help."
    items:
      - status: done
        text: "Claim detection from the text and audio of political debates."
        detail: "A claim is the statement an argument tries to support. We build a classifier that combines features from text and speech to detect claims in political debates, using an original dataset built from the 2015 UK political elections debate. We then release MM-USElecDeb60to16, the largest multimodal argument mining corpus to date, with 26,791 sentences from U.S. presidential debates aligned with their audio. Across three corpora, embedding-based audio encodings work better than feature-based ones."
        cite: [lippi-torroni-2016, mancini-etal-2022-multimodal]
      - status: done
        text: "Fallacy classification that listens to the speaker."
        detail: "A fallacy is a flaw or error in reasoning, such as an attack on the person instead of the point. We release the first corpus for multimodal fallacy classification in political debates. Our experiments show that adding audio to text improves classification performance."
        cite: [mancini-etal-2024-multimodal]
      - status: done
        text: "An open toolkit for multimodal argument mining."
        detail: "MAMKit is a public PyTorch toolkit that gathers datasets and models in one place, so that results are easy to reproduce and compare. It includes new baselines for encoding and combining text and audio. Our first results with it suggest that progress needs new annotation processes that capture auditory cues."
        cite: [mancini-etal-2024-mamkit]
      - status: done
        text: "A shared task on fallacies in text, audio, and both."
        detail: "We organized MM-ArgFallacy2025, a shared task in which teams detect and classify fallacies in U.S. presidential debates from text only, audio only, or both. Text-only systems perform best, audio-only systems improve over previous work, and combining the two gives limited gains."
        cite: [mancini-etal-2025-overview]
      - status: now
        text: "Measuring what audio adds to text, task by task."
        detail: "We compare text-only, audio-only, and combined models on the same argument mining tasks. The goal is to tell apart the tasks where audio helps from those where text is enough."
  - key: dialogues
    title: Dialogues
    icon: comments
    summary: "We study dialogue systems that exchange arguments with people. Such systems can explain their answers, which matters when users need to trust the information they receive."
    description: "A dialogue system is a computer program that talks with a person, such as a chatbot. An argumentative dialogue is a conversation in which the speakers give reasons for their claims and question the reasons of others. We ask how a dialogue system can reason with arguments, explain its answers, and discuss a topic the way people do."
    items:
      - status: done
        text: "Dialogue systems that reason with arguments."
        detail: "We propose a dialogue system architecture that uses computational argumentation, a formal way of modeling arguments and their conflicts, to reason and give consistent, explainable answers. A later version manages user data according to the principles of data minimization, purpose limitation, and integrity. It also motivates its responses to users. We illustrate both systems with a COVID-19 vaccine information case study and evaluate the privacy-preserving version empirically."
        cite: [10-1007-978-3-030-89391-0-27, fazzinga-2022200113]
      - status: done
        text: "A dataset of argumentative dialogues on scientific papers."
        detail: "We introduce ArgSciChat, a dataset of 41 dialogues between scientists on 20 NLP papers, with both exploratory and argumentative questions and answers. A pre-trained dialogue agent performs poorly on it. This result motivates dialogue agents that can reason and argue about their answers."
        cite: [ruggeri-etal-2023-dataset]
      - status: next
        text: "From argumentative dialogue benchmarks to tools people use."
        detail: "We plan to move from building benchmarks, which are shared datasets for testing systems, to building argumentative dialogue tools that people use in practice."
  - key: interpretability
    title: Interpretability
    icon: eye
    summary: "We build models that show why they make a decision. This helps people check a prediction and learn which parts of a text make an argument."
    description: "A model is interpretable when people can understand why it gives a certain output. One common form is an explanation, a piece of evidence that justifies a prediction. An explanation can be a sentence of background knowledge or a highlight, a span of the input text. We ask how models for argument analysis can explain their own decisions without losing accuracy. We also ask what these explanations tell us about the data."
    items:
      - status: done
        text: "Models that explain their output with natural language knowledge."
        detail: "We extend transformer models, a common type of neural network for text, with an external memory that stores explanations written in plain language. The model uses these stored texts to explain each classification it makes. Tests on legal texts and on argument mining show that the explanations are relevant and that classification performance is maintained or improved."
        cite: [ruggeri-etal-2024-combining]
      - status: done
        text: "Highlights that justify a prediction, learned end to end."
        detail: "In selective rationalization, one module picks highlights from the text and a second module predicts a label from those highlights alone. Training the two modules together often fails because one module dominates the other, a problem called interlocking. We present GenSPP, which avoids interlocking by training the two modules disjointly with genetic-based search. It requires no additional heuristics, sampling, or regularization."
        cite: [ruggeri-signorelli-2025-interlocking]
      - status: now
        text: "Finding the textual patterns behind each argument component."
        detail: "Argument components are the parts of an argument, such as a claim or a premise that supports it. We use local explanations, which justify one prediction at a time, to find which words and patterns typically mark each component."
  - key: reasoning
    title: Reasoning in LLMs
    icon: brain
    summary: "We use argumentation to test how large language models reason. This matters because these models now answer questions and judge content, yet their reasoning often fails in ways that are hard to see."
    description: "Large language models (LLMs) are AI systems trained on large amounts of text to read and write language. Reasoning is the ability to move from given information to a conclusion through steps that someone else can check. Argumentation studies exactly these steps: the claims people make, the reasons they give, and the links between them. We ask whether argumentation can serve as a tool to assess, and later improve, the reasoning of LLMs."
    items:
      - status: done
        text: Reconstructing the implied reasoning behind misogynistic messages.
        detail: "We frame misogyny detection as an argumentative reasoning task, where the model must generate the missing link between a message and the misogynistic meaning it implies. We build prompts in Italian and English on top of argumentation theory. LLMs fall short on this task and mostly rely on common stereotypes about women rather than on inductive reasoning, which means drawing general conclusions from specific cases."
        cite: [muti-etal-2024-language]
      - status: done
        text: Breaking claim verification into atomic reasoning types.
        detail: "We propose a framework that splits a claim and its evidence into the basic reasoning steps needed to verify it. With this framework we build RECV, a benchmark of real-world claims that tests deductive reasoning (conclusions that follow necessarily) and abductive reasoning (inferring the most plausible explanation). LLMs handle deductive problems but consistently fail on abductive ones, and asking them to explain their answers does not always help."
        cite: [dougrez-lewis-etal-2025-assessing]
      - status: now
        text: Using argument mining tasks to probe how LLMs reason.
        detail: "Argument mining is the automatic identification of arguments and their components in text and speech. We use its tasks as tests that show where LLM reasoning holds and where it breaks."
      - status: next
        text: Benchmarks centered on argumentation to evaluate LLM reasoning.
        detail: "We plan to build evaluation benchmarks in which each test item is an argumentative problem. This would let us measure reasoning skills directly instead of only final answers."
---
