---
id: PROG-INDEX
title: Program Registry
version: 1.1.0
status: approved
owner: Founder
reviewers: [Founder]
classification: internal
type: index
last_updated: 2026-07-11
next_review: 2027-01-07
parent: F-000
related_docs: [RFC-002, BATCH-INDEX]
---
# PROG-INDEX — Program Registry

| Field | Value |
|---|---|
| **ID** | PROG-INDEX |
| **Version** | 1.1.0 |
| **Status** | Approved |
| **Owner** | Founder |
| **Created** | 2026-07-11 |
| **Updated** | 2026-07-11 |
| **Classification** | Internal |
| **Type** | Index |
| **References** | [RFC-002 Program × Batch Operating Model](../canonical/10-rfc/RFC-002-program-batch-operating-model.md), [BATCH-INDEX](BATCH-INDEX.md) |

> Registry resmi **21 Program strategis Barberkas Foundry (P00–P20)**.
> Program = kapabilitas permanen yang *dimiliki* organisasi.
> Batch = kendaraan eksekusi yang *menyelesaikan* program secara bertahap ([BATCH-INDEX](BATCH-INDEX.md)).
> Struktur inti **dibekukan** (RFC-002 §3.2): yang berkembang adalah isi, bukan kerangka.

## Hirarki operasi

```
Empire (visi & warisan jangka panjang)
 └── Program (21 kapabilitas strategis — dokumen ini)
      └── Batch (gelombang implementasi — BATCH-INDEX)
           └── Epic → Task → ADR → Canonical → Knowledge Graph
```

## Registry Program

| ID | Program | Fase | Fokus | Status | Batch |
|---|---|---|---|---|---|
| P00 | [Foundation](P00-foundation/P00-000-program-charter.md) | Identity | Identitas, konstitusi, prinsip, terminologi, canonical rules | **Canonical** | 00 |
| P01 | [Enterprise Architecture](P01-enterprise-architecture/P01-000-program-charter.md) | Foundation | Blueprint sistem: context, capability map, domain, layer, integrasi | **Canonical** | 01 |
| P02 | Governance | Foundation | Charter governance, roles, decision model, audit, compliance, risk | Planned | 02 |
| P03 | Canonical Registry | Foundation | Registry schema, metadata, taxonomy, ontology, versioning, lifecycle | Planned | 03 |
| P04 | Knowledge Graph | Foundation | Entity model, relationships, semantic search, graph health | Planned | 04 |
| P05 | Human-in-the-Loop | Foundation | Review, approval, override, escalation, delegation, sign-off | Planned | 05 |
| P06 | Knowledge Nervous System | Intelligence | Sensors, perception, synapse, reflex, cortex, memory, learning | Planned | 06 |
| P07 | AI Council | Intelligence | Peran AI: architect, product, security, QA, governance, coordinator | Planned | 06 |
| P08 | Orchestration | Intelligence | Scheduler, planner, workflow, queue, monitoring, recovery | Planned | 07 |
| P09 | Memory Engine | Intelligence | Working/long-term/decision/experience memory, pattern library | Planned | 07 |
| P10 | Learning Engine | Intelligence | Learning pipeline, pattern mining, prompt/knowledge/policy evolution | Planned | 08 |
| P11 | Digital Twin | Autonomy | Twin organisasi: teams, projects, processes, assets, simulation | Planned | 08 |
| P12 | Enterprise Intelligence | Autonomy | Prediction, recommendation, gap detection, decision support | Planned | 09 |
| P13 | Autonomous Enterprise | Autonomy | Self audit, self heal, self optimize, self documentation, self review | Planned | 09 |
| P14 | Foundry Brain | Autonomy | Strategic/product/engineering/governance/knowledge/learning brain | Planned | 10 |
| P15 | Ecosystem | Legacy | Hubungan antar-repo, produk, layanan, SDK, API, dependensi lintas proyek | Planned | 11 |
| P16 | Meta Governance | Legacy | Governance atas governance: bagaimana kebijakan dibuat & dipensiunkan | Planned | 11 |
| P17 | Enterprise Operating Model | Legacy | Peran, alur kerja, ritme rilis, kolaborasi manusia–AI | Planned | 12 |
| P18 | Continuous Evolution | Legacy | Evaluasi berkala, metrics, retrospektif, perbaikan berbasis data | Planned | 12 |
| P19 | Research & Innovation | Legacy | Ide, eksperimen, prototipe, riset → dipromosikan jadi standar/produk | Planned | 13 |
| P20 | Empire Legacy | Legacy | Visi jangka panjang, warisan pengetahuan, kesinambungan lintas generasi | Planned | 14 |

## Aturan status program

| Status | Arti |
|---|---|
| `Planned` | Terdaftar; folder & dokumen belum dibuka |
| `Active` | Batch-nya sedang berjalan; folder `P<nn>-<slug>/` sudah ada |
| `Canonical` | Batch selesai penuh; seluruh dokumen approved & masuk knowledge graph |
| `Evolving` | Putaran spiral berikutnya — direvisi berdasarkan pembelajaran |

## Aturan

1. Program **tidak pernah dihapus atau diganti nomor** — sama seperti aturan ID [Q-995](../canonical/99-schema/995-numbering.md).
2. Folder program (`P<nn>-<slug>/`) baru dibuat ketika batch-nya mulai berjalan (lazy activation).
3. Setiap program dibuka dengan **Program Charter** (`P<nn>-000-program-charter.md`) sebagai parent seluruh dokumennya.
4. Roadmap bersifat **spiral**: setelah Batch 14 selesai, kembali ke Batch 00 untuk evaluasi ([RFC-002 §3.2.5](../canonical/10-rfc/RFC-002-program-batch-operating-model.md)).

## Version history

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-07-11 | Registry awal 21 program (RFC-002); P00 diaktifkan via Batch 00 |
| 1.1.0 | 2026-07-11 | Batch 00 & 01 selesai: P00 Foundation dan P01 Enterprise Architecture → **Canonical** (charter + BF-0001..0010, EA-0001..0012) |
