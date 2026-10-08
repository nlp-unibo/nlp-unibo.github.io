# Language Technologies Lab website

This repository holds the source of the [Language Technologies Lab website](https://nlp.unibo.it/).
Every page of the site is a text file in this repository.
When a change is merged, GitHub rebuilds the site with [Hugo](https://gohugo.io/) and the Hugo Blox theme, then publishes it on GitHub Pages.

This guide is written for lab members without web development experience.
Part 1 explains the few ideas you need.
Part 2 gives one recipe for each kind of content, such as a publication or a news item.
Part 3 explains how to publish a change, and Part 4 lists common problems.
Part 5 is a reference for maintainers.

## Contents

- [Part 1. Before you start](#part-1-before-you-start)
- [Part 2. Recipes](#part-2-recipes)
  - [Add a publication](#add-a-publication)
  - [Add a news item](#add-a-news-item)
  - [Add an event](#add-an-event)
  - [Add or update a team member](#add-or-update-a-team-member)
  - [Add a thesis](#add-a-thesis)
  - [Add a research proposal](#add-a-research-proposal)
  - [Add a project](#add-a-project)
  - [Edit the Work with us page](#edit-the-work-with-us-page)
  - [Add a research area](#add-a-research-area)
  - [Add a tool](#add-a-tool)
  - [Edit the homepage or the menu](#edit-the-homepage-or-the-menu)
- [Part 3. Publish your change](#part-3-publish-your-change)
- [Part 4. Common problems](#part-4-common-problems)
- [Part 5. Maintainer reference](#part-5-maintainer-reference)

## Part 1. Before you start

### What you need

You need a GitHub account with write access to this repository.
Ask the maintainer for access if you do not have it.
No installation is required for most changes, because GitHub's website can create and edit files.

### Six ideas that explain the whole site

A **page bundle** is a folder that holds one page.
It contains a file named `index.md` and any image or PDF used only by that page.
For example, a news item lives in `content/news/acl-2026/index.md`.

The **slug** is the name of that folder, such as `acl-2026`.
It becomes part of the web address, so the page above appears at `https://nlp.unibo.it/news/acl-2026/`.
Use lowercase letters, numbers, and hyphens only.
Do not rename a folder after publication, because every existing link to it would break.

The **front matter** is the block at the top of `index.md`, between two lines that contain only `---`.
It stores the page details, such as the title and the date, as `name: value` lines.
The text below the second `---` is the page body.

**Markdown** is the plain-text format of the body.
Write `**bold**` for **bold**, `*italic*` for *italic*, `## Heading` for a heading, `- item` for a list item, and `[text](https://example.org/)` for a link.

A **draft** is a page whose front matter contains `draft: true`.
Drafts appear in a local preview but never on the published site.

A **pull request** is a proposal to change the site.
GitHub checks it automatically, and the site changes only after the pull request is merged.

### Rules for front matter

Front matter uses YAML, which is sensitive to layout.
Follow these rules to avoid most errors.

1. Indent with spaces, never with tabs.
2. Keep the indentation of lists exactly as in the example you copy.
3. Write dates as `YYYY-MM-DD`, for example `2026-05-20`.
4. Put quotes around a value that contains a colon, a hash sign, or other punctuation, for example `title: "LLMs: a survey"`.
5. Never delete either `---` line.

### Two ways to work

The GitHub website is enough for text changes, new pages, and image uploads.
You cannot preview the site there, but the automatic check catches most mistakes.

Your own computer lets you preview every change before publication.
It needs a one-time setup, described in [Work on your computer](#work-on-your-computer).

Each recipe below works in both ways.
The fastest start on the GitHub website is to copy an existing page of the same kind and edit it.

## Part 2. Recipes

Every recipe ends with the same step: publish the change through a pull request, as described in [Part 3](#part-3-publish-your-change).

### Add a publication

Every publication lives in its own folder under `content/publication/`.
A folder name such as `rossi-etal-2026-example` works well: first author, `etal`, year, and one keyword.

```text
content/publication/rossi-etal-2026-example/
├── index.md       the page
├── cite.bib       the BibTeX record behind the Cite button
└── featured.jpg   an optional image
```

1. Create the folder and `index.md`.
   On the GitHub website, open any folder in `content/publication/`, copy its `index.md`, and paste it into a new file named `content/publication/<your-slug>/index.md`.
   On your computer, run `uv run python scripts/site.py new conference rossi-etal-2026-example`.
   Replace `conference` with `journal`, `workshop`, `preprint`, or `publication-highlight` as needed.
2. Fill in the fields in the table below, and delete every `TODO` text.
3. Create `cite.bib` in the same folder and paste the complete BibTeX record.
   Do not add a `note` field with internal ratings, because readers download this file.
4. Remove the `draft: true` line when the entry is ready.

| Field | What to write |
| --- | --- |
| `title` | The paper title, without LaTeX commands such as `\textbf` |
| `authors` | One author per line, starting with `- `. Write lab members exactly as their profile title, for example `Federico Ruggeri`, so that their names appear in bold and link to their profiles |
| `date` and `publishDate` | The publication date as `YYYY-MM-DD` |
| `publication_types` | `article-journal` for a journal paper, `paper-conference` for a conference or workshop paper, `article` for a preprint, or `chapter` for a book chapter |
| `publication` | The full venue name, for example `Proceedings of ACL 2026` |
| `categories` | Exactly one of `Journal`, `Conference`, `Workshop`, or `Preprint`, which sets its type in the filter of the Publications page. Add `Highlight` as a second value to also show the paper in the Highlights carousel |
| `abstract` | The abstract, shown in full on the publication page |
| `summary` | One sentence shown under the title of the publication page and on publication cards |
| `card_summary` | Optional sentence of at most 15 words that replaces the summary on the homepage preprint card |
| `doi` | The DOI without `https://doi.org/`, for example `10.18653/v1/2024.argmining-1.7` |
| `url_pdf`, `url_code`, `url_dataset` | Optional links that appear as buttons |
| `award` | Optional award name, for example `Best Paper Award`. It appears with a trophy under the title in every publication list |
| `tags` | Topic keywords. Add `student publication` to list the paper under "Work done with students" on the Work with us page |

Each publication page is a project page, like the pages that research groups publish for their papers.
It shows the title, the authors, the research topics, link buttons, a teaser, the body sections, and the citation.
The page is self-contained, so its text cites no other publication; its tags link to the tag pages.
The page answers four questions for a reader outside the field:

1. What is the paper about?
2. Which research topics does it cover?
3. Why was the work needed, and what did it aim for?
4. What did it find, and what should a reader take away?

Base every statement on the paper, and leave the details to the paper itself.

The template provides five body sections: **Research setting**, **Motivation**, **Approach**, **Results**, and **Takeaways**.
They guide the reader from the task, to the gap in related work, to the method, to the findings.
Never show a number or a term before the text has given its context.
Keep the five sections in every page, so that all pages share one structure.
Each `##` heading also appears in the section menu below the teaser.

| Extra | How to add it |
| --- | --- |
| Teaser and preview | The most representative figure of the paper, saved as `featured.png`. It appears as the teaser and on every publication card. A video named `teaser.mp4` replaces the teaser image on the page |
| Topics | `topics`, one to three keys from `data/topics.yaml`, shown as colored tags; they also feed the topic filter of the Publications page |
| Affiliations | `affiliations`, a list of institution names shown under the authors |
| Buttons | `url_pdf`, `url_code`, `url_dataset`, `url_project` (demo), `url_video`, `url_slides`, `url_poster`, `doi`, and `links` |

The body can use nine visual components.
Each component except `figure` and `svg` takes YAML between its opening and closing tags, and the publication templates show an example of each one.

| Component | Shows |
| --- | --- |
| `figure` | A figure from the paper, saved in the page folder. Reuse a figure only when its source is openly licensed, such as arXiv, the ACL Anthology, or CEUR-WS |
| `svg` | A schema drawn for the page as an SVG file, which follows light and dark mode |
| `gap` | A table that compares the paper with related work, with one row marked `ours: true` |
| `pipeline` | A method diagram with three to five steps, with optional parallel branches inside a step |
| `stages` | An interactive diagram with one tab per stage, which shows whether each component is optimized, trained, or frozen |
| `numbers` | Two to four headline numbers, placed in **Results** after the text that explains them |
| `bars` | An interactive bar chart of one metric, with optional standard deviations and a table view |
| `annotate` | An annotated text example with up to four labels, which readers can filter |
| `takeaways` | Three numbered takeaway cards |

A page without body sections shows only its abstract, so a new entry can be published before its page is complete.

The Publications page (`layouts/publication/section.html`) starts with the Highlights carousel, which loops and advances every eight seconds.
Every publication follows, newest first and grouped by year, with a search box, a filter by type, and a filter by topic.
The topic counts follow the chosen type and the search, and a topic without matches is hidden.
A `Highlight` publication appears both in the carousel and in the list.
Its card shows `featured.png` and the one-sentence `summary`, so give every highlight both.
When the figure is too detailed to read at card size, add a simpler `card.png` (1600 by 1000 pixels, large text) to the same folder: the card shows it, and the page keeps `featured.png` as its teaser.
Leave `featured: false` unchanged, because the Highlight category replaces it.

### Add a news item

1. Create `content/news/<slug>/index.md`, for example `content/news/acl-2026/index.md`.
   Copy an existing news item, or run `uv run python scripts/site.py new news acl-2026`.
2. Set `title`, `date`, and `summary`.
   The summary is the one sentence shown on the homepage and in the news list.
3. Write the text below the front matter.
4. Optionally upload `featured.jpg` or `featured.png` to the same folder as the listing image, and PDFs to link from the text.

```markdown
---
title: "Paper accepted at ACL 2026"
date: 2026-05-20
tags:
  - news
  - paper
summary: "Our paper on argument mining has been accepted at ACL 2026."
---

Our paper has been accepted at ACL 2026.

## Useful links

- [Conference website](https://2026.aclweb.org/)
- [Programme](programme.pdf)
```

The homepage shows the six most recent news items automatically.
The three newest appear as text cards, and the others appear as rows.
A preview does not link to the news page.
The title, the summary, and the links must therefore be enough on their own.

Every link in the text appears as a button on the preview, so a reader can open a program or a paper directly.
For a paper, use the paper title as the news title and write the venue in the summary.
List `topics` from `data/topics.yaml`, preferably the topics of the research areas.
Topics classify the item and do not appear on the preview.

The tags set the label on the preview.
The tag `paper` gives **Paper**, `special issue` gives **Call for papers**, `workshop` gives **Workshop**, and `event` gives **Event**.
Any other news item gets the label **News**.

A news item with a future date stays hidden until that date.
The site rebuilds every day at 04:00 UTC, so the item appears on the morning of its date.

### Add an event

1. Create `content/events/<slug>/index.md`, for example `content/events/2026clef/index.md`.
   Copy an existing event, or run `uv run python scripts/site.py new event 2026clef`.
2. Set `title`, `date`, `summary`, and `tags`.
3. Describe the event in the body, and link its website and any PDF placed in the same folder.

### Add or update a team member

Each member has a folder in `content/authors/` named after the full name in lowercase with hyphens, for example `content/authors/maria-rossi/`.
The folder contains `_index.md`, with an underscore, and a photo named `avatar.jpg` or `avatar.png`.

1. Copy the folder of an existing member, or run `uv run python scripts/site.py new person maria-rossi`.
2. Set `title` to the full name exactly as it appears in publications, for example `Maria Rossi`.
   The folder name must match it: validation rejects `maria-rossi` for a profile titled `Mario Rossi`.
3. Set `first_name`, `last_name`, `bio`, `interests`, `email`, and the `social` links.
   Leave out `role`, which only the head and the deputy of the lab set.
   For a member with a University of Bologna page, add a first social link with `icon: unibo` and `icon_pack: custom`, which shows the university seal.
   For a personal website, use `icon: globe` and `icon_pack: fas`.
4. Set `user_groups` to one of `Members`, `Associate Fellows`, or `Former Members`, with this exact spelling.
   The group selects the section of the People page.
   Set `weight` to order the people within a group, where lower values appear first.
5. Keep `highlight_name: true`, which shows the member in bold in author lists.
6. Replace the default `avatar.png` with a square photo named `avatar.jpg` or `avatar.png`, at most 5 MiB.
   Delete the default file when the photo is a JPEG, because the page shows only one avatar.

When a member leaves the lab, set their `user_groups` to `Former Members`.
Former members may omit `email`.
Without a photo, keep the default person avatar from `archetypes/person/avatar.png`.
Validation requires exactly one of the three groups.
Keep the folder, because their publications still link to it.

### Add a thesis

1. Create `content/theses/<year><name>/index.md`, for example `content/theses/2026mariarossi/index.md`.
   Copy an existing thesis, or run `uv run python scripts/site.py new masters-thesis 2026mariarossi`.
   Use `bachelors-thesis` for a bachelor's thesis.
2. Set `title`, `authors` with the student's name, and `date` as the graduation date.
3. Keep `categories` as `Master thesis` or `Bachelor thesis`.
   It sets the tag of the thesis under "Work done with students" on the Work with us page.
4. Set `url_pdf` to the thesis record, for example its AMS Laurea page, when it exists.
5. Set `topics` to one to three keys from `data/topics.yaml`, such as `[llms, legal]`.
   The topics appear as colored tags under "Work done with students" and feed its topic filter, next to a filter by kind and a search box.

### Add a research proposal

Research proposals are grouped by topic under `content/proposals/`.
Each topic is a folder whose `_index.md` holds the topic title, its `summary`, and its description.
The Work with us page lists every proposal automatically as a card, with a filter by topic; on phones the cards form one row that scrolls sideways.
Opening a card shows the `brief`, the contacts, the first three tags, **Choose this proposal**, and a **Full proposal** link when the proposal has a body.
A reader who chooses a proposal writes to its contacts.

```text
content/proposals/legal/
├── _index.md          the topic: title, summary, description
├── am/index.md        one proposal
└── unfairclauses/index.md
```

1. Run `uv run python scripts/site.py new proposal <topic>/<name>`, for example `new proposal legal/new-idea`.
   The topic folder must exist; the command creates a draft from `archetypes/proposal/index.md`, with a flow diagram to adapt.
2. Set `title`, `date`, `summary`, `brief`, `contacts`, and `tags`.
   The `summary` is one sentence for the card, and the `brief` is two to four sentences for the opened card.
   Each contact is a folder name in `content/authors/`, or, for a person outside the lab, a `name` and an `email`, for example `{name: Maria Rossi, email: maria.rossi@example.org}`.
   Use plain words for `tags`, such as `large language models`, not abbreviations.
   Validation requires `title`, `date`, `summary`, `brief`, and `contacts`.
   A topic `_index.md` needs `title` and `summary`.
3. Optionally, write the body: the proposal page, in the style of a publication page.
   Use `##` sections such as `Context`, `Objective`, `Directions`, and `References`; from 1200 px wide they appear in a side menu that marks the current section.
   Use `pipeline` flows for the method, built only from the proposal's own definitions and captioned as such.
   Set `math: true` when the body uses LaTeX.
   Without a body, the proposal page shows the `brief`, and the Work with us page shows no **Full proposal** link.
4. Remove `draft: true` when the proposal is ready.

To add a new topic, create a folder such as `content/proposals/new-topic/` with an `_index.md`.
Copy the `_index.md` of an existing topic and replace its title, summary, and description.

### Add a project

1. Create `content/projects/<slug>/index.md`, for example `content/projects/amica/index.md`.
   Copy an existing project, or run `uv run python scripts/site.py new national-project amica`.
   Use `international-project` for an international project.
2. Set `title`, `date` as the project start, `summary`, and `external_link` as the project website.
   End the title with the acronym in brackets, as in `Argument Mining In Covid-19 Articles (AMICA)`.
   The card shows the acronym as its headline and the rest of the title below it.
   The card shows the start year and the summary, and its Website chip opens `external_link`.
   The date orders the cards and places the project on the timeline at the top of the page.
3. List one or more `topics`, using the keys defined in `data/topics.yaml`.
   Topics appear as colored tags on the card and feed the topic filter.
4. Keep `categories` as `International project` or `National project`.
   It sets the scope label, the color on the timeline, and the scope filter.

Projects have no page of their own, so the file needs no body text.

### Edit the Work with us page

`content/work-with-us/index.md` holds the page as data: the `contacts` who receive every message, and one entry in `paths` per card under "What are you looking for?".
Contacts are folder names in `content/authors/`, whose `email` field is used; a path may set its own `contacts`.
Each path has a `key` (its anchor, such as `/work-with-us/#thesis`), a card `label` and `summary` of at most two sentences, an `icon`, a `title`, and Markdown `who` and `what`.
Its `steps` appear as a numbered list after the path card.
From 1200 px wide, a side menu beside the open path links to its summary and to each step.
Each step has a `title`, Markdown `text`, and an optional `show`, which places a section in the step.
The sections are `proposals` (the research proposals, with a topic filter), `projects` (the three most recent projects), and `contact` (the email form).
`inspiration: student-work` adds a last, unnumbered step with the work done with students.
Its `form` sets the email `subject`, which may name fields in braces such as `{proposal}`, and the `fields` to fill.
A field with `when`, such as `when: {funding: I need funding from the lab}`, appears only while the named field has that value.
A select field with `options: proposals` lists the research proposals.
A text field with `options: proposals` receives the title chosen with **Choose this proposal**.
The form opens the visitor's email app with recipients, subject, and body filled in; nothing passes through the site.
Without JavaScript the path cards are hidden, and every path and the research proposals are visible.
The work done with students then stays collapsed, and each path offers a plain email link with the same subject and an empty template.

### Add a research area

1. Create `content/research/<slug>/index.md`.
   Copy an existing area, or run `uv run python scripts/site.py new research <slug>`.
2. Set `title`, `summary`, and a `tagline` of at most 12 words.
   The tagline appears on the homepage card and on the research page; the page header shows the title alone.
   The research page (`layouts/research/list.html`) gives each area a full-width band: a mosaic of its `overview` schemas, then the tagline, the first line of `definition` (citations dropped), the `focus` topic titles, and the number of focus items by status. Its one-sentence `intro` lives in `content/research/_index.md`.
3. Set `icon` to a [Font Awesome 5](https://fontawesome.com/v5/search?m=free&s=solid) solid icon name, such as `comments` or `balance-scale`.
4. Set `weight` to order the cards, and `cover_pattern` to `dots`, `graph`, `tokens`, or `wave`.
5. Define the area in plain words, either in the body under a `## What is ...?` heading or in `definition`, a short Markdown text shown in a box under the title.
   Optional `overview` shows concept blocks under a "Core concepts" heading, two per row. Each block has an `icon`, a `title`, a short `text`, and an optional `schema`: an SVG file in the page folder, drawn with the `lt-s-*` classes so that it follows light and dark mode. The schemas of `content/research/am/` add `lt-s-node` boxes with a `lt-role-N` class, `lt-s-implicit` for dashed borders, and `lt-s-support` or `lt-s-attack` on edges.
   Optional `concepts` gives the background of the examples in a few Markdown paragraphs above the views: the notions the examples rely on, not a list of tasks. Its heading is `views_title`, "Core concepts" by default.
   The body, the definition, the core concepts, and the views share the first section band.
   Optional `views` add tabs under that background, one per argument model or domain.
   Each view shows one argument as marked text and as a graph, side by side on wide screens and stacked on narrow ones, with `roles`, `segments`, `rows`, and `edges`.
   Each component gets an ID, the initials of its role label (or the role's `short`) and its number within the role, such as P1; text tags and graph boxes show the ID, so the graph stays small. Mark [...] where text is omitted.
   Use `texts` instead of `segments` to show several texts side by side, such as a clause and its translation.
   An `implicit` component, which the text leaves unstated, follows the text in a dashed box; one with `kind: label` is a label assigned by the annotation, such as a category, drawn as a regular box with its text.
   Each row of `rows` is one line of the graph; nodes line up in columns, and supports and attacks are drawn in green and red.
   Picking a tab, or the first view coming into sight, types the text; the Annotate and Show graph buttons then mark its components and move them into the argument graph. Pointing at or focusing a box or a component lights both and dims the rest of the text.
   On research area pages and on the homepage, the section nearest a focus line is in focus, and the others shrink slightly and turn grey as they move away from it; the first section is in focus at the top of the page.
   Copy the views of `content/research/am/index.md`, and link the source of each example by name in its `caption`.
   A view with `type: detect` shows a document instead, as `document` and `sections`, each with a `title` and `sentences`.
   A sentence that the annotators marked has a `category` and a `level`: 1 clearly fair, 2 potentially unfair, or 3 clearly unfair.
   The document is written as in the argument views, with a Skip button; the Detect button then scans the document one sentence at a time and highlights each marked clause with its category and level, and a summary counts the unfair clauses.
   Copy the `terms` view of `content/research/legal/index.md`.
   A view with `type: rules` also shows a document, but each clause about personal data has a `level`, a `rule`, and `parts`; a clause matrix beside the text gives each clause an ID (C1, C2, ...) and a row with the type of its category, its specification, and its subcategories.
   A part is plain `text`, or a mark with a `role` (category, specification, or subcategory) and a `type` (open or closed); a specification holds its own `parts`.
   The view lists its annotation `rules`, each with a `level`, a number `n`, and the type that the category, the specification, and the subcategories need (open, closed, any, or none).
   The rules follow in the same columns. Detect opens the matrix, marks the clauses in the text, and fills their rows; Classify lights the rule with the same pattern as each row and adds its rule ID (such as L2 · R1) beside the clause ID.
   A graph view can set `graph_title` to rename its graph panel, such as Clause alignment for the cross-lingual view.
   `site.py check` fails when the marks of a clause do not match the rule it names.
   Copy the `privacy` view of `content/research/legal/index.md`.
   A view with `type: voices` shows illustrative `readings` of short sentences, each as a cue strip that aligns pitch, loudness, words, and pauses on one time grid, beside a table of `models`.
   Each word has `w`, a duration `dur` and an optional `pause` after it (seconds), a `pitch` pair (start and end, 0 to 1), and a `loud` value (0 to 1); each reading has a `label`, a `summary` of its cues in words, and a `gold` answer (`gold_label` names that row, Annotators by default), and the strip shows the speaking rate.
   Each model lists what it `hears` and one of `answers` per reading. The readings appear one after the other as plain text; Listen takes them in order, spreading the words on the time grid, opening the pitch and loudness rows, and drawing the cues word by word, and Classify shows the answers.
   Keep sentences to about four words, so a strip fits a phone without scrolling, and say in the caption that the cues and answers are constructed.
   `site.py check` fails without readings and a question, on a word outside these ranges, or when a model does not give one answer per reading. Copy the views of `content/research/speech/index.md`.
6. List the research areas in `fields`.
   Each block has a `title`, an `icon`, a `question`, a `summary`, and `tasks` that state their input and expected output.
   Selecting a block enlarges it and opens its tasks beside it.
7. List the lab topics in `focus`.
   The topics rotate in a carousel; the current dot fills until the next topic, and the rotation holds under the pointer, under keyboard focus, and while a detail box is open.
   Each topic has a card `summary`, a longer `description`, and `items` marked `done` (Explored), `now` (Current), or `next` (Future).
   An item has a short `text` for the card and a `detail` for the box below the carousel.
   An Explored item cites publications in `cite` by folder name, and the box lists them on the right.
   The topic titles appear as chips on the homepage card.
   Copy `content/research/am/index.md` as a starting point.
   The check fails on a missing or repeated key, an unknown status, or a citation of a missing publication.

The homepage shows one card per research area automatically.

### Add a tool

The Tools page lists only systems that readers can use today: an online service or demo, or an installable package.
A system built only to demonstrate a paper is a prototype: give its publication or thesis the `prototype` topic instead.
Each tool is one band with a schematic on the left and its description on the right, and the tool page redirects to `external_link`.

1. Create `content/tools/<slug>/index.md`.
   Copy an existing tool, or run `uv run python scripts/site.py new tool <slug>`.
2. Set `title`, `summary` in at most two sentences, and `date` as the first public release.
   The date orders the bands, newest first, and is not displayed.
3. Set `kind`, such as `Web service`, `Web demo`, or `Python library`. It appears as a pill under the name.
4. Add `schema: schema.svg`, an SVG file in the tool folder drawn with the `lt-s-*` classes, and a `caption` that names its source.
5. Set the links. Each one becomes a chip, and each is optional except `external_link`:
   `external_link` for the website, `demo` for a web demo, `code` for the repository, and `publication` for the folder name of the paper under `content/publication/`.
   Set `package` to the PyPI name to show its `pip install` command.
6. List one or more `topics`, using the keys defined in `data/topics.yaml`. They appear as colored tags.

### Edit the homepage or the menu

The homepage is defined in `content/_index.md` as a list of blocks: the hero, the research map, the latest news, and the latest preprints.
The texts of the hero and the section headings are front matter values in that file.
The blocks named `lt-*` are templates in `layouts/_partials/blocks/`.
A hero button that points to an unpublished page, such as a draft, is hidden.
The top menu is defined in `config/_default/menus.yaml`, where lower `weight` values appear first.
An entry with `parent: <identifier>` appears in the dropdown of the entry with that `identifier`, as News and Events do under **News & Events**.

The full menu fits on one line from 1280px, and narrower screens use the collapsed menu.
After adding a menu entry, check the menu at 1280px, and shorten a label or move it into a dropdown if the line wraps.

Ask the maintainer to review changes to the homepage, the menu, or any file outside `content/`, because they affect the whole site.

## Part 3. Publish your change

### On the GitHub website

1. Open <https://github.com/nlp-unibo/nlp-unibo.github.io>.
2. To edit a page, open its `index.md` and select the pencil icon.
   To create a page, select **Add file → Create new file** and type the full path, such as `content/news/acl-2026/index.md`.
   To add images or PDFs, open the page folder and select **Add file → Upload files**.
3. Select **Commit changes**, choose **Create a new branch for this commit and start a pull request**, and give the branch a short name such as `news/acl-2026`.
4. On the next screen, select **Create pull request**.
   Fill in the short template, and make sure the base branch is `hugoblox-template`.
5. Wait for the **Validate content and build** check.
   A green tick means the site builds.
   A red cross means that the check found a problem, which [Part 4](#part-4-common-problems) helps to fix.
6. To fix a problem, edit the file again in the same branch.
   The check runs again automatically.
7. When the check is green, merge the pull request, or ask the maintainer to merge it.

The site updates a few minutes after the merge.
Open the **Actions** tab to follow the **Deploy Hugo site to Pages** run, then check your page on <https://nlp.unibo.it/>.

### Work on your computer

The first setup installs everything the site needs into this folder, including the exact Hugo version used by GitHub.
It requires [Git](https://git-scm.com/) and [uv](https://docs.astral.sh/uv/getting-started/installation/), and it runs on Linux and macOS.
On Windows, use the [Windows Subsystem for Linux](https://learn.microsoft.com/windows/wsl/install) and run every command inside it.

```bash
git clone https://github.com/nlp-unibo/nlp-unibo.github.io.git
cd nlp-unibo.github.io
uv sync
uv run python scripts/site.py setup
```

For each change, start from the latest version and create a branch:

```bash
git switch hugoblox-template
git pull --ff-only
git switch -c news/acl-2026
```

Start the preview and open <http://localhost:1313/>.
The preview updates while you edit, and it also shows drafts and pages with a future date.

```bash
uv run python scripts/site.py serve
```

Before publishing, run the same check as GitHub, then commit and push:

```bash
uv run python scripts/site.py check
git add content/news/acl-2026
git commit -m "Add ACL 2026 news"
git push -u origin news/acl-2026
```

GitHub prints a link to open the pull request.
Continue from step 4 of the website instructions above.

### Before you merge

- [ ] The title, names, dates, venue, DOI, and links are correct.
- [ ] Every `TODO` text is gone, and `draft: true` is removed from pages meant to be public.
- [ ] Every image or PDF is at most 5 MiB, and its file name has no spaces.
- [ ] No private data, credentials, internal ratings, or copyrighted files were added.
- [ ] The **Validate content and build** check is green.
- [ ] After deployment, the page looks right on a computer and on a phone.

## Part 4. Common problems

The check prints one line per problem, starting with the file name.
The table below explains the most frequent messages.

| Message | Meaning and fix |
| --- | --- |
| `required field 'summary' is empty` | The named field is missing or empty. Add it to the front matter |
| `categories must be exactly one of ...` | The `categories` value is missing, misspelled, or repeated. Copy one allowed value from the message |
| `contains TODO marker` | A `TODO:` text from the template is still there. Replace it, or keep `draft: true` until the page is ready |
| `email link '...' must start with mailto:` | Write email links as `[Name](mailto:name@unibo.it)` |
| `local link '...' does not exist` | A link points to a missing file. Check the spelling and capitalization, and upload the file to the page folder |
| `invalid slug` | The folder name contains capitals, spaces, or other characters. Use lowercase letters, numbers, and hyphens only |
| `author slug must be '...'` | A member's folder name does not match their `title`. Rename the new folder as shown |
| `authors term '...' conflicts with '...'` | The same person is written in two ways, for example with and without an accent. Use the spelling of their profile |
| `tags term '...' conflicts with '...'` | The same tag is written in two ways, for example `semeval` and `SemEval`. Use the spelling of the existing tag |
| `exceeds 5 MiB asset limit` | Compress the image or PDF, then upload it again |
| `contains example domain` or `contains example email` | A template link or address such as `example.org` is still there. Replace it with the real one |
| `publication_types must be exactly one of ...` | Use one value from the message, as described in [Add a publication](#add-a-publication) |
| `missing page index` | The folder has no `index.md` (or `_index.md` for a member or a proposal topic). Check the file name |
| `pages must be folders with an index.md` | A page was saved as `name.md` directly in a section. Move it to `name/index.md` |
| `repeated key ...` | The same field appears twice in the front matter. Keep one of them |
| Warning `future publication date` | The page is valid but stays hidden until its date |
| Warning `missing cite.bib` | The publication has no BibTeX file, so its Cite button is empty. Add `cite.bib` |
| A YAML error with a line number | The front matter layout is broken. Check tabs, indentation, quotes, and both `---` lines near that line |

The following problems produce no message.

A page is missing from the site when it still has `draft: true`, when its `date` is in the future, or when it sits in the wrong folder.
A publication is missing from its list when its `categories` value selects another list.
An image is missing when the file name in the text differs from the uploaded file, including capitalization.
A change is not visible when the deployment is still running; wait a few minutes and reload the page without the browser cache.

## Part 5. Maintainer reference

### Repository structure

| Path | Purpose |
| --- | --- |
| `content/_index.md` | Homepage blocks |
| `content/authors/` | Member profiles and avatars |
| `content/publication/` | All publications; `categories` selects their list |
| `content/news/`, `content/events/` | News items and events |
| `content/projects/` | All projects; `categories` selects International or National |
| `content/theses/` | Master's and bachelor's theses; `categories` selects the list |
| `content/proposals/` | Research proposals, one folder per topic |
| `content/research/`, `content/tools/` | Research areas and tools |
| `content/people/` | Landing page |
| `content/work-with-us/` | Work with us page, as data for `layouts/work-with-us/single.html` |
| `content/categories/_index.md` | Citation view for category pages |
| `config/_default/` | Site settings (`hugo.yaml`, `params.yaml`) and the menu (`menus.yaml`) |
| `config/_default/module.yaml` | Theme modules, with one blox-seo file excluded |
| `data/topics.yaml` | Topic labels and tag colors for projects, tools, news, research areas, theses, and student publications |
| `data/themes/ltlab.toml` | Site colors, taken from the lab logo. The site shows only dark mode (`config/_default/params.yaml` sets no `theme_day`), and the light colors stay for a possible return |
| `data/fonts/ltlab.toml`, `static/fonts/inter/` | Self-hosted Inter font, under the SIL Open Font License |
| `assets/scss/template.scss` | Site-wide style rules layered over the theme |
| `assets/js/ltlab.js` | Scroll effects and publication year headings, loaded by `layouts/_partials/hooks/body-end/ltlab.html` |
| `assets/media/` | Shared images, including the homepage logo |
| `layouts/_shortcodes/` | Components for publication pages, such as `svg`, `stages`, and `pipeline` |
| `layouts/_partials/blocks/lt-*.html` | Homepage blocks: hero, research map, news, and preprints |
| `layouts/_partials/lt/` | Pieces shared by those blocks: generated cover art, link extraction, news labels, publication cards, and contact people (`contacts.html`, `people-row.html`) |
| `layouts/publication/single.html` | Publication page in the style of a research project page |
| `layouts/publication/section.html` | Publications page: highlights carousel, then every publication with search, type, and topic filters |
| `layouts/proposals/single.html` | Research proposal page in the style of a publication page |
| `assets/media/logo.svg`, `assets/media/icon.png` | Navbar logo and the favicon generated from it |
| `layouts/authors/list.html` | Theme profile page plus a kind badge on each Latest entry |
| `layouts/_partials/views/card.html` | Theme card view plus topic tags |
| `layouts/_partials/views/citation.html` | Theme citation view plus the award line and year data for headings |
| `static/media/icons/unibo-seal.svg` | University of Bologna seal for the `unibo` social icon |
| `layouts/redirect/single.html` | Layout for pages with `type: redirect` |
| `layouts/baseof.html`, `layouts/rss.xml`, `layouts/index.webmanifest`, other `layouts/_partials/` files | Theme templates with current Hugo calls in place of deprecated ones |
| `archetypes/` | Templates used by `site.py new` |
| `scripts/site.py` | Setup, preview, validation, and build commands |
| `scripts/test_site.py` | Self-checks for the validator, run by the pull-request workflow |
| `content/mm-argfallacy/` | Redirect from a shared-task short link to its event page |
| `.github/workflows/` | Pull-request validation (`validate.yml`) and deployment (`hugo.yml`) |
| `.github/pull_request_template.md` | Pull-request checklist |

### Categories

Publications, projects, and theses use one `categories` value to select the list they appear in.
A publication may also add `Highlight`, which also shows it in the Highlights carousel.
Validation rejects a missing or unknown value.
The theme would print categories in the page metadata, so `template.scss` hides them.

| Folder | Allowed `categories` values |
| --- | --- |
| `content/publication/` | `Journal`, `Conference`, `Workshop`, `Preprint`, plus an optional `Highlight` |
| `content/projects/` | `International project`, `National project` |
| `content/theses/` | `Master thesis`, `Bachelor thesis` |

The allowed values live in `SECTION_CATEGORIES` in `scripts/site.py`.
A new value also needs a list block on the matching landing page.

When moving a published page, keep its old path under `aliases`, so that external links redirect to the new address.

### Commands

| Command | Effect |
| --- | --- |
| `uv run python scripts/site.py setup` | Download the pinned Hugo and Go versions into the ignored `.tools/` folder |
| `uv run python scripts/site.py serve` | Start the local preview, including drafts and future pages |
| `uv run python scripts/site.py new TYPE SLUG` | Create a draft page from a template |
| `uv run python scripts/site.py content` | Validate front matter, slugs, required fields, categories, publication types, placeholders, local links, and asset sizes |
| `uv run python scripts/site.py templates` | Verify that every template generates a valid draft |
| `uv run python scripts/site.py build` | Build the production site under `.build/public` |
| `uv run python scripts/site.py check` | Run every validation, then the production build |
| `uv run python scripts/site.py clean` | Remove build output and caches, and keep the downloaded tools |
| `uv run python scripts/test_site.py` | Run the self-checks of the validator's link parser and front-matter loader |

The `new` command accepts `news`, `event`, `person`, `research`, `tool`, `national-project`, `international-project`, `bachelors-thesis`, `masters-thesis`, `publication-highlight`, `journal`, `conference`, `workshop`, `preprint`, and `proposal`.
A proposal slug names its topic folder, as in `new proposal legal/new-idea`.

The Hugo version comes from `.github/workflows/hugo.yml`, so local and GitHub builds always use the same version.
The production build uses its own resource folder, so `check` can run while the preview is open.

### Validation and deployment

Every pull request to `hugoblox-template` runs **Validate website**, which executes `site.py check` with the locked Python environment.
Merging into `hugoblox-template` runs **Deploy Hugo site to Pages**, which builds and publishes the site.
The same workflow also runs every day at 04:00 UTC, so pages with a future date appear once that date arrives.
If a deployment does not start, open the workflow in the **Actions** tab and select **Run workflow** on `hugoblox-template`.
Keep **Enforce HTTPS** enabled under **Settings → Pages** for the `nlp.unibo.it` custom domain.

### Review and emergency policy

The repository currently has one active maintainer, so pull requests require zero approvals and the **Validate content and build** status check.
The repository has no `CODEOWNERS` file, so new pull requests request no reviewers by default.
Request a reviewer explicitly when a change needs a second opinion.
When a second maintainer becomes active, increase the ruleset to one required approval and require another maintainer to review each change.
Resolve review threads and push follow-up fixes before merging whenever a review takes place.

Routine updates always follow the workflow in Part 3.
An emergency is limited to an active outage, security incident, privacy exposure, or similarly urgent risk to the live site.
Emergency changes still use a focused pull request and the required validation check whenever GitHub is operational.
If those controls prevent urgent risk mitigation, a repository administrator may temporarily amend the ruleset.
The administrator records the reason and the exact change in the pull request, restores the ruleset immediately afterward, and requests a retrospective review.
Deadlines and delayed content publication are not emergencies.

### Theme customization and upgrades

The site keeps the Hugo Blox theme unmodified and layers its changes on top.
Colors live in `data/themes/ltlab.toml`, fonts in `data/fonts/ltlab.toml`, and style rules in `assets/scss/template.scss`.
The collapsed menu between 992px and 1279px repeats the theme's mobile navbar rules from `components/_nav.scss`.

The theme is the Bootstrap edition of Hugo Blox at its last upstream commit, `62f5b139d3c5`, pinned in `go.mod`.
That edition is archived upstream, so no newer version exists.
The `layouts/` folder follows the template structure of Hugo 0.146 and later, with `_partials/`, `_shortcodes/`, and `_markup/` folders.
Hooks must stay in `layouts/_partials/hooks/`, because the theme reads hooks only from that folder.

Four files depend on theme internals and need attention when upgrading Hugo Blox.
First, `layouts/_partials/views/citation.html` is a copy of the theme's citation view with the award line and year data, so re-sync it with the new theme file.
Second, `layouts/_partials/views/card.html` is a copy of the theme's card view with topic tags, so re-sync it as well.
Third, `layouts/authors/list.html` is a copy of the theme's profile page with Latest badges, so re-sync it as well.
Fourth, the navbar rules in `template.scss` rely on the theme's navbar markup, so recheck the menu between 992px and 1279px.

Fifteen further templates are copies of theme files that differ only in their Hugo calls.
They use `hugo.Data` instead of `site.Data`, `site.Language.Locale` instead of `site.LanguageCode`, and `.IsBranch` instead of `.IsNode`.
Two of them come from the blox-seo module: `layouts/index.webmanifest` and `layouts/_partials/seo_tags.html`.
The other thirteen come from blox-bootstrap: `layouts/baseof.html`, `layouts/rss.xml`, and eleven files under `layouts/_partials/`.
When a Hugo release deprecates another call, search the theme modules for it and copy each affected file the same way.
One copy has a second change: `layouts/_partials/components/headers/navbar.html` shows the site title next to the logo.

`config/_default/module.yaml` imports blox-core and blox-seo directly, in the order the theme uses.
The direct import lets the site exclude `layouts/_markup/sitemap.xml` from blox-seo, which Hugo skips with a warning.

### License

The repository and the website are licensed under CC BY-NC-ND 4.0, as stated in the site footer and in `LICENSE`.
Code derived from the Hugo Blox template keeps its MIT License, and the Inter font keeps the SIL Open Font License.
The University of Bologna seal in `static/media/icons/unibo-seal.svg` is derived from the public-domain seal on Wikimedia Commons, cut out of a solid disc so that it matches the weight of the other icons.
The seal remains a university insignia, so the site uses it only to link to university pages.
The footer license is configured under `footer.copyright.license` in `config/_default/params.yaml`, so change both places together.
