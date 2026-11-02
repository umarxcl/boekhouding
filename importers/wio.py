#!/usr/bin/env python3
"""Importer voor Wio Business CSV-exporten (XCL).

Gebruik:
    python3 importers/wio.py <export.csv> [--ledger xcl/main.beancount] [--rules importers/rules_xcl.yaml]
                             [--out xcl/2026/import_<datum>.beancount] [--dry-run]

Wat het doet:
  1. Leest de Wio-export (beide rekeningen, AED en EUR, in een bestand).
  2. Slaat regels over waarvan het referentienummer al in het grootboek staat (dedup).
  3. Koppelt valutawissels (EUR-regel + AED-regel met opeenvolgende referentienummers) tot een boeking met koers.
  4. Koppelt Wio's wisselkoersopslag ("Original ref. number") aan de kaartbetaling waar hij bij hoort.
  5. Categoriseert op de regels in rules_xcl.yaml; zonder regel: Expenses:Onbekend met vlag "!".
  6. Schrijft Beancount-boekingen met metadata (ref, bron, uitleg) en een uitzonderingenlijst (JSON) voor de goedkeurings-Sheet.

Alles wat de importer niet zeker weet krijgt de vlag "!" en komt op de lijst. De importer boekt nooit iets definitief:
pas na goedkeuring wordt de vlag weggehaald en de maand gesloten.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import OrderedDict
from dataclasses import dataclass, field
from datetime import date
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

import yaml

ACCOUNT_BY_IBAN = {
    "AE450860000009202341633": ("Assets:Bank:Wio-AED", "AED"),
    "AE320860000009506419892": ("Assets:Bank:Wio-EUR", "EUR"),
}
UNKNOWN = "Expenses:Onbekend"
PRICES = Path(__file__).resolve().parent.parent / "shared/prices.beancount"


def load_prices() -> list[tuple[date, Decimal]]:
    """EUR/AED-koersen uit shared/prices.beancount (CBUAE), oplopend op datum."""
    out = []
    for line in PRICES.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^(\d{4}-\d{2}-\d{2})\s+price\s+EUR\s+([\d.]+)\s+AED", line)
        if m:
            out.append((date.fromisoformat(m.group(1)), Decimal(m.group(2))))
    return sorted(out)


def rate_on(prices: list[tuple[date, Decimal]], d: date) -> Decimal | None:
    """Laatste CBUAE-koers op of vóór de datum (None als er geen is: dan komt de post op de lijst)."""
    r = None
    for pd_, px in prices:
        if pd_ <= d:
            r = px
        else:
            break
    return r


@dataclass
class Row:
    iban: str
    currency: str
    ttype: str
    date: date
    ref: str
    desc: str
    amount: Decimal
    balance: Decimal
    orig_ref: str
    notes: str
    account: str = ""
    payee: str = ""
    flag: str = ""
    nl: str = ""
    fx_fee: Decimal | None = None
    fx_fee_ref: str = ""

    @property
    def bank_account(self) -> str:
        return ACCOUNT_BY_IBAN[self.iban][0]


def q2(x: Decimal) -> Decimal:
    return x.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def read_export(path: Path) -> list[Row]:
    rows: list[Row] = []
    with path.open(newline="", encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            iban = r["Account IBAN"].strip()
            if iban not in ACCOUNT_BY_IBAN:
                raise SystemExit(f"Onbekende rekening in export: {iban}")
            rows.append(Row(
                iban=iban,
                currency=r["Account currency"].strip(),
                ttype=r["Transaction type"].strip(),
                date=date.fromisoformat(r["Date"].strip()),
                ref=r["Ref. number"].strip(),
                desc=r["Description"].strip(),
                amount=Decimal(r["Amount"].strip()),
                balance=Decimal(r["Balance"].strip()),
                orig_ref=(r.get("Original ref. number") or "").strip(),
                notes=(r.get("Notes") or "").strip(),
            ))
    return rows


def existing_refs(ledger: Path) -> set[str]:
    """Referentienummers die al in het grootboek staan (metadata wio-ref en wio-fee-ref)."""
    refs: set[str] = set()
    pat = re.compile(r'^\s*wio-(?:ref|fee-ref|ref-2):\s*"?(\d+)"?', re.M)
    for p in [ledger.parent / "2026"]:
        if p.is_dir():
            for f in p.glob("*.beancount"):
                refs.update(pat.findall(f.read_text(encoding="utf-8")))
    return refs


def load_rules(path: Path) -> list[dict]:
    return yaml.safe_load(path.read_text(encoding="utf-8"))["rules"]


def match_rule(row: Row, rules: list[dict]) -> dict | None:
    hay = f"{row.ttype} {row.desc} {row.notes}".lower()
    for rule in rules:
        if rule.get("type") and rule["type"].lower() != row.ttype.lower():
            continue
        ok = True
        for frag in rule["match"]:
            if frag.startswith("re:"):
                if not re.search(frag[3:], hay, re.I):
                    ok = False
                    break
            elif frag.lower() not in hay:
                ok = False
                break
        if ok:
            return rule
    return None


def pair_fx(rows: list[Row]) -> list[tuple[Row, Row]]:
    """Koppel EUR-naar-AED wissels: de EUR-afboeking en de AED-bijboeking hebben opeenvolgende referentienummers."""
    ex = [r for r in rows if r.ttype == "Currency exchange"]
    pairs: list[tuple[Row, Row]] = []
    used: set[str] = set()
    for a in ex:
        if a.ref in used or a.amount >= 0:
            continue
        for b in ex:
            if b.ref in used or b is a or b.amount <= 0 or b.date != a.date:
                continue
            if abs(int(b.ref) - int(a.ref)) <= 2 and b.currency != a.currency:
                pairs.append((a, b))
                used.update({a.ref, b.ref})
                break
    return pairs


def attach_fees(rows: list[Row]) -> None:
    """Wio's wisselkoersopslag hoort bij de kaartbetaling met hetzelfde 'Original ref. number'."""
    by_ref = {r.ref: r for r in rows}
    for r in rows:
        if r.ttype == "Fees" and r.orig_ref and r.orig_ref in by_ref:
            parent = by_ref[r.orig_ref]
            parent.fx_fee = (parent.fx_fee or Decimal("0")) + r.amount
            parent.fx_fee_ref = r.ref
            r.ttype = "_attached"


def fmt_amount(x: Decimal, cur: str) -> str:
    return f"{q2(x):,.2f} {cur}"


def entry_for(row: Row, prices: list[tuple[date, Decimal]]) -> str:
    acct = row.account or UNKNOWN
    flag = row.flag or ("!" if acct == UNKNOWN else "*")
    # Resultaatrekeningen voeren alleen AED: een EUR-regel wordt omgerekend tegen de CBUAE-koers van de dag.
    convert = row.currency == "EUR" and acct.split(":")[0] in ("Income", "Expenses")
    rate = rate_on(prices, row.date) if convert else None
    if convert and rate is None:
        flag = "!"
    payee = row.payee or row.desc
    narration = row.desc if row.notes in ("", "N/A") else f"{row.desc} | {row.notes}"
    lines = [f'{row.date.isoformat()} {flag} "{payee}" "{narration}"',
             f'  wio-ref: "{row.ref}"',
             f'  wio-type: "{row.ttype}"',
             f'  bron: "Wio-export"']
    if row.nl:
        lines.append(f'  nl: "{row.nl}"')
    if row.fx_fee:
        lines.append(f'  wio-fee-ref: "{row.fx_fee_ref}"')
    if convert and rate is not None:
        aed = q2(-row.amount * rate)
        lines.append(f'  koers: "CBUAE {rate} AED per EUR"')
        lines.append(f"  {row.bank_account:<42} {fmt_amount(row.amount, 'EUR'):>18} @@ {fmt_amount(abs(aed), 'AED')}")
        lines.append(f"  {acct:<42} {fmt_amount(aed, 'AED'):>18}")
        return "\n".join(lines) + "\n"
    if convert and rate is None:
        lines.append(f'  nl: "Geen CBUAE-koers voor deze datum in shared/prices.beancount: koers toevoegen"')
    lines.append(f"  {row.bank_account:<42} {fmt_amount(row.amount, row.currency):>18}")
    if row.fx_fee:
        lines.append(f"  {row.bank_account:<42} {fmt_amount(row.fx_fee, row.currency):>18}")
        lines.append(f"  {'Expenses:Bank:Wisselkosten':<42} {fmt_amount(-row.fx_fee, row.currency):>18}")
    lines.append(f"  {acct:<42} {fmt_amount(-row.amount, row.currency):>18}")
    return "\n".join(lines) + "\n"


def entry_for_fx(a: Row, b: Row) -> str:
    """a = EUR-afboeking (negatief), b = AED-bijboeking (positief)."""
    rate = (b.amount / -a.amount).quantize(Decimal("0.0001"))
    return "\n".join([
        f'{a.date.isoformat()} * "Wio" "Valutawissel {a.currency} naar {b.currency} (koers {rate})"',
        f'  wio-ref: "{a.ref}"',
        f'  wio-ref-2: "{b.ref}"',
        f'  wio-type: "Currency exchange"',
        f'  bron: "Wio-export"',
        f"  {a.bank_account:<42} {fmt_amount(a.amount, a.currency):>18} @@ {fmt_amount(b.amount, b.currency)}",
        f"  {b.bank_account:<42} {fmt_amount(b.amount, b.currency):>18}",
    ]) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("csv", type=Path)
    ap.add_argument("--ledger", type=Path, default=Path("xcl/main.beancount"))
    ap.add_argument("--rules", type=Path, default=Path("importers/rules_xcl.yaml"))
    ap.add_argument("--out", type=Path)
    ap.add_argument("--exceptions", type=Path, help="JSON met de uitzonderingenlijst voor de goedkeurings-Sheet")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    rows = read_export(args.csv)
    seen = existing_refs(args.ledger)
    before = len(rows)
    rows = [r for r in rows if r.ref not in seen]
    skipped = before - len(rows)

    attach_fees(rows)
    fx_pairs = pair_fx(rows)
    fx_refs = {r.ref for p in fx_pairs for r in p}
    rules = load_rules(args.rules)
    prices = load_prices()

    entries: list[str] = []
    exceptions: list[dict] = []
    last_balance: dict[str, tuple[date, Decimal, str]] = {}
    first_balance: dict[str, tuple[date, Decimal, str]] = {}

    for r in sorted(rows, key=lambda x: (x.date, int(x.ref))):
        if r.iban not in first_balance:
            # saldo vóór de eerste regel van de export: moet aansluiten op wat al in het grootboek staat
            first_balance[r.iban] = (r.date, r.balance - r.amount, r.currency)
        last_balance[r.iban] = (r.date, r.balance, r.currency)
        if r.ttype == "_attached" or r.ref in fx_refs:
            continue
        rule = match_rule(r, rules)
        if rule:
            r.account, r.payee = rule["account"], rule.get("payee", "")
            r.flag, r.nl = rule.get("flag", ""), rule.get("nl", "")
        entries.append(entry_for(r, prices))
        if not rule or r.flag == "!":
            exceptions.append({
                "datum": r.date.isoformat(), "ref": r.ref, "rekening": r.bank_account,
                "bedrag": str(q2(r.amount)), "valuta": r.currency,
                "omschrijving": r.desc, "notitie": r.notes,
                "voorstel": r.account or UNKNOWN, "uitleg": r.nl or "Geen regel gevonden: welke rekening?",
                "akkoord": "", "opmerking": "",
            })
    for a, b in fx_pairs:
        entries.append(entry_for_fx(a, b))

    # Saldo-controle per rekening op de laatste dag van de export: Beancount checkt dit bij bean-check.
    balances = ["; Saldocontroles: begin (sluit aan op het grootboek vóór deze export) en einde (laatste regel van de export)\n"]
    for iban, (d, bal, cur) in first_balance.items():
        acct = ACCOUNT_BY_IBAN[iban][0]
        balances.append(f"{d.isoformat()} balance {acct:<32} {fmt_amount(bal, cur)}\n")
    for iban, (d, bal, cur) in last_balance.items():
        acct = ACCOUNT_BY_IBAN[iban][0]
        nxt = d.toordinal() + 1
        balances.append(f"{date.fromordinal(nxt).isoformat()} balance {acct:<32} {fmt_amount(bal, cur)}\n")

    header = (f"; Import uit {args.csv.name}\n; {len(entries)} boekingen, {len(fx_pairs)} valutawissels, "
              f"{skipped} regels overgeslagen (al aanwezig), {len(exceptions)} op de uitzonderingenlijst\n\n")
    text = header + "\n".join(sorted(entries)) + "\n" + "".join(balances)

    if args.dry_run or not args.out:
        sys.stdout.write(text)
    else:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text, encoding="utf-8")
        print(f"Geschreven: {args.out} ({len(entries)} boekingen, {len(exceptions)} uitzonderingen, {skipped} overgeslagen)")
    if args.exceptions:
        args.exceptions.write_text(json.dumps(exceptions, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
