---
id: BF-0009
title: Foundry Glossary
version: 1.0.0
status: approved
owner: Founder
reviewers: [Founder]
classification: internal
type: standard
last_updated: 2026-07-11
next_review: 2027-01-07
parent: P00-000
related_docs: [BF-0008, F-001]
---
# BF-0009 — Foundry Glossary

| Field | Value |
|---|---|
| **ID** | BF-0009 |
| **Version** | 1.0.0 |
| **Status** | Approved |
| **Owner** | Founder |
| **Created** | 2026-07-11 |
| **Updated** | 2026-07-11 |
| **Classification** | Internal |
| **Type** | Standard |
| **References** | [BF-0008 Terminology](BF-0008-terminology.md), [F-001 Glossary produk](../../canonical/00-foundation/001-glossary.md) |

> Kamus **ringkas lintas program** — satu tempat mencari arti istilah apa pun di Foundry.
> Aturan otoritas: istilah **struktural** → definisi penuh di [BF-0008](BF-0008-terminology.md);
> istilah **produk/bisnis** → definisi penuh di [F-001](../../canonical/00-foundation/001-glossary.md).
> Bila entri di sini bertentangan dengan sumber otoritatifnya, sumber otoritatif menang.

## A–F

| Istilah | Arti ringkas | Otoritas |
|---|---|---|
| **AaaS** | Agent-as-a-Service — pola delivery outcome via skill agentik. Internal only. | F-001 |
| **ADR** | Keputusan arsitektur permanen (setelah diputuskan). | BF-0008 |
| **BarberKas** | Produk pertama Foundry: SaaS operasional barbershop. | F-001 |
| **Barberkas Foundry** | Mesin/organisasi internal yang memproduksi & memelihara produk. | BF-0008 |
| **Batch** | Gelombang implementasi; satu batch = satu kapabilitas utuh = satu release. | BF-0008 |
| **Canonical** | Status pengetahuan tertinggi: approved + terdaftar + lolos gate. | BF-0008 |
| **Constitution** | Hukum tertinggi Foundry ([BF-0004](BF-0004-constitution.md)); precedence di atas semua dokumen. | BF-0004 |
| **Curator** | Peran manusia pengkurasi output agent. Internal only. | F-001 |
| **Empire** | Lapisan tertinggi: visi & warisan lintas generasi. Hanya satu. | BF-0008 |
| **Epic** | Kelompok pekerjaan satu tema di dalam batch. | BF-0008 |
| **Evidence Ledger** | Register bukti klaim publik ([C-082](../../canonical/08-commercial/082-evidence-ledger.md)). | F-001 |
| **Foundry** | Sinonim pendek Barberkas Foundry. Dilarang tampil ke pembeli. | BF-0008 |

## G–P

| Istilah | Arti ringkas | Otoritas |
|---|---|---|
| **HITL** | Human-in-the-Loop — titik keputusan yang wajib manusia. | BF-0008 |
| **Knowledge Graph** | Jaringan relasi antar dokumen/entity ([Q-994](../../canonical/99-schema/994-knowledge-graph.md)). | BF-0008 |
| **Lifecycle** | State machine dokumen Draft→Review→Approved→Deprecated→Archived ([Q-993](../../canonical/99-schema/993-lifecycle.md)). | Q-993 |
| **Manifest (registry)** | [MANIFEST.md](../../MANIFEST.md) — registry anti-orphan seluruh dokumen. | BF-0008 |
| **Manifest (sikap)** | [BF-0005](BF-0005-manifest.md) — pernyataan apa yang dipercayai & ditolak. | BF-0005 |
| **MoR** | Merchant of Record — pola pembayaran internal via Duitku ([ADR-003](../../canonical/03-architecture/adr/ADR-003-duitku-mor-payment.md)). | F-001 |
| **North Star** | Satu ukuran arah utama ([BF-0003](BF-0003-north-star.md)). | BF-0003 |
| **Orphan** | Dokumen ber-ID yang tidak terdaftar di MANIFEST → gagal gate. | Q-991 |
| **Program** | Kapabilitas strategis permanen; ada 21 (P00–P20), dibekukan. | BF-0008 |

## Q–Z

| Istilah | Arti ringkas | Otoritas |
|---|---|---|
| **Quality gate** | Validasi otomatis wajib PASS (`tools/validate_docs.py`). | BF-0008 |
| **Registry** | Daftar resmi dokumen + metadata (MANIFEST, PROG-INDEX). | BF-0008 |
| **RFC** | Usulan sebelum diputuskan; bukan acuan implementasi. | BF-0008 |
| **Sovereign** | Prinsip kedaulatan data/operasi tenant. Internal only. | F-001 |
| **Spiral** | Model roadmap: setelah batch terakhir kembali ke Batch 00. | BF-0008 |
| **SSOT** | Single Source of Truth — repo ini. | BF-0008 |
| **Task** | Unit kerja terkecil; format `P<nn>-E<nn>-T<nnn>`. | BF-0008 |
| **Truth-Lock** | Disiplin klaim berlabel bukti VERIFIED / INFERRED / NOT VERIFIED. | F-001 |

## Aturan pemeliharaan

1. Entri baru ditambahkan saat batch baru memperkenalkan istilah baru — dalam commit yang sama.
2. Kamus ini **tidak pernah** menjadi sumber definisi; ia hanya indeks. Definisi = kolom Otoritas.
3. Istilah internal (Foundry, AaaS, Sovereign, Curator, MoR) dilarang di materi publik
   ([BF-0004 Pasal 7](BF-0004-constitution.md), [B-011](../../canonical/01-brand/011-positioning-and-messaging.md)).

## Version history

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-07-11 | Kamus lintas program awal — Batch 00 |
