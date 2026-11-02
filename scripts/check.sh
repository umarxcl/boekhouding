#!/usr/bin/env bash
# Controleert beide grootboeken en telt open posten (vlag "!") en onbekende boekingen.
set -euo pipefail
cd "$(dirname "$0")/.."
for L in xcl/main.beancount mzml_ltd/main.beancount; do
  echo "== $L"
  bean-check "$L"
  open=$(grep -rhE '^[0-9]{4}-[0-9]{2}-[0-9]{2} !' "$(dirname "$L")" | wc -l)
  echo "   open posten (vlag !): $open"
done
echo "== Expenses:Onbekend"
bean-query xcl/main.beancount "select sum(position) where account = 'Expenses:Onbekend'" | tail -n +3
