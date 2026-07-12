---
id: BF-0008
title: Terminology
version: 1.0.0
status: approved
owner: Founder
reviewers: [Founder]
classification: internal
type: standard
last_updated: 2026-07-11
next_review: 2027-01-07
parent: P00-000
related_docs: [BF-0009, F-001]
---
# BF-0008 — Terminology

| Field | Value |
|---|---|
| **ID** | BF-0008 |
| **Version** | 1.0.0 |
| **Status** | Approved |
| **Owner** | Founder |
| **Created** | 2026-07-11 |
| **Updated** | 2026-07-11 |
| **Classification** | Internal |
| **Type** | Standard |
| **References** | [BF-0009 Glossary](BF-0009-glossary.md), [F-001 Glossary produk](../../canonical/00-foundation/001-glossary.md) |

> Istilah **struktural resmi** Barberkas Foundry — kosakata hirarki operasi.
> Definisi tunggal; pemakaian di luar definisi ini = salah pakai.
> Istilah produk/bisnis tetap di [F-001](../../canonical/00-foundation/001-glossary.md);
> kamus gabungan ringkas di [BF-0009](BF-0009-glossary.md).

## Hirarki operasi

```
Empire → Program → Batch → Epic → Task → ADR → Canonical → Knowledge Graph
```

| Istilah | Definisi resmi | Contoh |
|---|---|---|
| **Empire** | Lapisan tertinggi: visi, warisan, dan kesinambungan lintas generasi proyek. Hanya ada **satu**. | Barberkas Foundry Empire |
| **Program** | Kapabilitas strategis permanen yang *dimiliki* organisasi. Ada **21** (P00–P20), dibekukan. | P00 Foundation |
| **Batch** | Gelombang implementasi ber-milestone yang *menyelesaikan* (bagian) program. Satu batch = satu kapabilitas utuh = satu release. | Batch 00 |
| **Epic** | Kelompok pekerjaan besar di dalam batch, satu tema. | P06-E01 Sensors |
| **Task** | Unit kerja terkecil yang bisa diselesaikan dan direview. Format ID: `P<nn>-E<nn>-T<nnn>`. | P06-E01-T001 Git Sensor |
| **ADR** | Architecture Decision Record — keputusan *setelah* diputuskan; permanen. | ADR-003 |
| **RFC** | Request for Comments — usulan *sebelum* diputuskan. | RFC-002 |
| **Canonical** | Status pengetahuan tertinggi: approved + terdaftar di registry + lolos gate. | dokumen di `canonical/` & `programs/` approved |
| **Knowledge Graph** | Jaringan relasi antar dokumen/entity (parent, related, dependency). | Q-994 |
| **Registry** | Daftar resmi dokumen + metadata (MANIFEST, PROG-INDEX). Anti-orphan. | MANIFEST.md |
| **SSOT** | Single Source of Truth — repo ini sebagai acuan tunggal keputusan. | Barberkas-foundry-doc |
| **Quality gate** | Validasi otomatis yang wajib PASS sebelum perubahan diterima. | `tools/validate_docs.py` |
| **HITL** | Human-in-the-Loop — titik keputusan yang wajib manusia. | approval RFC |
| **Spiral** | Model roadmap: setelah batch terakhir kembali ke Batch 00 untuk kalibrasi. | putaran ke-2 Batch 00 |
| **Foundry** | Mesin internal SparkMind yang memproduksi & memelihara produk. **Internal only** — dilarang tampil ke pembeli. | Barberkas Foundry |

## Aturan pemakaian

1. **Program ≠ Batch.** Program = *apa yang dimiliki* (permanen); Batch = *kendaraan pengerjaan* (selesai lalu ditutup).
2. **RFC ≠ ADR.** RFC = usulan; ADR = keputusan. RFC tidak pernah jadi acuan implementasi.
3. **Canonical adalah status, bukan lokasi.** Dokumen draft di folder `canonical/` belum canonical.
4. Istilah baru bertingkat struktural (setara tabel di atas) hanya lewat RFC.
5. Konflik definisi dengan dokumen lain → dokumen ini menang untuk istilah struktural;
   [F-001](../../canonical/00-foundation/001-glossary.md) menang untuk istilah produk.

## Version history

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-07-11 | Terminologi struktural awal — Batch 00 |
