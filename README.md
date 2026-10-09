# Language Technologies Lab website

This repository holds the source of the [Language Technologies Lab website](https://nlp.unibo.it/), the site of the Language Technologies Lab at the University of Bologna.
Every page of the site is a text file in this repository.

## Where the site is published

The site is published at <https://nlp.unibo.it/> through GitHub Pages.
The main branch is `hugoblox-template`.
Every change reaches that branch through a pull request, which GitHub checks automatically.
When a pull request is merged, GitHub rebuilds the site with [Hugo](https://gohugo.io/) and the Hugo Blox theme, then publishes it within a few minutes.
The site also rebuilds every day at 04:00 UTC, so pages with a future date appear on their day.

## Choose your guide

| I want to ... | Read |
| --- | --- |
| add or change content, such as a publication, a news item, a person, or a project | [docs/editors.md](docs/editors.md) |
| change the design or the code | [docs/developers.md](docs/developers.md) |

The editors' guide needs no installation.
Every step works on the GitHub website, and each recipe opens a ready-made template.

## Preview the site on your computer

A local preview needs [Git](https://git-scm.com/) and [uv](https://docs.astral.sh/uv/getting-started/installation/), on Linux or macOS.
On Windows, use the [Windows Subsystem for Linux](https://learn.microsoft.com/windows/wsl/install).
After cloning the repository, run these three commands from its folder:

```bash
uv sync
uv run python scripts/site.py setup
uv run python scripts/site.py serve
```

The first two commands install the Python environment and the pinned Hugo version, once.
The third starts the preview at <http://localhost:1313/>, including drafts and pages with a future date.
Run `uv run python scripts/site.py check` before opening a pull request: it runs the same check as GitHub.

## License

The repository and the website are licensed under CC BY-NC-ND 4.0, as stated in the site footer and in `LICENSE`.
Code derived from the Hugo Blox template keeps its MIT License, and the Inter font keeps the SIL Open Font License.
