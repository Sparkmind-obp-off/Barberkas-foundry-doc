# BarberKas — Canonical SSOT v2

> **Single Source of Truth** untuk seluruh ekosistem BarberKas / SparkMind.
> Semua keputusan strategis, produk, arsitektur, engineering, keamanan, operasi,
> komersial, dan tata kelola **wajib mengacu pada repository ini**.

| Field | Value |
|---|---|
| **Version** | 2.0.0 |
| **Status** | Approved (baseline) |
| **Owner** | Founder / Product (SparkMind) |
| **Created** | 2026-07-10 |
| **Supersedes** | `archive/canonical-v1/`, `archive/ssot/` (B4, B5, FM, R6), `archive/barberkas-aaas-bundle/` |
| **Repo produk** | https://github.com/Sparkmind-obp-off/Barberkas-foundry |
| **Production** | https://barberkas-aaas.pages.dev · https://barberkas-foundry.biz.id |

---

## Mulai dari sini

1. **[canonical/00-INDEX.md](canonical/00-INDEX.md)** — peta lengkap seluruh dokumen canonical.
2. **[migration/MIGRATION-MAP.md](migration/MIGRATION-MAP.md)** — pemetaan dokumen lama → v2 (retained / merged / superseded / archived).
3. **[migration/AUDIT-REPORT-V2.md](migration/AUDIT-REPORT-V2.md)** — laporan audit & sintesis yang menghasilkan v2 ini.

## Struktur repository

```
canonical/
├── 00-INDEX.md              # Peta dokumen + aturan navigasi
├── 00-foundation/           # Charter, glossary, governance, doc policy
├── 01-brand/                # Brand architecture, positioning, messaging
├── 02-product/              # Product brief, ICP, feature matrix, packaging
├── 03-architecture/         # System overview, data architecture, ADR
├── 04-engineering/          # Engineering standards, testing, API standards
├── 05-security/             # Security baseline, risk register, privacy
├── 06-operations/           # SLO, runbooks, incident & DR
├── 07-ai/                   # AI agents policy, Session OS (FM layer)
├── 08-commercial/           # GTM, pricing evidence, evidence ledger
└── 09-governance/           # Production gate, enterprise gate, roadmap
migration/                   # Audit report v2 + migration map
archive/                     # SELURUH dokumen legacy (read-only, referensi)
```

## Aturan inti (non-negotiable)

1. **Repository ini adalah satu-satunya sumber kebenaran.** Dokumen di `archive/` bersifat
   read-only referensi sejarah; jika konflik, **canonical v2 menang**.
2. **Aturan bukti (Truth-Lock):** setiap klaim status diberi label
   `VERIFIED` / `INFERRED` / `NOT VERIFIED`. Marketing **tidak boleh** menjadi sumber
   kebenaran status fitur.
3. **Source-of-truth hierarchy:** telemetry produksi & payment records → automated tests/CI →
   source code + migrations + infra config → OpenAPI contract → product spec/runbook →
   website/README/marketing copy.
4. **Setiap dokumen wajib bermetadata** (lihat [Documentation Policy](canonical/00-foundation/003-documentation-policy.md)).
5. **Perubahan signifikan wajib ADR** di `canonical/03-architecture/adr/`.

## Status produk saat baseline v2 (jujur)

- **Pilot-grade (skor audit 1.9/5)** — layak pilot berbayar terkontrol 3–10 barbershop,
  **belum** self-serve SaaS massal, **belum** enterprise-grade.
- Gate menuju production & enterprise: [09-governance/091-production-gate.md](canonical/09-governance/091-production-gate.md)
  dan [09-governance/092-enterprise-gate.md](canonical/09-governance/092-enterprise-gate.md).

## Lifecycle dokumen

`Draft → Review → Approved → Deprecated → Archived`

## Changelog

Lihat [CHANGELOG.md](CHANGELOG.md).
