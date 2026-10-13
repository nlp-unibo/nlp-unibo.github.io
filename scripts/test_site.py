"""Self-checks for the link parser, front-matter loader, category, venue rank, proposal, page, and missing-publication rules in site.py: uv run python scripts/test_site.py"""

from datetime import date
import importlib.util
from pathlib import Path

import yaml

# site.py shares its name with a standard-library module, so it is loaded by path.
spec = importlib.util.spec_from_file_location("site_tools", Path(__file__).with_name("site.py"))
site_tools = importlib.util.module_from_spec(spec)
spec.loader.exec_module(site_tools)
EMAIL, UniqueKeyLoader, local_link_targets = site_tools.EMAIL, site_tools.UniqueKeyLoader, site_tools.local_link_targets
category_error = site_tools.category_error
view_errors = site_tools.view_errors
same_keyword = site_tools.same_keyword

page = Path("content/news/example/index.md")
body = """
[spaced](<my file.pdf>) [ref][r] `[code](missing.pdf)`
~~~
[fenced](missing.pdf)
~~~
[author](/author/federico-ruggeri/) [mail](mailto:a@unibo.it) [image](photo@2x.png)

[r]: reference.pdf
"""
targets = [target for target, _ in local_link_targets(page, body)]
assert targets == ["my file.pdf", "photo@2x.png", "reference.pdf"], targets
assert EMAIL.fullmatch("a.galassi@unibo.it")

try:
    yaml.load("title: a\ntitle: b\n", Loader=UniqueKeyLoader)
except yaml.YAMLError:
    pass
else:
    raise AssertionError("repeated keys must be rejected")

# The venue rank selects the Highlights, so `Highlight` is no longer a category.
assert category_error("publication", ["Journal"]) is None
assert category_error("publication", ["Highlight", "Journal"])
assert category_error("publication", ["Highlight"])
assert category_error("publication", ["Journal", "Conference"])
assert category_error("theses", ["Highlight", "Master thesis"])

assert same_keyword("argument mining", "Argument-Mining")
assert same_keyword("dialogue system", "dialogue systems")
assert same_keyword("argument mining", "argument minig")
assert not same_keyword("abductive reasoning", "deductive reasoning")
assert not same_keyword("multilingual", "multilingualism")

view = {"roles": [{"key": "clause"}], "texts": [{"segments": [{"id": "a", "role": "clause", "text": "x"}]}],
        "implicit": [{"id": "b", "role": "clause"}], "rows": [["a", "b"]], "edges": [{"from": "a", "to": "b", "relation": "support"}]}
assert view_errors(view) == [], view_errors(view)
assert view_errors({**view, "rows": [["a", "c"]]}) == ["rows or edges name an undefined component 'c'"]
assert view_errors({**view, "roles": []}) == ["component 'a' has an unknown role", "component 'b' has an unknown role"]
assert view_errors({**view, "implicit": [{"id": "a", "role": "clause"}, {"id": "b", "role": "clause"}]}) == ["component 'a' is repeated"]
assert view_errors({**view, "edges": [{"from": "a", "to": "b", "relation": "rebut"}]}) == ["edge relation 'rebut' is not support, attack, or link"]
assert view_errors({**view, "roles": [{"key": "clause", "label": "Claim"}, {"key": "c", "label": "Conclusion"}]}) == ["roles share the short name 'C'; set `short` on one of them"]
assert view_errors({**view, "roles": [{"key": "clause", "label": "Claim"}, {"key": "c", "label": "Conclusion", "short": "Co"}]}) == []
voices = {"type": "voices", "question": "Claim?", "readings": [{"gold": "No", "words": [{"w": "we", "dur": 0.2, "pitch": [0.4, 0.5], "loud": 0.5}]}],
          "models": [{"label": "Text", "answers": ["Yes"]}]}
assert view_errors(voices) == [], view_errors(voices)
assert view_errors({**voices, "models": [{"label": "Text", "answers": ["Yes", "No"]}]}) == ["model 'Text' needs one answer per reading"]
assert view_errors({**voices, "question": ""}) == ["voices view needs readings and a question"]
assert view_errors({**voices, "readings": [{"gold": "No", "words": [{"w": "we", "dur": 0, "pitch": [0.4], "loud": 2}]}]}) == [
    "reading 1: word 'we' needs a positive dur, a loud in [0, 1], and a pitch pair in [0, 1]"]

detect = {"type": "detect", "sections": [{"sentences": [{"text": "x"}, {"text": "y", "category": "Arbitration", "level": 2}]}]}
assert view_errors(detect) == [], view_errors(detect)
assert view_errors({**detect, "sections": []}) == ["detect view has no sentences"]
assert view_errors({"type": "detect", "sections": [{"sentences": [{"text": "y", "level": 4}]}]}) == ["sentence 1 needs a category and a level of 1, 2, or 3"]

rules = {"type": "rules", "rules": [{"level": 2, "n": 2, "category": "open", "specification": "open", "subcategory": "any"}],
         "sections": [{"sentences": [{"level": 2, "rule": 2, "parts": [
             {"role": "category", "type": "open", "text": "information"},
             {"role": "specification", "type": "open", "parts": [{"text": "such as"}, {"role": "subcategory", "type": "closed", "text": "name"}]}]}]}]}
assert view_errors(rules) == [], view_errors(rules)
assert view_errors({**rules, "rules": [{**rules["rules"][0], "category": "closed"}]}) == ["sentence 1: category is open, but level 2 rule 2 needs closed"]
assert view_errors({**rules, "rules": [{**rules["rules"][0], "n": 3}]}) == ["sentence 1: level 2 rule 2 is not listed"]

# A conference takes an ICORE class and a journal an SJR quartile; a workshop takes no rank.
venue_rank_error, proposal_errors = site_tools.venue_rank_error, site_tools.proposal_errors
assert venue_rank_error("Conference", "A*") is None
assert venue_rank_error("Conference", "Multiconference") is None
assert venue_rank_error("Journal", "Q1") is None
assert venue_rank_error("Journal", "") is None
assert venue_rank_error("Conference", "Q1")
assert venue_rank_error("Journal", "A")
assert venue_rank_error("Workshop", "B")

proposal = {"summary": "One short sentence.", "brief": "Two short sentences. Here.", "contacts": ["federico-ruggeri", {"name": "A B", "email": "a@unibo.it"}]}
body = "\n## Context\n\nText.\n\n## Objective\n\nText.\n\n{{< svg src=\"a.svg\" caption=\"## not a heading\" >}}\n"
assert proposal_errors(proposal, body, {"federico-ruggeri"}) == [], proposal_errors(proposal, body, {"federico-ruggeri"})
assert proposal_errors(proposal, "", {"federico-ruggeri"}) == []
assert proposal_errors(proposal, body, set()) == ["contact 'federico-ruggeri' is not a folder in content/authors"]
assert proposal_errors({**proposal, "contacts": [{"name": "A B"}]}, body, set()) == ["contact {'name': 'A B'} needs a name and an email"]
assert proposal_errors({**proposal, "brief": "word " * 71}, body, {"federico-ruggeri"}) == ["brief has 71 words; keep it at most 70"]
assert proposal_errors(proposal, "## Background\n\nText.", {"federico-ruggeri"}) == ["body sections are ['Background']; use exactly ## Context and ## Objective"]

# OpenAlex works are matched to publication pages by DOI, then by title; datasets and duplicate preprints are skipped.
missing_works, work_key = site_tools.missing_works, site_tools.work_key
def work(id, title, type="article", doi=None):
    return {"id": f"https://openalex.org/{id}", "doi": doi and f"https://doi.org/{doi}", "display_name": title, "type": type}
works = [work("W1", "On Pages", doi="10.1/A"), work("W2", "A Paper Title Here"), work("W3", "A New Paper"), work("W4", "A New Paper", "preprint"),
         work("W5", "Data", "dataset"), work("W6", "Only A Preprint", "preprint"), work("W7", "Only a preprint", "preprint"), work("W8", "Ignored")]
site = [("10.1/a", "Another title"), ("", "A paper title here.")]
assert [w["id"][-2:] for w in missing_works(works, site, {"w8"})] == ["W3", "W6"], missing_works(works, site, {"w8"})
assert work_key(works[0]) == "10.1/a" and work_key(works[1]) == "w2"

# One page is checked through page_errors, which reads nothing from disk: the vocabulary and the file test are passed in.
page_errors, Vocabulary = site_tools.page_errors, site_tools.Vocabulary
vocabulary = Vocabulary(venues={"acl": {"rank": "A*"}}, keywords=["argument mining"], topics={"nlp": {"label": "NLP"}},
                        focus_topics={"argumentation/fallacies"}, authors={"federico-ruggeri"})
person = {"title": "Ada Rossi", "first_name": "Ada", "last_name": "Rossi", "user_groups": ["Members"], "build": {"render": "always"},
          "email": "ada@unibo.it"}
def errors(section, slug, metadata, body="", **options):
    return page_errors(section, slug, metadata, body, vocabulary, **options)[0]
assert errors("authors", "ada-rossi", person) == [], errors("authors", "ada-rossi", person)

assert errors("authors", "ada", person) == ["author slug must be 'ada-rossi'"]
assert errors("authors", "Ada_Rossi", {**person, "title": "Ada_Rossi"})[0] == "invalid slug 'Ada_Rossi'"
assert errors("authors", "ada-rossi", {**person, "user_groups": ["Members", "Former Members"]}) == [
    "user_groups must be exactly one of Associate Fellows, External Collaborators, Former Members, Members"]
assert errors("authors", "ada-rossi", {**person, "email": ""}) == ["required field 'email' is empty"]
assert errors("authors", "ada-rossi", {**person, "email": "", "user_groups": ["Former Members"]}) == []

news = {"title": "Accepted", "date": "2026-01-10", "summary": ""}
assert errors("news", "accepted", news) == ["required field 'summary' is empty"]
assert errors("news", "accepted", {**news, "tags": ["Paper"]}) == []
assert errors("news", "accepted", {**news, "summary": "Lorem ipsum."}) == ["contains Lorem ipsum"]
assert errors("news", "accepted", {**news, "summary": "Draft.", "draft": True}, body="TODO") == []
assert page_errors("news", "accepted", {**news, "summary": "S."}, "", vocabulary, today=date(2026, 1, 9))[1] == [
    "future publication date 2026-01-10"]

page = Path("content/news/accepted/index.md")
body = "[slides](slides.pdf) [mail](a.b@unibo.it)"
assert errors("news", "accepted", {**news, "summary": "S."}, body, page=page, exists=lambda path: False) == [
    "local link 'slides.pdf' does not exist", "email link 'a.b@unibo.it' must start with mailto:"]
assert errors("news", "accepted", {**news, "summary": "S."}, body, page=page,
              exists=lambda path: path == page.parent / "slides.pdf") == ["email link 'a.b@unibo.it' must start with mailto:"]

paper = {"title": "P", "authors": ["A"], "date": "2025-01-01", "publication_types": ["paper-conference"],
         "categories": ["Conference"], "venue_key": "acl", "tags": ["argument mining"], "focus": ["argumentation/fallacies"]}
assert errors("publication", "p", paper, bib="") == []
assert page_errors("publication", "p", paper, "", vocabulary)[1] == ["missing cite.bib"]
assert errors("publication", "p", {**paper, "venue_key": "acm"}, bib="") == ["venue_key 'acm' is not defined in data/venues.yaml"]
assert errors("publication", "p", {**paper, "categories": ["Journal"]}, bib="") == [
    "venue rank 'A*' does not fit a Journal paper, which takes an SJR quartile: '', 'Q1', 'Q2', 'Q3', 'Q4'; check venue_key or categories"]
assert errors("publication", "p", {**paper, "publication_types": ["poster"]}, bib="") == [
    "publication_types must be exactly one of article, article-journal, book, chapter, paper-conference, report, thesis"]
assert errors("publication", "p", {**paper, "tags": ["Argument-Mining"]}, bib="") == [
    "tag 'Argument-Mining' is not in data/tags.yaml; use the existing 'argument mining'"]
assert errors("publication", "p", {**paper, "tags": ["speech"]}, bib="") == [
    "tag 'speech' is not in data/tags.yaml; add it there if it is a new keyword"]
assert errors("publication", "p", {**paper, "focus": ["argumentation/other"]}, bib="") == [
    "focus topic 'argumentation/other' is not a <area>/<key> of content/research"]
assert errors("publication", "p", {**paper, "categories": ["Preprint", "Conference"]}, bib="") == [
    "categories must be exactly one of Conference, Journal, Preprint, Workshop"]

area = {"title": "A", "date": "2025-01-01", "summary": "S.", "focus": [{"key": "f"}, {"key": "f"}], "fields": [{}]}
assert sorted(errors("research", "a", area)) == ["fields key None is missing or repeated", "focus key 'f' is missing or repeated"]
tool = {"title": "T", "date": "2025-01-01", "summary": "S.", "external_link": "https://x.org", "topics": ["nlp", "vision"]}
assert errors("tools", "t", tool) == ["topic 'vision' is not defined in data/topics.yaml"]
assert errors("proposals", "topic", {"title": "T", "summary": "S."}, required=site_tools.TOPIC_FIELDS) == []

print("site.py self-checks passed.")
