---
id: EA-0008
title: Event Model
version: 1.0.0
status: approved
owner: Founder
reviewers: [Founder]
classification: internal
type: specification
last_updated: 2026-07-11
next_review: 2027-01-07
parent: EA-0001
related_docs: [EA-0007, EA-0009, EA-0004]
---
# EA-0008 — Event Model

| Field | Value |
|---|---|
| **ID** | EA-0008 |
| **Version** | 1.0.0 |
| **Status** | Approved |
| **Owner** | Founder |
| **Created** | 2026-07-11 |
| **Updated** | 2026-07-11 |
| **Classification** | Internal |
| **Type** | Specification |
| **References** | [EA-0007 Integration](EA-0007-integration.md), [EA-0009 Data Flow](EA-0009-data-flow.md), [EA-0004 Domain Model](EA-0004-domain-model.md) |

> Katalog **event yang diakui** enterprise: event bisnis (produk), event sistem,
> dan event knowledge/governance. Penting untuk kejujuran arsitektur: hari ini
> **tidak ada event bus** — event diproses sinkron di dalam request/webhook.
> Katalog ini adalah bahasa bersama + fondasi bila kelak event-driven
> sungguhan dibangun (P06/P08).

## 1. Kondisi saat ini (jujur)

| Aspek | Kondisi |
|---|---|
| Event bus / queue | **Tidak ada** — NOT VERIFIED |
| Pemrosesan event | Sinkron dalam handler HTTP/webhook (Hono @ CF Workers) |
| Persistensi event | Tidak ada event store; state disimpan sebagai row D1 |
| Konsekuensi | "Event" di dokumen ini = kejadian domain yang dikenali kode, bukan message |

## 2. Event bisnis (domain D3 — produk)

| Event | Pemicu | Efek | Bukti |
|---|---|---|---|
| `booking.requested` | Customer via WA / owner via dashboard | FSM booking mulai | VERIFIED (fitur FSM) |
| `booking.confirmed` | FSM lengkap + slot valid | Row booking tersimpan; balasan WA | VERIFIED |
| `payment.invoice_created` | Checkout dimulai | Invoice Duitku dibuat (I-2) | VERIFIED |
| `payment.callback_received` | Duitku memanggil webhook (I-3) | Verifikasi signature → update status bayar | VERIFIED |
| `wa.message_received` | Fonnte webhook (I-4) | Mapping device→tenant → route ke FSM/AI | VERIFIED |
| `ai.reply_generated` | Assistant menjawab | Balasan terkirim via I-5 | VERIFIED (fitur) |

## 3. Event sistem (domain D4/L1)

| Event | Pemicu | Efek |
|---|---|---|
| `deploy.completed` | Push → CF Pages/Workers build | Versi baru live |
| `healthcheck.probed` | Probe endpoint health | Liveness Worker (bukan kesehatan dependensi — keterbatasan A-030) |
| `ci.gate_run` | (target) push ke repo docs | Quality gate PASS/FAIL — CI belum diaktifkan |

## 4. Event knowledge & governance (domain D1/D2)

| Event | Pemicu | Efek | Status |
|---|---|---|---|
| `doc.approved` | Review manusia selesai | Status front-matter → approved; masuk MANIFEST | VERIFIED (proses manual) |
| `rfc.decided` | Keputusan founder | RFC → Accepted; implementasi boleh mulai | VERIFIED |
| `batch.released` | Batch selesai + gate PASS | Entry CHANGELOG + status BATCH-INDEX | VERIFIED |
| `doc.review_overdue` | `next_review` lewat | WARNING dari validator | VERIFIED (otomatis) |
| `lesson.captured` | (target) retrospektif batch | Masuk memory/learning engine | NOT VERIFIED — P09/P10 |

## 5. Aturan

1. **Penamaan**: `<domain>.<kejadian_lampau>` huruf kecil — konsisten dengan
   bahasa ubiquitous [EA-0004](EA-0004-domain-model.md).
2. Event baru yang melintasi batas domain didaftarkan di katalog ini dulu.
3. Webhook inbound wajib **idempotent** — event yang sama dikirim dua kali
   tidak boleh menggandakan efek (aturan EA-0007 §3).
4. Bila kelak event bus dibangun (P06/P08): katalog ini menjadi kontrak awal;
   pengenalan infrastruktur event = RFC baru, bukan keputusan diam-diam.

## Version history

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-07-11 | Katalog event bisnis/sistem/knowledge + kondisi jujur tanpa event bus — Batch 01 |
