---
id: EA-0003
title: Capability Map
version: 1.0.0
status: approved
owner: Founder
reviewers: [Founder]
classification: internal
type: strategy
last_updated: 2026-07-11
next_review: 2027-01-07
parent: EA-0001
related_docs: [G-095, PROG-INDEX, EA-0010]
---
# EA-0003 — Capability Map

| Field | Value |
|---|---|
| **ID** | EA-0003 |
| **Version** | 1.0.0 |
| **Status** | Approved |
| **Owner** | Founder |
| **Created** | 2026-07-11 |
| **Updated** | 2026-07-11 |
| **Classification** | Internal |
| **Type** | Strategy |
| **References** | [G-095 Capability Map produk](../../canonical/09-governance/095-capability-map-operating-model.md), [PROG-INDEX](../PROGRAM-INDEX.md), [EA-0010 Dependency Map](EA-0010-dependency-map.md) |

> Peta kapabilitas **level enterprise** dan jembatannya ke dua peta yang sudah ada:
> [G-095](../../canonical/09-governance/095-capability-map-operating-model.md)
> (17 capability produk/bisnis) dan [PROG-INDEX](../PROGRAM-INDEX.md) (21 program strategis).
> Tanpa jembatan ini, dua peta itu berisiko tumbuh saling lepas.

## 1. Tiga tingkat kapabilitas

```
Tingkat 1 — ENTERPRISE (dokumen ini)     : 6 kapabilitas makro EC1–EC6
Tingkat 2 — PROGRAM (PROG-INDEX)         : 21 program P00–P20
Tingkat 3 — OPERASIONAL (G-095)          : 17 capability C1.x–C5.x produk/bisnis
```

## 2. Kapabilitas enterprise (EC)

| ID | Kapabilitas enterprise | Deskripsi | Program pendukung | Maturity | Bukti |
|---|---|---|---|:---:|---|
| EC1 | **Knowledge Management** | Menangkap, memvalidasi, menghubungkan, dan memelihara pengetahuan sebagai SSOT | P00, P03, P04, P06 | 3 | VERIFIED — docs-as-code v3 + gate |
| EC2 | **Governance & Decision** | Memutuskan dengan jejak (RFC/ADR), precedence jelas, HITL | P02, P05, P16 | 3 | VERIFIED — RFC/ADR layer aktif |
| EC3 | **Product Delivery** | Membangun & mengoperasikan produk (BarberKas dst.) | P01, P17 | 2 | INFERRED — G-095 C1.x rata-rata 2 |
| EC4 | **Intelligence & Learning** | Memori, pembelajaran, prediksi, AI council | P07–P12, P14 | 1 | NOT VERIFIED — baru skema |
| EC5 | **Autonomy & Evolution** | Self-audit, self-heal, evolusi berkelanjutan | P13, P18, P19 | 1 | NOT VERIFIED — belum dibangun |
| EC6 | **Ecosystem & Legacy** | Relasi antar-repo/produk, warisan lintas generasi | P15, P20 | 1 | NOT VERIFIED — single-repo saat ini |

Skala maturity 1–5 sama dengan G-095 (1 = ad-hoc, 3 = terdefinisi, 5 = teroptimasi).

## 3. Jembatan EC ↔ G-095 (kapabilitas operasional produk)

| EC | Capability G-095 yang menopang |
|---|---|
| EC1 | C5.2 Docs-as-code |
| EC2 | C5.1 Decision governance, C2.2 Risk management |
| EC3 | C1.1–C1.6 (product & engineering), C3.1–C3.3 (operations), C4.1–C4.3 (commercial) |
| EC4 | C1.5 AI assistance (satu-satunya pijakan saat ini) |
| EC5 | — (belum ada; kapabilitas masa depan) |
| EC6 | C2.1 Identity & access (fondasi trust lintas sistem) |

## 4. Aturan penggunaan

1. **Kapabilitas baru masuk lewat peta ini dulu** — sebelum jadi program/fitur,
   tentukan EC induknya; bila tidak muat di EC1–EC6 → RFC (indikasi struktur perlu evolusi).
2. Maturity EC dinilai ulang tiap review kuartalan bersama G-095 —
   nilai EC = agregat jujur dari tingkat di bawahnya, bukan aspirasi.
3. Investasi batch mengikuti gap: batch berikutnya diprioritaskan pada EC
   dengan gap terbesar antara maturity sekarang dan kebutuhan roadmap
   ([BATCH-INDEX](../BATCH-INDEX.md)).
4. Peta ini **tidak menggantikan** G-095 — G-095 tetap SSOT kapabilitas produk/bisnis.

## Version history

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-07-11 | Capability map enterprise EC1–EC6 + jembatan G-095/PROG-INDEX — Batch 01 |
