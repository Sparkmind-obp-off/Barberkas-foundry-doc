---
id: P02-000
title: Program Charter — Governance
version: 1.0.0
status: approved
owner: Founder
reviewers: [Founder]
classification: internal
type: strategy
last_updated: 2026-07-12
next_review: 2027-01-08
parent: PROG-INDEX
related_docs: [RFC-002, P00-000, P01-000, F-002, G-094]
---
# P02-000 — Program Charter — Governance

| Field | Value |
|---|---|
| **ID** | P02-000 |
| **Version** | 1.0.0 |
| **Status** | Approved |
| **Owner** | Founder |
| **Created** | 2026-07-12 |
| **Updated** | 2026-07-12 |
| **Classification** | Internal |
| **Type** | Strategy |
| **References** | [PROG-INDEX](../PROGRAM-INDEX.md), [P00-000 Foundation Charter](../P00-foundation/P00-000-program-charter.md), [P01-000 EA Charter](../P01-enterprise-architecture/P01-000-program-charter.md), [F-002 Governance](../../canonical/00-foundation/002-governance.md), [G-094 Docs Governance Workflows](../../canonical/09-governance/094-docs-governance-workflows.md) |

## Purpose

Program **P02 Governance** menaikkan governance Barberkas Foundry dari
*aturan dokumen tersebar* menjadi **sistem governance enterprise yang utuh**:
siapa memutuskan apa, lewat jalur mana, dengan bukti apa, dan bagaimana
penyimpangan ditangani. Ia menjawab pertanyaan yang belum dijawab penuh oleh
[F-002](../../canonical/00-foundation/002-governance.md) (governance dasar)
dan [G-094](../../canonical/09-governance/094-docs-governance-workflows.md)
(SOP dokumen): governance sebagai **kapabilitas enterprise permanen**, bukan
sekadar kebijakan per-dokumen.

**Posisi terhadap dokumen lama:** F-002 tetap SSOT *prinsip governance dasar*;
G-090…G-097 tetap SSOT *gate & register operasional*. P02 adalah lapisan
**enterprise governance (Foundry)** yang merangkai semuanya — merujuk, tidak
menggantikan. Bila ada kontradiksi, jalurnya RFC.

## Scope

Batch 02 menghasilkan 12 dokumen inti + charter ini:

| ID | Dokumen | Menjawab |
|---|---|---|
| GOV-0001 | Governance Charter | Mandat, otoritas, dan batas sistem governance |
| GOV-0002 | Roles | Peran governance yang diakui + acting rules |
| GOV-0003 | Responsibilities | Tanggung jawab per peran, per lapisan |
| GOV-0004 | Decision Model | Tipe keputusan, jalur, dan siapa berwenang |
| GOV-0005 | Approval Flow | Alur persetujuan end-to-end + SLA |
| GOV-0006 | Review Policy | Kebijakan review berkala & event-driven |
| GOV-0007 | Audit Policy | Audit internal: lingkup, frekuensi, bukti |
| GOV-0008 | Compliance | Kewajiban kepatuhan & cara memenuhinya |
| GOV-0009 | Risk | Kebijakan manajemen risiko enterprise |
| GOV-0010 | Escalation | Jalur eskalasi & trigger-nya |
| GOV-0011 | Exception Handling | Penyimpangan sah: syarat, batas waktu, pencatatan |
| GOV-0012 | Governance Metrics | Metrik kesehatan governance yang diukur |

> Tabel di atas memakai ID polos (belum link) — link diaktifkan saat tiap
> dokumen lahir; status final tercatat di [PROG-INDEX](../PROGRAM-INDEX.md).

**Di luar scope:** registry schema (P03), knowledge graph (P04), mekanisme
HITL detail (P05), serta gate operasional yang sudah hidup di
`canonical/09-governance/` (tetap SSOT di sana).

## Definition of Done (Batch 02)

1. Seluruh 13 dokumen berstatus `approved`, terdaftar di MANIFEST, lolos quality gate.
2. Tidak ada kontradiksi dengan F-002/G-090…G-097 yang approved — bila perlu ubah, jalurnya RFC.
3. PROG-INDEX menandai P02 `Active` → `Canonical`; release tercatat di CHANGELOG.

## Operating rules Batch 02

1. **1 dokumen = 1 commit + 1 push** — setiap dokumen baru langsung
   di-commit dan di-push agar riwayat granular dan tidak ada kerja menggantung.
2. Setiap commit wajib **quality gate PASS** — MANIFEST di-update bersama
   dokumen dalam commit yang sama (anti-orphan).
3. Semua dokumen memakai prefix `GOV-` sesuai [Q-995 §1.1](../../canonical/99-schema/995-numbering.md).

## Version history

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-07-12 | Charter program P02 — pembukaan Batch 02 |
