# Resolved questions and deliberate deferrals

The owner completed the decision rounds and delegated remaining small defaults in
[DEC-060](../decisions/decision-log.md#dec-060). There is **no outstanding product
question requiring another answer to finish this package**. Selected defaults stay
labeled Derived recommendations. Future proposals are not commitments.

<a id="q-001"></a>
## Q-001 — sport and geography
Resolved: any sport, searchable/custom entries, Spain/UK pilot focus with other
countries allowed (DEC-005/035/049).

<a id="q-002"></a>
## Q-002 — age-related scope
Resolved and closed: no restrictions, declaration, checks, age fields/filters,
guardian-specific flow or age-related messaging (DEC-013/014/017). Do not reopen.

<a id="q-003"></a>
## Q-003 — host occupancy
Resolved: optional playing host, playing-only occupancy, ordinary skill/role
eligibility for a playing host (DEC-006/058).

<a id="q-004"></a>
## Q-004 — capacity and participation changes
Resolved: mixed general/custom roles, capacity-safe switching before cutoff,
compatible host edits, removal exclusion until lifted, unchecked overlaps
(DEC-012/027/033/035/036/058). Atomicity/duplicate handling are selected defaults.

<a id="q-005"></a>
## Q-005 — skill
Resolved: per-sport self-declaration, three levels, range/Any level, missing level
accepted for Any level, unrestricted edits without losing current participation
(DEC-009–011/034). Current-rule transition details are in the selected defaults.

<a id="q-006"></a>
## Q-006 — discovery and public profiles
Resolved: public names/skill/roles/upcoming matches, no avatars/past lists; public
exact locations; map/distance and selected filters with soonest-start order
(DEC-038–040/044/046/050). Manual origin/radius and list defaults are documented.

<a id="q-007"></a>
## Q-007 — contact audience and optionality
Resolved: owner-selected public methods on profiles and active match pages,
including anonymous pre-join access; no methods required (DEC-023/024).

<a id="q-008"></a>
## Q-008 — external handoff and service notifications
Resolved methods and in-app-only service list (DEC-016/031). Deliberate launch/copy,
individual methods without group invites, read/unread behavior, event recipients
and 30-day notice lifetime are selected defaults or explicit retention decisions.

<a id="q-009"></a>
## Q-009 — ownership verification
Resolved: no email-verification gate, email password reset, contact format validation
only, no possession challenge or verified badge (DEC-045).

<a id="q-010"></a>
## Q-010 — contact lifecycle
Resolved: owner hide/edit/remove; no scheduled publication expiry; public profile
settings independent of participation; terminal match pages hide details; account
deletion removes public data immediately (DEC-024/048/050/054).

<a id="q-011"></a>
## Q-011 — match lifecycle and host controls
Resolved: start/end, automatic completion, start-time lock on time/location edits,
join/reconfirm cutoff, leave anytime while active, immediate release and competitive
reconfirmation, nonresponse expiry, compatible host edits, private removal reasons,
no transfer (DEC-022/025–033/043/053). No automatic penalties; exact boundaries,
repeat edits and reopening deadlines are selected defaults.

<a id="q-012"></a>
## Q-012 — identity and profiles
Resolved: email/password; hosting/joining/profile edits require accounts; public
browsing; no avatar or email verification; reset by email (DEC-037/038/044/045).

<a id="q-013"></a>
## Q-013 — support, deletion and retention
Resolved: external GitHub Issues, no in-app reporting/moderation/blocking; reasons
private to host/removed player; delete account personal data immediately and
withdraw/cancel all unfinished participation/hosting; terminal match records/notices
expire after 30 days and backups within 30 days (DEC-047/048/051–054).

<a id="q-014"></a>
## Q-014 — licensing and governance
Resolved: AGPL-3.0-only for code/docs (DEC-056). Repository maintainers own changes
and external support as a derived default. Preserve third-party notices; no
separate contribution agreement or governance body is introduced.

<a id="q-015"></a>
## Q-015 — architecture and PWA
Resolved product behavior: installable, offline screen, online-only match data and
actions (DEC-057). **Explicitly deferred:** technology/vendor selection under DEC-055.
Logical components, transactions, authorization and retention remain specified.

<a id="q-016"></a>
## Q-016 — quality and operation
Resolved: latest two stable Chrome/Safari/Firefox/Edge, mobile/desktop, WCAG 2.2 AA
target (DEC-059). Selected operational defaults include nonpersonal diagnostics,
30-day logs, durable jobs, restore/deletion checks and no commercial SLA.
Infrastructure budget, sizing, provider-specific recovery/load targets and actual
measured performance belong to implementation planning; no deployment is authorized.

<a id="q-017"></a>
## Q-017 — locations and languages
Resolved: custom sports/roles, map pin plus venue/address/city, public precision,
optional device origin/manual fallback, English/Spanish and match-local time with
zone, global location allowance (DEC-035/040/041/046/049).

<a id="q-018"></a>
## Q-018 — release boundary and business model
Resolved: free public-only MVP and explicit deferrals (DEC-042). No monetization,
future feature commitment or numerical growth target is invented. Future pilot
hypotheses remain proposals in the roadmap.

## Items that remain unknowable or implementation-dependent

- Earlier conversation and four assistant reply bodies were unavailable; current
  answers do not recover them. See [source coverage](../sources/recovery-status.md).
- The remote had no PR base. Delivery reports the final inspection and fallback.
- Stack/providers, operational resources and deployment are intentionally outside
  this technology-neutral documentation task.
- Acceptance scenarios cannot pass against an application that has not been built.

These limits are not hidden unresolved product choices or reasons to ask another
round. See [selected defaults](../decisions/derived-defaults.md) for their derivations.
