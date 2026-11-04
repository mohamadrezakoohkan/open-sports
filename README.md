# Open Sports — product documentation

A complete current product specification for an open-source sports matchmaking PWA.
**Open Sports is a working name derived from the repository, not recovered branding.**
This package documents the product; it contains no application implementation.

The owner resolved the product choices and delegated remaining small defaults.
**Historical coverage remains partial:** five original user turns were retrieved,
but four assistant reply bodies and earlier conversation history were unavailable.
Current decisions do not recover that missing history. See [source coverage](docs/sources/recovery-status.md).

## Read first

- [Vision, users and principles](docs/product/vision-and-principles.md)
- [MVP scope](docs/product/mvp.md) and [requirements with acceptance criteria](docs/product/requirements.md)
- [Contact publication/privacy](docs/product/communication-and-privacy.md)
- [Journeys](docs/product/journeys.md) and [UX](docs/product/ux.md)
- [Decision history](docs/decisions/decision-log.md) and [selected derived defaults](docs/decisions/derived-defaults.md)
- [Domain model](docs/architecture/domain-model.md), [architecture](docs/architecture/technical-overview.md), [quality/security](docs/architecture/security-and-nonfunctional.md)
- [Resolved questions and deliberate deferrals](docs/planning/open-questions.md), [roadmap](docs/planning/roadmap.md)
- [Validation](docs/validation/validation-report.md), [traceability](docs/validation/traceability.md), [delivery](docs/delivery.md)
- [Complete document index](docs/README.md)

## Current product baseline

| Area | Behavior |
|---|---|
| Scope | Free public-match PWA; any sport; Spain/UK pilot focus, other countries allowed |
| Accounts | Email/password, no email verification; email password reset |
| Public profile | Display name, per-sport skill, contextual roles, upcoming matches; no avatar or past-match list |
| Discovery | Map/distance, city, sport, date, skill, available places; soonest-start sort |
| Location | Public exact map pin plus venue/address/city; optional device origin or manual city/pin for distance |
| Joining | Signed-in, eligible, instant; no host approval; overlapping matches allowed without checks |
| Skill/places | Beginner/Intermediate/Advanced; host range or Any level; general and custom-role places can mix |
| Skill edits | Missing skill allowed for Any level; changing skill does not remove existing participation |
| Host | May organize without playing; playing host uses a place and ordinary eligibility |
| Deadline | One join/reconfirm deadline no later than start; leaving allowed anytime while participation is active |
| Role switch | Available before cutoff, capacity-safe; failure preserves the old place |
| Material edits | Before start, time/location edits release all places and require competitive reconfirmation by a new future deadline |
| Other edits | Capacity/role/skill-rule edits preserve every current player or require explicit removal first |
| Host controls | Edit, cancel, remove with reason; reason private to host/removed player; rejoin excluded until host lifts it; no transfer |
| Completion | Required start/end; time/location locked at start; auto-complete at end; terminal URLs show state only |
| Contacts | Owner-selected phone/email/WhatsApp/Telegram public on profiles and active match pages, including anonymous pre-join access; format checks only |
| Communication | External participant chat; in-app-only service notification list |
| Support | External GitHub Issues; no in-app reports, moderation or personal blocking |
| Deletion/retention | Immediate personal-data deletion; withdraw/cancel all unfinished matches; terminal details/notices expire after 30 days; backups within 30 days |
| Language/time | English/Spanish; match-local time with explicit zone |
| PWA/quality | Installable, online-only match data/actions; offline screen; latest two stable Chrome/Safari/Firefox/Edge; responsive; WCAG 2.2 AA target |
| Age-related scope | No age restrictions, declaration, age fields/filters or age-related messaging |
| License/architecture | AGPL-3.0-only for code/docs; technology-neutral architecture by explicit choice |

Private games, waitlists, recurring games, ratings, payments and venue booking are
deferred. Native chat, avatars, past-match lists and the other exclusions above are
outside MVP. The canonical [requirements](docs/product/requirements.md) include
testable behavior and edge cases.

## Evidence labels

**Confirmed** means an explicit user choice. **Proposal** means an unselected idea.
**Rejected** records an exclusion or incompatible option, with its scope.
**Open** identifies missing evidence or a deliberately unresolved implementation
choice. **Derived recommendation** marks new reasoning; defaults selected under
DEC-060 form the current baseline while retaining that label. Future ideas are
not silently adopted. See [CONTRIBUTING](CONTRIBUTING.md).

Former private contact grants, a leave cutoff, public past history, and proposed
moderation/verification features remain in history, not current requirements.

## Structure and maintenance

```text
README.md, AGENTS.md, CONTRIBUTING.md, CHANGELOG.md, LICENSE, LICENSE-STATUS.md
docs/
  product/       vision, MVP, requirements, journeys, communication/privacy, UX
  decisions/     decision log, selected defaults, template, superseded history
  sources/       exact conversation evidence, recovery limits, external references
  architecture/  domain model, neutral architecture, quality/security
  planning/      resolved questions, deliberate deferrals, roadmap/future ideas
  validation/    scenarios, traceability, documentation and instruction reviews
  delivery.md
scripts/check_docs.py
.github/PULL_REQUEST_TEMPLATE.md
```

Read [AGENTS.md](AGENTS.md) before changes; run:

```sh
python3 scripts/check_docs.py
```

The checker validates files, local links/anchors, identifiers, acceptance sections
and traceability. Product acceptance scenarios are **Not run**: no app exists here.
It does not prove historical completeness, external-link health or legal compliance.

## Repository delivery

The [destination repository](https://github.com/mohamadrezakoohkan/open-sports) was
accessible but empty, with no base branch for a PR. Work uses a dedicated local
branch; the default branch has not been initialized or pushed. See
[delivery status and integration instructions](docs/delivery.md) for the archive,
portable Git bundle and final Git inspection.

Licensed [AGPL-3.0-only](LICENSE); [license details](LICENSE-STATUS.md).
