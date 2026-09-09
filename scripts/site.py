#!/usr/bin/env python3
"""Bootstrap and validate the LT Lab Hugo site through uv.

Usage:
    uv run python scripts/site.py setup
    uv run python scripts/site.py serve
    uv run python scripts/site.py check
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
GO_VERSION = "1.24.3"
NODE_PACKAGES = ("lightningcss", "@tailwindcss/oxide", "sass-embedded", "pagefind")
CONTENT_TYPES = {
    "news": ("news", "news"),
    "event": ("events", "event"),
    "person": ("authors", "person"),
    "national-project": ("projects_national", "project"),
    "international-project": ("projects_international", "project"),
    "research": ("research", "research"),
    "tool": ("tools", "tool"),
    "bachelors-thesis": ("students_bscs", "bachelors-thesis"),
    "masters-thesis": ("students_mscs", "masters-thesis"),
    "publication-highlight": ("publication_highlights", "publication-highlight"),
    "journal": ("publication_journals", "publication-journal"),
    "conference": ("publication_conferences", "publication-conference"),
    "workshop": ("publication_workshops", "publication-workshop"),
    "preprint": ("publication_preprints", "publication-preprint"),
}
REQUIRED_FIELDS = {
    "authors": ("title", "first_name", "last_name", "role", "email", "user_groups"),
    "news": ("title", "date", "summary"),
    "events": ("title", "date"),
    "research": ("title", "date", "summary"),
    "projects_national": ("title", "date"),
    "projects_international": ("title", "date"),
    "tools": ("title", "date", "summary"),
    "students_bscs": ("title", "authors", "date", "publication_types"),
    "students_mscs": ("title", "authors", "date", "publication_types"),
    "publication_highlights": ("title", "authors", "date", "publication_types"),
    "publication_journals": ("title", "authors", "date", "publication_types"),
    "publication_conferences": ("title", "authors", "date", "publication_types"),
    "publication_workshops": ("title", "authors", "date", "publication_types"),
    "publication_preprints": ("title", "authors", "date", "publication_types"),
}
PUBLICATION_SECTIONS = {
    "publication_highlights",
    "publication_journals",
    "publication_conferences",
    "publication_workshops",
    "publication_preprints",
}
PLACEHOLDER_PATTERNS = {
    "Lorem ipsum": re.compile(r"\blorem ipsum\b", re.IGNORECASE),
    "example email": re.compile(r"\btest@example\.org\b", re.IGNORECASE),
    "example domain": re.compile(r"\bexample\.org\b", re.IGNORECASE),
    "TODO marker": re.compile(r"\bTODO:\s*", re.IGNORECASE),
    "publication boilerplate": re.compile(r"Add the \*\*full text\*\*", re.IGNORECASE),
}
MAX_ASSET_BYTES = 5 * 1024 * 1024


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
    return system, arch, "hugo.exe" if system == "windows" else "hugo"


def ensure_hugo() -> Path:
    version = read_hugo_version()
    system, arch, executable_name = platform_names()
    install_dir = TOOLS / "hugo" / version
    executable = install_dir / executable_name
    if executable.exists():
        return executable

    if system == "darwin":
        archive_name = f"hugo_extended_{version}_darwin-universal.tar.gz"
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


def ensure_node_tools() -> Path:
    npm = shutil.which("npm")
    if npm is None:
        raise RuntimeError("npm is required. Install current Node.js LTS, then rerun setup.")
    prefix = TOOLS / "node"
    pagefind = prefix / "node_modules" / ".bin" / "pagefind"
    if not pagefind.exists():
        prefix.mkdir(parents=True, exist_ok=True)
        run(
            [
                npm,
                "install",
                "--prefix",
                str(prefix),
                "--no-save",
                "--no-package-lock",
                *NODE_PACKAGES,
            ]
        )
    return prefix


def environment() -> tuple[dict[str, str], Path, Path]:
    hugo = ensure_hugo()
    go = ensure_go()
    node_prefix = ensure_node_tools()
    env = os.environ.copy()
    tool_paths = [
        str(hugo.parent),
        str(go.parent),
        str(node_prefix / "node_modules" / ".bin"),
    ]
    env["PATH"] = os.pathsep.join(tool_paths + [env.get("PATH", "")])
    env["GOMODCACHE"] = str(BUILD / "go-mod-cache")
    env["HUGO_CACHEDIR"] = str(BUILD / "hugo-cache")
    return env, hugo, go


def setup() -> None:
    env, hugo, go = environment()
    run([str(hugo), "version"], env=env)
    run([str(go), "version"], env=env)
    run(["node", "--version"], env=env)
    print("Local toolchain ready.")


def validate_front_matter() -> None:
    failures: list[str] = []
    checked = 0
    skipped = 0
    for path in sorted((ROOT / "content").rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            skipped += 1
            continue
        closing = text.find("\n---", 4)
        if closing == -1:
            failures.append(f"{path.relative_to(ROOT)}: missing closing YAML delimiter")
            continue
        try:
            metadata = yaml.safe_load(text[4:closing])
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
    print(f"Validated YAML front matter in {checked} content files ({skipped} without front matter skipped).")


def read_page(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
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


def local_link_targets(path: Path, body: str) -> list[tuple[str, list[Path]]]:
    clean_body = re.sub(r"<!--.*?-->", "", body, flags=re.DOTALL)
    clean_body = re.sub(r"```.*?```", "", clean_body, flags=re.DOTALL)
    raw_targets = [
        match.group(1).strip("<>")
        for match in re.finditer(r"!?\[[^\]]*\]\(\s*([^\s)]+)", clean_body)
    ]
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
        if not target:
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


def validate_content_quality() -> None:
    failures: list[str] = []
    warnings: list[str] = []
    checked_pages = 0
    checked_links = 0
    content_root = ROOT / "content"
    author_names: dict[str, tuple[str, Path]] = {}

    for section, required_fields in REQUIRED_FIELDS.items():
        section_dir = content_root / section
        seen_slugs: dict[str, str] = {}
        for directory in sorted(path for path in section_dir.iterdir() if path.is_dir()):
            slug = directory.name
            normalized_slug = slug.casefold()
            if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", slug):
                failures.append(f"{directory.relative_to(ROOT)}: invalid slug {slug!r}")
            if normalized_slug in seen_slugs:
                failures.append(
                    f"{directory.relative_to(ROOT)}: case-insensitive duplicate of {seen_slugs[normalized_slug]}"
                )
            seen_slugs[normalized_slug] = str(directory.relative_to(ROOT))

            page = directory / ("_index.md" if section == "authors" else "index.md")
            if not page.exists():
                failures.append(f"{directory.relative_to(ROOT)}: missing page index")
                continue
            metadata, body = read_page(page)
            checked_pages += 1
            for field in required_fields:
                if metadata.get(field) in (None, "", []):
                    failures.append(f"{page.relative_to(ROOT)}: required field {field!r} is empty")
            if section == "authors" and isinstance(metadata.get("title"), str):
                expected_slug = content_slug(metadata["title"])
                if slug != expected_slug:
                    failures.append(
                        f"{directory.relative_to(ROOT)}: author slug must be {expected_slug!r}"
                    )

            for author in metadata.get("authors", []):
                if not isinstance(author, str):
                    continue
                author_slug = content_slug(author)
                if author_slug in author_names and author_names[author_slug][0] != author:
                    first_name, first_page = author_names[author_slug]
                    failures.append(
                        f"{page.relative_to(ROOT)}: author {author!r} conflicts with "
                        f"{first_name!r} in {first_page.relative_to(ROOT)}"
                    )
                else:
                    author_names[author_slug] = (author, page)

            is_draft = metadata.get("draft") is True
            if not is_draft:
                visible_text = "\n".join(metadata_strings(metadata))
                visible_text += "\n" + re.sub(r"<!--.*?-->", "", body, flags=re.DOTALL)
                visible_text = re.sub(r"```.*?```", "", visible_text, flags=re.DOTALL)
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
                if "@" in raw_target:
                    failures.append(
                        f"{page.relative_to(ROOT)}: email link {raw_target!r} must start with mailto:"
                    )
                elif not any(candidate.exists() for candidate in candidates):
                    failures.append(f"{page.relative_to(ROOT)}: local link {raw_target!r} does not exist")

            if section in PUBLICATION_SECTIONS and not (directory / "cite.bib").exists():
                warnings.append(f"{directory.relative_to(ROOT)}: missing cite.bib")

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


def validate_configuration() -> None:
    workflow_version = read_hugo_version()
    netlify = (ROOT / "netlify.toml").read_text(encoding="utf-8")
    match = re.search(r'^\s*HUGO_VERSION\s*=\s*"([0-9.]+)"\s*$', netlify, re.MULTILINE)
    if not match:
        raise RuntimeError("Cannot find HUGO_VERSION in netlify.toml")
    netlify_version = match.group(1)
    if workflow_version != netlify_version:
        raise RuntimeError(
            "Hugo version mismatch: "
            f"GitHub Actions uses {workflow_version}, Netlify uses {netlify_version}"
        )
    print(f"Hugo versions aligned at {workflow_version}.")


def validate_archetypes() -> None:
    env, hugo, _ = environment()
    content_dir = BUILD / "archetype-check"
    if content_dir.exists():
        shutil.rmtree(content_dir)
    content_dir.mkdir(parents=True)
    try:
        for content_type, (section, kind) in CONTENT_TYPES.items():
            relative_path = f"{section}/template-check"
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
            if content_type in {
                "publication-highlight",
                "journal",
                "conference",
                "workshop",
                "preprint",
            } and not page.with_name("cite.bib").exists():
                raise RuntimeError(f"Archetype {kind!r} did not create cite.bib")
    finally:
        shutil.rmtree(content_dir, ignore_errors=True)
    print(f"Validated {len(CONTENT_TYPES)} content archetypes.")


def build() -> None:
    env, hugo, _ = environment()
    destination = BUILD / "public"
    if destination.exists():
        shutil.rmtree(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    run([str(hugo), "--gc", "--minify", "--destination", str(destination)], env=env)
    pagefind = TOOLS / "node" / "node_modules" / ".bin" / "pagefind"
    run([str(pagefind), "--site", str(destination)], env=env)
    print(f"Production build ready at {destination}")


def serve() -> None:
    env, hugo, _ = environment()
    run([str(hugo), "server", "--buildFuture", "--disableFastRender"], env=env)


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
        validate_configuration()
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
