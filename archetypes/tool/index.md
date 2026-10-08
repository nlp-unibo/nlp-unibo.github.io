---
title: '{{ replace .Name "-" " " | title }}'
# The first public release; it orders the Tools page, newest first.
date: '{{ now.Format "2006-01-02" }}'
draft: true
# Keys from data/topics.yaml, shown as colored tags. A system readers cannot use today is a prototype, not a tool.
topics:
  - toolkit
# Shown as a pill under the name, such as Web service, Web demo, or Python library.
kind: Python library
summary: "TODO: Say what the tool does in at most two sentences."

# An SVG file in this folder drawn with the `lt-s-*` classes, and a caption that names its source.
# schema: schema.svg
# caption: "TODO: Say what the schematic shows and where it comes from."

external_link: "https://example.org/"
# Optional link chips: a web demo, the source code, and the folder name of the paper under content/publication/.
# demo: "https://example.org/demo"
# code: "https://github.com/nlp-unibo/<repository>"
# publication: <folder>
# Optional PyPI name, shown as a `pip install` command.
# package: <name>
---
