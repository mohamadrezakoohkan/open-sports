# Selected derived defaults

**Status: Derived recommendations selected under [DEC-060](decision-log.md#dec-060).**
These complete small interaction and engineering details within the confirmed
decisions. They are the current implementation baseline, not individually confirmed
historical choices. This delegation does not select vendors or adopt future ideas.

## Admission and capacity

- One host per match and at most one active playing allocation per account/match.
  Organizing authority is separate; no host transfer.
- General and named-role pools have positive integer capacities; total capacity
  is their sum. Each player chooses exactly one pool. Trim role labels and reject
  duplicate labels within the same match.
- Offer existing sports before custom entry. Preserve distinct sport identifiers;
  do not infer shared skill from loosely similar free-text sport names.
- A playing host meets ordinary admission rules and consumes a suitable place.
  A host unable to meet playing eligibility may organize without playing.
- Publish with a future start, end after start, and future admission deadline no
  later than start. Admission and role switching require authoritative time
  **strictly before** the deadline; equality is closed.
- A host may edit/reopen the deadline before start if it remains future and no
  later than start. Leaving never reopens it automatically. An expired pending
  request is not revived; a person can attempt a fresh normal join if permitted.
- No automatic late-leave, no-show, overlap or reconfirmation-expiry penalties.
- Role switching atomically requires current skill eligibility, available target
  capacity and an open deadline. Failure preserves the old allocation.
- Level guidance: Beginner is learning fundamentals; Intermediate is familiar and
  reasonably consistent; Advanced is experienced. These are self-assessments,
  not ratings or promises of identical ability across sports.
- Current declarations apply to new joins, reconfirmations and role switches.
  Skill edits never remove an existing allocation. Capacity-only edits do not
  revalidate unrelated skill changes. A host changing the skill range must
  accommodate all current players' current declarations or remove them first.
- For a combined time/location and capacity/role/skill edit, check compatibility
  against the pre-edit active roster before releasing places for reconfirmation.
  Combining edits must not bypass recorded-reason removal.
- Repeated material edits replace pending requests with the newest revision and
  deadline. Old confirmations/expiry jobs cannot affect a newer allocation.
- Cancellation is terminal: no uncancel/reopen or completed-match editing.
  Until end, compatible non-time/location edits, withdrawal and host removal
  remain possible. Start locks time/location, including end-time edits.
- Leaving does not create an exclusion. Host removal excludes joining and
  reconfirming until lifted; lifting only enables a normal admission attempt.

## Match fields and presentation

Required: sport, map pin, venue/address text, city, start/end, location time zone,
place pools, skill range or Any level, admission deadline, and whether the host
plays. Resolve/select country from location without a country allowlist. Optional
title and practical instructions cannot add enforced eligibility criteria.

Render authored content as text. Selected bounds: display name/role 80 characters,
custom sport 100, title 140, venue/address 300, instructions 2,000, removal reason
1,000. Require a nonblank removal reason. These are derived limits. Pin, venue or
address changes require reconfirmation; there is no cosmetic-location bypass.

Public profiles show active future participation and future hosted matches,
identifying a non-playing organizer separately. Omit pending, left, removed,
cancelled and completed participation. No public past-history list. Owners retain
private access to current unfinished matches for management and withdrawal.

Terminal match URLs show only ended/cancelled state. After the full record expires
at 30 days, retain only a minimal nonpersonal marker: opaque ID and terminal state.
No names, contacts, location, schedule, roster, reason or narrative survive in it.

## Discovery and localization

- Public discovery contains published future matches, including full/closed
  matches unless filtered for available places. “Available” means unoccupied
  capacity while admission is open; individual eligibility is checked at admission,
  so a guest can still browse availability.
- Combine filters. Interpret dates in each venue's local calendar. Sort by start
  instant, with stable identifier as tie-breaker.
- Distance is approximate straight-line kilometers, labeled accordingly. An
  optional user-selected radius filters results; no radius is imposed initially.
  A selected city/map point or explicit device-location action sets the origin.
- Request geolocation only through “Use my location.” Denial/failure preserves
  manual input. Keep origin in the browsing session, not a public profile or
  permanent location history.
- Prefer browser English/Spanish, otherwise English; provide a language switch
  and save account/local preference. Do not automatically translate authored text.
- Store an instant plus IANA location time zone. Reject nonexistent local times
  and disambiguate repeated clock-change times. Show time zone/offset. Do not
  hard-code one offset per country.

## Accounts and contact handoff

- Email/password only; no social sign-in, verification gate, phone login, avatar,
  or required public contact. Password-reset email is an authentication channel.
- Use maintained authentication, secure password hashing, expiring single-use
  reset tokens, rate-limited sign-in/reset and non-enumerating reset responses.
  Do not implement custom password cryptography.
- Keep authentication email separate. A login-email change requires recent
  password authentication, without adding an email-verification gate. Invalidate
  obsolete reset tokens and sessions as appropriate to the change.
- Each method starts hidden. MVP stores at most one current value per method
  type; phone and WhatsApp remain independently selected.
- Accept international phone/WhatsApp numbers with country code, an email address,
  and a Telegram username (leading @ optional). Apply supported provider/URI
  format rules without possession challenges or verified badges.
- Individual methods only: no arbitrary chat URLs, group invites or bot credentials.
  Provide deliberate call/email/open-chat and copy actions using allowlisted
  destinations and safely encoded values. Do not prefill private match/account data.
  Failed opening leaves copying available; opening is not proof of sending.
- Never cache match/contact pages for offline browsing. Public responses use the
  current selected projection; invalidate app-controlled projections after changes.
  Previously rendered/external copies cannot be recalled.
- No in-app chat, personal blocking, reports, moderation dashboard or automatic
  support-issue submission.

## Service notifications

Private, reverse-chronological in-app list: unread/read state, unread count,
open-to-mark-read and mark-all-read. Expire each notice 30 days after creation.
No email/push service channel. Reading a notice never reconfirms participation.

Notify affected players of material/practical changes, cancellation, removal and
reconfirmation requests. Notify hosts of joins, withdrawals, reconfirmations and
role switches. Suppress duplicate self-notices for the actor. Lifting an exclusion
invites a normal join attempt without guaranteeing a place. Notify pending players
when their request expires.

Use idempotent event identifiers and current state links. Store no contact copies.
Only host/removed-player views expose a removal reason. Terminal links reveal only
terminal state.

## Retention and operations

Delete account personal data immediately from active storage when deletion commits;
revoke sessions, remove public projections and erase/anonymize personal references
and authored personal data in retained service records. Withdraw/cancel all unfinished
participation/hosting. Delete match details 30 days after completion/cancellation,
notices 30 days after creation, and backups within 30 days. Reapply deletions before
restored data can be served.

Repository maintainers own changes and external GitHub support. No commercial
response-time or availability SLA is promised. Use timeouts, rate limits,
transactional state changes, durable idempotent jobs and automated purge/recovery
checks. Routine logs exclude contacts/credentials and expire within 30 days. No
third-party behavioral analytics SDK is included in MVP.

Concrete hosting/database/map/authentication/SMTP vendors, infrastructure budgets
and load/service targets are deliberately deferred with implementation under
DEC-055. They must satisfy the fixed data, browser and quality rules before deployment.

Future pilot evaluation can use aggregate operational counts and voluntary feedback
about joining, coordination and reconfirmation. No numerical growth/revenue target,
research result or telemetry integration is invented.
