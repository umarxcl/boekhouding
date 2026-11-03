#!/usr/bin/env python3
"""Status columns J:L for the Goedkeuring Sheet, from the ledger (the ledger is leading).

Input (stdin): one reference per line, in the order of the Sheet rows below the header: a Wio reference, or a key
for rows without one (see MANUAL). Output (stdout): JSON 2D array incl. header, ready for Sheets update_values on
'<tab>'!J1:L<n+1>. Usage: printf '%s\n' 204001669 205413395 | python3 scripts/sheet_status.py
"""
import datetime as dt
import json
import sys
from pathlib import Path

from beancount import loader
from beancount.core import data

ROOT = Path(__file__).resolve().parent.parent
MANUAL = {  # rows in the Sheet that are not bank lines; keep in line with the ledger
    "CAPITAL": ["Equity:ShareCapital (paid 26-1-2026 from the EUR 25,000)", "Afgerond"],
    "INCL": ["Income:FXGain 843.98 (receipt matches the invoice in EUR)", "Afgerond"],
    "INV8": ["Income:Revenue:Advisory:Inclusionair, revenue 31-10-2026", "Afgerond"],
    "EKM": ["Expenses:Bank:Charges 394.02 (EUR 94.50 written off)", "Afgerond"],
}


def main():
    entries, _, _ = loader.load_file(str(ROOT / "xcl" / "main.beancount"))
    byref = {e.meta["wio-ref"]: e for e in entries if isinstance(e, data.Transaction) and "wio-ref" in e.meta}
    byinv = {e.meta.get("invoice"): e for e in entries if isinstance(e, data.Transaction) and e.meta.get("invoice")}
    today = dt.date.today().isoformat()
    rows = [["Geboekt (grootboek, leidend)", "Status", "Bijgewerkt"]]
    for ref in (l.strip() for l in sys.stdin if l.strip()):
        if ref in MANUAL:
            rows.append(MANUAL[ref] + [today])
            continue
        e = byref.get(ref) or byinv.get(ref)
        if e is None:
            rows.append(["NOT FOUND IN LEDGER", "Open: reference not found", today])
            continue
        ps = [p for p in e.postings if not p.account.startswith("Assets:Bank")]
        booked = ps[0].account if len(ps) == 1 else " | ".join(f"{p.account} {abs(p.units.number):,.2f}" for p in ps)
        status = "Open: " + str(e.meta.get("open", "")) if e.flag == "!" else "Afgerond"
        rows.append([booked, status, today])
    print(json.dumps(rows, ensure_ascii=False))


if __name__ == "__main__":
    main()
