# Validation report

## Documentation result

The Supabase and Dutch/Netherlands follow-up contains 31 Markdown files, 62 decision records,
36 requirements, 29 acceptance scenarios and selected derived defaults.
Supabase is selected; Dutch and the Netherlands extend language/pilot coverage.
Remaining providers and operational launch gates are Open.
The checks for this follow-up are recorded separately below.

### Supabase and Dutch/Netherlands follow-up — 2026-11-04

Executable checks: `python3 scripts/check_docs.py` and `git diff --check` pass.
The checker covers required files, local links/anchors, stable IDs, acceptance
sections and traceability. It does not execute the product scenarios.

Manual checks: compared the new decisions with exact SRC-030/SRC-032 excerpts;
preserved earlier neutrality, language and market decisions with successor links;
reviewed present-tense summaries, Supabase capability references and derived labels;
checked that Dutch/Netherlands coverage propagates through requirements, journeys,
UX, defaults, roadmap and scenarios without dropping English/Spanish, Spain/UK or
the allowance for other countries. The unchanged retention and no-verification
rules remain explicit; Q-019/020 identify missing operational evidence.

No application, translation catalog or provider configuration was created. No
product, translation-quality, live-email, concurrency, purge or restoration test
has run; TEST-029 and the expanded TEST-020/022 remain Not run. Mermaid diagrams
received textual review only, not rendering. Publication outcome is in the task handoff.

### Original baseline checks — historical PASS, 2026-11-04

Executable checks run:

- `python3 scripts/check_docs.py`: required files, local links/anchors, stable
  identifiers, acceptance sections and decision/requirement traceability.
- Python syntax parsing of the checker: PASS.
- Markdown trailing-whitespace and canonical-ID review: PASS.
- Staged Git whitespace review: recorded with final delivery verification.

Final checker counts are recorded in the accompanying delivery report, so this
file does not invent a pass for a differently packaged copy. Initial failures
were missing traceability rows/scenario coverage while decisions were being added;
they were corrected and the checker passed again.

## Original manual evidence and semantic review — historical PASS for available evidence

- Compared current decisions to recorded user answers, preserving exact answers,
  correction history and unavailable-source boundaries.
- Kept current public contacts separate from superseded private recipient grants.
- Reconciled unrestricted leaving, admission-only cutoff, competitive reconfirmation
  with zero reserved places, revision safety and no double-release.
- Reconciled host compatibility edits with nonretroactive player skill changes.
- Applied removal exclusion, private reasons, eligible playing host and atomic role changes.
- Removed public past lists, avatars, verification gates, in-app moderation/reporting,
  service email/push and offline match-data browsing.
- Applied public exact locations, global location allowance, English/Spanish and
  local-zone time consistently.
- Applied terminal state-only pages, all-unfinished-match deletion and 30-day retention.
- Distinguished explicit choices from selected derived defaults and future proposals.
- Reviewed the three Mermaid diagrams against the textual model. They were not
  rendered by a Mermaid engine; syntax/relationship review is manual.
- Reviewed the canonical GNU license text selection and explicit AGPL-3.0-only identifier.

[AGENTS instruction review](ai-instruction-review.md): final 15-point rule-file
review PASS, including license preservation and delegated-default terminology.
No nested conflicting instruction file was present.

## Product validation — Not run

The reading-guide follow-up passed the documentation checker and Git whitespace
check. A separate coverage check confirmed that the guide links to every other
Markdown document under `docs/`. Manual review checked its reading paths, status
explanations, and contact-visibility example against the canonical documents.
This navigation addition changes no product decisions.

No app implementation exists here. The [acceptance scenarios](acceptance-tests.md)
must be executed after implementation. No browser UI, assistive-technology,
load/performance, penetration, deployment, backup or live deletion test was run.
The [traceability matrix](traceability.md) establishes specification coverage only.

External references were consulted where relevant; there was no automated full
external-link audit. They are background, not substitutes for user decisions.

## Packaging and Git

Archive extraction/file equivalence and Git bundle cloning/checking are performed
as delivery verification and recorded in the accompanying delivery report.
The original final remote inspection remained empty with no PR base; no
default-branch initialization, remote push or PR creation occurred for that delivery.
The [Supabase follow-up inspection](../sources/conversation-evidence.md#src-031)
now finds `main`; current work uses `codex/select-supabase-mvp` for a PR.
See [delivery status](../delivery.md) and the task handoff for publication outcome.

## Historical completeness

Five original user turns and four unavailable assistant references were exposed.
Earlier conversation and reply bodies could not be recovered. The package captures
all available evidence and later answers, but cannot certify full fidelity to
unavailable history. See [recovery status](../sources/recovery-status.md).
