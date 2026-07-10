# BarberKas — Risk & Readiness Register

## Prioritized risk register

| ID | Priority | Risk | Evidence | Impact | Required mitigation | Exit/acceptance criteria |
|---|---|---|---|---|---|---|
| SEC-01 | P0 | Production auth can fail open when Clerk config is absent | `src/middleware/auth.ts` | Unauthorized access after secret/config drift | Explicit `APP_ENV`; production always fail closed | Tests prove missing/invalid config returns 503/401 for every protected route |
| SEC-02 | P0 | First user can become admin when no admin row/allowlist exists | `src/middleware/auth.ts:102-113` | Account takeover during bootstrap/reset | Remove automatic promotion; use one-time bootstrap secret/manual migration | Unknown first user remains unprivileged; bootstrap event audited |
| PAY-01 | P0 | Callback amount is signed but not reconciled against stored order amount | `src/routes/outcome.ts:285-327` | Wrong-value payment may mark order paid | Compare merchant, amount, currency/reference/order state; store callback event ledger | Mismatch returns rejection, raises alert, never marks paid; automated tests |
| ABUSE-01 | P0 | No rate limits/quotas visible on public and AI/payment surfaces | route/config audit | Spam, provider cost, D1/LLM exhaustion | Per-IP/tenant/user limits, WAF rules, bounded body size, quotas | 429 behavior tested; dashboards and alerts exist |
| QA-01 | P0 | No CI and negligible automated test coverage | no `.github/workflows`; `test` is curl | Regression/cross-tenant/payment defects reach prod | Unit, integration, E2E, migration and security tests + CI | Required checks block merge/deploy; critical paths green |
| CLAIM-01 | P0 | Landing says invoice auto-sent via WA while README says outbound blocked | landing + README | Mis-selling and trust/legal risk | Correct copy and introduce claim evidence ledger | Every live claim links to current evidence and owner |
| PRIV-01 | P1 | Customer phone/message/history lacks documented retention/delete/consent | schema/code/docs | Privacy complaints and compliance risk | Privacy inventory, consent, retention, export/delete and access policy | Privacy policy published; deletion/export tested |
| WEB-01 | P1 | Security headers absent | production headers | XSS/clickjacking/data leakage impact | CSP, HSTS, nosniff, frame-ancestors, referrer/permissions policy | Automated header test passes on all HTML/API responses |
| API-01 | P1 | Broad CORS and inconsistent schema validation | `src/index.tsx`, route review | Cross-origin abuse and malformed input | Allowlist origin; typed validators; size/enum/format limits | Negative contract tests pass |
| OPS-01 | P1 | No SLO, alerting, tracing, incident or DR evidence | repo/production review | Silent failure and slow recovery | Metrics, error tracking, synthetic probes, runbooks, backup/restore drills | Alert test and restore drill recorded; RPO/RTO met |
| DATA-01 | P1 | Weak relational constraints and denormalized service IDs | migrations | Integrity/reporting failures | Transaction line-item table, FK/CHECK constraints, lifecycle states | Migration/backfill complete; invariant tests pass |
| WEB-02 | P1 | “PWA” claim without manifest/service worker | manifest 404, repo review | Misleading claim, poor install/offline UX | Implement real PWA or remove claim | Installability audit passes or copy removed |
| SEO-01 | P2 | Duplicate domains and missing sitemap/canonical/schema | production checks | Split authority and weak discovery | Primary domain, redirects/canonical, sitemap, robots, OG/JSON-LD | Search-console-ready crawl passes |
| SUPPLY-01 | P2 | Dev tooling vulnerabilities | `npm audit` | Local/CI supply-chain exposure | Upgrade Wrangler/lockfile; Dependabot/Renovate | Full audit has no high/critical findings or accepted exception |
| UX-01 | P2 | Demo CTA requires login | production `/app` | Conversion drop | Isolated guest sandbox or product tour | Demo opens without account and contains no real tenant data |
| BRAND-01 | P2 | Excessive internal jargon and brand hierarchy | landing/docs | Confusion and lower conversion | Simplify around BarberKas and customer outcomes | Message test: target user understands offer in <10 seconds |

## Production launch gate

A paid public launch is allowed only when all are true:

- [ ] SEC-01, SEC-02, PAY-01, ABUSE-01, QA-01 and CLAIM-01 closed.
- [ ] Cross-tenant authorization matrix automated and passing.
- [ ] Payment create/callback/duplicate/mismatch/failure/refund tests passing.
- [ ] Outbound WhatsApp works on paid provider plan, with delivery telemetry and retry policy.
- [ ] Privacy Policy, ToS, refund/cancel and AI disclosure published.
- [ ] Backup completed and restore drill demonstrated.
- [ ] Alerts cover 5xx, auth anomalies, payment mismatch, webhook failures and WA delivery failure.
- [ ] Support owner, hours, escalation and incident communication defined.
- [ ] Landing claims match verified production capability.
- [ ] Three pilot customers complete activation without engineer intervention.

## Enterprise gate

Enterprise label may be used only when production gate passes plus:

- [ ] Granular RBAC per outlet/action and least privilege.
- [ ] SSO option and documented identity lifecycle.
- [ ] Immutable/exportable audit log.
- [ ] DPA, SLA, subprocessor list and security whitepaper.
- [ ] Configurable retention/export/delete and tenant offboarding.
- [ ] Pen-test remediation and vulnerability disclosure process.
- [ ] SBOM, SAST, dependency/secret scanning and signed release evidence.
- [ ] RPO/RTO contract backed by recurring restore/DR exercises.
- [ ] Capacity/load test for agreed tenant/outlet/transaction volume.
- [ ] Status page and formal incident notification workflow.

## Evidence ledger schema

Every marketing claim should be stored with:

`claim_id, exact_copy, surface, status, evidence_url_or_query, evidence_type, owner, verified_at, expires_at, reviewer, fallback_copy`

Expired or failed evidence automatically changes copy from “live/verified” to “pilot/beta/unavailable”.