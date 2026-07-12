---
id: EA-0011
title: Technology Principles
version: 1.0.0
status: approved
owner: Founder
reviewers: [Founder]
classification: internal
type: standard
last_updated: 2026-07-11
next_review: 2027-01-07
parent: EA-0001
related_docs: [EA-0012, EA-0010, A-030, ADR-002]
---
# EA-0011 — Technology Principles

| Field | Value |
|---|---|
| **ID** | EA-0011 |
| **Version** | 1.0.0 |
| **Status** | Approved |
| **Owner** | Founder |
| **Created** | 2026-07-11 |
| **Updated** | 2026-07-11 |
| **Classification** | Internal |
| **Type** | Standard |
| **References** | [EA-0001](EA-0001-enterprise-architecture.md), [EA-0012 Architecture Principles](EA-0012-architecture-principles.md), [A-030 System Overview](../../canonical/03-architecture/030-system-overview.md), [ADR-002 Edge-native Stack](../../canonical/03-architecture/adr/ADR-002-edge-native-stack.md) |

> Aturan **memilih, mengadopsi, dan memensiunkan teknologi** di seluruh
> enterprise Foundry. [EA-0012](EA-0012-architecture-principles.md) mengatur
> *cara mendesain*; dokumen ini mengatur *dengan apa membangun*. Setiap
> pengecualian wajib lewat RFC → ADR — tidak ada adopsi diam-diam.

## 1. Prinsip teknologi (TP-1 … TP-7)

| # | Prinsip | Arti operasional | Bukti kepatuhan hari ini |
|---|---|---|---|
| **TP-1** | **Edge-native, zero VPS** | Runtime produk berjalan di edge (Cloudflare Workers/Pages/D1); tidak ada server yang harus dirawat | [ADR-002](../../canonical/03-architecture/adr/ADR-002-edge-native-stack.md), [A-030](../../canonical/03-architecture/030-system-overview.md) — VERIFIED |
| **TP-2** | **Boring by default** | Pilih teknologi matang & terdokumentasi; teknologi eksperimental hanya di jalur riset (P19), bukan produksi | Stack: Hono, D1/SQLite, Python stdlib — VERIFIED |
| **TP-3** | **Stdlib dulu, dependensi belakangan** | Setiap dependensi baru = liability; tambah hanya bila stdlib/platform tidak cukup | `tools/validate_docs.py` 100% stdlib — VERIFIED |
| **TP-4** | **Buy/rent yang bukan inti, build yang inti** | Auth (Clerk), payment (Duitku), WA (Fonnte) disewa; domain logic & knowledge system dibangun sendiri | [EA-0010 §3](EA-0010-dependency-map.md) — VERIFIED |
| **TP-5** | **Exit path sadar untuk tiap vendor** | Boleh lock-in bila sadar, tercatat, dan ada rencana keluar kasar; dilarang lock-in tanpa keputusan | §3 dokumen ini + [S-051](../../canonical/05-security/051-risk-register.md) |
| **TP-6** | **Docs-as-code & machine-validated** | Pengetahuan diperlakukan seperti kode: versioned, di-lint, gated di CI | RFC-001, quality gate — VERIFIED |
| **TP-7** | **AI sebagai tenaga kerja, manusia sebagai otoritas** | AI boleh mengerjakan; keputusan & approval tetap manusia (HITL, P05) | [AI-070](../../canonical/07-ai/070-ai-agents-policy.md) — VERIFIED |

## 2. Prosedur adopsi teknologi baru

```
Kebutuhan → cek stack ada dulu (TP-3) → RFC (kandidat + kriteria §2.1)
        → keputusan = ADR → masuk registry EA-0006/EA-0010 → baru boleh dipakai
```

### 2.1 Kriteria evaluasi wajib (dinilai di RFC)

| Kriteria | Pertanyaan |
|---|---|
| Kecocokan edge | Jalan di Workers runtime tanpa Node API? (batas platform [A-030](../../canonical/03-architecture/030-system-overview.md)) |
| Kematangan | Umur, komunitas, jadwal rilis, catatan breaking change |
| Biaya total | Harga + waktu belajar + beban rawat, bukan harga lisensi saja |
| Exit cost | Bila vendor mati/berubah harga: berapa mahal keluar? (TP-5) |
| Keamanan & privasi | Sentuh PII? Selaras [S-050](../../canonical/05-security/050-security-baseline.md)/[S-052](../../canonical/05-security/052-privacy-and-data-protection.md)? |
| Jejak dependensi | Berapa transitive deps yang ikut masuk? (TP-3) |

### 2.2 Prosedur pensiun (deprecation)

1. Usulan pensiun lewat RFC (alasan + rencana migrasi).
2. Status komponen di [EA-0006](EA-0006-component-architecture.md) → `Deprecated`; dilarang pemakaian baru.
3. Migrasi selesai → hapus dari registry aktif; keputusan tetap tercatat di ADR (ID tidak di-reuse, [Q-995](../../canonical/99-schema/995-numbering.md)).

## 3. Posisi vendor & lock-in (jujur)

Konsentrasi tertinggi ada di **Cloudflare** (runtime + DB + hosting) — lock-in ini
**diterima sadar** via [ADR-002](../../canonical/03-architecture/adr/ADR-002-edge-native-stack.md):
harga yang dibayar untuk zero-ops. Konsekuensi & mitigasi:

| Vendor | Lock-in | Sikap | Exit path kasar |
|---|---|---|---|
| Cloudflare | **Tinggi** — Workers API + D1 | Diterima sadar (ADR-002) | D1 = SQLite → dump portabel; Hono jalan juga di Node/Deno/Bun |
| Clerk | Sedang — format JWT & user store | Diterima (ADR-001 fail-closed) | Ganti verifier JWT + ekspor user; kontrak auth di satu modul |
| Duitku | Sedang — API MoR | Diterima (ADR-003) | Pola MoR internal memudahkan ganti PSP |
| Fonnte | Sedang — WA gateway | Diterima | FSM terpisah dari transport ([A-030 §4](../../canonical/03-architecture/030-system-overview.md)) |
| LLM providers | Rendah | Multi-provider by design | Ganti provider = konfigurasi ([AI-070](../../canonical/07-ai/070-ai-agents-policy.md)) |

Risiko konsentrasi di-review kuartalan bersama [S-051 Risk Register](../../canonical/05-security/051-risk-register.md)
dan [EA-0010 Dependency Map](EA-0010-dependency-map.md).

## 4. Anti-pattern yang dilarang

| Anti-pattern | Kenapa dilarang |
|---|---|
| Adopsi framework/lib tanpa RFC/ADR | Melanggar jalur keputusan (F-002); menciptakan shadow stack |
| "Sekalian rewrite" saat menambah fitur | Risiko regresi masif; perubahan besar wajib RFC |
| Dependensi untuk hal yang bisa 20 baris stdlib | Melanggar TP-3; menambah permukaan serangan |
| Menyimpan state di memori/file Worker | Platform tidak menjaminnya; wajib D1/KV/R2 (A-030) |
| Teknologi eksperimental langsung ke produksi | Jalurnya P19 Research → RFC → ADR (TP-2) |

## 5. Hubungan dengan dokumen lain

- **[EA-0012](EA-0012-architecture-principles.md)** — prinsip *desain*; dokumen ini prinsip *pemilihan alat*.
- **[EA-0006](EA-0006-component-architecture.md)** / **[EA-0010](EA-0010-dependency-map.md)** — registry tempat hasil adopsi dicatat.
- **[ADR register](../../canonical/03-architecture/adr/ADR-INDEX.md)** — tempat keputusan teknologi final direkam.
- **[E-040](../../canonical/04-engineering/040-engineering-standards.md)** — standar pemakaian sehari-hari atas stack yang sudah diadopsi.

## Version history

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-07-11 | Prinsip teknologi TP-1..TP-7 + prosedur adopsi/pensiun + posisi lock-in — Batch 01 |
