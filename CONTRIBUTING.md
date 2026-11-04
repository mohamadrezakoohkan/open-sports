# Maintaining the product knowledge

## Evidence and status

| Label | Meaning | Promotion rule |
|---|---|---|
| Confirmed | Explicit user decision or directly stated product constraint | Cite a source ID and the exact supported scope |
| Proposal | Concrete option awaiting a decision | Keep its origin and alternatives; adoption needs explicit evidence |
| Rejected | Explicitly declined option, or option ruled out by a confirmed constraint | State which kind, scope, and known rationale; do not invent a historical debate |
| Open | Missing or unresolved product choice | Assign a question ID, impact, and decision owner role |
| Derived recommendation | Reasoning introduced during documentation work | State the derivation and whether selected under DEC-060 or merely suggested |

Status belongs to the claim, not merely the file. Mixed files label sections and
rows. A section-level label covers its subordinate bullets unless explicitly
overridden. Acceptance criteria under a Confirmed requirement are **derived
verification criteria**; they cannot expand the confirmed scope. Criteria for
proposed behavior remain proposed. Test cases have execution status separately.

The evidence register distinguishes original user instructions from the current
task, repository inspection, and external engineering references. External references
explain recommendations; they do not establish product decisions.

DEC-060 delegates remaining small defaults. The selected defaults in
[derived defaults](docs/decisions/derived-defaults.md) form the current implementation
baseline within confirmed constraints while retaining the Derived recommendation
label. Future ideas remain proposals; the delegation does not adopt them or select
a technology vendor. Do not relabel a delegated default as an explicit historical choice.

## Canonical locations

| Subject | Canonical file |
|---|---|
| Provenance and accessible source excerpts | [Evidence](docs/sources/conversation-evidence.md) |
| Unavailable source and retrieval limits | [Recovery status](docs/sources/recovery-status.md) |
| Decision, alternative, and proposal history | [Decision log](docs/decisions/decision-log.md) |
| Delivery scope | [MVP](docs/product/mvp.md) |
| Functional behavior and acceptance criteria | [Requirements](docs/product/requirements.md) |
| Contact authorization and lifecycle | [Communication/privacy](docs/product/communication-and-privacy.md) |
| Entity semantics and state invariants | [Domain model](docs/architecture/domain-model.md) |
| Architecture and engineering constraints | [Architecture](docs/architecture/technical-overview.md) |
| Unresolved choices | [Open questions](docs/planning/open-questions.md) |
| Verification scenarios and coverage | [Validation index](docs/README.md#validation) |

Summaries and journeys link to canonical rules. If a summary differs from its
canonical rule, fix the summary; if the rule conflicts with the evidence, preserve
the discrepancy and resolve the evidence first.

## Change procedure

1. Inspect the checkout, branch, existing instructions, and source status.
2. Add new evidence with speaker, message or document identifier, date if known,
   and an exact excerpt. Avoid unsupported dates, real contacts, and credentials.
3. Use a new DEC identifier for an adopted or superseding decision; retain the old
   record and add `Superseded by` links. Do not recycle identifiers.
4. Change requirements, scope, privacy rules, domain invariants, journeys, and tests
   that depend on that decision. Update the traceability rows in the same PR.
5. Record open conflicts instead of choosing whichever source sounds more precise.
   A later explicit user correction supersedes an earlier decision; a later assistant
   suggestion alone does not.
6. Add a changelog entry, run the checker, and perform the manual evidence review.
7. Submit on a dedicated branch with limitations and validation stated in the PR.

For newly recovered assistant messages, preserve their suggestions as proposals
until linked to an explicit user adoption. Recovery may reveal additional confirmed
requirements; the current baseline is not a reason to discard them.

## IDs and writing conventions

- SRC = evidence; DEC = confirmed decision; PROP = proposal; REJ = rejected option;
  Q = open question; REQ = requirement; J = journey; TEST = acceptance scenario.
- Three-digit stable numbers, for example `REQ-003`. Canonical records declare an
  explicit HTML anchor with the lower-case ID. Links use that anchor.
- Keep acceptance criteria observable. Identify actor, precondition, action,
  result, and denial/failure behavior. Avoid exact limits without a sourced
  decision; proposed limits need their own label.
- Use the [decision template](docs/decisions/template.md) for a new decision.
- Use English in this package; product UI supports English and Spanish.
- Version dates use ISO format; product event times use match-local time with an explicit zone.

## Review checklist

- Evidence is accessible or explicitly marked unavailable.
- No proposal was promoted through rewriting, tables, diagrams, or test wording.
- All confirmed constraints have requirements and acceptance coverage.
- Rejected alternatives retain scope and evidence; rationale gaps remain visible.
- Privacy examples use fictional participants and no real contact values.
- Source and context limitations remain prominent in README and delivery report.
- Product tests are marked Not run until an implementation actually executes them.
