#!/usr/bin/env python3
"""Builds docs/chart_of_accounts.md from the account metadata (note, vat, ct, related-party, ifrs, rgs), so the
plain-language explanation never drifts from the ledger. Usage: python3 scripts/chart_of_accounts_md.py"""
from pathlib import Path
from beancount import loader
from beancount.core import data

ROOT = Path(__file__).resolve().parent.parent
LEDGERS = [("XCL MANAGEMENT CONSULTANCIES - FZCO", ROOT / "xcl/main.beancount"),
           ("MZML HOLDING LIMITED", ROOT / "mzml_ltd/main.beancount")]
VAT = {"zero-rated-export": "zero-rated export (box 4)", "standard-5": "standard-rated 5% UAE (box 1)",
       "input-5": "5% input VAT with tax invoice showing TRN (box 9)",
       "reverse-charge": "reverse charge: self-assess and recover (boxes 3 and 10)",
       "blocked": "input VAT not recoverable (art. 53)", "exempt": "exempt purchase",
       "out-of-scope": "government fee, outside the scope of VAT", "zero-rated-purchase": "zero-rated purchase",
       "foreign": "consumed outside the UAE", "n/a": "no VAT consequence"}

out = ["# Chart of accounts in plain language\n",
       "Generated from the ledger (`scripts/chart_of_accounts_md.py`). Change the explanations in `accounts.beancount`, not here. "
       "Old Dutch account names: `docs/account_mapping_nl_en.md`.\n"]
for title, path in LEDGERS:
    entries, errors, _ = loader.load_file(str(path))
    if errors:
        raise SystemExit(f"{path}: {len(errors)} errors; run bean-check first")
    opens = [e for e in entries if isinstance(e, data.Open)]
    out.append(f"\n## {title}\n")
    out.append("| Account | What it is | VAT | CT | Related party | Financial statements | RGS |\n|---|---|---|---|---|---|---|")
    for e in sorted(opens, key=lambda x: x.account):
        m = e.meta
        out.append(f"| `{e.account}` | {m.get('note', '')} | {VAT.get(m.get('vat', ''), m.get('vat', ''))} | {m.get('ct', '')} | "
                   f"{m.get('related-party', '')} | {m.get('ifrs', '')} | {m.get('rgs', '')} |")
(ROOT / "docs/chart_of_accounts.md").write_text("\n".join(out) + "\n", encoding="utf-8")
print("docs/chart_of_accounts.md updated")
