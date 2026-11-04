# Historical snapshot: earlier contact-grant model

Captured 2026-11-04 immediately before applying the contact-visibility correction
in [DEC-020](../decision-log.md#dec-020).

**Historical design only.** The labels and detailed rules below describe the
pre-correction interpretation. They are preserved for decision history, not as the
current implementation contract. The user clarified that contact access must be
visible before anyone joins. Use the [current communication specification](../../product/communication-and-privacy.md)
and current decision log; do not reintroduce membership or named-grant gates from
this snapshot as universal prerequisites.

## Confirmed constraints

- MVP chat is external: [DEC-003](../decision-log.md#dec-003).
- Contact sharing is optional, participant-to-participant, and requires consent:
  [DEC-004](../decision-log.md#dec-004).
- Sharing is one-way with one named person for one match, includes non-playing
  hosts, and permits owner revocation of future access:
  [DEC-015](../decision-log.md#dec-015).
- Supported methods are phone, email, WhatsApp, and Telegram:
  [DEC-016](../decision-log.md#dec-016).
- Grants have no scheduled expiry and survive voluntary leaving. Blocking,
  cancellation, contact changes and owner revocation end future access:
  [DEC-018–019](../decision-log.md#dec-018).
- The same product flow applies across ages, with no age-related restrictions or
  messaging: [DEC-017](../decision-log.md#dec-017).

The model was drafted as **Proposal PROP-003** during reconstruction. The current
user has adopted the core scope/direction and method list above. The remaining
mechanics are proposals unless individually marked Confirmed. None is attributed
to an unavailable assistant reply.

## Communication model — confirmed core with proposed mechanics

Match facts and participation remain visible in the PWA. A player may separately
share a chosen contact method with a named participant or organizer for that match.
Refusing to share does not undo membership. The app does not require
every player to join a group or prove that an external conversation occurred.

There is no native conversation stream. Consent controls and system-generated
membership/status messages are not peer chat. Whether the MVP has contact requests,
push/email notifications, group invite links, or only owner-initiated sharing is
[Q-007](../../planning/open-questions.md#q-007) and [Q-008](../../planning/open-questions.md#q-008).

## Consent contract

| Rule | Behavior | Status and unresolved boundary |
|---|---|---|
| Default | No contact sharing through joining alone | Confirmed, DEC-004 |
| Actor | Contact owner chooses to share | Confirmed, DEC-015 |
| Recipient | One named person in the same match; non-playing host included | Confirmed, DEC-015; exact grant-creation predicate proposed |
| Direction | A → B is independent of B → A | Confirmed, DEC-015 |
| Scope | One match and one recipient | Confirmed, DEC-015; contact-version binding proposed |
| Information | Show recipient, method/value, match, lifetime conditions and external-control limits | Proposal for informed consent UI |
| Confirmation | Separate deliberate action; no preselected consent | Proposal implementing the confirmed voluntary choice |
| Repetition | Retrying the same grant does not create duplicate authorization | Proposal |
| New recipient | Requires their own authorization | Derived verification of confirmed named-recipient scope |
| Contact edit | Old-value grants end; replacement value needs its own consent | Confirmed event boundary, DEC-019; versioning proposed |
| Revocation | Owner can stop future in-app access | Confirmed, DEC-015; transaction/cache mechanics proposed |
| Expiry | No scheduled expiry, including after match completion | Confirmed, DEC-018 |
| Voluntary departure | Preserve existing grants | Confirmed, DEC-019; new-grant creation after leaving still Open |

Account login email/phone is not automatically a contact method. Selecting a method
for sharing and verifying an account serve different purposes. Verification of
ownership of each contact method is [Q-009](../../planning/open-questions.md#q-009).

## Proposed permission matrix

“Contact read” includes retrieving a raw value, rendering it, generating a deep
link containing it, copying it, or exporting it. Hiding text while exposing a URL
is still disclosure. All checks apply to direct API calls as well as UI controls.

| Actor | Public match facts | Private roster fields | Another user's contact | Create/revoke grant |
|---|---|---|---|---|
| Visitor | Candidate public subset | No | No | No |
| Signed-in person never in this match | Candidate public subset | No | No grant through this match | No new grant through this match under proposed creation gate |
| Active participant | Adopted participant fields | Adopted participant subset | Only with valid grant naming this actor | Own contact only |
| Playing host | Same participant access plus match-management fields | Required management subset | Same grant rule as any participant | Own contact only |
| Non-playing organizer | Management fields under agreed policy | Policy unresolved | Only with a valid grant naming this actor; eligibility Confirmed | Own contact only, through the same consent process |
| Participant who voluntarily left | Candidate public subset | No continuing private access proposed | Existing valid grants remain readable, Confirmed | Can revoke own grants; new-grant creation Open |
| Host-removed participant | Candidate public subset | No continuing private access proposed | Existing-grant behavior is being clarified | Can revoke own outstanding grants |
| Operator/support role | Explicitly approved minimum support fields | Restricted support workflow | No ordinary contact-browsing capability | No routine grant creation for others |

Exact roster fields and visibility are [Q-006](../../planning/open-questions.md#q-006).
A participant's display name is not automatically a private contact method, but
the roster can still reveal attendance and needs an audience decision.

## Proposed authorization predicates

Creation and retrieval need separate checks because existing grants survive
voluntary departure. **Proposed creation gate:** both people are current players
or the organizer in the originating match; consent names a recipient and method.
The precise creation eligibility remains Open.

For retrieval, use the following proposed server checks to enforce the confirmed rules:

1. The recipient is authenticated and is the named grantee.
2. The grant was validly created for this named recipient and originating match.
   Current playing membership is not required after voluntary leaving.
3. The originating match has not been cancelled. There is no expiry-time comparison.
4. The grant is active, the contact version matches, and both accounts remain active.
5. Neither user has invalidated access by blocking the other.

Host-removal behavior and reactivation after unblocking remain to be decided.

Missing data, unavailable authorization dependencies, and mismatched IDs deny access.
The server computes this predicate; a client-held “consented” flag is insufficient.
This predicate is a derived implementation recommendation for the proposed model.

## Contact lifecycle and proposed race behavior

| Event | Future in-app disclosure | Status |
|---|---|---|
| Owner revokes | Denied after revocation | Confirmed; ordering mechanics below proposed |
| Either party voluntarily leaves | Existing valid grants continue | Confirmed, DEC-019 |
| Host removes a person | Pending decision | Open, Q-010 |
| User rejoins after voluntary leaving | Existing valid grants still apply; no new consent needed solely for rejoining | Derived verification of DEC-019 |
| Match cancelled | Denied for grants originating in that match | Confirmed, DEC-019 |
| Match completes or time passes | Existing valid grants continue | Confirmed, DEC-018 |
| Match rescheduled | No expiry deadline to extend; preserve scope | Derived recommendation; edit flow still Open |
| Contact value changed | Old-value grants end; new value is not automatically shared | Confirmed, DEC-019 |
| Either party blocks | Deny contact access between the two people | Confirmed; unblock/regrant details Open |
| Contact deleted or account deleted/suspended | Deny future access under an adopted data-lifecycle policy | Proposal; retention separate |

None of these transitions erases a previously copied contact or removes a person
from an external conversation. Cancelling match A does not by itself invalidate a
separate otherwise-valid grant originating in match B; that follows the match scope.

For a read racing with revocation, define the authorization check/transaction as
the ordering point. Reads authorized before revocation commits may already be in
flight; later reads must fail. Refresh visible app contact views and avoid persistent
storage, but do not claim absolute recall from another person's device. If a UI
revocation attempt fails offline, show “Not yet revoked” until server confirmation.

## Proposed external handoff

1. Reauthorize the recipient's grant before retrieving the contact method.
2. Show the selected external destination and the fact that the next interaction
   happens outside the PWA.
3. Require a deliberate action to open it. Do not send messages or join groups
   automatically, and do not infer message delivery from a successful launch.
4. Use only the adopted contact methods and validated destination construction.
   If copying is allowed, make it an explicit action and explain that copies cannot
   be revoked by the app.
5. If no compatible app is installed or a link fails, show the approved fallback.
   The player remains joined; external failure is not membership failure.

Phone, email, WhatsApp and Telegram are Confirmed methods. Phone-number/username
formats, invite-link mechanics, SDKs and fallback behavior are not yet chosen.
Authentication email is not automatically a shareable contact. Granting one method
does not imply consent to every other method, even if they use the same identifier.

## External-service boundary

Participation and contact sharing are optional and do not require an account on
every supported external service. External services retain their own terms;
the internal [reference check](../../sources/external-references.md#provider-eligibility)
does not add product-facing age messaging, verification or a guardian flow. DEC-017
defines the product's current account and communication scope.

## Derived engineering recommendations

- Store contacts separately from public profile/match data; authorize every read.
- Keep contact values and contact-bearing URLs out of public pages, HTML metadata,
  search indexes, analytics, errors, logs, notification previews and shared caches.
- Do not persist granted contacts in a service-worker cache or offline data store.
  Public data caching must not accidentally include private fields.
- Audit grant creation/revocation using actor, recipient, match, method-version ID,
  timestamp, policy version and outcome; avoid the raw contact value in audit events.
- Prevent bulk enumeration and abuse; exact request limits need operational choices.
- Use synthetic contacts in fixtures and examples; keep production secrets out of
  the open repository.

## Draft UX text — Proposal

- Consent: “Share this contact with [participant] for [match]?”
- Lifetime: “Access has no time limit and stays available after leaving. You can revoke it.”
- Invalidation: “Blocking, match cancellation, or changing this contact ends access.”
- Optionality: “Sharing is optional. You can still participate without sharing.”
- Boundary: “They may copy your contact or use it outside this app.”
- Revocation: “Stop future access here. Details already viewed or copied cannot be recalled.”
- No consent: “No contact has been shared with you.”

Placeholders are intentional copy templates, not unspecified authorization fields
to ship unchanged. Final wording depends on the chosen providers and lifecycle.

Related: [requirements REQ-004 and REQ-011–015](../../product/requirements.md#req-004),
[contact journeys](../../product/journeys.md#j-004), [domain model](../../architecture/domain-model.md),
[privacy tests](../../validation/acceptance-tests.md#test-009).
