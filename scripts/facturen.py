#!/usr/bin/env python3
"""Writes xcl/2026/facturen.beancount: the XCL sales invoices INV-0001 to INV-0012 (Fiskl export) on their invoice dates.

Usage:
    python3 scripts/facturen.py            write the file; refuses if the existing file differs from what would be generated
    python3 scripts/facturen.py --check    only compare; exit code 1 if the file differs (shows the diff)
    python3 scripts/facturen.py --force    overwrite even if the existing file differs (hand edits are lost)

Source: Fiskl export (Sheet '2026-10-18-invoices-detail-01-Jan-26-to-18-Oct-26' and the CSV of 2-11-2026 in Drive,
Boekhouding/XCL/Verkoop 2026). EUR invoices: receivable in EUR at the CBUAE rate of the invoice date (last publication day
if that is a weekend day), revenue in AED. Receipts are in the monthly files (Wio import), on the same receivable account.
INV-0008 (Inclusionair, AED 89,120) is an advance invoice: invoice to Liabilities:DeferredRevenue, revenue on 31-10-2026.
Rates come from shared/prices.beancount; a missing rate leaves the invoice on '!' with a provisional rate.

This script owns only the invoice entries. Corrections are made here (in the data below) and the file is regenerated;
one-off manual journal entries (write-offs, reclassifications) belong in xcl/2026/adjustments.beancount, which this
script never touches. The overwrite guard protects hand edits made to facturen.beancount by mistake.
"""
from __future__ import annotations

import argparse
import difflib
import re
import sys
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "xcl/2026/facturen.beancount"

CAR, ZVW = "car contribution", "ZVW contribution"
# (number, invoice date, customer, receivable, revenue account, currency, amount, rate date, description, pdf name, drive-id)
INVOICES = [
    ("INV-0001", "2026-01-21", "Ekmekci Group B.V.", "Ekmekci", "ManagementFees:Ekmekci", "EUR", "7766.00", "2026-01-21", f"Management fee January 2026 (6,666) + {ZVW} (300) + {CAR} (800)", "INV-0001.pdf", "1_0Q03MTXoktexndqjF8upWHeJZ6uqrt-"),
    ("INV-0002", "2026-01-24", "MDI Consultants B.V.", "MDI", "ManagementFees:MDI", "EUR", "4500.00", "2026-01-23", "Management fee Q1 2026", None, None),
    ("INV-0003", "2026-02-17", "Ekmekci Group B.V.", "Ekmekci", "ManagementFees:Ekmekci", "EUR", "7716.00", "2026-02-17", f"Management fee February 2026 (6,666) + {CAR} (800) + {ZVW} (250)", "INV-0003.pdf", "1tk2Mjwb3HLQrfW665DNj0lQy9E3k0CBW"),
    ("INV-0004", "2026-03-17", "Ekmekci Group B.V.", "Ekmekci", "ManagementFees:Ekmekci", "EUR", "7716.00", "2026-03-17", f"Management fee March 2026 (6,666) + {CAR} (800) + {ZVW} (250)", "INV-0004.pdf", "1VLLpoaUHG3SC2eh5qMAm0yAwDa6RpPl1"),
    ("INV-0005", "2026-04-17", "Ekmekci Group B.V.", "Ekmekci", "ManagementFees:Ekmekci", "EUR", "7716.00", "2026-04-17", f"Management fee April 2026 (6,666) + {CAR} (800) + {ZVW} (250)", "INV-0005.pdf", "1Bqhu47oKCZ9ar0Pbgo9ozhIA7_PZcae1"),
    ("INV-0006", "2026-05-17", "Ekmekci Group B.V.", "Ekmekci", "ManagementFees:Ekmekci", "EUR", "7716.00", "2026-05-15", f"Management fee May 2026 (6,666) + {CAR} (800) + {ZVW} (250)", "INV-0006.pdf", "1_eWCQnypIiuMBbj1FggWHUE-Uqe7KmxP"),
    ("INV-0007", "2026-06-19", "Ekmekci Group B.V.", "Ekmekci", "ManagementFees:Ekmekci", "EUR", "7716.00", "2026-06-19", f"Management fee June 2026 (6,666) + {CAR} (800) + {ZVW} (250)", "INV-0007.pdf", "1yafw7NJ0p9uBQ6QCEGj3OPRwxrYH0Ozw"),
    ("INV-0009", "2026-07-17", "Ekmekci Group B.V.", "Ekmekci", "ManagementFees:Ekmekci", "EUR", "7716.00", "2026-07-17", f"Management fee July 2026 (6,666) + {CAR} (800) + {ZVW} (250)", "INV-0009.pdf", "1xvg9AfD3yn8GzmqjzsgPUFMGPhv7d8N_"),
    ("INV-0010", "2026-08-17", "Ekmekci Group B.V.", "Ekmekci", "ManagementFees:Ekmekci", "EUR", "7716.00", "2026-08-17", f"Management fee August 2026 (6,666) + {CAR} (800) + {ZVW} (250)", "INV-0010.pdf", "1GTqXv8-RRvMWha5liGQR46w-7Jm-tGUe"),
    ("INV-0011", "2026-09-17", "Ekmekci Group B.V.", "Ekmekci", "ManagementFees:Ekmekci", "EUR", "7716.00", "2026-09-17", f"Management fee (Fiskl description 'Aug 2026', invoice of 17-9) (6,666) + {CAR} (800) + {ZVW} (250)", "INV-0011.pdf", "1u3bJmvXy_rpKKJAY04B8V1WXS38kxysK"),
    # Description corrected after owner review 3-11-2026 (Fiskl said 'Managementfee feb 2026': a typo).
    ("INV-0012", "2026-10-17", "Ekmekci Group B.V.", "Ekmekci", "ManagementFees:Ekmekci", "EUR", "7716.00", None, f"Management fee October 2026 (6,916) + {CAR} (800), invoice date 17-10", "INV-0012.pdf", "1yFFqHPItxSHUQauS94BJvMgSnrOi4Py_"),
]
INV0008 = dict(nr="INV-0008", date="2026-06-29", customer="Inclusionair", amount=Decimal("89120.00"),
               pdf="INV-0008.pdf", drive="1Jq9HuJLTda91Oxp5sIAHqgERFzToR19p")
# INV-0002.pdf is not in Drive Verkoop 2026 (checked 2-11-2026): no document metadata.
FALLBACK_RATE_DATE = "2026-09-30"  # last known CBUAE rate for INV-0012 (October table not yet published)

# Owner review results (approval list 3-11-2026), written as metadata after the generated metadata.
REVIEW = {
    "INV-0012": ['  approved: "2026-11-03"', '  owner-answer: "niet feb, typfout; managementfee Ekmekci"',
                 '  open: "Description corrected to management fee October 2026; CBUAE rate October still to come"'],
    "INV-0008-revenue": ['  approved: "2026-11-03"', '  owner-answer: "tot eind oktober gerund en afgerond"',
                         '  note: "Service completed end of October 2026; revenue on 31-10-2026"'],
}
INV0008_REVENUE_FLAG = "*"  # delivery date confirmed by Umar 3-11-2026


def q2(x: Decimal) -> Decimal:
    return x.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def prices() -> dict[str, Decimal]:
    out = {}
    for line in (ROOT / "shared/prices.beancount").read_text(encoding="utf-8").splitlines():
        m = re.match(r"^(\d{4}-\d{2}-\d{2})\s+price\s+EUR\s+([\d.]+)\s+AED", line)
        if m:
            out[m.group(1)] = Decimal(m.group(2))
    return out


def fmt(x: Decimal, cur: str) -> str:
    return f"{q2(x):,.2f} {cur}"


def generate() -> tuple[str, int]:
    px = prices()
    out = ["; XCL sales invoices 2026 (Fiskl, INV-0001 to INV-0012), booked on the invoice date.",
           "; Generated by scripts/facturen.py: do not edit by hand (change the script and regenerate).",
           "; Receipts are in the monthly files (Wio import) on the same receivable account; manual journal entries in adjustments.beancount.",
           "; All 2026 revenue is zero-rated export (VAT reverse-charged to the customer, decision 21-10-2026).", ""]
    entries: list[tuple[str, str]] = []
    for nr, inv_date, customer, recv, rev, cur, amount_s, rate_date, descr, pdf, did in INVOICES:
        amount = Decimal(amount_s)
        flag, extra = "*", []
        if rate_date is None:
            rate_date, flag = FALLBACK_RATE_DATE, "!"
            rate = px[rate_date]
            extra.append(f'  note: "Provisional rate: the CBUAE October 2026 table is not yet published; rate of {rate_date} used, to be corrected once the rate of 16-10-2026 (last publication day before 17-10) is known. Description corrected: Fiskl said \'feb 2026\', a typo by Umar; this is the management fee for October 2026."')
            extra.append(f'  rate: "PROVISIONAL CBUAE {rate} AED per EUR (rate of {rate_date})"')
        else:
            rate = px[rate_date]
            extra.append(f'  rate: "CBUAE {rate} AED per EUR (rate of {rate_date})"')
        aed = q2(amount * rate)
        lines = [f'{inv_date} {flag} "{customer}" "Invoice {nr}: {descr}"', f'  invoice: "{nr}"']
        if pdf:
            lines += [f'  document: "{pdf}"', f'  drive-id: "{did}"']
        else:
            lines += ['  document-note: "INV-0002.pdf is missing in Drive Verkoop 2026; source is the Fiskl export"']
        lines += extra + REVIEW.get(nr, [])
        lines += [f"  {'Assets:Receivables:Trade:' + recv:<42} {fmt(amount, cur):>18} @@ {fmt(aed, 'AED')}",
                  f"  {'Income:Revenue:' + rev:<42} {fmt(-aed, 'AED'):>18}"]
        entries.append((inv_date, "\n".join(lines)))
    i = INV0008
    entries.append((i["date"], "\n".join([
        f'{i["date"]} * "{i["customer"]}" "Invoice {i["nr"]}: Development and digital delivery Leergang (advance payment, services delivered end of October 2026)"',
        f'  invoice: "{i["nr"]}"', f'  document: "{i["pdf"]}"', f'  drive-id: "{i["drive"]}"',
        '  note: "Advance invoice: revenue is recognised on 31-10-2026 (services delivered end of October 2026, per Umar); Fiskl states 24-5-2026 as delivery date"',
        f"  {'Assets:Receivables:Trade:Inclusionair':<42} {fmt(i['amount'], 'AED'):>18}",
        f"  {'Liabilities:DeferredRevenue':<42} {fmt(-i['amount'], 'AED'):>18}"])))
    entries.append(("2026-10-31", "\n".join([
        f'2026-10-31 {INV0008_REVENUE_FLAG} "{i["customer"]}" "Revenue INV-0008 recognised: Leergang services delivered end of October 2026"',
        f'  invoice: "{i["nr"]}"', f'  document: "{i["pdf"]}"', f'  drive-id: "{i["drive"]}"',
        '  initial-note: "Delivery date confirmed by Umar (3-11-2026): end of October 2026; Fiskl stated 24-5-2026 as the date of sale."',
        *REVIEW["INV-0008-revenue"],
        f"  {'Liabilities:DeferredRevenue':<42} {fmt(i['amount'], 'AED'):>18}",
        f"  {'Income:Revenue:Advisory:Inclusionair':<42} {fmt(-i['amount'], 'AED'):>18}"])))
    entries.sort(key=lambda t: t[0])
    out.append("\n\n".join(e for _, e in entries))
    return "\n".join(out) + "\n", len(entries)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="compare only; exit 1 if the file differs")
    ap.add_argument("--force", action="store_true", help="overwrite even if the existing file differs")
    args = ap.parse_args()
    text, n = generate()
    current = OUT.read_text(encoding="utf-8") if OUT.exists() else None
    rel = OUT.relative_to(ROOT)
    if current == text:
        print(f"{rel}: up to date ({n} entries)")
        return
    if current is not None and (args.check or not args.force):
        sys.stdout.writelines(difflib.unified_diff(current.splitlines(True), text.splitlines(True),
                                                   f"{rel} (current)", f"{rel} (generated)"))
        if args.check:
            sys.exit(1)
        sys.exit(f"\n{rel} differs from what the script generates (hand edits?). Move manual corrections to "
                 f"xcl/2026/adjustments.beancount or into this script, then rerun; --force overwrites.")
    if args.check:
        sys.exit(f"{rel} does not exist")
    OUT.write_text(text, encoding="utf-8")
    print(f"{rel}: written ({n} entries)")


if __name__ == "__main__":
    main()
