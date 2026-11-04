# Player and host journeys

These journeys apply confirmed rules and the selected derived defaults under DEC-060.
They are designed flows, not recovered historical wireframes or implemented UI.
Requirements remain canonical; see [MVP](mvp.md) and [acceptance scenarios](../validation/acceptance-tests.md).

<a id="j-001"></a>
## J-001 — discover and inspect a match

1. A visitor opens map/distance discovery with city, sport, date, skill and
   available-place controls, sorted by soonest start.
2. Open a public match page and inspect sport, location, schedule, capacity,
   admission conditions and deadline. Names, skills and roles are public; profiles
   show upcoming matches only, with no avatars. Exact location is public.
3. View any owner-selected public contact methods, even with no account and before
   anyone joins. Contact access does not consume capacity.
4. Choose whether to sign in and join. Publishing a contact is optional.

Empty, full, cancelled and admission-closed presentations must be distinguishable
under the selected UX defaults. Do not use public contact visibility as a reason to expose
private sign-in information.

<a id="j-002"></a>
## J-002 — instant join

1. Sign in with email/password if needed; no email-verification gate. Email reset
   is available for a forgotten password.
2. For a restricted match, declare the sport-specific skill and meet the allowed
   range. Any-level matches accept a missing level.
3. Select an available general or host-named role place.
4. Submit the join. Current eligibility, removal exclusion, capacity and deadline
   must be checked authoritatively under the recommended implementation.
5. Show active participation on success, without host approval.

A host who removed this person must explicitly lift the match-specific exclusion
before another join is allowed. Another match at an overlapping time causes no
check or warning. A simultaneous last-place race may fail without overbooking;
network uncertainty must not be displayed as confirmed success.

<a id="j-003"></a>
## J-003 — host a match, with or without playing

1. Choose a listed sport or enter a custom sport.
2. Supply match details and a host-set admission deadline no later than start.
   Choose a map pin and venue/address/city; require start and end, with end after start.
3. Configure general and/or named-role places and an allowed skill range or Any level.
4. Choose whether to play. If playing, meet ordinary skill/role rules and occupy
   a suitable place; otherwise consume none.
5. Publish through the hosting flow after reviewing the public details.
6. Manage details, cancellation and removals. Host transfer is outside MVP.

Publishing does not automatically publish a host's contact. A zero-player match
can display the host's already-selected public contact methods.

<a id="j-004"></a>
## J-004 — choose public contact methods and communicate externally

1. Open own contact settings and add any supported methods.
2. Explicitly choose which methods to display publicly.
3. Visitors see selected methods on profile and relevant match surfaces without
   joining or signing in. There is no individual recipient approval.
4. A visitor deliberately opens call/email/chat or copies the selected value,
   following the selected external-link defaults. Format checks do not verify ownership.
5. Owner hides or edits a method. Subsequent public responses follow the new setting.

Already copied contact values cannot be recalled. Leaving, removal or cancellation
does not change public profile settings. See [contact privacy](communication-and-privacy.md).

<a id="j-005"></a>
## J-005 — leave, remove, and permit rejoining

A player may leave at any time, including after the admission deadline. Release
any current allocation once. A late departure does not reopen joining.

A host may remove a player with a recorded reason. Release the allocation and
prevent the person joining/reconfirming that match until the host explicitly lifts
the exclusion. A lifted exclusion does not guarantee a place or bypass the deadline.

The removed person receives an in-app notice. Only that person and the host can
read the reason. Before cutoff, players can atomically switch to an eligible
available role; a failed switch preserves the old place. No automatic penalties.

<a id="j-006"></a>
## J-006 — change time/location and reconfirm

1. Before start, host selects a new time or location and a new shared join/reconfirm deadline:
   in the future and no later than the revised start.
2. Commit revised details and immediately release all current playing places.
3. Existing players receive in-app reconfirmation requests. Pending status reserves
   no place; the match can accept new eligible joins.
4. A previous player reads current details and tries to reconfirm. They compete
   with new joins under current conditions.
5. If a place is available and admission succeeds, participation becomes active.
   If full or ineligible, no allocation is created.
6. At deadline, close remaining unanswered requests automatically. Their places
   were already released; no second capacity decrement occurs.

A playing host is included in the participation rule. A non-playing host has no
playing allocation. Recommended revision handling prevents reconfirmation of stale
details or a stale expiry from removing a newer allocation.

<a id="j-007"></a>
## J-007 — edit capacity, roles, skill range, or cancel

For capacity/role/skill-range edits, preserve every current player's fit. Reject an
incompatible edit until the host explicitly removes affected players with reasons.
Do not silently evict or reassign them.

Cancellation stops future admission and generates in-app service notifications.
It does not hide profile contacts. At end the match completes automatically.
Completed/cancelled links show state only, without details/roster/contacts, and are
removed from discovery/profile lists. Full terminal records expire after 30 days.

<a id="j-008"></a>
## J-008 — check service notifications

A signed-in person visits their in-app notification list for match changes,
cancellations, removals and reconfirmation requests. There is no email or push
delivery of these service events in MVP.

A notification links to current state, not an assumed still-available place.
A missed reconfirmation may expire even if the notification was never read.
Opening marks a notice read; mark-all-read is available. Notices expire after
30 days. Host notices include joins, withdrawals and role switches under the
selected defaults; no contact values are copied into notice payloads.

<a id="j-009"></a>
## J-009 — change skill

Declare or edit a level separately for each sport. Changing it does not remove
existing participation. Future joins/reconfirmations use the current declaration
when the match restricts skill. Any-level matches do not require a level.

No verification, competitive rating, automatic matching or cross-sport level
propagation is implied.

<a id="j-010"></a>
## J-010 — delete an account

Confirm account deletion with an authenticated owner action. Immediately delete
active personal account data, hide profile/contacts, revoke access, withdraw from
all unfinished participation and cancel all unfinished hosted matches, including
ongoing matches. Release allocations once and issue normal in-app cancellation
notices to affected players. There is no transfer or hostless active match.

Erase/anonymize personal references in retained service data. Backups expire
within 30 days; restoration must apply erasures before serving data. This is
separate from public terminal pages showing only ended/cancelled state.

<a id="j-011"></a>
## J-011 — offline use and external support

Install the PWA through supported browser/platform affordances. Offline, show
the offline screen; do not browse cached match/contact data or queue actions.
After reconnecting, reconcile uncertain requests against authoritative state.

The support action opens the repository's GitHub Issues page. It does not create
an issue or attach personal data automatically; there is no in-app report/block
or moderation workflow.
