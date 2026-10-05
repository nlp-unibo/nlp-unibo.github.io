"""Self-checks for the link parser, front-matter loader, and category rule in site.py: uv run python scripts/test_site.py"""

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

assert category_error("publication", ["Journal"]) is None
assert category_error("publication", ["Highlight", "Journal"]) is None
assert category_error("publication", ["Highlight"])
assert category_error("publication", ["Journal", "Conference"])
assert category_error("publication", ["Highlight", "Highlight", "Journal"])
assert category_error("theses", ["Highlight", "Master thesis"])

view = {"roles": [{"key": "clause"}], "texts": [{"segments": [{"id": "a", "role": "clause", "text": "x"}]}],
        "implicit": [{"id": "b", "role": "clause"}], "rows": [["a", "b"]], "edges": [{"from": "a", "to": "b", "relation": "support"}]}
assert view_errors(view) == [], view_errors(view)
assert view_errors({**view, "rows": [["a", "c"]]}) == ["rows or edges name an undefined component 'c'"]
assert view_errors({**view, "roles": []}) == ["component 'a' has an unknown role", "component 'b' has an unknown role"]
assert view_errors({**view, "implicit": [{"id": "a", "role": "clause"}, {"id": "b", "role": "clause"}]}) == ["component 'a' is repeated"]
assert view_errors({**view, "edges": [{"from": "a", "to": "b", "relation": "rebut"}]}) == ["edge relation 'rebut' is not support, attack, or link"]

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

print("site.py self-checks passed.")
