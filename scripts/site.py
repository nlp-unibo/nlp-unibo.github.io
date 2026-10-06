#!/usr/bin/env python3
"""Bootstrap, preview, validate, and build the LT Lab Hugo site through uv.

Usage:
    uv run python scripts/site.py setup
    uv run python scripts/site.py serve
    uv run python scripts/site.py new TYPE SLUG
    uv run python scripts/site.py content
    uv run python scripts/site.py templates
    uv run python scripts/site.py build
    uv run python scripts/site.py check
    uv run python scripts/site.py clean
"""

from __future__ import annotations

import argparse
from datetime import date, datetime
import hashlib
import json
import os
from pathlib import Path
import platform
import re
import shutil
import stat
import subprocess
import sys
import tarfile
import tempfile
import unicodedata
import urllib.request
from urllib.parse import unquote

import yaml


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / ".tools"
BUILD = ROOT / ".build"
GO_VERSION = "1.27.1"
CONTENT_TYPES = {
    "news": ("news", "news"),
    "event": ("events", "event"),
    "person": ("authors", "person"),
    "national-project": ("projects", "project-national"),
    "international-project": ("projects", "project-international"),
    "research": ("research", "research"),
    "tool": ("tools", "tool"),
    "bachelors-thesis": ("theses", "bachelors-thesis"),
    "masters-thesis": ("theses", "masters-thesis"),
    "publication-highlight": ("publication", "publication-highlight"),
    "journal": ("publication", "publication-journal"),
    "conference": ("publication", "publication-conference"),
    "workshop": ("publication", "publication-workshop"),
    "preprint": ("publication", "publication-preprint"),
}
REQUIRED_FIELDS = {
    "authors": ("title", "first_name", "last_name", "user_groups"),
    "news": ("title", "date", "summary"),
    "events": ("title", "date", "summary"),
    "research": ("title", "date", "summary"),
    "projects": ("title", "date", "summary", "external_link", "topics", "categories"),
    "opportunities": ("title", "categories"),
    "tools": ("title", "date", "summary", "external_link", "topics"),
    "theses": ("title", "authors", "date", "publication_types", "categories"),
    "publication": ("title", "authors", "date", "publication_types", "categories"),
    "proposals": ("title", "date", "summary"),
}
# Proposals nest one folder per topic, whose _index.md needs these fields, around the proposal bundles.
TOPIC_FIELDS = ("title", "summary")
# publication_types values that the theme can label.
PUBLICATION_TYPES = {"article-journal", "paper-conference", "article", "chapter", "thesis", "report", "book"}
# Each `user_groups` value selects one group on the People page.
AUTHOR_GROUPS = {"Members", "Associate Fellows", "Former Members"}
# Each `categories` value selects one list on the section's landing page.
# A publication may add `Highlight`, which also lists it under Highlights.
SECTION_CATEGORIES = {
    "publication": {"Journal", "Conference", "Workshop", "Preprint"},
    "projects": {"International project", "National project"},
    "theses": {"Master thesis", "Bachelor thesis"},
    "opportunities": {"Challenge", "Academic workshop"},
}
PLACEHOLDER_PATTERNS = {
    "Lorem ipsum": re.compile(r"\blorem ipsum\b", re.IGNORECASE),
    "example email": re.compile(r"\btest@example\.org\b", re.IGNORECASE),
    "example domain": re.compile(r"\bexample\.org\b", re.IGNORECASE),
    "TODO marker": re.compile(r"\bTODO\b"),
    "publication boilerplate": re.compile(r"Add the \*\*full text\*\*", re.IGNORECASE),
}
MAX_ASSET_BYTES = 5 * 1024 * 1024


def rules_view_errors(view: dict) -> list[str]:
    """Return the problems of one rules view: marks with an unknown role or type, and clauses whose level and rule
    name no listed rule, or whose marks do not match the rule they name."""
    types = {"open", "closed"}
    rules = {(rule.get("level"), rule.get("n")): rule for rule in view.get("rules") or []}
    errors = [] if rules else ["rules view has no rules"]
    errors += [f"rule {key} has a type outside open, closed, any, or none" for key, rule in rules.items()
               if any(rule.get(name) not in types | {"any", "none"} for name in ("category", "specification", "subcategory"))]

    def marks(parts: list) -> list[dict]:
        found = []
        for part in parts or []:
            if part.get("role"):
                found.append(part)
            found += marks(part.get("parts"))
        return found

    sentences = [sentence for section in view.get("sections") or [] for sentence in section.get("sentences") or []]
    for n, sentence in enumerate(sentences, 1):
        found = marks(sentence.get("parts"))
        errors += [f"sentence {n}: mark {mark.get('text')!r} needs a role of category, specification, or subcategory and a type of open or closed"
                   for mark in found if mark.get("role") not in {"category", "specification", "subcategory"} or mark.get("type") not in types]
        if "level" not in sentence and "rule" not in sentence:
            continue
        rule = rules.get((sentence.get("level"), sentence.get("rule")))
        if not rule:
            errors.append(f"sentence {n}: level {sentence.get('level')} rule {sentence.get('rule')} is not listed")
            continue
        # A rule holds when each element is absent for `none`, present for `any`, and of the stated type otherwise;
        # subcategories are open when any of them is open.
        def kind(role: str) -> str:
            values = {mark.get("type") for mark in found if mark.get("role") == role}
            return "none" if not values else "open" if "open" in values else "closed"
        for name in ("category", "specification", "subcategory"):
            want, have = rule.get(name), kind(name)
            if not (want == have or (want == "any" and have != "none")):
                errors.append(f"sentence {n}: {name} is {have}, but level {rule.get('level')} rule {rule.get('n')} needs {want}")
    return errors


def view_errors(view: dict) -> list[str]:
    """Return the problems of one argument view: unknown roles, repeated components, rows and edges naming
    undefined components, unknown relations, or roles sharing a short name. A detect view needs sentences with text, and each annotated
    clause needs a category and a level of 1, 2, or 3."""
    if view.get("type") == "rules":
        return rules_view_errors(view)
    if view.get("type") == "detect":
        sentences = [sentence for section in view.get("sections") or [] for sentence in section.get("sentences") or []]
        errors = [] if sentences else ["detect view has no sentences"]
        for n, sentence in enumerate(sentences, 1):
            if not sentence.get("text"):
                errors.append(f"sentence {n} has no text")
            if ("level" in sentence or "category" in sentence) and (sentence.get("level") not in {1, 2, 3} or not sentence.get("category")):
                errors.append(f"sentence {n} needs a category and a level of 1, 2, or 3")
        return errors
    roles = {role.get("key") for role in view.get("roles") or []}
    texts = view.get("texts") or [{"segments": view.get("segments") or []}]
    parts = [segment for text in texts for segment in text.get("segments") or [] if segment.get("id")]
    parts += view.get("implicit") or []
    ids = {part.get("id") for part in parts}
    errors = [f"component {part.get('id')!r} has an unknown role" for part in parts if part.get("role") not in roles]
    listed = [part.get("id") for part in parts]
    errors += [f"component {key!r} is repeated" for key in sorted({str(key) for key in listed if listed.count(key) > 1})]
    errors += [f"edge relation {edge.get('relation')!r} is not support, attack, or link"
               for edge in view.get("edges") or [] if edge.get("relation") not in {"support", "attack", "link"}]
    named = [node for row in view.get("rows") or [] for node in row]
    named += [edge.get(end) for edge in view.get("edges") or [] for end in ("from", "to")]
    errors += [f"rows or edges name an undefined component {node!r}" for node in sorted({str(n) for n in named if n not in ids})]
    # Component IDs start with the role's short name (layouts/research/single.html), so short names must differ.
    shorts = [role.get("short") or "".join(word[:1].upper() for word in str(role.get("label", "")).split(" ")) for role in view.get("roles") or []]
    errors += [f"roles share the short name {short!r}; set `short` on one of them" for short in sorted({s for s in shorts if shorts.count(s) > 1})]
    return errors


def category_error(section: str, categories: list) -> str | None:
    allowed = SECTION_CATEGORIES[section]
    if section == "publication":
        highlights = categories.count("Highlight")
        categories = [category for category in categories if category != "Highlight"]
        if highlights > 1:
            return "categories must list Highlight at most once"
    if len(categories) != 1 or categories[0] not in allowed:
        suffix = ", optionally with Highlight" if section == "publication" else ""
        return f"categories must be exactly one of {', '.join(sorted(allowed))}{suffix}"
    return None


def run(command: list[str], *, env: dict[str, str] | None = None) -> None:
    print("+", " ".join(command), flush=True)
    subprocess.run(command, cwd=ROOT, env=env, check=True)


def read_hugo_version() -> str:
    workflow = (ROOT / ".github/workflows/hugo.yml").read_text(encoding="utf-8")
    match = re.search(r"^\s*HUGO_VERSION:\s*([0-9.]+)\s*$", workflow, re.MULTILINE)
    if not match:
        raise RuntimeError("Cannot find HUGO_VERSION in .github/workflows/hugo.yml")
    return match.group(1)


def download(url: str, destination: Path) -> None:
    print(f"Downloading {url}", flush=True)
    request = urllib.request.Request(url, headers={"User-Agent": "ltlab-site-bootstrap"})
    with urllib.request.urlopen(request) as response, destination.open("wb") as output:
        shutil.copyfileobj(response, output)


def read_url(url: str) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": "ltlab-site-bootstrap"})
    with urllib.request.urlopen(request) as response:
        return response.read().decode("utf-8")


def verify_sha256(archive: Path, expected: str) -> None:
    digest = hashlib.sha256()
    with archive.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    actual = digest.hexdigest()
    if actual != expected.strip().lower():
        raise RuntimeError(f"SHA-256 mismatch for {archive.name}: expected {expected}, got {actual}")


def platform_names() -> tuple[str, str, str]:
    system = platform.system().lower()
    machine = platform.machine().lower()
    arches = {
        "x86_64": "amd64",
        "amd64": "amd64",
        "aarch64": "arm64",
        "arm64": "arm64",
    }
    if machine not in arches:
        raise RuntimeError(f"Unsupported CPU architecture: {machine}")
    arch = arches[machine]
    if system not in {"linux", "darwin"}:
        raise RuntimeError(f"Unsupported operating system: {system}")
    return system, arch, "hugo"


def ensure_hugo() -> Path:
    version = read_hugo_version()
    system, arch, executable_name = platform_names()
    install_dir = TOOLS / "hugo" / version
    executable = install_dir / executable_name
    if executable.exists():
        return executable

    # macOS releases ship only as an installer package, which the system tar can unpack.
    if system == "darwin":
        archive_name = f"hugo_extended_{version}_darwin-universal.pkg"
    else:
        archive_name = f"hugo_extended_{version}_{system}-{arch}.tar.gz"
    release_url = f"https://github.com/gohugoio/hugo/releases/download/v{version}"
    checksums = read_url(f"{release_url}/hugo_{version}_checksums.txt")
    checksum = next(
        (line.split()[0] for line in checksums.splitlines() if line.split()[-1] == archive_name),
        None,
    )
    if checksum is None:
        raise RuntimeError(f"Checksum not found for {archive_name}")

    install_dir.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as temporary:
        archive = Path(temporary) / archive_name
        download(f"{release_url}/{archive_name}", archive)
        verify_sha256(archive, checksum)
        if system == "darwin":
            run(["tar", "-xf", str(archive), "-C", temporary, "Payload"])
            run(["tar", "-xf", str(Path(temporary) / "Payload"), "-C", str(install_dir), "hugo"])
        else:
            with tarfile.open(archive, "r:gz") as bundle:
                bundle.extractall(install_dir, filter="data")
    executable.chmod(executable.stat().st_mode | stat.S_IXUSR)
    return executable


def ensure_go() -> Path:
    system, arch, _ = platform_names()
    install_dir = TOOLS / "go" / GO_VERSION
    executable = install_dir / "go" / "bin" / "go"
    if executable.exists():
        return executable

    archive_name = f"go{GO_VERSION}.{system}-{arch}.tar.gz"
    url = f"https://go.dev/dl/{archive_name}"
    releases = json.loads(read_url("https://go.dev/dl/?mode=json&include=all"))
    checksum = next(
        (
            file["sha256"]
            for release in releases
            if release["version"] == f"go{GO_VERSION}"
            for file in release["files"]
            if file["filename"] == archive_name
        ),
        None,
    )
    if checksum is None:
        raise RuntimeError(f"Checksum not found for {archive_name}")
    install_dir.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as temporary:
        archive = Path(temporary) / archive_name
        download(url, archive)
        verify_sha256(archive, checksum)
        with tarfile.open(archive, "r:gz") as bundle:
            bundle.extractall(install_dir, filter="data")
    return executable


def environment() -> tuple[dict[str, str], Path, Path]:
    hugo = ensure_hugo()
    go = ensure_go()
    env = os.environ.copy()
    env["PATH"] = os.pathsep.join([str(hugo.parent), str(go.parent), env.get("PATH", "")])
    env["GOMODCACHE"] = str(BUILD / "go-mod-cache")
    env["HUGO_CACHEDIR"] = str(BUILD / "hugo-cache")
    return env, hugo, go


def setup() -> None:
    env, hugo, go = environment()
    run([str(hugo), "version"], env=env)
    run([str(go), "version"], env=env)
    print("Local toolchain ready.")


class UniqueKeyLoader(yaml.SafeLoader):
    """SafeLoader that rejects repeated keys, which PyYAML would otherwise overwrite silently."""

    def construct_mapping(self, node: yaml.MappingNode, deep: bool = False) -> dict:
        keys = [self.construct_object(key, deep=deep) for key, _ in node.value]
        repeated = sorted({str(key) for key in keys if keys.count(key) > 1})
        if repeated:
            raise yaml.constructor.ConstructorError(
                None, None, f"repeated key {', '.join(repeated)}", node.start_mark
            )
        return super().construct_mapping(node, deep=deep)


def validate_front_matter() -> None:
    failures: list[str] = []
    checked = 0
    for path in sorted((ROOT / "content").rglob("*.md")):
        text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
        if not text.startswith("---\n"):
            failures.append(f"{path.relative_to(ROOT)}: missing YAML front matter between --- lines")
            continue
        closing = text.find("\n---", 4)
        if closing == -1:
            failures.append(f"{path.relative_to(ROOT)}: missing closing YAML delimiter")
            continue
        try:
            metadata = yaml.load(text[4:closing], Loader=UniqueKeyLoader)
            if metadata is not None and not isinstance(metadata, dict):
                failures.append(f"{path.relative_to(ROOT)}: front matter must be a YAML mapping")
        except yaml.YAMLError as error:
            failures.append(f"{path.relative_to(ROOT)}: {error}")
        checked += 1
    if failures:
        print("Front-matter validation failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        raise SystemExit(1)
    print(f"Validated YAML front matter in {checked} content files.")


def read_page(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    if not text.startswith("---\n"):
        return {}, text
    closing = text.find("\n---", 4)
    metadata = yaml.safe_load(text[4:closing]) or {}
    return metadata, text[closing + 4 :]


def metadata_strings(value: object) -> list[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, dict):
        return [text for item in value.values() for text in metadata_strings(item)]
    if isinstance(value, (list, tuple)):
        return [text for item in value for text in metadata_strings(item)]
    return []


def content_date(value: object) -> date | None:
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    if isinstance(value, str):
        try:
            return date.fromisoformat(value[:10])
        except ValueError:
            return None
    return None


def content_slug(value: str) -> str:
    ascii_value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", ascii_value.lower()).strip("-")


# Site paths that Hugo generates from taxonomies rather than from content folders.
TAXONOMY_PREFIXES = ("/author/", "/authors/", "/tag/", "/category/", "/publication-type/")
EMAIL = re.compile(r"[^/\s]+@[^/\s]+\.[a-z]{2,}", re.IGNORECASE)


def strip_code(text: str) -> str:
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    text = re.sub(r"(```|~~~).*?\1", "", text, flags=re.DOTALL)
    return re.sub(r"`[^`\n]*`", "", text)


def local_link_targets(path: Path, body: str) -> list[tuple[str, list[Path]]]:
    clean_body = strip_code(body)
    raw_targets = [
        match.group(1) or match.group(2)
        for match in re.finditer(r"!?\[[^\]]*\]\(\s*(?:<([^>]+)>|([^\s)]+))", clean_body)
    ]
    raw_targets.extend(
        match.group(1) for match in re.finditer(r"^\s{0,3}\[[^\]]+\]:\s*<?([^\s>]+)>?", clean_body, re.MULTILINE)
    )
    raw_targets.extend(
        match.group(1)
        for match in re.finditer(r"(?:src|href)=[\"']([^\"']+)[\"']", clean_body, re.IGNORECASE)
    )
    results: list[tuple[str, list[Path]]] = []
    for raw_target in raw_targets:
        if not raw_target or raw_target.startswith(("#", "//", "{{", "{%")):
            continue
        if re.match(r"^[a-z][a-z0-9+.-]*:", raw_target, re.IGNORECASE):
            continue
        target = unquote(raw_target.split("#", 1)[0].split("?", 1)[0])
        if not target or target.startswith(TAXONOMY_PREFIXES):
            continue
        if target.startswith("/"):
            relative = target.lstrip("/")
            bases = [ROOT / "content" / relative, ROOT / "static" / relative, ROOT / "assets" / relative]
        else:
            bases = [path.parent / target]
        candidates: list[Path] = []
        for base in bases:
            candidates.extend((base, base / "index.md", base / "_index.md"))
            if not base.suffix:
                candidates.append(base.with_suffix(".md"))
        results.append((raw_target, candidates))
    return results


def section_pages(section: str) -> list[tuple[Path, Path, tuple[str, ...]]]:
    """Return (bundle folder, page file, required fields) for every entry of a validated section."""
    entries = []
    for directory in sorted(path for path in (ROOT / "content" / section).iterdir() if path.is_dir()):
        if section == "proposals":
            entries.append((directory, directory / "_index.md", TOPIC_FIELDS))
            for child in sorted(path for path in directory.iterdir() if path.is_dir()):
                entries.append((child, child / "index.md", REQUIRED_FIELDS[section]))
        else:
            page = directory / ("_index.md" if section == "authors" else "index.md")
            entries.append((directory, page, REQUIRED_FIELDS[section]))
    return entries


def validate_content_quality() -> None:
    failures: list[str] = []
    warnings: list[str] = []
    checked_pages = 0
    checked_links = 0
    content_root = ROOT / "content"
    # Hugo merges terms that share a URL, and then shows whichever spelling it reads first.
    term_names: dict[str, dict[str, tuple[str, Path]]] = {"authors": {}, "tags": {}, "categories": {}}
    project_topics = yaml.safe_load((ROOT / "data/topics.yaml").read_text(encoding="utf-8"))
    for key, topic in project_topics.items():
        if not isinstance(topic, dict) or not all(topic.get(field) for field in ("label", "background", "text")):
            failures.append(f"data/topics.yaml: topic {key!r} needs label, background, and text")

    for section in REQUIRED_FIELDS:
        for stray in sorted((content_root / section).glob("*.md")):
            if stray.name != "_index.md":
                failures.append(f"{stray.relative_to(ROOT)}: pages must be folders with an index.md")
        for directory, page, required_fields in section_pages(section):
            slug = directory.name
            if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", slug):
                failures.append(f"{directory.relative_to(ROOT)}: invalid slug {slug!r}")
            if not page.exists():
                failures.append(f"{directory.relative_to(ROOT)}: missing page index")
                continue
            metadata, body = read_page(page)
            checked_pages += 1
            is_draft = metadata.get("draft") is True
            for field in required_fields:
                if metadata.get(field) in (None, "", []):
                    failures.append(f"{page.relative_to(ROOT)}: required field {field!r} is empty")
            if section == "authors":
                groups = metadata.get("user_groups") or []
                if len(groups) != 1 or groups[0] not in AUTHOR_GROUPS:
                    allowed = ", ".join(sorted(AUTHOR_GROUPS))
                    failures.append(f"{page.relative_to(ROOT)}: user_groups must be exactly one of {allowed}")
                if groups != ["Former Members"] and not metadata.get("email"):
                    failures.append(f"{page.relative_to(ROOT)}: required field 'email' is empty")
            if section == "authors" and not is_draft and isinstance(metadata.get("title"), str):
                expected_slug = content_slug(metadata["title"])
                if slug != expected_slug:
                    failures.append(
                        f"{directory.relative_to(ROOT)}: author slug must be {expected_slug!r}"
                    )

            for taxonomy, names in term_names.items():
                for term in metadata.get(taxonomy) or []:
                    if not isinstance(term, str):
                        continue
                    term_slug = content_slug(term)
                    if term_slug in names and names[term_slug][0] != term:
                        first_name, first_page = names[term_slug]
                        failures.append(
                            f"{page.relative_to(ROOT)}: {taxonomy} term {term!r} conflicts with "
                            f"{first_name!r} in {first_page.relative_to(ROOT)}"
                        )
                    else:
                        names[term_slug] = (term, page)

            bib = directory / "cite.bib"
            if not is_draft:
                visible_text = "\n".join(metadata_strings(metadata)) + "\n" + strip_code(body)
                if bib.exists():
                    visible_text += "\n" + bib.read_text(encoding="utf-8")
                for name, pattern in PLACEHOLDER_PATTERNS.items():
                    if pattern.search(visible_text):
                        failures.append(f"{page.relative_to(ROOT)}: contains {name}")

            publication_date = content_date(metadata.get("publishDate", metadata.get("date")))
            if not is_draft and publication_date and publication_date > date.today():
                warnings.append(
                    f"{page.relative_to(ROOT)}: future publication date {publication_date.isoformat()}"
                )

            for raw_target, candidates in local_link_targets(page, body):
                checked_links += 1
                if any(candidate.exists() for candidate in candidates):
                    continue
                if EMAIL.fullmatch(raw_target):
                    failures.append(
                        f"{page.relative_to(ROOT)}: email link {raw_target!r} must start with mailto:"
                    )
                else:
                    failures.append(f"{page.relative_to(ROOT)}: local link {raw_target!r} does not exist")

            if section == "publication" and not bib.exists():
                warnings.append(f"{directory.relative_to(ROOT)}: missing cite.bib")
            if section in {"publication", "theses"} and not is_draft:
                types = metadata.get("publication_types") or []
                if len(types) != 1 or types[0] not in PUBLICATION_TYPES:
                    allowed = ", ".join(sorted(PUBLICATION_TYPES))
                    failures.append(
                        f"{page.relative_to(ROOT)}: publication_types must be exactly one of {allowed}"
                    )
            # Research area views, fields, and focus topics need unique keys; focus items need a known status,
            # and their citations must name existing publications.
            for name in ("views", "fields", "focus"):
                keys = [entry.get("key") for entry in metadata.get(name) or []]
                for key in {key for key in keys if keys.count(key) > 1 or not key}:
                    failures.append(f"{page.relative_to(ROOT)}: {name} key {key!r} is missing or repeated")
            for topic in metadata.get("focus") or []:
                for item in topic.get("items") or []:
                    if item.get("status") not in {"done", "now", "next"}:
                        failures.append(f"{page.relative_to(ROOT)}: focus item status must be done, now, or next")
                    for slug in item.get("cite") or []:
                        if not (content_root / "publication" / str(slug) / "index.md").exists():
                            failures.append(f"{page.relative_to(ROOT)}: focus item cites unknown publication {slug!r}")
            for view in metadata.get("views") or []:
                failures += [f"{page.relative_to(ROOT)}: view {view.get('key')!r}: {error}" for error in view_errors(view)]
            for topic in metadata.get("topics") or []:
                if topic not in project_topics:
                    failures.append(f"{page.relative_to(ROOT)}: topic {topic!r} is not defined in data/topics.yaml")
            if section in SECTION_CATEGORIES and not is_draft:
                error = category_error(section, metadata.get("categories") or [])
                if error:
                    failures.append(f"{page.relative_to(ROOT)}: {error}")

    checked_assets = 0
    for asset_root in (content_root, ROOT / "assets", ROOT / "static"):
        for path in asset_root.rglob("*"):
            if not path.is_file() or path.suffix.lower() in {".md", ".bib"}:
                continue
            checked_assets += 1
            if path.stat().st_size > MAX_ASSET_BYTES:
                size_mib = path.stat().st_size / (1024 * 1024)
                failures.append(
                    f"{path.relative_to(ROOT)}: {size_mib:.1f} MiB exceeds 5 MiB asset limit"
                )

    if warnings:
        print("Content-quality warnings:")
        for warning in warnings:
            print(f"- {warning}")
    if failures:
        print("Content-quality validation failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        raise SystemExit(1)
    print(
        f"Validated {checked_pages} content entries, {checked_links} local links, "
        f"and {checked_assets} assets."
    )


def validate_archetypes() -> None:
    env, hugo, _ = environment()
    content_dir = BUILD / "archetype-check"
    if content_dir.exists():
        shutil.rmtree(content_dir)
    content_dir.mkdir(parents=True)
    try:
        for content_type, (section, kind) in CONTENT_TYPES.items():
            relative_path = f"{section}/template-check-{content_type}"
            command = [
                str(hugo),
                "new",
                "content",
                "--contentDir",
                str(content_dir),
                "--kind",
                kind,
                relative_path,
            ]
            result = subprocess.run(
                command,
                cwd=ROOT,
                env=env,
                text=True,
                capture_output=True,
            )
            if result.returncode != 0:
                raise RuntimeError(
                    f"Archetype {kind!r} failed for {content_type!r}:\n{result.stderr}"
                )
            filename = "_index.md" if content_type == "person" else "index.md"
            page = content_dir / relative_path / filename
            if not page.exists():
                raise RuntimeError(f"Archetype {kind!r} did not create {page}")
            text = page.read_text(encoding="utf-8")
            metadata = yaml.safe_load(text.split("---", 2)[1])
            if not isinstance(metadata, dict) or metadata.get("draft") is not True:
                raise RuntimeError(f"Archetype {kind!r} must create draft content")
            if section == "publication" and not page.with_name("cite.bib").exists():
                raise RuntimeError(f"Archetype {kind!r} did not create cite.bib")
            if section in SECTION_CATEGORIES and category_error(section, metadata.get("categories") or []):
                raise RuntimeError(f"Archetype {kind!r} has an invalid categories value {metadata.get('categories')!r}")
            types = metadata.get("publication_types") or []
            if section in {"publication", "theses"} and (len(types) != 1 or types[0] not in PUBLICATION_TYPES):
                raise RuntimeError(f"Archetype {kind!r} has an invalid publication_types value {types!r}")
    finally:
        shutil.rmtree(content_dir, ignore_errors=True)
    print(f"Validated {len(CONTENT_TYPES)} content archetypes.")


def build() -> None:
    env, hugo, _ = environment()
    destination = BUILD / "public"
    if destination.exists():
        shutil.rmtree(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    # A separate resource directory keeps --gc from deleting files a running preview server uses.
    env["HUGO_RESOURCEDIR"] = str(BUILD / "resources")
    run([str(hugo), "--gc", "--minify", "--destination", str(destination)], env=env)
    print(f"Production build ready at {destination}")


def serve() -> None:
    env, hugo, _ = environment()
    run([str(hugo), "server", "--buildDrafts", "--buildFuture", "--disableFastRender", "--cleanDestinationDir"], env=env)


def new_content(content_type: str, slug: str) -> None:
    if content_type not in CONTENT_TYPES:
        available = ", ".join(CONTENT_TYPES)
        raise SystemExit(f"Unknown content type {content_type!r}. Choose one of: {available}")
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", slug):
        raise SystemExit("Slug must contain only lowercase letters, numbers, and hyphens.")
    section, kind = CONTENT_TYPES[content_type]
    env, hugo, _ = environment()
    relative_path = f"{section}/{slug}"
    run([str(hugo), "new", "content", "--kind", kind, relative_path], env=env)
    print(f"Created content/{relative_path}. Replace every TODO and remove draft only when ready.")


def clean() -> None:
    if BUILD.exists():
        shutil.rmtree(BUILD)
    print(f"Removed {BUILD}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "command",
        choices=("setup", "content", "templates", "build", "check", "serve", "new", "clean"),
    )
    parser.add_argument("content_type", nargs="?", help="Content type for the new command")
    parser.add_argument("slug", nargs="?", help="Lowercase, hyphen-separated slug for the new command")
    args = parser.parse_args()
    if args.command == "setup":
        setup()
    elif args.command == "content":
        validate_front_matter()
        validate_content_quality()
    elif args.command == "templates":
        validate_archetypes()
    elif args.command == "build":
        build()
    elif args.command == "check":
        validate_front_matter()
        validate_content_quality()
        validate_archetypes()
        build()
    elif args.command == "serve":
        serve()
    elif args.command == "new":
        if args.content_type is None or args.slug is None:
            parser.error("new requires CONTENT_TYPE and SLUG")
        new_content(args.content_type, args.slug)
    elif args.command == "clean":
        clean()


if __name__ == "__main__":
    main()
