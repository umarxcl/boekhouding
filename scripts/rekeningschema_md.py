#!/usr/bin/env python3
"""Maakt docs/rekeningschema.md uit de metadata van de rekeningen (nl, btw, ifrs), zodat de uitleg
in gewone taal nooit uit de pas loopt met het grootboek. Gebruik: python3 scripts/rekeningschema_md.py"""
from pathlib import Path
from beancount import loader
from beancount.core import data

ROOT = Path(__file__).resolve().parent.parent
LEDGERS = [("XCL MANAGEMENT CONSULTANCIES - FZCO", ROOT / "xcl/main.beancount"),
           ("MZML HOLDING LIMITED", ROOT / "mzml_ltd/main.beancount")]
BTW = {"0-export": "omzet 0%, export (vak 4)", "5-binnenland": "omzet 5% UAE (vak 1)",
       "5-voorbelasting": "5% voorbelasting met TRN-factuur (vak 9)", "verlegd": "verlegd: zelf aangeven en aftrekken (vak 3 en 10)",
       "geblokkeerd": "btw niet aftrekbaar (art. 53)", "vrijgesteld": "vrijgestelde inkoop", "buiten-reikwijdte": "heffing zonder btw",
       "0-inkoop": "nultarief-inkoop", "buitenland": "verbruikt buiten de UAE", "nvt": "geen btw-gevolg"}

out = ["# Rekeningschema in gewone taal\n",
       "Automatisch gemaakt uit het grootboek (`scripts/rekeningschema_md.py`). Wijzig de uitleg in `accounts.beancount`, niet hier.\n"]
for title, path in LEDGERS:
    entries, errors, _ = loader.load_file(str(path))
    opens = [e for e in entries if isinstance(e, data.Open)]
    out.append(f"\n## {title}\n")
    out.append("| Rekening | Wat het is | Btw | CT | Verbonden | Jaarrekening | RGS |\n|---|---|---|---|---|---|---|")
    for e in sorted(opens, key=lambda x: x.account):
        m = e.meta
        out.append(f"| `{e.account}` | {m.get('nl', '')} | {BTW.get(m.get('btw', ''), m.get('btw', ''))} | {m.get('ct', '')} | {m.get('verbonden', '')} | {m.get('ifrs', '')} | {m.get('rgs', '')} |")
(ROOT / "docs/rekeningschema.md").write_text("\n".join(out) + "\n", encoding="utf-8")
print("docs/rekeningschema.md bijgewerkt")
