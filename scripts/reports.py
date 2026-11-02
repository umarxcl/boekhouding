#!/usr/bin/env python3
"""Month-end reports for XCL from the ledger: trial balance, income statement, balance sheet,
director position (pro forma) and open items. Writes CSV files plus summary.md to reports/xcl/<YYYY-MM>/.

Usage: python3 scripts/reports.py --month 2026-10
EUR items: shown in EUR; the AED value uses the last published CBUAE rate on or before the month end and is
labelled provisional when that rate is older than the month end (monetary items must be revalued at the
month-end rate, art. 69 VAT law logic; no estimated rates).
"""
import argparse
import calendar
import csv
import datetime as dt
from collections import defaultdict
from decimal import Decimal
from pathlib import Path

from beancount import loader
from beancount.core import data

ROOT = Path(__file__).resolve().parent.parent
LEDGER = ROOT / "xcl" / "main.beancount"
D = Decimal


def load(month):
    y, m = map(int, month.split("-"))
    end = dt.date(y, m, calendar.monthrange(y, m)[1])
    entries, errors, _ = loader.load_file(str(LEDGER))
    if errors:
        raise SystemExit(f"Ledger has errors: {errors[:3]}")
    bal = defaultdict(lambda: defaultdict(D))
    flagged = []
    prices = []
    for e in entries:
        if isinstance(e, data.Price) and e.currency == "EUR" and e.amount.currency == "AED":
            prices.append((e.date, e.amount.number))
        if not isinstance(e, data.Transaction) or e.date > end:
            continue
        if e.flag == "!":
            flagged.append(e)
        for p in e.postings:
            bal[p.account][p.units.currency] += p.units.number
    prices = sorted(p for p in prices if p[0] <= end)
    rate_date, rate = prices[-1]
    return end, bal, flagged, rate_date, rate


def write_csv(path, header, rows):
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--month", required=True)
    a = ap.parse_args()
    end, bal, flagged, rate_date, rate = load(a.month)
    out = ROOT / "reports" / "xcl" / a.month
    out.mkdir(parents=True, exist_ok=True)
    provisional = rate_date != end
    f2 = lambda x: f"{x:.2f}"

    def aed_equiv(acct):
        return bal[acct].get("AED", D(0)) + bal[acct].get("EUR", D(0)) * rate

    accounts = sorted(bal)
    write_csv(out / "trial_balance.csv", ["account", "AED", "EUR"],
              [[x, f2(bal[x].get("AED", D(0))), f2(bal[x].get("EUR", D(0)))] for x in accounts
               if any(v != 0 for v in bal[x].values())])

    totals = {"Assets": D(0), "Liabilities": D(0), "Equity": D(0)}
    for x in accounts:
        root = x.split(":")[0]
        if root in totals and x != "Equity:FXTranslation":
            totals[root] += (D(1) if root == "Assets" else D(-1)) * aed_equiv(x)
    inc = [(x, -aed_equiv(x)) for x in accounts if x.startswith("Income:")]
    exp = [(x, aed_equiv(x)) for x in accounts if x.startswith("Expenses:")]
    rev_total = sum(v for _, v in inc)
    exp_total = sum(v for _, v in exp)
    result = rev_total - exp_total
    fx = sum(v.get("AED", D(0)) for v in bal.values()) + sum(v.get("EUR", D(0)) for v in bal.values()) * rate
    # independent of the statements: all AED units plus all EUR units at the closing rate (every transaction balances in weights)
    fx -= bal["Equity:FXTranslation"].get("AED", D(0))
    # Equity:FXTranslation holds the offset of the FX result booked by scripts/month_end.py; it is netted with the
    # translation of the EUR items and therefore not shown as equity. What remains is the FX difference not yet booked.
    write_csv(out / "income_statement.csv", ["account", "AED"],
              [[x, f2(v)] for x, v in inc if v != 0] + [["TOTAL INCOME", f2(rev_total)]]
              + [[x, f2(v)] for x, v in exp if v != 0] + [["TOTAL EXPENSES", f2(exp_total)], ["RESULT AS BOOKED", f2(result)],
               ["UNBOOKED FX DIFFERENCE ON EUR ITEMS (see balance_sheet.csv)", f2(fx)], ["RESULT INCL. UNBOOKED FX", f2(result + fx)]])

    rows = []
    totals = {"Assets": D(0), "Liabilities": D(0), "Equity": D(0)}
    for x in accounts:
        root = x.split(":")[0]
        if root not in totals or x == "Equity:FXTranslation":
            continue
        aed, eur = bal[x].get("AED", D(0)), bal[x].get("EUR", D(0))
        if aed == 0 and eur == 0:
            continue
        val = aed + eur * rate
        sign = D(1) if root == "Assets" else D(-1)
        totals[root] += sign * val
        rows.append([x, f2(sign * aed), f2(sign * eur), f2(sign * val)])
    rows += [["TOTAL ASSETS", "", "", f2(totals["Assets"])], ["TOTAL LIABILITIES", "", "", f2(totals["Liabilities"])],
             ["TOTAL EQUITY (booked)", "", "", f2(totals["Equity"])], ["RESULT YEAR TO DATE", "", "", f2(result)],
             ["UNBOOKED FX DIFFERENCE ON EUR ITEMS (realised + unrealised; negative = loss)", "", "", f2(fx)],
             ["CHECK after FX difference (must be 0.00)", "", "", f2(totals["Assets"] - totals["Liabilities"] - totals["Equity"] - result - fx)]]
    write_csv(out / "balance_sheet.csv", ["account", "AED", "EUR (native)", "AED value (EUR at rate %s of %s)" % (rate, rate_date)], rows)

    recv = aed_equiv("Assets:Receivables:Director:Umar")
    pay = -aed_equiv("Liabilities:Employees:SalaryPayable-Umar")
    loan_aed = -aed_equiv("Liabilities:ShareholderLoan:Umar-AED")
    loan_eur = -bal["Liabilities:ShareholderLoan:Umar-EUR"].get("EUR", D(0))
    loan_eur_aed = loan_eur * rate
    net_set_off = pay - recv
    write_csv(out / "director_position.csv", ["item", "AED", "note"], [
        ["Director current account (receivable from Umar)", f2(recv), "private spending and payments on his behalf, incl. 30% car"],
        ["Salary payable to Umar (accrued minus paid)", f2(-pay), "negative = XCL owes Umar"],
        ["Net after set-off (positive = Umar owes XCL)", f2(-net_set_off), "PRO FORMA: set-off is booked only after the addendum is signed"],
        ["Shareholder loan AED", f2(-loan_aed), "interest-free"],
        ["Shareholder loan EUR %s" % f2(loan_eur), f2(-loan_eur_aed), "AED value indicative at rate %s of %s" % (rate, rate_date)],
        ["Total position XCL vs Umar (positive = Umar owes XCL)", f2(-net_set_off - loan_aed - loan_eur_aed), "indicative"],
    ])

    items = []
    for e in sorted(flagged, key=lambda t: t.date):
        amt = next((p.units for p in e.postings if p.account.startswith("Assets:Bank")), e.postings[0].units)
        items.append([e.date, e.meta.get("wio-ref", e.meta.get("invoice", "")), f2(amt.number), amt.currency, e.narration, e.meta.get("open", "")])
    write_csv(out / "open_items.csv", ["date", "reference", "amount", "currency", "narration", "open reason"], items)

    summary = f"""# XCL month-end report {a.month}
Generated by scripts/reports.py on {dt.date.today()} from the ledger up to {end}.

| Item | AED |
|---|---|
| Income | {rev_total:,.2f} |
| Expenses | {exp_total:,.2f} |
| Result year to date, as booked | {result:,.2f} |
| Unbooked FX difference on EUR items (loss = negative) | {fx:,.2f} |
| Result incl. unbooked FX | {result + fx:,.2f} |
| Total assets | {totals['Assets']:,.2f} |
| Total liabilities | {totals['Liabilities']:,.2f} |
| Equity (booked) | {totals['Equity']:,.2f} |

EUR items valued at CBUAE rate {rate} of {rate_date}{' (PROVISIONAL: the rate of ' + str(end) + ' is not yet published)' if provisional else ''}.
Open items (flag !): {len(items)}; see open_items.csv. Director position: see director_position.csv.
"""
    (out / "summary.md").write_text(summary)
    print(summary)


if __name__ == "__main__":
    main()
