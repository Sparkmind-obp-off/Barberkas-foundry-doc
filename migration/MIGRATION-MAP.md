---
id: MIG-MAP
title: Legacy → Canonical SSOT v2
version: 2.0.0
status: approved
owner: Founder
reviewers: [Founder]
classification: internal
type: report
last_updated: 2026-07-10
next_review: 2026-10-08
parent: F-000
related_docs: []
---
# MIGRATION-MAP — Legacy → Canonical SSOT v2

| Field | Value |
|---|---|
| **ID** | MIG-MAP |
| **Version** | 2.0.0 |
| **Status** | Approved |
| **Owner** | Founder / Product |
| **Created** | 2026-07-10 |
| **Updated** | 2026-07-10 |
| **Classification** | Internal |

## Legenda disposisi

| Disposisi | Arti |
|---|---|
| **MERGED** | Konten diserap ke dokumen v2 (sumber jadi arsip read-only) |
| **SUPERSEDED** | Digantikan oleh dokumen v2; konflik → v2 menang |
| **ARCHIVED** | Nilai historis/operasional; tidak dipromosikan ke canonical |
| **DEFERRED** | Konten valid tapi eksekusinya ditunda (tercatat di dokumen v2 terkait) |

## 1. archive/canonical-v1/ (4 file)

| File legacy | Disposisi | Target v2 |
|---|---|---|
| 00-INDEX.md | SUPERSEDED | [canonical/00-INDEX.md](../canonical/00-INDEX.md) |
| 01-MASTER-AUDIT.md | MERGED | Tersebar: [P-020](../canonical/02-product/020-product-brief.md), [P-022](../canonical/02-product/022-feature-matrix.md), [B-010](../canonical/01-brand/010-brand-architecture.md), [S-050](../canonical/05-security/050-security-baseline.md), [AUDIT-REPORT-V2](AUDIT-REPORT-V2.md) |
| 02-RISK-AND-READINESS-REGISTER.md | MERGED | [S-051 Risk Register](../canonical/05-security/051-risk-register.md), [G-091](../canonical/09-governance/091-production-gate.md), [G-092](../canonical/09-governance/092-enterprise-gate.md), [C-082](../canonical/08-commercial/082-evidence-ledger.md) |
| 03-ROADMAP-AND-BACKLOG.md | MERGED | [G-090 Roadmap](../canonical/09-governance/090-roadmap.md), [G-093 DoR/DoD](../canonical/09-governance/093-definition-of-ready-done.md) |

## 2. archive/ssot/ — Batch 4 (8 file)

| File legacy | Disposisi | Target v2 |
|---|---|---|
| B4-00-INDEX.md | SUPERSEDED | [canonical/00-INDEX.md](../canonical/00-INDEX.md) |
| B4-01-REPOSITIONING-DOC.md | MERGED | [B-011 Positioning](../canonical/01-brand/011-positioning-and-messaging.md) |
| B4-02-TARGET-MARKET-DOC.md | MERGED | [P-021 ICP & JTBD](../canonical/02-product/021-icp-and-jtbd.md) |
| B4-03-PRODUCTIZED-OFFERS-DOC.md | MERGED + DEFERRED | [C-081 Pricing Catalog](../canonical/08-commercial/081-pricing-catalog.md) (multi-SKU/multi-vertikal DEFERRED) |
| B4-04-WINNING-GTM-BROAD-DOC.md | MERGED | [C-080 GTM Strategy](../canonical/08-commercial/080-gtm-strategy.md) |
| B4-05-MIGRATION-MAP-DOC.md | SUPERSEDED | Dokumen ini (MIGRATION-MAP v2) |
| B4-06-OUTCOME-ECONOMY-THESIS-DOC.md | ARCHIVED | Tesis internal; konteks di [B-010](../canonical/01-brand/010-brand-architecture.md) (istilah internal) |
| B4-07-EXECUTION-LOG-DOC.md | ARCHIVED | Log historis; eksekusi aktif via [G-090](../canonical/09-governance/090-roadmap.md) |

## 3. archive/ssot/ — Batch 5 (7 file)

| File legacy | Disposisi | Target v2 |
|---|---|---|
| B5-00-INDEX.md | SUPERSEDED | [canonical/00-INDEX.md](../canonical/00-INDEX.md) |
| B5-01-OAAS-RESEARCH-DOC.md | ARCHIVED | Riset dasar; kesimpulan diserap [F-004](../canonical/00-foundation/004-decision-framework.md) |
| B5-02-OUTCOME-FOUNDRY-CONCEPT-DOC.md | MERGED | [B-010 Brand Architecture](../canonical/01-brand/010-brand-architecture.md) (Outcome Foundry = platform internal) |
| B5-03-OUTCOME-BUSINESS-MODEL-DOC.md | MERGED | [P-023 Packaging](../canonical/02-product/023-packaging-and-pricing.md) (prinsip hibrida), [C-081](../canonical/08-commercial/081-pricing-catalog.md) |
| B5-04-OUTCOME-DELIVERY-ENGINE-DOC.md | ARCHIVED | Konsep delivery internal; relevansi operasional via [O-061](../canonical/06-operations/061-runbooks-and-incident.md) |
| B5-05-PIVOT-EXECUTION-MAP-DOC.md | MERGED | [G-090 Roadmap](../canonical/09-governance/090-roadmap.md) (R-series dikonsolidasi) |
| B5-06-GAP-CLOSURE-AND-SYNTHESIS-DOC.md | MERGED | [AUDIT-REPORT-V2](AUDIT-REPORT-V2.md) |

## 4. archive/ssot/ — R6 & standards (3 file)

| File legacy | Disposisi | Target v2 |
|---|---|---|
| R6-3-EVAL-LOOP-SPEC.md | MERGED (arah) + DEFERRED (implementasi) | [AI-070 §2](../canonical/07-ai/070-ai-agents-policy.md) |
| R6-4-AGENTSHIELD-SKU-SPEC.md | DEFERRED | SKU ditunda; guardrail keamanan agent di [AI-070 §3](../canonical/07-ai/070-ai-agents-policy.md) |
| SKILL-AUTHORING-STANDARD.md | SUPERSEDED | [AI-072 Skill Authoring Standard](../canonical/07-ai/072-skill-authoring-standard.md) |

## 5. archive/ssot/foundry-master/ (24 file)

| File legacy | Disposisi | Target v2 |
|---|---|---|
| FM-00-INDEX.md | SUPERSEDED | [AI-071 Session OS](../canonical/07-ai/071-session-os.md) |
| FM-01-MASTER-ARCHITECT-PROMPT-DOC.md | MERGED | [AI-071 Session OS](../canonical/07-ai/071-session-os.md) |
| FM-02-MASTER-HANDOFF-DOC.md | MERGED | [AI-071 Session OS](../canonical/07-ai/071-session-os.md) |
| FM-03-MASTER-SPRINT-KAS-DOC.md | MERGED | [AI-071 Session OS](../canonical/07-ai/071-session-os.md) |
| FM-04-RESUME-BOOT-DOC.md | MERGED | [AI-071 Session OS](../canonical/07-ai/071-session-os.md) |
| MANIFEST.md, README.md, resume_boot.py | ARCHIVED | Tooling/manifest historis |
| handoffs/ (13 file: HANDOFF-BKF-2026*, LATEST.md) | ARCHIVED | Log sesi historis — tetap referensi audit trail |
| sprints/ (3 file: SPRINT-KAS-*, .gitkeep) | ARCHIVED | Log sprint historis |

## 6. archive/barberkas-aaas-bundle/ (15 file)

| File legacy | Disposisi | Target v2 |
|---|---|---|
| 01-STRATEGIC-BRIEF-v1.0 | SUPERSEDED | [P-020 Product Brief](../canonical/02-product/020-product-brief.md) |
| 02-SECRET-DOCTRINE-v1.0 | ARCHIVED | Doktrin internal; prinsip yang bertahan → [F-000 Charter](../canonical/00-foundation/000-charter.md), [F-004](../canonical/00-foundation/004-decision-framework.md) |
| 03-MONETIZATION-MATRIX-v1.0 | MERGED + DEFERRED | [C-081 Pricing Catalog](../canonical/08-commercial/081-pricing-catalog.md) |
| 04-MASTER-ARCHITECT-v1.0 | MERGED | [A-030 System Overview](../canonical/03-architecture/030-system-overview.md), ADR register |
| 05-SPRINT-PLAN-v1.0 | SUPERSEDED | [G-090 Roadmap](../canonical/09-governance/090-roadmap.md) |
| 06-EXECUTE-PLAYBOOK-v1.0 | SUPERSEDED | [G-090](../canonical/09-governance/090-roadmap.md) + [O-061 Runbooks](../canonical/06-operations/061-runbooks-and-incident.md) |
| 07-AGENT-PRD-v1.0 | MERGED + DEFERRED | [AI-070 AI Agents Policy](../canonical/07-ai/070-ai-agents-policy.md) (6 agent tambahan DEFERRED) |
| 08-DESIGN-SYSTEM-v1.0 | ARCHIVED | Diserap saat redesign landing (backlog G-090 31–60 hari item 9) |
| 09-TODO-CHECKLIST-v1.0 | SUPERSEDED | [G-090 Roadmap](../canonical/09-governance/090-roadmap.md) |
| 10-DR-ADDENDUM-v1.0 | MERGED | [O-062 Backup & DR](../canonical/06-operations/062-backup-and-dr.md) |
| 11-CROSS-BRAND-MAP-v1.0 | MERGED | [B-010 Brand Architecture](../canonical/01-brand/010-brand-architecture.md) |
| MASTER-BUNDLE-v1.0.html, MANIFEST.md, README.md, build_html.py | ARCHIVED | Artefak build/manifest historis |

## 7. Ringkasan

| Disposisi | Jumlah file |
|---|---|
| MERGED (± kombinasi DEFERRED) | 22 |
| SUPERSEDED | 12 |
| ARCHIVED | 25 |
| DEFERRED murni | 2 |
| **Total legacy** | **61** |

**Invariant:** tidak ada informasi dihapus tanpa jejak. Semua file legacy tetap ada di
`archive/` (read-only). Konflik legacy vs v2 → **v2 menang** (aturan inti README).

## Change History

| Version | Date | Change |
|---|---|---|
| 2.0.0 | 2026-07-10 | Peta migrasi lengkap 61 file legacy → canonical v2 dengan disposisi & target eksplisit |
