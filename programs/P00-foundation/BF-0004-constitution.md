---
id: BF-0004
title: Constitution
version: 1.0.0
status: approved
owner: Founder
reviewers: [Founder]
classification: internal
type: policy
last_updated: 2026-07-11
next_review: 2027-01-07
parent: P00-000
related_docs: [BF-0006, BF-0010, F-002]
---
# BF-0004 — Constitution

| Field | Value |
|---|---|
| **ID** | BF-0004 |
| **Version** | 1.0.0 |
| **Status** | Approved |
| **Owner** | Founder |
| **Created** | 2026-07-11 |
| **Updated** | 2026-07-11 |
| **Classification** | Internal |
| **Type** | Policy |
| **References** | [P00-000 Charter](P00-000-program-charter.md), [F-002 Governance](../../canonical/00-foundation/002-governance.md), [BF-0010 Canonical Rules](BF-0010-canonical-rules.md) |

> Hukum tertinggi Barberkas Foundry. Seluruh program (P00–P20), kebijakan,
> standar, agent AI, dan otomasi **terikat** pada pasal-pasal di bawah.
> Amandemen hanya melalui RFC + persetujuan eksplisit Founder.

## Pasal 1 — Kebenaran (Truth-Lock)

1. Hanya klaim yang dapat dibuktikan yang boleh dinyatakan sebagai fakta.
2. Setiap klaim status/kemampuan wajib berlabel **VERIFIED / INFERRED / NOT VERIFIED**.
3. Jika dokumen bertentangan dengan kode/telemetry produksi, **kenyataan menang** —
   dokumen wajib segera dikoreksi.
4. Marketing copy tidak pernah menjadi sumber kebenaran.

## Pasal 2 — Satu Sumber Kebenaran

1. Pengetahuan resmi hanya hidup di dokumen **canonical** yang terdaftar di registry.
2. Dokumen tak terdaftar = orphan = tidak punya otoritas.
3. Duplikasi dilarang; konflik antar dokumen wajib diselesaikan lewat precedence
   ([BF-0010 §4](BF-0010-canonical-rules.md)), bukan dibiarkan.

## Pasal 3 — Manusia di Kemudi (Human-in-the-Loop)

1. Keputusan kelas berikut **wajib** persetujuan manusia, tanpa pengecualian:
   - keputusan yang tidak dapat dibatalkan (irreversible);
   - keamanan, privasi, dan data pelanggan;
   - komitmen komersial dan legal;
   - amandemen konstitusi ini dan perubahan struktur inti (RFC-002).
2. AI agent boleh **mengusulkan, men-draft, dan mengeksekusi** dalam batas mandat;
   tidak pernah **memutuskan** untuk kelas di atas.
3. Setiap override manusia atas usulan sistem dicatat sebagai pelajaran (P09/P10).

## Pasal 4 — Governance sebagai Kode

1. Aturan yang bisa divalidasi mesin **harus** divalidasi mesin (quality gate).
2. Perubahan signifikan mengikuti alur: **RFC → keputusan → ADR/standard → implementasi**.
3. Tidak ada dokumen berstatus `approved` tanpa reviewer tercatat.

## Pasal 5 — Memori Abadi

1. ID dokumen tidak pernah di-reuse; keputusan tidak pernah dihapus — hanya
   di-supersede atau di-archive.
2. Sejarah (ADR, RFC ditolak, migration map, archive) adalah aset, bukan sampah.

## Pasal 6 — Evolusi Terkendali

1. Struktur inti (Empire → Program → Batch → Epic → Task → ADR → Canonical) **dibekukan**;
   yang berevolusi adalah isi dan implementasi.
2. Perubahan struktur inti hanya melalui RFC dengan analisis dampak penuh.
3. Roadmap berjalan spiral: setiap putaran wajib mengevaluasi ulang fondasi.

## Pasal 7 — Batas Brand

1. Foundry adalah mesin **internal**. Istilah internal (Foundry, AaaS, Sovereign, dsb.)
   dilarang muncul di hadapan pembeli ([B-010 Aturan keras](../../canonical/01-brand/010-brand-architecture.md)).

## Amandemen

| Syarat | Ketentuan |
|---|---|
| Usulan | RFC baru dengan analisis dampak ke seluruh program |
| Keputusan | Founder secara eksplisit (tidak dapat didelegasikan ke agent) |
| Pencatatan | Version bump mayor + entri version history + CHANGELOG |

## Version history

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-07-11 | Konstitusi awal — 7 pasal — Batch 00 |
