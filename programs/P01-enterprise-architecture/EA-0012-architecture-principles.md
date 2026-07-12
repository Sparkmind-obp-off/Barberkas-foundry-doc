---
id: EA-0012
title: Architecture Principles
version: 1.0.0
status: approved
owner: Founder
reviewers: [Founder]
classification: internal
type: standard
last_updated: 2026-07-11
next_review: 2027-01-07
parent: EA-0001
related_docs: [EA-0011, EA-0005, BF-0006, F-004]
---
# EA-0012 — Architecture Principles

| Field | Value |
|---|---|
| **ID** | EA-0012 |
| **Version** | 1.0.0 |
| **Status** | Approved |
| **Owner** | Founder |
| **Created** | 2026-07-11 |
| **Updated** | 2026-07-11 |
| **Classification** | Internal |
| **Type** | Standard |
| **References** | [EA-0001](EA-0001-enterprise-architecture.md), [EA-0011 Technology Principles](EA-0011-technology-principles.md), [EA-0005 Layer Architecture](EA-0005-layer-architecture.md), [BF-0006 Principles](../P00-foundation/BF-0006-principles.md), [F-004 Decision Framework](../../canonical/00-foundation/004-decision-framework.md) |

> Prinsip **arsitektur enterprise yang mengikat** seluruh desain di Foundry —
> penutup Batch 01. Kalau [BF-0006](../P00-foundation/BF-0006-principles.md)
> adalah prinsip *organisasi* dan [EA-0011](EA-0011-technology-principles.md)
> prinsip *alat*, dokumen ini adalah prinsip *cara mendesain sistem*.
> Setiap desain yang melanggar prinsip di sini wajib membawa RFC.

## 1. Prinsip arsitektur (AP-1 … AP-10)

| # | Prinsip | Arti operasional |
|---|---|---|
| **AP-1** | **Truth-Lock: klaim = bukti** | Setiap klaim arsitektur berlabel VERIFIED / INFERRED / NOT VERIFIED; diagram tanpa bukti bukan arsitektur, melainkan aspirasi |
| **AP-2** | **SSOT tunggal per fakta** | Satu fakta hidup di satu dokumen; lainnya merujuk, tidak menyalin ([BF-0010](../P00-foundation/BF-0010-canonical-rules.md)) |
| **AP-3** | **Dependensi mengalir ke bawah** | Lapisan atas boleh bergantung ke bawah, tidak sebaliknya; siklus = cacat desain ([EA-0005 §2](EA-0005-layer-architecture.md)) |
| **AP-4** | **Fail-closed untuk keamanan** | Bila ragu (auth/tenant/entitlement gagal dievaluasi) → tolak; bypass darurat pun lewat prosedur ([ADR-001](../../canonical/03-architecture/adr/ADR-001-fail-closed-auth.md)) |
| **AP-5** | **Monolith dulu, pecah karena bukti** | Modular monolith sampai ada bukti beban/tim yang menuntut pemisahan; microservices tanpa bukti = kompleksitas gratis |
| **AP-6** | **Kontrak eksplisit antar bagian** | Integrasi lewat kontrak terdokumentasi (API [E-042](../../canonical/04-engineering/042-api-standards.md), event [EA-0008](EA-0008-event-model.md), schema [A-031](../../canonical/03-architecture/031-data-architecture.md)); dilarang bergantung pada internal pihak lain |
| **AP-7** | **Tenant isolation tidak bisa ditawar** | Setiap query & aliran data membawa batas tenant; kebocoran lintas tenant = insiden Sev-1 ([A-031](../../canonical/03-architecture/031-data-architecture.md), [S-050](../../canonical/05-security/050-security-baseline.md)) |
| **AP-8** | **Keputusan direkam, bukan diingat** | Keputusan desain signifikan = ADR; yang tidak terekam dianggap tidak pernah diputuskan ([F-004](../../canonical/00-foundation/004-decision-framework.md)) |
| **AP-9** | **Desain untuk digantikan, bukan diabadikan** | Komponen dibuat mudah diganti (kontrak jelas, state di storage, logic terpisah transport) — umur panjang milik enterprise, bukan milik komponen |
| **AP-10** | **Sederhana yang jujur > canggih yang semu** | Pilih desain paling sederhana yang memenuhi kebutuhan terverifikasi; kompleksitas harus dibayar bukti, bukan tren |

## 2. Cara memakai prinsip ini

```
Desain baru / perubahan
   │
   ├─ cek AP-1..AP-10  ──  lolos semua ──►  lanjut (catat ADR bila signifikan, AP-8)
   │
   └─ melanggar salah satu ──► RFC wajib:
        sebutkan prinsip yang dilanggar + alasan + batas waktu/exit
        → keputusan direkam sebagai ADR → pengecualian ter-audit
```

| Situasi | Prinsip yang paling sering menentukan |
|---|---|
| Menambah fitur produk | AP-5, AP-7, AP-10 |
| Integrasi vendor baru | AP-6, AP-9 + [EA-0011 §2](EA-0011-technology-principles.md) |
| Menambah program/dokumen baru | AP-2, AP-3, AP-8 |
| Insiden / perilaku tak terduga | AP-4, AP-7 |
| Godaan refactor besar | AP-1, AP-5, AP-10 |

## 3. Trade-off yang sudah diputuskan (jangan dibuka ulang tanpa RFC)

| Trade-off | Pilihan sadar | Direkam di |
|---|---|---|
| Kecepatan rilis vs kesempurnaan platform | Edge monolith ringan, zero-ops | [ADR-002](../../canonical/03-architecture/adr/ADR-002-edge-native-stack.md) |
| Kendali penuh vs beli layanan | Auth/payment/WA disewa (TP-4) | [ADR-001](../../canonical/03-architecture/adr/ADR-001-fail-closed-auth.md), [ADR-003](../../canonical/03-architecture/adr/ADR-003-duitku-mor-payment.md) |
| Fleksibilitas vs keamanan default | Fail-closed, deny-by-default | [ADR-001](../../canonical/03-architecture/adr/ADR-001-fail-closed-auth.md) |
| Struktur bebas vs struktur beku | 21 program dibekukan; isi yang berevolusi | [RFC-002](../../canonical/10-rfc/RFC-002-program-batch-operating-model.md) |

## 4. Hubungan dengan dokumen lain

- **[BF-0006 Principles](../P00-foundation/BF-0006-principles.md)** — prinsip organisasi (induk nilai).
- **[EA-0011 Technology Principles](EA-0011-technology-principles.md)** — pemilihan alat; AP + TP dibaca berpasangan.
- **[EA-0005 Layer Architecture](EA-0005-layer-architecture.md)** — AP-3 dieksekusi lewat aturan lapisan di sana.
- **[F-004 Decision Framework](../../canonical/00-foundation/004-decision-framework.md)** — kerangka evaluasi saat prinsip saling bertabrakan.
- **[G-091 Production Gate](../../canonical/09-governance/091-production-gate.md)** — pintu tempat kepatuhan prinsip diperiksa sebelum rilis.

## 5. Penutup Batch 01

Dengan EA-0012, ke-12 dokumen EA + charter P01 lengkap: struktur
(EA-0002…EA-0006), perilaku (EA-0007…EA-0010), dan aturan (EA-0011, EA-0012).
Program P01 memenuhi Definition of Done [P01-000](P01-000-program-charter.md)
dan siap ditandai **Canonical** di [PROG-INDEX](../PROGRAM-INDEX.md).

## Version history

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-07-11 | Prinsip arsitektur AP-1..AP-10 + trade-off terputus + penutup Batch 01 |
