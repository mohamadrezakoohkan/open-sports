# Acceptance scenarios

**Execution status: Not run against a product.** These scenarios test the confirmed
requirements and selected derived defaults. No application implementation exists
in this repository. Scenario design and documentation-check passes do not constitute
product-test, accessibility, security or performance passes.

<a id="test-001"></a>
## TEST-001 — Browser, installation and license

**Covers:** [REQ-001](../product/requirements.md#req-001).

**Setup/action:** Open core flows and installation paths on the adopted browser/OS matrix; inspect published source/license metadata.

**Expected:** Record latest two stable Chrome/Safari/Firefox/Edge versions and responsive mobile/desktop results. Installation works where supported by platform affordances; core web use remains usable. Source/docs identify AGPL-3.0-only. This does not certify conformance.

<a id="test-002"></a>
## TEST-002 — Instant join, last-place race and retry

**Covers:** [REQ-002](../product/requirements.md#req-002), [REQ-008](../product/requirements.md#req-008).

**Setup/action:** Race two eligible accounts for the last place; retry after losing a success response; repeat as guest.

**Expected:** At most one new allocation succeeds. Retry creates no duplicate; successful joining is immediate without host approval. A guest gets no allocation.

<a id="test-003"></a>
## TEST-003 — Skill declaration, editing and eligibility

**Covers:** [REQ-022](../product/requirements.md#req-022), [REQ-023](../product/requirements.md#req-023), [REQ-024](../product/requirements.md#req-024).

**Setup/action:** Join Any level without skill; try restricted joins with missing/out-of-range levels; edit a level after joining and attempt later readmission.

**Expected:** Any level permits missing skill. Restricted admission requires a current matching per-sport declaration. Editing does not remove current participation. New join/reconfirmation/role switch checks current eligibility. No verified-rating claim.

<a id="test-004"></a>
## TEST-004 — Playing and non-playing hosts

**Covers:** [REQ-007](../product/requirements.md#req-007), [REQ-020](../product/requirements.md#req-020).

**Setup/action:** Create equivalent matches with host playing or organizing only; try playing with an ineligible level/full target role.

**Expected:** Only an eligible playing host consumes one place. Non-playing hosting consumes none and may show chosen public contacts. Host authority and allocation remain separate.

<a id="test-005"></a>
## TEST-005 — Custom sports and mixed pools

**Covers:** [REQ-019](../product/requirements.md#req-019), [REQ-025](../product/requirements.md#req-025).

**Setup/action:** Create a custom sport with general places and named-role pools; fill one role while another pool has vacancies.

**Expected:** Custom sport and mixed pools work. Each participant chooses exactly one pool; another pool's vacancy cannot overbook a full role. Total occupancy counts active players only.

<a id="test-006"></a>
## TEST-006 — Unchecked overlaps

**Covers:** [REQ-030](../product/requirements.md#req-030).

**Setup/action:** Join/reconfirm two otherwise eligible matches with overlapping scheduled times.

**Expected:** Both may succeed independently; no overlap query, warning, rejection, automatic withdrawal or overlap penalty.

<a id="test-007"></a>
## TEST-007 — Withdrawal before and after admission closes

**Covers:** [REQ-009](../product/requirements.md#req-009), [REQ-027](../product/requirements.md#req-027).

**Setup/action:** Leave before cutoff and during an ongoing match after cutoff; repeat requests; leave a pending reconfirmation.

**Expected:** Withdrawal remains possible while active. Release an allocation once; pending holds none. No automatic reopening or penalty. Profile publication is unchanged.

<a id="test-008"></a>
## TEST-008 — Compatible edits and combined-edit bypass

**Covers:** [REQ-010](../product/requirements.md#req-010), [REQ-028](../product/requirements.md#req-028).

**Setup/action:** Shrink capacity/remove an occupied role/narrow skill range beyond current players; race an edit with joining; combine incompatible edits with a time change.

**Expected:** Reject incompatible changes until explicit recorded-reason removals occur. Combined material edits cannot evade the pre-edit compatibility rule. Capacity-only editing does not retroactively evict a player because they changed their declaration.

<a id="test-009"></a>
## TEST-009 — Anonymous public contact projection

**Covers:** [REQ-004](../product/requirements.md#req-004), [REQ-011](../product/requirements.md#req-011), [REQ-014](../product/requirements.md#req-014), [REQ-026](../product/requirements.md#req-026).

**Setup/action:** Choose some methods public, others hidden. Read profile and zero-player match HTML/API/prefetch as guest, player and host.

**Expected:** Each sees selected methods only; private contact/login data is absent, not merely visually hidden. A non-playing host can publish without taking a place. Viewing requires no account, membership or recipient grant.

<a id="test-010"></a>
## TEST-010 — Publication changes and match lifecycle

**Covers:** [REQ-004](../product/requirements.md#req-004), [REQ-012](../product/requirements.md#req-012), [REQ-014](../product/requirements.md#req-014).

**Setup/action:** Hide/edit a contact and read all app-controlled public surfaces; separately leave, remove and cancel while other methods remain public.

**Expected:** New responses follow owner selection; app-controlled old projections invalidate before success. Leaving/removal/cancellation do not change profile settings. Terminal match pages show no contact/details/roster. No recall of already copied values is claimed.

<a id="test-011"></a>
## TEST-011 — External handoff and format-only checks

**Covers:** [REQ-003](../product/requirements.md#req-003), [REQ-013](../product/requirements.md#req-013), [REQ-026](../product/requirements.md#req-026).

**Setup/action:** Try valid/invalid phone, email, WhatsApp and Telegram identifiers; attempt an arbitrary/group URL; simulate unavailable external apps.

**Expected:** Format validation without ownership challenge/badge. Deliberate allowlisted actions and copy fallback use selected current values, without private prefilled data. No native chat/history or claimed delivery acknowledgment.

<a id="test-012"></a>
## TEST-012 — Competitive reconfirmation and stale expiry

**Covers:** [REQ-008](../product/requirements.md#req-008), [REQ-029](../product/requirements.md#req-029).

**Setup/action:** Reschedule with active players; race reconfirmation against a new join for the last place; apply another revision and stale confirmation/expiry.

**Expected:** Release all original allocations immediately. Pending reserves zero. Only one last-place attempt succeeds. Reject stale confirmation; stale expiry cannot remove newer participation or double-release. Playing host must reconfirm too.

<a id="test-013"></a>
## TEST-013 — Deadline boundaries and manual reopening

**Covers:** [REQ-027](../product/requirements.md#req-027), [REQ-029](../product/requirements.md#req-029).

**Setup/action:** Attempt join/reconfirm at before/equal/after cutoff; set invalid reschedule cutoffs; manually reopen before start.

**Expected:** Strictly-before succeeds if other gates pass; equality/after fail. Leaving remains allowed. New material-edit cutoff must be future and no later than revised start. Valid manual reopening is permitted; expired requests do not revive or reserve places.

<a id="test-014"></a>
## TEST-014 — Host removal, private reason and rejoin exclusion

**Covers:** [REQ-028](../product/requirements.md#req-028).

**Setup/action:** Remove with/without reason; read reason as host, removed player, other player and guest; attempt return before/after exclusion is lifted.

**Expected:** Require a nonblank reason visible only to host/removed player. Removal excludes join/reconfirm until lifted; lifting does not bypass eligibility/capacity/cutoff. Nonhosts cannot remove others; no transfer control.

<a id="test-015"></a>
## TEST-015 — In-app notice delivery and reading

**Covers:** [REQ-031](../product/requirements.md#req-031).

**Setup/action:** Generate changes/cancellation/removal/reconfirmation and host membership events; retry processing; open/mark all read; advance 30 days.

**Expected:** Private chronological list with correct unread state, no duplicate or unnecessary self-notices. Links show current state, never a reserved-place promise. No service email/push. Notices expire 30 days after creation; reading never reconfirms.

<a id="test-016"></a>
## TEST-016 — Password account and public profile boundary

**Covers:** [REQ-005](../product/requirements.md#req-005), [REQ-006](../product/requirements.md#req-006), [REQ-014](../product/requirements.md#req-014).

**Setup/action:** Browse as guest; attempt protected actions; sign in/reset password; inspect public profiles and terminal pages.

**Expected:** Email/password protects hosting/joining/editing; browsing is public. No email-verification gate. Reset email is permitted authentication mail. Public names/skills/roles/upcoming matches only, no avatar/past list. Hidden contacts/login/reset/private reasons remain private.

<a id="test-017"></a>
## TEST-017 — Offline uncertainty and reconnect

**Covers:** [REQ-016](../product/requirements.md#req-016), [REQ-008](../product/requirements.md#req-008).

**Setup/action:** Disconnect during a write and reopen the installed app offline; reconnect and retry/reconcile.

**Expected:** Offline screen, no match/contact browsing and no queued action or false success. Reconnect resolves authoritative outcome without duplicate allocation. Only safe shell assets can be cached.

<a id="test-018"></a>
## TEST-018 — Accessibility and browser matrix

**Covers:** [REQ-017](../product/requirements.md#req-017).

**Setup/action:** Run core journeys with keyboard, zoom/reflow, adopted assistive technology and exact supported browser versions.

**Expected:** Assess WCAG 2.2 AA, focus, labels, errors, contrast and responsive layout. Maps have usable list/manual-location alternatives. Record failures and actual tested versions; documentation alone is not a pass.

<a id="test-019"></a>
## TEST-019 — Retention and restore protection

**Covers:** [REQ-018](../product/requirements.md#req-018).

**Setup/action:** Advance terminal-record/notice/log age to 30 days and exercise backup expiry; restore a backup predating a deletion.

**Expected:** Purge full terminal details/roster at terminal+30 days, notices/logs at creation+30 days; backups expire within 30 days. Restore reapplies deletions before serving data. Routine logs contain no contacts/credentials. Only minimal terminal ID/state markers remain.

<a id="test-020"></a>
## TEST-020 — Global map discovery and fallback

**Covers:** [REQ-006](../product/requirements.md#req-006), [REQ-019](../product/requirements.md#req-019).

**Setup/action:** Create matches across Spain/UK and another country; deny geolocation; select manual origin and filters/radius.

**Expected:** Global creation allowed. Manual city/pin fallback works; optional device origin only on request. Approximate straight-line kilometers are labeled; all filters combine and sort by soonest start. Exact venue location is public before joining.

<a id="test-021"></a>
## TEST-021 — Closed age-design scope

**Covers:** [REQ-021](../product/requirements.md#req-021).

**Setup/action:** Inspect signup, profile, discovery, hosting and participation fields/messages.

**Expected:** No age restriction, declaration, date of birth, verification, displayed age/filter, guardian-specific flow or age-related product message.

<a id="test-022"></a>
## TEST-022 — English/Spanish and location time zone

**Covers:** [REQ-032](../product/requirements.md#req-032).

**Setup/action:** Change interface language; view from another time zone; enter nonexistent/ambiguous clock-change times.

**Expected:** English/Spanish labels/errors/notices; venue-local time/deadline with explicit zone. Do not convert primary display to viewer time. Resolve clock ambiguity/reject nonexistent times; no single offset per country or automatic authored-text translation.

<a id="test-023"></a>
## TEST-023 — Free public-only MVP boundary

**Covers:** [REQ-033](../product/requirements.md#req-033).

**Setup/action:** Inspect hosting/participation and excluded feature routes.

**Expected:** Free usage, public matches only. No private games, waitlists/auto-promotion, recurrence, competitive ratings, checkout/payment or venue booking. Self-declared skill remains distinct from ratings.

<a id="test-024"></a>
## TEST-024 — External support without moderation tools

**Covers:** [REQ-015](../product/requirements.md#req-015).

**Setup/action:** Use support and inspect absent moderation/report/block routes.

**Expected:** Open the repository GitHub Issues URL without automatically filing an issue or attaching account/contact data. No in-app report queue, personal blocking or moderation UI. Host removal and server authorization still work.

<a id="test-025"></a>
## TEST-025 — Scheduled lifecycle and terminal privacy

**Covers:** [REQ-034](../product/requirements.md#req-034), [REQ-006](../product/requirements.md#req-006), [REQ-007](../product/requirements.md#req-007), [REQ-010](../product/requirements.md#req-010).

**Setup/action:** Attempt time/location edits at start; reach end; cancel another match; open both public links and inspect full responses after purge.

**Expected:** Time/location locks at start; automatic completion at end; cancellation stays cancelled. Terminal links expose only ended/cancelled state, without details/roster/contact payloads, and disappear from discovery/profiles. Full records purge after 30 days; marker remains minimal.

<a id="test-026"></a>
## TEST-026 — Account deletion across future and current matches

**Covers:** [REQ-035](../product/requirements.md#req-035), [REQ-018](../product/requirements.md#req-018).

**Setup/action:** Delete an account with public methods, upcoming/ongoing participation, hosted matches and notices; repeat/retry and restore an old backup.

**Expected:** Immediately remove active personal data/public projections and revoke access. Withdraw/cancel every unfinished participation/hosted match, including ongoing. Release once; no orphan host/transfer. Scrub personal references, notify affected players and enforce backup expiry/erasure on restore.

<a id="test-027"></a>
## TEST-027 — Atomic role switch and playing-host eligibility

**Covers:** [REQ-036](../product/requirements.md#req-036), [REQ-020](../product/requirements.md#req-020), [REQ-025](../product/requirements.md#req-025), [REQ-008](../product/requirements.md#req-008).

**Setup/action:** Switch role before cutoff while another account takes target capacity; try after cutoff and with current skill ineligible; repeat as playing host.

**Expected:** Success moves exactly one allocation. Failure leaves old place intact; no overbooking/duplication. Cutoff/skill rules apply equally to playing host. After cutoff, switching fails but leaving remains allowed.

<a id="test-028"></a>
## TEST-028 — Input bounds and compound edits

**Covers:** [REQ-007](../product/requirements.md#req-007), [REQ-010](../product/requirements.md#req-010).

**Setup/action:** Submit missing/invalid fields, duplicate role labels, end before start, closed publication cutoff, oversized text and compound material/rule edits.

**Expected:** Apply selected defaults for required fields/bounds and plain-text handling. Future start/deadline, ordered times and valid pools are required. Material location changes have no cosmetic bypass; incompatible rule edits require explicit removals first.
