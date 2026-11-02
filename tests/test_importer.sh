#!/usr/bin/env bash
# Importer test: imports the sample Wio export against the XCL chart of accounts and checks that the result is a valid
# ledger. Usage: bash tests/test_importer.sh   (writes to tests/tmp/, which is git-ignored)
set -euo pipefail
cd "$(dirname "$0")/.."
R="$(pwd)"
T=tests/tmp
rm -rf "$T" && mkdir -p "$T"
# The importer reads accounts.beancount next to --ledger and skips refs already in <ledger dir>/2026 (none here).
ln -s "$R/xcl/accounts.beancount" "$T/accounts.beancount"
cat > "$T/main.beancount" <<EOF
option "operating_currency" "AED"
option "operating_currency" "EUR"
plugin "beancount.plugins.check_commodity"
plugin "beancount.plugins.leafonly"
include "$R/shared/commodities.beancount"
include "$R/shared/prices.beancount"
include "accounts.beancount"
; test opening balances before the export (pad fills the difference from an equity account)
2026-09-28 pad Assets:Bank:Wio-AED Equity:OpeningBalance
2025-12-15 open Equity:TestPad-EUR EUR
2026-09-28 pad Assets:Bank:Wio-EUR Equity:TestPad-EUR
include "import.beancount"
EOF
python3 importers/wio.py tests/fixtures/wio_statement_2026-09-29_2026-10-29.csv --ledger "$T/main.beancount" \
  --out "$T/import.beancount" --exceptions "$T/exc.json"
bean-check "$T/main.beancount"
head -2 "$T/import.beancount" | grep -q "; 52 entries, 3 currency exchanges, 0 lines skipped" \
  || { echo "FAIL: unexpected entry count"; head -2 "$T/import.beancount"; exit 1; }
python3 -c "import json,sys; json.load(open(sys.argv[1]))" "$T/exc.json"
echo "importer test OK"
