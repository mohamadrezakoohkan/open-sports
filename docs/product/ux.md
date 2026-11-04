# UX and interaction guidance

These are **Derived recommendations selected under DEC-060** unless linked to a confirmed decision.
No wireframes, brand system, visual design, or usability research were recovered.

## Information structure

Selected navigation: Discover matches, My participation, Host a match,
Notifications, and Profile/settings. Public pages should allow viewing without
forcing account creation; sign-in is required at joining and other adopted account actions.

Separate the host's organizing role from their playing place. Show “Host” and
playing role independently. Display capacity as playing places, not number of
accounts associated with the event.

## Joining and reconfirming

- Label a successful instant join clearly. Do not show a host-approval state.
- Show skill range, available general/role places and admission deadline before joining.
- Treat Any level as an admission policy, not a selectable fourth player skill.
- On reconfirmation, show the changed time/location, current deadline and current
  availability. Explain that the former place was released and is not reserved.
- Show a failed admission as full, closed, excluded or ineligible as applicable.
  Do not imply host approval can override a full or closed match.
- Keep a leave action available after admission closes.
- Do not add overlap warnings or calendar-conflict checks.

## Contact publication

Selected methods are public on profiles and match pages, including for anonymous
viewers. Provide explicit per-method publication controls, with a clear public
audience. Do not use “share privately,” “approve recipient,” or membership-lock
icons for those public fields.

Keep authentication/recovery settings separate. A user's lack of public contacts
is valid; neither hosting nor joining should be framed as consent to publish.

Use [contact privacy](communication-and-privacy.md) as the canonical behavior.
Provider launches and copy fallback are selected defaults in
[derived defaults](../decisions/derived-defaults.md).

## Editing and destructive match actions

Preview consequential edits before committing. A time/location edit
should make immediate place release and required reconfirmation clear. Incompatible
capacity/role/skill edits explain which current allocations prevent the change.

Removal requires a reason. Cancellation and removal should avoid accidental taps,
but confirmation UI must not create a host-approval join gate. Only host and removed
player see a removal reason. Lock time/location edits at start; complete at end.
Terminal pages show only ended/cancelled state, with no details or roster.

## States, accessibility and language

- Distinguish empty search results, no contacts selected, full places, admission
  closed, cancelled, reconfirmation pending, expired request and network failure.
- Preserve form values on recoverable errors; explain what can be corrected.
- Provide keyboard navigation, clear focus, meaningful labels and text status.
  WCAG 2.2 AA is the confirmed target, not a verified result. Validate the latest
  two stable Chrome/Safari/Firefox/Edge versions on mobile/desktop.
- Avoid relying on color or icons alone for availability and privacy.
- Support English, Spanish and Dutch under
  [DEC-062](../decisions/decision-log.md#dec-062). Display match-local time with its
  time zone; language choice does not change the venue's time zone.
- Hosts choose a map pin plus venue/address/city; exact location is public.
- Public profiles/rosters show display names, skill and relevant roles; profiles
  show upcoming matches only. No avatars or public past-match lists.
- Offline, show an offline screen instead of cached match data or queued actions.
- Do not add age fields, filters, restrictions or age-related product messages.

See [resolved questions](../planning/open-questions.md) for deliberate deferrals and
[journeys](journeys.md) for the core interaction sequences.
