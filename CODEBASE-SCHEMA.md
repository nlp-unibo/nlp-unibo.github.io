# Codebase schema

This file records function-call relations and module dependencies of the Python tooling.
It omits behavior, which `docs/developers.md` describes.

## scripts/site.py

Dependencies: standard library, `yaml`; network access to OpenAlex, Google Scholar, and the Hugo and Go release servers.

| Function | Calls |
|---|---|
| `main` | `build`, `clean`, `new_content`, `publication_report`, `serve`, `setup`, `validate_archetypes`, `validate_content_quality`, `validate_front_matter` |
| `setup` | `environment`, `run` |
| `environment` | `ensure_go`, `ensure_hugo` |
| `ensure_hugo` | `download`, `platform_names`, `read_hugo_version`, `read_url`, `run`, `verify_sha256` |
| `ensure_go` | `download`, `platform_names`, `read_url`, `verify_sha256` |
| `build`, `serve`, `new_content` | `environment`, `run` |
| `validate_archetypes` | `category_error`, `environment` |
| `validate_content_quality` | `content_slug`, `local_link_targets`, `page_errors`, `read_page`, `same_keyword`, `section_pages` |
| `page_errors` | `category_error`, `content_date`, `content_slug`, `local_link_targets`, `metadata_strings`, `proposal_errors`, `same_keyword`, `strip_code`, `venue_rank_error`, `view_errors` |
| `view_errors` | `rules_view_errors`, `voices_view_errors` |
| `local_link_targets` | `strip_code` |
| `publication_report` | `content_slug`, `doi_key`, `foreign_affiliation`, `member_authors`, `missing_works`, `openalex_works`, `read_page`, `scholar_works`, `work_key` |
| `member_authors` | `content_slug` |
| `openalex_works` | `read_url` |
| `scholar_works` | `read_url`, `scholar_rows` |
| `missing_works` | `content_slug`, `work_key` |
| `work_key` | `doi_key` |

## scripts/test_site.py

Loads `scripts/site.py` by path and calls its pure functions, including `missing_works`, `scholar_rows`, `foreign_affiliation`, `member_authors`, and `page_errors`.
