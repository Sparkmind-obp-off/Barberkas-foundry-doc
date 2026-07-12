---
id: EA-0007
title: Integration
version: 1.0.0
status: approved
owner: Founder
reviewers: [Founder]
classification: internal
type: specification
last_updated: 2026-07-11
next_review: 2027-01-07
parent: EA-0001
related_docs: [EA-0002, EA-0008, E-042]
---
# EA-0007 — Integration

| Field | Value |
|---|---|
| **ID** | EA-0007 |
| **Version** | 1.0.0 |
| **Status** | Approved |
| **Owner** | Founder |
| **Created** | 2026-07-11 |
| **Updated** | 2026-07-11 |
| **Classification** | Internal |
| **Type** | Specification |
| **References** | [EA-0002 Context Diagram](EA-0002-context-diagram.md), [EA-0008 Event Model](EA-0008-event-model.md), [E-042 API Standards](../../canonical/04-engineering/042-api-standards.md) |

> Registry **titik integrasi** enterprise — internal maupun eksternal — beserta
> pola, arah, dan kontrolnya. Integrasi yang tidak terdaftar di sini dianggap
> tidak resmi (aturan boundary [EA-0002 §3](EA-0002-context-diagram.md)).

## 1. Integrasi eksternal (runtime produk)

| # | Integrasi | Arah | Pola | Kontrol keamanan | Bukti |
|---|---|---|---|---|---|
| I-1 | Clerk → App | inbound (JWT di tiap request) | Token verification | Fail-closed ([ADR-001](../../canonical/03-architecture/adr/ADR-001-fail-closed-auth.md)) | VERIFIED |
| I-2 | App → Duitku | outbound (create invoice) | REST request/response | Kredensial server-side | VERIFIED |
| I-3 | Duitku → App | inbound `/webhook/duitku` | Webhook + signature | Signature verification ([ADR-003](../../canonical/03-architecture/adr/ADR-003-duitku-mor-payment.md)) | VERIFIED |
| I-4 | Fonnte → App | inbound `/webhooks/fonnte` | Webhook | Device→tenant mapping anti-spoof ([ADR-004](../../canonical/03-architecture/adr/ADR-004-wa-device-tenant-mapping.md)) | VERIFIED |
| I-5 | App → Fonnte | outbound (send message) | REST API | Token server-side | VERIFIED |
| I-6 | App → LLM providers | outbound | REST API | Cost caps & policy ([AI-070](../../canonical/07-ai/070-ai-agents-policy.md)) | VERIFIED |
| I-7 | App → D1 | internal binding | CF Workers binding | Tenant isolation ([A-031](../../canonical/03-architecture/031-data-architecture.md)) | VERIFIED |

## 2. Integrasi knowledge & governance

| # | Integrasi | Arah | Pola | Bukti |
|---|---|---|---|---|
| K-1 | Repo docs ↔ GitHub | dua arah | git push/pull | VERIFIED |
| K-2 | Quality gate → repo | lokal/CI | `validate_docs.py` pre-merge | VERIFIED (lokal); CI belum diaktifkan |
| K-3 | AI agents ↔ repo docs | dua arah | Sandbox agentik, output direview manusia | VERIFIED (praktik, [AI-071](../../canonical/07-ai/071-session-os.md)) |
| K-4 | `programs/` ↔ `canonical/` | referensi silang | Link + precedence BF-0010 | VERIFIED |

## 3. Pola integrasi yang diakui

| Pola | Kapan dipakai | Aturan |
|---|---|---|
| **Webhook inbound** | Vendor mendorong event (payment, WA) | Wajib verifikasi asal (signature/mapping); idempotent |
| **REST outbound** | App memanggil vendor | Kredensial di secret store, tidak pernah di kode/frontend |
| **Runtime binding** | Layanan CF (D1, KV) | Lewat binding Workers, bukan koneksi jaringan manual |
| **Git-based** | Pengetahuan & keputusan | Semua perubahan lewat commit — auditable by default |

Anti-pola: integrasi point-to-point tak terdaftar; duplikasi logic per kanal
(transport baru wajib menyambung ke FSM/logic yang ada — prinsip A-030 §4).

## 4. Aturan

1. **Integrasi baru = update dokumen ini + review** pada commit yang sama
   (analog aturan MANIFEST).
2. Setiap integrasi eksternal wajib punya **kontrol keamanan eksplisit**;
   tanpa itu statusnya maksimal Draft.
3. Kontrak API formal (OpenAPI) belum ada — **gap yang diakui**, target
   [E-042](../../canonical/04-engineering/042-api-standards.md); sampai ada,
   perilaku endpoint didokumentasikan minimal di runbook.
4. Kegagalan integrasi vendor masuk register risiko
   ([S-051](../../canonical/05-security/051-risk-register.md)).

## Version history

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-07-11 | Registry integrasi I-1..I-7 + K-1..K-4 + pola — Batch 01 |
