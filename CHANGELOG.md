# Changelog — Canonical SSOT

Format mengikuti [Keep a Changelog](https://keepachangelog.com/) + SemVer untuk versi repo dokumentasi.

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
