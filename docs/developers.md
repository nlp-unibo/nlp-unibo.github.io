# Developers' guide

This guide is for developers who change the design, the JavaScript, the templates, or the build of the Language Technologies Lab website.
It tells you where each piece lives and how to change it without breaking existing behaviour.
Content editors should read [`../README.md`](../README.md) and [`editors.md`](editors.md) instead.

## Contents

1. [Architecture](#1-architecture)
2. [Code map](#2-code-map)
3. [Styles](#3-styles)
4. [JavaScript](#4-javascript)
5. [Shortcodes and publication pages](#5-shortcodes-and-publication-pages)
6. [Recipes](#6-recipes)
7. [Testing](#7-testing)
8. [Upgrades and policy](#8-upgrades-and-policy)
9. [Local workflow](#9-local-workflow)
10. [Content internals](#10-content-internals)

## 1. Architecture

### How a page is built

```text
content/<section>/<slug>/index.md        front matter + Markdown body
        |
        v
Hugo 0.167 (extended) + Hugo Blox modules (config/_default/module.yaml)
        |
        v
layouts/ in this repository              overrides theme templates of the same path
        |
        v
assets pipeline                          scss/main.scss (theme) imports assets/scss/template.scss (ours)
                                         js/ltlab.js is minified and fingerprinted by a body-end hook
        |
        v
public/ (GitHub Actions) or .build/public (site.py build)
```

1. Hugo reads a page bundle from `content/`.
   Its section, `type`, or `layout` selects a template.
2. Hugo looks up that template first in this repository's `layouts/`, then in the theme modules.
3. The template renders partials from `layouts/_partials/`, which also follow the repository-first rule.
4. The theme's `layouts/_partials/site_head.html` compiles `scss/main.scss` with `toCSS`.
   That file imports Bootstrap, the theme styles, `template`, and `custom`, in that order.
   Our `assets/scss/template.scss` replaces the theme's empty `template.scss`, so our rules load after the theme rules.
5. `layouts/_partials/hooks/body-end/ltlab.html` loads `assets/js/ltlab.js` with `minify | fingerprint` as a deferred script with an `integrity` hash.
6. `layouts/_partials/hooks/head-start/lt-js.html` adds the `lt-js` class to `<html>` before the first paint.

### Override order

Hugo resolves every template, partial, shortcode, asset, and data file in this order.

1. This repository (`layouts/`, `assets/`, `data/`, `static/`).
2. `blox-bootstrap/v5`, imported with `ignoreImports: true`, so its own imports are not pulled in.
3. `blox-core`, imported directly.
4. `blox-seo`, imported directly, with `layouts/_markup/sitemap.xml` excluded through its `mounts`.

A file at the same relative path as a theme file replaces it completely.
To change one theme template, copy it from the module cache and edit the copy.
The module cache lives in `.build/go-mod-cache/` after `site.py setup` or any build.

Hooks are an exception.
`blox-core/functions/get_hook` reads `layouts/_partials/hooks/<hook>/` from the project folder with `os.ReadDir`, and includes every file in it in name order.
Keep hooks in that folder, because the theme never looks for hooks inside modules.
The site copies of `site_head.html` and `site_js.html` call the `head-start`, `head-end`, and `body-end` hooks.

Homepage blocks follow the theme's v2 block parser.
A `block: lt-news` entry in `content/_index.md` renders `layouts/_partials/blocks/lt-news.html`, and the build fails when that partial does not exist.
The block partial receives the block as `.wcBlock`.

### Toolchain: `scripts/site.py`

`site.py` downloads pinned tools into the ignored `.tools/` folder and runs Hugo with caches under `.build/`.
It reads the Hugo version from `HUGO_VERSION` in `.github/workflows/hugo.yml`, so local and CI builds use the same version.
The Go version is the `GO_VERSION` constant in `site.py` (currently `1.27.1`).
Both downloads are checked against their published SHA-256 checksums.

| Command | Effect |
| --- | --- |
| `uv run python scripts/site.py setup` | Download the pinned Hugo extended and Go into `.tools/`, then print their versions |
| `uv run python scripts/site.py serve` | Run `hugo server --buildDrafts --buildFuture --disableFastRender --cleanDestinationDir` |
| `uv run python scripts/site.py new TYPE SLUG` | Run `hugo new content --kind <archetype>` for one entry of `CONTENT_TYPES` |
| `uv run python scripts/site.py content` | Validate YAML front matter (repeated keys included), then content quality: slugs, required fields, groups, categories, publication types, topics, research views, placeholders, local links, and asset sizes |
| `uv run python scripts/site.py templates` | Create one draft from every archetype in `.build/archetype-check` and verify it |
| `uv run python scripts/site.py build` | Run `hugo --gc --minify --destination .build/public` with `HUGO_RESOURCEDIR=.build/resources` |
| `uv run python scripts/site.py check` | Run `content`, `templates`, and `build` in that order |
| `uv run python scripts/site.py clean` | Remove `.build/`; the tools in `.tools/` stay |
| `uv run python scripts/test_site.py` | Run the self-checks of the link parser, the front-matter loader, the category rule, and the research view validators |

`new` accepts `news`, `person`, `research`, `tool`, `national-project`, `international-project`, `bachelors-thesis`, `masters-thesis`, `publication-highlight`, `journal`, `conference`, `workshop`, `preprint`, and `proposal`.
A proposal slug is `TOPIC/NAME`, as in `new proposal legal/new-idea`, and the topic folder must exist.

The production build uses its own resource folder, so `--gc` cannot delete files that a running preview uses.
You can therefore run `check` while `serve` is running.

### Deployment

Two workflows live in `.github/workflows/`.

| Workflow | Trigger | Steps |
| --- | --- | --- |
| `validate.yml`, **Validate website** (job **Validate content and build**) | Pull requests to `hugoblox-template`, manual dispatch | Set up uv, restore `.tools` and `.build/go-mod-cache` (keyed on `site.py`, `hugo.yml`, `go.mod`, `go.sum`), `uv sync --locked`, `scripts/test_site.py`, `site.py check` |
| `hugo.yml`, **Deploy Hugo site to Pages** | Push to `hugoblox-template`, manual dispatch, daily at 04:00 UTC | Install Hugo extended `HUGO_VERSION` from the release `.deb`, `hugo --minify --baseURL <pages url>`, upload `public/`, deploy to GitHub Pages |

The daily run publishes pages whose future date has arrived.
If a deployment does not start, open the workflow in the **Actions** tab and select **Run workflow** on `hugoblox-template`.
Keep **Enforce HTTPS** enabled under **Settings → Pages** for the `nlp.unibo.it` custom domain.

## 2. Code map

### Directories and key files

| Path | Purpose |
| --- | --- |
| `config/_default/hugo.yaml` | Site title, base URL, permalinks, taxonomies, outputs, image settings, and a cascade that hides share buttons |
| `config/_default/params.yaml` | Theme parameters: dark-only appearance (`theme_night: ltlab`, no `theme_day`), font set, navbar, footer license, features |
| `config/_default/menus.yaml` | Top menu; lower `weight` comes first |
| `config/_default/module.yaml` | Theme module imports and the blox-seo mount that excludes `_markup/sitemap.xml` |
| `config/_default/languages.yaml` | Single English language |
| `go.mod`, `go.sum` | Module versions; the theme is pinned to commit `62f5b139d3c5` |
| `content/_index.md` | Homepage blocks |
| `content/authors/` | Member profiles (`_index.md`) and avatars |
| `content/publication/` | All publications; `categories` selects their list |
| `content/news/` | News items; the section cascade sets `build.render: never`, so items have no page |
| `content/projects/`, `content/tools/` | Projects and tools; a cascade gives each page `type: redirect` |
| `content/theses/` | Master's and bachelor's theses, rendered by theme layouts |
| `content/proposals/` | Research proposals, one folder per topic with an `_index.md` |
| `content/research/` | Research areas; `am`, `legal`, and `speech` hold the reference `views` |
| `content/people/index.md` | People page (`type: people`) |
| `content/work-with-us/index.md` | Work with us page, as data for `layouts/work-with-us/single.html` |
| `content/categories/_index.md` | Citation view for category term pages |
| `content/mm-argfallacy/` | Website of the MM-ArgFallacy shared task |
| `data/themes/ltlab.toml` | Theme colours for the `[light]` and `[dark]` modes |
| `data/fonts/ltlab.toml`, `static/fonts/inter/` | Inter font set, self-hosted, under the SIL Open Font License |
| `data/topics.yaml` | Topic keys with `label`, `background`, and `text` colours |
| `assets/scss/template.scss` | Every site style rule, layered over the theme |
| `assets/js/ltlab.js` | Every site behaviour, as progressive enhancement |
| `assets/media/logo.svg`, `assets/media/icon.png` | Navbar and hero logo, and the favicon generated from it |
| `archetypes/` | Templates used by `site.py new`, one folder per kind |
| `scripts/site.py`, `scripts/test_site.py` | Toolchain and validator, and its self-checks |
| `pyproject.toml`, `uv.lock` | Python environment (PyYAML only) |
| `.github/workflows/` | Validation (`validate.yml`) and deployment (`hugo.yml`) |
| `.github/pull_request_template.md` | Pull-request checklist |

### Layouts per section

| Layout | Renders |
| --- | --- |
| `layouts/publication/section.html` | Publications page: Highlights carousel, then every publication with search, type, and topic filters (`lt/pub-browser.html`). The theme's file name `section.html` wins over `list.html` |
| `layouts/publication/single.html` | Publication page in the style of a research project page, with a side section menu from 1200px and a Cite block from `cite.bib` |
| `layouts/news/list.html` | News page: kind filter, year links, a timeline of news items and publications grouped by year, and a Back to top button |
| `layouts/research/list.html` | Research page: one band per area with a mosaic of its `overview` schemas |
| `layouts/research/single.html` | Research area page: body, `definition`, `overview`, `views` (argument, detect, rules, voices), `fields`, and `focus` |
| `layouts/projects/list.html` | Projects page: start-year timeline, then project cards with scope and topic filters |
| `layouts/tools/list.html` | Tools page: one band per tool with its `schema`, pills, install line, and link chips |
| `layouts/people/single.html` | People page: one band per `user_groups` value |
| `layouts/authors/list.html` | Profile page: header band, news and theses, publications with filters |
| `layouts/proposals/single.html` | Research proposal page in the style of a publication page |
| `layouts/work-with-us/single.html` | Work with us page: path tabs, steps, email form, proposals, work done with students |
| `layouts/redirect/single.html` | Pages with `type: redirect`: an alias page to `target` or `external_link`; the build fails without one |
| `layouts/baseof.html`, `layouts/rss.xml`, `layouts/index.webmanifest` | Theme copies with current Hugo calls |

Theses, tag pages, category pages, and `content/mm-argfallacy/` use theme layouts.

### Homepage blocks

`content/_index.md` lists the blocks under `sections`.
Each block partial lives in `layouts/_partials/blocks/` and reads its settings from `.wcBlock.content`.

| Block | Partial | `content` keys |
| --- | --- | --- |
| `lt-hero` | `lt-hero.html` | `eyebrow`, `title`, `text` (Markdown), optional `buttons` (`text`, `url`, `secondary`); a button to an unpublished internal page is dropped |
| `lt-research` | `lt-research.html` | `title`, optional `section` (default `research`); one card per area by weight, with `focus` titles or the `h3` headings as topics |
| `lt-news` | `lt-news.html` | `title`, `count` (default 6), `featured` (default 3), `more` (`text`, `url`) |
| `lt-papers` | `lt-papers.html` | `title`, `count` (default 3), optional `category`, `more`; a carousel of `lt/pub-card.html` |

Every block also accepts `eyebrow` and `subtitle` through `lt/section-head.html`.

### Partials in `layouts/_partials/lt/`

| Partial | Input | Output |
| --- | --- | --- |
| `contacts.html` | List of author folder names or `{name, email}` maps | Returns people with `name`, `email`, `url`, `avatar`, `initials`; fails the build on an unknown author or a missing email |
| `people-row.html` | Output of `contacts.html` | Avatar row linked to profiles or `mailto:` |
| `cover.html` | `seed`, optional `pattern` (`tokens`, `graph`, `wave`, `dots`), optional `tall` | Generated SVG cover art, stable for a given seed |
| `links.html` | A page | Returns the links of its body as `name`, `url`, Font Awesome `icon` |
| `link-chips.html` | `links`, `max` | Chip list |
| `news-data.html` | A news page or a publication | Returns `kind`, `date`, `iso`, `venue`, `summary`, `links`, `id` for previews |
| `news-kind.html` | A page | Returns the kind `label`, `icon`, `slug` (pill colour), and `key` (filter value), derived from tags |
| `page-intro.html` | A page | Opening band with a screen-reader `h1` and the `intro` |
| `person-social.html` | A profile | Labelled social icon buttons |
| `person-topics.html` | A profile | Returns `works_on`, or the three most frequent publication topics except `prototype` |
| `pub-browser.html` | `pubs`, `id`, `title` | Search, type and topic filters, count, year groups of `pub-row.html` |
| `pub-card.html` | A publication, or `{page, year, kind}` | Wide carousel card |
| `pub-meta.html` | A publication | Returns `kind`, `venue`, `links`, `tldr`, shared by cards and pages |
| `pub-row.html` | A publication | Compact list row |
| `rule-parts.html` | Parts of a rules-view sentence | Marked spans, recursive |
| `section-head.html` | A block | Eyebrow, title, subtitle, and "see all" link |
| `topic-tags.html` | Topic keys | Coloured tags from `data/topics.yaml`; unknown keys are skipped |

### Theme copies

Four files are theme copies with real changes, and they need a re-sync on every theme upgrade:

- `layouts/_partials/views/citation.html`: citation view plus the award line and `data-year`.
- `layouts/_partials/views/card.html`: card view plus topic tags.
- `layouts/authors/list.html`: started as the theme's profile page and is now a full rewrite.
- The navbar rules in `template.scss`, which depend on the theme's navbar markup.

Fifteen further files are copies that differ only in their Hugo calls (see [Upgrades](#hugo-and-hugo-blox-upgrades)).
`layouts/_partials/components/headers/navbar.html` also shows the site title next to the logo.

### Shortcodes

| Shortcode | File |
| --- | --- |
| `svg`, `gap`, `pipeline`, `stages`, `bars`, `numbers`, `annotate`, `takeaways` | `layouts/_shortcodes/<name>.html` |
| `figure` and other theme shortcodes | The blox-bootstrap module |

Section 5 documents each one.

## 3. Styles

### Organization of `template.scss`

The file has no partials.
Find a section by searching for its heading comment.
The sections appear in this order.

| Heading comment (search for it) | Covers |
| --- | --- |
| `Brand palette from the lab logo` | Sass colour variables |
| `Inter is self-hosted` | `@font-face` rules |
| `Typography`, `Page and section titles are left-aligned` | Headings and the orange rule under titles |
| `List cards`, `Citation lists`, `Buttons`, `Hero backdrop`, `Award line`, `Topic tags`, `Kind badges`, `Year headings` | Theme list views and shared small pieces |
| `Translucent navbar` | Navbar background and the `lt-scrolled` hairline |
| `Scroll reveal`, `Section focus` | Motion driven by the script, plus print and reduced-motion overrides |
| `Keep every menu label on one line`, `The full menu needs about 1280px` | Collapsed navbar between 992px and 1279px |
| `Homepage blocks (layouts/_partials/blocks/lt-*.html) and publication pages` | Second variable block, then the navbar brand |
| `Shared pieces`, `Cards`, `Hero`, `Research map` | Buttons, pills, chips, tags, cards, homepage hero and research map |
| `Paper carousel` | Carousel track, controls, depth effect, Highlights slides, autoplay dots |
| `News` | Homepage news block |
| `Publication page in the style of a research project page` | Publication page header, teaser, body, and citation |
| `Visual components for publication pages` | `.lt-viz`, then `Pipeline`, `Gap table`, `Bars`, `Takeaways`, `Annotated text`, `Stage diagram`, `Inline SVG figures` |
| `Research area pages` | Definition, core concepts, argument views, graph and edges, detect, voices, and rules views, field blocks, focus carousel, topic boxes, bands |
| `Research section page` | `layouts/research/list.html` |
| `Work with us page` | Path picker, view transition, steps, contact box, expandable sections, proposals, student work |
| `A view that returns to its blank state`, `View animation` | States that exist only while a research view plays, and the flying boxes |
| `Research proposal page`, `Side section menu` | Proposal header and the sticky side menu shared with publication pages |
| `Publications page`, `Projects page`, `News page`, `Tools page`, `People page` | One section per list layout |
| `Opening band of section pages`, `Profile page` | `lt/page-intro.html` and `layouts/authors/list.html` |

### Colour tokens

Colours live in five places.
Change them together.

| Where | What |
| --- | --- |
| Top of `template.scss` | `$lt-navy` `#003060`, `$lt-blue` `#105080`, `$lt-sky` `#60c0e0`, `$lt-orange` `#f09010`, `$lt-border`, `$lt-muted` |
| `Homepage blocks` section of `template.scss` | `$lt-ink`, `$lt-dark-border`, `$lt-dark-muted`, `$lt-dark-card` |
| `Visual components` section of `template.scss` | `$lt-cat-light` and `$lt-cat-dark`, the four validated categorical slots used by `.lt-c1` to `.lt-c4` |
| `Argument views` section of `template.scss` | CSS custom properties `--lt-role-1` to `--lt-role-4`, `--lt-support`, `--lt-attack`, scoped to `.lt-arg-views`, `.lt-overview`, `.lt-research-mosaic`, `.lt-tool-figure`, with a `.dark` variant |
| `data/themes/ltlab.toml` | Theme `primary`, `link`, `link_hover`, `background`, menu colours, and `home_section_odd` / `home_section_even` band colours |
| `data/topics.yaml` | Topic tag colours |
| `layouts/_partials/lt/cover.html` | Four hard-coded gradient palettes for generated covers |

The first comment of `template.scss` states that `ltlab.toml` uses the same values as the Sass palette.
Role and relation colours were checked for colour vision deficiency, and every coloured mark also carries a text label.
Keep both properties when you change a colour.

The script sets these custom properties at run time: `--lt-f` (section focus), `--lt-autoplay` (carousel delay), and `--lt-ring`, `--lt-fill`, `--lt-lift` (flying boxes).
Templates set `--lt-cols` (graph columns), `--t` (voice reading start), and `--w`, `--l`, `--ew` (bars).

### Dark mode

The site shows only dark mode.
`params.yaml` sets `theme_night: ltlab` and no `theme_day`.
`layouts/_partials/functions/parse_theme.html` then stores `light = false`, and `layouts/baseof.html` adds the `dark` class to `<body>` on every page.
The theme also hides the day and night switch.

Write every rule for light mode first, then its override under `.dark`:

```scss
.lt-meta { color: $lt-muted; }
.dark .lt-meta { color: $lt-dark-muted; }
```

The light rules stay so that the site can return to two modes by adding `theme_day` again.
Only the `.dark` rules are visible today, so check them first.
A rule without a `.dark` override shows its light value on the dark background.

### Breakpoints

The theme uses Bootstrap 4 breakpoints, and the site reuses them.

| Query | Use |
| --- | --- |
| `max-width: 575.98px` | Phones |
| `max-width: 767.98px` | Small tablets and phones; most stacked layouts |
| `max-width: 991.98px`, `min-width: 992px` | Research view panels side by side from 992px |
| `min-width: 992px and max-width: 1279.98px` | Collapsed navbar, which repeats the theme's below-992px rules from `components/_nav.scss` |
| `min-width: 1200px` | Side section menus on publication, proposal, and Work with us pages |
| `min-width: 576px`, `min-width: 768px` | A few grid steps |

The full menu fits on one line from 1280px.
After adding a menu entry, check the menu at 1280px.

### Motion

Every animation is optional.
The site handles motion in three layers.

1. `prefers-reduced-motion: reduce` media blocks in `template.scss` turn off transitions and reveal states.
2. `ltlab.js` checks `matchMedia("(prefers-reduced-motion: reduce)")` before every animation, smooth scroll, autoplay, and the section focus effect.
3. The `lt-js` class on `<html>`, added by `layouts/_partials/hooks/head-start/lt-js.html`, lets CSS match the state that the deferred script will set, from the first paint.
   Use it to avoid a flash, as in `.lt-js .lt-carousel-track` and `.lt-js .lt-to-top:not(.is-shown)`.
   Without JavaScript the class never appears, so the no-script state stays visible.

The `@media print` block also resets the reveal and focus states.
Section focus keeps opacity at 0.94 or more, so muted text keeps a 4.5:1 contrast.

### Sass gotchas

Hugo compiles the theme's `main.scss` with its default Sass transpiler, LibSass.
LibSass treats some CSS function names as Sass functions.

- Write CSS `min()` and `max()` with mixed units as `unquote("min(...)")`, as in the `.lt-arg-panels` grid columns.
- Write `grayscale(calc(...))` as `unquote("grayscale(...)")`, as in `.lt-section-focus`, because `grayscale` is a Sass colour function.
- `color-mix()`, `clamp()`, `:has()`, and `translate`/`scale` properties pass through unchanged.
- `rgba($sass-colour, alpha)` works on Sass variables, not on CSS custom properties.
  Use `color-mix(in srgb, var(--lt-role) 12%, transparent)` for custom properties.

## 4. JavaScript

### Structure and conventions

`assets/js/ltlab.js` is one immediately invoked function.
Each behaviour is one block that starts with a comment, finds its elements with `querySelectorAll`, and does nothing when none exist.
Every behaviour is progressive enhancement: the page must stay complete without it.

Two early `return` statements end the function.
Under reduced motion, the function returns before the section focus block.
Without `IntersectionObserver`, it returns before the scroll reveal block.
Add new behaviours **above** the section focus block, or they will not run under reduced motion.

### Custom events

| Event | Dispatched on | When | Detail | Listened to by |
| --- | --- | --- | --- | --- |
| `lt-select` | Tab container (`.lt-stages`, `.lt-arg-views`) | Every selection, including the initial one | The tab, or `null` for none | Work with us paths |
| `lt-chosen` | Tab container | After a click, once a view transition has finished | The tab | Work with us paths (scroll to panel) |
| `lt-show` | Tab panel | A reader picks its tab | None | Argument views, document views |
| `lt-hide` | Tab panel | Its tab loses the selection while the panel is visible | None | Argument views, document views |
| `lt-slide` | `[data-lt-carousel]` | The current slide index changes | Slide index | Research focus topics |
| `lt-reset` | `[data-lt-fields]` | Work with us changes path | None | Field blocks (close quietly) |

The paths and the proposal pick also dispatch a bubbling `input` event on the proposal field after setting its value, so the mail form updates.

### Element APIs

| Property | Set on | Use |
| --- | --- | --- |
| `carousel.ltGo(index)` | Every `[data-lt-carousel]` | Scroll to slide `index`; loops when `data-lt-loop` is set, clamps otherwise |
| `carousel.ltHold(reason, on)` | Carousels with `data-lt-autoplay`, only when motion is allowed | Add or remove a hold reason; any hold pauses autoplay and sets `is-holding`. Built-in reasons: `pointer`, `focus`; the focus topics add `topic` |
| `graph.ltShow(ids)` | `[data-lt-graph]` | Draw only edges between nodes in the `Set` `ids`; `null` draws all |
| `graph.ltDraw()` | `[data-lt-graph]` | Redraw the edges |
| `view.ltWrite()`, `view.ltBlank()` | Document views | Write the document again, or reset it to blank |
| `view.ltRun` | Argument views | State of the current animation run |

Check that an API exists before calling it, as the focus topics do with `carousel && carousel.ltHold`.

### Behaviour catalogue

The behaviours below appear in file order.
"Fallback" is what a reader sees without JavaScript.

| Behaviour | Markup hook | What it does | Fallback |
| --- | --- | --- | --- |
| Navbar state | `#navbar-main` | Toggles `lt-scrolled` once the page scrolls more than 8px | No hairline |
| Citation year headings | `.wg-collection:not(.lt-no-years)`, `.universal-wrapper` with six or more `.pub-list-item[data-year]` | Inserts `h2.lt-year` before the first item of each year | No headings |
| Copy button | `[data-lt-copy="<selector>"]` with an inner `span` label | Copies the text of the selected element and shows "Copied" for 1.6s | Button does nothing; the text stays selectable |
| Annotated text | `.lt-annotate`, `.lt-annotate-key[data-lt-label]`, `mark[data-lt-label]` | A legend key toggles `aria-pressed`, sets `data-lt-focus` on the figure, and adds `is-dim` to other marks | Every label visible |
| Tabs | `.lt-stages`, `.lt-arg-views` with `[role="tab"][aria-controls]`; options `data-lt-empty`, `data-lt-morph` | Switches panels, moves with Left and Right arrows, selects the tab named by the URL hash, emits `lt-select`, `lt-show`, `lt-hide`, `lt-chosen` | Every panel visible; stages show each stage under its name and hide the tabs. A scripted click (`event.isTrusted` false) selects at once, without the view transition |
| Section menu | `.lt-proj-nav` with `a[href^="#"]` (except `.lt-path-side-back`) | Sets `aria-current` on the link of the section that passed 150px from the top | Plain anchor links |
| Work with us paths | `.lt-paths`, `[data-lt-section]`, `[data-lt-slot]`, `data-lt-open`, `.lt-proposal-pick[data-lt-proposal]`, `[data-lt-proposals]` | Hides the shared bands, moves them into the open path's slots, resets fields and filters on path change, writes `#<path>` to the URL, opens a path from `#<path>-contact`, `-about`, `-inspiration`, or `-step-N`, fills the proposal field from `?proposal=` | Path cards hidden (`.lt-paths:not(.is-enhanced)`); every panel and section visible |
| Back to top | `[data-lt-to-top="<selector>"]` | Adds `is-shown` once the named element has scrolled out above | Always shown; `.lt-js` hides it from the first paint when the script runs |
| Filters | `[data-lt-filter-scope]`, `[data-lt-filter-group]` with `[data-lt-filter]` buttons, optional `data-lt-filter-key`, `[data-lt-search]`, `[data-lt-count]`, items with `data-lt-tag` | Combines every group and the search in one scope, hides items, empty `.lt-work-year` / `.lt-news-year` groups and their `.lt-news-years` links, recounts "Label (n)" buttons, writes the count | Every item listed; groups hidden by `.lt-filter:not(.is-enhanced)`; the search keeps `hidden` |
| Mail form | `.lt-mail-form` with `data-lt-to`, `data-lt-names` (`|`-separated), `data-lt-subject` (`{field}` placeholders); fields with `data-lt-label`; `data-lt-when`, `data-lt-when-value`; proposals with `data-lt-proposal-title`, `data-lt-proposal-to`, `data-lt-proposal-names` | Shows the form, hides `.lt-mail-direct`, updates `.lt-mail-subject` and `.lt-mail-names`, shows conditional fields, opens a `mailto:` URL on submit | Form `hidden`; the `.lt-mail-direct` link carries a prefilled email |
| Argument graphs | `[data-lt-graph]` with an `svg`, `[data-lt-node]`, and `.lt-arg-edges li[data-from][data-to][data-relation][data-label]` | Draws orthogonal SVG edges with arrowheads and placed labels, redraws on resize, adds `is-drawn` | Edges listed as text |
| Graph linking | `.lt-arg-view [data-lt-graph]`, `[data-lt-node]`, `[data-lt-span]` | Pointer or focus lights a component and its box (`is-linked`, view `is-linking`) | No linking |
| Rules linking | `.lt-rules`, `[data-lt-clause]`, `[data-lt-card]` | Pointer or focus lights a clause and its matrix row | No linking |
| Argument view animation (motion only) | `.lt-arg-view` inside `.lt-arg-views`, not `.lt-detect`, `.lt-rules`, `.lt-speech`; `.lt-arg-controls [data-lt-action="skip|annotate|graph|replay"]`, `.lt-arg-link` | Writes the text, marks components, moves each to its graph box, grows edges; Replay scrolls back to the tabs | Final state; controls keep `hidden` |
| Document view animation (motion only) | `.lt-detect`, `.lt-rules`, `.lt-speech`; `.lt-detect-controls [data-lt-action="skip|detect|classify|replay"]`; `[data-lt-sentence]`, `[data-lt-clause][data-lt-rule]`, `[data-lt-card]`, `[data-lt-rulecard]`, `data-lt-play` | Writes the document, then scans sentences (detect), fills the clause matrix and matches rules (rules), or plays cue strips and answers (voices) | Final state; controls keep `hidden` |
| Field blocks | `[data-lt-fields]` with `.lt-fields-grid`, `.lt-field[aria-controls]`, `.lt-field-back` | Opens one block and its panel, hides the others; back button, second click, or Escape closes; listens to `lt-reset` | Every panel visible below its block |
| Focus topics | `.lt-focus`, `.lt-focus-card`, `a[data-lt-topic]`, `.lt-topic-box#topic-<key>`, `.lt-topic-close` | Opens the detail box of the centred card, holds autoplay, closes on `lt-slide`, opens from `#topic-<key>`; the close button sets `data-lt-focus-hold` until the next user input | Every box visible; card links jump to it |
| Bar growth | `.lt-bars` | Adds `is-waiting`, removes it when the chart enters the view | Complete bars |
| Carousel | `[data-lt-carousel]`, `.lt-carousel-track`, `.lt-carousel-nav`, `[data-lt-slide="<i>"]`, `[data-lt-step="-1"]` and `[data-lt-step="1"]`; options `is-centered`, `data-lt-loop`, `data-lt-autoplay="<ms>"` | Shows the controls, adds `is-enhanced`, moves one slide per swipe, horizontal wheel gesture, arrow key, dot, or arrow; clones end slides for centred loops; emits `lt-slide`; autoplay fills the current dot and advances on `animationend` | Native scroll-snap track; controls stay `hidden` |
| Section focus (motion only) | Two or more `.home-section` or `.lt-band` elements, on the homepage (`.home-section`) or a research area page (`.lt-focus`) | Adds `lt-section-focus` to `<body>` and writes `--lt-f` (0 to 1) on each section from its distance to a focus line; frozen while `<body>` has `data-lt-focus-hold` | Every section at full size and colour |
| Scroll reveal (motion and `IntersectionObserver` only) | `.card-simple`, `.lt-card` outside `.home-section` and `.lt-band` | Adds `lt-reveal`, then `lt-visible` once the card enters the view | Cards visible at once |

### Details worth knowing

**Carousel.**
The track ignores vertical page scrolling once the script runs.
A carousel needs both the `.lt-carousel-nav` element and the two `[data-lt-step]` buttons, because the script uses them without checking.
`ltHold` exists only when autoplay is active, which never happens under reduced motion.
Only a width change re-centres the track, because mobile browsers also resize when their toolbars hide.

**Section focus.**
The focus line starts at the top of the first section and moves to 40% of the window height as the reader scrolls.
Over the last 40% of the page, it moves to the bottom of the window.
A section fades over 35% of the window height away from the line.
Only the children of a section are scaled, so the section box and its measured position stay put.
Scripts that measure positions inside a scaled section divide by `getBoundingClientRect().width / offsetWidth`, as the graph code does.
Set `data-lt-focus-hold` on `<body>` before any change that shortens the page, so sections the reader did not scroll keep their size.

**Work with us view transition.**
The `.lt-paths` container carries `data-lt-empty` and `data-lt-morph`.
`data-lt-empty` starts with no tab selected.
`data-lt-morph` wraps the tab change in `document.startViewTransition` when the browser supports it and motion is allowed.
Each tab has an inline `view-transition-name: lt-path-<key>`, so each card glides to its compact tab.
`lt-chosen` fires only after `transition.finished`, so the scroll to the panel uses the settled layout.
The CSS lives under the `Choosing a path runs a view transition` comment.

**News back to top.**
`layouts/news/list.html` renders `<a class="lt-to-top" href="#top" data-lt-to-top=".lt-news-page .lt-filter">`.
`#top` is the `id` of `<body>`.
Point `data-lt-to-top` at any element to reuse the button on another page.

## 5. Shortcodes and publication pages

### Shared rules

Every site shortcode except `svg` takes YAML between its opening and closing tags.
The template parses it with `transform.Unmarshal .Inner`.
Quote any value that contains `: `, a `#`, or starts with a special character, or the page fails to build.
Quote numbers such as `"72.30"` to keep trailing zeros.
`caption` is a shortcode parameter, not YAML, and accepts Markdown.
`ours: true` adds the shared "This work" label.

### `svg`

Inlines an SVG file from the page folder, so CSS can theme it.
Parameters: `src` (required), `caption`.
The build fails when the file is missing.

```text
{{< svg src="schema.svg" caption="The task setup." >}}
```

Draw only with these classes, which `.lt-svg` styles in both modes.

| Class | Draws |
| --- | --- |
| `lt-s-txt`, `lt-s-strong`, `lt-s-small`, `lt-s-sub`, `lt-s-mono` | Text: body, bold, small, small-caps label, monospace |
| `lt-s-tok`, `lt-s-on`, `lt-s-ontxt`, `lt-s-off` | Token boxes: neutral, selected, selected text, masked |
| `lt-s-box` with `lt-s-sel` or `lt-s-pred` | Module boxes in orange or blue |
| `lt-s-label` with `lt-s-labeltxt` | Output pill and its text |
| `lt-s-arrow`, `lt-s-head` | Connector line and arrowhead |
| `lt-s-node` with `lt-role-N`, `lt-s-implicit`, `lt-s-support`, `lt-s-attack` | Role boxes and relation edges, in the colours of the research views |

### `gap`

Comparison with related work.
YAML: `columns`, `rows` with `name`, `cells`, and `ours`, and an optional `label` for the first column header (default `Approach`).
A cell is `true`, `false`, `"partial"`, or short Markdown text.

```text
{{< gap caption="How the paper relates to prior work." >}}
columns: [End-to-end training, No extra hyper-parameters]
rows:
  - name: Select-then-predict
    cells: [true, false]
  - name: This paper
    ours: true
    cells: [true, true]
{{< /gap >}}
```

### `pipeline`

Method diagram, a row of steps that scrolls on narrow screens.
YAML: a list of steps with `title`, optional `text`, optional Font Awesome solid `icon`, `highlight: true` for the novel step, and optional `branches` (`title`, `text`).

```text
{{< pipeline caption="How the method flows." >}}
- title: Input text
  icon: file-alt
- title: Generator
  text: Selects highlights.
  highlight: true
{{< /pipeline >}}
```

### `stages`

Tabs, one per training stage, with the state of each component.
YAML: `flow` (component names), `stages` with `title`, `text`, and `states` (component to `evolved`, `trained`, `frozen`, or `data`).
Optional `labels`, `legend`, and `icons` rename a state.
The figure `id` is a hash of the inner YAML, so two identical blocks on one page would share an `id`.

```text
{{< stages caption="One generation of the method." >}}
flow: [Input text, Generator, Predictor]
stages:
  - title: 1. Train the predictor
    text: The generator is frozen.
    states: {Input text: data, Generator: frozen, Predictor: trained}
{{< /stages >}}
```

### `bars`

Horizontal bar chart of one metric, with a "Show as table" view.
YAML: `metric`, optional `unit`, `min`, `max`, `lower_is_better`, and `bars` with `label`, `value`, optional `err`, and `ours`.
`min` defaults to 0, and `max` defaults to the largest value plus its error.

```text
{{< bars caption="Source: Table 2 of the paper." >}}
metric: Macro-F1
max: 100
bars:
  - label: Baseline
    value: "72.30"
    err: "1.20"
  - label: Our model
    value: "81.10"
    ours: true
{{< /bars >}}
```

### `numbers`

Two to four headline numbers, in Results only.
YAML: a list of `value` and `label`.
No caption.

```text
{{< numbers >}}
- value: "76.02"
  label: highlight F1
{{< /numbers >}}
```

### `annotate`

Annotated text with up to four labels and a clickable legend.
YAML: `labels` (legend order) and `segments` with `text` and optional `label`.
Segments are joined by spaces, so punctuation belongs at the end of a segment.

```text
{{< annotate caption="An example from the dataset." >}}
labels: [Claim, Premise]
segments:
  - text: "The clause is unfair"
    label: Claim
  - text: because
  - text: "it limits the consumer's rights."
    label: Premise
{{< /annotate >}}
```

### `takeaways`

Numbered cards.
YAML: a list of `title` and `text`.
No caption.

```text
{{< takeaways >}}
- title: Short headline.
  text: One or two sentences.
{{< /takeaways >}}
```

### `figure`

The theme's `figure` shortcode shows an image from the page folder: `{{< figure src="method.png" caption="..." >}}`.

### Publication body pages

`layouts/publication/single.html` renders a publication as a project page.
The header shows the kind pill, venue and year, title, `summary`, authors, `topics`, `affiliations`, `award`, and link buttons from `lt/pub-meta.html`.
The teaser is `teaser.mp4`, else the `*featured*` image, else a generated cover.
The side menu lists every `<h2 id>` of the body plus Cite, and appears only with two or more entries.
A page without a body shows its `abstract`.

The publication archetypes give every body the same five `##` sections, in this order:

1. **Research setting**: the task and the field for a newcomer, with one visual (a schema, a pipeline, or a real example).
2. **Motivation**: the gap, with a `gap` table, then the objective in one blockquote that starts with `**Objective.**`.
3. **Approach**: the method around one paper figure, a `pipeline`, or a `stages` diagram.
4. **Results**: what was measured, then `numbers`, then a `bars` chart or a table.
5. **Takeaways**: one `takeaways` block with three items.

The page is self-contained and cites no other publication.
`featured.png` is the teaser and the card image; an optional `card.*` image replaces it on cards only.
The archetypes keep the component examples inside an HTML comment, escaped as `{{</* name */>}}`, so Hugo does not run them.
Proposal pages use `## Context`, `## Objective`, and `## References` the same way.

## 6. Recipes

### Add a homepage block

1. Create `layouts/_partials/blocks/lt-<name>.html`.
   Start with a comment that states what the block shows and which `content` keys it reads.

   ```go-html-template
   {{/* Upcoming events: the next `count` news items tagged `event`. */}}
   {{ $block := .wcBlock }}
   {{ partial "lt/section-head.html" $block }}
   <div class="lt-<name>">...</div>
   ```

2. Add the block to `sections` in `content/_index.md`:

   ```yaml
   - block: lt-<name>
     id: <name>
     content:
       title: Events
   ```

3. Add its styles to the `Homepage blocks` part of `template.scss`, with a `.dark` override for every colour.
4. Check that the section focus effect still reads well, since every `.home-section` takes part in it.

### Add a shortcode

1. Create `layouts/_shortcodes/<name>.html`.
   Start with a comment that lists the inner YAML keys.
2. Parse with `{{- $d := transform.Unmarshal .Inner -}}` and wrap the output in `<figure class="lt-viz lt-<name>">`.
3. Read the caption with `{{ with .Get "caption" }}<figcaption>{{ . | markdownify }}</figcaption>{{ end }}`.
4. Fail loudly on bad input with `errorf`, as `svg` does for a missing file.
5. Add styles after `Visual components for publication pages`, with `.dark` overrides and a `.lt-viz-scroll` wrapper for wide content.
6. Give every chart a table or text view, and every colour a visible label.
7. Add the shortcode to section 5 of this guide and to the comment in the publication archetypes.
   Escape it there as `{{</* name */>}}`.

### Add a page type or section

1. Create `content/<section>/_index.md` with `title` and, if wanted, `intro` for `lt/page-intro.html`.
2. Create `layouts/<section>/list.html` and, for pages with their own address, `layouts/<section>/single.html`.
   Each file defines the main block:

   ```go-html-template
   {{- define "main" -}}
   <article class="lt-proj">
     {{ partial "lt/page-intro.html" . }}
     <div class="lt-band">...</div>
   </article>
   {{- end -}}
   ```

   A page that sets `type: <name>` uses `layouts/<name>/single.html` instead of its section folder, as `content/people/index.md` does.
3. Create `archetypes/<kind>/index.md`.
   Set `draft: true`, fill every required field with a `TODO:` value, and escape shortcodes as `{{ "{{<" }} name {{ ">}}" }}` outside comments.
4. In `scripts/site.py`, add the kind to `CONTENT_TYPES`, and add the section with its required fields to `REQUIRED_FIELDS`.
   `REQUIRED_FIELDS` decides which sections `content` validates; the folder `content/<section>/` must exist.
   Add the section to `SECTION_CATEGORIES` if `categories` selects a list.
5. Add a menu entry in `config/_default/menus.yaml` and check the menu at 1280px.
6. Add styles under a new heading comment named after the layout file.

### Change colours or fonts

- Brand colours: change the Sass variables at the top of `template.scss` and the matching values in `data/themes/ltlab.toml`.
- Band backgrounds: change `home_section_odd` and `home_section_even` under `[dark]` in `ltlab.toml`.
- Topic colours: change `background` and `text` in `data/topics.yaml`; keep a 4.5:1 contrast between them.
- Research view colours: change `--lt-role-*`, `--lt-support`, and `--lt-attack` in both the light and the `.dark` blocks.
- Fonts: put the `woff2` files in `static/fonts/<font>/`, update the `@font-face` loop at the top of `template.scss`, and set the names in `data/fonts/ltlab.toml`.
  Keep `google_fonts = ""` so pages make no request to a font provider, and record the font license.

### Add a JavaScript behaviour

1. Add one block to `assets/js/ltlab.js`, above the `Section focus` block.
2. Write a comment above it that states what it does, its markup hook, and its fallback without the script.
3. Hook it on a `data-lt-*` attribute, or on a class the template already sets, and do nothing when no element matches:

   ```js
   // Expanders: a `data-lt-expand` button shows the element its value names. Without the script the element is visible.
   document.querySelectorAll("[data-lt-expand]").forEach((button) => {
     const target = document.querySelector(button.dataset.ltExpand);
     if (!target) return;
     target.hidden = true;
     button.hidden = false;
     button.addEventListener("click", () => {
       target.hidden = !target.hidden;
       button.setAttribute("aria-expanded", String(!target.hidden));
     });
   });
   ```

4. Render the complete content in the template, and let the script hide or rearrange it.
   Render script-only controls with `hidden`, and let the script reveal them, or add `is-enhanced` and hide controls with `:not(.is-enhanced)` in CSS.
5. Use `.lt-js` in CSS for states that must hold from the first paint.
6. Check `matchMedia("(prefers-reduced-motion: reduce)").matches` before every animation, smooth scroll, and timer, and fall back to the final state.
7. Talk to other behaviours through the `lt-*` events or the element APIs, not through shared globals.
8. Mention the template partial and the stylesheet section in the comment, so a reader can find all three parts.

### Add a validation rule to `scripts/site.py`

1. Add the check inside the per-page loop of `validate_content_quality()`, next to the related checks.
   Append to `failures` for errors and to `warnings` for problems that still build.
   Start every message with `page.relative_to(ROOT)` or `directory.relative_to(ROOT)`.

   ```python
   if section == "tools" and not is_draft and not str(metadata.get("external_link", "")).startswith("https://"):
       failures.append(f"{page.relative_to(ROOT)}: external_link must start with https://")
   ```

2. For a rule on nested data, write a pure function that returns a list of messages, as `view_errors()` does, and call it from the loop.
3. Add an `assert` for the new rule to `scripts/test_site.py`, which loads `site.py` by path.
4. Add the message and its fix to the message table for editors.
5. Run `uv run python scripts/test_site.py` and `uv run python scripts/site.py content`.

## 7. Testing

### Preview

A preview runs with `uv run python scripts/site.py serve` at <http://localhost:1313/>.
It shows drafts and future pages and rebuilds on save.
Run only one server at a time.

### Checks

| Command | Use |
| --- | --- |
| `uv run python scripts/test_site.py` | After a change to `site.py`; it runs without Hugo |
| `uv run python scripts/site.py content` | After a content or front-matter change; it runs without Hugo |
| `uv run python scripts/site.py check` | Before every pull request |

`check` fails on any validation failure and on any Hugo error.
It does not fail on Hugo warnings.
Read the build output: the production build must print no `WARN` line.

### Screenshots

Check every visual change at 1366px and 390px wide.
Take full-page screenshots with Playwright and reduced motion, so that revealed cards and focused sections show their final state.

```python
# uv run -q --with playwright python shot.py URL OUT.png WIDTH
# First run: uv run -q --with playwright playwright install chromium
import asyncio, sys
from playwright.async_api import async_playwright

async def main():
    url, out, width = sys.argv[1], sys.argv[2], int(sys.argv[3])
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": width, "height": 900}, reduced_motion="reduce")
        await page.goto(url, wait_until="networkidle")
        await page.screenshot(path=out, full_page=True)
        await browser.close()

asyncio.run(main())
```

Save screenshots outside the repository.
For motion work, also check the page by hand without reduced motion, and with JavaScript disabled for the fallback.

### What CI runs

On every pull request to `hugoblox-template`, **Validate content and build** runs `uv sync --locked`, `scripts/test_site.py`, and `site.py check`.
The pull request needs that status check to merge.
After the merge, **Deploy Hugo site to Pages** builds with `hugo --minify` and publishes.

## 8. Upgrades and policy

### Hugo and Hugo Blox upgrades

The site keeps the Hugo Blox theme unmodified and layers its changes on top.

The theme is the Bootstrap edition of Hugo Blox at its last upstream commit, `62f5b139d3c5`, pinned in `go.mod`.
That edition is archived upstream, so no newer version exists.
The `layouts/` folder follows the template structure of Hugo 0.146 and later, with `_partials/` and `_shortcodes/` folders.

To upgrade Hugo:

1. Change `HUGO_VERSION` in `.github/workflows/hugo.yml`; `site.py` reads it from there.
2. Run `uv run python scripts/site.py check` and fix every error and warning.
3. When a release deprecates a call, search the theme modules in `.build/go-mod-cache/` for it, and copy each affected file into `layouts/` with the new call.

To upgrade Go for local builds, change `GO_VERSION` in `scripts/site.py`.

Four files depend on theme internals and need attention when the theme changes:

1. `layouts/_partials/views/citation.html` copies the theme's citation view, with the award line and year data.
2. `layouts/_partials/views/card.html` copies the theme's card view, with topic tags.
3. `layouts/authors/list.html` replaces the theme's profile page.
4. The navbar rules in `template.scss` rely on the theme's navbar markup, so recheck the menu between 992px and 1279px.

Fifteen further templates are copies of theme files that differ only in their Hugo calls.
They use `hugo.Data` instead of `site.Data`, `site.Language.Locale` instead of `site.LanguageCode`, and `.IsBranch` instead of `.IsNode`.
Two of them come from blox-seo: `layouts/index.webmanifest` and `layouts/_partials/seo_tags.html`.
The other thirteen come from blox-bootstrap: `layouts/baseof.html`, `layouts/rss.xml`, and eleven files under `layouts/_partials/`.
Those eleven are `site_head.html`, `site_js.html`, `search.html`, `page_header.html`, `cookie_consent.html`, `components/footers/minimal.html`, `components/headers/navbar.html`, `components/page_sharer.html`, and `functions/get_address.html`, `get_pub_types.html`, `parse_theme.html`.
`components/headers/navbar.html` also shows the site title next to the logo.

`config/_default/module.yaml` imports blox-core and blox-seo directly, in the order the theme uses.
The direct import lets the site exclude `layouts/_markup/sitemap.xml` from blox-seo, which Hugo would skip with a warning.

### Review and emergency policy

The repository has one active maintainer, so pull requests require zero approvals and the **Validate content and build** status check.
The repository has no `CODEOWNERS` file, so new pull requests request no reviewers by default.
Request a reviewer explicitly when a change needs a second opinion.
When a second maintainer becomes active, raise the ruleset to one required approval and require another maintainer to review each change.
Resolve review threads and push follow-up fixes before merging whenever a review takes place.

Routine updates always follow the pull-request workflow.
An emergency is limited to an active outage, a security incident, a privacy exposure, or a similarly urgent risk to the live site.
Emergency changes still use a focused pull request and the required check whenever GitHub is operational.
If those controls prevent urgent mitigation, a repository administrator may amend the ruleset temporarily.
The administrator records the reason and the exact change in the pull request, restores the ruleset immediately afterwards, and requests a retrospective review.
Deadlines and delayed content are not emergencies.

### License

The repository and the website are licensed under CC BY-NC-ND 4.0, as stated in the site footer and in `LICENSE`.
Code derived from the Hugo Blox template keeps its MIT License, and the Inter font keeps the SIL Open Font License.
The footer license is configured under `footer.copyright.license` in `config/_default/params.yaml`, so change it and `LICENSE` together.

## 9. Local workflow

### Two ways to work

The GitHub website is enough for text changes, new pages, and image uploads.
You cannot preview the site there, but the automatic check catches most mistakes.

Your own computer lets you preview every change before publication.
It needs a one-time setup, described in [Work on your computer](#work-on-your-computer).

Every recipe in [editors.md](editors.md) works in both ways.

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
Continue from the pull request steps in [editors.md](editors.md#5-publish-your-change).

### Create content from the command line

- Publication: On your computer, run `uv run python scripts/site.py new conference rossi-etal-2026-example`.
  Replace `conference` with `journal`, `workshop`, `preprint`, or `publication-highlight` as needed.
- News item: Copy an existing news item, or run `uv run python scripts/site.py new news acl-2026`.
- Team member: Copy the folder of an existing member, or run `uv run python scripts/site.py new person maria-rossi`.
  Without a photo, keep the default person avatar from `archetypes/person/avatar.png`.
- Thesis: Copy an existing thesis, or run `uv run python scripts/site.py new masters-thesis 2026mariarossi`.
  Use `bachelors-thesis` for a bachelor's thesis.
- Research proposal: Run `uv run python scripts/site.py new proposal <topic>/<name>`, for example `new proposal legal/new-idea`.
  The topic folder must exist; the command creates a draft from `archetypes/proposal/index.md`, with a flow diagram to adapt.
- Project: Copy an existing project, or run `uv run python scripts/site.py new national-project amica`.
  Use `international-project` for an international project.
- Research area: Copy an existing area, or run `uv run python scripts/site.py new research <slug>`.
- Tool: Copy an existing tool, or run `uv run python scripts/site.py new tool <slug>`.

### Categories

The theme would print categories in the page metadata, so `template.scss` hides them.
The allowed values live in `SECTION_CATEGORIES` in `scripts/site.py`.
A new value also needs a list block on the matching landing page.

## 10. Content internals

Notes on how some pages render their content, kept from the former README.

The Publications page (`layouts/publication/section.html`) starts with the Highlights carousel, which loops and advances every eight seconds.
Every publication follows, newest first and grouped by year, with a search box, a filter by type, and a filter by topic.
The topic counts follow the chosen type and the search, and a topic without matches is hidden.

The research page (`layouts/research/list.html`) gives each area a full-width band: a mosaic of its `overview` schemas, then the tagline, the first line of `definition` (citations dropped), the `focus` topic titles, and the number of focus items by status. Its one-sentence `intro` lives in `content/research/_index.md`.

The schemas of `content/research/am/` add `lt-s-node` boxes with a `lt-role-N` class, `lt-s-implicit` for dashed borders, and `lt-s-support` or `lt-s-attack` on edges.

Each component gets an ID, the initials of its role label (or the role's `short`) and its number within the role, such as P1; text tags and graph boxes show the ID, so the graph stays small. Mark [...] where text is omitted.
Each row of `rows` is one line of the graph; nodes line up in columns, and supports and attacks are drawn in green and red.
Picking a tab, or the first view coming into sight, types the text; the Annotate and Show graph buttons then mark its components and move them into the argument graph. Pointing at or focusing a box or a component lights both and dims the rest of the text.
On research area pages and on the homepage, the section nearest a focus line is in focus, and the others shrink slightly and turn grey as they move away from it; the first section is in focus at the top of the page.
The document is written as in the argument views, with a Skip button; the Detect button then scans the document one sentence at a time and highlights each marked clause with its category and level, and a summary counts the unfair clauses.
A view with `type: rules` also shows a document, but each clause about personal data has a `level`, a `rule`, and `parts`; a clause matrix beside the text gives each clause an ID (C1, C2, ...) and a row with the type of its category, its specification, and its subcategories.
A part is plain `text`, or a mark with a `role` (category, specification, or subcategory) and a `type` (open or closed); a specification holds its own `parts`.
The view lists its annotation `rules`, each with a `level`, a number `n`, and the type that the category, the specification, and the subcategories need (open, closed, any, or none).
The rules follow in the same columns. Detect opens the matrix, marks the clauses in the text, and fills their rows; Classify lights the rule with the same pattern as each row and adds its rule ID (such as L2 · R1) beside the clause ID.
Each word has `w`, a duration `dur` and an optional `pause` after it (seconds), a `pitch` pair (start and end, 0 to 1), and a `loud` value (0 to 1); each reading has a `label`, a `summary` of its cues in words, and a `gold` answer (`gold_label` names that row, Annotators by default), and the strip shows the speaking rate.
Each model lists what it `hears` and one of `answers` per reading. The readings appear one after the other as plain text; Listen takes them in order, spreading the words on the time grid, opening the pitch and loudness rows, and drawing the cues word by word, and Classify shows the answers.
The topics rotate in a carousel; the current dot fills until the next topic, and the rotation holds under the pointer, under keyboard focus, and while a detail box is open.

The homepage is defined in `content/_index.md` as a list of blocks: the hero, the research map, the latest news, and the latest papers.
The blocks named `lt-*` are templates in `layouts/_partials/blocks/`.
The full menu fits on one line from 1280px, and narrower screens use the collapsed menu.
Ask the maintainer to review changes to the homepage, the menu, or any file outside `content/`, because they affect the whole site.
