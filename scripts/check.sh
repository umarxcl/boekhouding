#!/usr/bin/env bash
# Checks both ledgers and counts open items (flag "!") and postings on the suspense account.
set -euo pipefail
cd "$(dirname "$0")/.."
for L in xcl/main.beancount mzml_ltd/main.beancount; do
  echo "== $L"
  bean-check "$L"
  open=$(grep -rhE '^[0-9]{4}-[0-9]{2}-[0-9]{2} !' "$(dirname "$L")" | wc -l)
  echo "   open items (flag !): $open"
done
echo "== Invoices file matches scripts/facturen.py"
python3 scripts/facturen.py --check
echo "== Month-end entries match scripts/month_end.py"
python3 scripts/month_end.py --through 2026-10 --check
echo "== Expenses:Suspense (must be nil at month-end close)"
bean-query xcl/main.beancount "select sum(position) where account = 'Expenses:Suspense'" | tail -n +3
