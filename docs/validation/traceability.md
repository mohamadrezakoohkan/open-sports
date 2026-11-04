# Source-to-decision-to-requirement traceability

This is documentary coverage, not product-test execution. Superseded decisions
remain linked to successor requirements; do not test their old behavior as current.
Selected defaults retain their Derived recommendation label under DEC-060.

## Requirements to scenarios

| Requirement | Verification scope | Acceptance scenarios |
|---|---|---|
| [REQ-001](../product/requirements.md#req-001) | sports matchmaking PWA | [TEST-001](acceptance-tests.md#test-001) |
| [REQ-002](../product/requirements.md#req-002) | instant public joining | [TEST-002](acceptance-tests.md#test-002) |
| [REQ-003](../product/requirements.md#req-003) | external-only participant chat | [TEST-011](acceptance-tests.md#test-011) |
| [REQ-004](../product/requirements.md#req-004) | optional owner-controlled contact publication | [TEST-009](acceptance-tests.md#test-009), [TEST-010](acceptance-tests.md#test-010) |
| [REQ-005](../product/requirements.md#req-005) | email/password accounts and upcoming-only profiles | [TEST-016](acceptance-tests.md#test-016) |
| [REQ-006](../product/requirements.md#req-006) | public map discovery and details | [TEST-016](acceptance-tests.md#test-016), [TEST-020](acceptance-tests.md#test-020), [TEST-025](acceptance-tests.md#test-025) |
| [REQ-007](../product/requirements.md#req-007) | host a scheduled public match | [TEST-004](acceptance-tests.md#test-004), [TEST-025](acceptance-tests.md#test-025), [TEST-028](acceptance-tests.md#test-028) |
| [REQ-008](../product/requirements.md#req-008) | reliable capacity and joining | [TEST-002](acceptance-tests.md#test-002), [TEST-012](acceptance-tests.md#test-012), [TEST-017](acceptance-tests.md#test-017), [TEST-027](acceptance-tests.md#test-027) |
| [REQ-009](../product/requirements.md#req-009) | leave participation | [TEST-007](acceptance-tests.md#test-007) |
| [REQ-010](../product/requirements.md#req-010) | edit or cancel a match | [TEST-008](acceptance-tests.md#test-008), [TEST-025](acceptance-tests.md#test-025), [TEST-028](acceptance-tests.md#test-028) |
| [REQ-011](../product/requirements.md#req-011) | public contact visibility | [TEST-009](acceptance-tests.md#test-009) |
| [REQ-012](../product/requirements.md#req-012) | hide and edit published contacts | [TEST-010](acceptance-tests.md#test-010) |
| [REQ-013](../product/requirements.md#req-013) | external contact handoff and format validation | [TEST-011](acceptance-tests.md#test-011) |
| [REQ-014](../product/requirements.md#req-014) | field-level public/private data boundary | [TEST-009](acceptance-tests.md#test-009), [TEST-010](acceptance-tests.md#test-010), [TEST-016](acceptance-tests.md#test-016) |
| [REQ-015](../product/requirements.md#req-015) | external support; no in-app reporting or moderation tools | [TEST-024](acceptance-tests.md#test-024) |
| [REQ-016](../product/requirements.md#req-016) | installation and online-only match data | [TEST-017](acceptance-tests.md#test-017) |
| [REQ-017](../product/requirements.md#req-017) | accessibility and supported browsers | [TEST-018](acceptance-tests.md#test-018) |
| [REQ-018](../product/requirements.md#req-018) | data lifecycle and operation | [TEST-019](acceptance-tests.md#test-019), [TEST-026](acceptance-tests.md#test-026) |
| [REQ-019](../product/requirements.md#req-019) | any sport and global locations with Spain/UK pilot focus | [TEST-005](acceptance-tests.md#test-005), [TEST-020](acceptance-tests.md#test-020) |
| [REQ-020](../product/requirements.md#req-020) | optional playing host | [TEST-004](acceptance-tests.md#test-004), [TEST-027](acceptance-tests.md#test-027) |
| [REQ-021](../product/requirements.md#req-021) | no age-specific product flow | [TEST-021](acceptance-tests.md#test-021) |
| [REQ-022](../product/requirements.md#req-022) | host eligibility limited to skill and role | [TEST-003](acceptance-tests.md#test-003) |
| [REQ-023](../product/requirements.md#req-023) | self-declared sport-specific skill | [TEST-003](acceptance-tests.md#test-003) |
| [REQ-024](../product/requirements.md#req-024) | skill scale and host range | [TEST-003](acceptance-tests.md#test-003) |
| [REQ-025](../product/requirements.md#req-025) | role-specific and general places | [TEST-005](acceptance-tests.md#test-005), [TEST-027](acceptance-tests.md#test-027) |
| [REQ-026](../product/requirements.md#req-026) | four optional contact methods | [TEST-009](acceptance-tests.md#test-009), [TEST-011](acceptance-tests.md#test-011) |
| [REQ-027](../product/requirements.md#req-027) | shared admission deadline | [TEST-007](acceptance-tests.md#test-007), [TEST-013](acceptance-tests.md#test-013) |
| [REQ-028](../product/requirements.md#req-028) | host management powers | [TEST-008](acceptance-tests.md#test-008), [TEST-014](acceptance-tests.md#test-014) |
| [REQ-029](../product/requirements.md#req-029) | material edit and reconfirmation | [TEST-012](acceptance-tests.md#test-012), [TEST-013](acceptance-tests.md#test-013) |
| [REQ-030](../product/requirements.md#req-030) | overlapping matches allowed | [TEST-006](acceptance-tests.md#test-006) |
| [REQ-031](../product/requirements.md#req-031) | in-app service notification list | [TEST-015](acceptance-tests.md#test-015) |
| [REQ-032](../product/requirements.md#req-032) | languages and local match time | [TEST-022](acceptance-tests.md#test-022) |
| [REQ-033](../product/requirements.md#req-033) | free public-only MVP | [TEST-023](acceptance-tests.md#test-023) |
| [REQ-034](../product/requirements.md#req-034) | scheduled lifecycle and terminal pages | [TEST-025](acceptance-tests.md#test-025) |
| [REQ-035](../product/requirements.md#req-035) | account deletion effects | [TEST-026](acceptance-tests.md#test-026) |
| [REQ-036](../product/requirements.md#req-036) | atomic role switching before cutoff | [TEST-027](acceptance-tests.md#test-027) |

## Decision evidence and current requirement coverage

| Decision | Source | Disposition | Requirements |
|---|---|---|---|
| [DEC-001](../decisions/decision-log.md#dec-001) | [SRC-006](../sources/conversation-evidence.md#src-006) | Confirmed; exact scope/refinements in canonical record | [REQ-001](../product/requirements.md#req-001) |
| [DEC-002](../decisions/decision-log.md#dec-002) | [SRC-002](../sources/conversation-evidence.md#src-002) | Confirmed; exact scope/refinements in canonical record | [REQ-002](../product/requirements.md#req-002) |
| [DEC-003](../decisions/decision-log.md#dec-003) | [SRC-003](../sources/conversation-evidence.md#src-003) | Confirmed; exact scope/refinements in canonical record | [REQ-003](../product/requirements.md#req-003) |
| [DEC-004](../decisions/decision-log.md#dec-004) | [SRC-004](../sources/conversation-evidence.md#src-004) | Confirmed; exact scope/refinements in canonical record | [REQ-004](../product/requirements.md#req-004) |
| [DEC-005](../decisions/decision-log.md#dec-005) | [SRC-009](../sources/conversation-evidence.md#src-009) | Confirmed; exact scope/refinements in canonical record | [REQ-019](../product/requirements.md#req-019) |
| [DEC-006](../decisions/decision-log.md#dec-006) | [SRC-009](../sources/conversation-evidence.md#src-009) | Confirmed; exact scope/refinements in canonical record | [REQ-020](../product/requirements.md#req-020) |
| [DEC-007](../decisions/decision-log.md#dec-007) | [SRC-009](../sources/conversation-evidence.md#src-009) | Confirmed; exact scope/refinements in canonical record | [REQ-002](../product/requirements.md#req-002), [REQ-008](../product/requirements.md#req-008) |
| [DEC-008](../decisions/decision-log.md#dec-008) | [SRC-009](../sources/conversation-evidence.md#src-009), [SRC-010](../sources/conversation-evidence.md#src-010) | Adults-only part superseded by DEC-014 | [REQ-021](../product/requirements.md#req-021) |
| [DEC-009](../decisions/decision-log.md#dec-009) | [SRC-010](../sources/conversation-evidence.md#src-010) | Confirmed; exact scope/refinements in canonical record | [REQ-022](../product/requirements.md#req-022) |
| [DEC-010](../decisions/decision-log.md#dec-010) | [SRC-010](../sources/conversation-evidence.md#src-010) | Confirmed; exact scope/refinements in canonical record | [REQ-023](../product/requirements.md#req-023) |
| [DEC-011](../decisions/decision-log.md#dec-011) | [SRC-011](../sources/conversation-evidence.md#src-011) | Confirmed; exact scope/refinements in canonical record | [REQ-024](../product/requirements.md#req-024) |
| [DEC-012](../decisions/decision-log.md#dec-012) | [SRC-011](../sources/conversation-evidence.md#src-011) | Confirmed; exact scope/refinements in canonical record | [REQ-025](../product/requirements.md#req-025) |
| [DEC-013](../decisions/decision-log.md#dec-013) | [SRC-011](../sources/conversation-evidence.md#src-011) | Confirmed; exact scope/refinements in canonical record | [REQ-021](../product/requirements.md#req-021) |
| [DEC-014](../decisions/decision-log.md#dec-014) | [SRC-012](../sources/conversation-evidence.md#src-012) | Confirmed; exact scope/refinements in canonical record | [REQ-021](../product/requirements.md#req-021) |
| [DEC-015](../decisions/decision-log.md#dec-015) | [SRC-012](../sources/conversation-evidence.md#src-012) | Private-grant model superseded by DEC-023/024 | [REQ-011](../product/requirements.md#req-011), [REQ-012](../product/requirements.md#req-012) |
| [DEC-016](../decisions/decision-log.md#dec-016) | [SRC-012](../sources/conversation-evidence.md#src-012) | Confirmed; exact scope/refinements in canonical record | [REQ-026](../product/requirements.md#req-026) |
| [DEC-017](../decisions/decision-log.md#dec-017) | [SRC-013](../sources/conversation-evidence.md#src-013) | Confirmed; exact scope/refinements in canonical record | [REQ-021](../product/requirements.md#req-021) |
| [DEC-018](../decisions/decision-log.md#dec-018) | [SRC-013](../sources/conversation-evidence.md#src-013) | Confirmed; exact scope/refinements in canonical record | [REQ-012](../product/requirements.md#req-012) |
| [DEC-019](../decisions/decision-log.md#dec-019) | [SRC-013](../sources/conversation-evidence.md#src-013) | Grant lifecycle superseded by DEC-023/024 | [REQ-012](../product/requirements.md#req-012) |
| [DEC-020](../decisions/decision-log.md#dec-020) | [SRC-014](../sources/conversation-evidence.md#src-014) | Confirmed; exact scope/refinements in canonical record | [REQ-011](../product/requirements.md#req-011) |
| [DEC-021](../decisions/decision-log.md#dec-021) | [SRC-014](../sources/conversation-evidence.md#src-014) | Leave restriction superseded by DEC-032 | [REQ-027](../product/requirements.md#req-027) |
| [DEC-022](../decisions/decision-log.md#dec-022) | [SRC-014](../sources/conversation-evidence.md#src-014) | Confirmed; exact scope/refinements in canonical record | [REQ-028](../product/requirements.md#req-028) |
| [DEC-023](../decisions/decision-log.md#dec-023) | [SRC-015](../sources/conversation-evidence.md#src-015) | Confirmed; exact scope/refinements in canonical record | [REQ-011](../product/requirements.md#req-011) |
| [DEC-024](../decisions/decision-log.md#dec-024) | [SRC-015](../sources/conversation-evidence.md#src-015) | Confirmed; exact scope/refinements in canonical record | [REQ-004](../product/requirements.md#req-004), [REQ-012](../product/requirements.md#req-012), [REQ-026](../product/requirements.md#req-026) |
| [DEC-025](../decisions/decision-log.md#dec-025) | [SRC-016](../sources/conversation-evidence.md#src-016) | Leave restriction superseded by DEC-032 | [REQ-027](../product/requirements.md#req-027) |
| [DEC-026](../decisions/decision-log.md#dec-026) | [SRC-016](../sources/conversation-evidence.md#src-016) | Confirmed; exact scope/refinements in canonical record | [REQ-029](../product/requirements.md#req-029) |
| [DEC-027](../decisions/decision-log.md#dec-027) | [SRC-016](../sources/conversation-evidence.md#src-016) | Confirmed; exact scope/refinements in canonical record | [REQ-030](../product/requirements.md#req-030) |
| [DEC-028](../decisions/decision-log.md#dec-028) | [SRC-017](../sources/conversation-evidence.md#src-017) | Confirmed; exact scope/refinements in canonical record | [REQ-029](../product/requirements.md#req-029) |
| [DEC-029](../decisions/decision-log.md#dec-029) | [SRC-017](../sources/conversation-evidence.md#src-017) | Leaving removed from deadline by DEC-032 | [REQ-027](../product/requirements.md#req-027), [REQ-029](../product/requirements.md#req-029) |
| [DEC-030](../decisions/decision-log.md#dec-030) | [SRC-017](../sources/conversation-evidence.md#src-017) | Confirmed; exact scope/refinements in canonical record | [REQ-029](../product/requirements.md#req-029) |
| [DEC-031](../decisions/decision-log.md#dec-031) | [SRC-018](../sources/conversation-evidence.md#src-018) | Confirmed; exact scope/refinements in canonical record | [REQ-031](../product/requirements.md#req-031) |
| [DEC-032](../decisions/decision-log.md#dec-032) | [SRC-018](../sources/conversation-evidence.md#src-018) | Confirmed; exact scope/refinements in canonical record | [REQ-009](../product/requirements.md#req-009), [REQ-027](../product/requirements.md#req-027) |
| [DEC-033](../decisions/decision-log.md#dec-033) | [SRC-018](../sources/conversation-evidence.md#src-018) | Confirmed; exact scope/refinements in canonical record | [REQ-010](../product/requirements.md#req-010), [REQ-028](../product/requirements.md#req-028) |
| [DEC-034](../decisions/decision-log.md#dec-034) | [SRC-019](../sources/conversation-evidence.md#src-019) | Confirmed; exact scope/refinements in canonical record | [REQ-023](../product/requirements.md#req-023), [REQ-024](../product/requirements.md#req-024) |
| [DEC-035](../decisions/decision-log.md#dec-035) | [SRC-019](../sources/conversation-evidence.md#src-019) | Confirmed; exact scope/refinements in canonical record | [REQ-019](../product/requirements.md#req-019), [REQ-025](../product/requirements.md#req-025) |
| [DEC-036](../decisions/decision-log.md#dec-036) | [SRC-019](../sources/conversation-evidence.md#src-019) | Confirmed; exact scope/refinements in canonical record | [REQ-028](../product/requirements.md#req-028) |
| [DEC-037](../decisions/decision-log.md#dec-037) | [SRC-020](../sources/conversation-evidence.md#src-020) | Confirmed; exact scope/refinements in canonical record | [REQ-005](../product/requirements.md#req-005) |
| [DEC-038](../decisions/decision-log.md#dec-038) | [SRC-020](../sources/conversation-evidence.md#src-020) | Past lists superseded by DEC-044 | [REQ-005](../product/requirements.md#req-005), [REQ-006](../product/requirements.md#req-006) |
| [DEC-039](../decisions/decision-log.md#dec-039) | [SRC-020](../sources/conversation-evidence.md#src-020) | Confirmed; exact scope/refinements in canonical record | [REQ-006](../product/requirements.md#req-006) |
| [DEC-040](../decisions/decision-log.md#dec-040) | [SRC-021](../sources/conversation-evidence.md#src-021) | Confirmed; exact scope/refinements in canonical record | [REQ-006](../product/requirements.md#req-006), [REQ-007](../product/requirements.md#req-007) |
| [DEC-041](../decisions/decision-log.md#dec-041) | [SRC-021](../sources/conversation-evidence.md#src-021) | Confirmed; exact scope/refinements in canonical record | [REQ-032](../product/requirements.md#req-032) |
| [DEC-042](../decisions/decision-log.md#dec-042) | [SRC-021](../sources/conversation-evidence.md#src-021) | Confirmed; exact scope/refinements in canonical record | [REQ-033](../product/requirements.md#req-033) |
| [DEC-043](../decisions/decision-log.md#dec-043) | [SRC-022](../sources/conversation-evidence.md#src-022) | Confirmed; exact scope/refinements in canonical record | [REQ-007](../product/requirements.md#req-007), [REQ-034](../product/requirements.md#req-034) |
| [DEC-044](../decisions/decision-log.md#dec-044) | [SRC-022](../sources/conversation-evidence.md#src-022) | Confirmed; exact scope/refinements in canonical record | [REQ-005](../product/requirements.md#req-005), [REQ-006](../product/requirements.md#req-006) |
| [DEC-045](../decisions/decision-log.md#dec-045) | [SRC-022](../sources/conversation-evidence.md#src-022) | Confirmed; exact scope/refinements in canonical record | [REQ-005](../product/requirements.md#req-005), [REQ-013](../product/requirements.md#req-013), [REQ-026](../product/requirements.md#req-026) |
| [DEC-046](../decisions/decision-log.md#dec-046) | [SRC-023](../sources/conversation-evidence.md#src-023) | Confirmed; exact scope/refinements in canonical record | [REQ-006](../product/requirements.md#req-006) |
| [DEC-047](../decisions/decision-log.md#dec-047) | [SRC-023](../sources/conversation-evidence.md#src-023) | Confirmed; exact scope/refinements in canonical record | [REQ-015](../product/requirements.md#req-015) |
| [DEC-048](../decisions/decision-log.md#dec-048) | [SRC-023](../sources/conversation-evidence.md#src-023) | Confirmed; exact scope/refinements in canonical record | [REQ-018](../product/requirements.md#req-018), [REQ-035](../product/requirements.md#req-035) |
| [DEC-049](../decisions/decision-log.md#dec-049) | [SRC-024](../sources/conversation-evidence.md#src-024) | Confirmed; exact scope/refinements in canonical record | [REQ-019](../product/requirements.md#req-019) |
| [DEC-050](../decisions/decision-log.md#dec-050) | [SRC-024](../sources/conversation-evidence.md#src-024) | Confirmed; exact scope/refinements in canonical record | [REQ-006](../product/requirements.md#req-006), [REQ-034](../product/requirements.md#req-034) |
| [DEC-051](../decisions/decision-log.md#dec-051) | [SRC-024](../sources/conversation-evidence.md#src-024) | Confirmed; exact scope/refinements in canonical record | [REQ-015](../product/requirements.md#req-015) |
| [DEC-052](../decisions/decision-log.md#dec-052) | [SRC-025](../sources/conversation-evidence.md#src-025) | Confirmed; exact scope/refinements in canonical record | [REQ-035](../product/requirements.md#req-035) |
| [DEC-053](../decisions/decision-log.md#dec-053) | [SRC-025](../sources/conversation-evidence.md#src-025) | Confirmed; exact scope/refinements in canonical record | [REQ-028](../product/requirements.md#req-028) |
| [DEC-054](../decisions/decision-log.md#dec-054) | [SRC-025](../sources/conversation-evidence.md#src-025) | Confirmed; exact scope/refinements in canonical record | [REQ-018](../product/requirements.md#req-018), [REQ-035](../product/requirements.md#req-035) |
| [DEC-055](../decisions/decision-log.md#dec-055) | [SRC-026](../sources/conversation-evidence.md#src-026) | Confirmed deliberate technology deferral | [REQ-001](../product/requirements.md#req-001) |
| [DEC-056](../decisions/decision-log.md#dec-056) | [SRC-026](../sources/conversation-evidence.md#src-026) | Confirmed; exact scope/refinements in canonical record | [REQ-001](../product/requirements.md#req-001) |
| [DEC-057](../decisions/decision-log.md#dec-057) | [SRC-026](../sources/conversation-evidence.md#src-026) | Confirmed; exact scope/refinements in canonical record | [REQ-001](../product/requirements.md#req-001), [REQ-016](../product/requirements.md#req-016) |
| [DEC-058](../decisions/decision-log.md#dec-058) | [SRC-027](../sources/conversation-evidence.md#src-027) | Confirmed; exact scope/refinements in canonical record | [REQ-020](../product/requirements.md#req-020), [REQ-025](../product/requirements.md#req-025), [REQ-036](../product/requirements.md#req-036) |
| [DEC-059](../decisions/decision-log.md#dec-059) | [SRC-027](../sources/conversation-evidence.md#src-027) | Confirmed; exact scope/refinements in canonical record | [REQ-001](../product/requirements.md#req-001), [REQ-017](../product/requirements.md#req-017) |
| [DEC-060](../decisions/decision-log.md#dec-060) | [SRC-027](../sources/conversation-evidence.md#src-027) | Confirmed delegation; defaults remain Derived recommendations | [REQ-008](../product/requirements.md#req-008), [REQ-013](../product/requirements.md#req-013), [REQ-031](../product/requirements.md#req-031) |

## Additional coverage

- [Source coverage](../sources/recovery-status.md) records unavailable historical context.
- [Journeys](../product/journeys.md) assemble requirements into user flows.
- [Selected derived defaults](../decisions/derived-defaults.md) resolve delegated details.
- [Historical contact model](../decisions/history/contact-grants-before-correction.md) is archived, not current behavior.
- [Resolved questions](../planning/open-questions.md) distinguish completed choices from intentional technical deferrals.
- [Validation report](validation-report.md) records checks actually performed.
