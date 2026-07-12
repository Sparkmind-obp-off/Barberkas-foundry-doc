---
id: EA-0002
title: Context Diagram
version: 1.0.0
status: approved
owner: Founder
reviewers: [Founder]
classification: internal
type: specification
last_updated: 2026-07-11
next_review: 2027-01-07
parent: EA-0001
related_docs: [EA-0007, A-030]
---
# EA-0002 — Context Diagram

| Field | Value |
|---|---|
| **ID** | EA-0002 |
| **Version** | 1.0.0 |
| **Status** | Approved |
| **Owner** | Founder |
| **Created** | 2026-07-11 |
| **Updated** | 2026-07-11 |
| **Classification** | Internal |
| **Type** | Specification |
| **References** | [EA-0001](EA-0001-enterprise-architecture.md), [EA-0007 Integration](EA-0007-integration.md), [A-030 System Overview](../../canonical/03-architecture/030-system-overview.md) |

> Batas enterprise (C4 Level-1 diperluas ke level Foundry): apa yang **di dalam**
> kendali kami, siapa aktor **di luar**, dan melalui saluran apa mereka berinteraksi.

## 1. Diagram konteks enterprise

```
                        ┌────────────────────────────────────────────────┐
   AKTOR MANUSIA        │            BARBERKAS FOUNDRY (enterprise)      │   PIHAK EKSTERNAL
                        │                                                │
 Founder/Curator ──────►│  ┌──────────────┐      ┌─────────────────┐    │
 (governance, HITL)     │  │ Knowledge     │      │ Produk:          │    │◄──── Clerk (identity)
                        │  │ Layer         │◄────►│ BarberKas        │    │◄──── Duitku (payment MoR)
 Owner barbershop ─────►│  │ (SSOT docs,   │      │ (Hono @ CF       │    │◄──── Fonnte (WA gateway)
 (pengguna produk)      │  │ programs/,    │      │ Workers + D1)    │    │◄──── LLM providers (Groq dkk.)
                        │  │ canonical/)   │      └─────────────────┘    │◄──── Cloudflare (runtime)
 Staff barbershop ─────►│  └──────────────┘      ┌─────────────────┐    │◄──── GitHub (repo, CI)
                        │  ┌──────────────┐      │ Tooling:         │    │
 Customer (via WA) ────►│  │ AI Agents     │◄────►│ quality gate,    │    │
                        │  │ (pelaksana,   │      │ CI, sandbox      │    │
                        │  │ terikat AI-070)│     └─────────────────┘    │
                        │  └──────────────┘                              │
                        └────────────────────────────────────────────────┘
```

## 2. Aktor & relasi

### 2.1 Aktor manusia

| Aktor | Peran terhadap enterprise | Saluran |
|---|---|---|
| Founder / Curator | Pemegang keputusan akhir (HITL); owner semua role saat ini | GitHub, sandbox agentik, dashboard |
| Owner barbershop | Pembeli & admin tenant produk | Browser (Clerk auth) |
| Staff barbershop | Operator harian tenant | Browser |
| Customer akhir | Booking & interaksi via WA | WhatsApp (via Fonnte) |

### 2.2 Sistem eksternal (di luar kendali)

| Sistem | Fungsi | Risiko ketergantungan → mitigasi |
|---|---|---|
| Cloudflare | Runtime (Workers/Pages/D1) | Vendor lock-in edge → [EA-0011 §3](EA-0011-technology-principles.md) |
| Clerk | Identity & JWT | Fail-closed auth ([ADR-001](../../canonical/03-architecture/adr/ADR-001-fail-closed-auth.md)) |
| Duitku | Payment MoR | Callback signature verification ([ADR-003](../../canonical/03-architecture/adr/ADR-003-duitku-mor-payment.md)) |
| Fonnte | WhatsApp gateway | Device→tenant mapping anti-spoof ([ADR-004](../../canonical/03-architecture/adr/ADR-004-wa-device-tenant-mapping.md)) |
| LLM providers | AI assistants | Cost caps & safety ([AI-070](../../canonical/07-ai/070-ai-agents-policy.md)) |
| GitHub | SSOT hosting, CI quality gate | Registry & gate lokal tetap jalan tanpa CI |

### 2.3 Di dalam batas enterprise

| Elemen | Deskripsi | SSOT |
|---|---|---|
| Knowledge Layer | `canonical/` + `programs/` + registry + gate | repo ini |
| Produk BarberKas | Aplikasi multi-tenant edge-native | [A-030](../../canonical/03-architecture/030-system-overview.md) |
| AI Agents | Pelaksana terikat policy; output direview manusia | [AI-070](../../canonical/07-ai/070-ai-agents-policy.md) |
| Tooling | validate_docs.py, CI workflow, sandbox | [MANIFEST §1](../../MANIFEST.md) |

## 3. Aturan batas (boundary rules)

1. **Semua trust boundary crossing wajib terautentikasi** — tidak ada endpoint
   anonim yang mengubah state (fail-closed, ADR-001).
2. **Identitas eksternal tidak pernah dipercaya mentah** — pemetaan (device WA,
   callback payment) diverifikasi server-side (ADR-003, ADR-004).
3. **Vendor eksternal masuk hanya lewat titik integrasi terdaftar** di
   [EA-0007](EA-0007-integration.md); integrasi baru = update EA-0007 + review.
4. Konteks ini direview setiap ada aktor/vendor baru — diagram usang = error governance.

## Version history

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-07-11 | Context diagram enterprise — Batch 01 |
