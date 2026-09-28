"""Self-checks for the link parser and front-matter loader in site.py: uv run python scripts/test_site.py"""

import importlib.util
from pathlib import Path

import yaml

# site.py shares its name with a standard-library module, so it is loaded by path.
spec = importlib.util.spec_from_file_location("site_tools", Path(__file__).with_name("site.py"))
site_tools = importlib.util.module_from_spec(spec)
spec.loader.exec_module(site_tools)
EMAIL, UniqueKeyLoader, local_link_targets = site_tools.EMAIL, site_tools.UniqueKeyLoader, site_tools.local_link_targets

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

print("site.py self-checks passed.")
