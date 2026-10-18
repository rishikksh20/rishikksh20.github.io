#!/usr/bin/env python3
"""Render the checked-in CV page from PROFILE.md (development tool only)."""

import html
import re
import unicodedata
from pathlib import Path

try:
    from markdown_it import MarkdownIt
except ImportError:
    raise SystemExit("Install the renderer: python3 -m pip install -r scripts/requirements.txt")

ROOT = Path(__file__).resolve().parent.parent
markdown = MarkdownIt("commonmark", {"html": False}).enable("table")
tokens = markdown.parse((ROOT / "PROFILE.md").read_text())
sections = []
used_slugs = set()
for index, token in enumerate(tokens):
    if token.type != "heading_open":
        continue
    title = tokens[index + 1].content
    slug = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode().lower()
    slug = re.sub(r"[^a-z0-9\s-]", "", slug)
    slug = re.sub(r"\s+", "-", slug.strip())
    candidate = slug
    counter = 1
    while candidate in used_slugs:
        candidate = f"{slug}-{counter}"
        counter += 1
    used_slugs.add(candidate)
    token.attrSet("id", candidate)
    if token.tag == "h2":
        sections.append((candidate, title))

body = markdown.renderer.render(tokens, markdown.options, {})
body = body.replace('href="https://rishikksh20.github.io/"', 'href="index.html"')
body = body.replace('href="https://rishikksh20.github.io/resume.html"', 'href="#cv"')
body = body.replace("<table>", '<div class="table-scroll" role="region" aria-label="CV reference table" tabindex="0"><table>')
body = body.replace("</table>", "</table></div>")
toc = "\n".join(f'<a href="#{slug}">{html.escape(title)}</a>' for slug, title in sections)
template = (ROOT / "scripts/cv-template.html").read_text()
output = template.replace("<!-- CONTENTS -->", toc).replace("<!-- CV -->", body)
(ROOT / "resume.html").write_text(output)
print(f"Rendered resume.html from PROFILE.md ({len(sections)} sections)")
