# Vision, users, and principles

## Product identity — Confirmed

An open-source sports matchmaking PWA for any sport, piloting across all cities in
Spain, the United Kingdom and the Netherlands. Matches in other countries remain
allowed. The interface supports English, Spanish and Dutch; the Netherlands and
Dutch scope extension is [DEC-062](../decisions/decision-log.md#dec-062). Hosts can
organize with or without playing. Eligible, signed-in players instantly join public
matches. Playing places can be general or host-named roles; skill is self-declared
separately for each sport.

Participant chat is external. Owners may publish phone, email, WhatsApp and Telegram
methods on profiles and match pages for anyone to view, including anonymous visitors.
Publication is optional and owner-controlled, independent of joining.

The product has no age restrictions, age-specific account flow, displayed ages,
age filters or age-related product messaging. The former adults-only selection
was explicitly superseded and this design topic is closed.

The [decision log](../decisions/decision-log.md) preserves exact choices and
supersessions. MVP is free and public-only; later monetization, final brand and
competitive positioning are uncommitted future topics, not invented market claims.
“Matchmaking” does not establish automatic player pairing.

## Working vision — Derived recommendation

Help people find opportunities to play sport, fill playing places, and coordinate
externally while controlling which contact details they make public.

This is a synthesis of current decisions, not a recovered mission statement or
validated market proposition.

## User hypotheses — Proposal

| Role or situation | Need to validate | Relevant behavior |
|---|---|---|
| Player seeking a game | Find a suitable place at a useful time/location | Public discovery, skill/role eligibility, instant join |
| Organizer | Fill places and manage changes without having to play | Optional participation, edits, cancellation, removals |
| Player wanting control over contact exposure | Choose whether and what to publish | Per-method public visibility settings independent of joining |
| Player affected by a reschedule | Understand changed details and whether a place remains | In-app notice, competitive reconfirmation, explicit deadline |
| Occasional visitor | Inspect a match before creating an account | Public pages and selected contact methods |
| Maintainer/operator | Understand product intent and run a coherent service | Source-linked decisions, documented invariants and operations |

These are role hypotheses, not research-backed personas. No interviews, market
size, measured conversion, or validated demand is claimed.

## Principles

| Principle | Status | Implication |
|---|---|---|
| Instant public joining | Confirmed | No host-approval queue for eligible public joins |
| External MVP conversation | Confirmed | No native participant chat |
| Explicit public-contact choice | Confirmed | Adding/joining does not automatically publish contacts |
| Playing capacity is separate from organizing | Confirmed | Non-playing hosts consume no place |
| Participation is revisable | Confirmed | Players may leave at any time |
| Rescheduling requires renewed participation | Confirmed | Release places and require competitive reconfirmation |
| Clear authoritative outcomes | Derived recommendation | Never present a failed/offline mutation as success |
| Preserve evidence and changes | Documentation requirement | Retain sources, statuses and superseded decisions |

## Trade-offs and hypotheses

Public contacts permit pre-join coordination but can be copied by anyone who sees
them. Hiding them later changes app publication, not external copies. Optional
publication means some matches may have no external contact path.

Immediate joining removes host approval but requires reliable capacity and clear
eligibility. Rescheduling without reservations lets new players fill places while
previous players may lose theirs. In-app-only service notifications may be missed.
Allowing overlapping matches leaves scheduling responsibility with players.

These are derived implications, not recovered historical rationale or measured
results. [Roadmap hypotheses](../planning/roadmap.md) describe ways to validate them.
