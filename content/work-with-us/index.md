---
title: Work with us
date: 2026-09-28

# The old For Students page now lives here.
aliases:
  - /students/
  - /students_publications/

# Intro: shown under the title. Markdown.
intro: |
  We welcome students and researchers who want to work on natural language processing with us.
  Choose what you are looking for: each option explains who can apply and lets you write to us directly.

# Contacts: the people who receive every message, as folder names in content/authors, whose `email` is used.
# A path may set its own `contacts`.
contacts: [paolo-torroni, andrea-galassi, federico-ruggeri]

# Paths: one tab each. A path has a `key` (its anchor, such as /work-with-us/#thesis), a tab `label`, an `icon`
# (Font Awesome 5 solid), a `title`, and Markdown `who`, `what`, `steps`, and an optional `note`.
# `form` sets the email: `subject` may name fields in braces, such as {proposal}; each field has a `key`, a `label`,
# a `type` (text, textarea, or select), `options` for a select (a list, or `proposals` for the research proposals),
# and `required`. Every form also asks for the sender's name.
# `show` lists the sections below the card that the path opens: proposals, student-work, or projects.
paths:
  - key: thesis
    label: A master thesis
    icon: graduation-cap
    title: Master thesis
    who: "Students of the University of Bologna enrolled in the [Master's degree in Artificial Intelligence](https://corsi.unibo.it/2cycle/artificial-intelligence)."
    what: "A master thesis is a research activity on one of our research proposals, supervised by the lab members that the proposal names."
    steps:
      - "Choose a proposal from the research proposals below."
      - "Write to us with the form, stating how many exams you still have to pass and the degree session in which you intend to graduate."
    note: "Please contact us at least six months before your intended degree session."
    form:
      subject: "[Master thesis] {proposal}"
      fields:
        - {key: proposal, label: Proposal, type: select, options: proposals, required: true}
        - {key: exams, label: Exams still to pass, type: text, required: true}
        - {key: session, label: Intended degree session, type: text, required: true}
        - {key: message, label: Message, type: textarea}
    show: [proposals, student-work]
  - key: project
    label: An NLP project work
    icon: tools
    title: Project work
    who: "Students of the University of Bologna enrolled in the [Master's degree in Artificial Intelligence](https://corsi.unibo.it/2cycle/artificial-intelligence)."
    what: "A project work is a 3 CFU activity. You can choose one of our research proposals or propose a topic of your own."
    steps:
      - "Choose a topic, from the research proposals below or of your own."
      - "Write to us with the form, describing the topic and your intended approach."
    form:
      subject: "[Project work] {topic}"
      fields:
        - {key: topic, label: Topic, type: text, required: true}
        - {key: approach, label: Intended approach, type: textarea, required: true}
    show: [proposals, student-work]
  - key: visiting
    label: A visiting period
    icon: plane
    title: Visiting student or researcher
    who: "Master and PhD students enrolled at another institution, and researchers affiliated with another institution."
    what: "A student visit typically lasts between three and six months, and its funding is expected from the home institution. Funding for a researcher visit is expected from the applicant."
    steps:
      - "Write to us with the form, to agree on the visit and its research topic."
      - "Researchers attach a curriculum vitae, a research statement, and a proposal for the research activity during the visit."
      - "Students then complete the required formalities with the administrations of their home institution and of the University of Bologna."
    form:
      subject: "[{role}] Application"
      fields:
        - {key: role, label: I am applying as, type: select, options: [Visiting student, Visiting researcher], required: true}
        - {key: institution, label: Home institution, type: text, required: true}
        - {key: topic, label: Research topic of the visit, type: textarea, required: true}
    show: [proposals]
  - key: programme
    label: A master or PhD place
    icon: university
    title: Master or PhD programme
    who: "Students who intend to enroll in a master or PhD programme at the University of Bologna and to work with the lab."
    what: "Admission follows the official procedures of the University of Bologna: see the [admission page of the Master's degree in Artificial Intelligence](https://corsi.unibo.it/2cycle/artificial-intelligence/admission) and the [application page of the PhD in Computer Science and Engineering](https://phd.unibo.it/cse/en/apply)."
    steps:
      - "Write to us before applying, to discuss your research interests."
    form:
      subject: "[Prospective student] {programme}"
      fields:
        - {key: programme, label: Programme, type: select, options: [Master's degree in Artificial Intelligence, PhD in Computer Science and Engineering], required: true}
        - {key: interests, label: Research interests, type: textarea, required: true}
    show: [student-work]
  - key: partnership
    label: A project partnership
    icon: handshake
    title: Project partnership
    who: "Companies, public institutions, and research groups that want to start a research project with us."
    what: "We take part in national and international research projects. The most recent ones are listed below, and the [Projects](/projects/) page lists all of them."
    steps:
      - "Write to us with the form, describing your organisation and your idea."
    form:
      subject: "[Partnership] {organisation}"
      fields:
        - {key: organisation, label: Organisation, type: text, required: true}
        - {key: idea, label: Your idea, type: textarea, required: true}
    show: [projects]
---
