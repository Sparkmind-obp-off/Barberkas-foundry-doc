---
id: EA-0006
title: Component Architecture
version: 1.0.0
status: approved
owner: Founder
reviewers: [Founder]
classification: internal
type: specification
last_updated: 2026-07-11
next_review: 2027-01-07
parent: EA-0001
related_docs: [EA-0005, EA-0007, A-030]
---
# EA-0006 — Component Architecture

| Field | Value |
|---|---|
| **ID** | EA-0006 |
| **Version** | 1.0.0 |
| **Status** | Approved |
| **Owner** | Founder |
| **Created** | 2026-07-11 |
| **Updated** | 2026-07-11 |
| **Classification** | Internal |
| **Type** | Specification |
| **References** | [EA-0005 Layer Architecture](EA-0005-layer-architecture.md), [EA-0007 Integration](EA-0007-integration.md), [A-030 System Overview](../../canonical/03-architecture/030-system-overview.md) |

> Inventaris **komponen nyata** enterprise per lapisan (C4 Level-2/3 gaya ringkas),
> masing-masing dengan status verifikasi. Komponen yang belum ada **tidak
> dicantumkan sebagai ada** — hanya sebagai target berlabel.

## 1. Komponen per lapisan

### L5–L6 — Knowledge & Governance (repo ini)

| Komponen | Fungsi | Status |
|---|---|---|
| `canonical/` (12 layer folder) | SSOT produk BarberKas | VERIFIED |
| `programs/` (P00, P01) | Layer organisasi Foundry | VERIFIED |
| MANIFEST + indeks layer | Registry anti-orphan | VERIFIED |
| `tools/validate_docs.py` | Quality gate 8 pemeriksaan | VERIFIED |
| `tools/ci/docs-quality.yml` | CI gate (belum diaktifkan ke `.github/workflows/`) | VERIFIED (file), NOT VERIFIED (aktif) |
| RFC/ADR register | Jejak keputusan | VERIFIED |

### L3 — Application (BarberKas, repo kode terpisah)

| Komponen | Fungsi | Status |
|---|---|---|
| Hono app @ CF Workers | Backend + SSR views (~5.200 LOC) | VERIFIED (A-030) |
| D1 multi-tenant schema | Data persist, `tenant_id` di semua tabel | VERIFIED ([A-031](../../canonical/03-architecture/031-data-architecture.md)) |
| Booking FSM | Alur reservasi (dipakai ulang lintas kanal) | VERIFIED |
| Payment module (Duitku) | Invoice + callback signature verification | VERIFIED ([ADR-003](../../canonical/03-architecture/adr/ADR-003-duitku-mor-payment.md)) |
| WA webhook handler (Fonnte) | Inbound WA → FSM; anti-spoof mapping | VERIFIED ([ADR-004](../../canonical/03-architecture/adr/ADR-004-wa-device-tenant-mapping.md)) |
| AI assistants (Stylist/Marketing/Receptionist) | LLM-backed, terikat [AI-070](../../canonical/07-ai/070-ai-agents-policy.md) | VERIFIED (fitur), INFERRED (kualitas) |
| Health endpoint | Liveness Worker saja | VERIFIED — keterbatasan diakui A-030 |

### L2–L1 — Integration & Infrastructure

| Komponen | Fungsi | Status |
|---|---|---|
| Clerk (JWT) | Identity; fail-closed ([ADR-001](../../canonical/03-architecture/adr/ADR-001-fail-closed-auth.md)) | VERIFIED |
| Cloudflare Workers/Pages/D1 | Runtime edge-native ([ADR-002](../../canonical/03-architecture/adr/ADR-002-edge-native-stack.md)) | VERIFIED |
| GitHub | Hosting SSOT + CI | VERIFIED |
| Sandbox agentik | Lingkungan kerja AI agent | VERIFIED (praktik), diatur [AI-071](../../canonical/07-ai/071-session-os.md) |

### L4 — Intelligence (target, BELUM ADA)

| Komponen target | Program | Status |
|---|---|---|
| Knowledge graph engine | P04 | NOT VERIFIED — baru skema Q-994 |
| Memory engine | P09 | NOT VERIFIED |
| Learning pipeline | P10 | NOT VERIFIED |
| AI council & orchestrator | P07, P08 | NOT VERIFIED |

## 2. Aturan komponen

1. **Komponen baru** didaftarkan di sini (level enterprise) atau A-030 (level
   produk) pada batch yang sama dengan pembuatannya.
2. Setiap komponen punya **satu owner role** ([G-096](../../canonical/09-governance/096-responsibility-stakeholder-matrix.md)) — tidak ada komponen tak bertuan.
3. Komponen L4 hanya boleh dipromosikan dari NOT VERIFIED setelah ada bukti
   berjalan + review manusia (BF-0010).
4. Menghapus komponen = deprecation Q-993, bukan sekadar menghapus baris.

## Version history

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-07-11 | Inventaris komponen enterprise + status verifikasi — Batch 01 |
