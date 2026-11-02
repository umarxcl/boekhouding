#!/usr/bin/env python3
"""Splits the output of importers/wio.py into xcl/2026/MM.beancount (one file per month).

Usage: python3 scripts/split_maanden.py <import.beancount> [--dir xcl/2026] [--year 2026] [--force]

An entry belongs to the month of its date. Balance assertions follow the same rule; a balance assertion on the first day of
the month AFTER the last month goes into the file of the last month. An existing month file is never overwritten without
--force: month files contain owner-review edits (approved, owner-answer, note, reclassifications) that the import does not
reproduce. For a later import into a month that already has a file, append the new entries instead.
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
          "December"]


def is_balance(block: str) -> bool:
    return re.match(r"^\d{4}-\d{2}-\d{2} balance ", block) is not None


def blocks(text: str) -> list[str]:
    """Cut the text into blocks: an entry (header plus indented lines) or a single line."""
    out, cur = [], []
    for line in text.splitlines():
        if re.match(r"^\d{4}-\d{2}-\d{2} ", line):
            if cur:
                out.append("\n".join(cur))
            cur = [line]
        elif line.startswith((" ", "\t")) and cur:
            cur.append(line)
        else:
            if cur:
                out.append("\n".join(cur))
                cur = []
    if cur:
        out.append("\n".join(cur))
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("source", type=Path)
    ap.add_argument("--dir", type=Path, default=Path("xcl/2026"))
    ap.add_argument("--year", default="2026")
    ap.add_argument("--force", action="store_true", help="overwrite existing month files (owner-review edits are lost)")
    args = ap.parse_args()

    per_month: dict[str, list[str]] = defaultdict(list)
    for b in blocks(args.source.read_text(encoding="utf-8")):
        per_month[b[5:7]].append(b)
    months = sorted(m for m in per_month if per_month[m])
    last = months[-1]
    # balance assertions after the last month (first day of the next month) belong to the last month
    if int(last) < 12:
        nxt = f"{int(last) + 1:02d}"
        if nxt in per_month and all(is_balance(b) for b in per_month[nxt]):
            per_month[last].extend(per_month.pop(nxt))
    existing = [args.dir / f"{m}.beancount" for m in per_month if (args.dir / f"{m}.beancount").exists()]
    if existing and not args.force:
        sys.exit("Refusing to overwrite existing month files (they may contain owner-review edits): "
                 + ", ".join(str(p) for p in existing) + ". Use --force to overwrite.")
    args.dir.mkdir(parents=True, exist_ok=True)
    for m in sorted(per_month):
        month_blocks = sorted(per_month[m], key=lambda b: (b[:10], not is_balance(b), b))
        n_tx = sum(1 for b in month_blocks if not is_balance(b))
        head = (f"; XCL entries {MONTHS[int(m) - 1]} {args.year} (importer wio.py from the Wio annual export; {n_tx} entries)\n"
                f"; Attachments: Drive Boekhouding/XCL/Inkoop {args.year}. Flag ! = not yet reviewed (see Sheet 'Boekhouding - Goedkeuring').\n\n")
        (args.dir / f"{m}.beancount").write_text(head + "\n\n".join(month_blocks) + "\n", encoding="utf-8")
        print(f"{args.dir}/{m}.beancount: {n_tx} entries")


if __name__ == "__main__":
    main()
