#!/usr/bin/env python3
"""Splitst de uitvoer van importers/wio.py in xcl/2026/MM.beancount (een bestand per maand).

Gebruik: python3 scripts/split_maanden.py <import.beancount> [--dir xcl/2026] [--jaar 2026]

Een boeking hoort bij de maand van haar datum. Saldocontroles (balance) volgen dezelfde regel; een saldocontrole die op de
eerste dag van de maand NA de laatste maand valt, komt in het bestand van de laatste maand. Een bestaand bestand voor
dezelfde maand wordt overschreven (de import is de bron; handmatige correcties horen in een nieuwe boeking in de lopende maand).
"""
from __future__ import annotations

import argparse
import re
from collections import defaultdict
from pathlib import Path

MAANDEN = ["januari", "februari", "maart", "april", "mei", "juni", "juli", "augustus", "september", "oktober", "november", "december"]


def is_saldo(blok: str) -> bool:
    return re.match(r"^\d{4}-\d{2}-\d{2} balance ", blok) is not None


def blokken(text: str) -> list[str]:
    """Knip de tekst in blokken: een boeking (kop plus ingesprongen regels) of een losse regel."""
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
    ap.add_argument("bron", type=Path)
    ap.add_argument("--dir", type=Path, default=Path("xcl/2026"))
    ap.add_argument("--jaar", default="2026")
    args = ap.parse_args()

    per_maand: dict[str, list[str]] = defaultdict(list)
    for b in blokken(args.bron.read_text(encoding="utf-8")):
        per_maand[b[5:7]].append(b)
    maanden = sorted(m for m in per_maand if per_maand[m])
    laatste = maanden[-1]
    # saldocontroles na de laatste maand (eerste dag van de volgende maand) horen bij de laatste maand
    if int(laatste) < 12:
        volgende = f"{int(laatste) + 1:02d}"
        if volgende in per_maand and all(is_saldo(b) for b in per_maand[volgende]):
            per_maand[laatste].extend(per_maand.pop(volgende))
    args.dir.mkdir(parents=True, exist_ok=True)
    for m in sorted(per_maand):
        blokken_m = sorted(per_maand[m], key=lambda b: (b[:10], not is_saldo(b), b))
        n_tx = sum(1 for b in blokken_m if not is_saldo(b))
        kop = (f"; Boekingen XCL {MAANDEN[int(m) - 1]} {args.jaar} (importer wio.py uit de Wio-jaarexport; {n_tx} boekingen)\n"
               f"; Bijlagen: Drive Boekhouding/XCL/Inkoop {args.jaar}. Vlag ! = nog niet beoordeeld (zie Sheet Boekhouding - Goedkeuring).\n\n")
        (args.dir / f"{m}.beancount").write_text(kop + "\n\n".join(blokken_m) + "\n", encoding="utf-8")
        print(f"{args.dir}/{m}.beancount: {n_tx} boekingen")


if __name__ == "__main__":
    main()
