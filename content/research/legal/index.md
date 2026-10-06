---
title: Legal Analytics
date: 2026-02-27

tags:
  - legal
  - legal analytics
  - research

summary: The process of automatically understanding and extracting legal knowledge from legal documents.

# Font Awesome icon shown on the homepage research card
icon: balance-scale
weight: 2

# Homepage research card: tagline and cover pattern (dots, graph, tokens, or wave).
tagline: Turning court decisions and contracts into structured legal knowledge.
cover_pattern: tokens

# Definition: a short answer to "What is legal analytics?" under the title. Markdown, one idea per sentence.
definition: |
  Legal analytics applies artificial intelligence and natural language processing, the study of how computers handle language, to legal documents such as laws, court decisions, contracts, and privacy policies ([Lippi et al., 2019](/publication/lippi-2019-claudette/); [Zhong et al., 2020](https://doi.org/10.18653/v1/2020.acl-main.466)).
  It finds the parts of a document, the arguments of a court, the unfair terms of a contract, and the likely outcome of a case.
  These documents are long and hard to read, so such tools can support consumers, lawyers, judges, and public agencies.

# Core concepts: one block per concept, with a short text and a small schema (an SVG file in this folder, drawn with the `lt-s-*` classes).
overview:
  - icon: stream
    title: Structure
    text: "Legal documents are long and unstructured. Systems first parse a raw document into its relevant parts, such as the facts, the requests of a party, or the arguments of a lawyer. Each sentence can also receive a rhetorical role, the function it plays in the document."
    schema: schema-structure.svg
  - icon: landmark
    title: Arguments
    text: "Argument mining retrieves the chains of premises and conclusions behind a decision, which show the reasoning of a court. Legal arguments use components tailored to the domain, such as factual and legal premises, and argument schemes such as rule or precedent."
    schema: schema-arguments.svg
  - icon: gavel
    title: Outcome
    text: "Outcome prediction links the text of a case to the decision of the court. For instance, a system predicts whether the court upholds or rejects the request of a party."
    schema: schema-outcome.svg
  - icon: user-shield
    title: Compliance
    text: "Compliance analysis checks whether a document respects the law. Systems flag terms of service clauses that may be unfair to consumers, and check privacy policies against the General Data Protection Regulation (GDPR), the EU data protection law."
    schema: schema-compliance.svg

# What is legal annotation?: background for the views below, shown as their section introduction. Markdown, one idea per sentence.
views_title: What is legal annotation?
concepts: |
  Legal analytics starts from annotation.
  Legal experts mark the parts of a document that matter for a legal question and give each part a label.
  An annotation schema fixes these parts, their labels, and their links, and guidelines tell the annotators how to apply it.
  The agreement between annotators measures how reliable the labels are.
  Models trained on such annotations produce the same structure for new documents.

  The examples below follow the four core concepts.
  For structure, privacy policies are annotated through explicit rules that the GDPR motivates.
  For arguments, court decisions are annotated with chains of premises and conclusions.
  For outcome, decisions are annotated with the requests of the parties, their claims and arguments, and the final ruling.
  For compliance, terms of service are annotated with the category and the fairness level of each clause.
  The last example follows one annotated clause across two languages.

# Views: interactive examples, grouped by annotation concept and by method.
# `roles` fixes the role labels and their color order; a segment with `id` is a marked component, one without is plain text.
# `texts` replaces `segments` to show several texts side by side, each with a `label` and a `lang`.
# Graph nodes show component IDs (role initials, or a role's `short`, plus a number). `implicit` adds components that the text leaves unstated, with a `node` text;
# an implicit component with `kind: label` is a label assigned by the annotation, drawn as a regular box.
# `tag` adds a type label to a component; `rows` places nodes in the graph from top to bottom.
# `edges` link components: `relation` is support, attack, or link, and `label` overrides the edge text.
# `caption` is Markdown: link each cited paper by its name. `graph_title` renames the graph panel, "Argument graph" by default.
views:
  # `type: rules` shows a document beside a clause matrix: Detect marks the clauses and fills their rows, Classify lights the matching rule.
  # A clause with a `level` and a `rule` concerns personal data; its `parts` are plain `text` or marks with a `role`
  # (category, specification, or subcategory) and a `type` (open or closed), and a specification holds its own `parts`.
  # `rules` lists the annotation rules: each states the type of the category, the specification, and the subcategories (open, closed, any, or none).
  - key: privacy
    type: rules
    group: Annotation
    label: Structure
    description: "Under the EU General Data Protection Regulation (GDPR), a privacy policy must say which categories of personal data it processes. Experts mark each clause about data with its category of data, the specification that introduces a list, and the subcategories in that list. Each mark is open when its terms are vague or its list is open-ended, and closed when they are precise or exhaustive."
    caption: "Clauses from the TikTok privacy policy of 19 November 2023, with the expert annotation used in [Grundler et al. (2025)](/publication/grundler-2025-detecting/). The rules are those of Table 2 of the paper."
    document: TikTok privacy policy
    levels:
      "1": Sufficiently informative
      "2": Insufficiently informative
    rules:
      - {level: 1, n: 1, category: closed, specification: none, subcategory: none}
      - {level: 1, n: 2, category: closed, specification: any, subcategory: any}
      - {level: 1, n: 3, category: open, specification: closed, subcategory: closed}
      - {level: 2, n: 1, category: open, specification: none, subcategory: none}
      - {level: 2, n: 2, category: open, specification: open, subcategory: any}
      - {level: 2, n: 3, category: open, specification: closed, subcategory: open}
    sections:
      - sentences:
          - level: 2
            rule: 1
            parts:
              - {role: category, type: open, text: "Profile Information"}
              - {text: "."}
          - level: 1
            rule: 2
            parts:
              - {text: "We collect"}
              - {role: category, type: closed, text: "information that you provide when you set up an account"}
              - {text: ","}
              - role: specification
                type: open
                parts:
                  - {text: "such as"}
                  - {role: subcategory, type: closed, text: "your date of birth"}
                  - {text: ","}
                  - {role: subcategory, type: closed, text: "username"}
                  - {text: ","}
                  - {role: subcategory, type: closed, text: "email address"}
                  - {text: "and/or"}
                  - {role: subcategory, type: closed, text: "telephone number"}
                  - {text: ", and"}
                  - {role: subcategory, type: closed, text: "password"}
                  - {text: "."}
          - level: 2
            rule: 2
            parts:
              - {text: "You can add"}
              - {role: category, type: open, text: "other information to your profile"}
              - {text: ","}
              - role: specification
                type: open
                parts:
                  - {text: "such as"}
                  - {role: subcategory, type: open, text: "a bio"}
                  - {text: "or"}
                  - {role: subcategory, type: closed, text: "a profile photo"}
                  - {text: "."}
      - sentences:
          - parts:
              - {text: "Merchants, Payment and Transaction Fulfillment Providers."}
          - level: 2
            rule: 2
            parts:
              - {text: "We receive"}
              - {role: category, type: open, text: "information about you"}
              - {text: "from merchants as well as payment and transaction fulfillment providers,"}
              - role: specification
                type: open
                parts:
                  - {text: "such as"}
                  - {role: subcategory, type: closed, text: "payment confirmation details"}
                  - {text: ", and"}
                  - {role: subcategory, type: closed, text: "information about the delivery of products you have purchased"}
                  - {text: "through our shopping features"}
              - {text: "."}
  - key: decisions
    group: Annotation
    label: Arguments
    description: "In court decisions, legal premises state rules, precedents, or principles, and factual premises describe the case. Legal premises also carry the argumentation scheme they follow."
    caption: "Paragraph 46 of Case C-850/19 P of the Court of Justice of the European Union, shortened, as annotated by [Santin et al. (2023)](/publication/10-1145-3594536-3595174/)."
    roles:
      - {key: legal, label: Legal premise}
      - {key: factual, label: Factual premise}
    segments:
      - {text: "[...]"}
      - {id: d2, role: factual, text: "However, it must be pointed out that that argument is based on a misreading of that judgment."}
      - {text: "[...]"}
      - {id: d3, role: legal, tag: "Precedent, classification", text: "It is apparent from that judgment that the fact of coming from a compulsory levy is, on the contrary, sufficient to identify State resources"}
      - {text: "(see, to that effect, [...]). [...]"}
      - {id: d5, role: factual, text: "The first part of the fourth ground of appeal must therefore be rejected as unfounded."}
    rows: [[d3], [d2], [d5]]
    edges:
      - {from: d3, to: d2, relation: support}
      - {from: d2, to: d5, relation: support}
  - key: outcome
    group: Annotation
    label: Outcome
    description: "Tax decisions are annotated with the request of each party, the claims that ground it, the arguments that support the claims, and the decision of the court on the request. Outcome prediction learns from these annotated parts whether the court upholds or rejects a request."
    caption: "Decision 362/2018 of an Italian Regional Tax Commission from the italianVAT corpus, shortened, as annotated by [Galli et al. (2022)](/publication/galli-etal-2022-outcomes/). The English text is our translation of the Italian original."
    roles:
      - {key: request, label: Request}
      - {key: claim, label: Claim}
      - {key: argument, label: Argument}
      - {key: decision, label: Decision}
    segments:
      - {text: "[...]"}
      - {id: r, role: request, text: "The first-instance decision was appealed by the tax office before this Regional Tax Commission,"}
      - {id: c, role: claim, text: "which insisted that its assessment was correct"}
      - {id: a, role: argument, text: "because the analysis of the company revealed undeclared revenues, assessed inductively, and the disallowance of non-deductible costs."}
      - {text: "[...] For these reasons, [the Commission]"}
      - {id: d, role: decision, tag: Upheld, text: "upholds the appeal of the tax office and reverses the first-instance decision."}
    rows: [[d], [r], [c], [a]]
    edges:
      - {from: d, to: r, relation: link, label: upholds}
      - {from: c, to: r, relation: support}
      - {from: a, to: c, relation: support}
  # `type: detect` shows a document whose sentences Detect scans; a sentence with a `category` and a `level`
  # (1 clearly fair, 2 potentially unfair, 3 clearly unfair) is a clause marked by the annotators.
  - key: terms
    type: detect
    group: Annotation
    label: Compliance
    description: "Online terms of service often contain clauses that may be unfair to consumers under EU law. Each such clause gets a category, such as unilateral termination, and a fairness level: clearly fair, potentially unfair, or clearly unfair."
    caption: "Two sections of the Academia.edu terms of service, as annotated by legal experts in [Lippi et al. (2019)](/publication/lippi-2019-claudette/). Detect shows these expert labels, which the CLAUDETTE classifiers learn to reproduce."
    document: Academia.edu terms of service
    sections:
      - title: Modification
        sentences:
          - {category: Unilateral change, level: 2, text: "Academia.edu reserves the right, at its sole discretion, to modify the Site, Services and these Terms, at any time and without prior notice."}
          - {text: "If we modify these Terms we will post the modification on the Site or provide you with notice of the modification."}
          - {text: "We will also update the “Last Updated Date” at the top of these Terms."}
          - {category: Contract by using, level: 2, text: "By continuing to access or use the Site or Services after we have posted a modification on the Site or have provided you with notice of a modification, you are indicating that you agree to be bound by the modified Terms."}
          - {text: "If the modified Terms are not acceptable to you, your only recourse is to cease using the Site and Services."}
      - title: Termination and Account Cancellation
        sentences:
          - {category: Unilateral termination, level: 3, text: "Academia.edu reserves the right, at its sole discretion, to discontinue or terminate the Site and Services and to terminate these Terms, at any time and without prior notice."}
          - {category: Unilateral termination, level: 3, text: "If you breach any of these Terms, Academia.edu will have the right to suspend or disable your Account or terminate these Terms, at its sole discretion and without prior notice to you."}
          - {category: Unilateral termination, level: 3, text: "Academia.edu reserves the right to revoke your access to and use of the Site, Services and Collective Content at any time, with or without cause."}
          - {text: "You may cancel your Account at any time by visiting your Account Settings page and clicking on “Remove” or by sending an email to feedback@academia.edu."}
  - key: languages
    group: Annotation
    label: Cross-linguality
    graph_title: Clause alignment
    description: "Annotation projection copies the labels of an English contract to the same contract in another language, so that a classifier can be trained there without new annotation. The example shows why sentence-level projection is hard: one English sentence matches two German ones."
    caption: "Example 4.1 of [Galassi et al. (2020)](/publication/galassi-etal-2020-cross/), from the Box.com terms of service. Both versions show the annotation of legal experts."
    roles:
      - {key: source, label: Annotated clause}
      - {key: target, label: Matching clause}
    texts:
      - label: English
        lang: en
        segments:
          - {id: en, role: source, tag: "content removal, unilateral termination", text: "We reserve the right to delete or disable Content alleged to violate copyright laws or these Terms and reserve the right to terminate the account(s) of violators."}
      - label: German
        lang: de
        segments:
          - {id: de1, role: target, tag: "content removal", text: "Wir behalten uns das Recht vor, Inhalte zu löschen oder zu deaktivieren, die vorgeblich gegen Urheberrechtsgesetze oder diese Bedingungen verstoßen."}
          - {id: de2, role: target, tag: "unilateral termination", text: "Zusätzlich behalten wir uns das Recht vor, den/die Account(s) des Beschuldigten zu sperren."}
    rows: [[en], [de1, de2]]
    edges:
      - {from: en, to: de1, relation: link, label: content removal}
      - {from: en, to: de2, relation: link, label: unilateral termination}

# Research areas: one block per macro topic. Selecting a block enlarges it and opens its tasks beside it.
# Each task states its input and the expected output.
fields:
- key: reading-documents
  title: Reading legal documents
  icon: book-open
  question: "How can a computer find the parts, names, and topics of a legal document?"
  summary: "Legal documents are long, unstructured, and written in legal jargon. Systems label their sentences, names, topics, and key statements so that later tasks can build on them."
  tasks:
  - name: Rhetorical role labelling
    text: "Given a court judgment split into sentences, the task is to label each sentence with its rhetorical role, such as preamble, facts, or arguments. A rhetorical role is the function that a sentence plays in the document."
  - name: Legal named entity recognition
    text: "Given a legal document, the task is to find named entities, such as the petitioner, respondent, court, or statute. Named entities are specific names."
  - name: Legal topic classification
    text: "Given a law or another legal document, the task is to assign one or more topic labels from a fixed list of categories."
  - name: Extraction of legal principles
    text: "Given a court decision, the task is to find the passages where the court states a principle of law or a general interpretation."
- key: legal-argumentation
  title: Legal argumentation
  icon: landmark
  question: "How do courts justify their decisions, and can a computer trace that reasoning?"
  summary: "Argument mining finds the premises and conclusions in a text and the links between them. In law, it gives structured access to the reasoning of courts."
  tasks:
  - name: Argument component classification
    text: "Given the sentences of a court decision, the task is to find the argumentative ones. Each argument component is then classified as a premise, which gives a reason, or a conclusion, which follows from the premises."
  - name: Premise type classification
    text: "Given a premise, the task is to classify it as factual, legal, or both. A factual premise describes events of the case, while a legal premise states rules, precedents, or principles."
  - name: Argument scheme classification
    text: "Given a legal premise, the task is to assign one or more argument schemes, such as rule, precedent, or principle. An argument scheme is a typical pattern of reasoning."
  - name: Argument structure prediction
    text: "Given pairs of argument components, the task is to predict whether they are linked. For linked pairs, the task is to say whether one supports or attacks the other."
- key: outcome-prediction
  title: Predicting outcomes
  icon: gavel
  question: Can the text of a case indicate how the court will decide?
  summary: "Outcome prediction links the text of a case to the final decision of the court. Studies rely either on features that describe the case or on the text of the decisions."
  tasks:
  - name: Judgment outcome prediction
    text: "Given the description of a case or an appeal, the task is to predict whether the court approves or dismisses it."
  - name: Request outcome prediction
    text: "Given a request by a party, with its claims and arguments, the task is to predict whether the court upholds or rejects that request."
  - name: Violation prediction
    text: "Given a decision of the European Court of Human Rights, the task is to predict whether the court found a violation. A violation is a breach of an article of the European Convention on Human Rights."
  - name: Unanimity prediction
    text: "Given the description of a case, the task is to predict whether the judges reached the decision unanimously."
- key: consumer-protection
  title: Protecting consumers
  icon: user-shield
  question: "Which terms in online contracts and privacy policies may harm consumers?"
  summary: "Consumers rarely read terms of service, the contracts that govern online services. Systems flag clauses that may be unfair and check privacy policies against data protection law."
  tasks:
  - name: Unfair clause detection
    text: "Given a sentence from a terms of service document, the task is to say whether it contains a potentially unfair clause. A clause is unfair when it creates a significant imbalance in rights and obligations, to the detriment of the consumer."
  - name: Unfairness category classification
    text: "Given a potentially unfair clause, the task is to assign its category, such as limitation of liability or unilateral termination. Some datasets also grade each clause as clearly fair, potentially unfair, or clearly unfair."
  - name: Explaining unfairness
    text: "Given a clause classified as unfair, the task is to retrieve the legal rationales that explain why it may be unfair. Rationales are short justifications written by legal experts."
  - name: Privacy policy assessment
    text: "Given a privacy policy, the task is to check each clause against the General Data Protection Regulation (GDPR), the EU data protection law. The check covers required information, lawful processing, and clear language."
  - name: Data practice identification
    text: "Given a privacy policy, the task is to identify the data processing practices it describes, such as data collection, transfer, and sharing."
- key: multilingual
  title: Working across languages
  icon: language
  question: How can legal language tools work beyond English?
  summary: "Most legal language tools are built for English, while the European Union works in 24 official languages. Researchers transfer annotations, translate documents, and compare models on multilingual benchmarks."
  tasks:
  - name: Annotation projection
    text: "Given a document annotated in one language and its version in another language, the task is to transfer the labels onto the matching sentences. The two versions may not be exact translations."
  - name: Transfer through machine translation
    text: "Given legal documents in a new language, the task is to reuse an English system through machine translation. Either the training documents or each query document is translated."
  - name: Cross-lingual transfer
    text: "Given a model trained on one language, the task is to apply it to another language without new labels. It relies on features shared across languages."
  - name: Multilingual benchmarking
    text: "Given a collection of legal datasets in many languages, the task is to compare models with shared aggregate scores."
- key: llms-and-law
  title: Large language models and law
  icon: microchip
  question: "Can large language models handle legal tasks from a few examples?"
  summary: "Large language models (LLMs), such as ChatGPT or GPT-4, can address a task from an instruction and a few examples. Their results on legal tasks are mixed, so studies compare them with smaller models trained on labelled data."
  tasks:
  - name: Prompting for unfair clause detection
    text: "Given a terms of service clause and an instruction, the task is to have an LLM say whether the clause is unfair. The prompt may include a few examples."
  - name: Example selection for legal argument mining
    text: "Given a legal argument mining task and a pool of labelled examples, the task is to choose which examples the LLM sees. The choice can change for each new input."
  - name: LLM annotation for training data
    text: "Given court decisions without labels, the task is to have an LLM label them. A smaller model is then trained on these labels and compared with the LLM."
  - name: Legal benchmarks for LLMs
    text: "Given a shared set of legal tasks written by experts, the task is to measure how well LLMs reason about law with few examples."

# Our focus: the lab topics, shown as a rotating carousel and, below it, one detail box per topic.
# `status` is done (Explored), now (Current), or next (Future).
# `text` is the bullet on the card, and `detail` explains it in the detail box.
# `cite` lists publication folder names; Explored objectives show them on the right of the detail box.
focus:
- key: argumentation
  title: Legal argumentation
  icon: sitemap
  summary: "We study how machines can find and classify the arguments that courts write in their decisions. This gives structured access to the reasoning behind a judgment."
  description: "Argument mining is the automatic detection of arguments and their parts in text. In a court decision, a premise is a reason, and a conclusion is the point the court reaches from it. Premises can be legal, such as a rule or a precedent, or factual, such as an event in the case. An argument scheme is the pattern of reasoning that a legal premise follows, such as reasoning from a precedent. We ask whether models can recover these parts and their links, and whether similar decisions share similar arguments."
  items:
  - status: done
    text: Demosthenes, a corpus of arguments in EU court decisions.
    detail: "We present Demosthenes, a corpus of 40 decisions of the Court of Justice of the European Union on fiscal state aid. The annotation marks argumentative elements, their types, and their argument schemes on three levels. We define four classification tasks and test language models and traditional classifiers on them."
    cite:
    - grundler-etal-2022-cjeu-arguments
  - status: done
    text: Predicting the links between legal arguments.
    detail: "Argument structure prediction finds the relations between arguments or their parts. We add a new annotation layer of links to Demosthenes, with types such as support, rebuttal, and undercut. In our experiments, an ensemble of residual networks gives the best results."
    cite:
    - 10-1145-3594536-3595174
  - status: done
    text: A challenge on arguments in Italian tax decisions.
    detail: "AMELIA is a challenge with three classification tasks on 225 Italian decisions on Value Added Tax. The tasks label each component as premise or conclusion, each premise as legal or factual, and each legal premise by its argument scheme. Since the classes are highly unbalanced, evaluation uses the macro F1 score."
    cite:
    - grundler-etal-2024-amelia
  - status: done
    text: Choosing examples for LLMs by similarity to the input.
    detail: "Large language models (LLMs) can learn a task from a few examples given in the prompt, called demonstrations. We compare dynamic selection, which picks new demonstrations for each input, with fixed demonstrations chosen by experts or by the LLM. Over 34 configurations and 3 tasks, dynamic selection performs better, which suggests that similarity is an important criterion."
    cite:
    - alfieri-2025-dynamic
  - status: now
    text: Legal argument mining with LLMs in Italian and English.
    detail: "We compare LLMs and fine-tuned models on the argument mining tasks of Demosthenes and AMELIA. The goal is to see which tasks LLMs handle and where expert-annotated training data is still needed."
  - status: next
    text: Do similar decisions convey similar legal arguments?
    detail: "We plan to measure whether decisions that are similar in content also share premises and argument schemes. This could support the retrieval of relevant arguments and counterarguments for legal practitioners."
- key: prediction
  title: Judgement prediction
  icon: gavel
  summary: "We study whether the text of a decision can tell a model how a court ruled. We also ask which parts of the text carry that information."
  description: "Judgement prediction, also called outcome prediction, is the automatic prediction of the decision of a judge. Here the input is the text of a judicial decision and the output is whether a request is upheld or rejected. A request is upheld when the court accepts it, and rejected when the court refuses it. We ask which parts of a decision, such as the claims and arguments of the parties, are most informative for this task."
  items:
  - status: done
    text: Predicting outcomes of Italian tax decisions.
    detail: "We present a new corpus of 226 annotated decisions on Value Added Tax by Italian Regional Tax law commissions. We predict whether each request is upheld or rejected in the final decision. We test traditional classifiers with TF-IDF and Sentence-BERT representations to find which parts of a decision are most informative."
    cite:
    - galli-etal-2022-outcomes
  - status: now
    text: Predicting outcomes from what the parties submit.
    detail: "Our current predictions use the narrative that the court writes. We aim to add the information that the parties provide before the case, which is closer to a realistic prediction setting."
  - status: next
    text: Neural models and legal embeddings for outcome prediction.
    detail: "We plan to test more advanced neural architectures and embeddings trained on legal text. We also plan to balance the classes with oversampling or data augmentation."
- key: interpretability
  title: Interpretability
  icon: lightbulb
  summary: "We build models that explain their decisions with the reasons a legal expert would give. This helps users check a prediction and trust the tool."
  description: "A model is interpretable when people can understand why it gives a certain output. A legal rationale is a short justification, written by legal experts, of why a clause is unfair. A memory-augmented neural network stores such texts in an external memory and uses them while it classifies. We ask whether rationales can explain predictions to users without lowering accuracy."
  items:
  - status: done
    text: "Memory networks that explain unfairness with legal rationales."
    detail: "We link the unfair clauses of a corpus of Terms of Service to a knowledge base of legal rationales. Memory-augmented neural networks use these rationales as context knowledge. The rationales improve classification accuracy and offer natural language explanations of otherwise opaque outcomes."
    cite:
    - lagioia-etal-2019-detecting
    - ruggeri-etal-2022-detecting
  - status: done
    text: "Explanations of unfairness for consumers in the CLAUDETTE tool."
    detail: "We extend CLAUDETTE, a tool that detects potentially unfair clauses in online Terms of Service. The tool now shows users the legal rationales of unfairness for five categories. These are arbitration, unilateral change, content removal, unilateral termination, and limitation of liability."
    cite:
    - liepina-etal-2022-claudette
  - status: done
    text: "Transformers that explain their output with stored explanations."
    detail: "We extend transformer models with external memories that store explanations in natural language. The model uses them to explain its classification outputs. Tests on legal text analysis and argument mining show relevant explanations, with classification performance kept or improved."
    cite:
    - ruggeri-etal-2024-combining
  - status: now
    text: Retrieving legal rationales to guide LLMs.
    detail: "Retrieval-augmented generation lets an LLM read relevant documents before it answers. We study this approach with legal rationales as the external knowledge base for unfair clause detection."
  - status: next
    text: Explanations of unfairness in several languages.
    detail: "We plan to attach legal rationales as explanations of unfairness in a multilingual setting. This would bring explanations to consumers who read Terms of Service in languages other than English."
- key: unfairness
  title: Unfair clause detection
  icon: file-contract
  summary: "We build systems that find clauses in online contracts and privacy policies that may harm consumers. Few people read these documents, so automatic tools can help consumers and lawyers."
  description: "Terms of Service are the contracts that govern the relation between an online platform and its users. A clause is potentially unfair when it may break consumer protection law, for instance by letting the provider change the contract alone. Unfair clause detection finds such clauses, and classification assigns each one to a category of unfairness. We ask how well machine learning, from traditional classifiers to LLMs, performs on this task and on related checks of privacy policies."
  items:
  - status: done
    text: CLAUDETTE, a detector of potentially unfair clauses.
    detail: "We annotate a corpus of 50 online Terms of Service with eight categories of potentially unfair clauses. We train classifiers that detect these clauses and assign them to categories. A public web server, CLAUDETTE, lets users submit a document and inspect the output."
    cite:
    - lippi-2019-claudette
  - status: done
    text: Checking privacy policies against the GDPR.
    detail: "The General Data Protection Regulation (GDPR) is the EU law on personal data. We define a methodology to assess privacy policies under its provisions, and we analyse the policies of 14 online platforms and services. The resulting annotated corpus supports machine learning systems that check compliance and adequacy."
    cite:
    - contissa-2018-automated
  - status: done
    text: Comparing LLMs with fine-tuned models on unfair clauses.
    detail: "We compare several prompt strategies on five small LLMs and two larger LLMs against fine-tuned BERT-based models. Small LLMs fall short of satisfactory performance on this task. At this stage, BERT-based models remain superior for detecting and classifying unfair clauses."
    cite:
    - 2025worth
  - status: done
    text: Detecting vague clauses in Italian privacy policies.
    detail: "We detect vague clauses in Italian privacy policies. We compare transformers, LLMs, and cross-lingual techniques."
    cite:
    - grundler-2025-detecting
  - status: now
    text: Fine-tuning LLMs on legal contracts.
    detail: "We test parameter-efficient fine-tuning, which trains only a small part of an LLM, on our data and on other legal corpora. The goal is to close the gap between LLMs and fine-tuned BERT-based models."
  - status: next
    text: Keeping annotations up to date when the law changes.
    detail: "We plan to refine annotation guidelines and labels automatically when the legislation changes. Memory networks and retrieval-augmented generation are possible ways to do this."
- key: summarization
  title: Summarization
  icon: align-left
  summary: "We ask whether machines can summarize legal documents by following given guidelines. We also ask whether these summaries are useful to legal experts."
  description: "Summarization is the automatic production of a shorter text that keeps the main content of a longer one. Guided summarization follows instructions on what the summary must contain, such as the outcome of a case or its key arguments. Legal documents are long and structured, and experts need summaries they can rely on. We ask how to produce such summaries and how to evaluate them with legal experts."
  items:
  - status: now
    text: Summaries of court decisions guided by their arguments.
    detail: "We study whether the argumentative structure of a decision, such as its premises and conclusions, can guide what a summary keeps."
  - status: next
    text: Asking legal experts whether summaries are useful.
    detail: "We plan to evaluate generated summaries with legal experts, using explicit criteria for each quality of a summary. This would show whether summaries help in practice and not only on automatic metrics."
- key: crosslinguality
  title: Cross-linguality
  icon: globe-europe
  summary: "We study how to move legal annotations and models from one language to another. In the European Union, the same document often exists in several languages."
  description: "Cross-linguality is the use of data or models in one language to solve a task in another language. Annotation projection copies the labels of a document onto its version in another language. The two versions are often not exact translations, so sentences do not match one to one. We ask whether projection or machine translation can replace the costly annotation of a new corpus for each language."
  items:
  - status: done
    text: Projecting labels between English and German documents.
    detail: "We present the first English-German parallel corpus for unfair clause detection in privacy policies and Terms of Service. The corpus is asymmetric, so the two versions do not match sentence by sentence. Among language-agnostic projection methods, word embeddings combined with dynamic time warping perform best."
    cite:
    - galassi-etal-2020-cross
  - status: done
    text: Unfair clause detection in four languages.
    detail: "We extend our corpus to 50 contracts in each of English, German, Italian, and Polish. We compare new corpora per language, projected annotations, translated training documents, and translation at prediction time. Building a new annotated corpus for each language can often be avoided with no significant loss in performance."
    cite:
    - 10-1007-s-10506-024-09398-7
  - status: done
    text: LEXTREME, a multilingual benchmark for legal NLP.
    detail: "LEXTREME gathers 11 datasets covering 24 languages, including a corpus of Terms of Service in four languages from the CLAUDETTE project. Two aggregate scores compare models across datasets and across languages. Even the best baseline achieves only modest results, so the benchmark leaves ample room for improvement."
    cite:
    - niklaus-etal-2023-lextreme
  - status: now
    text: Multilingual embeddings for clause detection.
    detail: "Multilingual embeddings place texts in different languages in one shared space. We use them to capture relations across language versions of the same contract."
  - status: next
    text: LLMs on multilingual legal corpora.
    detail: "We plan to test LLMs on the multilingual CLAUDETTE corpora. This would show whether LLMs reduce the need for translation or projection."
- key: decisions
  title: Reading court decisions
  icon: file-alt
  summary: "We study how machines can find the parts and key statements of a court decision. Legal experts are few and costly, so we also study how to build training data with less of their time."
  description: "A court decision has functional parts, such as the facts, the arguments of the parties, and the ruling. Rhetorical role prediction labels each sentence with the part it belongs to. Legal named entity recognition finds names such as the petitioner, the court, or the statute. Some sentences state general principles that later decisions cite, which the Court of Justice of the European Union expresses as judicial interpretative formulas. We ask how to find these elements and how to train models when labelled data are scarce."
  items:
  - status: done
    text: "Rhetorical roles and legal entities in Indian court decisions."
    detail: "We take part in the LegalEval shared task on Indian legal documents. A context-aware model adds information from nearby sentences and reaches 81.12% micro-F1 on rhetorical role prediction. For legal named entity recognition, a model based on XLNet with a dependency parser reaches 87.43% macro-F1."
    cite:
    - noviello-etal-2023-teamunibo
  - status: done
    text: "Data augmentation for sentences that state principles of law."
    detail: "Data augmentation creates new training examples from existing ones. We replace words with candidates from WordNet, a lexical database, and pick the one closest in GloVe word embeddings. On decisions of the Court of Justice of the European Union, legal experts judge this method more robust than the alternatives."
    cite:
    - percin-etal-2022-combining
  - status: done
    text: Extracting interpretative formulas from EU tax decisions.
    detail: "Judicial interpretative formulas are general statements of the Court of Justice of the European Union that later decisions cite. We define annotation guidelines and label 21 decisions on VAT by experts, plus 80 decisions labelled by LLMs for training. BERT-based models trained on this data perform comparably to LLMs."
    cite:
    - grundler-2025-automated
  - status: now
    text: Balancing scarce legal datasets.
    detail: "Many of our legal datasets have highly unbalanced classes. We study oversampling and data augmentation to give models enough examples of rare classes."
  - status: next
    text: Rhetorical roles in EU and Italian decisions.
    detail: "We plan to label the functional parts of EU and Italian decisions. These parts could then guide argument mining, outcome prediction, and summarization."
---
