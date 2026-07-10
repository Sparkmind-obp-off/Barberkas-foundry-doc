# BarberKas Foundry — Canonical Audit Index

**Status:** baseline audit independen  
**Tanggal:** 2026-07-10  
**Objek:** `barberkas-aaas.pages.dev`, `barberkas-foundry.biz.id`, dan repository `Sparkmind-obp-off/Barberkas-foundry`

## Dokumen canonical

1. [01-MASTER-AUDIT.md](./01-MASTER-AUDIT.md) — executive summary, scorecard, temuan produk/brand/teknis, dan keputusan.
2. [02-RISK-AND-READINESS-REGISTER.md](./02-RISK-AND-READINESS-REGISTER.md) — risk register, production gate, enterprise gate, serta acceptance criteria.
3. [03-ROADMAP-AND-BACKLOG.md](./03-ROADMAP-AND-BACKLOG.md) — roadmap 30/60/90 hari, backlog P0–P3, DoR, dan DoD.

## Aturan bukti

- **VERIFIED:** diperiksa langsung melalui situs, endpoint produksi, build, atau source code.
- **INFERRED:** kesimpulan kuat dari bukti tetapi belum diuji end-to-end dengan akun/uang nyata.
- **NOT VERIFIED:** klaim belum memiliki bukti independen yang cukup.

## Source-of-truth hierarchy yang direkomendasikan

1. Production telemetry dan payment/provider records.
2. Automated tests dan CI release evidence.
3. Source code + migrations + infrastructure config.
4. API/OpenAPI contract.
5. Product specification dan runbook.
6. Website/README/marketing copy.

Marketing tidak boleh menjadi sumber kebenaran untuk status fitur.