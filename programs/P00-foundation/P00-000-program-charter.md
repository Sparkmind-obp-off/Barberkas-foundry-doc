---
id: P00-000
title: Program Charter — Foundation
version: 1.0.0
status: approved
owner: Founder
reviewers: [Founder]
classification: internal
type: strategy
last_updated: 2026-07-11
next_review: 2027-01-07
parent: PROG-INDEX
related_docs: [RFC-002, BATCH-INDEX, F-000]
---
# P00-000 — Program Charter — Foundation

| Field | Value |
|---|---|
| **ID** | P00-000 |
| **Version** | 1.0.0 |
| **Status** | Approved |
| **Owner** | Founder |
| **Created** | 2026-07-11 |
| **Updated** | 2026-07-11 |
| **Classification** | Internal |
| **Type** | Strategy |
| **References** | [PROG-INDEX](../PROGRAM-INDEX.md), [RFC-002](../../canonical/10-rfc/RFC-002-program-batch-operating-model.md), [F-000 Charter](../../canonical/00-foundation/000-charter.md) |

## Purpose

Program **P00 Foundation** membangun **identitas Barberkas Foundry** sebagai entitas
organisasi di atas produk: siapa kami, mengapa kami ada, ke mana kami menuju,
aturan apa yang tidak boleh dilanggar, dan bagaimana pengetahuan menjadi canonical.

P00 adalah **root** seluruh program lain — P01–P20 tidak boleh bertentangan dengan
dokumen P00 yang berstatus approved.

## Scope

Batch 00 menghasilkan 10 dokumen inti:

| ID | Dokumen | Menjawab |
|---|---|---|
| [BF-0001](BF-0001-vision.md) | Vision | Dunia seperti apa yang ingin diwujudkan |
| [BF-0002](BF-0002-mission.md) | Mission | Apa yang kami kerjakan setiap hari untuk mencapainya |
| [BF-0003](BF-0003-north-star.md) | North Star | Satu ukuran arah yang tidak boleh hilang |
| [BF-0004](BF-0004-constitution.md) | Constitution | Hukum tertinggi Foundry — pasal yang mengikat semua program |
| [BF-0005](BF-0005-manifest.md) | Manifest | Pernyataan sikap: apa yang kami percayai & tolak |
| [BF-0006](BF-0006-principles.md) | Principles | Prinsip kerja operasional yang menurunkan konstitusi |
| [BF-0007](BF-0007-values.md) | Values | Nilai budaya yang menuntun perilaku manusia & agent |
| [BF-0008](BF-0008-terminology.md) | Terminology | Istilah resmi Foundry (Empire, Program, Batch, …) |
| [BF-0009](BF-0009-glossary.md) | Glossary | Kamus ringkas seluruh istilah lintas program |
| [BF-0010](BF-0010-canonical-rules.md) | Canonical Rules | Aturan bagaimana pengetahuan menjadi canonical |

**Di luar scope:** arsitektur sistem (P01), governance operasional (P02),
registry teknis (P03) — masing-masing punya program sendiri.

## Relasi dengan Canonical SSOT produk

- `canonical/` (F-000 dst.) = SSOT **produk BarberKas**.
- `programs/P00/` = identitas **Barberkas Foundry** (organisasi/foundry di atas produk).
- Precedence bila konflik: BF-0004 Constitution → F-000 Charter → dokumen lain
  (diatur rinci di [BF-0010 §4](BF-0010-canonical-rules.md)).

## Definition of Done (Batch 00)

1. Seluruh 10 dokumen berstatus `approved`, terdaftar di MANIFEST, lolos quality gate.
2. PROG-INDEX menandai P00 = `Active` → `Canonical` setelah review putaran pertama.
3. Release tercatat di CHANGELOG.

## Version history

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-07-11 | Charter program P00 — pembukaan Batch 00 |
