#!/usr/bin/env python3
"""
validate_docs.py — Canonical SSOT Quality Gate (Hardening Phase 3, RFC-001)

Menjalankan seluruh quality gate docs-as-code sesuai Q-991 §3:
  1. Front-matter YAML wajib ada & seluruh field wajib valid (tipe + enum)
  2. `id` unik di seluruh repo & terdaftar di MANIFEST (anti-orphan)
  3. `parent` / `related_docs` merujuk ID yang ada (anti-dangling)
  4. `status: approved` mensyaratkan `reviewers` tidak kosong
  5. `next_review` lewat → WARNING "review overdue"
  6. Broken relative link checker (semua [teks](path) intra-repo)
  7. Orphan detector: file canonical tanpa entri MANIFEST = error;
     entri MANIFEST tanpa file = dangling = error
  8. Heading validator: tepat satu H1 per dokumen, `title` == bagian H1
  9. Duplicate ID / duplicate H1 detector

Exit code: 0 = lolos (warning boleh), 1 = ada error.
Tanpa dependensi eksternal — hanya stdlib (front-matter diparse manual,
subset YAML yang dipakai Q-991: skalar, list inline [a, b], null).

Pemakaian:
    python3 tools/validate_docs.py [--root PATH]
"""

import argparse
import datetime
import os
import re
import sys

# ---------------------------------------------------------------- konstanta

SKIP_DIRS = {".git", "archive", "node_modules", ".wrangler", ".github"}
DOC_DIRS = ("canonical", "migration")  # folder yang wajib front-matter
ROOT_DOCS = ("MANIFEST.md",)           # dokumen root yang wajib front-matter

REQUIRED_FIELDS = [
    "id", "title", "version", "status", "owner", "reviewers",
    "classification", "type", "last_updated", "next_review",
    "parent", "related_docs",
]

ENUM_STATUS = {"draft", "review", "approved", "deprecated", "archived"}
ENUM_CLASSIFICATION = {"internal", "public-safe", "confidential"}
ENUM_TYPE = {
    "strategy", "policy", "standard", "guideline", "procedure",
    "runbook", "adr", "rfc", "specification", "register", "index", "report",
}
ENUM_OWNER = {
    "Founder", "Product", "Engineering", "Security", "Operations", "Commercial",
}

RE_SEMVER = re.compile(r"^\d+\.\d+\.\d+$")
RE_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
RE_LINK = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
RE_FENCE = re.compile(r"^```.*?^```\s*?$", re.M | re.S)

errors: list[str] = []
warnings: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


# ------------------------------------------------------------- front-matter

def parse_front_matter(text: str, path: str):
    """Parse subset YAML front-matter sesuai Q-991. Return dict | None."""
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        err(f"{path}: front-matter dibuka '---' tetapi tidak ditutup")
        return None
    body = text[3:end].strip("\n")
    meta = {}
    for line in body.splitlines():
        line = line.split("  #", 1)[0].rstrip()  # buang komentar inline
        if not line.strip() or line.strip().startswith("#"):
            continue
        if ":" not in line:
            err(f"{path}: baris front-matter tidak valid: {line!r}")
            continue
        key, _, val = line.partition(":")
        key = key.strip()
        val = val.strip()
        if val.startswith("[") and val.endswith("]"):
            inner = val[1:-1].strip()
            meta[key] = [v.strip() for v in inner.split(",") if v.strip()] if inner else []
        elif val in ("null", "~", ""):
            meta[key] = None
        else:
            meta[key] = val.strip("'\"")
    return meta


def validate_meta(meta: dict, path: str) -> None:
    for f in REQUIRED_FIELDS:
        if f not in meta:
            err(f"{path}: field wajib hilang: `{f}`")
    if "status" in meta and meta["status"] not in ENUM_STATUS:
        err(f"{path}: status tidak valid: {meta['status']!r} (enum: {sorted(ENUM_STATUS)})")
    if "classification" in meta and meta["classification"] not in ENUM_CLASSIFICATION:
        err(f"{path}: classification tidak valid: {meta['classification']!r}")
    if "type" in meta and meta["type"] not in ENUM_TYPE:
        err(f"{path}: type tidak valid: {meta['type']!r}")
    if "owner" in meta and meta["owner"] not in ENUM_OWNER:
        err(f"{path}: owner tidak valid: {meta['owner']!r} (role, bukan nama; enum: {sorted(ENUM_OWNER)})")
    if "version" in meta and not (isinstance(meta["version"], str) and RE_SEMVER.match(meta["version"] or "")):
        err(f"{path}: version bukan semver: {meta.get('version')!r}")
    for datef in ("last_updated", "next_review"):
        v = meta.get(datef)
        if datef in meta and not (isinstance(v, str) and RE_DATE.match(v or "")):
            err(f"{path}: {datef} bukan tanggal YYYY-MM-DD: {v!r}")
    if not isinstance(meta.get("reviewers"), list):
        err(f"{path}: reviewers harus list")
    if not isinstance(meta.get("related_docs"), list):
        err(f"{path}: related_docs harus list")
    # Aturan 4: approved wajib punya reviewer
    if meta.get("status") == "approved" and isinstance(meta.get("reviewers"), list) and not meta["reviewers"]:
        err(f"{path}: status approved tetapi reviewers kosong (Q-991 §3.4)")
    # Aturan 5: review overdue
    nr = meta.get("next_review")
    if isinstance(nr, str) and RE_DATE.match(nr):
        if datetime.date.fromisoformat(nr) < datetime.date.today():
            warn(f"{path}: review overdue (next_review {nr})")


# ------------------------------------------------------------------ helpers

def iter_md_files(root: str):
    for dirpath, dirnames, filenames in os.walk(root):
        rel = os.path.relpath(dirpath, root)
        parts = rel.split(os.sep)
        if parts[0] in SKIP_DIRS:
            dirnames[:] = []
            continue
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for f in sorted(filenames):
            if f.endswith(".md"):
                yield os.path.normpath(os.path.join(dirpath, f))


def needs_front_matter(relpath: str) -> bool:
    if relpath in ROOT_DOCS:
        return True
    return relpath.startswith(tuple(d + os.sep for d in DOC_DIRS))


def parse_manifest_ids(root: str):
    """Ambil registry §2 MANIFEST: {id: relpath|None}."""
    mpath = os.path.join(root, "MANIFEST.md")
    registry = {}
    if not os.path.exists(mpath):
        err("MANIFEST.md tidak ditemukan di root")
        return registry
    text = open(mpath, encoding="utf-8").read()
    sec = re.search(r"## 2\. Registry dokumen(.*?)(?=\n## |\Z)", text, re.S)
    if not sec:
        err("MANIFEST.md: seksi '## 2. Registry dokumen' tidak ditemukan")
        return registry
    for line in sec.group(1).splitlines():
        if not line.startswith("|") or line.startswith("|---") or "| ID |" in line:
            continue
        cols = [c.strip() for c in line.strip("|").split("|")]
        if len(cols) < 2 or not cols[0]:
            continue
        doc_id = cols[0]
        m = RE_LINK.search(cols[1])
        registry[doc_id] = os.path.normpath(m.group(2)) if m else None
    return registry


# --------------------------------------------------------------------- main

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    args = ap.parse_args()
    root = os.path.abspath(args.root)

    manifest = parse_manifest_ids(root)
    seen_ids: dict[str, str] = {}
    all_meta: dict[str, dict] = {}
    files = list(iter_md_files(root))

    # ---- pass 1: front-matter, heading, links
    for path in files:
        rel = os.path.relpath(path, root)
        text = open(path, encoding="utf-8", errors="replace").read()
        # buang fenced code block agar contoh template tidak dihitung H1/link
        scanned = RE_FENCE.sub("", text)

        # H1 check
        h1s = re.findall(r"^# (.+)$", scanned, re.M)
        if len(h1s) == 0:
            err(f"{rel}: tidak punya H1")
        elif len(h1s) > 1:
            err(f"{rel}: H1 duplikat ({len(h1s)} buah)")

        # broken links (semua md, termasuk yang tanpa front-matter)
        for m in RE_LINK.finditer(scanned):
            link = m.group(2).split("#")[0].strip()
            if not link or link.startswith(("http://", "https://", "mailto:")):
                continue
            target = os.path.normpath(os.path.join(os.path.dirname(path), link))
            if not os.path.exists(target):
                err(f"{rel}: broken link → ({m.group(2)})")

        if not needs_front_matter(rel):
            continue

        meta = parse_front_matter(text, rel)
        if meta is None:
            err(f"{rel}: front-matter YAML wajib (Q-991) tidak ditemukan")
            continue
        validate_meta(meta, rel)
        all_meta[rel] = meta

        doc_id = meta.get("id")
        if doc_id:
            if doc_id in seen_ids:
                err(f"{rel}: ID duplikat `{doc_id}` (sudah dipakai {seen_ids[doc_id]})")
            else:
                seen_ids[doc_id] = rel
            # orphan check: wajib terdaftar di MANIFEST
            if doc_id not in manifest:
                err(f"{rel}: ORPHAN — id `{doc_id}` tidak terdaftar di MANIFEST §2")

        # title == H1 (bagian setelah em-dash bila ada)
        if h1s and meta.get("title"):
            h1 = h1s[0]
            h1_title = h1.split("—", 1)[1].strip() if "—" in h1 else h1.strip()
            if meta["title"] not in (h1_title, h1.strip()):
                warn(f"{rel}: title front-matter ({meta['title']!r}) ≠ H1 ({h1_title!r})")

    # ---- pass 2: dangling parent/related & manifest ↔ file
    for rel, meta in all_meta.items():
        parent = meta.get("parent")
        if parent is not None and parent not in seen_ids:
            err(f"{rel}: parent dangling → `{parent}` tidak ada")
        if parent is None and meta.get("id") != "F-000":
            err(f"{rel}: parent null hanya boleh untuk F-000 (Q-991 §2)")
        for rd in meta.get("related_docs") or []:
            if rd not in seen_ids:
                err(f"{rel}: related_docs dangling → `{rd}` tidak ada")

    for doc_id, relpath in manifest.items():
        if doc_id not in seen_ids:
            err(f"MANIFEST.md: entri dangling — `{doc_id}` tidak ditemukan sebagai front-matter id di repo")
        if relpath and not os.path.exists(os.path.join(root, relpath)):
            err(f"MANIFEST.md: entri `{doc_id}` menunjuk file yang tidak ada: {relpath}")

    # ---- laporan
    print(f"Dokumen diperiksa : {len(files)}")
    print(f"Front-matter valid: {len(all_meta)}")
    print(f"ID terdaftar      : {len(seen_ids)} (MANIFEST: {len(manifest)})")
    if warnings:
        print(f"\nWARNING ({len(warnings)}):")
        for w in warnings:
            print(f"  ⚠ {w}")
    if errors:
        print(f"\nERROR ({len(errors)}):")
        for e in errors:
            print(f"  ✗ {e}")
        print("\nQUALITY GATE: FAILED")
        return 1
    print("\nQUALITY GATE: PASSED ✅")
    return 0


if __name__ == "__main__":
    sys.exit(main())
