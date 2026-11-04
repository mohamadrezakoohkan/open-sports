# External references and constraints

These references were consulted during reconstruction. They inform engineering
recommendations and external constraints, **not recovered product decisions**.
User decisions remain in the [decision log](../decisions/decision-log.md).

<a id="provider-eligibility"></a>
## Selected providers and age eligibility

Checked 2026-11-04. Recheck before launch because provider terms can change.

| Provider | Observed primary-source terms | Product implication — derived |
|---|---|---|
| Telegram | Its terms require users in EU countries and the United Kingdom to be at least 18 to sign up. [Telegram terms](https://telegram.org/tos) | The app's all-ages policy cannot imply Telegram access for every participant in the Spain/UK/Netherlands pilot |
| WhatsApp, EEA | The terms set a baseline of 13 for independent use, subject to a higher local requirement, and describe parent-managed accounts below that age where available. [EEA terms](https://www.whatsapp.com/legal/terms-of-service-eea?lang=en) | Do not promise independent access at every age or assume parent-managed accounts are available everywhere |
| WhatsApp, UK | The UK terms also state a baseline of 13, subject to a higher local requirement, and describe parent-managed accounts where available. [UK terms](https://www.whatsapp.com/legal/terms-of-service-uk) | Keep provider eligibility separate from the PWA's participation scope |

The EEA and UK WhatsApp pages displayed an effective date of 2026-08-17. No assumption
was made about parent-managed-account availability in a particular pilot city.
Phone/email support does not select an underlying carrier or email provider; no
universal age-access claim is made for those services either.

**Product decision:** DEC-017 specifies no age restrictions or age-related product
messaging. These internal reference notes do not add a birth-date field, declaration,
guardian model, provider-specific age notice, or a compliance conclusion. General
handoff behavior remains a separate product choice.

## Engineering background

The following official sources were checked during preparation. They provide
background for draft engineering choices, rather than evidence of user adoption:

- [MDN: offline and background operation](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Offline_and_background_operation)
  — PWA caching and offline behavior require an explicit design.
- [OWASP: authorization guidance](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)
  — background for server-side, per-request access checks and default denial.
- [W3C: WCAG 2.2](https://www.w3.org/TR/WCAG22/)
  — reference for the selected accessibility target; no product conformance is claimed.

## Technical and licensing options checked 2026-11-04

These sources initially informed options presented to the owner. The owner first
chose technology neutrality and AGPL-3.0-only in DEC-055/056, then selected Supabase
as the backend in [DEC-061](../decisions/decision-log.md#dec-061). Frontend and other
provider choices remain deferred. No product dependencies are installed.

- [Next.js PWA guide](https://nextjs.org/docs/app/guides/progressive-web-apps):
  framework support for building a PWA. Push examples do not override the chosen
  in-app-only service notifications.
- [Next.js self-hosting guide](https://nextjs.org/docs/app/guides/self-hosting):
  self-hosted deployment is an option, not a confirmed hosting choice.
- [Supabase password authentication](https://supabase.com/docs/guides/auth/passwords)
  and [configuration](https://supabase.com/docs/guides/auth/general-configuration):
  email/password, password-reset email and configurable email confirmation.
  Production SMTP and retention settings still need deployment decisions.
- [MIT license summary/text](https://choosealicense.com/licenses/mit/) and
  [AGPL summary/text](https://choosealicense.com/licenses/agpl-3.0/): background
  for the owner's licensing choice, not an inferred license grant.

- [GNU AGPL version 3 canonical text](https://www.gnu.org/licenses/agpl-3.0.txt):
  retrieved unchanged as the repository LICENSE after the explicit AGPL-3.0-only
  decision. A browser fetch of the HTML version timed out; the canonical text
  download succeeded.

<a id="supabase-free-hosting"></a>
## Supabase hosted Free constraints

Checked 2026-11-04 against the linked official sources. These are provider facts,
not user decisions or a guarantee that the documented MVP fits the Free plan.
Recheck before provisioning or launch.

| Subject | Observed provider position | Product implication — Derived recommendation |
|---|---|---|
| Free allowances | $0/month, 500 MB database, 50,000 monthly active Auth users, 5 GB egress, 5 GB cached egress and 1 GB file storage; limit of two active Free projects. [Pricing](https://supabase.com/pricing) | Measure realistic pilot consumption; unlimited API requests do not mean unlimited storage, bandwidth or compute |
| Inactivity pause | Low database activity over seven days can trigger pausing; a paused project can be restored, including data/configuration, for up to one year. [Project pausing](https://supabase.com/docs/guides/platform/free-project-pausing) | Do not assume continuous jobs or expiry of retained data within 30 days; resolve Q-019 before deployment |
| Backup/recovery | Daily managed backups are documented for paid plans; Supabase recommends regular exports/off-site backups for Free projects. [Database backups](https://supabase.com/docs/guides/platform/backups) | Define and verify bounded recovery copies and deletion-aware restoration; Free is not proof of the DEC-054 backup bound |
| Password-reset email | Default SMTP sends only to project-team addresses, currently at two messages/hour, and is not intended for production. Custom SMTP permits delivery to the product's users. [Custom SMTP](https://supabase.com/docs/guides/auth/auth-smtp) | Configure a sender and provider for public reset emails under Q-020; vendor, domain and cost remain unresolved |

**Open conflict:** paused recoverable data can outlive the confirmed 30-day bound.
The public documentation above does not establish a Free configuration satisfying
all deletion/retention requirements. Keep [Q-019](../planning/open-questions.md#q-019)
open until a supported operating configuration is evidenced, or the owner explicitly
changes the requirement in a new decision. No paid upgrade is adopted here.

<a id="supabase-technical"></a>
## Supabase technical references

Checked 2026-11-04. These support the **Derived recommendations** in the
[architecture](../architecture/technical-overview.md), not an assertion that the
owner explicitly chose each mechanism.

- [Supabase source repository](https://github.com/supabase/supabase): open-source
  Postgres platform; managed cloud limits/terms are separate from code availability.
  Preserve applicable dependency notices when implementation chooses versions.
- [Password authentication](https://supabase.com/docs/guides/auth/passwords) and
  [Auth configuration](https://supabase.com/docs/guides/auth/general-configuration):
  email/password recovery and configurable email confirmation. Disabling Confirm
  Email avoids a sign-in verification gate; its internal confirmation state does
  not prove address ownership.
- [PostGIS](https://supabase.com/docs/guides/database/extensions/postgis): indexed
  geographic types and queries for location filtering/distance; not a map-tile or
  geocoding service.
- [Database functions](https://supabase.com/docs/guides/database/functions),
  [PostgREST transactions](https://docs.postgrest.org/en/stable/references/transactions.html)
  and [PostgreSQL locking](https://www.postgresql.org/docs/current/explicit-locking.html):
  basis for server-side atomic transitions. Each API request has its own transaction;
  locking and constraints must still be designed for competing mutations.
- [Row Level Security](https://supabase.com/docs/guides/database/postgres/row-level-security)
  and [column privileges](https://supabase.com/docs/guides/database/postgres/column-level-security):
  row filtering does not hide private columns; grants, views and privileged functions
  require explicit review. Default view behavior can bypass underlying RLS.
- [Supabase Cron](https://supabase.com/docs/guides/cron): `pg_cron` schedules SQL or
  database functions and records runs. Job capability does not establish successful
  cleanup, operation during pausing or compliant provider backup expiry.
