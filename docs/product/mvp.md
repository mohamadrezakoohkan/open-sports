# MVP scope and release boundary

## Current scope

The first release is a free, installable PWA for public sports matches. It covers
any sport with searchable/custom entries. Spain and UK cities are the pilot focus;
other countries are permitted. UI is English/Spanish, with venue-local times and
explicit time zones.

The core loop is public discovery → email/password account → host or instantly
join → manage/leave/reconfirm → coordinate through optional public contact methods
and external communication. The [requirements](requirements.md) and
[selected derived defaults](../decisions/derived-defaults.md) define precise behavior.

| Priority | Capability | Requirements |
|---|---|---|
| P0 | Installable online-only PWA, supported browsers/accessibility | REQ-001, REQ-016–017 |
| P0 | Email/password accounts, reset, public upcoming-only profiles | REQ-005 |
| P0 | Map/filter discovery and public exact locations | REQ-006, REQ-019, REQ-032 |
| P0 | Publish start/end, places, skill range and admission deadline | REQ-007, REQ-020–025, REQ-027 |
| P0 | Instant capacity-safe join, unrestricted leave, role switching | REQ-002, REQ-008–009, REQ-036 |
| P0 | Host edits/cancel/removal, competitive reconfirmation, completion | REQ-010, REQ-028–030, REQ-034 |
| P0 | Optional public contacts, current visibility controls, external handoff | REQ-003–004, REQ-011–014, REQ-026 |
| P0 | Private in-app service list and external GitHub support | REQ-015, REQ-031 |
| P0 | Account deletion and bounded retention | REQ-018, REQ-035 |

Priority is a selected derived planning default under DEC-060, not an invented
earlier backlog. Every listed capability belongs to the documented MVP baseline.

## Confirmed exclusions

- Private matches, waitlists, recurrence, ratings, payments and venue booking.
- Host approval for public joining and host transfer.
- Native participant chat and email/push match-service notifications.
- Mandatory/automatic contact disclosure, named-recipient contact grants and ownership verification.
- Avatars and public past-match lists.
- In-app reports, moderation tools and personal blocking.
- Age restrictions, declaration/verification, age fields/filters and age-related messaging.
- Schedule-overlap checks or warnings.
- Offline match browsing and queued offline actions.

Selected derived exclusions also keep automatic penalties, external group invites,
social sign-in and behavioral analytics SDKs outside this small release.
Future ideas in the [roadmap](../planning/roadmap.md) are uncommitted.

## Scope and history

Current decisions replace earlier private contact grants, leave cutoffs, past-match
lists and proposed moderation features. [Decision history](../decisions/decision-log.md)
preserves those changes. The full original conversation was unavailable; this scope
is reconstructed from accessible sources and the owner's current answers.

## Implementation and release gates

1. Select stack/providers later without changing the fixed rules; technology neutrality
   is deliberate, not missing product design.
2. Implement and pass the [acceptance scenarios](../validation/acceptance-tests.md),
   especially concurrency, reconfirmation, public/private projections and deletion.
3. Validate the browser matrix, installation affordances and WCAG target on real UI.
4. Configure purge/backups, reset-email delivery, support and restoration to satisfy
   the adopted retention rules.
5. Publish the operated source version and license information; preserve third-party notices.
6. Pilot and use aggregate outcomes/voluntary feedback to decide expansion.

This documentation completes specification work, not application implementation,
deployment or release certification.
