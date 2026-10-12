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
# a `type` (text, textarea, select, number, a whole number from 0 with a counter, or month, a month and year written as
# "March 2027"), an optional `when` that shows the field only when another field has a value, such
# as {funding: I need funding from the lab}, or `when_more`, which shows it only when a number field is above a value,
# such as {exams: 0}, `options` (a list for a select, or `proposals`, which lists the research proposals
# in a select and lets "Choose this proposal" fill a text field), `required`, and, for a month, an optional `after` list, such as
# [{field: start, months: 6, message: "..."}]: each rule blocks the email, showing its message, until the month is at
# least that many months after the named field (0 months: not before it). A hidden or empty field is skipped. Every form also asks for the sender's name.
paths:
  - key: thesis
    label: Master thesis
    summary: "A research thesis on one of our proposals, for master students of the University of Bologna."
    icon: graduation-cap
    title: Master thesis
    who: "Master students of the University of Bologna. Most come from the [Master's degree in Artificial Intelligence](https://corsi.unibo.it/2cycle/artificial-intelligence), but other degrees are welcome."
    what: "A master thesis is a research activity on one of our research proposals, supervised by the lab members that the proposal names."
    steps:
      - title: Choose a proposal
        text: "Open a proposal to read its description and supervisors, then select **Choose this proposal**."
        show: proposals
      - title: Write to us
        text: "Tell us how many exams you still have to pass and when you expect to finish them, when you can start, and the degree session in which you intend to graduate. We reserve at least six months for a thesis, so the session must be at least six months after your start, and not before the end of your exams. You may start before your last exam."
        show: contact
    inspiration: student-work
    form:
      subject: "[Master thesis] {proposal}"
      fields:
        - {key: proposal, label: Proposal, type: select, options: proposals, required: true}
        - {key: exams, label: Exams still to pass, type: number, required: true}
        - {key: exams_end, label: Estimated period to finish remaining exams, type: month, when_more: {exams: 0}, required: true}
        - {key: start, label: Available to start, type: month, required: true}
        - {key: session, label: Intended degree session, type: month, required: true, after: [{field: start, months: 6, message: "We reserve at least six months for a thesis: choose a session at least six months after your start."}, {field: exams_end, months: 0, message: "Choose a session no earlier than the end of your remaining exams."}]}
        - {key: message, label: Message, type: textarea}
  - key: project
    label: NLP project work
    summary: "A 3 CFU project for the Master's degree in Artificial Intelligence, on our proposals or on a topic of your own."
    icon: tools
    title: Project work
    who: "Students of the University of Bologna enrolled in the [Master's degree in Artificial Intelligence](https://corsi.unibo.it/2cycle/artificial-intelligence)."
    what: "A project work is a 3 CFU activity. You can choose one of our research proposals or propose a topic of your own."
    steps:
      - title: Read the course pages
        text: "The [course page](https://www.unibo.it/en/study/course-units-transferable-skills-moocs/course-unit-catalogue/course-unit/2026/530679) and the [Virtuale page](https://virtuale.unibo.it/course/view.php?id=81838) describe the project work and how it is assessed."
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
    what: "A student visit typically lasts between three and six months."
    steps:
      - title: Find a research topic
        text: "Our research proposals show the topics we currently work on."
        show: proposals
      - title: Write to us
        text: "Agree with us on the visit and its research topic. Tell us how the visit is funded: by your home institution, or by the lab, and in that case how much funding you need. Researchers attach a curriculum vitae, a research statement, and a proposal for the research activity during the visit."
        show: contact
      - title: Complete the formalities
        text: "Students complete the required formalities with the administrations of their home institution and of the University of Bologna."
    form:
      subject: "[{role}] Application"
      fields:
        - {key: role, label: I am applying as, type: select, options: [Visiting student, Visiting researcher], required: true}
        - {key: institution, label: Home institution, type: text, required: true}
        - {key: topic, label: Research topic of the visit, type: textarea, required: true}
        - {key: funding, label: Funding, type: select, options: [Funded by my home institution, I need funding from the lab], required: true}
        - {key: amount, label: Funding needed from the lab, type: text, required: true, when: {funding: I need funding from the lab}}
  - key: programme
    label: Master or PhD
    summary: "Admission to a master or PhD programme of the University of Bologna, to work with the lab."
    icon: university
    title: Master or PhD programme
    who: "Students who intend to enroll in a master or PhD programme at the University of Bologna and to work with the lab."
    what: "Admission follows the official procedures of the University of Bologna."
    steps:
      - title: Apply
        text: "Follow the [admission page of the Master's degree in Artificial Intelligence](https://corsi.unibo.it/2cycle/artificial-intelligence/admission) or the [application page of the PhD in Computer Science and Engineering](https://phd.unibo.it/cse/en/apply)."
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
