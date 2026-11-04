# Security and non-functional requirements

Confirmed targets and selected derived controls are distinguished below. This is
a specification, not an audit of an implemented service or a compliance certificate.

## Confirmed targets

- Responsive mobile/desktop, latest two stable Chrome/Safari/Firefox/Edge versions.
- WCAG 2.2 AA target for core journeys; record tested versions/results at release.
- Installable PWA, offline screen, online-only match data and actions.
- Explicit owner selection before public contact publication; hidden values stay private.
- Removal reasons visible only to host and removed player.
- Immediate account personal-data deletion; all unfinished participation/hosting
  withdrawn/cancelled; terminal records/notices deleted after 30 days; backups within 30 days.
- No in-app reports/moderation/personal blocking; external GitHub support only.

## Selected authorization and data controls

Apply server-side per-request authorization, separate public projections from
private account data, and authorize owner/host mutations independently. Hiding
fields in UI is insufficient. Public HTML, APIs, embedded state and prefetch must
exclude unpublished contact, login/reset data, private notices and removal reasons.

Use maintained password authentication, secure hashes, rate-limited sign-in/reset
and expiring single-use reset tokens. No email-verification gate or contact ownership
challenge is introduced. Validate text as data and allowlist external destinations.

Public contacts can be copied by visitors. Owner hiding updates future app responses;
it does not recall external copies. Terminal match pages expose no old details or
roster even if the data remains inside the 30-day retention window.

[OWASP authorization guidance](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)
is engineering background; the product decisions remain source-linked in this repository.

<a id="supabase-access-controls"></a>
## Supabase access controls

**Status: Derived recommendation** applying the existing controls to the
[selected backend](../decisions/decision-log.md#dec-061). No policies have been
implemented or tested.

- Enable RLS on exposed tables and restrict grants for anonymous and authenticated
  roles. Owner and host permissions need independent checks; RLS does not enforce
  capacity, revision or lifecycle invariants by itself.
- Keep authentication email, unpublished contacts, private notices and removal
  reasons outside public projections. Row access does not hide columns. Deny raw
  table access that would bypass a projection, including through nested API queries.
- Review views and functions as authorization boundaries. Views may bypass
  underlying RLS by default; use invoker semantics where appropriate. Any privileged
  projection or mutation must explicitly authorize its caller and fields, constrain
  function execution grants and fix its search path. Public access to a function
  cannot imply public access to its underlying private data.
- Keep secret/service-role credentials server-side; they can bypass ordinary data
  policies. A browser publishable key is not a substitute for authorization.
- Configure Supabase Auth for email/password with Confirm Email disabled, preserving
  DEC-045. Do not present provider-internal confirmation state as verified ownership.
  Test reset redirects and custom SMTP delivery before public use; no verification
  gate or match-service emails are introduced.
- Verify deletion across Auth, sessions and application records. An Auth admin call
  and a database RPC are separate operations; deletion must fail closed and retry
  safely without restoring access or retaining personal data as a normal success.

The [official technical sources](../sources/external-references.md#supabase-technical)
describe these mechanisms. Acceptance must exercise anonymous callers, owners,
other signed-in users, hosts and removed players against API payloads, not only UI.

## Integrity and reliability

| Failure mode | Selected control | Acceptance evidence |
|---|---|---|
| Last-place race or duplicate retry | Atomic allocation and unique/idempotent transition | Concurrent join/reconfirm and repeated request |
| Old details accepted | Revision checks | Reschedule/reconfirm race |
| Expiry releases twice | Pending holds no place; revision-aware expiry | Stale expiry after successful reconfirmation |
| Host edit evicts silently | Pre-edit roster compatibility check | Capacity/role/skill edit with concurrent join |
| Failed role switch loses place | Atomic transfer | Target pool fills during switch |
| Old public contact survives hide | Fresh projection/invalidation | Read profile/match payloads after change |
| Offline screen implies participation | No offline match data/writes; reconcile | Disconnect during mutation |
| Notification disagrees with state | Durable idempotent service event | Failure/retry between commit and list projection |
| Backup revives a deleted account | Erasure-aware restoration | Restore within retention window |

## Accessibility and browser verification

Use the [WCAG 2.2 criteria](https://www.w3.org/TR/WCAG22/) with automated checks
and manual keyboard, focus, zoom, contrast, reflow and assistive-technology review.
Test discovery/maps with a usable list/manual-location fallback, all forms, privacy
controls, joining/switching/reconfirmation and error recovery.

Supported-browser versions are rolling; record exact versions at release.
Installation affordances vary with browser/OS, so test supported installation
paths without claiming identical UI everywhere. Core web use must remain usable.

## Operation and observability

Repository maintainers own external support and product decisions. No commercial
SLA or measured performance claim is made. Routine diagnostics exclude contacts,
credentials and contact-bearing links; cap them at 30 days. No third-party behavioral
analytics SDK is part of MVP.

Exercise purge, deletion, restoration, retry and worker-delay behavior before
deployment. Reject implementations that cannot meet immediate deletion or the
30-day backup bound. Supabase is selected, but its hosted Free pausing/recovery
behavior remains an unresolved deployment conflict in
[Q-019](../planning/open-questions.md#q-019). Scheduled cleanup cannot prove provider
snapshot expiry or run while its database is paused. A paid plan's advertised backup
window alone also does not verify deletion across every retained copy.

Resolve hosting retention and [SMTP setup](../planning/open-questions.md#q-020),
then size the pilot and measure concrete performance/load/recovery targets on
realistic devices and connections. Track free-plan consumption using the
[dated provider limits](../sources/external-references.md#supabase-free-hosting);
reaching a quota does not authorize an automatic paid upgrade.

No product implementation exists here. See [validation report](../validation/validation-report.md)
for documentation checks and [scenarios](../validation/acceptance-tests.md) for
product tests that remain Not run.
