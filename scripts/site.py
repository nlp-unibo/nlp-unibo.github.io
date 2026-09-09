#!/usr/bin/env python3
"""Bootstrap and validate the LT Lab Hugo site through uv.

Usage:
    uv run python scripts/site.py setup
    uv run python scripts/site.py serve
    uv run python scripts/site.py check
"""

from __future__ import annotations

import argparse
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
import urllib.request

import yaml


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / ".tools"
BUILD = ROOT / ".build"
GO_VERSION = "1.24.3"
NODE_PACKAGES = ("lightningcss", "@tailwindcss/oxide", "sass-embedded", "pagefind")


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


def clean() -> None:
    if BUILD.exists():
        shutil.rmtree(BUILD)
    print(f"Removed {BUILD}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("setup", "content", "build", "check", "serve", "clean"))
    args = parser.parse_args()
    if args.command == "setup":
        setup()
    elif args.command == "content":
        validate_front_matter()
    elif args.command == "build":
        build()
    elif args.command == "check":
        validate_front_matter()
        validate_configuration()
        build()
    elif args.command == "serve":
        serve()
    elif args.command == "clean":
        clean()


if __name__ == "__main__":
    main()
