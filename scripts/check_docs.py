#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-only
"""Dependency-free checks for this Markdown documentation repository.

Checks the repository's inline-link convention, explicit stable-ID anchors,
required content, and requirement/decision traceability. This is not a general
Markdown parser, external-link checker, or product acceptance-test runner.
"""

from collections import Counter
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md", "AGENTS.md", "CONTRIBUTING.md", "CHANGELOG.md", "LICENSE", "LICENSE-STATUS.md",
    ".github/PULL_REQUEST_TEMPLATE.md", "docs/README.md", "docs/delivery.md",
    "docs/sources/conversation-evidence.md", "docs/sources/recovery-status.md",
    "docs/sources/external-references.md",
    "docs/product/vision-and-principles.md", "docs/product/mvp.md",
    "docs/product/requirements.md", "docs/product/journeys.md",
    "docs/product/communication-and-privacy.md", "docs/product/ux.md",
    "docs/architecture/domain-model.md", "docs/architecture/technical-overview.md",
    "docs/architecture/security-and-nonfunctional.md", "docs/decisions/decision-log.md",
    "docs/decisions/template.md", "docs/decisions/derived-defaults.md",
    "docs/decisions/history/contact-grants-before-correction.md", "docs/planning/open-questions.md",
    "docs/planning/roadmap.md", "docs/validation/traceability.md",
    "docs/validation/acceptance-tests.md", "docs/validation/validation-report.md",
    "docs/validation/ai-instruction-review.md",
]
ID = r"(?:SRC|DEC|PROP|REJ|Q|REQ|J|TEST)-\d{3}"
LINK = re.compile(r"(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)")


def prose(text):
    """Remove fenced code while preserving prose, headings, and HTML anchors."""
    result, fence = [], None
    for line in text.splitlines():
        marker = re.match(r"^\s*(`{3,}|~{3,})", line)
        if marker:
            token = marker.group(1)
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            continue
        if fence is None:
            result.append(line)
    return "\n".join(result)


def anchors(text):
    result = set(re.findall(r'<a\s+id="([^"]+)"\s*>', text))
    counts = Counter()
    for heading in re.findall(r"^#{1,6}\s+(.+?)\s*#*\s*$", text, re.M):
        heading = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", heading)
        slug = re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
        n = counts[slug]
        counts[slug] += 1
        result.add(slug if not n else f"{slug}-{n}")
    return result


def main():
    errors = []
    for rel in REQUIRED:
        if not (ROOT / rel).is_file():
            errors.append(f"Missing required file: {rel}")
    files = sorted(p for p in ROOT.rglob("*.md") if ".git" not in p.parts)
    raw = {p: p.read_text(encoding="utf-8") for p in files}
    texts = {p: prose(t) for p, t in raw.items()}
    anchor_sets = {p: anchors(t) for p, t in texts.items()}
    declared = {}
    for path, text in texts.items():
        for value in re.findall(r'<a\s+id="([^"]+)"\s*>', text):
            if re.fullmatch(ID, value.upper()):
                key = value.upper()
                if key in declared:
                    errors.append(f"Duplicate canonical ID {key}: {path.relative_to(ROOT)}")
                declared[key] = path
    links = 0
    for path, text in texts.items():
        for target in LINK.findall(text):
            target = target.strip().strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc:
                continue
            links += 1
            dest = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            try:
                dest.relative_to(ROOT)
            except ValueError:
                errors.append(f"Link escapes repository: {path.relative_to(ROOT)} -> {target}")
                continue
            if not dest.exists():
                errors.append(f"Broken link: {path.relative_to(ROOT)} -> {target}")
            elif parsed.fragment and dest.suffix == ".md":
                if unquote(parsed.fragment) not in anchor_sets.get(dest, set()):
                    errors.append(f"Missing anchor: {path.relative_to(ROOT)} -> {target}")
        # Archived source and the template may quote arbitrary identifiers.
        if path.name not in {"conversation-evidence.md", "template.md"}:
            for key in set(re.findall(rf"\b{ID}\b", text)):
                if key not in declared:
                    errors.append(f"Undeclared ID {key}: {path.relative_to(ROOT)}")
    trace = texts.get(ROOT / "docs/validation/traceability.md", "")
    req_text = texts.get(ROOT / "docs/product/requirements.md", "")
    for key in sorted(declared):
        if key.startswith(("REQ-", "DEC-")) and key not in trace:
            errors.append(f"Missing traceability coverage for {key}")
        if key.startswith("REQ-"):
            match = re.search(rf'<a id="{key.lower()}"></a>(.*?)(?=<a id="req-|\Z)', req_text, re.S)
            if not match or "Acceptance criteria" not in match.group(1):
                errors.append(f"Missing acceptance criteria for {key}")
    req_rows = [line for line in trace.splitlines() if re.match(r"\| \[REQ-\d{3}\]", line)]
    for line in req_rows:
        if not re.search(r"TEST-\d{3}", line):
            errors.append(f"Requirement traceability row lacks a test: {line}")
    for p, text in raw.items():
        if not text.endswith("\n"):
            errors.append(f"Missing final newline: {p.relative_to(ROOT)}")
        if "\x00" in text:
            errors.append(f"NUL byte: {p.relative_to(ROOT)}")
    if errors:
        print("FAIL — documentation checks")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"PASS — {len(files)} Markdown files; {links} local links; {len(declared)} canonical IDs.")
    print("Required files, local targets/anchors, ID references, acceptance sections, and traceability checked.")
    print("External URLs, Mermaid rendering, source fidelity, and product behavior require separate review.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
