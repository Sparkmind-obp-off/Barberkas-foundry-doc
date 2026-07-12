---
id: EA-0001
title: Enterprise Architecture
version: 1.0.0
status: approved
owner: Founder
reviewers: [Founder]
classification: internal
type: strategy
last_updated: 2026-07-11
next_review: 2027-01-07
parent: P01-000
related_docs: [EA-0005, EA-0012, A-030]
---
# EA-0001 — Enterprise Architecture

| Field | Value |
|---|---|
| **ID** | EA-0001 |
| **Version** | 1.0.0 |
| **Status** | Approved |
| **Owner** | Founder |
| **Created** | 2026-07-11 |
| **Updated** | 2026-07-11 |
| **Classification** | Internal |
| **Type** | Strategy |
| **References** | [P01-000 Charter](P01-000-program-charter.md), [EA-0005 Layer Architecture](EA-0005-layer-architecture.md), [A-030 System Overview](../../canonical/03-architecture/030-system-overview.md) |

> Dokumen payung Batch 01: **blueprint enterprise Barberkas Foundry** —
> apa yang dimaksud "enterprise" di sini, dari apa ia tersusun, dan bagaimana
> membaca 12 dokumen EA sebagai satu kesatuan.

## 1. Apa yang dimaksud "enterprise"

Enterprise di Foundry = **tiga lapisan yang saling menopang**:

| Lapisan | Isi | SSOT |
|---|---|---|
| **Organisasi (Foundry)** | 21 program, governance, knowledge system, manusia + AI | `programs/` |
| **Produk** | BarberKas (dan produk berikutnya) | `canonical/` |
| **Runtime** | Sistem berjalan: CF Workers, D1, integrasi vendor | source code + [A-030](../../canonical/03-architecture/030-system-overview.md) |

Kesalahan klasik yang dihindari: menyamakan "arsitektur enterprise" dengan
"arsitektur aplikasi". A-030 menjawab *bagaimana BarberKas berjalan*;
EA menjawab *bagaimana seluruh Foundry — pengetahuan, keputusan, produk,
dan sistem — tersusun dan berevolusi*.

## 2. Peta dokumen EA (cara membaca)

```
              EA-0001 (payung — dokumen ini)
                 │
   ┌─────────────┼──────────────────┐
 STRUKTUR      PERILAKU           ATURAN
   │             │                  │
 EA-0002 Context EA-0007 Integration EA-0011 Technology Principles
 EA-0003 Capability EA-0008 Event Model EA-0012 Architecture Principles
 EA-0004 Domain  EA-0009 Data Flow
 EA-0005 Layer   EA-0010 Dependency
 EA-0006 Component
```

| Pertanyaan | Baca |
|---|---|
| Di mana batas enterprise & siapa aktor luarnya? | [EA-0002](EA-0002-context-diagram.md) |
| Kapabilitas apa yang dimiliki/ingin dimiliki? | [EA-0003](EA-0003-capability-map.md) |
| Konsep & entity apa yang jadi bahasa bersama? | [EA-0004](EA-0004-domain-model.md) |
| Bagaimana lapisan tersusun dari visi ke infrastruktur? | [EA-0005](EA-0005-layer-architecture.md) |
| Komponen nyata apa yang ada & statusnya? | [EA-0006](EA-0006-component-architecture.md) |
| Bagaimana bagian-bagian terhubung? | [EA-0007](EA-0007-integration.md), [EA-0008](EA-0008-event-model.md), [EA-0009](EA-0009-data-flow.md) |
| Apa bergantung pada apa? | [EA-0010](EA-0010-dependency-map.md) |
| Aturan memilih teknologi & mendesain? | [EA-0011](EA-0011-technology-principles.md), [EA-0012](EA-0012-architecture-principles.md) |

## 3. Postur arsitektur (jujur, per 2026-07-11)

| Aspek | Kondisi | Label |
|---|---|---|
| Runtime produk | Monolith ringan edge-native (Hono @ CF Workers, D1) | VERIFIED (A-030) |
| Docs-as-code | 56+ dokumen machine-validated, quality gate CI-ready | VERIFIED (RFC-001) |
| Layer organisasi | Program × Batch baru dimulai (Batch 00–01) | VERIFIED (RFC-002) |
| Knowledge graph & intelligence | Baru skema (Q-994); engine belum ada | NOT VERIFIED — target P04+ |
| Otomasi/AI council/orchestration | Belum dibangun | NOT VERIFIED — target P06–P08 |

EA ini sengaja **mendeskripsikan target tanpa memalsukan kondisi sekarang**:
setiap dokumen EA memisahkan "kondisi saat ini" dari "arsitektur target" dengan label bukti.

## 4. Aturan perubahan

1. Perubahan struktur EA (menambah/menghapus dokumen EA-*) = RFC baru.
2. Perubahan isi substansial = bump minor/major + re-review.
3. EA tidak boleh bertentangan dengan ADR approved; bila target EA menuntut
   perubahan ADR → RFC → ADR baru yang men-supersede.

## Version history

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-07-11 | Blueprint payung EA — Batch 01 |
