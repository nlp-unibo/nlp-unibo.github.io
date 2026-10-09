# Editors' guide

This guide explains how to add or change content on the [Language Technologies Lab website](https://nlp.unibo.it/).
It is written for lab members who are not programmers.
You only need a web browser and a GitHub account with write access to this repository.
Ask the maintainer for access if you do not have it.

To change the design or the code of the site, read [the developers' guide](developers.md) instead.

## Contents

- [1. Five ideas that explain the site](#1-five-ideas-that-explain-the-site)
- [2. What appears where](#2-what-appears-where)
- [3. Recipes](#3-recipes)
  - [Add a publication](#add-a-publication)
  - [Add a news item](#add-a-news-item)
  - [Add or update a person](#add-or-update-a-person)
  - [Add a thesis](#add-a-thesis)
  - [Add a research proposal](#add-a-research-proposal)
  - [Add a project](#add-a-project)
  - [Add a tool](#add-a-tool)
  - [Add a research area](#add-a-research-area)
  - [Edit the homepage](#edit-the-homepage)
  - [Edit the menu](#edit-the-menu)
  - [Edit a page introduction](#edit-a-page-introduction)
  - [Edit the Work with us page](#edit-the-work-with-us-page)
- [4. Change existing content](#4-change-existing-content)
  - [Find and edit a file](#find-and-edit-a-file)
  - [Remove a paper from the Highlights carousel, or add one](#remove-a-paper-from-the-highlights-carousel-or-add-one)
  - [Change the text of a page](#change-the-text-of-a-page)
  - [Replace an image](#replace-an-image)
  - [Reorder items](#reorder-items)
  - [Hide or remove a page](#hide-or-remove-a-page)
  - [Add a schema to a page](#add-a-schema-to-a-page)
- [5. Publish your change](#5-publish-your-change)
- [6. Publication blog pages](#6-publication-blog-pages)

## 1. Five ideas that explain the site

### One folder per page

Every page of the site is a folder.
The folder holds a text file named `index.md` and the images or PDFs that only this page uses.
For example, a news item lives in `content/news/acl-2026/index.md`.
A person is the one exception: the file is named `_index.md`, with an underscore.

The name of the folder is the **slug**.
A slug becomes part of the web address of the page.
Use lowercase letters, numbers, and hyphens only, such as `acl-2026`.
Do not rename a folder after publication, because every existing link to it would break.
If you must move a published page, keep its old path in a list named `aliases` in its front matter, so that old links still work.

### Front matter

The **front matter** is the block at the top of the file, between two lines that contain only `---`.
It stores the details of the page, one per line, as `name: value`.
Each of these names is a **field**, such as `title` or `date`.
The text below the second `---` is the **body** of the page.

The body uses **Markdown**, a plain-text format.
Write `**bold**` for **bold** and `*italic*` for *italic*.
Write `## Heading` for a heading and `- item` for a list item.
Write `[text](https://example.com/)` for a link.

The front matter uses **YAML**, a format that is sensitive to layout.
Follow these rules to avoid most errors:

1. Indent with spaces, never with tabs.
2. Keep the indentation of lists exactly as in the template.
3. Write dates as `YYYY-MM-DD`, for example `2026-05-20`.
4. Put double quotes around a value that contains a colon or a hash sign, for example `title: "LLMs: a survey"`.
5. Never delete either `---` line.
6. A line that starts with `#` is a **comment**: a note for editors that the site ignores.

### Where files go

Each kind of content has its own folder under `content/`.

| Content | Folder |
| --- | --- |
| Publications | `content/publication/` |
| News items | `content/news/` |
| People | `content/authors/` |
| Theses | `content/theses/` |
| Research proposals | `content/proposals/<topic>/` |
| Projects | `content/projects/` |
| Tools | `content/tools/` |
| Research areas | `content/research/` |
| Homepage | `content/_index.md` |
| Menu | `config/_default/menus.yaml` |

Publications, projects, and theses use one `categories` value to choose the list they appear in.
The check rejects a missing or unknown value.

| Folder | Allowed `categories` values |
| --- | --- |
| `content/publication/` | `Journal`, `Conference`, `Workshop`, `Preprint`, plus an optional `Highlight` |
| `content/projects/` | `International project`, `National project` |
| `content/theses/` | `Master thesis`, `Bachelor thesis` |

Several fields take **topics**: keys from `data/topics.yaml` that appear as colored tags.
The keys are `legal`, `argument-mining`, `fairness`, `ethics`, `llms`, `industry`, `privacy`, `information-retrieval`, `sustainability`, `prototype`, `toolkit`, `multimodal`, `reproducibility`, `benchmark`, `speech`, `interpretability`, `llm-reasoning`, `biomedical`, `dialogue`, `knowledge-extraction`, `model-compression`, and `fact-checking`.
Ask the maintainer to add a new topic.

### Preview and review

The GitHub website cannot preview the site.
Instead, every change goes through a **pull request**: a proposal to change the site, which others can read before it takes effect.
A pull request lives on a **branch**, a separate copy of the files where your edits wait.
GitHub runs an automatic **check** on every pull request.
The check reads every page and builds the whole site, and it reports each problem it finds.
The live site does not change until the pull request is merged.

### Publishing

**Merging** a pull request copies your branch into the main version of the site, the branch named `hugoblox-template`.
GitHub then rebuilds the site and publishes it at <https://nlp.unibo.it/> within a few minutes.
A page with `draft: true` in its front matter is never published.
A page with a future date stays hidden until that date.
The site rebuilds every day at 04:00 UTC, so such a page appears on the morning of its date.

## 2. What appears where

Each row says where you create the content, where the site shows it without further work, and what you still have to do by hand.

| Content | Where you create it | Where it shows up automatically | What it does NOT do automatically |
| --- | --- | --- | --- |
| Publication | `content/publication/<slug>/index.md` | Its own page at `/publication/<slug>/`. The Publications page, grouped by year, with type and topic filters. The Highlights carousel of the Publications page, when `categories` includes `Highlight`. The News page timeline, as a **Paper** or **Preprint** item on its `date`. The homepage "Latest papers" block, while it is among the three newest by `date`. The profile page of each lab author named in `authors`. The "Works on" topics of those authors, unless they set `works_on`. "Work done with students" on the Work with us page, when `tags` includes `student publication` | No news item: the homepage News block lists news items only, so an acceptance needs a news item that you write. No research area: an area lists the paper only when one of its `focus` items cites the folder name in `cite`. No tool: the Tools page links the paper only when a tool names it in `publication` |
| News item | `content/news/<slug>/index.md` | The News page timeline, with its topic tags. The homepage News block, while it is among the six newest (the three newest as cards) | No page of its own: the preview shows only the title, the venue, the summary, and the links of the body. No topic tags on the homepage. Not on profile pages, even with an `authors` list. No publication entry |
| Person | `content/authors/<first-last>/_index.md` | The People page, in the group set by `user_groups`, ordered by `weight`. A profile page at `/author/<first-last>/`, with their publications and theses. Their name in bold, linked to the profile, in every author list that spells it exactly as `title` | No change to publications: a publication joins the profile only when its `authors` list spells the name exactly as the profile `title`. No menu entry |
| Thesis | `content/theses/<year><name>/index.md` | "Work done with students" on the Work with us page, with its topics. The Theses list at `/theses/`. The profile page of the student, when the student has one | Not on the News page or the homepage. No link to the supervisors, who are not listed |
| Research proposal | `content/proposals/<topic>/<slug>/index.md` | A card on the Work with us page, under its topic filter. Its own page at `/proposals/<topic>/<slug>/` | No news item. A topic folder that does not exist yet needs its own `_index.md` first |
| Project | `content/projects/<slug>/index.md` | A card and a timeline entry on the Projects page, with scope and topic filters. The three newest projects (by `date`) in a step of the Work with us page | No page of its own: the address of the project redirects to `external_link`. No link to its publications or people |
| Tool | `content/tools/<slug>/index.md` | A band on the Tools page, newest `date` first. A **Paper** link chip, when `publication` names a publication folder | No page of its own: the address of the tool redirects to `external_link`. Not on the homepage. The publication page does not mention the tool |
| Research area | `content/research/<slug>/index.md` | A card in the homepage Research block, ordered by `weight`. A band on the Research page. Its own page at `/research/<slug>/`, which lists the publications cited in `focus` | No publications are collected by topic: only the folder names in `cite` appear. No menu entry |
| Homepage block | `content/_index.md` | The block texts and the number of items it shows | The News, Latest papers, and Research blocks choose their items themselves: you cannot pick items there |
| Menu | `config/_default/menus.yaml` | The top menu on every page | A new page never adds itself to the menu |

## 3. Recipes

Every recipe follows the same pattern.

1. Select the **Start** link of the recipe.
   GitHub opens a new file, already named and filled with a template.
2. Change the placeholder folder name in the file name box into your slug.
3. Replace every `TODO` text.
   The check fails while a `TODO` text is left, so you cannot publish an unfinished page by mistake.
4. Select **Commit changes** and open a pull request, as described in [4. Publish your change](#5-publish-your-change).
5. Upload images or PDFs into the same folder of your branch, as described in [Add images and files](#add-images-and-files).

The fastest alternative is to copy an existing page of the same kind and edit it.
To edit an existing page, open its file on GitHub and select the pencil icon.

### Add images and files

Images and PDFs live in the folder of the page that uses them.
Upload them after you have opened the pull request, so that they land in your branch:

1. On the pull request page, select your branch name, shown under the title.
   GitHub opens the files of your branch.
2. Open the folder of your page.
3. Select **Add file**, then **Upload files**, and drag the files in.
4. Choose **Commit directly to the `<your-branch>` branch**, then select **Commit changes**.

Follow these rules for every file:

- Keep each file at most 5 MiB.
- Use lowercase letters, numbers, and hyphens in file names, with no spaces.
- File names are case sensitive: `Featured.PNG` is not `featured.png`.
- Use the exact names that a recipe asks for, such as `featured.png` or `avatar.jpg`.
- Upload only files that you may publish, with no private data.

### Add a publication

**Start:** [create `content/publication/surname-etal-2026-keyword/index.md`](https://github.com/nlp-unibo/nlp-unibo.github.io/new/hugoblox-template?filename=content/publication/surname-etal-2026-keyword/index.md&value=---%0A%23%20Replace%20every%20TODO.%20The%20check%20fails%20while%20one%20is%20left.%0Atitle%3A%20%22TODO%3A%20Paper%20title%22%0A%23%20One%20author%20per%20line.%20Write%20each%20lab%20member%20exactly%20as%20the%20title%20of%20their%20profile.%0Aauthors%3A%0A%20%20-%20%22TODO%3A%20First%20Author%22%0A%20%20-%20%22TODO%3A%20Second%20Author%22%0Aauthor_notes%3A%20%5B%5D%0A%23%20The%20publication%20date%2C%20as%20YYYY-MM-DD.%20It%20places%20the%20paper%20on%20the%20News%20timeline.%0Adate%3A%20%22TODO%3A%20YYYY-MM-DD%22%0A%23%20The%20day%20the%20page%20appears%20on%20the%20site.%20Usually%20the%20same%20as%20date.%0ApublishDate%3A%20%22TODO%3A%20YYYY-MM-DD%22%0A%23%20article-journal%2C%20paper-conference%2C%20article%20%28preprint%29%2C%20or%20chapter%0Apublication_types%3A%0A%20%20-%20paper-conference%0Apublication%3A%20%22TODO%3A%20Full%20venue%20name%22%0Apublication_short%3A%20%22%22%0A%23%20Without%20https%3A%2F%2Fdoi.org%2F%0Adoi%3A%20%22%22%0Aabstract%3A%20%22TODO%3A%20Abstract%22%0A%23%20One%20sentence%2C%20shown%20under%20the%20title%20and%20on%20publication%20cards%0Asummary%3A%20%22TODO%3A%20One%20sentence%22%0A%23%20Optional%2C%20at%20most%2015%20words%2C%20for%20the%20homepage%20card%0Acard_summary%3A%20%22%22%0A%23%20Keywords.%20Add%20student%20publication%20for%20work%20done%20with%20students.%0Atags%3A%20%5B%5D%0A%23%20One%20to%20three%20keys%20from%20data%2Ftopics.yaml%0Atopics%3A%20%5B%5D%0Afeatured%3A%20false%0Aurl_pdf%3A%20%22%22%0Aurl_code%3A%20%22%22%0Aurl_dataset%3A%20%22%22%0Aurl_poster%3A%20%22%22%0Aurl_project%3A%20%22%22%0Aurl_slides%3A%20%22%22%0Aurl_video%3A%20%22%22%0Aimage%3A%0A%20%20caption%3A%20%22%22%0A%20%20focal_point%3A%20%22%22%0A%20%20preview_only%3A%20false%0Aprojects%3A%20%5B%5D%0A%23%20Exactly%20one%20of%20Journal%2C%20Conference%2C%20Workshop%2C%20Preprint.%20Add%20Highlight%20for%20the%20carousel.%0Acategories%3A%0A%20%20-%20Conference%0Aaffiliations%3A%20%5B%5D%0A---%0A%0A%3C%21--%20The%20body%20is%20optional.%20Leave%20it%20empty%3A%20the%20page%20then%20shows%20the%20abstract.%20--%3E%0A)

Name the folder after the first author, `etal`, the year, and one keyword, such as `rossi-etal-2026-example`.
A folder holds these files:

```text
content/publication/rossi-etal-2026-example/
├── index.md       the page
├── cite.bib       the BibTeX record behind the Cite button
└── featured.png   the main figure, optional
```

| Field | Required | Example | Rule |
| --- | --- | --- | --- |
| `title` | Required | `"Let Guidelines Guide You"` | The paper title, without LaTeX commands such as `\textbf` |
| `authors` | Required | `- Federico Ruggeri` | One author per line, starting with `- `. Spell lab members exactly as the `title` of their profile, so that their name is bold and links to the profile |
| `date` | Required | `2026-05-20` | The publication date. It orders every list and places the paper on the News timeline |
| `publishDate` | Optional | `2026-05-20` | The day the page appears. Usually the same as `date` |
| `publication_types` | Required | `- paper-conference` | Exactly one of `article-journal` (journal), `paper-conference` (conference or workshop), `article` (preprint), or `chapter` (book chapter) |
| `categories` | Required | `- Conference` | Exactly one of `Journal`, `Conference`, `Workshop`, or `Preprint`. Add `Highlight` as a second value to show the paper in the Highlights carousel |
| `publication` | Optional | `"Proceedings of ACL 2026"` | The full venue name |
| `abstract` | Optional | `"We introduce ..."` | Shown in full on the publication page |
| `summary` | Optional | `"GCAM has annotators report ..."` | One sentence, shown under the title and on publication cards. Every highlight needs one |
| `card_summary` | Optional | `"Annotators report guidelines, not labels."` | At most 15 words. Replaces the summary on the homepage card |
| `doi` | Optional | `10.18653/v1/2024.argmining-1.7` | Without `https://doi.org/` |
| `url_pdf`, `url_code`, `url_dataset`, `url_project`, `url_video`, `url_slides`, `url_poster` | Optional | `https://aclanthology.org/...` | Each becomes a button. `url_project` is labeled Demo |
| `links` | Optional | `- name: arXiv` then `  url: https://arxiv.org/abs/...` | Extra buttons, each with a `name` and a `url` |
| `topics` | Optional | `[argument-mining, llms]` | One to three topic keys. They feed the topic filter of the Publications page |
| `tags` | Optional | `- argument mining` | Keywords. Add `student publication` to list the paper under "Work done with students" |
| `award` | Optional | `Best Paper Award` | Shown with a trophy under the title in every publication list |
| `affiliations` | Optional | `- University of Bologna` | Institution names shown under the authors |
| `featured` | Optional | `false` | Leave it `false`: the `Highlight` category replaces it |

Then add the citation file:

1. In the folder of your publication on your branch, select **Add file**, then **Create new file**.
2. Name it `cite.bib` and paste the complete BibTeX record.
3. Do not add a `note` field with internal ratings, because readers download this file.

Images:

- `featured.png` (or `featured.jpg`) is the most representative figure of the paper.
  It becomes the teaser of the page and the preview on every card.
  Give every `Highlight` publication both `featured.png` and a `summary`, because its carousel card shows them.
- `card.png` is optional.
  Add it when `featured.png` is too detailed to read at card size: 1600 by 1000 pixels, with large text.
  Cards then show `card.png`, and the page keeps `featured.png`.
- `teaser.mp4` is an optional short video that replaces the teaser image on the page.
- Write the source of the figure in `image: caption:`, such as "(Figure 1 of the paper)".
  Reuse a figure only when its source is openly licensed, such as arXiv, the ACL Anthology, or CEUR-WS.

What else to update:

- **Acceptance news.** The homepage News block lists news items only.
  For an acceptance, [add a news item](#add-a-news-item) dated on the day of the acceptance.
  Use the paper title as the news title, write the venue in `venue`, and tag it `paper`.
  Link the publication page, such as `[Read more](/publication/rossi-etal-2026-example/)`.
- **Research area.** To list the paper on a research area page, add its folder name to the `cite` list of a `focus` item in `content/research/<area>/index.md`.
- **Tool.** When the paper describes a tool, set `publication: <folder name>` in the tool.

Common mistakes:

- An author spelled in two ways, such as with and without an accent, creates two people.
  The check reports `authors term '...' conflicts with '...'`.
- The paper is missing from the expected list because `categories` selects another one.
- A published paper loses its arXiv link on the News timeline, because the venue version replaces it.
  This is intended.
- No `cite.bib` file: the check warns `missing cite.bib`, and the Cite button is missing.

The body of the file can stay empty.
The page then shows the abstract.
Some publications also have a long body page; see [5. Publication blog pages](#6-publication-blog-pages).

### Add a news item

**Start:** [create `content/news/short-name-2026/index.md`](https://github.com/nlp-unibo/nlp-unibo.github.io/new/hugoblox-template?filename=content/news/short-name-2026/index.md&value=---%0Atitle%3A%20%22TODO%3A%20Headline%22%0A%23%20YYYY-MM-DD.%20A%20future%20date%20keeps%20the%20item%20hidden%20until%20that%20day.%0Adate%3A%20%22TODO%3A%20YYYY-MM-DD%22%0A%23%20The%20tag%20paper%2C%20special%20issue%2C%20shared%20task%2C%20workshop%2C%20or%20event%20sets%20the%20label.%20Otherwise%3A%20News.%0Atags%3A%0A%20%20-%20news%0Asummary%3A%20%22TODO%3A%20At%20most%20two%20sentences.%22%0A%23%20Optional%2C%20shown%20in%20italics%20under%20the%20title%2C%20such%20as%20a%20venue%20or%20a%20journal%0Avenue%3A%20%22%22%0A%23%20Keys%20from%20data%2Ftopics.yaml%0Atopics%3A%20%5B%5D%0A---%0A%0A-%20%5BTODO%3A%20Link%20text%5D%28https%3A%2F%2FTODO%29%0A)

A news item has no page of its own.
Its preview on the News page and on the homepage shows the title, the venue, the summary, and the links of its body.
The title, the summary, and the links must therefore make sense on their own.

| Field | Required | Example | Rule |
| --- | --- | --- | --- |
| `title` | Required | `"Paper accepted at ACL 2026"` | The headline. For an acceptance, the paper title |
| `date` | Required | `2026-05-20` | A future date keeps the item hidden until that day |
| `summary` | Required | `"Our paper on argument mining was accepted."` | At most two sentences |
| `tags` | Optional | `- paper` | Sets the label of the preview, see below |
| `venue` | Optional | `"Transactions of the ACL (TACL)"` | Shown in italics under the title, such as the journal of a call for papers |
| `topics` | Optional | `[argument-mining]` | Topic keys, preferably those of the research areas. Shown on the News page only |

The tags set the label of the preview.
The first matching rule wins:

| Tag | Label |
| --- | --- |
| `paper` | **Paper** |
| `special issue` | **Call for papers** |
| `shared task` | **Shared task** |
| `workshop` | **Workshop** |
| `event` | **Event** |
| any other | **News** |

Below the front matter, write a list of links.
Each link becomes a button on the preview.

```markdown
- [Conference website](https://2026.aclweb.org/)
- [Programme](programme.pdf)
```

Upload a PDF, such as a programme, into the same folder and link it by its file name.
A website with more content, such as a shared task, lives in its own section, such as `content/mm-argfallacy/2025/`, and the news item links to it.
Ask the maintainer to set up such a section.

What else to update: nothing.
A new publication needs no news item, because it joins the News timeline by itself.
Only an acceptance needs one.

Common mistakes:

- A summary longer than two sentences, which crowds the homepage card.
- A link to a file that you did not upload, or uploaded with a different name.
  The check reports `local link '...' does not exist`.
- An email written as a plain address.
  Write `[Write to us](mailto:name@unibo.it)`.

### Add or update a person

**Start:** [create `content/authors/firstname-lastname/_index.md`](https://github.com/nlp-unibo/nlp-unibo.github.io/new/hugoblox-template?filename=content/authors/firstname-lastname/_index.md&value=---%0A%23%20The%20full%20name%2C%20exactly%20as%20in%20publications.%20The%20folder%20name%20is%20this%20name%20in%20lowercase%20with%20hyphens.%0Atitle%3A%20%22TODO%3A%20Firstname%20Lastname%22%0Afirst_name%3A%20%22TODO%3A%20Firstname%22%0Alast_name%3A%20%22TODO%3A%20Lastname%22%0Asuperuser%3A%20false%0Aorganizations%3A%0A%20%20-%20name%3A%20University%20of%20Bologna%0A%20%20%20%20url%3A%20%22https%3A%2F%2Fwww.unibo.it%2F%22%0A%23%20One%20sentence%2C%20shown%20on%20the%20People%20page%0Abio%3A%20%22TODO%3A%20One%20sentence%20on%20your%20research.%22%0Ainterests%3A%0A%20%20-%20Natural%20Language%20Processing%0Asocial%3A%0A%20%20-%20icon%3A%20envelope%0A%20%20%20%20icon_pack%3A%20fas%0A%20%20%20%20link%3A%20%22mailto%3ATODO%40unibo.it%22%0Aemail%3A%20%22TODO%40unibo.it%22%0Ahighlight_name%3A%20true%0A%23%20Optional%3A%20up%20to%20three%20keys%20from%20data%2Ftopics.yaml%20for%20%22Works%20on%22%0A%23%20works_on%3A%20%5Bargument-mining%2C%20llms%5D%0A%23%20Exactly%20one%20of%20Members%2C%20Associate%20Fellows%2C%20Former%20Members%0Auser_groups%3A%0A%20%20-%20Members%0A%23%20Lower%20values%20appear%20first%20in%20the%20group%0Aweight%3A%20100%0A---%0A%0ATODO%3A%20A%20longer%20biography%2C%20in%20a%20few%20sentences.%0A)

Name the folder after the full name in lowercase, with hyphens and no accents, such as `maria-rossi`.
The folder must match the `title`: the check rejects `maria-rossi` for a profile titled `Mario Rossi`.

| Field | Required | Example | Rule |
| --- | --- | --- | --- |
| `title` | Required | `Maria Rossi` | The full name exactly as in publications |
| `first_name`, `last_name` | Required | `Maria`, `Rossi` | Used for the initials when there is no photo |
| `user_groups` | Required | `- Members` | Exactly one of `Members`, `Associate Fellows`, or `Former Members`, with this spelling. It selects the section of the People page |
| `email` | Required, except for former members | `maria.rossi@unibo.it` | Also used when a proposal names this person as a contact |
| `weight` | Optional | `100` | Orders people within a group. Lower values appear first |
| `bio` | Optional | `"Her research ..."` | One sentence, shown on the People page card |
| `interests` | Optional | `- Argument Mining` | One interest per line |
| `social` | Optional | see below | Icons with links, shown on the profile and the card |
| `works_on` | Optional | `[argument-mining, llms]` | At most three topic keys for "Works on". Without it, the site picks the three most frequent topics of the person's publications |
| `highlight_name` | Optional | `true` | Keep it `true`: it shows the person in bold in author lists |
| `role` | Do not set | | Only the head and the deputy of the lab set it |

Social links use these icons:

| Link | `icon` | `icon_pack` |
| --- | --- | --- |
| University of Bologna page, listed first | `university` | `fas` |
| Email, as `mailto:...` | `envelope` | `fas` |
| Personal website | `globe` | `fas` |
| GitHub | `github` | `fab` |
| LinkedIn | `linkedin` | `fab` |
| Google Scholar | `google-scholar` | `ai` |

The body below the front matter is the longer biography on the profile page.

Images: upload one square photo named `avatar.jpg` or `avatar.png`, at most 5 MiB.
Keep only one avatar file in the folder, because the site shows only the first one it finds.
Without a photo, the People page shows the initials.

To update a person, open `content/authors/<folder>/_index.md` and select the pencil icon.
When a member leaves the lab, set `user_groups` to `Former Members`.
Former members may omit `email`.
Keep the folder, because their publications still link to it.

Common mistakes:

- A folder name that does not match the title.
  The check reports `author slug must be '...'` with the right name.
- A group spelled differently, such as `Member`.
  The check reports `user_groups must be exactly one of ...`.
- A name spelled differently in publications, which leaves those publications off the profile.

### Add a thesis

**Start:** [create `content/theses/2026firstnamelastname/index.md`](https://github.com/nlp-unibo/nlp-unibo.github.io/new/hugoblox-template?filename=content/theses/2026firstnamelastname/index.md&value=---%0Atitle%3A%20%22TODO%3A%20Thesis%20title%22%0Aauthors%3A%0A%20%20-%20%22TODO%3A%20Student%20Name%22%0A%23%20The%20graduation%20date%2C%20YYYY-MM-DD%0Adate%3A%20%22TODO%3A%20YYYY-MM-DD%22%0Adoi%3A%20%22%22%0Apublication_types%3A%0A%20%20-%20thesis%0Apublication%3A%20%22%22%0Apublication_short%3A%20%22%22%0Aabstract%3A%20%22%22%0Asummary%3A%20%22%22%0A%23%20For%20a%20bachelor%20thesis%2C%20write%20bachelor%20thesis%20here%20and%20Bachelor%20thesis%20in%20categories.%0Atags%3A%0A%20%20-%20master%20thesis%0A%20%20-%20student%0A%23%20The%20AMS%20Laurea%20record%2C%20when%20it%20exists%0Aurl_pdf%3A%20%22%22%0Acategories%3A%0A%20%20-%20Master%20thesis%0A%23%20One%20to%20three%20keys%20from%20data%2Ftopics.yaml%0Atopics%3A%20%5B%5D%0A---%0A)

Name the folder after the year and the student's name, without hyphens, such as `2026mariarossi`.

| Field | Required | Example | Rule |
| --- | --- | --- | --- |
| `title` | Required | `"AI solutions for ..."` | The thesis title |
| `authors` | Required | `- Maria Rossi` | The student's name |
| `date` | Required | `2026-03-20` | The graduation date |
| `publication_types` | Required | `- thesis` | Keep `thesis` |
| `categories` | Required | `- Master thesis` | `Master thesis` or `Bachelor thesis`. It sets the kind under "Work done with students" |
| `tags` | Optional | `- master thesis` | Keep `master thesis` and `student`, or `bachelor thesis` and `student` |
| `url_pdf` | Optional | `https://amslaurea.unibo.it/...` | The thesis record, such as its AMS Laurea page, when it exists |
| `topics` | Optional | `[llms, legal]` | One to three topic keys. They feed the topic filter under "Work done with students" |
| `abstract`, `summary` | Optional | | Leave them empty when you have no text |

A thesis needs no image and no body.

What else to update: when the thesis led to a paper, add the paper as a publication with the tag `student publication`.

Common mistakes:

- A bachelor thesis left with `Master thesis` in `categories`.
- Topic keys that do not exist.
  The check reports `topic '...' is not defined in data/topics.yaml`.

### Add a research proposal

**Start:** [create `content/proposals/legal/short-name/index.md`](https://github.com/nlp-unibo/nlp-unibo.github.io/new/hugoblox-template?filename=content/proposals/legal/short-name/index.md&value=---%0Atitle%3A%20%22TODO%3A%20Proposal%20title%22%0Adate%3A%20%22TODO%3A%20YYYY-MM-DD%22%0A%23%20One%20sentence%20of%20about%2018%20words%2C%20shown%20on%20the%20card%0Asummary%3A%20%22TODO%3A%20One%20sentence%20that%20says%20what%20the%20proposal%20does.%22%0A%23%20Two%20to%20four%20sentences%2C%20at%20most%2070%20words%2C%20shown%20on%20the%20opened%20card%0Abrief%3A%20%22TODO%3A%20The%20problem%2C%20the%20idea%2C%20and%20what%20a%20student%20would%20do.%22%0A%23%20Folder%20names%20in%20content%2Fauthors%2C%20or%20%7Bname%3A%20Full%20Name%2C%20email%3A%20address%7D%20for%20a%20person%20outside%20the%20lab%0Acontacts%3A%0A%20%20-%20TODO-folder-name%0A%23%20Plain%20words%2C%20not%20abbreviations.%20The%20opened%20card%20shows%20the%20first%20three.%0Atags%3A%0A%20%20-%20TODO%20tag%0A---%0A%0A%3C%21--%20The%20body%20is%20optional.%20Without%20it%2C%20the%20proposal%20page%20shows%20the%20brief.%20Delete%20all%20sections%20below%20to%20skip%20it.%20--%3E%0A%0A%23%23%20Context%0A%0ATODO%3A%20The%20research%20setting%2C%20with%20every%20technical%20term%20defined%20at%20its%20first%20use.%0A%0A%23%23%20Objective%0A%0ATODO%3A%20What%20the%20proposal%20aims%20at%2C%20in%20one%20or%20two%20sentences.%0A)

Research proposals are grouped by topic under `content/proposals/`.
Each topic is a folder whose `_index.md` holds the topic title, its `summary`, and its description.
The topics today are `argument-mining`, `interpretability`, `legal`, and `unstructured-knowledge`.
In the file name box, replace `legal` with the topic folder and `short-name` with your slug.

```text
content/proposals/legal/
├── _index.md          the topic: title, summary, description
├── am/index.md        one proposal
└── unfairclauses/index.md
```

The Work with us page lists every proposal as a card, with a filter by topic.
On phones the cards form one row that scrolls sideways.
Opening a card shows the `brief`, the contacts, the first three tags, **Choose this proposal**, and a **Full proposal** link when the proposal has a body.
A reader who chooses a proposal writes to its contacts.

| Field | Required | Example | Rule |
| --- | --- | --- | --- |
| `title` | Required | `Argument Mining on Legal Datasets` | The proposal title |
| `date` | Required | `2026-03-02` | The day you add it |
| `summary` | Required | `"Mine the arguments of legal documents ..."` | One sentence of about 18 words, shown on the card |
| `brief` | Required | `"Argumentation in legal documents ..."` | Two to four sentences, at most 70 words: the problem, the idea, and what a student would do |
| `contacts` | Required | `- andrea-galassi` | Folder names in `content/authors/`. For a person outside the lab, write `{name: Maria Rossi, email: maria.rossi@unibo.it}` |
| `tags` | Optional | `- legal analytics` | Plain words, not abbreviations. The card shows the first three |
| `math` | Optional | `true` | Set it when the body uses LaTeX |

The body is optional.
It is the proposal page, in the style of a publication page.
Use `##` sections such as `Context`, `Objective`, `Directions`, and `References`.
On wide screens they appear in a side menu that marks the current section.
Define every technical term at its first use.

Some proposals add a `pipeline` flow diagram, built only from the proposal's own definitions and captioned as such.
Copy one from an existing proposal.
Without a body, the proposal page shows the `brief`, and the card shows no **Full proposal** link.

To add a new topic, create its `_index.md` first.
**Start:** [create `content/proposals/new-topic/_index.md`](https://github.com/nlp-unibo/nlp-unibo.github.io/new/hugoblox-template?filename=content/proposals/new-topic/_index.md&value=---%0Atitle%3A%20%22TODO%3A%20Topic%20title%22%0Asummary%3A%20%22TODO%3A%20One%20sentence%20on%20the%20topic.%22%0A---%0A%0ATODO%3A%20A%20short%20description%20of%20the%20topic%2C%20in%20a%20few%20sentences.%0A)
A topic needs `title` and `summary`.

Common mistakes:

- A contact that is not a folder name, such as `Andrea Galassi` instead of `andrea-galassi`.
  The build fails with `contact "..." is not in content/authors`.
- A contact whose profile has no `email`, such as a former member.
  The build fails with `author "..." has no email`.
- A proposal saved directly in `content/proposals/` instead of inside a topic folder.

### Add a project

**Start:** [create `content/projects/acronym/index.md`](https://github.com/nlp-unibo/nlp-unibo.github.io/new/hugoblox-template?filename=content/projects/acronym/index.md&value=---%0A%23%20End%20with%20the%20acronym%20in%20brackets%3A%20it%20becomes%20the%20card%20headline.%0Atitle%3A%20%22TODO%3A%20Full%20Project%20Name%20%28ACRONYM%29%22%0A%23%20The%20project%20start%2C%20YYYY-MM-DD%0Adate%3A%20%22TODO%3A%20YYYY-MM-DD%22%0A%23%20One%20or%20more%20keys%20from%20data%2Ftopics.yaml%0Atopics%3A%0A%20%20-%20TODO-topic%0Asummary%3A%20%22TODO%3A%20One%20sentence%20on%20the%20project.%22%0A%23%20The%20project%20website%0Aexternal_link%3A%20%22https%3A%2F%2FTODO%22%0A%23%20International%20project%20or%20National%20project%0Acategories%3A%0A%20%20-%20National%20project%0A---%0A)

Projects have no page of their own, so the file needs no body.
The card links straight to the project website.

| Field | Required | Example | Rule |
| --- | --- | --- | --- |
| `title` | Required | `Argument Mining In Covid-19 Articles (AMICA)` | End with the acronym in brackets. The card shows the acronym as its headline and the rest below it |
| `date` | Required | `2021-01-01` | The project start. It orders the cards and places the project on the timeline |
| `summary` | Required | `"The AMICA project ..."` | One sentence, shown on the card with the start year |
| `external_link` | Required | `http://amica.unimore.it/` | The project website, opened by the Website chip |
| `topics` | Required | `- argument-mining` | One or more topic keys, shown as tags and used by the topic filter |
| `categories` | Required | `- National project` | `International project` or `National project`. It sets the scope label, the timeline color, and the scope filter |

Common mistakes:

- A title without the acronym in brackets, which leaves the card without a short headline.
- A `categories` value spelled differently, such as `national project`.

### Add a tool

**Start:** [create `content/tools/tool-name/index.md`](https://github.com/nlp-unibo/nlp-unibo.github.io/new/hugoblox-template?filename=content/tools/tool-name/index.md&value=---%0Atitle%3A%20%22TODO%3A%20Tool%20name%22%0A%23%20The%20first%20public%20release%2C%20YYYY-MM-DD.%20It%20orders%20the%20Tools%20page.%0Adate%3A%20%22TODO%3A%20YYYY-MM-DD%22%0A%23%20One%20or%20more%20keys%20from%20data%2Ftopics.yaml%0Atopics%3A%0A%20%20-%20toolkit%0A%23%20Web%20service%2C%20Web%20demo%2C%20or%20Python%20library%0Akind%3A%20Python%20library%0Asummary%3A%20%22TODO%3A%20What%20the%20tool%20does%2C%20in%20at%20most%20two%20sentences.%22%0A%23%20The%20tool%20website%0Aexternal_link%3A%20%22https%3A%2F%2FTODO%22%0A%23%20Optional%3A%20remove%20the%20%23%20to%20use%20a%20line.%0A%23%20schema%3A%20schema.svg%0A%23%20caption%3A%20%22What%20the%20schematic%20shows%20and%20where%20it%20comes%20from.%22%0A%23%20demo%3A%20%22https%3A%2F%2F...%22%0A%23%20code%3A%20%22https%3A%2F%2Fgithub.com%2Fnlp-unibo%2F...%22%0A%23%20publication%3A%20folder-name-in-content-publication%0A%23%20license%3A%20MIT%0A%23%20package%3A%20pypi-name%0A---%0A)

The Tools page lists only systems that readers can use today: an online service or demo, or an installable package.
A system built only to demonstrate a paper is a prototype.
Give its publication or thesis the `prototype` topic instead.
Each tool is one band, with a schematic on the left and its description on the right.
The address of the tool redirects to `external_link`.

| Field | Required | Example | Rule |
| --- | --- | --- | --- |
| `title` | Required | `MAMKit` | The tool name |
| `date` | Required | `2024-08-08` | The first public release. It orders the bands, newest first, and is not displayed |
| `summary` | Required | `"MAMKit is an open-source ..."` | At most two sentences |
| `external_link` | Required | `https://nlp.unibo.it/mamkit/` | The tool website |
| `topics` | Required | `[argument-mining, toolkit]` | One or more topic keys |
| `kind` | Optional | `Python library` | Shown as a pill, such as `Web service`, `Web demo`, or `Python library` |
| `demo` | Optional | `https://...` | A web demo, shown as a chip |
| `code` | Optional | `https://github.com/nlp-unibo/mamkit` | The source code, shown as a chip |
| `publication` | Optional | `mancini-etal-2024-mamkit` | The folder name of the paper under `content/publication/`, shown as a Paper chip |
| `license` | Optional | `MIT` | The license of the public code. It shows an open-source pill |
| `package` | Optional | `mamkit` | The PyPI name. It shows the `pip install` command |
| `schema`, `caption` | Optional | `schema.svg` | A schematic and a caption that names its source |

In the template, the optional fields start with `#`.
Remove the `#` and the space after it to use a field.

The schematic is an SVG file in the tool folder, drawn with the site's `lt-s-*` style classes so that it follows the site colors.
Drawing one needs some code, so ask the maintainer for it, or leave `schema` out.

Common mistakes:

- A `publication` value that names no existing folder.
  The build fails with `publication "..." not found`.
- A `schema` value whose file you did not upload.
  The build fails with `tool schema "..." not found`.

### Add a research area

**Start:** [create `content/research/short-name/index.md`](https://github.com/nlp-unibo/nlp-unibo.github.io/new/hugoblox-template?filename=content/research/short-name/index.md&value=---%0Atitle%3A%20%22TODO%3A%20Research%20area%20name%22%0Adate%3A%20%22TODO%3A%20YYYY-MM-DD%22%0Atags%3A%0A%20%20-%20research%0Asummary%3A%20%22TODO%3A%20One%20sentence%20on%20the%20area.%22%0A%23%20A%20Font%20Awesome%205%20solid%20icon%20name%2C%20such%20as%20comments%20or%20balance-scale%0Aicon%3A%20comments%0A%23%20Position%20on%20the%20homepage%20and%20the%20Research%20page.%20Lower%20comes%20first.%0Aweight%3A%2010%0A%23%20At%20most%2012%20words%2C%20shown%20on%20the%20homepage%20card%0Atagline%3A%20%22TODO%3A%20Tagline%22%0A%23%20dots%2C%20graph%2C%20tokens%2C%20or%20wave%0Acover_pattern%3A%20dots%0Afields%3A%0A%20%20-%20key%3A%20first-field%0A%20%20%20%20title%3A%20%22TODO%3A%20Block%20title%22%0A%20%20%20%20icon%3A%20search%0A%20%20%20%20question%3A%20%22TODO%3A%20The%20question%20this%20family%20of%20tasks%20answers.%22%0A%20%20%20%20summary%3A%20%22TODO%3A%20One%20or%20two%20sentences.%22%0A%20%20%20%20tasks%3A%0A%20%20%20%20%20%20-%20name%3A%20%22TODO%3A%20Task%20name%22%0A%20%20%20%20%20%20%20%20text%3A%20%22TODO%3A%20Given%20an%20input%2C%20the%20task%20is%20to%20produce%20an%20output.%22%0A%23%20status%3A%20done%20%28Explored%29%2C%20now%20%28Current%29%2C%20or%20next%20%28Future%29.%20cite%3A%20publication%20folder%20names.%0Afocus%3A%0A%20%20-%20key%3A%20first-topic%0A%20%20%20%20title%3A%20%22TODO%3A%20Topic%20title%22%0A%20%20%20%20icon%3A%20comments%0A%20%20%20%20summary%3A%20%22TODO%3A%20At%20most%20two%20sentences.%22%0A%20%20%20%20description%3A%20%22TODO%3A%20Two%20to%20four%20sentences%20for%20a%20reader%20outside%20the%20field.%22%0A%20%20%20%20items%3A%0A%20%20%20%20%20%20-%20status%3A%20done%0A%20%20%20%20%20%20%20%20text%3A%20%22TODO%3A%20Short%20bullet%20of%20at%20most%2012%20words.%22%0A%20%20%20%20%20%20%20%20detail%3A%20%22TODO%3A%20Two%20or%20three%20sentences%20on%20what%20was%20done.%22%0A%20%20%20%20%20%20%20%20cite%3A%20%5B%5D%0A---%0A%0A%23%23%20What%20is%20TODO%3F%0A%0ATODO%3A%20Define%20the%20research%20area%20in%20three%20or%20four%20plain%20sentences.%0A)

A research area is the largest page of the site, and the homepage shows one card per area.
Agree on a new area with the maintainer first.
The easiest start is to copy `content/research/am/index.md` and replace its content.

| Field | Required | Example | Rule |
| --- | --- | --- | --- |
| `title` | Required | `Argument Mining` | The area name. The page header shows it alone |
| `date` | Required | `2026-02-27` | The day you add it |
| `summary` | Required | `"The automatic identification ..."` | One sentence |
| `tagline` | Optional | `"Extracting, linking, evaluating ..."` | At most 12 words, shown on the homepage card and the Research page |
| `icon` | Optional | `network-wired` | A [Font Awesome 5](https://fontawesome.com/v5/search?m=free&s=solid) solid icon name |
| `weight` | Optional | `1` | Orders the cards. Lower values appear first |
| `cover_pattern` | Optional | `graph` | `dots`, `graph`, `tokens`, or `wave` |
| `definition` | Optional | Markdown text | A short answer to "What is ...?" in a box under the title |
| `fields` | Optional | see template | One block per family of tasks. Each `key` must be unique |
| `focus` | Optional | see template | The lab topics, with `items` of status `done`, `now`, or `next`. Each `key` must be unique |

How the parts work:

- The Research page gives each area a full-width band.
  The band starts with a mosaic of its `overview` schemas and the tagline.
  It then shows the first line of `definition` without citations, the `focus` topic titles, and the number of focus items by status.
  The one-sentence `intro` of the Research page lives in `content/research/_index.md`.
- Define the area in plain words, either in the body under a `## What is ...?` heading or in `definition`.
- Optional `overview` shows concept blocks under a "Core concepts" heading, two per row.
  Each block has an `icon`, a `title`, a short `text`, and an optional `schema` SVG file in the page folder.
- Optional `concepts` gives the background of the examples in a few Markdown paragraphs above the views.
  It holds the notions the examples rely on, not a list of tasks.
  Its heading is `views_title`, "Core concepts" by default.
- The body, the definition, the core concepts, and the views share the first section band.
- `fields` lists the families of tasks.
  Each block has a `title`, an `icon`, a `question`, a `summary`, and `tasks` that state their input and expected output.
  Selecting a block enlarges it and opens its tasks beside it.
- `focus` lists the lab topics, which rotate in a carousel.
  Each topic has a card `summary`, a longer `description`, and `items` marked `done` (Explored), `now` (Current), or `next` (Future).
  An item has a short `text` for the card and a `detail` for the box below the carousel.
  An Explored item cites publications in `cite` by folder name, and the box lists them on the right.
  The topic titles appear as chips on the homepage card.

Interactive views (optional `views`) add tabs under the background, one per argument model or domain.
They are detailed data, so copy an existing view and change its text:

- Argument views show one argument as marked text and as a graph, side by side on wide screens and stacked on narrow ones.
  Each view has `roles`, `segments`, `rows`, and `edges`.
  Use `texts` instead of `segments` to show several texts side by side, such as a clause and its translation.

  An `implicit` component, which the text leaves unstated, appears in a dashed box.
  One with `kind: label` is a label assigned by the annotation, such as a category.
  Mark [...] where text is omitted, and link the source of each example by name in its `caption`.
  A graph view can set `graph_title` to rename its graph panel, such as Clause alignment for the cross-lingual view.
  Copy the views of `content/research/am/index.md`.
- A view with `type: detect` shows a document as `document` and `sections`, each with a `title` and `sentences`.
  A marked sentence has a `category` and a `level`: 1 clearly fair, 2 potentially unfair, or 3 clearly unfair.
  Copy the `terms` view of `content/research/legal/index.md`.
- A view with `type: rules` also shows a document, where each clause about personal data has a `level`, a `rule`, and `parts`.
  A part is plain `text`, or a mark with a `role` (category, specification, or subcategory) and a `type` (open or closed).
  The view lists its annotation `rules`, each with a `level`, a number `n`, and the type that each element needs (open, closed, any, or none).
  The check fails when the marks of a clause do not match the rule it names.
  Copy the `privacy` view of `content/research/legal/index.md`.
- A view with `type: voices` shows `readings` of short sentences as cue strips, beside a table of `models`.
  Each word has `w`, a duration `dur`, an optional `pause`, a `pitch` pair from 0 to 1, and a `loud` value from 0 to 1.
  Each reading has a `label`, a `summary`, and a `gold` answer.
  Each model gives one of `answers` per reading.
  Keep sentences to about four words, so that a strip fits a phone without scrolling.
  Say in the caption that the cues and answers are constructed.
  The check fails without readings and a `question`, on a value outside these ranges, or when a model does not give one answer per reading.
  Copy the views of `content/research/speech/index.md`.

Common mistakes:

- A `cite` entry that names no existing publication folder.
  The check reports `focus item cites unknown publication '...'`.
- A missing or repeated `key` in `fields`, `focus`, or `views`.
- A focus `status` other than `done`, `now`, or `next`.

### Edit the homepage

**Start:** [edit `content/_index.md`](https://github.com/nlp-unibo/nlp-unibo.github.io/edit/hugoblox-template/content/_index.md)

The homepage is a list of four blocks: the hero, the Research map, the News, and the Latest papers.
You can change the texts of each block in this file.
They are the hero texts (`eyebrow`, `title`, `text`) and the `title` of each section.
You can change how many items a block shows: `count` and `featured` for the News block, and `count` for Latest papers.
The blocks choose their items themselves, so you add content through the other recipes, not here.

| Block | Shows |
| --- | --- |
| `lt-hero` | The lab logo and the hero texts. A hero button that points to an unpublished page is hidden |
| `lt-research` | One card per research area, ordered by `weight` |
| `lt-news` | The newest news items (6 by default, the first 3 as cards). Publications never appear here |
| `lt-papers` | The newest publications by `date` (3 by default), preprints included |

Ask the maintainer to review every homepage change, because it affects the first page every visitor sees.

### Edit the menu

**Start:** [edit `config/_default/menus.yaml`](https://github.com/nlp-unibo/nlp-unibo.github.io/edit/hugoblox-template/config/_default/menus.yaml)

Each menu entry has a `name`, a `url`, and a `weight`.
Lower `weight` values appear first.
An entry with `parent: <identifier>` appears in the dropdown of the entry with that `identifier`.
The full menu fits on one line on screens at least 1280 pixels wide.
After adding an entry, ask the maintainer to check that the menu still fits on one line, and shorten a label if it wraps.
Every menu change needs review by the maintainer.

### Edit a page introduction

The Research, Projects, Tools, People, and News pages open with one sentence instead of their title.
Edit it in the `intro` field of `content/research/_index.md`, `content/projects/_index.md`, `content/tools/_index.md`, `content/people/index.md`, or `content/news/_index.md`, in at most 25 words.

### Edit the Work with us page

**Start:** [edit `content/work-with-us/index.md`](https://github.com/nlp-unibo/nlp-unibo.github.io/edit/hugoblox-template/content/work-with-us/index.md)

The file holds the page as data.
Ask the maintainer to review every change, because the page sends emails to the lab.

- `contacts` lists the people who receive every message, as folder names in `content/authors/`, whose `email` field is used.
  A path may set its own `contacts`.
- `paths` has one entry per card under "What are you looking for?".
  Each path has a `key`, its anchor, such as `/work-with-us/#thesis`.
  It also has a card `label` and `summary` of at most two sentences, an `icon`, a `title`, and Markdown `who` and `what`.
- Its `steps` appear as a numbered list after the path card.
  On wide screens, a side menu beside the open path links to its summary and to each step.
  Each step has a `title`, Markdown `text`, and an optional `show`.
  The `show` field places a section in the step.
  The sections are `proposals` (the research proposals, with a topic filter), `projects` (the three most recent projects), and `contact` (the email form).
- `inspiration: student-work` adds a last, unnumbered step with the work done with students.
- Its `form` sets the email `subject`, which may name fields in braces such as `{proposal}`, and the `fields` to fill.
  A field with `when`, such as `when: {funding: I need funding from the lab}`, appears only while the named field has that value.
  A select field with `options: proposals` lists the research proposals.
  A text field with `options: proposals` receives the title chosen with **Choose this proposal**.
- The form opens the visitor's email app with recipients, subject, and body filled in.
  Nothing passes through the site.
- Without JavaScript the path cards are hidden, and every path and the research proposals are visible.
  The work done with students then stays collapsed, and each path offers a plain email link with the same subject and an empty template.

## 4. Change existing content

Every change to an existing page follows the same steps.
Find the file, edit it on the GitHub website, and publish the change as in [Publish your change](#5-publish-your-change).

### Find and edit a file

1. Open the page on the site and note its address, for example `/publication/rossi-etal-2026-example/`.
2. Find the matching file with the table below.
3. On GitHub, open the file and select the pencil icon (**Edit this file**).
4. Change the text, then select **Commit changes** and choose **Create a new branch for this commit and start a pull request**.

| Page on the site | File to edit |
| --- | --- |
| Homepage blocks and their titles | `content/_index.md` |
| A publication, `/publication/<slug>/` | `content/publication/<slug>/index.md` |
| A news item on the News page | `content/news/<slug>/index.md` |
| A person, `/author/<name>/` | `content/authors/<name>/_index.md` |
| A research area, `/research/<slug>/` | `content/research/<slug>/index.md` |
| A research proposal, `/proposals/<topic>/<slug>/` | `content/proposals/<topic>/<slug>/index.md` |
| A project or a tool | `content/projects/<slug>/index.md` or `content/tools/<slug>/index.md` |
| The introduction of a list page, such as Publications or Tools | `_index.md` in the folder of that section |
| The Work with us page | `content/work-with-us/index.md` |
| The menu | `config/_default/menus.yaml` |

A file has two parts.
The front matter, between the two `---` lines, holds named fields such as `title` and `summary`.
The body, after the second `---`, holds the text of the page.
Research area pages and the Work with us page keep almost all their text in front matter fields, so edit the field that holds the sentence you want to change.
Use the search box of GitHub (press `/` in the repository) to find a sentence when you are not sure which file holds it.

### Remove a paper from the Highlights carousel, or add one

The Highlights carousel of the Publications page shows every publication whose `categories` list includes `Highlight`.

1. Open `content/publication/<slug>/index.md`.
2. In `categories`, delete the line `  - Highlight`, and keep the type line (`Journal`, `Conference`, `Workshop`, or `Preprint`).
3. Commit to a new branch and open a pull request.

To add a paper to the carousel, add the line `  - Highlight` under its type.
A highlighted paper needs a `featured.png` image and a `summary`, because its carousel card shows them.

```yaml
categories:
  - Conference
  - Highlight
```

### Change the text of a page

- **A sentence in a field:** edit the value after the field name.
  Keep the quotes when the value has them, and keep the indentation of the line.
- **A paragraph in a field that starts with `|`:** the text continues on the indented lines below.
  Edit those lines and keep their indentation.
- **The body of a page:** edit the text after the second `---` line as normal text.
  Markdown formatting applies: `**bold**`, `*italic*`, and `[link text](https://...)`.
- **A date:** use the form `YYYY-MM-DD`.
  On publications and news, the date also moves the item on the News timeline.

### Replace an image

Upload the new image into the same folder with the same file name, for example `featured.png`.
GitHub replaces the old file in your branch.
Keep the image size close to the old one, so the page layout does not change.

### Reorder items

People and research areas are ordered by `weight`: a lower number comes first.
Items inside a list field, such as the concept blocks of a research area, keep their order in the file.
Publications, news items, projects, and tools are ordered by `date`, newest first.
Change these fields to reorder items.

### Hide or remove a page

- **Hide a page for a while:** add the line `draft: true` to its front matter.
  The page disappears from the site but stays in the repository.
  Delete the line to show the page again.
- **Remove a page for good:** delete its whole folder.
  On GitHub, open each file of the folder and select **Delete file** from the `...` menu, all in the same branch.
  The check fails when another page still points to the removed one.
  For example, a research area may cite a deleted publication in `cite`, or a tool may name it in `publication`.
  Remove those references in the same pull request.
- **A person who leaves the lab:** do not delete the profile, because their publications link to it.
  Change `user_groups` to `Former Members`.

### Add a schema to a page

A schema is a small drawing, such as the claim and premise graphs on the Argument Mining page.
Schemas are SVG files: text files that describe shapes, which the site colors to match its style.

**Change the words of an existing schema.**
Open the SVG file in the page folder, for example `content/research/am/schema-relations.svg`.
Each `<text ...>Claim</text>` line holds one label: change the word between `>` and `<`.
Also update the `aria-label` on the first line, which describes the drawing for screen readers.
Keep labels short, because a longer word may overflow its box.

**Add a new schema to a research area.**

1. Copy an existing schema of the same page, which already uses the right style classes.
   Open it, select **Raw**, copy the text, and create a new file in the same folder, such as `schema-new.svg`.
2. Change the labels as above.
   Moving or adding boxes means changing the `x`, `y`, `width`, and `height` numbers; ask the maintainer when the drawing needs a new shape.
3. Point a concept block to the file by its name, in the `overview` list of the research area:

   ```yaml
   overview:
     - icon: project-diagram
       title: Relations
       text: "One short paragraph about the concept."
       schema: schema-new.svg
   ```

Each `overview` block shows under "Core concepts" on the research area page, and its schema also joins the mosaic of that area on the Research page.
A tool takes one schema in its `schema` field.
A publication blog page shows a schema with `{{< svg src="schema-new.svg" caption="What it shows." >}}` in its body.

Draw only with the style classes that the existing schemas use, such as `lt-s-node`, `lt-s-txt`, `lt-s-arrow`, `lt-s-support`, and `lt-s-attack`.
Never set colors in the file: the classes give the site colors.
The full list of classes is in the developers' guide, section 5, under [`svg`](developers.md#svg).
The build fails with `overview schema "..." not found` when a block names a file that is not in the folder.

## 5. Publish your change

### Open a pull request

1. Create or edit the file through a **Start** link or the pencil icon.
2. Select **Commit changes**.
3. Choose **Create a new branch for this commit and start a pull request**.
   Give the branch a short name such as `news/acl-2026`.
4. Select **Propose changes**, then **Create pull request**.
   Make sure the base branch is `hugoblox-template`.
5. Fill in the short template: say what the change does, and tick the boxes that apply.
6. Add images or other files to the same branch, as described in [Add images and files](#add-images-and-files).

To change a file again before merging, open it on your branch and edit it there.
The check runs again after each commit.

### Read the check result

At the bottom of the pull request, GitHub shows the **Validate content and build** check.

- A yellow dot means the check is still running.
  It takes a few minutes.
- A green tick means the site builds with your change.
- A red cross means the check found a problem.

To read the problem, select **Details** next to the red cross.
Open the step **Validate content and production build**.
Each problem is one line that starts with the file name.

### Merge

When the check is green, read your change once more against this list:

- [ ] The title, names, dates, venue, DOI, and links are correct.
- [ ] Every `TODO` text is gone, and `draft: true` is removed from pages meant to be public.
- [ ] Every image or PDF is at most 5 MiB, and its file name has no spaces.
- [ ] No private data, credentials, internal ratings, or copyrighted files were added.

Then select **Merge pull request**, or ask the maintainer to merge it.
The site updates a few minutes after the merge.
To follow the update, open the **Actions** tab and select the **Deploy Hugo site to Pages** run.
Then check your page on <https://nlp.unibo.it/>, on a computer and on a phone.

### When the check fails

The table lists the messages of the check and how to fix each one.
`...` stands for a name or value that the message fills in.

| Message | Meaning and fix |
| --- | --- |
| `required field '...' is empty` | The named field is missing or empty. Add it to the front matter |
| `contains TODO marker` | A `TODO` text from the template is still there. Replace it, or add `draft: true` until the page is ready |
| `contains example domain` or `contains example email` | A template address such as `example.org` or `test@example.org` is still there. Replace it with the real one |
| `contains Lorem ipsum` or `contains publication boilerplate` | Placeholder text from an old template is still there. Replace it |
| `categories must be exactly one of ...` | The `categories` value is missing, misspelled, or repeated. Copy one allowed value from the message |
| `categories must list Highlight at most once` | Remove the second `Highlight` |
| `publication_types must be exactly one of ...` | Use one value from the message, as described in [Add a publication](#add-a-publication) |
| `user_groups must be exactly one of ...` | Use exactly one of `Members`, `Associate Fellows`, or `Former Members` |
| `author slug must be '...'` | A person's folder name does not match their `title`. Create the folder with the name the message shows |
| `authors term '...' conflicts with '...'` | The same person is written in two ways, for example with and without an accent. Use the spelling of their profile |
| `tags term '...' conflicts with '...'` | The same tag is written in two ways, for example `semeval` and `SemEval`. Use the spelling of the existing tag |
| `topic '...' is not defined in data/topics.yaml` | Use a topic key from the list in [Where files go](#where-files-go) |
| `email link '...' must start with mailto:` | Write email links as `[Name](mailto:name@unibo.it)` |
| `local link '...' does not exist` | A link points to a missing file. Check the spelling and capitals, and upload the file to the page folder |
| `invalid slug '...'` | The folder name contains capitals, spaces, or other characters. Use lowercase letters, numbers, and hyphens only |
| `missing page index` | The folder has no `index.md` (or `_index.md` for a person or a proposal topic). Check the file name |
| `pages must be folders with an index.md` | A page was saved as `name.md` directly in a section. Save it as `name/index.md` instead |
| `... MiB exceeds 5 MiB asset limit` | Compress the image or PDF, then upload it again |
| `missing YAML front matter between --- lines` | The file must start with a `---` line. Restore it |
| `missing closing YAML delimiter` | The second `---` line is missing. Restore it |
| `front matter must be a YAML mapping` | The front matter is not a list of `name: value` lines. Compare it with the template |
| `repeated key ...` | The same field appears twice in the front matter. Keep one of them |
| A YAML error with a line number | The front matter layout is broken. Check tabs, indentation, quotes, and both `---` lines near that line |
| `fields key '...' is missing or repeated` (also `focus` and `views`) | Give every block of a research area its own `key` |
| `focus item status must be done, now, or next` | Fix the `status` of a focus item |
| `focus item cites unknown publication '...'` | The `cite` list names a folder that does not exist in `content/publication/`. Fix the folder name |
| `view '...': ...` | An interactive view of a research area is inconsistent. Compare it with the view you copied, or ask the maintainer |
| `publication "..." not found for ...` | A tool names a missing publication folder in `publication`. Fix the folder name |
| `tool schema "..." not found in ...` | A tool names a schematic file you did not upload. Upload it, or remove `schema` |
| `contact "..." is not in content/authors` | A proposal or the Work with us page names a contact folder that does not exist. Fix the folder name |
| `author "..." has no email` | A contact's profile has no `email`. Add it, or choose another contact |
| `contact ... needs a name and an email` | A contact outside the lab needs both `name` and `email` |

Two messages are only warnings, and the check still passes:

| Warning | Meaning |
| --- | --- |
| `future publication date ...` | The page is valid but stays hidden until its date |
| `missing cite.bib` | The publication has no BibTeX file, so its Cite button is missing. Add `cite.bib` |

Some problems produce no message:

- A page is missing from the site when it still has `draft: true`, when its date is in the future, or when it sits in the wrong folder.
- A publication is missing from a list when its `categories` value selects another list.
- An image is missing when the file name in the text differs from the uploaded file, including capitals.
- A change is not visible while the deployment is still running.
  Wait a few minutes, then reload the page without the browser cache.

When you cannot fix a failure, write a comment on the pull request and ask the maintainer.

## 6. Publication blog pages

A publication can have a long body: a page that tells the story of the paper, like the project pages that research groups publish.
31 of the 77 publications have one today, such as `content/publication/ruggeri-et-al-2026-gcam/`.
Such a page explains the paper to a reader outside the field, in five sections: **Research setting**, **Motivation**, **Approach**, **Results**, and **Takeaways**.
It uses visual components such as figures, method diagrams, and result charts.

Writing one follows a brief from the maintainer, which sets the structure and the style of every page.
Ask the maintainer for it before you start.
You may leave the body empty: the page then shows the abstract, and you or someone else can add the long page later.

The page answers four questions for a reader outside the field:

1. What is the paper about?
2. Which research topics does it cover?
3. Why was the work needed, and what did it aim for?
4. What did it find, and what should a reader take away?

Base every statement on the paper, and leave the details to the paper itself.
Keep the five sections in every page, so that all pages share one structure.

For reference, the body can use these components.
Each component except `figure` and `svg` takes YAML between its opening and closing tags.
The publication templates in `archetypes/` show an example of each one.

| Component | Shows |
| --- | --- |
| `figure` | A figure from the paper, saved in the page folder. Reuse a figure only when its source is openly licensed, such as arXiv, the ACL Anthology, or CEUR-WS |
| `svg` | A schema drawn for the page as an SVG file, which follows the site colors |
| `gap` | A table that compares the paper with related work, with one row marked `ours: true` |
| `pipeline` | A method diagram with three to five steps, with optional parallel branches inside a step |
| `stages` | An interactive diagram with one tab per stage, which shows whether each component is optimized, trained, or frozen |
| `numbers` | Two to four headline numbers, placed in **Results** after the text that explains them |
| `bars` | An interactive bar chart of one metric, with optional standard deviations and a table view |
| `annotate` | An annotated text example with up to four labels, which readers can filter |
| `takeaways` | Three numbered takeaway cards |

The page is self-contained, so its text cites no other publication.
Never show a number or a term before the text has given its context.
Each `##` heading also appears in the section menu below the teaser.
