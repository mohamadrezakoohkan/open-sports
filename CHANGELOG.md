# Changelog

## 2026-11-04 — Supabase backend and Dutch/Netherlands MVP scope

- Recorded the free-cloud research request and exact Supabase selection as
  SRC-029/030; added DEC-061 and partially superseded DEC-055 for the backend only.
- Updated current architecture and summaries; labeled component mapping as Derived
  recommendations while leaving frontend, map and SMTP providers unselected.
- Preserved product behavior and the 30-day backup bound. Added Q-019/020 for
  free-hosting/retention feasibility and public password-reset delivery, with
  requirement links and TEST-029; product scenarios remain Not run.
- Updated source coverage, traceability and current delivery status. SRC-031
  records the now-existing main branch; earlier empty-remote evidence is preserved.
- Added Dutch alongside English/Spanish and the Netherlands alongside Spain/UK
  under DEC-062/SRC-032. Updated requirements, journeys, UX, discovery/language
  defaults, roadmap and acceptance coverage while retaining other countries.
- Documentation only: no application code, provider resources, deployment or paid
  service commitment. Work is isolated on `codex/select-supabase-mvp` for PR review.

## 2026-11-04 — documentation reading guide

- Added `docs/reading-guide.md` at the owner's request, with a first-reading order,
  paths by task, a complete document map, status and identifier explanations,
  an evidence-to-test example, and maintenance guidance.
- Linked the guide from both entry-point READMEs. Product decisions are unchanged.

## 2026-11-04 — initial documentation reconstruction

- Recovered five user turns from the referenced conversation; recorded four
  unavailable assistant replies and the unavailable earlier history.
- Preserved four confirmed product constraints with source references.
- Added explicitly proposed MVP details, journeys, contact-sharing rules, domain
  model, architecture, acceptance scenarios, and a roadmap without commitments.
- Added decision history, derived exclusions, source-to-test traceability,
  documentation checks, and repository guidance for future agents.
- Resolved the repository placeholder from the user's follow-up URL. Inspected
  the empty remote; prepared a local dedicated branch and offline deliverables.
- No product implementation, deployment, license selection, remote default-branch
  initialization, or PR creation occurred.

## 2026-11-04 — product clarification round 1

- Recorded new user decisions separately from recovered conversation history:
  any sport, cities across Spain and the United Kingdom as pilot, optional host
  playing participation, and signed-in joining subject to host-selected eligibility.
- Added DEC-005–007 and REQ-019–020; refined admission requirements and MVP summaries.
- Preserved “no age range” verbatim while clarifying its meaning for accounts and
  age filters. Allowed host eligibility criteria and skill assessment remain pending.

## 2026-11-04 — product clarification round 2

- Recorded adults-only MVP participation with no displayed ages or age filters.
- Limited host eligibility criteria to skill level and playing position/role.
- Confirmed self-declared skill separately for each sport; no verified skill
  assessment is required by the selected MVP mechanism.
- Added DEC-008–010 and REQ-021–023. Preserved the earlier age ambiguity as history
  and linked it to the explicit clarification.
- Adult-check mechanism, skill scale, and role-capacity model are the next pending choices.

## 2026-11-04 — product clarification round 3

- Confirmed Beginner/Intermediate/Advanced declarations with a host-selected skill
  range or “Any level,” and optional role-specific places alongside general-place matches.
- Explicitly excluded age declaration; preserved the previously selected adults-only
  policy while clarifying whether it remains a policy without checks or is removed.
- Added DEC-011–013, REQ-024–025, and explicit rejection REJ-004; updated the source
  record and decision agenda. Contact-sharing scope and providers are now being asked.

## 2026-11-04 — product clarification round 4

- Replaced the former adults-only restriction with all-ages participation, preserving
  the earlier choice as a partially superseded decision.
- Adopted one-way named-person/match contact sharing, including non-playing hosts,
  with owner revocation. Selected phone, email, WhatsApp and Telegram.
- Added DEC-014–016 and REQ-026; recorded primary external-provider references
  separately from product decisions.

## 2026-11-04 — product clarification round 5

- Closed age-specific product design: no age restrictions, checks, declarations,
  age-specific account flows or age-related product messaging.
- Adopted no scheduled contact-access expiry and continuation after voluntary
  leaving; blocking, cancellation, contact changes and explicit revocation end access.
- Separated grant-creation proposals from grant-read authorization to preserve
  valid post-departure access. Host removal remains a distinct pending choice.
- Added DEC-017–019 and updated requirements, consent rules, and decision agenda.

## 2026-11-04 — contact correction and match lifecycle rounds

- Preserved the prior contact-grant specification in a clearly superseded history
  document. Replaced the current model with owner-selected public methods on
  profiles/match pages, including anonymous and pre-join access (DEC-020/023/024).
- Confirmed host controls without transfer and host-defined deadlines (DEC-021/022).
- Initially adopted a shared join/leave deadline, then explicitly superseded its
  leaving restriction: players may leave anytime; the deadline gates joining and
  reconfirmation only (DEC-025/029/032).
- Required reconfirmation after time/location changes, immediate release of all
  playing places, competition with new joins, and automatic nonresponse closure
  without double-release (DEC-026/028/030).
- Allowed overlapping matches without checks/warnings (DEC-027).
- Selected in-app-only service notifications and compatible capacity/role/skill
  edits that preserve current players (DEC-031/033).
- Allowed missing skill for Any level, edits without losing current participation,
  custom sports, host-named roles and mixed place pools (DEC-034/035).
- Made removal a match-specific rejoin exclusion until the host lifts it (DEC-036).
- Updated current requirements, journeys, privacy rules and proposed architecture;
  sign-in, public roster fields and discovery choices are the current question round.

## 2026-11-04 — account, discovery, localization and scope rounds

- Selected email/password accounts for hosting/joining/profile edits, with public
  browsing (DEC-037).
- Selected public display names, skills, roles and past/upcoming matches, without
  avatars (DEC-038).
- Added map/distance, city, sport, date, skill and available-place discovery with
  soonest-start sorting (DEC-039).
- Selected public exact location through a map pin and venue/address/city, and
  English/Spanish with match-local time and explicit time zone (DEC-040/041).
- Confirmed free public-only MVP, deferring private games, waitlists, recurrence,
  ratings, payments and venue booking (DEC-042).
- Match timing/completion, public-history edges, and account/contact verification
  are being resolved next.

## 2026-11-04 — completed product baseline

- Required start/end, start-time lock on time/location and automatic completion.
- Replaced public past-match lists with upcoming-only lists; terminal links show
  state only without details or roster.
- Selected no email verification, email reset and contact format validation only.
- Added optional device-location/manual origin, global locations beyond the pilot,
  external GitHub Issues support and exclusion of in-app reporting/moderation.
- Defined immediate account-data deletion across all unfinished participation and
  hosted matches, private removal reasons, 30-day terminal-record/notice retention
  and backups expiring within 30 days.
- Selected technology neutrality, AGPL-3.0-only for code/docs, an installable PWA
  with online-only match data/actions, ordinary playing-host eligibility, atomic
  role switching, and browser/WCAG targets.
- Recorded the owner's delegation to select small defaults and finish; added the
  derived-defaults document and closed the question register with explicit deferrals.
- Updated requirements, journeys, domain/architecture, privacy and acceptance
  coverage; preserved superseded contact, cutoff and profile-history choices.
- Rechecked the empty remote and its missing PR base. Prepared local-only delivery
  without default-branch initialization or any remote push.
