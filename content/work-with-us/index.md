---
title: Work with us
date: 2026-09-28

# The old For Students page now lives here.
aliases:
  - /students/
  - /students_publications/

# Contacts: the people who receive every message, as folder names in content/authors, whose `email` is used.
# A path may set its own `contacts`.
contacts: [paolo-torroni, andrea-galassi, federico-ruggeri]

# Paths: one card each under "What are you looking for?". A path has a `key` (its anchor, such as /work-with-us/#thesis),
# a card `label` and `summary` (at most two sentences), an `icon` (Font Awesome 5 solid), a `title`, and Markdown `who`
# and `what`. Its `steps` are numbered in order: each has a `title`, Markdown `text`, and an optional `show`, which places
# a section in the step: proposals, projects, or contact (the email form). `inspiration: student-work` adds a last,
# unnumbered step with the work done with students.
# `form` sets the email: `subject` may name fields in braces, such as {proposal}; each field has a `key`, a `label`,
# a `type` (text, textarea, or select), `options` (a list for a select, or `proposals`, which lists the research proposals
# in a select and lets "Choose this proposal" fill a text field), and `required`. Every form also asks for the sender's name.
paths:
  - key: thesis
    label: Master thesis
    summary: "A research thesis for the Master's degree in Artificial Intelligence, on one of our proposals."
    icon: graduation-cap
    title: Master thesis
    who: "Students of the University of Bologna enrolled in the [Master's degree in Artificial Intelligence](https://corsi.unibo.it/2cycle/artificial-intelligence)."
    what: "A master thesis is a research activity on one of our research proposals, supervised by the lab members that the proposal names."
    steps:
      - title: Choose a proposal
        text: "Open a proposal to read its description and supervisors, then select **Choose this proposal**."
        show: proposals
      - title: Write to us
        text: "State how many exams you still have to pass and the degree session in which you intend to graduate. Please contact us at least six months before that session."
        show: contact
    inspiration: student-work
    form:
      subject: "[Master thesis] {proposal}"
      fields:
        - {key: proposal, label: Proposal, type: select, options: proposals, required: true}
        - {key: exams, label: Exams still to pass, type: text, required: true}
        - {key: session, label: Intended degree session, type: text, required: true}
        - {key: message, label: Message, type: textarea}
  - key: project
    label: NLP project work
    summary: "A 3 CFU project for the Master's degree in Artificial Intelligence, on our proposals or on a topic of your own."
    icon: tools
    title: Project work
    who: "Students of the University of Bologna enrolled in the [Master's degree in Artificial Intelligence](https://corsi.unibo.it/2cycle/artificial-intelligence)."
    what: "A project work is a 3 CFU activity. You can choose one of our research proposals or propose a topic of your own."
    steps:
      - title: Choose a topic
        text: "Select **Choose this proposal** on one of our research proposals, or write a topic of your own in the next step."
        show: proposals
      - title: Write to us
        text: "Describe the topic and your intended approach."
        show: contact
    inspiration: student-work
    form:
      subject: "[Project work] {topic}"
      fields:
        - {key: topic, label: Topic, type: text, options: proposals, required: true}
        - {key: approach, label: Intended approach, type: textarea, required: true}
  - key: visiting
    label: Visiting period
    summary: "A research stay of a few months, for students and researchers of another institution."
    icon: plane
    title: Visiting student or researcher
    who: "Master and PhD students enrolled at another institution, and researchers affiliated with another institution."
    what: "A student visit typically lasts between three and six months, and its funding is expected from the home institution. Funding for a researcher visit is expected from the applicant."
    steps:
      - title: Find a research topic
        text: "Our research proposals show the topics we currently work on."
        show: proposals
      - title: Write to us
        text: "Agree with us on the visit and its research topic. Researchers attach a curriculum vitae, a research statement, and a proposal for the research activity during the visit."
        show: contact
      - title: Complete the formalities
        text: "Students complete the required formalities with the administrations of their home institution and of the University of Bologna."
    form:
      subject: "[{role}] Application"
      fields:
        - {key: role, label: I am applying as, type: select, options: [Visiting student, Visiting researcher], required: true}
        - {key: institution, label: Home institution, type: text, required: true}
        - {key: topic, label: Research topic of the visit, type: textarea, required: true}
  - key: programme
    label: Master or PhD place
    summary: "Admission to a master or PhD programme of the University of Bologna, to work with the lab."
    icon: university
    title: Master or PhD programme
    who: "Students who intend to enroll in a master or PhD programme at the University of Bologna and to work with the lab."
    what: "Admission follows the official procedures of the University of Bologna."
    steps:
      - title: Write to us
        text: "Discuss your research interests with us before applying."
        show: contact
      - title: Apply
        text: "Follow the [admission page of the Master's degree in Artificial Intelligence](https://corsi.unibo.it/2cycle/artificial-intelligence/admission) or the [application page of the PhD in Computer Science and Engineering](https://phd.unibo.it/cse/en/apply)."
    inspiration: student-work
    form:
      subject: "[Prospective student] {programme}"
      fields:
        - {key: programme, label: Programme, type: select, options: [Master's degree in Artificial Intelligence, PhD in Computer Science and Engineering], required: true}
        - {key: interests, label: Research interests, type: textarea, required: true}
  - key: partnership
    label: Project partnership
    summary: "A national or international research project with a company, a public institution, or a research group."
    icon: handshake
    title: Project partnership
    who: "Companies, public institutions, and research groups that want to start a research project with us."
    what: "We take part in national and international research projects."
    steps:
      - title: See our recent projects
        text: "The [Projects](/projects/) page lists all of them."
        show: projects
      - title: Write to us
        text: "Describe your organisation and your idea."
        show: contact
    form:
      subject: "[Partnership] {organisation}"
      fields:
        - {key: organisation, label: Organisation, type: text, required: true}
        - {key: idea, label: Your idea, type: textarea, required: true}
---
