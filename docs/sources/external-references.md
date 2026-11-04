# External references and constraints

These references were consulted during reconstruction. They inform engineering
recommendations and external constraints, **not recovered product decisions**.
User decisions remain in the [decision log](../decisions/decision-log.md).

<a id="provider-eligibility"></a>
## Selected providers and age eligibility

Checked 2026-11-04. Recheck before launch because provider terms can change.

| Provider | Observed primary-source terms | Product implication — derived |
|---|---|---|
| Telegram | Its terms require users in EU countries and the United Kingdom to be at least 18 to sign up. [Telegram terms](https://telegram.org/tos) | The app's all-ages policy cannot imply Telegram access for every participant in the Spain/UK pilot |
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

These sources informed options presented to the owner. The owner chose a
technology-neutral architecture and AGPL-3.0-only, separately recorded in DEC-055/056.
No product dependencies are installed.

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
