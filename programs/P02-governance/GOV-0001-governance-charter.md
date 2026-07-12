---
id: GOV-0001
title: Governance Charter
version: 1.0.0
status: approved
owner: Founder
reviewers: [Founder]
classification: internal
type: policy
last_updated: 2026-07-12
next_review: 2027-01-08
parent: P02-000
related_docs: [F-002, G-094, BF-0004, P02-000]
---
# GOV-0001 — Governance Charter

| Field | Value |
|---|---|
| **ID** | GOV-0001 |
| **Version** | 1.0.0 |
| **Status** | Approved |
| **Owner** | Founder |
| **Created** | 2026-07-12 |
| **Updated** | 2026-07-12 |
| **Classification** | Internal |
| **Type** | Policy |
| **References** | [P02-000 Charter](P02-000-program-charter.md), [F-002 Governance](../../canonical/00-foundation/002-governance.md), [BF-0004 Constitution](../P00-foundation/BF-0004-constitution.md), [G-094 Docs Workflows](../../canonical/09-governance/094-docs-governance-workflows.md) |

> Piagam sistem governance enterprise Foundry: **mandat, otoritas, batas,
> dan hierarki norma**. Semua dokumen GOV-0002…GOV-0012 berdiri di atas piagam ini.

## 1. Mandat

Sistem governance Foundry ada untuk menjamin tiga hal — tidak lebih:

| # | Jaminan | Arti |
|---|---|---|
| 1 | **Kualitas** | Setiap artefak (dokumen, kode, keputusan) melewati standar & gate yang terukur |
| 2 | **Akuntabilitas** | Setiap keputusan punya pemilik, jalur, dan bukti yang dapat diaudit |
| 3 | **Arah** | Evolusi enterprise tetap sejalan konstitusi ([BF-0004](../P00-foundation/BF-0004-constitution.md)) & north star |

Governance **bukan** birokrasi: aturan yang tidak melindungi salah satu
jaminan di atas wajib dihapus lewat RFC.

## 2. Hierarki norma

Bila dua aturan bertabrakan, yang lebih tinggi menang:

```
1. Konstitusi          BF-0004 (amandemen hanya via RFC + Founder)
2. Piagam & kebijakan  GOV-0001, F-002, kebijakan (type: policy)
3. Standar             Q-99x, EA-0011/0012, dokumen type: standard
4. Prosedur & SOP      G-094, GOV-0005..0007, type: procedure
5. Guideline           type: guideline — boleh disimpangi dengan alasan tercatat
```

## 3. Otoritas

| Otoritas | Pemegang | Catatan |
|---|---|---|
| Final authority & veto | **Founder** | Termasuk amandemen konstitusi (via RFC) |
| Otoritas domain | Owner layer (Product/Engineering/Security/Operations/Commercial) | Sesuai GOV-0002 Roles |
| Otoritas eksekusi | AI workforce | Mengerjakan; tidak pernah menyetujui (HITL, [AI-070](../../canonical/07-ai/070-ai-agents-policy.md)) |

**Prinsip pemisahan**: yang mengerjakan ≠ yang menyetujui. Selama tim = 1
orang, Founder memegang semua role *acting* namun approval tetap eksplisit
(commit terpisah / catatan review) agar jejak audit tidak hilang.

## 4. Batas sistem governance

Governance **mengatur**: dokumen canonical & programs, keputusan arsitektur
(ADR), perubahan besar (RFC), rilis, risiko, kepatuhan, dan pengecualian.

Governance **tidak mengatur**: isi kreatif eksploratif (draft riset, spike),
folder `archive/` (read-only), dan keputusan operasional harian yang reversibel
& berdampak rendah (GOV-0004 Decision Model mengklasifikasikan ini sebagai Type-C).

## 5. Amandemen piagam

Perubahan GOV-0001 = perubahan besar → wajib RFC + persetujuan Founder +
pencatatan di CHANGELOG. Tidak ada jalur cepat.

## Version history

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-07-12 | Piagam governance enterprise — Batch 02 |
