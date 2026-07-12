---
id: EA-0009
title: Data Flow
version: 1.0.0
status: approved
owner: Founder
reviewers: [Founder]
classification: internal
type: specification
last_updated: 2026-07-11
next_review: 2027-01-07
parent: EA-0001
related_docs: [EA-0008, A-031, S-052]
---
# EA-0009 — Data Flow

| Field | Value |
|---|---|
| **ID** | EA-0009 |
| **Version** | 1.0.0 |
| **Status** | Approved |
| **Owner** | Founder |
| **Created** | 2026-07-11 |
| **Updated** | 2026-07-11 |
| **Classification** | Internal |
| **Type** | Specification |
| **References** | [EA-0008 Event Model](EA-0008-event-model.md), [A-031 Data Architecture](../../canonical/03-architecture/031-data-architecture.md), [S-052 Privacy & Data Protection](../../canonical/05-security/052-privacy-and-data-protection.md) |

> Aliran data end-to-end lintas enterprise + klasifikasi datanya.
> Skema tabel tetap di [A-031](../../canonical/03-architecture/031-data-architecture.md);
> dokumen ini memetakan **bagaimana data bergerak** melintasi batas.

## 1. Aliran utama (runtime produk)

### F-1 Booking via WhatsApp

```
Customer WA ─► Fonnte ─► /webhooks/fonnte ─► device→tenant mapping (ADR-004)
  ─► FSM booking ─► D1 (row booking, scoped tenant_id)
  ─► balasan via Fonnte send API ─► Customer WA
```

### F-2 Pembayaran

```
Owner/Customer ─► App checkout ─► Duitku create invoice (I-2)
Duitku ─► /webhook/duitku (I-3) ─► signature verification (ADR-003)
  ─► update payment status di D1 ─► notifikasi
```

### F-3 Dashboard owner/staff

```
Browser ─► Clerk JWT (ADR-001, fail-closed) ─► Hono app
  ─► query D1 (WHERE tenant_id = ...) ─► SSR view
```

### F-4 AI assistant

```
Pesan/tugas ─► App ─► prompt + konteks tenant ─► LLM provider (I-6)
  ─► jawaban ─► guard AI-070 ─► kanal (WA/dashboard)
```

## 2. Aliran knowledge & governance

### F-5 Perubahan pengetahuan

```
Draft (AI agent / manusia) ─► review manusia (HITL)
  ─► commit git ─► quality gate validate_docs.py ─► approved di MANIFEST
  ─► (target) knowledge graph engine P04
```

### F-6 Keputusan

```
Usulan ─► RFC (10-rfc/) ─► keputusan founder ─► ADR / perubahan canonical
  ─► tercatat di CHANGELOG per release batch
```

## 3. Klasifikasi data yang mengalir

| Kategori | Contoh | Klasifikasi | Aturan |
|---|---|---|---|
| Data pelanggan tenant | Nama, nomor WA, riwayat booking | Confidential | Isolasi `tenant_id`; privasi [S-052](../../canonical/05-security/052-privacy-and-data-protection.md) |
| Data pembayaran | Invoice, status, referensi Duitku | Confidential | Tidak menyimpan kredensial kartu (MoR di Duitku) |
| Kredensial & secrets | API key vendor, JWT secret | Confidential | Secret store CF; tidak pernah di repo/frontend |
| Dokumen canonical | Seluruh `canonical/` + `programs/` | Internal | Front-matter `classification` per dokumen |
| Telemetri | Log Worker, hasil gate | Internal | Tidak memuat PII bila bisa dihindari |

## 4. Aturan

1. **Semua data tenant mengalir dengan `tenant_id`** — query tanpa scoping
   tenant adalah bug keamanan, bukan sekadar bug ([A-031](../../canonical/03-architecture/031-data-architecture.md)).
2. Data melintasi trust boundary hanya lewat integrasi terdaftar
   ([EA-0007](EA-0007-integration.md)).
3. PII keluar enterprise (ke LLM provider dll.) diminimalkan — kirim konteks
   secukupnya, bukan dump data (AI-070, S-052).
4. Aliran baru = update dokumen ini + tinjauan privasi bila menyentuh PII.
5. Backup/restore D1 belum dibuktikan — gap diakui, target
   [O-062](../../canonical/06-operations/062-backup-and-dr.md); sampai itu
   selesai, aliran F-1..F-3 punya risiko kehilangan data yang tercatat di S-051.

## Version history

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-07-11 | Data flow F-1..F-6 + klasifikasi & aturan — Batch 01 |
