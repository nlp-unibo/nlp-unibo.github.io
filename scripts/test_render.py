"""Checks of the rendered templates: the site content plus fixture pages is built into .build/render-check, and the
HTML is read back. Run: uv run python scripts/test_render.py"""

import importlib.util
from pathlib import Path
import re
import shutil
import subprocess

# site.py shares its name with a standard-library module, so it is loaded by path.
spec = importlib.util.spec_from_file_location("site_tools", Path(__file__).with_name("site.py"))
site_tools = importlib.util.module_from_spec(spec)
spec.loader.exec_module(site_tools)
ROOT, BUILD = site_tools.ROOT, site_tools.BUILD

# Fixture publications are dated 2099, so they lead the homepage Latest papers carousel.
FIXTURES = {
    "publication/render-check-year/index.md": """---
title: Render Check Year Only
authors: [Ada Rossi]
date: '2099-01-01'
publication_types: [paper-conference]
categories: [Conference]
venue_key: acl
doi: 10.0000/render-check
---
""",
    "publication/render-check-month/index.md": """---
title: Render Check Month Only
authors: [Ada Rossi]
date: '2099-03-01'
publication_types: [paper-conference]
categories: [Conference]
venue_key: acl
doi: 10.0000/render-check
---
""",
    "publication/render-check-schema/index.md": """---
title: Render Check Schema
authors: [Ada Rossi]
date: '2098-06-15'
publication_types: [paper-conference]
categories: [Conference]
venue_key: acl
---

## Research setting

A body gives the paper its own page, whose teaser is card.svg.
""",
    # A drawn card without a <title> still builds; its teaser then has no caption.
    "publication/render-check-schema/card.svg": '<svg viewBox="0 0 10 10" xmlns="http://www.w3.org/2000/svg"><rect width="10" height="10"/></svg>',
}


def build() -> Path:
    work = BUILD / "render-check"
    shutil.rmtree(work, ignore_errors=True)
    shutil.copytree(ROOT / "content", work / "content")
    for name, text in FIXTURES.items():
        (work / "content" / name).parent.mkdir(parents=True, exist_ok=True)
        (work / "content" / name).write_text(text, encoding="utf-8")
    env, hugo, _ = site_tools.environment()
    env["HUGO_RESOURCEDIR"] = str(work / "resources")
    result = subprocess.run([str(hugo), "--buildFuture", "--contentDir", str(work / "content"), "--destination",
                             str(work / "public")], cwd=ROOT, env=env, text=True, capture_output=True)
    assert result.returncode == 0, result.stderr
    return work / "public"


def latest_paper_dates(home: str) -> dict[str, str]:
    """Map each Latest papers card title to the text of its <time>."""
    track = home.split('aria-label="Latest papers"', 1)[1].split('class="lt-carousel-nav"', 1)[0]
    cards = re.findall(r'class="lt-slide-title">(?:<a[^>]*>)?([^<]+).*?<time[^>]*>([^<]+)</time>', track, re.DOTALL)
    return dict(cards)


def carousel_navs(html: str) -> list[tuple[int, int, list[str]]]:
    """For each carousel: its slide count, its dot count, and the labels of its arrows, previous first."""
    found = []
    for part in html.split("data-lt-carousel")[1:]:
        track = part.split('class="lt-carousel-track"', 1)[1].split('class="lt-carousel-nav"', 1)[0]
        nav = part.split('class="lt-carousel-nav"', 1)[1].split("</div>\n    </div>", 1)[0]
        slides = len(re.findall(r'<article class="lt-card[^"]*(?:lt-slide|lt-focus-card)', track))
        found.append((slides, nav.count("data-lt-slide="), re.findall(r'data-lt-step="-?1" aria-label="([^"]+)"', nav)))
    return found


if __name__ == "__main__":
    public = build()
    home = (public / "index.html").read_text(encoding="utf-8")
    dates = latest_paper_dates(home)
    # A date on the first of January means the year alone; the first of a month means the month alone.
    assert dates.get("Render Check Year Only") == "2099", dates
    assert dates.get("Render Check Month Only") == "Mar 2099", dates

    news = (public / "news" / "index.html").read_text(encoding="utf-8")
    assert re.search(r'id="news-render-check-year"[^>]*>.*?<time datetime="2099">2099</time>', news, re.DOTALL)
    assert re.search(r'id="news-render-check-month"[^>]*>.*?<time datetime="2099-03">Mar 2099</time>', news, re.DOTALL)

    schema_page = (public / "publication" / "render-check-schema" / "index.html").read_text(encoding="utf-8")
    teaser = schema_page.split('class="lt-proj-teaser"', 1)[1].split("</figure>", 1)[0]
    assert "lt-proj-teaser-schema" in teaser and "<figcaption" not in teaser, teaser

    # Every carousel has one dot per slide, and its arrows read previous, then next.
    research = next((public / "research").glob("*/index.html")).read_text(encoding="utf-8")
    for html, noun in ((home, "paper"), ((public / "publication" / "index.html").read_text(encoding="utf-8"), "highlight"),
                       (research, "topic")):
        navs = carousel_navs(html)
        assert navs, noun
        for slides, dots, arrows in navs:
            assert slides and slides == dots, (noun, slides, dots)
            assert arrows == [f"Previous {noun}", f"Next {noun}"], arrows

    print("Rendered-template checks passed.")
