# BarberKas — Canonical Roadmap & Prioritized Backlog

## North-star and activation

**ICP:** owner barbershop independen 1–3 outlet di Indonesia yang masih mengelola transaksi/booking/retensi secara manual atau terpencar di WhatsApp.

**Activation:** dalam 24 jam setelah onboarding, tenant berhasil login, mengatur layanan/capster, mencatat transaksi pertama, menerima booking pertama, dan melihat laporan harian tanpa bantuan engineer.

**North-star:** jumlah outlet aktif mingguan yang mencatat transaksi dan menjalankan minimal satu workflow booking/retention.

Guardrails: cross-tenant incident = 0, payment mismatch = 0, WA failed rate terlihat, COGS per tenant di bawah batas paket, support burden terukur.

## 0–30 days — Make it truthful and safe

### P0

1. Fail-closed auth untuk production dan hapus first-user auto-admin.
2. Rekonsiliasi amount/merchant/reference payment callback + callback event ledger.
3. Rate limit, quotas, body-size limits dan anti-abuse pada public/AI/payment/webhook routes.
4. Automated tests: auth matrix, cross-tenant reads/writes, payment, webhook idempotency, booking duplicate, migration smoke.
5. CI required checks: install, type/build, unit, integration, lint, dependency/secret scan.
6. Sinkronkan semua marketing claims; ubah outbound WA/invoice dan PWA menjadi beta/tidak tersedia sampai terbukti.
7. Aktifkan paket outbound WA yang valid dan ukur delivery, failure, retry.

### P1

8. Security headers/CSP dan CORS allowlist.
9. Typed request validation + normalized error contract.
10. Error tracking, structured logs, request ID, synthetic health dan alerting.
11. Privacy Policy, ToS, refund/cancel, AI disclosure, consent case study.
12. Backup dan restore drill D1; tetapkan RPO/RTO.
13. Guest demo terisolasi dari tenant nyata.

**30-day exit:** semua P0 ditutup; satu release melewati CI; payment and tenant-isolation tests hijau; copy tidak mengandung klaim kontradiktif.

## 31–60 days — Make it operable and sellable

1. Simplify navigation: owner daily ops vs operator/admin console dipisahkan.
2. Finalize Starter/Growth/Multi-Outlet entitlements, limits, overage dan implementation fee.
3. Onboarding wizard, sample import, guided checklist dan lifecycle trial→active→suspended→churned.
4. Customer export/delete, tenant offboarding dan retention jobs.
5. Normalize transaction line items dan tambah DB CHECK/FK constraints.
6. OpenAPI contract, pagination/idempotency conventions dan versioning policy.
7. Operational dashboard: payment, WA, LLM, errors, latency, activation and retention.
8. Runbooks: provider outage, payment mismatch, leaked webhook secret, tenant isolation, restore.
9. SEO: one primary domain, redirects/canonical, sitemap, OG/JSON-LD and evidence-rich case studies.
10. Pilot onboarding untuk 3–5 barbershop dengan consent dan measurement plan.

**60-day exit:** 3 pilot aktif, median activation <24 jam, weekly usage terlihat, support and provider costs tercatat.

## 61–90 days — Prove retention and controlled scale

1. Automated dunning/renewal or explicitly managed invoice workflow.
2. Cancellation/churn reason and win-back experiments.
3. Role permissions per action/outlet; sensitive action confirmation/audit.
4. Load/concurrency tests against agreed pilot volume.
5. Incident drill and second restore drill.
6. COGS and gross-margin dashboard per package.
7. Evaluate AI outputs with golden datasets, safety rules, latency/cost caps and fallback metrics.
8. Publish public status/support/security pages.
9. Convert at least two pilots to recurring paid customers.
10. Decide expansion based on activation and retention evidence—not feature count.

**90-day exit:** paid retention evidence exists, no unresolved P0/P1, operational burden and unit economics acceptable.

## 6–12 months — Enterprise path (only if demanded)

- Multi-outlet hierarchy and granular RBAC.
- SSO/SAML/OIDC enterprise and identity lifecycle.
- Immutable/exportable audit logs.
- SLA/DPA/subprocessor/security package.
- DR/capacity program, status page and incident notification.
- Pen-test and vulnerability disclosure.
- Configurable retention/residency/export controls.
- Procurement-ready contracts and support tiers.

## Backlog decisions

### Build now

- Trust/security/quality/operations controls.
- Core kasir, booking, WA and customer retention reliability.
- Guest demo, onboarding and reporting.

### Fix now

- Claim contradictions, payment reconciliation, auth bootstrap, fail-open behavior, rate limiting, security headers, CORS and tests.

### Remove or hide

- F0–F7/DoO/Foundry internals from owner dashboard.
- “Enterprise”, “PWA”, “auto-send”, and “live” labels without valid evidence.
- Real customer tenant from public demo selector unless consent and strict demo data isolation exist.

### Defer

- Six additional agents.
- Salon/klinik/laundry/cafe expansion.
- Cross-shop benchmarking.
- “AI Company in a Box”.

## Definition of Ready

A backlog item is ready only when it has: user/problem, owner, scope/non-scope, threat/privacy impact, API/data impact, acceptance criteria, telemetry, test plan, rollout/rollback, dependencies and copy/status effect.

## Definition of Done

An item is done only when:

- Code reviewed and CI green.
- Unit/integration/E2E and negative authorization tests pass.
- Migration is backward-compatible and rollback/repair documented.
- Logging/metrics/alerts exist without leaking secrets/PII.
- Security/privacy review complete for sensitive changes.
- Documentation and evidence ledger updated.
- Staged/canary verification completed.
- Production acceptance evidence linked.
- Marketing status updated from roadmap/beta/live based on proof.

## Suggested ownership

- Founder/Product: positioning, packaging, claim ledger, pilots and pricing.
- Engineering: auth, payment, API, data, CI and reliability.
- Security/Privacy owner: threat model, policies, testing and incident readiness.
- Operations/Support: onboarding, runbooks, SLO and provider escalation.
- Design/Research: owner workflow, guest demo, accessibility and usability.
- Sales/Marketing: evidence-based pages, consented case studies, no unverified claims.