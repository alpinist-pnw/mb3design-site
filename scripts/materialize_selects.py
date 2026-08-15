#!/usr/bin/env python3
"""Materialize 04-Website Vault from docs/ref/selects_manifest.csv.

The manifest is the source of truth. This script is idempotent and copy-only:
  - copies each row's canonical original into 04-Website Vault/{project}/{chapter}/
  - hash-verifies every copy (sha256)
  - never touches originals; never deletes anything unless --prune is passed
  - writes _materialized.csv (run record) into 04-Website Vault

Manifest columns: project,chapter,beat,hero,source_path,notes
  source_path is relative to the vault root (e.g. "01-Projects Vault/C2M/M100-.../04_Drawings/x.pdf")

Usage:
  python3 scripts/materialize_selects.py --dry-run
  python3 scripts/materialize_selects.py
  python3 scripts/materialize_selects.py --prune   # remove staged files no longer in manifest
"""
import argparse, csv, hashlib, shutil, sys
from datetime import datetime
from pathlib import Path

VAULT = Path("/Users/mark/Library/CloudStorage/GoogleDrive-mark@mb3ltd.com/My Drive/VAULT/MB3 DESIGN-VAULT")
WEB = VAULT / "04-Website Vault"
MANIFEST = Path(__file__).resolve().parent.parent / "docs/ref/selects_manifest.csv"
CHAPTERS = {"01_Vision","02_Translation","03_Prototyping","04_Fabrication","05_Logistics","06_Install","07_Reveal"}
KEEP = {"_README.md", "_materialized.csv"}

def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--prune", action="store_true", help="delete staged files not in manifest")
    a = ap.parse_args()

    rows = list(csv.DictReader(MANIFEST.open(newline="")))
    errors, planned = [], []
    for i, r in enumerate(rows, 2):
        if r["chapter"] not in CHAPTERS:
            errors.append(f"line {i}: bad chapter {r['chapter']!r}"); continue
        src = VAULT / r["source_path"]
        if not src.is_file():
            errors.append(f"line {i}: source missing: {r['source_path']}"); continue
        dst = WEB / r["project"] / r["chapter"] / src.name
        planned.append((r, src, dst))
    if errors:
        print("MANIFEST ERRORS:\n  " + "\n  ".join(errors)); sys.exit(1)

    expected = {dst for _, _, dst in planned}
    dups = [d for d in expected if sum(1 for *_, x in planned if x == d) > 1]
    if dups:
        print("COLLISIONS (same filename, same project/chapter):\n  " + "\n  ".join(map(str, dups))); sys.exit(1)

    copied = skipped = 0
    record = []
    for r, src, dst in planned:
        h = sha256(src)
        status = "exists"
        if dst.exists() and sha256(dst) == h:
            skipped += 1
        else:
            status = "copy"
            if not a.dry_run:
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)
                if sha256(dst) != h:
                    print(f"HASH MISMATCH after copy: {dst}"); sys.exit(2)
            copied += 1
        print(f"{status:6} {r['project']}/{r['chapter']}/{src.name}")
        record.append({**r, "select_path": str(dst.relative_to(VAULT)), "sha256": h})

    # stale = staged files not in manifest
    stale = [p for p in WEB.rglob("*") if p.is_file() and p.name not in KEEP and not p.name.startswith(".") and p not in expected]
    for p in stale:
        if a.prune and not a.dry_run:
            p.unlink(); print(f"pruned {p.relative_to(WEB)}")
        else:
            print(f"STALE  {p.relative_to(WEB)}  (not in manifest; --prune to remove)")

    if not a.dry_run:
        with (WEB / "_materialized.csv").open("w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["project","chapter","beat","hero","source_path","select_path","sha256","notes"])
            w.writeheader(); w.writerows(record)
        (WEB / "_materialized.csv").touch()
    print(f"\n{'DRY RUN — ' if a.dry_run else ''}{len(planned)} selects: {copied} copied, {skipped} already current, {len(stale)} stale, run {datetime.now():%Y-%m-%dT%H%M}")

if __name__ == "__main__":
    main()
