---
id: BF-0006
title: Principles
version: 1.0.0
status: approved
owner: Founder
reviewers: [Founder]
classification: internal
type: standard
last_updated: 2026-07-11
next_review: 2027-01-07
parent: P00-000
related_docs: [BF-0004, BF-0005, BF-0007]
---
# BF-0006 — Principles

| Field | Value |
|---|---|
| **ID** | BF-0006 |
| **Version** | 1.0.0 |
| **Status** | Approved |
| **Owner** | Founder |
| **Created** | 2026-07-11 |
| **Updated** | 2026-07-11 |
| **Classification** | Internal |
| **Type** | Standard |
| **References** | [BF-0004 Constitution](BF-0004-constitution.md), [BF-0007 Values](BF-0007-values.md) |

> 10 prinsip kerja operasional yang menurunkan konstitusi menjadi keputusan sehari-hari.
> Format tiap prinsip: pernyataan → artinya dalam praktik → anti-pola.

## PR-01 — Evidence before claim

Klaim mengikuti bukti, bukan sebaliknya.
**Praktik:** label VERIFIED/INFERRED/NOT VERIFIED di setiap klaim status.
**Anti-pola:** menulis "done" di feature matrix karena kode "hampir jadi".

## PR-02 — Registry or it doesn't exist

Pengetahuan yang tidak terdaftar tidak punya otoritas.
**Praktik:** setiap dokumen baru langsung masuk MANIFEST + front-matter lengkap.
**Anti-pola:** catatan penting hidup di chat/notion/kepala orang.

## PR-03 — One change, many artifacts

Satu perubahan pengetahuan harus terpropagasi: registry, index, graph, changelog.
**Praktik:** checklist release batch; ke depan diotomasi (P08 Orchestration).
**Anti-pola:** update dokumen tanpa update index/manifest.

## PR-04 — Propose loudly, decide formally

Ide bebas diajukan (RFC), keputusan selalu formal (ADR/approval).
**Praktik:** perubahan signifikan dimulai dari RFC; keputusan dicatat dengan konteksnya.
**Anti-pola:** keputusan besar "disepakati lisan" lalu hilang.

## PR-05 — Human gate for heavy doors

Pintu berat (irreversible/security/commercial) hanya dibuka manusia.
**Praktik:** daftar kelas keputusan HITL di [BF-0004 Pasal 3](BF-0004-constitution.md).
**Anti-pola:** auto-merge perubahan kebijakan karena "CI hijau".

## PR-06 — Small batches, finished batches

Kerjakan per batch kapabilitas utuh; selesaikan tuntas sebelum lanjut.
**Praktik:** satu batch = satu milestone = satu release ([BATCH-INDEX](../BATCH-INDEX.md)).
**Anti-pola:** membuka lima batch paralel, tidak satu pun canonical.

## PR-07 — Machine-validate everything validatable

Aturan yang bisa dicek mesin tidak boleh bergantung pada ingatan manusia.
**Praktik:** quality gate `tools/validate_docs.py` wajib PASS di setiap commit.
**Anti-pola:** review manual untuk hal yang bisa di-lint.

## PR-08 — Memory is sacred

ID permanen, keputusan tidak dihapus, pelajaran dicatat.
**Praktik:** supersede/archive, jangan delete; lessons learned per batch.
**Anti-pola:** force-push yang menghapus sejarah; reuse ID dokumen lama.

## PR-09 — Frozen skeleton, living flesh

Struktur inti stabil; isi berevolusi cepat.
**Praktik:** perubahan struktur = RFC; perubahan isi = alur normal.
**Anti-pola:** reorganisasi folder besar-besaran tiap kali ada ide baru.

## PR-10 — Spiral, not straight line

Setiap putaran kembali ke fondasi untuk kalibrasi berdasarkan pembelajaran.
**Praktik:** setelah batch terakhir, buka kembali Batch 00 dengan lensa retro.
**Anti-pola:** roadmap linear yang tidak pernah menoleh ke belakang.

## Version history

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-07-11 | 10 prinsip awal — Batch 00 |
