---
id: EA-0010
title: Dependency Map
version: 1.0.0
status: approved
owner: Founder
reviewers: [Founder]
classification: internal
type: register
last_updated: 2026-07-11
next_review: 2027-01-07
parent: EA-0001
related_docs: [EA-0005, EA-0007, S-051]
---
# EA-0010 — Dependency Map

| Field | Value |
|---|---|
| **ID** | EA-0010 |
| **Version** | 1.0.0 |
| **Status** | Approved |
| **Owner** | Founder |
| **Created** | 2026-07-11 |
| **Updated** | 2026-07-11 |
| **Classification** | Internal |
| **Type** | Register |
| **References** | [EA-0005 Layer Architecture](EA-0005-layer-architecture.md), [EA-0007 Integration](EA-0007-integration.md), [S-051 Risk Register](../../canonical/05-security/051-risk-register.md) |

> Register **apa bergantung pada apa** di tiga tingkat: antar-program,
> antar-sistem, dan terhadap vendor. Ketergantungan yang tak terpetakan adalah
> risiko tersembunyi; register ini membuatnya terlihat dan bisa dikelola.

## 1. Ketergantungan antar-program (P00–P20)

```
P00 Foundation ──► semua program (identitas, aturan, terminologi)
P01 EA ──► P02–P20 (blueprint yang diacu semua)
P02 Governance ──► P05 HITL, P16 Meta Governance
P03 Canonical Registry ──► P04 Knowledge Graph ──► P06 KNS ──► P09/P10 ──► P12–P14
P07 AI Council + P08 Orchestration ──► butuh P04–P06 dulu
P11–P14 (Autonomy) ──► butuh seluruh fase Intelligence
P15–P20 (Legacy) ──► butuh fondasi + intelligence matang
```

| Program | Bergantung pada | Alasan |
|---|---|---|
| P01 | P00 | Bahasa & aturan canonical dari BF-0008/BF-0010 |
| P02–P05 | P00, P01 | Governance & registry mengacu blueprint EA |
| P06–P10 | P03, P04 | Engine butuh registry & graph yang sehat |
| P11–P14 | P06–P10 | Autonomy tanpa memory/learning = klaim kosong |
| P15–P20 | hampir semua | Legacy dibangun di atas semuanya |

**Aturan urutan batch mengikuti peta ini** — [BATCH-INDEX](../BATCH-INDEX.md)
tidak boleh menjadwalkan program sebelum dependensinya selesai.

## 2. Ketergantungan sistem (runtime)

| Sistem | Bergantung pada | Jenis | Bila putus |
|---|---|---|---|
| App BarberKas | Cloudflare Workers/D1 | Hard | Produk mati total |
| App | Clerk | Hard (auth) | Login gagal — fail-closed, tidak ada bypass |
| App | Duitku | Soft (payment saja) | Booking jalan, pembayaran tertunda |
| App | Fonnte | Soft (kanal WA) | Kanal dashboard tetap hidup |
| App | LLM providers | Soft (AI assistants) | Fitur AI degradasi, core tetap jalan |
| Repo docs | GitHub | Medium | Kerja lokal tetap bisa; kolaborasi & CI berhenti |
| Quality gate | Python 3 stdlib | Hard (untuk gate) | Gate tak jalan — merge harus ditunda |

## 3. Ketergantungan vendor (konsentrasi risiko)

| Vendor | Layanan | Konsentrasi | Mitigasi tercatat |
|---|---|---|---|
| Cloudflare | Runtime + DB + hosting | **Tinggi** — single point | Diterima sadar via [ADR-002](../../canonical/03-architecture/adr/ADR-002-edge-native-stack.md); exit cost diakui |
| Clerk | Identity | Sedang | Fail-closed (ADR-001); migrasi = ganti verifier JWT |
| Duitku | Payment MoR | Sedang | Pola MoR internal (ADR-003) memudahkan ganti PSP |
| Fonnte | WA gateway | Sedang | Logic FSM terpisah dari transport (A-030 §4) |
| LLM providers | AI | Rendah | Multi-provider by design (AI-070) |

Risiko konsentrasi vendor terhubung ke register risiko
[S-051](../../canonical/05-security/051-risk-register.md); review kuartalan.

## 4. Aturan

1. **Dependensi baru wajib didaftarkan di sini** pada batch yang sama —
   antar-program, sistem, maupun vendor.
2. Setiap dependensi hard wajib punya catatan "bila putus" — tanpa itu review ditolak.
3. Arah dependensi mengikuti aturan lapisan [EA-0005 §3](EA-0005-layer-architecture.md);
   siklus (A→B→A) dilarang — bila terdeteksi, pecahkan via RFC.
4. Q-994 knowledge graph adalah pasangan data dari peta ini; bila kelak engine
   P04 hidup, register ini menjadi sumber edge `depends_on`.

## Version history

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-07-11 | Dependency map program/sistem/vendor + aturan — Batch 01 |
