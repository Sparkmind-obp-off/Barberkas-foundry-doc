# Changelog — Canonical SSOT

Format mengikuti [Keep a Changelog](https://keepachangelog.com/) + SemVer untuk versi repo dokumentasi.

## [3.0.0] — 2026-07-10 — "Hardening v3" (RFC-001)

Program hardening penuh v2 → v3 dalam 5 batch (H1–H5), payung: [RFC-001](canonical/10-rfc/RFC-001-docs-hardening-v3.md).

### Added — H1 (Phase 1: Foundation)
- `canonical/99-schema/` — Docs-as-Code schema layer:
  - [Q-990 Document Schema](canonical/99-schema/990-document-schema.md) — struktur wajib dokumen.
  - [Q-991 Metadata Schema](canonical/99-schema/991-metadata-schema.md) — YAML front-matter wajib (id, title, version, status, owner, reviewers, classification, type, last_updated, next_review, parent, related_docs).
  - [Q-992 Taxonomy](canonical/99-schema/992-taxonomy.md) — 12 tipe dokumen + aturan otoritas.
  - [Q-993 Lifecycle](canonical/99-schema/993-lifecycle.md) — state machine Draft→Review→Approved→Deprecated→Archived.
  - [Q-994 Knowledge Graph](canonical/99-schema/994-knowledge-graph.md) — parent/children/dependency antar dokumen.
  - [Q-995 Numbering & ID](canonical/99-schema/995-numbering.md) — konvensi ID permanen.
- [MANIFEST.md](MANIFEST.md) — registry resmi seluruh folder & dokumen (orphan/dangling = gagal gate).

### Added — H2 (Phase 2: Governance)
- `canonical/10-rfc/` — RFC layer: [RFC-INDEX](canonical/10-rfc/RFC-INDEX.md), [RFC-000 Template](canonical/10-rfc/RFC-000-template.md), [RFC-001 Docs Hardening v3](canonical/10-rfc/RFC-001-docs-hardening-v3.md).
- [G-094 Docs Governance Workflows](canonical/09-governance/094-docs-governance-workflows.md) — board, review/approval, RFC, ADR, deprecation, exception policy.

### Added — H3 (Phase 3: Quality)
- [tools/validate_docs.py](tools/validate_docs.py) — quality gate 8 pemeriksaan: front-matter Q-991, ID unik, orphan/dangling vs MANIFEST, broken link, H1 tunggal, integritas parent/related.
- [tools/ci/docs-quality.yml](tools/ci/docs-quality.yml) — CI workflow (aktivasi: salin ke `.github/workflows/`).
- Retrofit YAML front-matter Q-991 ke **53 dokumen** (canonical + migration + MANIFEST).

### Added — H4 (Phase 4+7: IA/Enterprise)
- [G-095 Capability Map & Operating Model](canonical/09-governance/095-capability-map-operating-model.md) — 17 capability / 5 domain + maturity 1–5 + operating model founder-led.
- [G-096 Responsibility & Stakeholder Matrix](canonical/09-governance/096-responsibility-stakeholder-matrix.md) — RACI per capability + 7 stakeholder + jalur eskalasi.
- [G-097 Risk & Compliance Matrix](canonical/09-governance/097-risk-compliance-matrix.md) — heatmap 16 risiko (render S-051) + compliance matrix 7 kewajiban (K1–K7).

### Changed
- [Q-994 Knowledge Graph](canonical/99-schema/994-knowledge-graph.md) diperluas dengan node/edge G-095..G-097; status Draft → Approved.
- MANIFEST & 00-INDEX diperbarui setiap batch — registry final: **56 dokumen**.
- Semua dokumen canonical kini machine-validated; commit yang gagal gate tidak boleh merge (G-094).

### Governance
- Quality gate status akhir: **PASSED** — 59 file diperiksa, 56 front-matter valid & terdaftar.

## [2.0.0] — 2026-07-10

### Added
- Struktur Canonical SSOT v2 penuh: `00-foundation` s/d `09-governance` (10 layer).
- Metadata standar pada semua dokumen (id, version, status, owner, references).
- `migration/MIGRATION-MAP.md` — pemetaan 61 file legacy → v2.
- `migration/AUDIT-REPORT-V2.md` — audit gabungan docs.zip + canonical.zip.
- ADR register (`03-architecture/adr/`) dengan 6 keputusan kanonik terdokumentasi.
- Evidence Ledger schema & claim governance (`08-commercial/082-evidence-ledger.md`).
- Production gate & enterprise gate sebagai dokumen governance terpisah.

### Changed
- **Terminologi dinormalisasi**: BarberKas = product brand; SparkMind = company brand;
  Outcome Foundry / AaaS / Sovereign / Curator / MoR = istilah **internal** (bukan pesan pembeli).
- Risk register v1 diperluas dengan traceability ke roadmap & gate.
- Roadmap 30/60/90 dikonsolidasikan dari canonical v1 + B5-05 R-series.

### Deprecated / Superseded
- `archive/ssot/` (B4-*, B5-*, FM-*, R6-*, SKILL-AUTHORING-STANDARD) — superseded, tetap
  sebagai referensi sejarah & sumber detail.
- `archive/barberkas-aaas-bundle/` (11 dokumen AaaS v1.0) — superseded.
- `archive/canonical-v1/` (audit baseline 2026-07-10) — kontennya diserap penuh ke v2.

### Removed
- Tidak ada informasi yang dihapus tanpa jejak — semua legacy dipertahankan di `archive/`.
