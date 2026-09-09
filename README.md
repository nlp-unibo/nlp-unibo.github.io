# Language Technologies Lab website

Source repository for the [Language Technologies Lab website](https://nlp.unibo.it/). The site is built with [Hugo](https://gohugo.io/) and Hugo Blox, then deployed to GitHub Pages.

## Quick contribution workflow

1. Start from the `hugoblox-template` branch. This is the repository's current default branch and source of truth.
2. Create a branch for your change. Use a descriptive name such as `news/acl-2026` or `people/add-maria-rossi`.
3. Edit or add files under `content/`.
4. Preview the site locally when possible.
5. Commit and push your branch.
6. Open a pull request against `hugoblox-template` and ask another lab member to review it.
7. Wait for **Validate content and build** check to pass.
8. Merge only after checking text, links, dates, images, and build results.
9. Monitor automatic deployment from GitHub **Actions** as described in [Publishing](#publishing).

For small text corrections, the whole workflow can be completed in GitHub's web interface. Do not edit generated files or the published website directly.

## Repository structure

| Path | Purpose |
| --- | --- |
| `content/` | All pages and displayed text |
| `content/_index.md` | Homepage layout and homepage collections |
| `content/authors/` | Team member profiles and avatars |
| `content/news/` | News posts |
| `content/events/` | Event pages |
| `content/research/` | Research-area pages |
| `content/projects_national/` | National projects |
| `content/projects_international/` | International projects |
| `content/publication_highlights/` | Highlighted publications |
| `content/publication_journals/` | Journal articles |
| `content/publication_conferences/` | Conference papers |
| `content/publication_workshops/` | Workshop papers |
| `content/publication_preprints/` | Preprints |
| `content/students_bscs/` | Bachelor's theses |
| `content/students_mscs/` | Master's theses |
| `content/students_proposals/` | Thesis proposals grouped by topic |
| `content/students_workshops/` | Student workshop pages |
| `content/tools/` | Lab tools and software |
| `config/_default/menus.yaml` | Top navigation menu |
| `config/_default/hugo.yaml` | Site title, URL, and core Hugo settings |
| `config/_default/params.yaml` | Theme and site-feature settings |
| `assets/media/` | Shared images, including homepage assets |
| `.github/workflows/hugo.yml` | GitHub Pages build and deployment workflow |

Most content entries are **page bundles**: one directory containing an `index.md` file and any files used only by that page.

```text
content/news/example-news/
├── index.md
├── featured.jpg
└── programme.pdf
```

Use lowercase directory and file names. Prefer short hyphen-separated slugs, for example `acl-2026`, and avoid spaces.

## Page format

Markdown pages normally contain:

1. YAML front matter between two `---` lines.
2. Page text written in Markdown.

```markdown
---
title: "Page title"
date: 2026-05-20
tags:
  - natural language processing
  - event
summary: "Short text used in page lists and previews."
---

Page body starts here.
```

Important rules:

- Use spaces, not tabs, in YAML.
- Use dates in `YYYY-MM-DD` format.
- Quote values containing punctuation when unsure.
- Keep indentation consistent.
- Do not remove either `---` delimiter.
- Use relative links for files in the same page directory: `[Programme](programme.pdf)`.
- Use standard Markdown links for external pages: `[ACL](https://www.aclweb.org/)`.
- Copy a nearby, working page of the same type before creating a page from scratch. Existing fields differ by content type.

## Creating new content from templates

Use repository archetypes instead of copying old entries. Generator creates page bundle in correct directory, fills title and date, and marks page `draft: true`:

```bash
uv run python scripts/site.py new TYPE slug
```

Available types:

```text
news                     event
person                   research
tool                     national-project
international-project    bachelors-thesis
masters-thesis           publication-highlight
journal                  conference
workshop                 preprint
```

Examples:

```bash
uv run python scripts/site.py new news acl-2026
uv run python scripts/site.py new person maria-rossi
uv run python scripts/site.py new international-project example-project
uv run python scripts/site.py new conference rossi-etal-2026-example
```

Slugs must contain lowercase letters, numbers, and hyphens only. Replace every `TODO`, add page files such as avatars or PDFs, preview page, then remove `draft: true` when ready to publish. Publication templates also create `cite.bib`.

## Updating existing content

1. Find the relevant `index.md` under `content/`.
2. Edit front matter for metadata shown in cards and lists.
3. Edit Markdown below front matter for main page content.
4. Place page-specific images, PDFs, or other downloads beside `index.md`.
5. Preview and check every changed link.

Do not rename a page directory without good reason: its name usually forms part of the public URL, so renaming it can break existing links.

## Adding news or events

Use `new news <slug>` or `new event <slug>`. This creates `content/news/<slug>/index.md` or `content/events/<slug>/index.md`.

```markdown
---
title: "Title of the news item"
date: 2026-05-20
tags:
  - natural language processing
  - workshop
summary: "One-sentence summary shown in listing cards."
---

Brief introduction.

## Details

Full text.

## Useful links

- [External page](https://example.org/)
- [Programme](programme.pdf)
```

Place `programme.pdf` and other page-specific files in the same directory. A listing image can usually be supplied as `featured.jpg` or `featured.png`.

## Adding or updating a team member

Each profile lives at `content/authors/<firstname-lastname>/_index.md`. Avatar lives in same directory and must be named `avatar.jpg` or `avatar.png`.

Run `new person <firstname-lastname>`, then update every personal field. Important fields include:

- `title`, `first_name`, and `last_name`
- `role`
- `organizations`
- `bio`
- `interests`
- `education`
- `social`
- `email`
- `user_groups`

`user_groups` controls where profile appears on People page. Current displayed groups are:

- `Head`
- `Academic Members`
- `Research Fellows`
- `PhD Students`

Use group spelling and capitalization exactly as shown. Check email addresses and all profile links before merging.

## Adding a project, research area, tool, or thesis

Use matching `new` content type, then update generated entry:

- National project: `content/projects_national/<slug>/index.md`
- International project: `content/projects_international/<slug>/index.md`
- Research area: `content/research/<slug>/index.md`
- Tool: `content/tools/<slug>/index.md`
- Bachelor's thesis: `content/students_bscs/<year-and-student>/index.md`
- Master's thesis: `content/students_mscs/<year-and-student>/index.md`

Keep section `_index.md` files unchanged unless changing section title, layout, filters, or ordering.

## Adding a publication

Choose correct section and create one directory per publication:

```text
content/publication_conferences/paper-slug/
├── index.md
├── cite.bib
└── featured.jpg        # optional
```

Use matching publication generator (`journal`, `conference`, `workshop`, `preprint`, or `publication-highlight`). Update at least:

- `title`
- `authors`
- `date` and `publishDate`
- `publication_types`
- `publication`
- `abstract`
- `tags`
- `doi` and relevant `url_*` fields
- `projects` or custom `links`, when applicable

Add complete BibTeX record to `cite.bib`. Keep author names consistent across profile and publication files. Never copy stale DOI, URL, abstract, or publication venue from template entry.

Publication locations:

- Highlights: `content/publication_highlights/`
- Journals: `content/publication_journals/`
- Conferences: `content/publication_conferences/`
- Workshops: `content/publication_workshops/`
- Preprints: `content/publication_preprints/`

## Editing homepage and navigation

Homepage content and collections are defined in `content/_index.md`. Collection filters refer to content directories, so preserve directory names unless also updating filters.

Top navigation lives in `config/_default/menus.yaml`. Lower `weight` values appear earlier. Test navigation changes locally before merging.

Changes outside `content/` can affect whole site. Ask repository maintainer for review before changing `config/`, `layouts/`, `go.mod`, or GitHub Actions workflow.

## Editing through GitHub website

Useful for text-only changes and small additions:

1. Open <https://github.com/nlp-unibo/nlp-unibo.github.io>.
2. Confirm branch selector shows `hugoblox-template`.
3. Create new branch from `hugoblox-template`.
4. Navigate to file and select pencil icon to edit it.
5. To create page, choose **Add file → Create new file** and enter full path, such as `content/news/acl-2026/index.md`.
6. To add images or PDFs, open target directory and choose **Add file → Upload files**.
7. Commit changes to your branch.
8. Open pull request targeting `hugoblox-template`.

Avoid editing binary files such as images and PDFs in text editor. Upload replacements instead.

## Editing locally with uv

Requirements:

- Git
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- Current Node.js LTS and npm

Repository tooling downloads pinned Hugo Extended and Go versions into ignored `.tools/` directory. Hugo version comes directly from `.github/workflows/hugo.yml`, keeping local and GitHub builds aligned. Python dependencies live in ignored `.venv/` environment managed by uv.

Clone, initialize, and create work branch:

```bash
git clone https://github.com/nlp-unibo/nlp-unibo.github.io.git
cd nlp-unibo.github.io
git switch hugoblox-template
git pull --ff-only
uv sync
uv run python scripts/site.py setup
git switch -c news/acl-2026
```

Preview during editing:

```bash
uv run python scripts/site.py serve
```

Open <http://localhost:1313/>. Preview includes pages whose publication date is in future.

Available commands:

```bash
# Validate content metadata, slugs, placeholders, local links, and asset sizes (fast)
uv run python scripts/site.py content

# Verify every content archetype generates a valid draft bundle
uv run python scripts/site.py templates

# Create production build and Pagefind index under .build/public
uv run python scripts/site.py build

# Validate front matter and configuration, build site, and generate search index
uv run python scripts/site.py check

# Remove generated build and caches; keep downloaded tools
uv run python scripts/site.py clean
```

Run `check` before opening a pull request. Downloaded tools, virtual environment, build output, caches, and Hugo's machine-specific `assets/jsconfig.json` are excluded by `.gitignore`.

Commit and push:

```bash
git status
git diff
git add content/path-you-changed
git commit -m "Add ACL 2026 news"
git push -u origin news/acl-2026
```

Then open pull request against `hugoblox-template`.

## Pull-request validation

Every pull request targeting `hugoblox-template` automatically runs **Validate website**. This read-only workflow:

1. Creates locked uv environment.
2. Validates YAML front matter and required fields under `content/`.
3. Rejects invalid or duplicate slugs, inconsistent author names, visible placeholders, and broken local links.
4. Rejects individual assets larger than 5 MiB and reports future publication dates.
5. Checks Hugo version stays aligned across deployment configurations.
6. Generates and validates every content archetype.
7. Builds production site with pinned Hugo version used for deployment.
8. Generates Pagefind search index.

Do not merge while **Validate content and build** is failing. Open failed check, inspect first meaningful error, push fix to same branch, and wait for rerun.

## Publishing

Merging into `hugoblox-template` automatically starts the **Deploy Hugo site to Pages** workflow. Keep **Enforce HTTPS** enabled under **Settings → Pages** for the `nlp.unibo.it` custom domain.

After merging:

1. Open repository's **Actions** tab.
2. Select latest **Deploy Hugo site to Pages** run.
3. Wait for build and deploy jobs to finish with green checks.
4. Verify changed page at <https://nlp.unibo.it/>.
5. Confirm <http://nlp.unibo.it/> redirects to HTTPS.

If automatic run fails to start, open workflow and use **Run workflow** with `hugoblox-template`. Do not publish from old `hugo` branch.

## Review checklist

Before merging:

- [ ] Change is on branch created from latest `hugoblox-template`.
- [ ] Correct content directory used.
- [ ] YAML front matter parses and indentation uses spaces.
- [ ] Title, author names, dates, venue, DOI, and URLs are correct.
- [ ] No private data, credentials, drafts, or copyrighted files were added accidentally.
- [ ] Images have sensible dimensions; every image or PDF is at most 5 MiB.
- [ ] Local `uv run python scripts/site.py check` succeeds.
- [ ] GitHub **Validate content and build** check succeeds.
- [ ] Changed page looks correct on desktop and mobile.
- [ ] Links and downloads work.
- [ ] Pull request targets `hugoblox-template`.
- [ ] Deployment workflow succeeds after merge.

## Common problems

### Page is missing

- Check page is under correct `content/` directory.
- Check `date` or `publishDate`; future content stays hidden in normal production build.
- Check front matter delimiters and YAML indentation.
- Check section landing-page filters include content directory.

### Image or PDF is missing

- Check filename capitalization; paths are case-sensitive.
- Keep page-specific file beside page's `index.md`.
- Use relative path such as `paper.pdf`, not local computer path.
- Avoid spaces in filenames.

### Build fails

Read first meaningful error in GitHub Actions log. It usually identifies file and line containing malformed YAML, invalid shortcode, missing dependency, or bad configuration. Fix on same branch and push again.

### Site still shows old content

Confirm deployment workflow completed successfully, then refresh page without browser cache. GitHub Pages may take a few minutes to update.
