# Source recovery and completeness

**Status: current documentation baseline complete; historical coverage partial.**
Prepared 2026-11-04. A complete file set is not a claim that the entire earlier
conversation was available.

## What was accessible

The [evidence register](conversation-evidence.md) preserves the five returned user
turns verbatim, the current task, the repository URL clarification, and inspection
results. The prior-conversation preview adds no distinct product evidence beyond
those turns; its final long user request was truncated, but the reader recovered
that request in full.

| Source | Recoverable content | Treatment |
|---|---|---|
| [SRC-001](conversation-evidence.md#src-001) | Request to design join flow, host approvals, roles, availability, external chat | Topics to resolve, not adopted behavior |
| [SRC-002](conversation-evidence.md#src-002) | Instant join for public matches | Confirmed constraint |
| [SRC-003](conversation-evidence.md#src-003) | External chat only for MVP | Confirmed constraint |
| [SRC-004](conversation-evidence.md#src-004) | Optional participant-to-participant contact sharing with consent | Confirmed constraint |
| [SRC-005](conversation-evidence.md#src-005) | Full documentation task, placeholder URL, fidelity and validation instructions | Documentation scope/history |
| [SRC-006](conversation-evidence.md#src-006) | Open-source sports matchmaking PWA; current delivery instructions | Confirmed product identity and delivery scope |
| [SRC-007](conversation-evidence.md#src-007) | Actual GitHub URL | Repository destination |
| [SRC-008](conversation-evidence.md#src-008) | Empty repository, branch and permission observations | Delivery limitation |
| [SRC-009](conversation-evidence.md#src-009) | Current user decisions on sport/geography, host occupancy, and joining eligibility | New confirmed constraints; age wording subsequently clarified in SRC-010 |
| [SRC-010](conversation-evidence.md#src-010) | Adults-only MVP without age display/filters; skill/role-only host criteria; self-declared skill per sport | Adults-only subsequently superseded; other refinements retained |
| [SRC-011](conversation-evidence.md#src-011) | Three-level skill scale, optional role places, and explicit exclusion of age declaration | New confirmed refinements; age policy later resolved by SRC-012/013 |
| [SRC-012](conversation-evidence.md#src-012) | All ages; one-way named-person/match sharing including non-playing hosts; four contact methods | Age-policy supersession; private grant model later superseded |
| [SRC-013](conversation-evidence.md#src-013) | No age-specific product flow/messages; no scheduled contact expiry; keep grants after leaving with named invalidation events | Age topic closed; grant lifecycle later superseded |
| [SRC-014](conversation-evidence.md#src-014) | Contact interpretation corrected; pre-join visibility; host cutoff and management powers | Contact model corrected, no host transfer |
| [SRC-015](conversation-evidence.md#src-015) | Owner-selected contacts public on profiles/match pages, including anonymous access | Current public model replaces named-recipient grants |
| [SRC-016](conversation-evidence.md#src-016) | Shared join/leave cutoff, reconfirm after time/location changes, unchecked overlaps | Leaving component later superseded |
| [SRC-017](conversation-evidence.md#src-017) | Immediate place release, new shared deadline, automatic nonresponse removal | Competitive reconfirmation adopted |
| [SRC-018](conversation-evidence.md#src-018) | In-app service notices only; leave anytime; compatible capacity/role/skill edits | Current admission-only deadline |
| [SRC-019](conversation-evidence.md#src-019) | Optional skill for Any level, unrestricted skill edits, custom sports/roles, mixed pools, removal exclusion | Current refinements |
| [SRC-020](conversation-evidence.md#src-020) | Email/password; public names/skill/roles/history; no avatars; map/distance and filters | Current refinements |
| [SRC-021](conversation-evidence.md#src-021) | Public exact location, English/Spanish, match-local time, free public-only MVP and explicit deferrals | Retained; language coverage extended by DEC-062 |
| [SRC-022](conversation-evidence.md#src-022) | Start/end and automatic completion, upcoming-only profiles, no email verification | Supersedes past-match list selection |
| [SRC-023](conversation-evidence.md#src-023) | Optional device map origin, external support only, account deletion effects | Current refinements |
| [SRC-024](conversation-evidence.md#src-024) | Global countries allowed, terminal state-only pages, GitHub Issues support | Current refinements |
| [SRC-025](conversation-evidence.md#src-025) | Deletion covers ongoing matches, private removal reasons, immediate deletion/30-day retention | Current refinements |
| [SRC-026](conversation-evidence.md#src-026) | Neutral architecture, AGPL-3.0-only, installable online-only PWA | Backend deferral superseded by DEC-061; other choices retained |
| [SRC-027](conversation-evidence.md#src-027) | Host eligibility/role switching, browser/accessibility baseline, delegated defaults and finish instruction | Closes question rounds |
| [SRC-028](conversation-evidence.md#src-028) | Final remote inspection: still empty, no branch/PR base, connector read-only | Final delivery limitation |
| [SRC-029](conversation-evidence.md#src-029) | Research open-source backends and free cloud hosting | Research scope; assistant recommendations are not decisions |
| [SRC-030](conversation-evidence.md#src-030) | Select Supabase | Backend selection partially supersedes DEC-055 through DEC-061 |
| [SRC-031](conversation-evidence.md#src-031) | Follow-up inspection finds main and reading-guide branches | A PR base now exists; earlier delivery observations remain historical |
| [SRC-032](conversation-evidence.md#src-032) | Add Dutch and Netherlands market | Additive MVP language/pilot expansion under DEC-062 |

## Unavailable assistant bodies

| Message ID | Returned reference index | Missing subject |
|---|---|---|
| `9eb4191a-59f7-4e62-95b2-c4eac26cde08` | 1 | Rules and player/host flows after instant-join selection |
| `489490f9-8a43-4bca-910b-ed3d8d53ed41` | 2 | Detailed external communication and privacy rules |
| `a63188a8-daea-46a7-b82c-01768d498e18` | 3 | Detailed optional contact-sharing design |
| `cbdaa21f-ab7e-4df7-9fcf-954c3f129d9d` | 0 | Earlier response to the repository-documentation task |

The references contained no usable reply text. A content-reference index is not a
summary of the missing reply. No requirements were inferred from those bodies.
No assistant reply was returned for the earliest join-flow design request.

## Earlier context that remains unavailable

The returned view begins with the request to design joining. Any earlier vision,
persona research, sport choices, business model, MVP boundary, technical stack,
UX decisions, data model, rejected alternatives, or roadmap commitments are
unknown. Even whether each of these was discussed cannot be verified from the
accessible view. Their omission does not establish that they were never decided.

## Retrieval attempts and limits

1. Read the referenced conversation with a ten-turn limit and the maximum allowed
   per-item output length. Five turns were returned; no older cursor was supplied.
2. Read the full returned user messages and checked the cached preview for additions.
3. Tried the original conversation URL in the available browser. It showed a
   logged-out page and “Not Found,” not the conversation. No login was changed.
4. Inspected the current workspace and the user-supplied GitHub repository. Both
   provided no existing product documentation; the remote was empty.

An initial reader call requested too large an item limit; it was corrected. This
was an argument error, not evidence that older messages do not exist. No attachments
were returned by the successful reader call.

## Recovery work to perform when more evidence arrives

The owner can supply the original transcript or accessible assistant reply text.
Record it with message identifiers where available. Compare it to the current
decisions, then reconcile these likely high-impact gaps first:

1. Exact MVP scope, target sports, geography, and audience.
2. Host/player roles, slot counts, capacity, eligibility, cancellation and removal.
3. Contact consent scope, provider selection, expiry and revocation.
4. Existing technology, license, deployment and privacy commitments.
5. Alternatives, rationale and superseded decisions.

Preserve new conflicts in [open questions](../planning/open-questions.md). Do not
quietly overwrite reconstructed proposals or attribute them to the old conversation.
Use the [maintenance procedure](../../CONTRIBUTING.md) to adopt or supersede records.

## Completeness judgment

- The initial four constraints (three from recovered product choices and product
  identity from the current task) are preserved and explicitly refined where
  corrected. Fifty-eight subsequent decision records capture current clarifications.
  These are new decisions, not recovered older history.
- Current requirements, scenarios and traceability cover the resulting baseline.
  Small defaults are selected under the owner's explicit delegation and labeled accordingly.
- All five available historical user turns are preserved.
- Product question rounds are complete. Supabase is now selected as the backend;
  Dutch and the Netherlands are added to language/pilot scope. Remaining providers
  and operational launch gates are recorded as Open.
- Full fidelity to the unavailable conversation cannot be validated.
- No implementation readiness, release readiness, or legal compliance is claimed.
