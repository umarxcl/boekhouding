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

  7. Koppelt bijlagen uit Drive via importers/documenten_xcl.yaml (sleutel: Wio-referentie): metadata document/drive-id en,
     als de bon de uitgave zakelijk maakt (regel Umar 2-11-2026), de zakelijke rekening in plaats van de rekening-courant.
  8. Schrijft per maand-eerste een balance-regel per bankrekening, zodat elk maandsaldo tegen het Wio-afschrift sluit.

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


def rate_on(prices: list[tuple[date, Decimal]], d: date) -> tuple[date, Decimal] | None:
    """Laatste CBUAE-koers op of vóór de datum (None als er geen is: dan komt de post op de lijst)."""
    r = None
    for pd_, px in prices:
        if pd_ <= d:
            r = (pd_, px)
        else:
            break
    return r


def load_account_currencies(accounts: Path) -> dict[str, set[str]]:
    """Toegestane valuta's per rekening uit accounts.beancount (de importer past het rekeningschema nooit aan)."""
    out: dict[str, set[str]] = {}
    for line in accounts.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\d{4}-\d{2}-\d{2}\s+open\s+(\S+)\s+([A-Z,]+)", line)
        if m:
            out[m.group(1)] = set(m.group(2).split(","))
    return out


def load_documents(path: Path) -> dict[str, dict]:
    """Bijlagekoppelingen per Wio-referentie (importers/documenten_xcl.yaml)."""
    if not path.exists():
        return {}
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return {str(k): v for k, v in (data.get("documenten") or {}).items()}


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
    fx_fee_kind: str = ""
    tags: str = ""
    docs: list = field(default_factory=list)
    final: tuple = ()

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
    hay = f"{row.ttype} {row.desc} {row.notes} {row.tags}".lower()
    for rule in rules:
        if rule.get("type") and rule["type"].lower() != row.ttype.lower():
            continue
        if rule.get("currency") and rule["currency"] != row.currency:
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
    """Koppel valutawissels: de afboeking (negatief) en de bijboeking (positief) in de andere valuta staan op dezelfde dag met
    dicht bij elkaar liggende referentienummers; de koers EUR/AED moet geloofwaardig zijn (3,9 tot 4,7)."""
    ex = sorted((r for r in rows if r.ttype == "Currency exchange"), key=lambda r: (r.date, int(r.ref)))
    pairs: list[tuple[Row, Row]] = []
    used: set[str] = set()
    for a in ex:
        if a.ref in used or a.amount >= 0:
            continue
        best = None
        for b in ex:
            if b.ref in used or b is a or b.amount <= 0 or b.date != a.date or b.currency == a.currency:
                continue
            gap = abs(int(b.ref) - int(a.ref))
            aed, eur = (b.amount, -a.amount) if b.currency == "AED" else (-a.amount, b.amount)
            if gap <= 12 and Decimal("3.9") <= aed / eur <= Decimal("4.7") and (best is None or gap < best[0]):
                best = (gap, b)
        if best:
            pairs.append((a, best[1]))
            used.update({a.ref, best[1].ref})
    return pairs


def attach_fees(rows: list[Row]) -> None:
    """Wio's wisselkoersopslag hoort bij de kaartbetaling met hetzelfde 'Original ref. number'."""
    by_ref = {r.ref: r for r in rows}
    for r in rows:
        if r.ttype == "Fees" and r.orig_ref and r.orig_ref in by_ref:
            parent = by_ref[r.orig_ref]
            parent.fx_fee = (parent.fx_fee or Decimal("0")) + r.amount
            parent.fx_fee_ref = r.ref
            parent.tags += " " + r.desc.lower()
            if "foreign exchange" not in r.desc.lower():
                parent.fx_fee_kind = "overig"
            r.ttype = "_attached"


def fmt_amount(x: Decimal, cur: str) -> str:
    return f"{q2(x):,.2f} {cur}"


PRIVATE = "Assets:Rekening-courant:Umar"


def entry_for(row: Row, prices: list[tuple[date, Decimal]], acct_cur: dict[str, set[str]] | None = None) -> str:
    acct = row.account or UNKNOWN
    flag = row.flag or ("!" if acct == UNKNOWN else "*")
    allowed = (acct_cur or {}).get(acct)
    extra_nl = ""
    # Rekeningen die geen EUR voeren (resultaat, eigen vermogen, AED-debiteuren): een EUR-regel wordt omgerekend tegen de
    # CBUAE-koers van de dag. Geen koers = vlag "!". Een AED-regel op een rekening zonder AED valt terug op Onbekend.
    convert = row.currency == "EUR" and allowed is not None and "EUR" not in allowed
    if convert is False and row.currency == "EUR" and allowed is None:
        convert = acct.split(":")[0] in ("Income", "Expenses")
    if allowed is not None and row.currency not in allowed and not convert:
        extra_nl = f"Rekening {acct} kent geen {row.currency}: ontbrekende rekening of andere keuze nodig"
        acct, flag = UNKNOWN, "!"
    found = rate_on(prices, row.date) if convert else None
    rate = found[1] if found else None
    stale = bool(found) and (row.date - found[0]).days > 4
    if convert and (rate is None or stale):
        flag = "!"
        extra_nl = ("Geen CBUAE-koers van deze dag in shared/prices.beancount; laatst bekende koers gebruikt, koers toevoegen"
                    if rate is not None else "Geen CBUAE-koers beschikbaar: koers toevoegen")
    payee = row.payee or row.desc
    narration = row.desc if row.notes in ("", "N/A") else f"{row.desc} | {row.notes}"
    narration = narration.replace('"', "'")
    row.final = (acct, flag)
    lines = [f'{row.date.isoformat()} {flag} "{payee}" "{narration}"',
             f'  wio-ref: "{row.ref}"',
             f'  wio-type: "{row.ttype}"',
             f'  bron: "Wio-export"']
    inv = re.search(r"INV-\d{4}", row.notes)
    if inv:
        lines.append(f'  factuur: "{inv.group(0)}"')
    for i, (dname, did) in enumerate(row.docs):
        suf = "" if i == 0 else f"-{i + 1}"
        lines.append(f'  document{suf}: "{dname}"')
        lines.append(f'  drive-id{suf}: "{did}"')
    nl = row.nl or extra_nl
    if row.nl and extra_nl:
        nl = f"{row.nl} | {extra_nl}"
    if nl:
        lines.append(f'  nl: "{nl}"')
    if row.fx_fee:
        lines.append(f'  wio-fee-ref: "{row.fx_fee_ref}"')
    # Kosten die Wio bij de betaling rekent: bij een privé-uitgave horen ze bij de rekening-courant, anders bankkosten.
    fee_acct = ("Expenses:Bank:Kosten" if row.fx_fee_kind == "overig" else "Expenses:Bank:Wisselkosten")
    if row.fx_fee and acct == PRIVATE:
        fee_acct = PRIVATE
    if convert and rate is not None:
        aed = q2(-row.amount * rate)
        lines.append(f'  koers: "CBUAE {rate} AED per EUR (koers van {found[0].isoformat()})"')
        lines.append(f"  {row.bank_account:<42} {fmt_amount(row.amount, 'EUR'):>18} @@ {fmt_amount(abs(aed), 'AED')}")
        lines.append(f"  {acct:<42} {fmt_amount(aed, 'AED'):>18}")
        return "\n".join(lines) + "\n"
    if convert and rate is None:
        acct, flag = UNKNOWN, "!"
        lines[0] = lines[0].replace(" * ", " ! ", 1)
    lines.append(f"  {row.bank_account:<42} {fmt_amount(row.amount, row.currency):>18}")
    if row.fx_fee:
        lines.append(f"  {row.bank_account:<42} {fmt_amount(row.fx_fee, row.currency):>18}")
        lines.append(f"  {fee_acct:<42} {fmt_amount(-row.fx_fee, row.currency):>18}")
    lines.append(f"  {acct:<42} {fmt_amount(-row.amount, row.currency):>18}")
    return "\n".join(lines) + "\n"


def entry_for_fx(a: Row, b: Row) -> str:
    """a = afboeking (negatief), b = bijboeking (positief) in de andere valuta."""
    aed, eur = (b.amount, -a.amount) if b.currency == "AED" else (-a.amount, b.amount)
    rate = (aed / eur).quantize(Decimal("0.0001"))
    return "\n".join([
        f'{a.date.isoformat()} * "Wio" "Valutawissel {a.currency} naar {b.currency} (koers {rate})"',
        f'  wio-ref: "{a.ref}"',
        f'  wio-ref-2: "{b.ref}"',
        f'  wio-type: "Currency exchange"',
        f'  bron: "Wio-export"',
        f"  {a.bank_account:<42} {fmt_amount(a.amount, a.currency):>18} @@ {fmt_amount(b.amount, b.currency)}",
        f"  {b.bank_account:<42} {fmt_amount(b.amount, b.currency):>18}",
    ]) + "\n"


def month_starts(d0: date, d1: date) -> list[date]:
    """Eerste dag van elke maand na d0 tot en met d1."""
    out, y, m = [], d0.year, d0.month
    while True:
        m += 1
        if m == 13:
            y, m = y + 1, 1
        d = date(y, m, 1)
        if d > d1:
            return out
        out.append(d)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("csv", type=Path)
    ap.add_argument("--ledger", type=Path, default=Path("xcl/main.beancount"))
    ap.add_argument("--rules", type=Path, default=Path("importers/rules_xcl.yaml"))
    ap.add_argument("--documents", type=Path, default=Path("importers/documenten_xcl.yaml"))
    ap.add_argument("--since", type=date.fromisoformat, help="alleen regels vanaf deze datum (inclusief)")
    ap.add_argument("--until", type=date.fromisoformat, help="alleen regels tot en met deze datum")
    ap.add_argument("--out", type=Path)
    ap.add_argument("--exceptions", type=Path, help="JSON met de uitzonderingenlijst voor de goedkeurings-Sheet")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    rows = read_export(args.csv)
    if args.since:
        rows = [r for r in rows if r.date >= args.since]
    if args.until:
        rows = [r for r in rows if r.date <= args.until]
    seen = existing_refs(args.ledger)
    before = len(rows)
    rows = [r for r in rows if r.ref not in seen]
    skipped = before - len(rows)

    attach_fees(rows)
    fx_pairs = pair_fx(rows)
    fx_refs = {r.ref for p in fx_pairs for r in p}
    rules = load_rules(args.rules)
    prices = load_prices()
    docs = load_documents(args.documents)
    acct_cur = load_account_currencies(args.ledger.parent / "accounts.beancount")

    entries: list[str] = []
    exceptions: list[dict] = []
    series: dict[str, list[tuple[date, Decimal]]] = {}
    first_balance: dict[str, tuple[date, Decimal, str]] = {}
    ncard = 0

    for r in sorted(rows, key=lambda x: (x.date, int(x.ref))):
        if r.iban not in first_balance:
            # saldo vóór de eerste regel van de export: moet aansluiten op wat al in het grootboek staat
            first_balance[r.iban] = (r.date, r.balance - r.amount, r.currency)
        series.setdefault(r.iban, []).append((r.date, r.balance))
        if r.ttype == "_attached" or r.ref in fx_refs:
            continue
        rule = match_rule(r, rules)
        if rule:
            r.account, r.payee = rule["account"], rule.get("payee", "")
            r.flag, r.nl = rule.get("flag", ""), rule.get("nl", "")
        doc = docs.get(r.ref)
        if doc:
            r.docs = [(d["naam"], d["id"]) for d in doc.get("bestanden", [])]
            if doc.get("account"):
                r.account = doc["account"]
            if "flag" in doc:
                r.flag = doc["flag"] or ""
            if doc.get("nl"):
                r.nl = doc["nl"]
            elif doc.get("account") and not doc.get("flag"):
                r.nl = "Bon of factuur in Drive gekoppeld: zakelijk (regel Umar 2-11-2026)"
        entries.append(entry_for(r, prices, acct_cur))
        acct, flag = r.final
        if flag == "!":
            exceptions.append({
                "datum": r.date.isoformat(), "ref": r.ref, "rekening": r.bank_account,
                "bedrag": str(q2(r.amount)), "valuta": r.currency,
                "omschrijving": r.desc, "notitie": r.notes,
                "voorstel": acct, "uitleg": r.nl or "Geen regel gevonden: welke rekening?",
                "document": r.docs[0][0] if r.docs else "",
                "akkoord": "", "opmerking": "",
            })
    for a, b in fx_pairs:
        entries.append(entry_for_fx(a, b))

    # Saldocontroles: begin (sluit aan op het grootboek vóór deze export), elke maandeerste en einde (dag na de laatste regel).
    balances = ["; Saldocontroles: begin, elke maandeerste en einde, tegen het Wio-afschrift\n"]
    for iban, (d, bal, cur) in first_balance.items():
        acct = ACCOUNT_BY_IBAN[iban][0]
        balances.append(f"{d.isoformat()} balance {acct:<32} {fmt_amount(bal, cur)}\n")
    for iban, ser in series.items():
        acct, cur = ACCOUNT_BY_IBAN[iban]
        d_first, d_last = ser[0][0], ser[-1][0]
        marks = month_starts(d_first, date.fromordinal(d_last.toordinal() + 1))
        for mk in marks:
            bal = [b for (dd, b) in ser if dd < mk][-1]
            balances.append(f"{mk.isoformat()} balance {acct:<32} {fmt_amount(bal, cur)}\n")
        end = date.fromordinal(d_last.toordinal() + 1)
        if end not in marks:
            balances.append(f"{end.isoformat()} balance {acct:<32} {fmt_amount(ser[-1][1], cur)}\n")

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
