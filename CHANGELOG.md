# Changelog — Canonical SSOT

Format mengikuti [Keep a Changelog](https://keepachangelog.com/) + SemVer untuk versi repo dokumentasi.

## [3.1.0] — 2026-07-11 — "Program × Batch: Batch 00–01" (RFC-002)

Layer organisasi Foundry `programs/` diaktifkan lewat [RFC-002 Program × Batch Operating Model](canonical/10-rfc/RFC-002-program-batch-operating-model.md): 21 program strategis (P00–P20) × 15 batch eksekusi.

### Added — Batch 00 (P00 Foundation — identitas Foundry)
- `programs/` — layer organisasi baru dengan dua index:
  - [PROG-INDEX](programs/PROGRAM-INDEX.md) — registry 21 program strategis P00–P20.
  - [BATCH-INDEX](programs/BATCH-INDEX.md) — roadmap 15 batch (spiral, bukan linear).
- [RFC-002 Program × Batch Operating Model](canonical/10-rfc/RFC-002-program-batch-operating-model.md) — payung layer `programs/`.
- `programs/P00-foundation/` — 11 dokumen identitas:
  [P00-000 Charter](programs/P00-foundation/P00-000-program-charter.md),
  [BF-0001 Vision](programs/P00-foundation/BF-0001-vision.md),
  [BF-0002 Mission](programs/P00-foundation/BF-0002-mission.md),
  [BF-0003 North Star](programs/P00-foundation/BF-0003-north-star.md),
  [BF-0004 Constitution](programs/P00-foundation/BF-0004-constitution.md),
  [BF-0005 Manifest](programs/P00-foundation/BF-0005-manifest.md),
  [BF-0006 Principles](programs/P00-foundation/BF-0006-principles.md),
  [BF-0007 Values](programs/P00-foundation/BF-0007-values.md),
  [BF-0008 Terminology](programs/P00-foundation/BF-0008-terminology.md),
  [BF-0009 Foundry Glossary](programs/P00-foundation/BF-0009-glossary.md),
  [BF-0010 Canonical Rules](programs/P00-foundation/BF-0010-canonical-rules.md).

### Added — Batch 01 (P01 Enterprise Architecture — blueprint sistem)
- `programs/P01-enterprise-architecture/` — 13 dokumen blueprint:
  [P01-000 Charter](programs/P01-enterprise-architecture/P01-000-program-charter.md),
  [EA-0001 Enterprise Architecture](programs/P01-enterprise-architecture/EA-0001-enterprise-architecture.md),
  [EA-0002 Context Diagram](programs/P01-enterprise-architecture/EA-0002-context-diagram.md),
  [EA-0003 Capability Map](programs/P01-enterprise-architecture/EA-0003-capability-map.md),
  [EA-0004 Domain Model](programs/P01-enterprise-architecture/EA-0004-domain-model.md),
  [EA-0005 Layer Architecture](programs/P01-enterprise-architecture/EA-0005-layer-architecture.md),
  [EA-0006 Component Architecture](programs/P01-enterprise-architecture/EA-0006-component-architecture.md),
  [EA-0007 Integration](programs/P01-enterprise-architecture/EA-0007-integration.md),
  [EA-0008 Event Model](programs/P01-enterprise-architecture/EA-0008-event-model.md),
  [EA-0009 Data Flow](programs/P01-enterprise-architecture/EA-0009-data-flow.md),
  [EA-0010 Dependency Map](programs/P01-enterprise-architecture/EA-0010-dependency-map.md),
  [EA-0011 Technology Principles](programs/P01-enterprise-architecture/EA-0011-technology-principles.md) — TP-1..TP-7 + prosedur adopsi/pensiun teknologi,
  [EA-0012 Architecture Principles](programs/P01-enterprise-architecture/EA-0012-architecture-principles.md) — AP-1..AP-10 + trade-off yang diputus.

### Changed
- [tools/validate_docs.py](tools/validate_docs.py) — `DOC_DIRS` diperluas: `canonical`, `migration`, **`programs`** — seluruh layer programs kini machine-validated.
- [MANIFEST.md](MANIFEST.md) v3.1.0 — folder `programs/` + 27 entri baru (RFC-002, PROG/BATCH-INDEX, P00, P01); registry: **83 dokumen**.
- [Q-995 Numbering](canonical/99-schema/995-numbering.md) v3.1.0 — §1.1 prefix layer `programs/`: `PROG-INDEX`/`BATCH-INDEX`, `P<nn>-`, `BF-`, `EA-`.
- [RFC-INDEX](canonical/10-rfc/RFC-INDEX.md) v3.1.0 — registrasi RFC-002.
- [00-INDEX](canonical/00-INDEX.md) v3.1.0 — seksi Programs (PROG-INDEX, BATCH-INDEX, P00, P01).
- [PROG-INDEX](programs/PROGRAM-INDEX.md) v1.1.0 — P00 & P01 → **Canonical**.
- [BATCH-INDEX](programs/BATCH-INDEX.md) v1.1.0 — Batch 00 & 01 → **Done — Canonical**; Batch 02 (P02 Governance) berikutnya.

### Governance
- Quality gate status: **PASSED** — 86 file diperiksa, 83 dokumen bermetadata & terdaftar di MANIFEST.
- Batch 00 & 01 memenuhi definisi selesai [BATCH-INDEX §Aturan batch](programs/BATCH-INDEX.md): seluruh dokumen `approved` + terdaftar + gate PASS + release CHANGELOG ini.

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
