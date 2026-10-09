---
title: Improving the Teaching of Artificial Intelligence Through Project-Based Learning
  on a Board Game

# Authors
# A YAML list of author names
# If you created a profile for a user (e.g. the default `admin` user at `content/authors/admin/`), 
# write the username (folder name) here, and it will be replaced with their full name and linked to their profile.
authors:
- Allegra De Filippo
- Andrea Galassi
- Alessandro Soriani
- Giada Trisolini
- Federico Baldo
- Federico Chesani
- Paola Mello
- Michela Milano

# Author notes (such as 'Equal Contribution')
# A YAML list of notes for each author in the above `authors` list
author_notes: []

date: '2025-01-01'

# Date to publish webpage (NOT necessarily Bibtex publication's date).
publishDate: '2026-03-02T12:28:22.087802Z'

# Publication type.
# A single CSL publication type but formatted as a YAML list (for Hugo requirements).
publication_types:
- article-journal

# Publication name and optional abbreviated publication name.
publication: '*Intelligenza Artificiale*'
publication_short: ''

doi: 10.1177/17248035241297789

abstract: "Traditional university lessons do not provide students with the opportunity to put theoretical concepts into practice. Project-Based Learning is designed to involve students through the proposition of real-word problems in the form of a project. The main objective of this work is to improve several aspects of the student’s learning experience (e.g., their motivation and interest) through practical experience during a master degree course in Artificial Intelligence. We propose an application of Project-Based Learning through the use of a game-based competition. The experience is designed as an activity that takes place in parallel with respect to the usual lessons. Then, we assessed the significance and the impact of this approach, from the educational point of view, through questionnaires proposed to the students involved. The results of a 3-year study involving more than 200 students are positive. Students reacted favorably to the experience: they think this experience improved their knowledge of AI, their motivation, and their skills. The competitive aspect is considered beneficial from multiple perspectives. Finally, the design of the experience seems to be robust and remains effective in a setting of remote lectures."

# Summary. An optional shortened abstract.
summary: Over three years, 244 master students built AI players for the board game Tablut, and they report gains in AI knowledge, motivation, and teamwork.

tags:
- project-based learning
- artificial intelligence teaching
- game-based competition
- tablut
- higher education

topics: []

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
  caption: "Initial setup of Tablut, the board game of the competition, redrawn from Figure 1 of the paper."
  focal_point: ''
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects: ['internal-project']` links to `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []
categories:
  - Journal
aliases:
  - /publication_journals/de-2025-improving/
---

## Research setting

The paper studies how to teach Artificial Intelligence (AI) to master students with a practical project.
It applies Project-Based Learning (PBL), a teaching approach in which students learn by working, alone or in groups, on a real problem that ends in a product.
Here the problem is a game: each team writes an AI player for Tablut, an ancient Nordic board game, and the players then face each other in a competition.
Tablut is played on a 9 x 9 board by two players with different roles, and each AI player must be able to play both roles.

Tablut suits a first AI course for three reasons given in the paper.
Both players see the whole board and no move depends on chance, so simple state-space search, the exploration of possible future board positions, can play it.
It is asymmetric, because the two sides start with different checkers and goals, as the board at the top of this page shows.
It is also little studied and still unsolved, so students cannot copy a known solution.

{{< pipeline caption="What an AI player for Tablut does at each turn, following the requirements in Section 4.2 of the paper." >}}
- title: Board state
  text: The player receives the current position.
  icon: chess-board
- title: Decide
  text: For example, by searching possible future positions.
  icon: project-diagram
  highlight: true
- title: Legal move
  text: It returns a move that follows the rules.
  icon: chess-knight
{{< /pipeline >}}

## Motivation

University AI lessons are mostly lectures, which leave students few chances to put theory into practice.
Competitions can raise interest and motivation.
They can also cause stress and performance anxiety, or draw attention away from the regular course.
An earlier edition of this experience used the game Nine Men's Morris, and its students asked for a less-known game and for freedom in the programming language.

{{< gap caption="How this study extends the earlier edition of the experience, as described in Sections 2.2 and 4.1 of the paper." >}}
label: Study
columns: [Asymmetric game, Any programming language, Courses and iterations, Students analyzed, Remote lectures analyzed]
rows:
  - name: Earlier edition on Nine Men's Morris (Chesani et al., 2017)
    cells: [false, false, "1 course, 3 iterations", "36", "not discussed"]
  - name: This paper (Tablut competition)
    ours: true
    cells: [true, true, "2 courses, 6 iterations", "166 answers", true]
{{< /gap >}}

> **Objective.** Improve the learning experience of AI students, such as their motivation and interest, through a project run as a game competition, and measure its effects on knowledge, motivation, soft skills, and the competitive aspect.

## Approach

The experience runs within the course Fundamentals of Artificial Intelligence, for a Master Degree in Computer Engineering and a Master Degree in AI at the University of Bologna.
Participation is voluntary, in teams of at most 4 students, and finishing the activity gives a bonus of about 7% on the final course score.

{{< pipeline caption="How one semester of the experience unfolds (Section 4.2 of the paper)." >}}
- title: Launch
  text: Introduced about 4 weeks into the course.
  icon: flag
- title: Build a player
  text: Teams code their AI player in 6 to 8 weeks.
  icon: code
  highlight: true
- title: Validation
  text: Staff checks that every player works.
  icon: check-circle
- title: Matches
  text: Two round-robin groups, then a final.
  icon: trophy
- title: Results lesson
  text: Teams present their work, and winners are announced.
  icon: chalkboard-teacher
{{< /pipeline >}}

In the round-robin groups, each player meets every other player twice, once as attacker and once as defender.
Each game runs as three processes: two players and a Java server that acts as game engine and referee.
Players run inside virtual machines with the same fixed resources, which makes the comparison fair.

{{< svg src="arch.svg" caption="How a game is run (Section 4.3 of the paper). JSON messages let each team use the programming language it prefers." >}}

To measure the effects, students fill in an anonymous, voluntary questionnaire every semester.
It has 4 groups of 5 statements: knowledge of AI (A), interest and motivation (B), personal skills (C), and competition (D).
During the COVID-19 pandemic, a fifth group (E) asked about remote lectures.
Students rate each statement on a Likert scale from 1 (strongly disagree) to 5 (strongly agree).
A t-test checks whether the answers are statistically significant, and two education researchers group the answers to an open question into categories.

## Results

The experience ran for 6 semesters, from 2019 to 2021.
The results are the average Likert score and the standard deviation for each statement, over all questionnaire answers.

{{< numbers >}}
- value: "244"
  label: students in 85 teams over 6 semesters
- value: "166"
  label: questionnaire answers, about 70% of participants
- value: "4.46"
  label: "agreement that competing promotes motivation and interest (out of 5)"
{{< /numbers >}}

{{< bars caption="Average Likert score from 1 (strongly disagree) to 5 (strongly agree) for a selection of statements; whiskers show one standard deviation. Source: Table 3 of the paper." >}}
metric: Average agreement (Likert scale)
unit: ""
min: 1
max: 5
bars:
  - label: "A1 Consolidates theoretical AI concepts"
    value: "4.34"
    err: "0.73"
  - label: "A4 Teaches new programming concepts"
    value: "3.63"
    err: "1.08"
  - label: "B1 Course assessment before the experience"
    value: "3.93"
    err: "0.87"
  - label: "B2 Course assessment after the experience"
    value: "4.22"
    err: "0.77"
  - label: "C5 Teaches cooperation and teamwork"
    value: "4.30"
    err: "0.95"
  - label: "D1 Competing improves team collaboration"
    value: "4.23"
    err: "0.89"
  - label: "D2 Competing improves collaboration with other teams"
    value: "2.85"
    err: "1.19"
  - label: "D3 Competing promotes motivation and interest"
    value: "4.46"
    err: "0.83"
  - label: "D4 Participation is linked to winning the first prize"
    value: "2.45"
    err: "1.21"
{{< /bars >}}

Students agree that the project consolidates AI concepts and teaches problem solving, but less so programming.
The course assessment rises from 3.93 to 4.22 after the experience, and all five skill statements score above 4.
Competition motivates students and strengthens collaboration inside teams, but not between teams.
For almost all statements in groups A to D the t-test gives a p-value below 0.001; the exception is D2, with a p-value of 0.106.

The pandemic did not change the overall picture.
Comparing answers before and during COVID-19, only three statements differ significantly (p < 0.05), all about organization and collaboration.

| Statement | Before COVID-19 | During COVID-19 | p-value |
|---|---|---|---|
| C4 Knowledge on work organization | 4.40 ± 0.76 | 4.00 ± 1.04 | 0.003 |
| C5 Knowledge on cooperation and teamwork | 4.45 ± 0.82 | 4.16 ± 1.04 | 0.035 |
| D2 Collaboration with other teams | 3.05 ± 1.15 | 2.67 ± 1.21 | 0.038 |

*Average Likert score ± standard deviation (Table 4 of the paper).*

The open question collects suggestions for improvement.
The most frequent ones concern technology, such as the server code (13% of answers), timing and deadlines (11%), and the explanation of the task (10%).
Another 10% of answers only express appreciation for the experience.

## Takeaways

{{< takeaways >}}
- title: A game project teaches AI.
  text: Students agree that building a Tablut player consolidates AI concepts, teaches new ways to solve problems, and builds teamwork and work organization skills.
- title: Competition motivates without the prize.
  text: The statement that competing promotes motivation gets the highest score (4.46 out of 5). The link between participation and the first prize gets a low one (2.45). It does not improve collaboration between teams.
- title: The design works in remote teaching.
  text: Answers before and during COVID-19 are almost the same. Students ask for more time, more discussion with peers and staff, and more laboratory lessons.
{{< /takeaways >}}
