# tools/ — Docs Quality Gates

Tooling docs-as-code untuk Canonical SSOT (Hardening Phase 3, RFC-001).

## validate_docs.py

Quality gate tunggal, tanpa dependensi eksternal (stdlib only).

```bash
python3 tools/validate_docs.py [--root PATH]
```

| # | Gate | Sumber aturan | Severity |
|---|---|---|---|
| 1 | Front-matter YAML wajib + tipe/enum valid | Q-991 §1–2 | error |
| 2 | `id` unik seluruh repo | Q-991 §3.2 | error |
| 3 | `parent` / `related_docs` tidak dangling | Q-991 §3.3 | error |
| 4 | `status: approved` wajib punya reviewers | Q-991 §3.4 | error |
| 5 | `next_review` lewat tanggal | Q-991 §3.5 | warning |
| 6 | Broken relative link | Q-990 | error |
| 7 | Orphan (file tanpa entri MANIFEST) & dangling manifest | MANIFEST §3 | error |
| 8 | Tepat satu H1; `title` ≈ H1 | Q-990 | error / warning |

Exit code `0` = lolos (warning boleh ada), `1` = gagal.
Fenced code block diabaikan (contoh template tidak dihitung H1/link).

## CI

Workflow [tools/ci/docs-quality.yml](ci/docs-quality.yml) menjalankan gate ini pada
setiap push & pull request ke `main`. Commit yang gagal gate **tidak boleh
di-merge** (G-094 §review).

> **Aktivasi:** token GitHub App yang dipakai bot tidak punya permission
> `workflows`, sehingga file CI disimpan di `tools/ci/`. Untuk mengaktifkan,
> salin manual sekali via web/CLI dengan akun yang berwenang:
>
> ```bash
> mkdir -p .github/workflows
> cp tools/ci/docs-quality.yml .github/workflows/
> git add .github && git commit -m "ci: enable docs quality gate" && git push
> ```

## Cakupan

- Wajib front-matter: `canonical/**`, `migration/**`, `MANIFEST.md`.
- Dikecualikan: `archive/` (frozen legacy), `README.md`, `CHANGELOG.md`, `tools/README.md`.
