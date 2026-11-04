# Communication and contact privacy

## Current model — Confirmed

Users choose which of their contact methods to publish. Published methods appear
on profiles and match pages and are visible to anyone, including visitors without
accounts, before they join a match. Joining, playing, sign-in, and individual
recipient approval are not prerequisites. A non-playing host can display contacts
on a match with no players.

Supported methods are **phone number, email, WhatsApp, and Telegram**. Every method
is optional. Owners explicitly choose methods to display and may hide or change
them later. Adding a private method or signing in with an email does not publish
it automatically. There is no scheduled publication expiry.

Canonical decisions: [DEC-003](../decisions/decision-log.md#dec-003),
[DEC-016](../decisions/decision-log.md#dec-016), and
[DEC-023–024](../decisions/decision-log.md#dec-023). Canonical requirements:
[REQ-004](requirements.md#req-004), [REQ-011–014](requirements.md#req-011),
and [REQ-026](requirements.md#req-026).

The previous named-recipient, per-match grant design was explicitly corrected by
the user. It is preserved in the [historical snapshot](../decisions/history/contact-grants-before-correction.md)
and must not be implemented as the current contact-access contract.

## Audience and control matrix

| Actor or surface | Published methods | Unpublished methods | Can change publication? |
|---|---|---|---|
| Anonymous profile visitor | Visible | Not returned | No |
| Anonymous match visitor | Visible for users represented on the page | Not returned | No |
| Signed-in nonparticipant | Same public audience | No additional access | Own methods only |
| Participant | Same public audience | Membership gives no additional access | Own methods only |
| Host, including a non-playing host | Same public audience | Hosting gives no additional access to other users' methods | Own methods only |
| Contact owner | Can see and manage own methods | Accessible through their private settings | Yes |
| Operator | No in-app operator role | Infrastructure access is a later deployment concern | No product moderation authority |

Public display name, skill, role and upcoming matches are selected, with no
avatars or past-match lists, under DEC-038 as revised by DEC-044. Precise layout remains in
[Q-006](../planning/open-questions.md#q-006). Public audience applies whenever a
user's contact methods are displayed; it does not authorize exporting arbitrary
account fields or inventing a public user directory.

## Publication and lifecycle rules

The owner-control rules are Confirmed. Event consequences below are **derived
applications** of that public model, rather than independent recovered decisions.

| Event | Future app behavior |
|---|---|
| Owner adds a method without choosing to display it | Keep it private |
| Owner chooses to display a method | Show that selected method publicly on the supported surfaces |
| Owner hides a method | Stop returning it in subsequent public responses |
| Owner changes a displayed value | Show the new selected value; stop returning the previous one |
| Owner removes a method | Stop returning it publicly; detailed storage retention is separate |
| Person joins, leaves, is removed, or fails to reconfirm | Do not change their profile publication settings |
| Match is cancelled or completed | Show only terminal match state, without details/roster/contacts; do not change profile publication settings |
| A signed-in person is blocked | Do not promise to conceal public contacts from their anonymous browsing |
| Time passes | No scheduled expiry; owner choice continues |
| Account is deleted | Immediately hide its profile/contacts and apply the adopted participation/hosting deletion rules; storage purge is separate |
| Personal blocking | No personal blocking feature or in-app moderation tools in MVP |

No recipient-grant object, reciprocal sharing step, per-match consent refresh, or
contact-access timer is needed by the current public model. Participation records
must not contain frozen contact copies. Contact values already copied, sent, or
captured outside the app cannot be recalled by hiding them later.

The earlier blocking/cancellation/contact-change invalidations in DEC-019 applied
to grants. They are superseded, not current promises that public information can
be hidden from a named viewer.

## External communication boundary

MVP participant chat is external. The app does not provide a native participant
inbox, messages, read receipts, attachments, or conversation history. Service
notifications about match events are a separate product decision.

**Derived recommendations selected under DEC-060:**

- Use deliberate actions such as calling, emailing, opening a chat, or copying a
  visible value. Do not launch another application automatically on page load.
- Support phone and WhatsApp numbers as separately selected methods, even if their
  values coincide. Selecting one must not silently publish the other.
- Normalize supported identifiers and build destinations from allowlisted schemes
  and provider routes. Do not treat contact text as arbitrary executable links.
- Provide a copy fallback if the external application cannot open. Launch success
  is not proof of message delivery.
- Let a person join or host without publishing a contact; show useful match details
  even when no contacts are present. Optional publication cannot become compulsory
  merely to ensure coordination.
- Do not retrieve or store external conversation content.

Format validation without ownership verification is Confirmed by DEC-045. Exact
formats and launch/copy behavior are specified in
[selected defaults](../decisions/derived-defaults.md); external group invites are
outside that individual-contact baseline. See [Q-008](../planning/open-questions.md#q-008)
and [Q-009](../planning/open-questions.md#q-009).

## Private data boundaries — Derived recommendations

Keep sign-in identifiers and recovery details separate from public contact fields.
Allow anonymous reads of explicitly published methods, but never return unpublished
values in page HTML, public API responses, structured metadata, hidden UI elements,
prefetch payloads, or error text. Hiding a field visually is not sufficient.

Authorize writes to the owner on the server. Use current publication state for
public responses rather than cached membership snapshots. Specify cache invalidation
so hiding or editing a method updates app-controlled surfaces; avoid persistent
offline copies of contact-bearing pages. Account personal data is deleted immediately;
terminal match details/notices expire after 30 days and backups within 30 days.
Do not acknowledge a visibility change while app-controlled projections still
serve the prior value on a new request.

Exclude raw contact values and destination links from routine analytics, logs, and
notification payloads. Public visibility does not make copying those values into
every operational system necessary.

## Product wording — Proposed

Before publication: “Anyone can see the contact methods you choose to display,
including people without an account.”

In settings: “Hide this contact” and “Change contact.”

After hiding: “This contact is no longer shown. People who already copied it may
still have it.”

These are selected draft copy defaults, subject to implementation wording review.
No age-specific product flow or
message is added; [DEC-017](../decisions/decision-log.md#dec-017) is closed. Internal
[external references](../sources/external-references.md) do not change that product scope.

## Verification

Derived acceptance scenarios must cover:

1. Anonymous access to selected host contacts on a zero-player match.
2. Anonymous access to selected profile contacts without joining any match.
3. No exposure of unselected fields, including a private sign-in email.
4. Owner hide/edit affecting subsequent profile and match responses.
5. No publication caused by joining, hosting, or another person's contact choice.
6. A non-playing host publishing without consuming a playing place.
7. Independent phone, email, WhatsApp, and Telegram publication choices.
8. Leaving, removal, cancellation, and blocking never being described as private
   recipient revocation of still-public profile details.

See [acceptance scenarios](../validation/acceptance-tests.md). These are a specification;
no product implementation has been tested.
