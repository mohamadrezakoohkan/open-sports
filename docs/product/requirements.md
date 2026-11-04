# Requirements and acceptance criteria

This is the current specification. **Confirmed** constraints come from the decision
log. **Proposal** and **Derived recommendation** remain visibly separate. Small defaults
selected under DEC-060 are the current baseline in [derived defaults](../decisions/derived-defaults.md);
unselected future proposals are not commitments. Acceptance criteria for confirmed behavior
are derived verification statements, not recovered historical test cases.

The latest rules supersede earlier drafts: contacts are owner-selected and public;
players may leave at any time; time/location edits free places immediately and
require competitive reconfirmation. The deadline governs joining and reconfirming.

Canonical context: [MVP](mvp.md), [contact privacy](communication-and-privacy.md),
[decisions](../decisions/decision-log.md), and [open questions](../planning/open-questions.md).
[Acceptance scenarios](../validation/acceptance-tests.md) have not been run against
a product implementation.

<a id="req-001"></a>
## REQ-001 — sports matchmaking PWA

**Status:** Confirmed product identity under [DEC-001](../decisions/decision-log.md#dec-001)
and Supabase backend selection under [DEC-061](../decisions/decision-log.md#dec-061).

Provide a browser-accessible, installable PWA for sports matchmaking. Code and documentation are AGPL-3.0-only under DEC-056. Match data/actions require connectivity under DEC-057. Support the latest two stable Chrome/Safari/Firefox/Edge versions on responsive mobile/desktop under DEC-059. Supabase is the selected backend under DEC-061; other stack choices remain deferred as described in the [architecture](../architecture/technical-overview.md).

**Acceptance criteria:**

- The product's purpose is sports matchmaking and its delivery platform is the web/PWA.
- The repository includes AGPL-3.0-only licensing and identifies source publication.
- Installation is supported; release checks cover the adopted browser matrix without assuming every browser offers identical installation UI.
- The implemented backend uses Supabase while preserving the requirements below;
  record provider configuration and release evidence under [TEST-029](../validation/acceptance-tests.md#test-029).

<a id="req-002"></a>
## REQ-002 — instant public joining

**Status:** Confirmed; [DEC-002](../decisions/decision-log.md#dec-002), [DEC-007](../decisions/decision-log.md#dec-007), [DEC-009](../decisions/decision-log.md#dec-009).

A signed-in eligible user can instantly join an available public match place without host approval, before admission closes.

**Acceptance criteria:**

- A successful join immediately creates participation, with no pending host-approval queue.
- Guests must sign in to join. Skill restrictions and selected role availability are enforced.
- A full match or closed admission does not accept a new playing allocation.
- Contact viewing is public and does not require joining.

<a id="req-003"></a>
## REQ-003 — external-only participant chat

**Status:** Confirmed; [DEC-003](../decisions/decision-log.md#dec-003).

MVP participant conversation happens externally. Service notifications are covered by REQ-031.

**Acceptance criteria:**

- There is no native participant inbox, chat composer, message history, or read receipt.
- External handoff does not claim a message has been delivered.
- In-app service notifications are not exposed as a participant conversation channel.

<a id="req-004"></a>
## REQ-004 — optional owner-controlled contact publication

**Status:** Confirmed; [DEC-004](../decisions/decision-log.md#dec-004) as refined by [DEC-023](../decisions/decision-log.md#dec-023)/024.

Owners explicitly choose which contact methods to display publicly and can hide or change them. Joining and hosting do not themselves authorize publication.

**Acceptance criteria:**

- A person may have no published contact methods.
- Adding a method does not publish it without the owner's explicit selection.
- Publishing one's own method does not publish anyone else's method.
- An authentication identifier is not automatically a public contact.

<a id="req-005"></a>
## REQ-005 — email/password accounts and upcoming-only profiles

**Status:** Confirmed: [DEC-037](../decisions/decision-log.md#dec-037), [DEC-038](../decisions/decision-log.md#dec-038) as refined by [DEC-044](../decisions/decision-log.md#dec-044), and [DEC-045](../decisions/decision-log.md#dec-045).

Use email/password accounts for hosting, joining and editing profiles. No email-verification step. Provide email password reset. Profiles expose display name, sport-specific skill, contextual roles and upcoming matches only; no avatars or past-match lists. Public-contact selection remains separate.

**Acceptance criteria:**

- Guests can browse but must sign in for hosting, joining or profile edits.
- No avatar input/upload or public past-match history exists.
- Password reset uses authentication email; service-notification email remains excluded.
- Verify reset delivery to an ordinary user outside the Supabase project team;
  resolve [Q-020](../planning/open-questions.md#q-020) before public launch.
- No email-verification gate prevents ordinary account use.
- Private authentication/recovery fields do not appear publicly unless independently selected as contacts.
- Derived recommendation: reset tokens are single-use, expire and do not expose account existence.

<a id="req-006"></a>
## REQ-006 — public map discovery and details

**Status:** Confirmed: [DEC-038](../decisions/decision-log.md#dec-038)–040, [DEC-044](../decisions/decision-log.md#dec-044), [DEC-046](../decisions/decision-log.md#dec-046), [DEC-050](../decisions/decision-log.md#dec-050).

Discover public upcoming matches using map/distance, city, sport, date, skill range and available-place controls, sorted by soonest start. Use optional device location or a visitor-selected city/map point for distance. Exact pin/venue/address/city, names, skill and roles are public. Profiles show upcoming participation only.

**Acceptance criteria:**

- Denying/unavailable geolocation does not block browsing; manual origin remains available.
- All selected filters work with soonest-start order, not an implied proximity ranking.
- Exact location and selected contacts are visible before joining.
- No past/cancelled matches appear in discovery or profile lists.
- Completed/cancelled direct links show only the terminal state, without match details, roster or contacts.
- Derived recommendation: upcoming profile lists contain active future participation, not pending/left/removed records.

<a id="req-007"></a>
## REQ-007 — host a scheduled public match

**Status:** Confirmed core fields: [DEC-006](../decisions/decision-log.md#dec-006), [DEC-011](../decisions/decision-log.md#dec-011)/012, [DEC-035](../decisions/decision-log.md#dec-035), [DEC-040](../decisions/decision-log.md#dec-040) and [DEC-043](../decisions/decision-log.md#dec-043).

Signed-in hosts choose a sport, public map pin with venue/address/city, start/end times, general/role capacities, skill range or Any level, and admission deadline. End follows start. The host chooses whether to play.

**Acceptance criteria:**

- Required start/end and location fields are present; end is later than start.
- Admission deadline is no later than start.
- General/role pools determine playing capacity; only a playing host occupies a place.
- Time/location edits are rejected once the match has started.
- Optional title/description are a derived UX recommendation, not additional required fields.

<a id="req-008"></a>
## REQ-008 — reliable capacity and joining

**Status:** Derived recommendation; instant admission and role availability are Confirmed.

Use authoritative, atomic admission with one playing allocation per person per match, safe retries, and consistent total/role capacity.

**Acceptance criteria:**

- Two simultaneous attempts for the last place cannot both succeed.
- A retry after an uncertain response cannot duplicate one person's allocation.
- Recheck eligibility, capacity, deadline, and current match version at commit.
- Reconfirmation and a new join compete for the same current inventory.

<a id="req-009"></a>
## REQ-009 — leave participation

**Status:** Confirmed; [DEC-032](../decisions/decision-log.md#dec-032).

Players may leave at any time. The admission deadline does not restrict withdrawal. Contact publication remains independent.

**Acceptance criteria:**

- A player can withdraw before or after the join/reconfirm deadline.
- Leaving releases their current allocation once; leaving a pending reconfirmation releases none.
- Late leaving does not reopen joining automatically.
- Leaving does not hide their public profile contacts.
- Selected derived default: repeat withdrawal requests are harmless. Completed/cancelled matches are terminal, without active participation to withdraw.

<a id="req-010"></a>
## REQ-010 — edit or cancel a match

**Status:** Confirmed powers and edit rules; [DEC-022](../decisions/decision-log.md#dec-022), [DEC-026](../decisions/decision-log.md#dec-026), [DEC-033](../decisions/decision-log.md#dec-033).

Hosts may edit and cancel. Time/location changes require the release/reconfirmation flow in REQ-029. Capacity, role and skill-range edits must leave all current players eligible and accommodated.

**Acceptance criteria:**

- An incompatible capacity/role/skill edit is rejected until affected players have been explicitly removed with recorded reasons.
- A compatible edit does not silently remove or reassign an existing player.
- Time/location changes use reconfirmation, including when other fields change in the same edit.
- Cancellation makes the match unavailable for new joins/reconfirmation.
- Match cancellation does not change users' public profile contact settings.
- Selected derived default: repeated cancellation is harmless; completed/cancelled matches cannot be edited or reopened.

<a id="req-011"></a>
## REQ-011 — public contact visibility

**Status:** Confirmed; [DEC-023](../decisions/decision-log.md#dec-023).

Display selected contacts on users' profiles and match pages to everyone, including anonymous visitors, without membership or named-recipient grants. Canonical details are in communication-and-privacy.md.

**Acceptance criteria:**

- An anonymous visitor can see selected host methods on a zero-player match.
- A person can see selected profile methods without joining any match.
- Membership and hosting do not unlock unpublished contacts.
- A non-playing host can publish methods without taking a place.
- No per-recipient consent step or reciprocal grant is required.

<a id="req-012"></a>
## REQ-012 — hide and edit published contacts

**Status:** Confirmed owner controls; [DEC-024](../decisions/decision-log.md#dec-024). Lifecycle consequences are derived.

The owner can hide, change, or remove methods. There is no scheduled expiry. Published values are current profile data, not copied into match memberships.

**Acceptance criteria:**

- Subsequent public responses omit a hidden or removed value and use an updated value.
- Unaffected methods keep their own visibility settings.
- Leaving, removal, completion, and cancellation do not change the profile publication setting.
- Blocking is not represented as preventing anonymous access to still-public methods.
- UI does not claim to recall contact details already copied externally.

<a id="req-013"></a>
## REQ-013 — external contact handoff and format validation

**Status:** Confirmed methods and format-only validation: [DEC-016](../decisions/decision-log.md#dec-016) and [DEC-045](../decisions/decision-log.md#dec-045). Launch/copy details are Derived recommendations.

Validate formats of phone, email, WhatsApp and Telegram methods without ownership verification. Participant conversations remain external.

**Acceptance criteria:**

- Invalid formats are rejected with a correctable field error.
- Do not require ownership challenges, provider sign-in or verified-owner badges.
- Recommended: deliberate contact actions use allowlisted routes/schemes and current published values.
- Recommended: provide copy fallback when an external app cannot open.
- Opening an external destination is not proof a message was sent; no conversation content is stored.

<a id="req-014"></a>
## REQ-014 — field-level public/private data boundary

**Status:** Derived recommendation implementing explicit publication consent.

Return published fields to public viewers, keep unpublished fields private, and authorize owner writes on the server.

**Acceptance criteria:**

- Anonymous HTML/API responses contain selected methods but no unpublished contact values, private sign-in identifiers, or recovery data.
- Private data is not merely hidden with presentation code.
- Nonowners cannot change contact values or publication choices.
- Logs, error payloads and routine analytics avoid raw contact values and contact-bearing URLs.
- Selected default: contact/profile data is not served from an offline or stale public projection; hide/edit/delete invalidates app-controlled projections before success is acknowledged.

<a id="req-015"></a>
## REQ-015 — external support; no in-app reporting or moderation tools

**Status:** Confirmed: [DEC-047](../decisions/decision-log.md#dec-047) and [DEC-051](../decisions/decision-log.md#dec-051). Host removal remains Confirmed separately.

Provide an external support link to https://github.com/mohamadrezakoohkan/open-sports/issues. Exclude in-app reports, moderation tools and personal blocking from MVP.

**Acceptance criteria:**

- The support action opens the repository's GitHub Issues page.
- Opening support does not file an issue or automatically attach contacts/account data.
- No report queue, personal-block flow or admin moderation UI is included.
- Host removal with recorded reason and its match-specific rejoin exclusion still work.
- Server authorization and privacy controls remain required boundaries, not moderation features.

<a id="req-016"></a>
## REQ-016 — installation and online-only match data

**Status:** Confirmed by [DEC-057](../decisions/decision-log.md#dec-057); retry/caching enforcement details are derived recommendations.

Support installation. When offline, show an offline screen; require a connection for match data and all actions. Do not offer cached match browsing or queued offline writes.

**Acceptance criteria:**

- No offline or timed-out request is shown as confirmed participation without authoritative success.
- An uncertain join can be reconciled without duplicating an allocation.
- No match/contact-bearing page is available as an offline browsing cache.
- A static shell/offline message may be cached without match/account data.
- Reconnect before reading current availability or performing any action.

<a id="req-017"></a>
## REQ-017 — accessibility and supported browsers

**Status:** Confirmed target under [DEC-059](../decisions/decision-log.md#dec-059); verification details are selected derived defaults.

Target WCAG 2.2 AA for core flows under DEC-059. Support responsive mobile/desktop and the latest two stable Chrome/Safari/Firefox/Edge versions. Documentation does not establish conformance.

**Acceptance criteria:**

- Verify keyboard and assistive-technology paths cover discovery, joining, reconfirmation, hosting and privacy settings.
- Errors identify the field and resolution; state is not conveyed only by color.
- Verify focus, labels, contrast, and responsive layout are checked manually as well as automatically.

<a id="req-018"></a>
## REQ-018 — data lifecycle and operation

**Status:** Confirmed deletion/retention under [DEC-048](../decisions/decision-log.md#dec-048), [DEC-052](../decisions/decision-log.md#dec-052) and [DEC-054](../decisions/decision-log.md#dec-054); operating mechanisms are selected derived defaults, with vendor sizing deliberately deferred.

Delete account personal data immediately, withdraw all unfinished participation, and cancel all unfinished hosted matches. See REQ-035. Delete completed/cancelled match records and notifications after 30 days; backups expire within 30 days.

**Acceptance criteria:**

- Confirmed: public profile/contact responses stop exposing the deleted account immediately.
- Confirmed: all unfinished playing places are released and all unfinished hosted matches cancelled.
- Confirmed: delete account personal data immediately in active storage; backup copies expire within 30 days.
- Confirmed: match records are deleted 30 days after completion/cancellation and notifications 30 days after creation; clock anchors are derived details.
- Selected default: restoration must not resurrect later deletion or public-visibility choices.
- Selected default: diagnose failed state changes without raw contacts in routine logs.
- No measured availability/performance is claimed; restore must not make deleted personal data live again.
- Verify the deployed provider's backups, paused-project snapshots and restoration
  against the same retention bounds; [Q-019](../planning/open-questions.md#q-019)
  remains Open until evidence supports them. Backend selection is not a waiver.

<a id="req-019"></a>
## REQ-019 — any sport and global locations with Spain/UK/Netherlands pilot focus

**Status:** Confirmed: [DEC-005](../decisions/decision-log.md#dec-005), [DEC-035](../decisions/decision-log.md#dec-035), [DEC-049](../decisions/decision-log.md#dec-049) and the expansion in [DEC-062](../decisions/decision-log.md#dec-062).

Support a searchable sport list plus custom sports. Cities across Spain, the United
Kingdom and the Netherlands are the pilot focus; other countries are allowed.

**Acceptance criteria:**

- No single-sport restriction or handpicked city shortlist is imposed.
- Hosts can choose a listed sport or enter a custom one.
- Hosting/discovery supports cities across Spain, the UK and the Netherlands;
  no selected-city shortlist narrows the pilot scope.
- Hosting outside those three countries is not rejected by a geographic allowlist.
- Time-zone/location modeling supports the chosen venue rather than assuming one pilot-country offset.

<a id="req-020"></a>
## REQ-020 — optional playing host

**Status:** Confirmed; [DEC-006](../decisions/decision-log.md#dec-006).

The host chooses whether to play. Only playing participants occupy capacity.

**Acceptance criteria:**

- A non-playing host does not reduce available playing places.
- A playing host occupies one available general or appropriate role place.
- Host control and playing participation are separate concepts.
- A playing host follows the same current skill/role admission rules under DEC-058.
- Joining/leaving as a player does not itself transfer host authority.

<a id="req-021"></a>
## REQ-021 — no age-specific product flow

**Status:** Confirmed; [DEC-013](../decisions/decision-log.md#dec-013)/014/017; closed.

Allow all ages with no age restrictions or age-related product messaging. The former adults-only requirement is superseded.

**Acceptance criteria:**

- No age declaration, date-of-birth field, age verification, displayed age, or age filter is introduced.
- No age-specific guardian account flow or product messaging is added.
- Host-defined eligibility does not introduce age restrictions.

<a id="req-022"></a>
## REQ-022 — host eligibility limited to skill and role

**Status:** Confirmed; [DEC-009](../decisions/decision-log.md#dec-009).

Host-selected admission criteria are sport-specific skill level and playing position/role only.

**Acceptance criteria:**

- A host can specify the supported skill range and available role places.
- No additional personal criteria are exposed as host eligibility rules.
- Sign-in, available capacity, match state and admission deadline are system conditions, not extra host-selected personal criteria.

<a id="req-023"></a>
## REQ-023 — self-declared sport-specific skill

**Status:** Confirmed; [DEC-010](../decisions/decision-log.md#dec-010).

Players declare skill separately for each sport; no automatic rating or verification is adopted. Under DEC-034, a declaration is required only for a skill-restricted match and may be edited at any time without removing existing participation.

**Acceptance criteria:**

- A person's football level does not automatically set their tennis level.
- A declared value is described as self-declared, not independently verified.
- Any-level admission accepts a missing level; restricted admission requires a current matching level.
- Editing a level does not remove current participation. A later join/reconfirmation uses the current declaration.

<a id="req-024"></a>
## REQ-024 — skill scale and host range

**Status:** Confirmed; [DEC-011](../decisions/decision-log.md#dec-011).

Player values are Beginner, Intermediate, and Advanced. Hosts choose an inclusive allowed range or Any level.

**Acceptance criteria:**

- A single selected level and a contiguous multi-level range can be represented.
- Any level is a host admission setting, not a fourth player rating.
- Admission compares the sport-specific declaration to the selected range.
- Any-level matches accept missing declarations under DEC-034; restricted matches do not.

<a id="req-025"></a>
## REQ-025 — role-specific and general places

**Status:** Confirmed; [DEC-012](../decisions/decision-log.md#dec-012) and [DEC-035](../decisions/decision-log.md#dec-035).

Hosts can combine general and role-specific places in one match. Role names are host-defined. Players select one available general or named-role place when joining.

**Acceptance criteria:**

- A role-specific place is unavailable once its allotted capacity is occupied.
- A player selects an available role when that match uses role-specific places.
- A general-place match does not require a playing-role selection.
- Mixed general and role-specific pools are supported, with one allocation in one pool per player.
- Role labels are host-defined; capacity-safe role switching before the deadline is supported under DEC-058 and REQ-036.

<a id="req-026"></a>
## REQ-026 — four optional contact methods

**Status:** Confirmed: [DEC-016](../decisions/decision-log.md#dec-016), [DEC-023](../decisions/decision-log.md#dec-023)/024 and [DEC-045](../decisions/decision-log.md#dec-045).

Support phone, email, WhatsApp and Telegram as independently selected public methods. Validate formats only, without verifying ownership.

**Acceptance criteria:**

- All four types are supported; none is mandatory.
- Publishing phone does not automatically publish WhatsApp, or vice versa.
- Authentication email is not automatically the displayed email.
- A valid format does not receive a verified-owner claim or require a possession challenge.

<a id="req-027"></a>
## REQ-027 — shared admission deadline

**Status:** Confirmed; [DEC-025](../decisions/decision-log.md#dec-025)/029 as revised by [DEC-032](../decisions/decision-log.md#dec-032).

The host sets one deadline for joining and reconfirming, no later than match start. Leaving is unrestricted. After a time/location change, the replacement deadline must be in the future and no later than the revised start.

**Acceptance criteria:**

- The same deadline gates new joins and reconfirmations.
- Leaving works after the deadline.
- An edit cannot retain a deadline after the revised start.
- A material edit must set a valid future deadline.
- Selected derived default under DEC-060: admission is allowed strictly before the deadline; the authoritative clock closes admission at equality.

<a id="req-028"></a>
## REQ-028 — host management powers

**Status:** Confirmed; [DEC-022](../decisions/decision-log.md#dec-022)/033.

The host can edit details, cancel, and remove players with a recorded reason. MVP does not support host transfer.

**Acceptance criteria:**

- Removal requires a recorded reason and releases any occupied place once.
- A non-host cannot obtain these powers merely by joining.
- Capacity, roles and skill edits preserve all current players or require explicit removals first.
- No host-transfer control is provided.
- Under DEC-036, removal blocks rejoining/reconfirming that match until the host explicitly lifts the exclusion.
- Lifting an exclusion does not automatically reinstate the player or bypass normal admission rules.
- Under DEC-053, the reason is visible only to the host and removed player; other participants and anonymous visitors cannot read it.

<a id="req-029"></a>
## REQ-029 — material edit and reconfirmation

**Status:** Confirmed; [DEC-026](../decisions/decision-log.md#dec-026), [DEC-028](../decisions/decision-log.md#dec-028)/029/030.

When time or location changes after people join, immediately release existing playing places and require everyone to reconfirm against the revised match. Pending players hold no reservation. The host sets a new shared admission deadline; unanswered reconfirmations close automatically at it.

**Acceptance criteria:**

- The edit releases all current allocations and records who needs to reconfirm, without reserving their places.
- A reconfirmation competes with new joins under current skill, role, capacity and deadline conditions.
- If places fill first, reconfirmation cannot overbook; prior participation gives no priority.
- At deadline, a pending nonresponse closes without decrementing capacity a second time.
- An older pending expiry cannot remove a person who has successfully reconfirmed.
- A non-playing host has no playing allocation to release; a playing host is included in the everyone rule.
- Derived recommendation: version edits and reconfirmations so acceptance of old details cannot confirm a later revision.

<a id="req-030"></a>
## REQ-030 — overlapping matches allowed

**Status:** Confirmed; [DEC-027](../decisions/decision-log.md#dec-027).

Allow participation in overlapping scheduled matches without checking or warning.

**Acceptance criteria:**

- Admission and reconfirmation do not reject or warn on another match's scheduled overlap.
- No automatic withdrawal or overlap-based penalty is introduced.
- Independent eligibility, place availability and deadline conditions still apply.

<a id="req-031"></a>
## REQ-031 — in-app service notification list

**Status:** Confirmed; [DEC-031](../decisions/decision-log.md#dec-031).

Show match changes, cancellations, removals and reconfirmation requests in an in-app notification list. No service email or browser push in MVP.

**Acceptance criteria:**

- Each relevant affected user can find the event in their in-app list.
- Reconfirmation notices link to current details, deadline and current place availability without promising a reserved place.
- There is no email or browser-push delivery of these match service events.
- Creation of a notice is not described as proof of reading or successful external contact.
- Selected derived defaults: use event IDs against duplicates; reverse chronological list with unread/read state, open-to-mark-read and mark-all-read.
- Delete notifications 30 days after creation under DEC-054.

<a id="req-032"></a>
## REQ-032 — languages and local match time

**Status:** Confirmed; [DEC-041](../decisions/decision-log.md#dec-041), extended by
[DEC-062](../decisions/decision-log.md#dec-062).

Support English, Spanish and Dutch. Show each match in its venue-local time with its time zone.

**Acceptance criteria:**

- Core interface labels, validation messages and service notices have English,
  Spanish and Dutch variants.
- Apply the [language-selection default](../decisions/derived-defaults.md#discovery-and-localization)
  to all three supported languages, retaining a manual switch and English fallback.
- Match time and admission deadline are presented in the match location's time zone, explicitly identified.
- The primary time display does not silently change to the viewer's time zone.
- Derived recommendation: store an unambiguous instant and location time-zone identifier; handle seasonal clock changes and distinct zones within a country.
- User-entered sport, role, venue or description text is not promised automatic translation.

<a id="req-033"></a>
## REQ-033 — free public-only MVP

**Status:** Confirmed; [DEC-042](../decisions/decision-log.md#dec-042).

MVP is free to use and includes public matches only. Private games, waitlists, recurring games, ratings, payments and venue booking are deferred.

**Acceptance criteria:**

- No payment is required to use MVP hosting or participation.
- No private-game, waitlist, recurring-game, rating, checkout or venue-booking flow is provided in MVP.
- A full match cannot create an implied queue or automatic promotion.
- Self-declared skill remains supported and is not represented as a verified or competitive rating.

<a id="req-034"></a>
## REQ-034 — scheduled lifecycle and terminal pages

**Status:** Confirmed: [DEC-043](../decisions/decision-log.md#dec-043) and [DEC-050](../decisions/decision-log.md#dec-050).

Require start/end. Lock time/location edits once started; automatically mark ended matches completed. Completed/cancelled pages show only “Match ended” or “Match cancelled”, with no match details or roster.

**Acceptance criteria:**

- Time/location edits from a stale client fail at or after start.
- A match automatically becomes completed at end; a cancelled match stays cancelled.
- Completed/cancelled matches disappear from discovery and profile upcoming lists.
- Direct terminal-page responses omit details, roster and contact values, including embedded payloads.
- Derived recommendation: retain a minimal terminal-state identifier independently of any later record-purge policy.


<a id="req-035"></a>
## REQ-035 — account deletion effects

**Status:** Confirmed: [DEC-048](../decisions/decision-log.md#dec-048), [DEC-052](../decisions/decision-log.md#dec-052), [DEC-054](../decisions/decision-log.md#dec-054).

Immediately delete account personal data and hide profile/contacts, withdraw participation in every unfinished match and cancel every unfinished hosted match, including ongoing ones.

**Acceptance criteria:**

- Public profile/contact reads stop exposing the deleted account immediately.
- Release unfinished allocations once; non-playing hosts do not release nonexistent places.
- Cancel unfinished hosted matches without host transfer or orphaning an active event.
- Affected players receive normal in-app cancellation notices.
- Active personal account data is deleted immediately; backup copies expire within 30 days.
- Derived recommendation: delete/anonymize personal references in retained match/notices/audit data and reapply erasures before restored data is served.

<a id="req-036"></a>
## REQ-036 — atomic role switching before cutoff

**Status:** Confirmed behavior under [DEC-058](../decisions/decision-log.md#dec-058); transaction details are selected derived defaults under DEC-060.

A player, including a playing host, may switch to an available role/general place before the admission deadline while preserving capacity.

**Acceptance criteria:**

- A successful switch transfers exactly one allocation from the old pool to the new pool.
- An unavailable target, unmet current skill rule or closed deadline leaves the old allocation unchanged.
- Switching does not create duplicate participation or exceed either pool's capacity under concurrent joins.
- At/after cutoff, reject switching while continuing to allow leaving.
