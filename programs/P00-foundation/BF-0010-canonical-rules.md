---
id: BF-0010
title: Canonical Rules
version: 1.0.0
status: approved
owner: Founder
reviewers: [Founder]
classification: internal
type: policy
last_updated: 2026-07-11
next_review: 2027-01-07
parent: P00-000
related_docs: [BF-0004, Q-993, F-002]
---
# BF-0010 — Canonical Rules

| Field | Value |
|---|---|
| **ID** | BF-0010 |
| **Version** | 1.0.0 |
| **Status** | Approved |
| **Owner** | Founder |
| **Created** | 2026-07-11 |
| **Updated** | 2026-07-11 |
| **Classification** | Internal |
| **Type** | Policy |
| **References** | [BF-0004 Constitution](BF-0004-constitution.md), [Q-993 Lifecycle](../../canonical/99-schema/993-lifecycle.md), [F-002 Governance](../../canonical/00-foundation/002-governance.md) |

> Aturan tunggal **bagaimana pengetahuan menjadi canonical** di seluruh Foundry —
> berlaku untuk `canonical/` (SSOT produk) dan `programs/` (layer organisasi).
> Canonical adalah **status**, bukan lokasi ([BF-0008](BF-0008-terminology.md)).

## 1. Syarat canonical

Sebuah dokumen berstatus canonical jika — dan hanya jika — **seluruh** syarat terpenuhi:

| # | Syarat | Divalidasi oleh |
|---|---|---|
| 1 | Front-matter lengkap & valid ([Q-991](../../canonical/99-schema/991-metadata-schema.md)) | quality gate |
| 2 | `status: approved` + reviewers tidak kosong | quality gate |
| 3 | Terdaftar di [MANIFEST](../../MANIFEST.md) (anti-orphan) | quality gate |
| 4 | `parent` & `related_docs` tidak dangling | quality gate |
| 5 | Tidak ada broken link | quality gate |
| 6 | Klaim penting berlabel bukti (Truth-Lock) | reviewer manusia |
| 7 | Tidak bertentangan dengan dokumen precedence lebih tinggi (§4) | reviewer manusia |

Syarat 1–5 dicek mesin (`tools/validate_docs.py`); syarat 6–7 adalah tanggung jawab
reviewer manusia (HITL) — mesin tidak pernah meng-approve sendiri
([BF-0004 Pasal 3](BF-0004-constitution.md)).

## 2. Jalur menuju canonical

```
draft ──► review ──► approved(+registered+gate PASS) = CANONICAL
  ▲                       │
  └── revisi minor ◄──────┘        deprecated ──► archived (ID tetap hidup)
```

1. **Draft** — boleh dibuat siapa pun (manusia/agent); belum boleh dirujuk sebagai acuan.
2. **Review** — minimal satu reviewer manusia; keputusan dicatat.
3. **Approved** — masuk MANIFEST dalam commit yang sama; gate wajib PASS.
4. **Perubahan** setelah approved = bump version (SemVer) + version history + re-review
   bila substansial ([Q-993](../../canonical/99-schema/993-lifecycle.md)).
5. **Deprecated/Archived** — ID tidak pernah di-reuse ([Q-995](../../canonical/99-schema/995-numbering.md)).

## 3. Aturan batch (RFC-002)

1. Satu batch = satu unit canonical: batch **tidak dianggap selesai** sampai seluruh
   dokumennya canonical + CHANGELOG mencatatnya sebagai satu release.
2. Prefix ID batch didaftarkan di [Q-995 §1](../../canonical/99-schema/995-numbering.md)
   *sebelum* dokumen pertama ditulis.
3. Dokumen batch yang setengah jadi berstatus `draft`/`review` — boleh di-commit,
   tetapi PROG-INDEX tetap menandai batch `In progress`.

## 4. Precedence (jembatan `programs/` × `canonical/`)

Bila dua dokumen approved saling bertentangan, urutan yang menang:

```
1. BF-0004 Constitution           (hukum tertinggi Foundry)
2. F-000 Charter + F-002 Governance  (otoritas SSOT produk)
3. Policy / Standard approved     (Q-99x, BF-00xx, dokumen layer)
4. Specification / Guideline / Runbook
5. Index / Report                 (tidak pernah jadi sumber kebenaran)
```

Aturan tambahan:

1. **Domain scope**: `programs/` mengatur *organisasi Foundry*; `canonical/` mengatur
   *produk BarberKas*. Konflik lintas domain diselesaikan di level konstitusi/charter,
   bukan dengan mengedit dokumen level bawah.
2. Istilah struktural → [BF-0008](BF-0008-terminology.md) menang;
   istilah produk → [F-001](../../canonical/00-foundation/001-glossary.md) menang.
3. Deteksi konflik adalah tugas reviewer; konflik yang lolos = bug governance →
   dicatat sebagai lesson learned.

## 5. Larangan

1. Meng-approve dokumen sendiri tanpa reviewer (walau owner).
2. Menandai canonical tanpa entri MANIFEST (orphan).
3. Mengedit RFC setelah decided; mengedit dokumen `migration/`/`archive/` (frozen).
4. Menurunkan status approved → draft tanpa jejak version history.
5. Klaim "canonical"/"enterprise-ready" di materi publik tanpa bukti
   ([C-082](../../canonical/08-commercial/082-evidence-ledger.md)).

## Version history

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-07-11 | Aturan canonical lintas repo — penutup Batch 00 |
