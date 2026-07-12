---
id: BATCH-INDEX
title: Batch Roadmap
version: 1.1.0
status: approved
owner: Founder
reviewers: [Founder]
classification: internal
type: index
last_updated: 2026-07-11
next_review: 2026-10-09
parent: PROG-INDEX
related_docs: [RFC-002]
---
# BATCH-INDEX — Batch Roadmap

| Field | Value |
|---|---|
| **ID** | BATCH-INDEX |
| **Version** | 1.1.0 |
| **Status** | Approved |
| **Owner** | Founder |
| **Created** | 2026-07-11 |
| **Updated** | 2026-07-11 |
| **Classification** | Internal |
| **Type** | Index |
| **References** | [PROG-INDEX](PROGRAM-INDEX.md), [RFC-002](../canonical/10-rfc/RFC-002-program-batch-operating-model.md) |

> Roadmap eksekusi **Program × Batch**. Satu batch = satu kapabilitas utuh =
> satu milestone = satu release dokumentasi. Batch dikerjakan berurutan;
> sebuah batch baru dimulai hanya setelah batch sebelumnya **selesai & canonical**.

## Roadmap

| Batch | Program | Kapabilitas | Dokumen (±) | Status |
|---|---|---|---|---|
| **00** | P00 | Foundation — identitas Foundry | 10 (BF-0001…BF-0010) | ✅ **Done — Canonical** |
| **01** | P01 | Enterprise Architecture — blueprint sistem | 12 (EA-0001…EA-0012) | ✅ **Done — Canonical** |
| 02 | P02 | Governance — charter, decision model, audit | 12 (GOV-…) | ⏭️ **Next** |
| 03 | P03 | Canonical Registry — schema, taxonomy, lifecycle | 10 (CAN-…) | Planned |
| 04 | P04 | Knowledge Graph — entity, relationships, health | 8 (KG-…) | Planned |
| 05 | P05 | Human-in-the-Loop — review, approval, escalation | 8 (HITL-…) | Planned |
| 06 | P06 + P07 | Knowledge Nervous System + AI Council | 20 (KNS-… + AIC-…) | Planned |
| 07 | P08 + P09 | Orchestration + Memory Engine | 18 (ORCH-… + MEM-…) | Planned |
| 08 | P10 + P11 | Learning Engine + Digital Twin | 18 (LEARN-… + DT-…) | Planned |
| 09 | P12 + P13 | Enterprise Intelligence + Autonomous Enterprise | 16 (EI-… + AUTO-…) | Planned |
| 10 | P14 | Foundry Brain | 8 (BRAIN-…) | Planned |
| 11 | P15 + P16 | Ecosystem + Meta Governance | ±16 | Planned |
| 12 | P17 + P18 | Enterprise Operating Model + Continuous Evolution | ±16 | Planned |
| 13 | P19 | Research & Innovation | ±8 | Planned |
| 14 | P20 | Empire Legacy | ±8 | Planned |

**Total ± 178 dokumen inti** dalam 15 batch.

## Siklus spiral

```
00–05 → Foundation    (identitas, arsitektur, governance, knowledge)
06–10 → Intelligence  (KNS, AI Council, orchestration, memory, learning, brain)
11–14 → Legacy        (ecosystem, operating model, evolution, empire)
  ↺  kembali ke Batch 00 — evaluasi visi & prinsip berdasarkan pembelajaran
```

Roadmap **spiral, bukan linear**: setelah Batch 14, putaran berikutnya kembali ke
Batch 00 untuk mengevaluasi visi, prinsip, dan arsitektur berdasarkan pembelajaran.
Setiap putaran membuat Foundry lebih matang tanpa menambah konsep baru yang sulit dipelihara.

## Aturan batch

1. Batch selesai = seluruh dokumennya `approved` + terdaftar di MANIFEST + quality gate PASS
   + tercatat di CHANGELOG sebagai satu release.
2. Prefix dokumen per batch didaftarkan di [Q-995 §1](../canonical/99-schema/995-numbering.md)
   **sebelum** batch dimulai.
3. Perubahan roadmap (menggabung/memecah batch) memerlukan RFC baru.
4. Status di tabel ini di-update setiap batch berpindah status.

## Version history

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-07-11 | Roadmap awal 15 batch × 21 program (RFC-002); Batch 00 dimulai |
| 1.1.0 | 2026-07-11 | Batch 00 (P00, 11 dokumen) & Batch 01 (P01, 13 dokumen) selesai — Canonical; Batch 02 (P02 Governance) berikutnya |
