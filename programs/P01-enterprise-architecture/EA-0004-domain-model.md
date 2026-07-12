---
id: EA-0004
title: Domain Model
version: 1.0.0
status: approved
owner: Founder
reviewers: [Founder]
classification: internal
type: specification
last_updated: 2026-07-11
next_review: 2027-01-07
parent: EA-0001
related_docs: [A-031, BF-0008, Q-994]
---
# EA-0004 — Domain Model

| Field | Value |
|---|---|
| **ID** | EA-0004 |
| **Version** | 1.0.0 |
| **Status** | Approved |
| **Owner** | Founder |
| **Created** | 2026-07-11 |
| **Updated** | 2026-07-11 |
| **Classification** | Internal |
| **Type** | Specification |
| **References** | [A-031 Data Architecture](../../canonical/03-architecture/031-data-architecture.md), [BF-0008 Terminology](../P00-foundation/BF-0008-terminology.md), [Q-994 Knowledge Graph](../../canonical/99-schema/994-knowledge-graph.md) |

> Domain enterprise + entity inti per domain — **bahasa ubiquitous** yang dipakai
> semua program. Detail skema data produk tetap di
> [A-031](../../canonical/03-architecture/031-data-architecture.md);
> dokumen ini memetakan level konsep di atasnya.

## 1. Peta domain

```
┌─────────────────────────── BARBERKAS FOUNDRY ───────────────────────────┐
│                                                                          │
│  D1 KNOWLEDGE        D2 GOVERNANCE       D3 PRODUCT (BarberKas)          │
│  dokumen, registry,  keputusan, RFC/ADR, tenant, booking, payment,       │
│  graph, lifecycle    review, risiko      WA session, AI assistant        │
│                                                                          │
│  D4 EXECUTION        D5 INTELLIGENCE     D6 ECOSYSTEM                    │
│  program, batch,     memory, lesson,     repo, produk, vendor,           │
│  epic, task, release pattern, insight    integrasi                       │
└──────────────────────────────────────────────────────────────────────────┘
```

## 2. Entity inti per domain

### D1 — Knowledge

| Entity | Definisi | ID scheme | Status |
|---|---|---|---|
| Document | Unit pengetahuan ber-front-matter | Q-995 | VERIFIED |
| Registry | Daftar resmi (MANIFEST, PROG-INDEX, indeks layer) | `SSOT-*`, `*-INDEX` | VERIFIED |
| Relation | Edge parent/related/depends antar dokumen | Q-994 | VERIFIED (skema) |
| Lifecycle State | draft→review→approved→deprecated→archived | Q-993 | VERIFIED |

### D2 — Governance

| Entity | Definisi | Status |
|---|---|---|
| RFC | Usulan sebelum keputusan | VERIFIED |
| ADR | Keputusan arsitektur permanen | VERIFIED |
| Review | Persetujuan manusia atas dokumen/perubahan | VERIFIED |
| Risk | Item register risiko + mitigasi ([S-051](../../canonical/05-security/051-risk-register.md)) | VERIFIED |
| Gate | Syarat lulus (quality/production/enterprise gate) | VERIFIED |

### D3 — Product (BarberKas)

| Entity | Definisi | Status |
|---|---|---|
| Tenant | Barbershop pelanggan; unit isolasi data | VERIFIED (A-031) |
| User | Owner/staff terautentikasi (Clerk) | VERIFIED |
| Booking | Reservasi layanan | VERIFIED |
| Payment | Transaksi via Duitku MoR | VERIFIED |
| WA Session | Percakapan customer via Fonnte | VERIFIED |
| AI Assistant | Stylist/Marketing/Receptionist agent | VERIFIED |

### D4 — Execution

| Entity | Definisi | Status |
|---|---|---|
| Program | Kapabilitas permanen P00–P20 | VERIFIED (RFC-002) |
| Batch | Gelombang implementasi ber-release | VERIFIED |
| Epic / Task | Unit kerja `P<nn>-E<nn>` / `P<nn>-E<nn>-T<nnn>` | VERIFIED (skema) |
| Release | Snapshot canonical satu batch di CHANGELOG | VERIFIED |

### D5 — Intelligence (target — belum ada engine)

| Entity | Definisi | Status |
|---|---|---|
| Memory | Rekaman keputusan/pengalaman terstruktur | NOT VERIFIED — P09 |
| Lesson | Pembelajaran tervalidasi dari retrospektif | NOT VERIFIED — P10 |
| Pattern | Pola berulang yang dipromosikan jadi standar | NOT VERIFIED — P10 |
| Insight | Temuan/rekomendasi berbasis data | NOT VERIFIED — P12 |

### D6 — Ecosystem

| Entity | Definisi | Status |
|---|---|---|
| Repository | Repo kode/dokumen dalam ekosistem | VERIFIED (2 repo) |
| Vendor | Pihak eksternal terintegrasi | VERIFIED (EA-0002 §2.2) |
| Integration | Titik sambung terdaftar ([EA-0007](EA-0007-integration.md)) | VERIFIED |

## 3. Relasi lintas domain (inti)

```
Program (D4) ──produces──► Document (D1) ──governed-by──► Gate/Review (D2)
Document (D1) ──describes──► Tenant/Booking/… (D3)
Task (D4) ──decided-by──► ADR (D2)
Memory/Lesson (D5) ──derived-from──► Release + Review (D4, D2)   [target]
Vendor (D6) ──constrained-by──► Risk (D2)
```

## 4. Aturan

1. **Satu istilah satu makna**: konflik penamaan diselesaikan lewat
   [BF-0008](../P00-foundation/BF-0008-terminology.md) (struktural) /
   [F-001](../../canonical/00-foundation/001-glossary.md) (produk).
2. Entity baru lintas program didaftarkan di sini dulu sebelum dipakai skema lain.
3. Entity D5 berlabel NOT VERIFIED sampai engine-nya nyata — dokumen ini tidak
   boleh dijadikan bukti kapabilitas intelligence.

## Version history

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-07-11 | Domain model enterprise 6 domain — Batch 01 |
