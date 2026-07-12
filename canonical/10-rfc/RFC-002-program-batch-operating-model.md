---
id: RFC-002
title: Program × Batch Operating Model
version: 1.0.0
status: approved
owner: Founder
reviewers: [Founder]
classification: internal
type: rfc
last_updated: 2026-07-11
next_review: 2026-10-09
parent: RFC-INDEX
related_docs: [RFC-001, F-002, Q-995]
---
# RFC-002 — Program × Batch Operating Model

| Field | Value |
|---|---|
| **ID** | RFC-002 |
| **Status** | Accepted → Implemented (Batch 00) |
| **Author** | Founder |
| **Created** | 2026-07-11 |
| **Decided** | 2026-07-11 |
| **Decision** | Adopsi model Program × Batch; implementasi dimulai Batch 00 |
| **Type** | RFC |
| **References** | [RFC-INDEX](RFC-INDEX.md), [F-002 Governance](../00-foundation/002-governance.md), [Q-995 Numbering](../99-schema/995-numbering.md) |

## 1. Summary

Mengangkat repo ini dari **Knowledge Repository** (SSOT v3) menjadi
**program arsitektur & governance jangka panjang** dengan model **Program × Batch**:

- **21 Program strategis (P00–P20)** = kapabilitas yang *dimiliki* organisasi.
- **Batch implementasi** = gelombang pengerjaan yang *menyelesaikan* program secara bertahap.
- Hirarki penuh: `Empire → Program → Batch → Epic → Task → ADR → Canonical → Knowledge Graph`.

## 2. Motivation

**VERIFIED** (audit repo v3.0.0, 2026-07-11):

1. SSOT v3 sudah machine-validated (56 dokumen, 8 quality gate) — fondasi docs-as-code selesai (RFC-001).
2. Namun belum ada **struktur program jangka panjang**: tidak ada peta kapabilitas strategis
   Foundry (di luar produk BarberKas), tidak ada roadmap batch bertingkat, dan tidak ada
   identitas Foundry sebagai entitas di atas produk.
3. Diskusi arah (chat log 2026-07-10/11) menyimpulkan dua kandidat model:
   - Versi A: 15 batch implementasi (fokus *apa yang dikerjakan*).
   - Versi B: 21 program P00–P20 (fokus *apa yang dimiliki*).

**Keputusan:** gabungkan keduanya — Program sebagai struktur permanen, Batch sebagai kendaraan eksekusi.

## 3. Proposal

### 3.1 Struktur baru

```
programs/                          # layer baru (di-validate quality gate)
├── PROGRAM-INDEX.md               # registry 21 program P00–P20
├── BATCH-INDEX.md                 # roadmap batch + mapping Program × Batch
└── P00-foundation/                # satu folder per program (dibuka saat batch-nya jalan)
    ├── P00-000-program-charter.md
    └── BF-0001-vision.md … BF-0010-canonical-rules.md
```

### 3.2 Aturan

1. **Struktur inti dibekukan**: 1 Empire, 21 Program, batch eksekusi bertahap.
   Yang berkembang adalah *isi*, bukan kerangka.
2. Setiap batch = satu kapabilitas utuh → selesai sebagai satu kesatuan → menjadi canonical → satu release.
3. Program docs tunduk pada seluruh standar 99-schema (front-matter Q-991, lifecycle Q-993,
   manifest anti-orphan, quality gate `tools/validate_docs.py`).
4. Penomoran baru didaftarkan di [Q-995 §1](../99-schema/995-numbering.md):
   prefix `PROG-`/`P<nn>` untuk program, `BF-` (batch Foundation), prefix batch lain menyusul per batch.
5. Roadmap bersifat **spiral, bukan linear**: setelah batch terakhir, kembali ke Batch 00
   untuk evaluasi berdasarkan pembelajaran.
6. Relasi dengan canonical produk: `canonical/` tetap SSOT produk BarberKas;
   `programs/` adalah lapisan Foundry (organisasi) di atasnya. Bila konflik → precedence F-000 §Otoritas berlaku,
   dan BF-0010 Canonical Rules mengatur jembatan keduanya.

### 3.3 Daftar 21 Program

P00 Foundation · P01 Enterprise Architecture · P02 Governance · P03 Canonical Registry ·
P04 Knowledge Graph · P05 Human-in-the-Loop · P06 Knowledge Nervous System · P07 AI Council ·
P08 Orchestration · P09 Memory Engine · P10 Learning Engine · P11 Digital Twin ·
P12 Enterprise Intelligence · P13 Autonomous Enterprise · P14 Foundry Brain · P15 Ecosystem ·
P16 Meta Governance · P17 Enterprise Operating Model · P18 Continuous Evolution ·
P19 Research & Innovation · P20 Empire Legacy.

Detail scope tiap program: [PROGRAM-INDEX](../../programs/PROGRAM-INDEX.md).

## 4. Alternatives considered

| Alternatif | Alasan ditolak |
|---|---|
| Per-dokumen (tanpa batch) | Struktur berubah terus; tidak pernah ada unit "selesai & canonical" |
| Hanya 15 batch (Versi A) | Tidak merekam kapabilitas permanen; roadmap habis setelah batch terakhir |
| Hanya 21 program (Versi B) | Terlalu abstrak; tidak ada kendaraan eksekusi yang realistis |
| Folder baru di `canonical/` (mis. `11-programs/`) | Mencampur SSOT produk dengan layer organisasi; nomor layer produk jadi rancu |

## 5. Impact

- **Baru:** `programs/` (PROGRAM-INDEX, BATCH-INDEX, P00 + 10 dokumen BF Batch 00).
- **Diubah:** Q-995 (prefix baru), MANIFEST (registry), 00-INDEX, README, CHANGELOG,
  `tools/validate_docs.py` (folder `programs/` masuk cakupan gate).
- **Tidak diubah:** seluruh isi `canonical/` v3 dan `archive/`.

## 6. Rollout

| Tahap | Isi | Status |
|---|---|---|
| Batch 00 | Foundation (P00): BF-0001–BF-0010 + framework programs/ | ✅ RFC ini |
| Batch 01+ | Sesuai [BATCH-INDEX](../../programs/BATCH-INDEX.md) | Direncanakan |

## Version history

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-07-11 | RFC diajukan, diputuskan, dan mulai diimplementasikan (Batch 00) |
