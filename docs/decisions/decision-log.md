# Decisions, proposals, and alternatives

This is the canonical status register. Sources are in the
[evidence register](../sources/conversation-evidence.md); inaccessible rationale
is explicitly left unknown. Record date for this reconstruction: 2026-11-04.

**Current contact model:** [DEC-023](#dec-023) and [DEC-024](#dec-024) resolve the
correction in DEC-020: owner-selected public contacts on profiles and match pages,
visible to anonymous visitors without joining. The old named-recipient grant model
is historical, not the implementation contract.

The owner completed the decision rounds in DEC-060. Early scope/open-detail notes
record what was known at the time; current resolutions are in the linked
[requirements](../product/requirements.md), [resolved questions](../planning/open-questions.md)
and [selected defaults](derived-defaults.md). Do not implement a historical superseded rule.

## Decision records — current and superseded

<a id="dec-001"></a>
### DEC-001 — open-source sports matchmaking PWA

- **Status:** Confirmed, from the current task, not recovered historical detail.
- **Source:** [SRC-006](../sources/conversation-evidence.md#src-006).
- **Decision:** The product is an open-source sports matchmaking progressive web app.
- **Scope:** Product identity and delivery format. No named sport, algorithm,
  platform support matrix, license, framework, hosting provider, or revenue model
  follows automatically from that statement.
- **Rationale:** Not provided in the accessible context.
- **Consequences — derived:** Define web and installation expectations; choose an
  explicit license; distinguish finding/joining matches from algorithmic pairing.
- **Links:** [REQ-001](../product/requirements.md#req-001),
  [Q-001](../planning/open-questions.md#q-001), [Q-014](../planning/open-questions.md#q-014).
- **History:** No previous competing platform or license decision was recovered.

<a id="dec-002"></a>
### DEC-002 — public matches use instant join

- **Status:** Confirmed.
- **Source:** [SRC-002](../sources/conversation-evidence.md#src-002).
- **Decision:** Use instant join for public matches.
- **Scope:** Successful public joining does not wait for an individual host approval.
  [DEC-007](#dec-007) now confirms sign-in and host-selected eligibility gates;
  [DEC-009](#dec-009) limits those host criteria to skill and playing role. Instant joining does not
  establish unlimited places or permission to bypass eligibility checks.
- **Rationale:** The user selected this option; their detailed reasoning and the
  assistant's subsequent rule design are unavailable.
- **Consequences — derived:** Admission should return a clear success or failure;
  concurrent requests need consistent membership/capacity handling if adopted.
- **Links:** [REQ-002](../product/requirements.md#req-002),
  [J-002](../product/journeys.md#j-002), [REJ-001](#rej-001).
- **History:** The earlier request included host approvals as a topic, not an
  adopted rule. The later selection resolves public joining only. No confirmed
  earlier approval policy is marked superseded.

<a id="dec-003"></a>
### DEC-003 — external chat only in MVP

- **Status:** Confirmed.
- **Source:** [SRC-003](../sources/conversation-evidence.md#src-003).
- **Decision:** MVP conversation between users happens through external chat.
- **Scope:** No native peer-to-peer or group conversation feature in the MVP.
  Transactional status UI, consent UI, support reporting, and delivery notifications
  are distinct functions whose scope must be decided separately.
- **Rationale:** Not recovered. Reduced implementation work is a plausible derived
  benefit, not a documented reason the user gave.
- **Consequences — derived:** External handoff needs explicit destination/context
  and failure handling; external membership and messages are outside app control.
- **Links:** [REQ-003](../product/requirements.md#req-003),
  [communication rules](../product/communication-and-privacy.md), [REJ-002](#rej-002).
- **History:** Earlier external chat was a design topic; this user instruction
  makes it the explicit MVP choice. Later contact sharing refines coordination
  without changing where chat happens.

<a id="dec-004"></a>
### DEC-004 — optional participant contact sharing with consent

- **Status:** Confirmed.
- **Source:** [SRC-004](../sources/conversation-evidence.md#src-004).
- **Decision:** Support optional participant-to-participant contact sharing with consent.
- **Scope:** Sharing is voluntary; participation alone is not consent. The source
  originally left detailed mechanics open. [DEC-015](#dec-015) historically selected
  directional, named-person, match-scoped sharing including non-playing hosts and
  owner revocation; [DEC-016](#dec-016) selects contact methods. DEC-018 and DEC-019
  historically settled grant lifetime/events. The grant model was later superseded;
  current mechanics are DEC-023/024 and the selected defaults.
- **Current correction:** [DEC-023](#dec-023) and [DEC-024](#dec-024) replace the
  participant-only/named-grant interpretation with voluntary public display selected
  by the contact owner. The original consent intent survives as owner control over
  publication, not recipient-by-recipient permission.
- **Rationale:** Not recovered.
- **Consequences — derived:** Separate match membership from permission to disclose
  contact details. Explain that app-side revocation cannot retrieve copied details.
- **Links:** [REQ-004](../product/requirements.md#req-004),
  [privacy specification](../product/communication-and-privacy.md), [REJ-003](#rej-003).
- **History:** This follows external-chat selection. There is no accessible evidence
  that mandatory disclosure or mandatory group membership was ever accepted.
  Owner-selected public disclosure was explicitly adopted later in DEC-023/024.

<a id="dec-005"></a>
### DEC-005 — any sport, with a Spain and United Kingdom pilot

- **Status:** Confirmed during the current decision round, 2026-11-04.
- **Source:** [SRC-009](../sources/conversation-evidence.md#src-009).
- **Decision:** MVP covers any sport and all cities in Spain and the United Kingdom
  as the pilot footprint. It is not restricted to one pilot city or one sport.
- **Scope:** Country-wide city coverage in both countries. The sport catalog,
  location dataset, supported languages, and behavior outside the pilot remain Open.
- **Age wording:** The initial wording was first clarified as adults-only in
  [DEC-008](#dec-008), then explicitly changed to all ages in [DEC-014](#dec-014).
  No displayed ages or age filters remains the current UI decision.
- **Rationale:** The selection is explicit; no further reason was supplied.
- **Consequences — derived:** Location and time handling must accommodate both
  countries; sport-specific eligibility cannot assume a single shared skill scale.
- **Links:** [REQ-019](../product/requirements.md#req-019).
- **History:** Resolves the prior sports/geography gap. A one-city pilot was not
  adopted. Age eligibility was clarified in the following decision round.

<a id="dec-006"></a>
### DEC-006 — optional host participation and occupancy

- **Status:** Confirmed during the current decision round, 2026-11-04.
- **Source:** [SRC-009](../sources/conversation-evidence.md#src-009).
- **Decision:** The host chooses whether to play; only playing participants occupy
  places. A non-playing host organizes without consuming a player place.
- **Scope:** Organizer status and playing membership are distinct. A playing host
  consumes one place as a participant; the timing and rules for changing that
  choice remains Open. [DEC-022](#dec-022) excludes host transfer from MVP. DEC-015 records
  contact-sharing eligibility for non-playing hosts without special access to others' contacts.
- **Rationale:** The user adopted the suggested occupancy model without adding a reason.
- **Links:** [REQ-020](../product/requirements.md#req-020).
- **History:** Resolves host occupancy within PROP-002; does not approve all other
  membership and host-management proposals.

<a id="dec-007"></a>
### DEC-007 — signed-in joining with host-selected eligibility

- **Status:** Confirmed during the current decision round, 2026-11-04.
- **Source:** [SRC-009](../sources/conversation-evidence.md#src-009).
- **Decision:** Only signed-in users who meet the host-selected skill or other
  eligibility rules may instantly join an available public match place.
- **Scope:** Eligibility is a joining gate, not merely advice. Passing the adopted
  rules still leads to instant joining under DEC-002, without host approval.
- **Refinements:** [DEC-009](#dec-009) limits host criteria to skill and playing role;
  [DEC-010](#dec-010) establishes self-declared levels per sport. [DEC-014](#dec-014)
  removes the former platform adults-only restriction.
- **Open boundaries:** How hosts configure rules, skill scales, role capacities,
  and the effect of rule changes on existing participants.
- **Rationale:** The selection is explicit; no further reason was supplied.
- **Links:** [REQ-002](../product/requirements.md#req-002),
  [REQ-008](../product/requirements.md#req-008).
- **History:** Refines DEC-002. The proposed default of advisory skill alone and
  instant guest joining were not selected.

<a id="dec-008"></a>
### DEC-008 — adults-only MVP without displayed ages or age filters

- **Status:** Confirmed historically; **adults-only restriction superseded by
  [DEC-014](#dec-014)** on 2026-11-04. No age display or age filters remains Confirmed.
- **Source:** [SRC-010](../sources/conversation-evidence.md#src-010).
- **Original decision:** MVP participation was adults only. Age was not to be
  displayed, and the product would have no age filters.
- **Current scope:** Preserve this record as history. Do not enforce its former
  adults-only restriction. [DEC-013](#dec-013) excludes age declaration; DEC-014
  admits all ages; [DEC-017](#dec-017) closes age-specific flows and messaging.
- **Rationale:** Explicit clarification by the user; no additional rationale supplied.
- **Links:** [REQ-021](../product/requirements.md#req-021).
- **History:** Clarifies the ambiguous “no age range” wording in SRC-009. There was
  no previously confirmed all-ages policy to supersede.

<a id="dec-009"></a>
### DEC-009 — host eligibility limited to skill and playing role

- **Status:** Confirmed during the current decision round, 2026-11-04.
- **Source:** [SRC-010](../sources/conversation-evidence.md#src-010).
- **Decision:** Hosts may enforce skill level and playing position/role only as
  participant eligibility criteria.
- **Scope:** Additional host-selected personal eligibility criteria are excluded
  from MVP. Platform sign-in, match availability and adopted
  safety rules are separate checks, not additional host-customizable criteria.
- **Refinement:** [DEC-012](#dec-012) establishes optional role-specific places.
- **Open boundaries:** Sport-specific role catalogs, mixing role-specific and
  general places in one match, and changing rules after joining.
- **Rationale:** The user selected this bounded set; no further reason supplied.
- **Links:** [REQ-022](../product/requirements.md#req-022).
- **History:** Resolves the broad “skill or other eligibility rules” wording in
  DEC-007 without removing instant joining for users who meet the rules.

<a id="dec-010"></a>
### DEC-010 — self-declared skill separately for each sport

- **Status:** Confirmed during the current decision round, 2026-11-04.
- **Source:** [SRC-010](../sources/conversation-evidence.md#src-010).
- **Decision:** Players declare their own level separately for each sport.
- **Scope:** MVP joining uses the declared level for the match's sport. It does
  not require a verified assessment or a community-generated rating. The scale
  is resolved by [DEC-011](#dec-011); explanatory guidance, editing policy and
  missing-level flow remain Open.
- **Rationale:** The user adopted self-declaration without adding a reason.
- **Consequences — derived:** The interface should identify levels as self-declared;
  eligibility checks verify the stored declaration against the host rule, not the
  player's actual sporting ability.
- **Links:** [REQ-023](../product/requirements.md#req-023).
- **History:** Resolves the assessment source. External ratings and community
  ratings were offered alternatives but were not selected for this MVP mechanism.

<a id="dec-011"></a>
### DEC-011 — three player skill levels and a host-selected range

- **Status:** Confirmed during the current decision round, 2026-11-04.
- **Source:** [SRC-011](../sources/conversation-evidence.md#src-011).
- **Decision:** Self-declared player levels are Beginner, Intermediate, and Advanced
  for each sport. Hosts choose an allowed range or “Any level.”
- **Scope:** “Any level” removes the match's skill restriction; it is a host setting,
  not a fourth player rating. The scale is shared across sports, but each player's
  declaration remains sport-specific under DEC-010.
- **Open boundaries:** Missing declarations, editing existing declarations, effects
  on already joined matches, and explanatory guidance for each sport.
- **Rationale:** The user selected the proposed scale without adding a reason.
- **Links:** [REQ-024](../product/requirements.md#req-024).
- **History:** Resolves the skill-scale gap; numeric 1–5 and established external
  rating scales were offered alternatives but not selected for MVP.

<a id="dec-012"></a>
### DEC-012 — optional role-specific places

- **Status:** Confirmed during the current decision round, 2026-11-04.
- **Source:** [SRC-011](../sources/conversation-evidence.md#src-011).
- **Decision:** Hosts can define role-specific places. Players select an available
  role when joining. Matches may instead use general places without role allocation.
- **Scope:** Role allocation is optional, so a sport/match does not need named roles
  simply to be supported. Host participation still counts only when the host plays.
- **Open boundaries:** Role catalogs/custom roles, mixing role-specific and general
  places, changing an occupied role, and assigning a playing host's role.
- **Rationale:** The user adopted the optional role-place model without adding a reason.
- **Links:** [REQ-025](../product/requirements.md#req-025).
- **History:** Resolves optional versus compulsory role allocation and the core
  join interaction. A shared undifferentiated pool with role eligibility only was
  not selected as the model for role-specific matches.

<a id="dec-013"></a>
### DEC-013 — exclude age declaration

- **Status:** Confirmed during the current decision round, 2026-11-04.
- **Source:** [SRC-011](../sources/conversation-evidence.md#src-011).
- **Decision:** Drop age declaration completely; the MVP has no mandatory age
  declaration step, checkbox, or age declaration required before joining.
- **Scope:** This rejects the proposed 18+ self-declaration mechanism. It does not
  approve another age-check mechanism. The later [DEC-014](#dec-014) separately
  removes DEC-008's adults-only restriction; the no-declaration decision remains current.
- **Rationale:** Explicit user instruction; no additional reason supplied.
- **Links:** [REQ-021](../product/requirements.md#req-021), [REJ-004](#rej-004).
- **History:** The declaration was a proposal, never a previously confirmed requirement.

<a id="dec-014"></a>
### DEC-014 — all-ages participation

- **Status:** Confirmed during the current decision round, 2026-11-04.
- **Source:** [SRC-012](../sources/conversation-evidence.md#src-012).
- **Decision:** Remove the adults-only restriction and allow all ages to participate.
- **Supersedes:** The adults-only restriction in [DEC-008](#dec-008). Its no-age-display
  and no-age-filter decisions remain current, as does no age declaration in DEC-013.
- **Scope:** Product audience; not an assertion that every age may use every
  external provider. [DEC-017](#dec-017) confirms no age-based account branching,
  restrictions or product communication.
- **Rationale:** Explicit user change; no further rationale supplied.
- **Links:** [REQ-021](../product/requirements.md#req-021),
  [Q-002](../planning/open-questions.md#q-002).
- **Consequences — derived:** Keep provider terms separate from the app's audience;
  do not silently restore the rejected age declaration or age-specific product flows.

<a id="dec-015"></a>
### DEC-015 — one-way contact sharing per named person and match

- **Status:** Confirmed historically; **named-recipient/match-scoped grant model
  superseded by [DEC-023](#dec-023) and [DEC-024](#dec-024)**. Non-playing hosts may
  still publish their own contacts, and one owner's choice does not publish another's.
- **Source:** [SRC-012](../sources/conversation-evidence.md#src-012).
- **Decision:** A contact owner optionally shares with one named person for one
  match. Sharing is one-way, never automatically reciprocal. Non-playing hosts
  are included as eligible sharers and recipients. The owner may stop future access.
- **Scope:** Organizer status does not bypass the contact owner's consent. Sharing
  with A does not authorize B or participants in another match. The same product
  flow applies across ages under DEC-017.
- **Refinements:** DEC-018 excludes scheduled expiry. DEC-019 retains grants after
  voluntary leaving and ends access for its named invalidation events.
- **Open boundaries:** Host removal, requests versus owner-initiated sharing,
  contact-method versioning, and exact creation/read eligibility checks.
- **Rationale:** The user adopted the named one-way model without adding a reason.
- **Links:** [REQ-011](../product/requirements.md#req-011),
  [REQ-012](../product/requirements.md#req-012).
- **History:** Adopts the core audience/direction/scope of PROP-003, not all its
  proposed lifecycle and implementation details. Mutual exchange and whole-match
  sharing were offered alternatives but not selected.

<a id="dec-016"></a>
### DEC-016 — phone, email, WhatsApp, and Telegram

- **Status:** Confirmed during the current decision round, 2026-11-04.
- **Source:** [SRC-012](../sources/conversation-evidence.md#src-012).
- **Decision:** Support phone number, email, WhatsApp, and Telegram as optional
  contact methods in MVP, under the same consent model.
- **Scope:** Supporting four methods does not require a participant to provide
  all four or to open accounts with every provider. Native chat remains excluded.
- **Open boundaries:** Verification, identifiers, copy/call/email/chat actions,
  provider eligibility handling, group links and fallback behavior.
- **Rationale:** The user selected these four methods; no further reason supplied.
- **Links:** [REQ-026](../product/requirements.md#req-026),
  [provider constraints](../sources/external-references.md#provider-eligibility).
- **History:** Resolves the contact-method list. Exact provider behavior and terms
  are external constraints, not additional user product decisions.

<a id="dec-017"></a>
### DEC-017 — no age-specific restrictions, flows, or product messaging

- **Status:** Confirmed during the current decision round, 2026-11-04.
- **Source:** [SRC-013](../sources/conversation-evidence.md#src-013).
- **Decision:** The product has no age restrictions and no communication about age.
  Use the standard account/participation/contact flow without age-specific branching.
- **Scope:** No age declaration, birth-date collection, age verification, displayed
  ages, age filters, age-related onboarding text, or guardian-specific flow is
  part of this MVP specification. Close the age-design question rather than adding
  a substitute mechanism the user did not request.
- **Rationale:** The user explicitly declined further age-specific design complexity.
- **Links:** [REQ-021](../product/requirements.md#req-021),
  [Q-002](../planning/open-questions.md#q-002).
- **History:** Completes the clarification following DEC-014; retains no age
  declaration from DEC-013. Internal historical records and external-source notes
  do not become product-facing messages or claims about third-party access.

<a id="dec-018"></a>
### DEC-018 — no scheduled contact-access expiry

- **Status:** Confirmed historically. No time-based expiry is retained by the current
  owner-controlled publication model in [DEC-024](#dec-024); references to individual
  grants below describe the former design.
- **Source:** [SRC-013](../sources/conversation-evidence.md#src-013).
- **Decision:** Shared contact access has no time-based automatic expiry. The owner
  can revoke it; the explicit event invalidations in DEC-019 also apply.
- **Scope:** Neither match completion nor the passage of 24 hours ends a grant.
  This is an access-lifetime rule, not a separate decision on account deletion,
  storage retention or backup retention.
- **Rationale:** The user chose owner-controlled lifetime over the proposed timers.
- **Links:** [REQ-012](../product/requirements.md#req-012).
- **History:** “Only when the owner revokes it” answered the automatic-expiry
  question; the same reply separately approved DEC-019's event invalidations.
  Read those answers together, rather than claiming there can be no other event.

<a id="dec-019"></a>
### DEC-019 — contact access survives leaving, with specific invalidation events

- **Status:** Confirmed historically; **grant-specific invalidation model superseded
  by [DEC-023](#dec-023) and [DEC-024](#dec-024)**. Public contacts are controlled by
  their owner, not by each viewer's participation or block relationship.
- **Source:** [SRC-013](../sources/conversation-evidence.md#src-013).
- **Decision:** End future access for blocking, match cancellation, contact-value
  changes and explicit owner revocation. Keep existing access after voluntary leaving.
- **Scope:** Leaving does not revoke previously granted access or require a fresh
  grant just because the person rejoins. Recipient and originating-match scope
  remain unchanged. Cancellation affects grants for the cancelled match; contact
  changes invalidate access to the changed value rather than silently sharing its
  replacement. Blocking ends sharing between the affected people.
- **Open boundaries:** Host removal is being clarified separately; creation of
  new grants after leaving and exact unblock/regrant behavior need definition.
- **Rationale:** The user selected these event boundaries; no additional reason supplied.
- **Links:** [REQ-012](../product/requirements.md#req-012),
  [communication/privacy](../product/communication-and-privacy.md).
- **History:** Replaces the unapproved proposal that every departure should revoke
  access. No already-copied external detail is represented as recallable.

<a id="dec-020"></a>
### DEC-020 — contact access is visible before anyone joins

- **Status:** Confirmed correction during the current decision round, 2026-11-04.
- **Source:** [SRC-014](../sources/conversation-evidence.md#src-014).
- **Decision:** Contact access must always be visible, including when nobody has
  joined a match. Joining is not a prerequisite for the intended contact access.
- **Scope:** Corrects the assistant's membership-gated interpretation. The current
  owner/audience/display-control answers in DEC-023 and DEC-024 establish public,
  owner-selected methods on profiles and match pages, including anonymous viewing.
- **Revises:** DEC-015's assumed universal named-recipient access model and the
  membership assumptions behind PROP-003. DEC-018 and DEC-019 are retained as
  historical answers pending reconciliation, not mechanically applied to a new audience.
- **Rationale:** The user explicitly identified a misunderstanding from the beginning.
- **Links:** [REQ-011](../product/requirements.md#req-011),
  [Q-007](../planning/open-questions.md#q-007).
- **Boundary:** Do not interpret this correction as permission to disclose every
  user's account phone/email. Resolve owner, audience and display choice first.

<a id="dec-021"></a>
### DEC-021 — host-configurable joining and leaving cutoffs

- **Status:** Confirmed during the current decision round, 2026-11-04.
- **Source:** [SRC-014](../sources/conversation-evidence.md#src-014).
- **Decision:** The host sets a join/leave cutoff for each match.
- **Scope:** Timing is configurable per match rather than a single fixed global
  start/end rule. Separate versus shared cutoff fields, permissible bounds,
  defaults, time-zone presentation, and changing cutoffs after players join remain Open.
- **Rationale:** The user selected host control rather than the proposed fixed timing.
- **Links:** [REQ-027](../product/requirements.md#req-027).
- **History:** Neither the fixed start/end cutoff nor the suggested no-penalty
  policy was adopted by this answer. Penalties remain a separate question.

<a id="dec-022"></a>
### DEC-022 — host editing, cancellation and reasoned player removal

- **Status:** Confirmed during the current decision round, 2026-11-04.
- **Source:** [SRC-014](../sources/conversation-evidence.md#src-014).
- **Decision:** The host can edit match details, cancel a match, and remove a player
  with a recorded reason. Host transfer is excluded from MVP.
- **Scope:** Recording a reason is required for removal. Whether it is shown to
  the removed player or others, allowed edit windows, notifications and appeal
  handling remain Open. No new contact-access effect is inferred from removal.
- **Rationale:** The user adopted these controls without adding a reason.
- **Links:** [REQ-028](../product/requirements.md#req-028), [REJ-005](#rej-005).
- **History:** Adopts the relevant host powers in PROP-002; the alternative with
  host transfer was offered but not selected.

<a id="dec-023"></a>
### DEC-023 — public contacts on profiles and match pages

- **Status:** Confirmed during the current decision round, 2026-11-04.
- **Source:** [SRC-015](../sources/conversation-evidence.md#src-015).
- **Decision:** Users' displayed contacts are visible on their profiles and match
  pages to anyone viewing the page, including visitors without an account.
- **Scope:** No sign-in, joining, playing-place occupancy, or individual recipient
  grant is required to view an owner-selected public method. Match pages can expose
  the host's public contacts before anyone joins. Participant/roster layout is a
  separate UI decision; a contact shown on a page has this public audience.
- **Supersedes:** The named-person/per-match authorization model in DEC-015 and
  the grant-specific access transitions of DEC-019. Resolves DEC-020's correction.
- **Rationale:** The user explicitly clarified profile/match surfaces and anonymous viewing.
- **Links:** [REQ-011](../product/requirements.md#req-011),
  [communication/privacy](../product/communication-and-privacy.md).
- **Consequences — derived:** Blocking or removing one signed-in person cannot be
  represented as making a contact unavailable to them through an anonymous public
  page. This model has public visibility controls rather than private recipient grants.

<a id="dec-024"></a>
### DEC-024 — explicit owner choice of publicly displayed methods

- **Status:** Confirmed during the current decision round, 2026-11-04.
- **Source:** [SRC-015](../sources/conversation-evidence.md#src-015).
- **Decision:** The owner explicitly chooses which contact methods to display and
  may hide or change them later. The audience is public under DEC-023.
- **Scope:** Consent applies to publication of the selected method, not to each
  viewer. Unselected contact fields and authentication identifiers are not published
  automatically. Contact methods remain optional; adding one is not the same as
  choosing to display it.
- **Lifetime:** The absence of scheduled expiry from DEC-018 is retained. A published method
  stays public until its owner changes/hides/removes it or the account/data itself
  becomes unavailable under a separately defined account lifecycle.
- **Consequences — derived:** Joining, leaving, removal, match completion and match
  cancellation do not themselves change a profile method's public setting. Editing
  a displayed value updates that selected public method; it does not require a
  recipient-by-recipient regrant. Already copied values cannot be recalled.
- **Rationale:** The user selected explicit owner control over automatic display.
- **Links:** [REQ-004](../product/requirements.md#req-004),
  [REQ-012](../product/requirements.md#req-012), [REQ-026](../product/requirements.md#req-026).
- **History:** Reconciles optional consent with public pre-join visibility. Earlier
  grant details remain in the [historical snapshot](history/contact-grants-before-correction.md).

<a id="dec-025"></a>
### DEC-025 — one shared join/leave deadline

- **Status:** Partially superseded by DEC-032, 2026-11-04. The deadline no longer limits leaving.
- **Source:** [SRC-016](../sources/conversation-evidence.md#src-016).
- **Decision:** The host sets one shared deadline for joining and leaving, no later
  than the match start. This refines DEC-021; independent join and leave deadlines
  are not part of this model.
- **Open details:** How a time/location edit resets deadlines, and the precise
  boundary instant, remain to be specified. No penalty scheme is implied.
- **Rationale:** Explicit user selection; no further rationale supplied.
- **Links:** [REQ-027](../product/requirements.md#req-027).

<a id="dec-026"></a>
### DEC-026 — reconfirm after time or location changes

- **Status:** Confirmed, 2026-11-04.
- **Source:** [SRC-016](../sources/conversation-evidence.md#src-016).
- **Decision:** When the host changes the match's time or location after players
  have joined, everyone must reconfirm participation in the changed match.
- **Scope:** Existing players, including a playing host. The host's edit is not
  assumed to reconfirm their playing participation. Non-playing hosts have no
  playing participation to reconfirm. These are derived applications of the rule.
- **Open details:** Pending-place reservation, deadline, nonresponse handling,
  notification channel, and editing window. Cosmetic corrections have not been
  distinguished from location/time changes by the owner.
- **Rationale:** Explicit user selection; no further rationale supplied.
- **Links:** [REQ-029](../product/requirements.md#req-029).

<a id="dec-027"></a>
### DEC-027 — allow overlapping participation without checks

- **Status:** Confirmed, 2026-11-04.
- **Source:** [SRC-016](../sources/conversation-evidence.md#src-016).
- **Decision:** A person may join matches whose scheduled playing times overlap.
  Do not check for overlaps or show overlap warnings.
- **Consequences — derived:** Admission and reconfirmation do not query other
  match bookings to prevent schedule conflicts. No automatic withdrawal or
  conflict-based penalty follows from overlapping times.
- **Rationale:** Explicit user selection; no further rationale supplied.
- **Links:** [REQ-030](../product/requirements.md#req-030).

<a id="dec-028"></a>
### DEC-028 — reconfirmation does not reserve a place

- **Status:** Confirmed, 2026-11-04.
- **Source:** [SRC-017](../sources/conversation-evidence.md#src-017).
- **Decision:** Immediately free existing players' places when a time/location
  edit requires reconfirmation. Reconfirmation competes with new joins.
- **Consequences — derived:** Pending reconfirmation uses zero playing capacity.
  A player can lose the chance to return if other people fill the match or their
  required role. Prior participation is not a reservation or priority entitlement.
- **Rationale:** Explicit choice over keeping places reserved; no further reason supplied.
- **Links:** [REQ-029](../product/requirements.md#req-029).

<a id="dec-029"></a>
### DEC-029 — reset the shared deadline after material edits

- **Status:** Confirmed with leaving removed from the deadline by DEC-032, 2026-11-04.
- **Source:** [SRC-017](../sources/conversation-evidence.md#src-017).
- **Decision:** After a time/location change, the host sets one new shared deadline
  for joining, leaving, and reconfirming. It must be in the future and no later
  than the revised match start.
- **Consequences — derived:** A material edit with no valid future deadline cannot
  be committed as a normal reschedule. Editing the location while retaining a
  past start does not satisfy the rule. Separate reconfirmation cutoffs are excluded.
- **Rationale:** User selected a single shared deadline.
- **Links:** [REQ-027](../product/requirements.md#req-027), [REQ-029](../product/requirements.md#req-029).

<a id="dec-030"></a>
### DEC-030 — close unanswered reconfirmations automatically

- **Status:** Confirmed, 2026-11-04.
- **Source:** [SRC-017](../sources/conversation-evidence.md#src-017).
- **Decision:** Automatically remove players who have not reconfirmed by the new deadline.
- **Consequences — derived:** Their places were already released under DEC-028.
  Expiry closes the pending record and must not decrement occupancy again or remove
  a different player's allocation. A successful reconfirmation is not expired by
  an older pending request. No separate penalty is implied.
- **Rationale:** Explicit choice over indefinite pending status.
- **Links:** [REQ-029](../product/requirements.md#req-029).

<a id="dec-031"></a>
### DEC-031 — service notifications in the app only

- **Status:** Confirmed, 2026-11-04.
- **Source:** [SRC-018](../sources/conversation-evidence.md#src-018).
- **Decision:** Match changes, cancellations, removals and reconfirmation requests
  appear in an in-app notification list only. No email or browser push channel for
  these service events in MVP. Participant conversation remains external.
- **Consequences — derived:** A person who does not revisit the app may miss a
  change or reconfirmation deadline. Notification creation does not prove it was read.
  Authentication/recovery email, if later selected, is a separate purpose.
- **Rationale:** User selected the in-app-only option.
- **Links:** [REQ-031](../product/requirements.md#req-031).

<a id="dec-032"></a>
### DEC-032 — players may leave at any time

- **Status:** Confirmed, 2026-11-04.
- **Source:** [SRC-018](../sources/conversation-evidence.md#src-018).
- **Decision:** Let players leave at any time. The host-set deadline prevents
  joining and reconfirming only, not leaving.
- **Supersedes:** The leave-cutoff component of DEC-021/025/029. The single deadline
  and start-time bounds remain for joining/reconfirming; material edits still reset it.
- **Consequences — derived:** A late departure can free a place that cannot be filled
  after admission closes. Do not extend the deadline automatically or add an
  automatic penalty. Historical completed-match record treatment remains to be defined.
- **Rationale:** User expressly chose unrestricted withdrawal.
- **Links:** [REQ-009](../product/requirements.md#req-009), [REQ-027](../product/requirements.md#req-027).

<a id="dec-033"></a>
### DEC-033 — host edits must preserve existing players' fit

- **Status:** Confirmed, 2026-11-04.
- **Source:** [SRC-018](../sources/conversation-evidence.md#src-018).
- **Decision:** Changes to capacity, role places, or the allowed skill range are
  permitted only if all current players still fit. Otherwise the host must first
  remove affected players using the recorded-reason removal flow.
- **Consequences — derived:** No silent eviction, role reassignment, or overcapacity
  caused by editing. Time/location edits continue to use the distinct release and
  reconfirmation rule. Pending reconfirmations hold no place; they must meet current
  admission conditions when attempting to return.
- **Rationale:** Explicit choice over reconfirmation for these edits.
- **Links:** [REQ-010](../product/requirements.md#req-010), [REQ-028](../product/requirements.md#req-028).

<a id="dec-034"></a>
### DEC-034 — optional skill for unrestricted matches and unrestricted skill editing

- **Status:** Confirmed, 2026-11-04.
- **Source:** [SRC-019](../sources/conversation-evidence.md#src-019).
- **Decision:** Require a sport-specific skill declaration only for skill-restricted
  matches. Players may edit skill anytime without removal from existing participation.
- **Consequences — derived:** Any-level admission accepts a missing declaration.
  New joins/reconfirmations use the current declaration. A skill change does not
  reserve eligibility for later readmission. Host rule edits still obey DEC-033.
- **Rationale:** Explicit user selection; no additional rationale supplied.
- **Links:** [REQ-023](../product/requirements.md#req-023), [REQ-024](../product/requirements.md#req-024).

<a id="dec-035"></a>
### DEC-035 — searchable and custom sports, custom roles, mixed places

- **Status:** Confirmed, 2026-11-04.
- **Source:** [SRC-019](../sources/conversation-evidence.md#src-019).
- **Decision:** Provide a searchable sport list plus custom sport entries; hosts
  define role names; a match may combine general and role-specific places.
- **Consequences — derived:** Treat general and named-role capacities as separate
  selectable pools. Their sum determines total playing capacity. A playing
  allocation uses exactly one pool. Catalog normalization and duplicate sport
  handling are implementation choices, not a reason to prohibit custom sports.
- **Rationale:** User chose flexible input over fixed sport/role catalogs.
- **Links:** [REQ-019](../product/requirements.md#req-019), [REQ-025](../product/requirements.md#req-025).

<a id="dec-036"></a>
### DEC-036 — removal excludes rejoining until the host lifts it

- **Status:** Confirmed, 2026-11-04.
- **Source:** [SRC-019](../sources/conversation-evidence.md#src-019).
- **Decision:** Host removal prevents rejoining that same match unless the host
  explicitly allows the person to rejoin.
- **Consequences — derived:** Removal is a match-specific admission exclusion,
  including reconfirmation. Lifting it does not allocate a place or bypass current
  deadlines, capacity, sign-in or skill/role rules. It is not an account-wide ban.
- **Rationale:** User selected this over immediate eligible rejoining.
- **Links:** [REQ-028](../product/requirements.md#req-028).

<a id="dec-037"></a>
### DEC-037 — email/password accounts

- **Status:** Confirmed, 2026-11-04.
- **Source:** [SRC-020](../sources/conversation-evidence.md#src-020).
- **Decision:** Use email and password. Hosting, joining and editing profiles
  require an account; browsing remains public.
- **Open details:** Email verification and password recovery mechanics. Login
  email is private unless separately chosen as a public contact.
- **Rationale:** User selected email/password over email-link and social options.
- **Links:** [REQ-005](../product/requirements.md#req-005).

<a id="dec-038"></a>
### DEC-038 — public names, skill, roles and match history; no avatars

- **Status:** Partially superseded by DEC-044: past-match lists removed; other fields retained.
- **Source:** [SRC-020](../sources/conversation-evidence.md#src-020).
- **Decision:** Public display name, skill, playing role, and past/upcoming matches.
  Do not include avatars. Owner-selected contact fields remain independently controlled.
- **Consequences — derived:** Public profiles include participation history and
  upcoming matches; match rosters show relevant names, sport-specific skills and
  selected roles. No global role is inferred for every sport. Missing optional skill
  is shown as undeclared, not invented. Exact history treatment of cancelled,
  withdrawn, removed and unconfirmed participation still needs definition.
- **Rationale:** Explicit user-selected field set.
- **Links:** [REQ-005](../product/requirements.md#req-005), [REQ-006](../product/requirements.md#req-006).

<a id="dec-039"></a>
### DEC-039 — map distance and filtered discovery

- **Status:** Confirmed, 2026-11-04.
- **Source:** [SRC-020](../sources/conversation-evidence.md#src-020).
- **Decision:** Include distance in a map, city, sport, date, skill range and
  available-place discovery controls, with results sorted by soonest start.
- **Open details:** Distance origin, map provider, geolocation fallback, exact
  distance filtering/presentation and default dates. No ranking algorithm or
  overlap-based exclusion is inferred.
- **Rationale:** Explicit user-selected discovery controls.
- **Links:** [REQ-006](../product/requirements.md#req-006).

<a id="dec-040"></a>
### DEC-040 — public exact match locations

- **Status:** Confirmed, 2026-11-04.
- **Source:** [SRC-021](../sources/conversation-evidence.md#src-021).
- **Decision:** Host chooses a map pin plus venue/address text and city. Exact
  location is public before joining.
- **Consequences — derived:** Location is not a membership-gated secret. Changes
  to the match pin/address/venue location use the material-edit reconfirmation rule.
  Geocoding provider and mismatch validation remain engineering choices.
- **Rationale:** Explicit choice over hiding precise location until joining.
- **Links:** [REQ-006](../product/requirements.md#req-006), [REQ-007](../product/requirements.md#req-007).

<a id="dec-041"></a>
### DEC-041 — English/Spanish and match-local time

- **Status:** Confirmed, 2026-11-04.
- **Source:** [SRC-021](../sources/conversation-evidence.md#src-021).
- **Decision:** English and Spanish UI; display each match's local time with its
  time zone rather than converting the primary display to viewer-local time.
- **Consequences — derived:** Model the venue's time zone, including differences
  within Spain/UK and seasonal offsets; do not use a single hard-coded offset per
  country. User-entered sport/role/venue text is not automatically translated.
- **Rationale:** Explicit language and time-display choice.
- **Links:** [REQ-032](../product/requirements.md#req-032).

<a id="dec-042"></a>
### DEC-042 — free public-only MVP and explicit deferrals

- **Status:** Confirmed, 2026-11-04.
- **Source:** [SRC-021](../sources/conversation-evidence.md#src-021).
- **Decision:** MVP is free to use and supports public matches only. Defer private
  games, waitlists, recurring games, ratings, payments and venue booking.
- **Consequences — derived:** No MVP checkout, reservation/payment integration,
  waitlist auto-promotion, repeat-event generator, private admission or reputation
  score. Self-declared skill remains supported and is distinct from ratings.
- **Rationale:** User adopted the stated small first-release boundary.
- **Links:** [REQ-033](../product/requirements.md#req-033), [MVP](../product/mvp.md).
- **History:** These features were previously suggested deferrals; they are now
  confirmed exclusions for MVP, not permanent rejections or future commitments.

<a id="dec-043"></a>
### DEC-043 — start/end schedule, edit lock and automatic completion

- **Status:** Confirmed, 2026-11-04.
- **Source:** [SRC-022](../sources/conversation-evidence.md#src-022).
- **Decision:** Require start and end times; lock time/location edits once started; mark completed automatically at end.
- **Consequences — derived:** End follows start. Cancelled matches do not become completed through the normal end timer. Other host powers are separate.
- **Rationale:** Explicit user selection; no additional rationale supplied.
- **Links:** [REQ-007](../product/requirements.md#req-007), [REQ-034](../product/requirements.md#req-034).

<a id="dec-044"></a>
### DEC-044 — upcoming matches only; no public past-match lists

- **Status:** Confirmed, 2026-11-04.
- **Source:** [SRC-022](../sources/conversation-evidence.md#src-022).
- **Decision:** Drop past matches; show upcoming matches only. This supersedes the past-history part of DEC-038; its other public fields and no-avatar choice remain.
- **Consequences — derived:** Upcoming profile lists contain current active future participation, not withdrawn, removed, pending or cancelled records. No public past-participation feature is included. Stored-data retention is separate.
- **Rationale:** Explicit user selection; no additional rationale supplied.
- **Links:** [REQ-005](../product/requirements.md#req-005), [REQ-006](../product/requirements.md#req-006).

<a id="dec-045"></a>
### DEC-045 — no email verification; email reset and contact format checks

- **Status:** Confirmed, 2026-11-04.
- **Source:** [SRC-022](../sources/conversation-evidence.md#src-022).
- **Decision:** No email verification step. Provide email password reset. Public contact methods receive format validation only, without ownership verification.
- **Consequences — derived:** Do not add verified-owner badges or provider login requirements. Reset email is an authentication message, distinct from excluded match service emails. Authentication email stays private unless independently published.
- **Rationale:** Explicit user selection; no additional rationale supplied.
- **Links:** [REQ-005](../product/requirements.md#req-005), [REQ-013](../product/requirements.md#req-013), [REQ-026](../product/requirements.md#req-026).

<a id="dec-046"></a>
### DEC-046 — optional device location and manual distance origin

- **Status:** Confirmed, 2026-11-04.
- **Source:** [SRC-023](../sources/conversation-evidence.md#src-023).
- **Decision:** Use optional device location for map distance; otherwise use a city or map point chosen by the visitor.
- **Consequences — derived:** Denial or unavailability of geolocation must not prevent discovery. Do not treat browsing origin as the match venue or a permanent public profile location.
- **Rationale:** Explicit user selection; no additional rationale supplied.
- **Links:** [REQ-006](../product/requirements.md#req-006).

<a id="dec-047"></a>
### DEC-047 — external support without in-app reporting or moderation tools

- **Status:** Confirmed, 2026-11-04.
- **Source:** [SRC-023](../sources/conversation-evidence.md#src-023).
- **Decision:** No in-app reports or moderation tools; handle support externally.
- **Consequences — derived:** No personal blocking/report queue/admin moderation UI is adopted. Host removal, server authorization and owner data controls remain. This replaces the proposed reporting/blocking scope in PROP-005/REQ-015, not the confirmed host controls.
- **Rationale:** Explicit user selection; no additional rationale supplied.
- **Links:** [REQ-015](../product/requirements.md#req-015).

<a id="dec-048"></a>
### DEC-048 — immediate account-deletion effects

- **Status:** Confirmed, 2026-11-04.
- **Source:** [SRC-023](../sources/conversation-evidence.md#src-023).
- **Decision:** On account deletion, immediately hide profile/contacts, withdraw from upcoming matches, and cancel upcoming hosted matches.
- **Consequences — derived:** No host transfer or hostless upcoming event is created. Retention/purge timing and already-started matches remain separate choices.
- **Rationale:** Explicit user selection; no additional rationale supplied.
- **Links:** [REQ-018](../product/requirements.md#req-018), [REQ-035](../product/requirements.md#req-035).

<a id="dec-049"></a>
### DEC-049 — global locations allowed beyond the pilot focus

- **Status:** Confirmed, 2026-11-04.
- **Source:** [SRC-024](../sources/conversation-evidence.md#src-024).
- **Decision:** Spain and the UK are the focus, but hosts may create matches in other countries.
- **Consequences — derived:** Do not enforce a Spain/UK-only creation allowlist. The pilot footprint is focus and coverage, not exclusion of other places.
- **Rationale:** Explicit user selection; no additional rationale supplied.
- **Links:** [REQ-019](../product/requirements.md#req-019).

<a id="dec-050"></a>
### DEC-050 — terminal match pages contain state only

- **Status:** Confirmed, 2026-11-04.
- **Source:** [SRC-024](../sources/conversation-evidence.md#src-024).
- **Decision:** Completed/cancelled matches are absent from discovery and profile lists. Direct links show only “Match ended” or “Match cancelled”, hiding roster and match details.
- **Consequences — derived:** Do not leak old details, roster or contacts in the terminal page's public response. A person's profile contacts remain public if still selected; this is a surface change, not recipient revocation.
- **Rationale:** Explicit user selection; no additional rationale supplied.
- **Links:** [REQ-006](../product/requirements.md#req-006), [REQ-034](../product/requirements.md#req-034).

<a id="dec-051"></a>
### DEC-051 — support through repository GitHub Issues

- **Status:** Confirmed, 2026-11-04.
- **Source:** [SRC-024](../sources/conversation-evidence.md#src-024).
- **Decision:** Link external support to https://github.com/mohamadrezakoohkan/open-sports/issues.
- **Consequences — derived:** Opening the support destination does not automatically file an issue, attach account/contact data, or provide an in-app moderation flow.
- **Rationale:** Explicit user selection; no additional rationale supplied.
- **Links:** [REQ-015](../product/requirements.md#req-015).

<a id="dec-052"></a>
### DEC-052 — account deletion applies to all unfinished matches

- **Status:** Confirmed, 2026-11-04.
- **Source:** [SRC-025](../sources/conversation-evidence.md#src-025).
- **Decision:** Deletion withdraws the person from every unfinished match and cancels every unfinished match they host, including ongoing matches. Refines DEC-048.
- **Consequences — derived:** No unfinished hosted match remains published without its host; cancellation notifications go to affected accounts. Finished records follow retention policy.
- **Rationale:** Explicit user selection; no additional rationale supplied.
- **Links:** [REQ-035](../product/requirements.md#req-035).

<a id="dec-053"></a>
### DEC-053 — removal reasons visible only to host and removed player

- **Status:** Confirmed, 2026-11-04.
- **Source:** [SRC-025](../sources/conversation-evidence.md#src-025).
- **Decision:** Only the host and the removed player may see a recorded host-removal reason.
- **Consequences — derived:** Do not expose reasons on public rosters/profiles, in anonymous payloads, or to other participants. No in-app operator/moderation privilege is introduced.
- **Rationale:** Explicit user selection; no additional rationale supplied.
- **Links:** [REQ-028](../product/requirements.md#req-028).

<a id="dec-054"></a>
### DEC-054 — immediate account-data deletion and 30-day retention

- **Status:** Confirmed, 2026-11-04.
- **Source:** [SRC-025](../sources/conversation-evidence.md#src-025).
- **Decision:** Delete account personal data immediately. Delete completed/cancelled match records and notifications after 30 days. Backups expire within 30 days.
- **Consequences — derived:** Derived clock anchors: match retention starts at completion/cancellation; notice retention at creation. Delete or anonymize personal account references immediately in retained service records. Backup restores must reapply deletions before serving data. Minimal nonpersonal terminal markers are a separate implementation detail; they must not retain deleted match details.
- **Rationale:** Explicit user selection; no additional rationale supplied.
- **Links:** [REQ-018](../product/requirements.md#req-018), [REQ-035](../product/requirements.md#req-035).

<a id="dec-055"></a>
### DEC-055 — technology-neutral architecture for now

- **Status:** Confirmed intentional deferral, 2026-11-04.
- **Source:** [SRC-026](../sources/conversation-evidence.md#src-026).
- **Decision:** Keep architecture technology-neutral for now.
- **Consequences — derived:** Describe logical components, authorization, transactions,
  revisions and scheduled work without selecting Next.js, Supabase or a hosting vendor.
  Stack/provider/resource choices belong to later implementation decisions.
- **Rationale:** User chose neutrality rather than either offered stack.
- **Links:** [technical overview](../architecture/technical-overview.md), [REQ-001](../product/requirements.md#req-001).

<a id="dec-056"></a>
### DEC-056 — AGPL-3.0-only for code and documentation

- **Status:** Confirmed, 2026-11-04.
- **Source:** [SRC-026](../sources/conversation-evidence.md#src-026).
- **Decision:** License repository code and documentation under AGPL-3.0-only.
- **Consequences — derived:** Include the license text and explicit only-version
  identifier. Preserve third-party license notices; do not relabel independent
  dependencies or third-party material as solely owned by this project.
- **Rationale:** User selected the option described as keeping modified networked versions open.
- **Links:** [license status](../../LICENSE-STATUS.md), [REQ-001](../product/requirements.md#req-001).

<a id="dec-057"></a>
### DEC-057 — installable PWA; offline screen instead of offline match data

- **Status:** Confirmed, 2026-11-04.
- **Source:** [SRC-026](../sources/conversation-evidence.md#src-026).
- **Decision:** Support installation. Show an offline screen when disconnected;
  require a connection for match data and all actions.
- **Consequences — derived:** No offline match browsing, queued participation writes
  or cached contact-bearing pages. A static application shell/offline message can
  be cached without retaining match or personal data. Reconcile uncertain writes
  after reconnecting rather than assuming success.
- **Rationale:** User selected online-only data over cached browsing.
- **Links:** [REQ-001](../product/requirements.md#req-001), [REQ-016](../product/requirements.md#req-016).

<a id="dec-058"></a>
### DEC-058 — playing-host eligibility and capacity-safe role switching

- **Status:** Confirmed, 2026-11-04.
- **Source:** [SRC-027](../sources/conversation-evidence.md#src-027).
- **Decision:** A playing host follows the same skill/role rules as other players.
  Players may switch to an available role before admission deadline while preserving capacity.
- **Consequences — derived:** Switch atomically without losing the old place on failure.
  After deadline, reject role switching while still allowing withdrawal. A host who
  cannot meet playing eligibility can organize without playing.
- **Rationale:** Explicit user selection.
- **Links:** [REQ-020](../product/requirements.md#req-020), [REQ-025](../product/requirements.md#req-025), [REQ-036](../product/requirements.md#req-036).

<a id="dec-059"></a>
### DEC-059 — browser and accessibility baseline

- **Status:** Confirmed, 2026-11-04.
- **Source:** [SRC-027](../sources/conversation-evidence.md#src-027).
- **Decision:** Support the latest two stable versions of Chrome, Safari, Firefox
  and Edge, responsive mobile/desktop, targeting WCAG 2.2 AA.
- **Consequences — derived:** Record actual tested versions at each release rather
  than pinning today's versions in product policy. Installation UI may differ by
  platform; browsing/core flows must remain usable within the support matrix.
- **Rationale:** Explicit user selection.
- **Links:** [REQ-001](../product/requirements.md#req-001), [REQ-017](../product/requirements.md#req-017).

<a id="dec-060"></a>
### DEC-060 — choose and document remaining small defaults; finish

- **Status:** Confirmed delegation, 2026-11-04.
- **Source:** [SRC-027](../sources/conversation-evidence.md#src-027).
- **Decision:** Choose coherent small interaction/engineering defaults within
  confirmed decisions, label them Derived recommendations, and finish the documentation.
- **Scope:** This permits concrete defaults without attributing each to an explicit
  user selection. It does not override confirmed exclusions, select a vendor after
  DEC-055, deploy a product, invent lost conversation text or initialize/push a default branch.
- **Rationale:** User selected completion with documented defaults over more questions.
- **Links:** [derived defaults](derived-defaults.md), [requirements](../product/requirements.md).

## Proposal register

These proposals originated during reconstruction, not unavailable assistant replies.
Their final dispositions below preserve the distinction between a user decision
and a selected derived mechanism.

<a id="prop-001"></a>
### PROP-001 — minimal discover, host, and join loop

**Status:** Core scope adopted by the current decisions, including DEC-037–042;
small interactions selected under DEC-060. The initial browse/authenticate/publish/
join/leave/cancel proposal is implemented in the [MVP specification](../product/mvp.md),
with explicit fields and acceptance criteria. It is no longer an unresolved release boundary.

<a id="prop-002"></a>
### PROP-002 — bounded membership and host controls

**Status:** Host powers/occupancy/cutoffs adopted by DEC-006/022/025–033/036/053/058.
One allocation per person, atomic capacity, one organizer and revision-safe retry
handling are **selected derived defaults** under DEC-060. See [domain model](../architecture/domain-model.md).

<a id="prop-003"></a>
### PROP-003 — directional, match-scoped contact grants

**Status:** Superseded historical proposal after DEC-023/024. DEC-015 previously
selected named recipients, one-match scope and owner revocation; DEC-018/019
refined lifetime. The user's correction replaced this model with optional public
publication. Preserve the [historical snapshot](history/contact-grants-before-correction.md);
do not implement its grants or invalidation rules.

<a id="prop-004"></a>
### PROP-004 — server-authoritative modular application

**Status:** Selected derived architecture under DEC-060, deliberately technology-neutral
under DEC-055. Logical modules, authoritative transactions, public/private projections,
durable jobs and external handoff are specified without vendor selection.
See [architecture](../architecture/technical-overview.md).

<a id="prop-005"></a>
### PROP-005 — launch quality and abuse safeguards

**Status:** Split disposition. Browser/accessibility and online-only behavior are
adopted in DEC-057/059. Safe logs, retry/recovery and deletion checks are selected
derived defaults. The earlier block/report/moderation proposal is **Rejected for MVP**
by DEC-047; support is external through GitHub Issues under DEC-051.
See [quality/security](../architecture/security-and-nonfunctional.md).

## Rejected or ruled-out options

**Evidence distinction:** No explicit rejection explanation was recovered from the
original conversation. REJ-001–003 are **Rejected for the stated scope because they
conflict with a confirmed selection**; this does not assert that they were all
debated previously. REJ-004 and REJ-005 record explicit exclusions in the current chat.

<a id="rej-001"></a>
### REJ-001 — host approval as the normal public-join gate

**Status:** Rejected for public matches by DEC-002. Scope does not include private
matches, safety enforcement, or eligibility checks. A required host approval would
change instant joining into a pending request. No other historical rationale is known.

<a id="rej-002"></a>
### REJ-002 — native participant chat in the MVP

**Status:** Rejected for MVP by DEC-003. Reconsideration after MVP requires a new
decision; this is not a permanent prohibition. The comparative cost discussion, if
one occurred, is unavailable.

<a id="rej-003"></a>
### REJ-003 — compulsory or automatic participant contact disclosure

**Status:** Rejected by DEC-004. Joining, hosting, or opening a match cannot by itself
authorize sharing someone's contact details. DEC-024 defines consent as the owner's
explicit choice to publish individual methods to everyone viewing the page.

<a id="rej-004"></a>
### REJ-004 — mandatory age declaration

**Status:** Rejected explicitly in [SRC-011](../sources/conversation-evidence.md#src-011).
The user said “drop age declaration completely.” Remove that proposed onboarding
step; do not replace it silently with birth-date collection or external verification.
DEC-014 subsequently removes the adults-only restriction while preserving this rejection.

<a id="rej-005"></a>
### REJ-005 — host transfer in MVP

**Status:** Rejected for MVP by the explicit choice in
[DEC-022](#dec-022). The user selected host management without transfer after an
alternative including accepted transfer was offered. No additional rationale was
supplied. Reconsideration after MVP requires a new decision.

## Evolution and conflicts

Available order: join design topics → public instant join → external MVP chat →
optional contact sharing → documentation request → current PWA task → repository URL.
The current decision round then established sport/geographic scope, host occupancy,
and signed-in eligibility gates. These additions are contemporary decisions, not
newly recovered parts of the original conversation.
The next clarification established adults-only participation, no displayed age or
age filters, skill/role-only host eligibility, and self-declared skill per sport.
The following round selected the three-level skill scale and optional role-specific
places, and explicitly rejected age declaration. The relationship between the
remaining adults-only policy and the removal of checks was then resolved by DEC-014:
the policy restriction is superseded and all ages are included. DEC-015 and DEC-016
adopted named one-way sharing, non-playing host inclusion, and four contact methods.
The age-policy change is preserved as an explicit supersession, not an unresolved
contradiction. DEC-017 then closed age-specific flows and messaging. DEC-018 and
DEC-019 removed proposed contact timers and departure revocation while retaining
specific event invalidations. DEC-020 subsequently identified a foundational contact
misunderstanding: access must be visible even before anyone joins. The owner/audience
was resolved by DEC-023 and DEC-024: owner-selected public methods visible to
anonymous viewers on profiles and match pages. DEC-021 and DEC-022 confirmed
host-defined cutoffs and host controls without transfer. The potential tension
between optional contacts and coordination is accepted: a match may have no public
contact methods; see [Q-007](../planning/open-questions.md#q-007). Missing earlier decisions may introduce
conflicts; do not claim the complete history is consistent.

The recovered original decisions have no known superseded predecessors. The current
chat includes the age-policy supersession DEC-008 → DEC-014 and contact-model
supersession DEC-015/019 → DEC-023/024. DEC-025 defines one shared cutoff,
DEC-026 requires reconfirmation after time/location edits, and DEC-027 allows
unchecked overlapping participation. Future changes
should use the [template](template.md) and retain dated supersession links.

Later rounds replaced the leave restriction with unrestricted withdrawal, adopted
competitive reconfirmation and in-app-only notices, then resolved skill/catalog/
removal rules. Public past-match lists selected in DEC-038 were removed by DEC-044.
Email/password without verification, public exact locations, language/time display,
free public-only scope, global location allowance, external support, terminal-page
privacy and deletion/retention were resolved in DEC-037–054. The owner then chose
technology neutrality, AGPL-3.0-only, an online-only installable PWA, host/role rules,
a browser/accessibility baseline, and delegated small defaults (DEC-055–060).
No further product answers are required to complete this documentation baseline.
