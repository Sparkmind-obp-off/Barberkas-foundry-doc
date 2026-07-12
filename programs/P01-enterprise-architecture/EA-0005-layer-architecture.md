---
id: EA-0005
title: Layer Architecture
version: 1.0.0
status: approved
owner: Founder
reviewers: [Founder]
classification: internal
type: specification
last_updated: 2026-07-11
next_review: 2027-01-07
parent: EA-0001
related_docs: [EA-0006, EA-0010, A-030]
---
# EA-0005 — Layer Architecture

| Field | Value |
|---|---|
| **ID** | EA-0005 |
| **Version** | 1.0.0 |
| **Status** | Approved |
| **Owner** | Founder |
| **Created** | 2026-07-11 |
| **Updated** | 2026-07-11 |
| **Classification** | Internal |
| **Type** | Specification |
| **References** | [EA-0001](EA-0001-enterprise-architecture.md), [EA-0006 Component Architecture](EA-0006-component-architecture.md), [A-030 System Overview](../../canonical/03-architecture/030-system-overview.md) |

> Tujuh lapisan enterprise Barberkas Foundry — dari visi Empire sampai
> infrastruktur — beserta aturan siapa boleh bergantung pada siapa.
> Lapisan adalah **struktur logis**, bukan struktur deploy: beberapa lapisan
> hari ini masih tipis atau berupa target.

## 1. Peta lapisan

```
L7  EMPIRE / VISION       visi jangka panjang, warisan (P20)
L6  GOVERNANCE            keputusan, RFC/ADR, gate, HITL (P02, P05, P16)
L5  KNOWLEDGE             SSOT docs, registry, graph, lifecycle (P00, P03, P04)
L4  INTELLIGENCE          memory, learning, council, orchestration (P06–P14) [target]
L3  APPLICATION           produk BarberKas: Hono app, AI assistants (A-030)
L2  INTEGRATION           webhook, API, auth, payment callback (EA-0007)
L1  INFRASTRUCTURE        Cloudflare Workers/Pages/D1, GitHub, CI
```

## 2. Deskripsi per lapisan

| Lapisan | Isi | Status bukti | SSOT |
|---|---|---|---|
| L7 Empire | Visi, misi, north star, konstitusi | VERIFIED — [BF-0001](../P00-foundation/BF-0001-vision.md)–[BF-0004](../P00-foundation/BF-0004-constitution.md) | `programs/P00-foundation/` |
| L6 Governance | RFC, ADR, review, quality/production/enterprise gate | VERIFIED — F-002, G-09x, RFC layer | `canonical/09-governance/`, `10-rfc/` |
| L5 Knowledge | Dokumen canonical, MANIFEST, numbering, lifecycle, graph schema | VERIFIED — RFC-001 (v3), gate PASS | `canonical/99-schema/`, MANIFEST |
| L4 Intelligence | Memory engine, learning, AI council, orchestration, brain | NOT VERIFIED — target P06–P14; baru skema [Q-994](../../canonical/99-schema/994-knowledge-graph.md) | belum ada |
| L3 Application | BarberKas: booking, payment, WA, AI assistants | VERIFIED — [A-030](../../canonical/03-architecture/030-system-overview.md) | `canonical/03-architecture/` |
| L2 Integration | Titik sambung internal & vendor (Clerk, Duitku, Fonnte, LLM) | VERIFIED — [EA-0007](EA-0007-integration.md) | EA-0007 |
| L1 Infrastructure | CF Workers/Pages/D1, GitHub repo & CI, sandbox agentik | VERIFIED — ADR-002 | [ADR-002](../../canonical/03-architecture/adr/ADR-002-edge-native-stack.md) |

## 3. Aturan ketergantungan antar lapisan

```
arah ketergantungan yang diizinkan:  atas ──► bawah (L7 → L1)
```

1. **Lapisan hanya boleh bergantung ke bawah** — L5 boleh mengasumsikan L1
   (repo GitHub ada), tetapi L1 tidak boleh mengasumsikan isi L5.
2. **Loncat lapisan diperbolehkan, memutar balik tidak** — L6 boleh langsung
   memakai L1 (CI menjalankan gate); L3 tidak boleh mendikte isi L6.
3. **L4 (Intelligence) dibangun di atas L5/L6, bukan menggantikannya** —
   engine apa pun kelak membaca registry & graph yang sudah ada; keputusan
   akhir tetap di L6 (HITL, [AI-070](../../canonical/07-ai/070-ai-agents-policy.md)).
4. Ketergantungan lintas lapisan yang baru wajib tercatat di
   [EA-0010 Dependency Map](EA-0010-dependency-map.md).

## 4. Kondisi saat ini vs target

| Lapisan | Sekarang | Target berikutnya |
|---|---|---|
| L7–L5 | Terisi & machine-validated | Spiral evaluasi tiap putaran batch |
| L4 | Kosong (hanya skema) | Batch 04+ (P04 graph engine) → Batch 06–10 |
| L3–L1 | Berjalan (pilot) | Formalisasi kontrak API (E-042), backup/DR (O-062) |

Dokumen ini tidak mengklaim L4 ada — klaim kemampuan intelligence sebelum
engine-nya nyata melanggar [BF-0010 Canonical Rules](../P00-foundation/BF-0010-canonical-rules.md).

## Version history

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-07-11 | Layer architecture 7 lapisan + aturan dependensi — Batch 01 |
