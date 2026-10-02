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
  - [Add a challenge or workshop suggestion](#add-a-challenge-or-workshop-suggestion)
  - [Add a research area](#add-a-research-area)
  - [Add a tool](#add-a-tool)
  - [Publish the Work with us page](#publish-the-work-with-us-page)
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
| `categories` | Exactly one of `Journal`, `Conference`, `Workshop`, or `Preprint`, which selects the list on the Publications page. Add `Highlight` as a second value to also list the paper under Highlights |
| `abstract` | The abstract |
| `doi` | The DOI without `https://doi.org/`, for example `10.18653/v1/2024.argmining-1.7` |
| `url_pdf`, `url_code`, `url_dataset` | Optional links that appear as buttons |
| `award` | Optional award name, for example `Best Paper Award`. It appears with a trophy under the title in every publication list |
| `tags` | Topic keywords. Add `student publication` to show the paper on the For Students page |

A `Highlight` publication appears both under Highlights and in its venue list.
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

The homepage shows the five most recent news items automatically.
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
3. Set `first_name`, `last_name`, `role`, `bio`, `interests`, `email`, and the `social` links.
4. Set `user_groups` to one of `Head`, `Academic Members`, `Research Fellows`, or `PhD Students`, with this exact spelling.
   The group selects the section of the People page.
5. Keep `highlight_name: true`, which shows the member in bold in author lists.
6. Upload a square photo as `avatar.jpg` or `avatar.png`, at most 5 MiB.

To remove a former member from the People page, set their `user_groups` to `Alumni`.
The People page shows only the four groups above, and validation requires a group.
Keep the folder, because their publications still link to it.

### Add a thesis

1. Create `content/theses/<year><name>/index.md`, for example `content/theses/2026mariarossi/index.md`.
   Copy an existing thesis, or run `uv run python scripts/site.py new masters-thesis 2026mariarossi`.
   Use `bachelors-thesis` for a bachelor's thesis.
2. Set `title`, `authors` with the student's name, and `date` as the graduation date.
3. Keep `categories` as `Master thesis` or `Bachelor thesis`.
   It selects the list on the For Students page.
4. Set `url_pdf` to the thesis record, for example its AMS Laurea page, when it exists.

### Add a research proposal

Research proposals are grouped by topic under `content/proposals/`.
Each topic is a folder whose `_index.md` holds the topic title, its `summary`, and its description.
The For Students page shows one card per topic automatically.

```text
content/proposals/legal/
├── _index.md          the topic: title, summary, description
├── am/index.md        one proposal
└── unfairclauses/index.md
```

1. Copy an existing proposal folder inside the right topic, for example `content/proposals/legal/am/`, and give it a new name.
2. Set `title`, `date`, `summary`, and `tags`.
   Validation requires `title`, `date`, and `summary`.
   A topic `_index.md` needs `title` and `summary`.
3. Write the body with a **Description**, a **Contact** line, and optional **References**.
   Write each contact as an email link, for example `[Maria Rossi](mailto:maria.rossi@unibo.it)`.

To add a new topic, create a folder such as `content/proposals/new-topic/` with an `_index.md`.
Copy the `_index.md` of an existing topic and replace its title, summary, and description.

### Add a project

1. Create `content/projects/<slug>/index.md`, for example `content/projects/amica/index.md`.
   Copy an existing project, or run `uv run python scripts/site.py new national-project amica`.
   Use `international-project` for an international project.
2. Set `title`, `date` as the project start, `summary`, and `external_link` as the project website.
   The Projects page shows only the summary, and the card opens `external_link` directly.
   The date orders the list and is not displayed.
3. List one or more `topics`, using the keys defined in `data/topics.yaml`.
   Each topic appears as a colored tag on the card.
   To add a topic or change its label or color, edit `data/topics.yaml`.
4. Keep `categories` as `International project` or `National project`.
   It selects the list on the Projects page.

Projects have no page of their own, so the file needs no body text.

### Add a challenge or workshop suggestion

The For Students page suggests international challenges and academic workshops as project-work topics.

1. Copy an existing folder in `content/opportunities/`, for example `content/opportunities/semeval/`.
2. Set `title`, `tags`, and `url_project` as the website of the challenge or workshop.
3. Set `categories` to `Challenge` or `Academic workshop`.
4. Describe it in two or three sentences in the body.

### Add a research area

1. Create `content/research/<slug>/index.md`.
   Copy an existing area, or run `uv run python scripts/site.py new research <slug>`.
2. Set `title` and `summary`.
   The summary appears on the homepage tile.
3. Set `icon` to a [Font Awesome 5](https://fontawesome.com/v5/search?m=free&s=solid) solid icon name, such as `comments` or `balance-scale`.
4. Describe the topics in the body.

The homepage shows one tile per research area automatically.

### Add a tool

A tool card links directly to the tool's own website, and the tool page redirects there.

1. Create `content/tools/<slug>/index.md`.
   Copy an existing tool, or run `uv run python scripts/site.py new tool <slug>`.
2. Set `title`, `date`, and `summary`.
   The date orders the list and is not displayed.
3. Set `external_link` to the tool's website.
4. List one or more `topics`, using the keys defined in `data/topics.yaml`.
   Each topic appears as a colored tag on the card.

### Publish the Work with us page

The Work with us page is written but hidden, because its procedures are still being finalized.
It lives in `content/work-with-us/index.md` and appears in the local preview at `/work-with-us/`.

1. Delete the `draft: true` line and its comment in `content/work-with-us/index.md`.
2. In `config/_default/menus.yaml`, remove the `#` at the start of the three `Work with us` lines, and delete the comment above them.

### Edit the homepage or the menu

The homepage is defined in `content/_index.md` as a list of blocks, such as the hero, the figures, the research tiles, and the latest news.
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
| `author '...' conflicts with '...'` | The same person is written in two ways, for example with and without an accent. Use the spelling of their profile |
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
| `content/opportunities/` | Challenges and academic workshops suggested to students |
| `content/research/`, `content/tools/` | Research areas and tools |
| `content/students/`, `content/people/`, `content/work-with-us/` | Landing pages |
| `content/categories/_index.md` | Citation view for category pages |
| `config/_default/` | Site settings (`hugo.yaml`, `params.yaml`) and the menu (`menus.yaml`) |
| `data/topics.yaml` | Topic labels and tag colors for projects and tools |
| `data/themes/ltlab.toml` | Site colors for light and dark mode, taken from the lab logo |
| `data/fonts/ltlab.toml`, `static/fonts/inter/` | Self-hosted Inter font, under the SIL Open Font License |
| `assets/scss/template.scss` | Site-wide style rules layered over the theme |
| `assets/js/ltlab.js` | Scroll effects and publication year headings, loaded by `layouts/partials/hooks/body-end/ltlab.html` |
| `assets/media/` | Shared images, including the homepage logo |
| `layouts/shortcodes/` | `section-cards` (proposal topics), `section-tiles` (research tiles), and `site-stats` (homepage figures) |
| `layouts/partials/views/card.html` | Theme card view plus topic tags |
| `layouts/partials/views/citation.html` | Theme citation view plus the award line and year data for headings |
| `layouts/redirect/single.html` | Layout for pages with `type: redirect` |
| `archetypes/` | Templates used by `site.py new` |
| `scripts/site.py` | Setup, preview, validation, and build commands |
| `scripts/test_site.py` | Self-checks for the validator, run by the pull-request workflow |
| `content/mm-argfallacy/` | Redirect from a shared-task short link to its event page |
| `.github/workflows/` | Pull-request validation (`validate.yml`) and deployment (`hugo.yml`) |
| `.github/pull_request_template.md` | Pull-request checklist |

### Categories

Publications, projects, theses, and opportunities use one `categories` value to select the list they appear in.
A publication may also add `Highlight`, which lists it under Highlights as well.
Validation rejects a missing or unknown value.
The theme would print categories in the page metadata, so `template.scss` hides them.

| Folder | Allowed `categories` values |
| --- | --- |
| `content/publication/` | `Journal`, `Conference`, `Workshop`, `Preprint`, plus an optional `Highlight` |
| `content/projects/` | `International project`, `National project` |
| `content/theses/` | `Master thesis`, `Bachelor thesis` |
| `content/opportunities/` | `Challenge`, `Academic workshop` |

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

The `new` command accepts `news`, `event`, `person`, `research`, `tool`, `national-project`, `international-project`, `bachelors-thesis`, `masters-thesis`, `publication-highlight`, `journal`, `conference`, `workshop`, and `preprint`.
Research proposals and opportunities have no template, so contributors copy an existing entry.

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

Three files depend on theme internals and need attention when upgrading Hugo Blox.
First, `layouts/partials/views/citation.html` is a copy of the theme's citation view with the award line and year data, so re-sync it with the new theme file.
Second, `layouts/partials/views/card.html` is a copy of the theme's card view with topic tags, so re-sync it as well.
Third, the navbar rules in `template.scss` rely on the theme's navbar markup, so recheck the menu between 992px and 1279px.

### License

The repository and the website are licensed under CC BY-NC-ND 4.0, as stated in the site footer and in `LICENSE`.
Code derived from the Hugo Blox template keeps its MIT License, and the Inter font keeps the SIL Open Font License.
The footer license is configured under `footer.copyright.license` in `config/_default/params.yaml`, so change both places together.
