#!/usr/bin/env python3
"""Maakt docs/rekeningschema.md uit de metadata van de rekeningen (nl, btw, ifrs), zodat de uitleg
in gewone taal nooit uit de pas loopt met het grootboek. Gebruik: python3 scripts/rekeningschema_md.py"""
from pathlib import Path
from beancount import loader
from beancount.core import data

ROOT = Path(__file__).resolve().parent.parent
LEDGERS = [("XCL MANAGEMENT CONSULTANCIES - FZCO", ROOT / "xcl/main.beancount"),
           ("MZML HOLDING LIMITED", ROOT / "mzml_ltd/main.beancount")]
BTW = {"nvt": "geen btw-gevolg", "0-export": "omzet 0% (export van diensten)",
       "5-voorbelasting": "5% voorbelasting aftrekbaar met TRN-factuur", "geen-aftrek": "geen voorbelasting"}

out = ["# Rekeningschema in gewone taal\n",
       "Automatisch gemaakt uit het grootboek (`scripts/rekeningschema_md.py`). Wijzig de uitleg in `accounts.beancount`, niet hier.\n"]
for title, path in LEDGERS:
    entries, errors, _ = loader.load_file(str(path))
    opens = [e for e in entries if isinstance(e, data.Open)]
    out.append(f"\n## {title}\n")
    out.append("| Rekening | Wat het is | Btw | Jaarrekening |\n|---|---|---|---|")
    for e in sorted(opens, key=lambda x: x.account):
        m = e.meta
        out.append(f"| `{e.account}` | {m.get('nl', '')} | {BTW.get(m.get('btw', ''), m.get('btw', ''))} | {m.get('ifrs', '')} |")
(ROOT / "docs/rekeningschema.md").write_text("\n".join(out) + "\n", encoding="utf-8")
print("docs/rekeningschema.md bijgewerkt")
