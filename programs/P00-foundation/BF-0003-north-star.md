---
id: BF-0003
title: North Star
version: 1.0.0
status: approved
owner: Founder
reviewers: [Founder]
classification: internal
type: strategy
last_updated: 2026-07-11
next_review: 2027-01-07
parent: P00-000
related_docs: [BF-0001, BF-0002]
---
# BF-0003 — North Star

| Field | Value |
|---|---|
| **ID** | BF-0003 |
| **Version** | 1.0.0 |
| **Status** | Approved |
| **Owner** | Founder |
| **Created** | 2026-07-11 |
| **Updated** | 2026-07-11 |
| **Classification** | Internal |
| **Type** | Strategy |
| **References** | [BF-0001 Vision](BF-0001-vision.md), [BF-0002 Mission](BF-0002-mission.md), [P-021 ICP & JTBD](../../canonical/02-product/021-icp-and-jtbd.md) |

## North Star Foundry

> **Verified Knowledge Utilization (VKU)** — proporsi keputusan (manusia maupun agent)
> yang diambil dengan mengacu pada dokumen canonical yang valid, terkini, dan terverifikasi.

Jika VKU tinggi: SSOT benar-benar dipakai, bukan pajangan. Jika VKU rendah:
ada pengetahuan yang usang, sulit ditemukan, atau tidak dipercaya — itu sinyal
perbaikan paling prioritas.

## Metric tree

```
VKU (North Star)
├── Coverage   : % area keputusan yang punya dokumen canonical approved
├── Freshness  : % dokumen dengan next_review belum lewat
├── Integrity  : quality gate pass rate (target: 100% di main)
├── Findability: waktu rata-rata menemukan dokumen acuan (via index/graph)
└── Adoption   : % RFC/ADR/PR yang mengutip dokumen canonical sebagai basis
```

## Guardrail metrics (tidak boleh memburuk demi VKU)

| Guardrail | Ambang |
|---|---|
| Human approval tetap ada untuk keputusan kelas kritis | 100% (tanpa pengecualian) |
| Lead time batch (mulai → canonical) | Tidak memburuk 2 batch berturut-turut |
| Beban review manusia | Tidak melebihi kapasitas yang disepakati di P05 |

## Relasi dengan North Star produk

North Star produk BarberKas (activation & retention pelanggan barbershop —
[P-021](../../canonical/02-product/021-icp-and-jtbd.md)) **tetap terpisah dan berdaulat**.
VKU adalah north star *mesin pengetahuannya*; hipotesisnya: VKU yang sehat
mempercepat dan memperjujur setiap keputusan produk.

## Kadens pengukuran

| Ritme | Aktivitas |
|---|---|
| Setiap commit | Integrity (quality gate CI) |
| Setiap batch release | Coverage, Freshness, Adoption |
| Setiap putaran spiral (kembali ke Batch 00) | Review penuh metric tree + kalibrasi ambang |

Formal baseline & scorecard akan ditetapkan di P18 Continuous Evolution;
sampai saat itu, pengukuran dilakukan manual saat release batch.

## Version history

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-07-11 | Dokumen awal — Batch 00 |
