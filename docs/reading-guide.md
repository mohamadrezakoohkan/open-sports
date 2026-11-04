# How to read the documentation

Start here if you are new to Open Sports or need to find the right document for a
decision, design, implementation task, or review. This guide explains how the files
fit together; the [documentation index](README.md) is the shorter directory.
The linked specifications remain the authoritative locations for product rules.

## First reading: understand the current product

Read these in order. Follow detailed requirement and decision links when you need
an exact rule rather than reading the whole historical conversation first.

1. [Repository overview](../README.md) — understand the product, current baseline,
   exclusions, license, and delivery status.
2. [Source coverage and recovery limits](sources/recovery-status.md) — understand
   which original messages were available. The current specification is complete
   under the owner's decisions and delegation; the recovered history is partial.
3. [Vision, users, and principles](product/vision-and-principles.md) — understand
   the intended purpose and distinguish confirmed identity from user hypotheses.
4. [MVP scope](product/mvp.md) — establish what belongs in the first release and
   what is excluded or deferred.
5. [Journeys](product/journeys.md) and [UX guidance](product/ux.md) — follow how
   visitors, players, and hosts experience the product and its failure states.
6. [Requirements and acceptance criteria](product/requirements.md) — read the
   precise behavior. Read [communication and privacy](product/communication-and-privacy.md)
   alongside any profile, contact, roster, notification, or deletion requirement.
7. [Selected derived defaults](decisions/derived-defaults.md) — complete the small
   interaction and engineering details delegated by the owner.
8. [Validation report](validation/validation-report.md) — see what was actually
   checked. Documentation validation does not mean an application has passed tests.

## Choose a path for your work

After the first reading, use the path that matches your task. These paths are
navigation advice, not additional product requirements.

| Your task | Read next, in order | What you should be able to answer |
|---|---|---|
| Assess product scope or priorities | [MVP](product/mvp.md) → [requirements](product/requirements.md) → [decision log](decisions/decision-log.md) → [resolved questions](planning/open-questions.md) → [roadmap](planning/roadmap.md) | What is committed, why it changed, and which ideas remain uncommitted? |
| Design screens and interactions | [Journeys](product/journeys.md) → [UX](product/ux.md) → [privacy](product/communication-and-privacy.md) → [defaults](decisions/derived-defaults.md) → [quality targets](architecture/security-and-nonfunctional.md) | What can each actor see or do, and what happens when an action fails? |
| Implement a feature | Its [requirement](product/requirements.md) → [defaults](decisions/derived-defaults.md) → [domain model](architecture/domain-model.md) → [architecture](architecture/technical-overview.md) → [security and quality](architecture/security-and-nonfunctional.md) → [acceptance scenarios](validation/acceptance-tests.md) | Which rules, permissions, state transitions, and failure cases must the implementation preserve? |
| Review or test behavior | [Traceability](validation/traceability.md) → relevant [requirements](product/requirements.md) and [scenarios](validation/acceptance-tests.md) → [validation report](validation/validation-report.md) | Is every requirement covered, and which checks have actually run? |
| Understand or change a decision | [Decision log](decisions/decision-log.md) → linked [source excerpt](sources/conversation-evidence.md) → [question status](planning/open-questions.md) → [contribution process](../CONTRIBUTING.md) | What is the evidence, what was superseded, and which documents depend on the rule? |

Supabase is selected for the backend in [DEC-061](decisions/decision-log.md#dec-061),
partially superseding the earlier technology-neutral decision. Other vendors in
[external references](sources/external-references.md) remain background unless
explicitly adopted; the Supabase component mapping is a Derived recommendation.
The [roadmap](planning/roadmap.md) is not a promise to ship every listed idea.

## Read status labels before acting on a statement

The full definitions and promotion rules live in [CONTRIBUTING](../CONTRIBUTING.md).
Labels apply to individual claims or labeled sections, not automatically to every
sentence in a file.

| Label or qualifier | How to read it |
|---|---|
| **Confirmed** | An explicit user choice with supporting evidence. Check its scope and any later refinement or supersession. |
| **Derived recommendation** | Reasoning added during documentation. Defaults selected under [DEC-060](decisions/decision-log.md#dec-060) form the current baseline within confirmed constraints; other suggestions are not automatically adopted. |
| **Proposal** | An idea awaiting adoption, unless its record explicitly links to an adopted disposition. Do not treat proposed wording, research hypotheses, or future ideas as confirmed rules. |
| **Rejected** | An excluded or incompatible option within the stated scope. An MVP exclusion is not necessarily a permanent prohibition. |
| **Open** | Missing evidence or an unresolved choice. Read the current resolution: a historical note may have been closed, and some implementation choices are intentionally deferred. |
| **Superseded / historical** | Evidence of a previous position. Follow its replacement link before implementing anything. |

Execution status is separate from product status. A confirmed requirement can have
an acceptance scenario marked **Not run**. This repository specifies the product
but contains no application implementation.

The decision log and changelog preserve earlier states. Do not read an early
record's “Open” wording as a new unanswered question when later records resolve it.
For example, the [earlier private contact-grant design](decisions/history/contact-grants-before-correction.md)
is preserved for history; current [contact publication rules](product/communication-and-privacy.md)
use owner-selected public methods.

## Follow a rule from evidence to verification

Stable identifiers let you connect documents without relying on their order:

| Prefix | Identifies | Canonical location |
|---|---|---|
| SRC | Source evidence | [Conversation evidence](sources/conversation-evidence.md) |
| DEC | Decision, including later supersessions | [Decision log](decisions/decision-log.md) |
| PROP / REJ | Proposal or rejected option | [Decision log](decisions/decision-log.md) |
| Q | Question and its current resolution or deferral | [Question register](planning/open-questions.md) |
| REQ | Requirement and acceptance criteria | [Requirements](product/requirements.md) |
| J | User journey | [Journeys](product/journeys.md) |
| TEST | Acceptance scenario and execution status | [Acceptance scenarios](validation/acceptance-tests.md) |

For example, to understand anonymous contact visibility, follow
[SRC-015](sources/conversation-evidence.md#src-015) →
[DEC-023](decisions/decision-log.md#dec-023) →
[REQ-011](product/requirements.md#req-011) →
[TEST-009](validation/acceptance-tests.md#test-009).
Read the [privacy specification](product/communication-and-privacy.md) for the
complete audience and lifecycle rules. The [traceability matrix](validation/traceability.md)
provides these connections across the baseline, including superseded decisions.

## Complete document map

Use this map when you know the question but not the filename. This guide and the
[index](README.md) cover navigation; the documents below own the detailed content.

| Area | Documents and purpose |
|---|---|
| Product purpose and scope | [Vision and principles](product/vision-and-principles.md): purpose, user hypotheses, trade-offs. [MVP](product/mvp.md): release boundary, exclusions, and implementation gates. |
| Product behavior | [Requirements](product/requirements.md): precise rules and acceptance criteria. [Journeys](product/journeys.md): actor flows and edge cases. [Communication/privacy](product/communication-and-privacy.md): publication, audiences, lifecycle, and external communication. [UX](product/ux.md): interactions, states, language, and accessibility guidance. |
| Architecture | [Domain model](architecture/domain-model.md): glossary, entities, states, relationships, and invariants. [Technical overview](architecture/technical-overview.md): selected Supabase backend, derived component mapping, transactions, trust boundaries, and remaining choices. [Security and non-functional requirements](architecture/security-and-nonfunctional.md): authorization, reliability, operations, browser support, and accessibility targets. |
| Decisions | [Decision log](decisions/decision-log.md): choices, evidence, alternatives, and supersession history. [Derived defaults](decisions/derived-defaults.md): selected small details. [Decision template](decisions/template.md): format for a new decision. [Historical contact grants](decisions/history/contact-grants-before-correction.md): superseded design, retained as context only. |
| Sources | [Conversation evidence](sources/conversation-evidence.md): accessible excerpts and inspection observations. [Recovery status](sources/recovery-status.md): missing history and retrieval limits. [External references](sources/external-references.md): engineering and licensing background, separate from user decisions. |
| Planning | [Question register](planning/open-questions.md): resolutions, intentional deferrals, and unknowable context. [Roadmap](planning/roadmap.md): suggested sequence, research hypotheses, success measures, and uncommitted future ideas. |
| Validation | [Traceability](validation/traceability.md): evidence-to-rule and rule-to-scenario coverage. [Acceptance scenarios](validation/acceptance-tests.md): future product checks. [Validation report](validation/validation-report.md): checks performed and their limits. [AI instruction review](validation/ai-instruction-review.md): review of repository agent guidance, not product certification. |
| Delivery | [Delivery and Git integration](delivery.md): archive/bundle use, branch status, and later integration procedure. |
| Repository overview and maintenance | [Root README](../README.md): baseline and entry points. [CONTRIBUTING](../CONTRIBUTING.md): canonical locations and update procedure. [AGENTS](../AGENTS.md): repository instructions for agents. [CHANGELOG](../CHANGELOG.md): dated evolution, including now-superseded stages. |
| License and review support | [LICENSE](../LICENSE): license text. [License status](../LICENSE-STATUS.md): selected identifier and scope. [PR template](../.github/PULL_REQUEST_TEMPLATE.md): review handoff. [Documentation checker](../scripts/check_docs.py): executable documentation checks. |

## When documents appear to disagree

Start with the relevant [canonical location](../CONTRIBUTING.md#canonical-locations).
Check the decision's status, scope, source, and superseding links. Current rules
must reflect explicit user corrections and the selected defaults within their
delegated scope; a later assistant suggestion alone does not override a decision.

If a summary or journey differs from its canonical rule, correct the summary.
If the canonical rule conflicts with the evidence and explicit later decisions do
not resolve it, preserve the discrepancy and record it through the
[maintenance process](../CONTRIBUTING.md#change-procedure). Do not silently choose
the most detailed-looking statement or invent the contents of an unavailable reply.

## Before changing the documentation

Read [AGENTS](../AGENTS.md) and [CONTRIBUTING](../CONTRIBUTING.md). For a product
behavior change, update the supporting evidence and decision history, then the
affected requirements, privacy/domain rules, journeys, scenarios, traceability,
and changelog. Keep stable identifiers and preserve superseded history.

Run the existing check from the repository root:

```sh
python3 scripts/check_docs.py
```

Review meaning and source fidelity separately. The checker covers local document
structure, links, identifiers, acceptance sections, and traceability; it does not
run the product scenarios, recover missing history, or certify the application.
Follow [delivery guidance](delivery.md) for branch and integration constraints.
When adding or moving a document, update this guide and the [index](README.md).
