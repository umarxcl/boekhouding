# Runbook

Purpose: someone without prior knowledge (Umar himself, a replacement, or an accountant) can use this to understand, run and recover the system. Status: 3 November 2026, phase 1 (no own server; runs as scheduled Claude tasks). The bookkeeping is in English since 3-11-2026; old Dutch account names: `docs/account_mapping_nl_en.md`.

## 1. Components

| Component | Where | Owner |
|---|---|---|
| Ledger | GitHub `umarxcl/boekhouding` (private) | Umar |
| Private ledger | GitHub `umarxcl/boekhouding-prive` (private, stricter) | Umar |
| Attachments and bank exports | Google Drive, folder Boekhouding (owner mail@umarmirza.nl) | Umar |
| Approval and reports | Google Sheet "Boekhouding – Goedkeuring" and the existing Sheet "Cashflow" | Umar |
| Execution | Claude (scheduled tasks in the project Boekhouding NL & UAE) | Claude |

## 2. Monthly cycle

1. Twice a month Umar puts the Wio export (CSV, both accounts in one file) in Drive, folder `Boekhouding/Bankexports/Wio/`. File name as Wio provides it; the importer reads the dates from the content.
2. The run fetches the ledger, imports new exports (`importers/wio.py`), skips known reference numbers, categorises with `importers/rules_xcl.yaml`, links attachments from Drive (`importers/documenten_xcl.yaml`) and writes the entries to `xcl/2026/MM.beancount`.
3. Everything uncertain gets flag `!` and goes in the Sheet "Goedkeuring", tab of that month, with a one-line explanation (the importer's exceptions JSON).
4. Umar enters "akkoord" (approved) or a comment per line. A comment can be another account ("private"), a receipt ("it is in Drive under ..."), or a question.
5. The run processes the answers (metadata `approved`, `owner-answer` verbatim, `note`), removes the flags, adds new rules to `rules_xcl.yaml` when Umar says so, books salary, housing, provisions and exchange differences (in `xcl/2026/adjustments.beancount`), checks the bank balances against the statement, and closes the month (git tag).
6. Reports (balance sheet, P&L, cash flow, director's current account, VAT overview) go to the Sheet; the Cashflow Sheet gets the actuals; Umar gets one message.

## 3. Checks on every run

- `bash scripts/check.sh`: `bean-check` on both ledgers (balanced entries, existing accounts, balance assertions), count of open items (`!`), `facturen.beancount` matches `scripts/facturen.py`, balance of `Expenses:Suspense`.
- `bash tests/test_importer.sh` after any change to the importer, the rules or the chart of accounts.
- Opening and closing balance of each export against the ledger (the importer writes `balance` assertions).
- No `!` left in a month that is being closed; `Expenses:Suspense` must be nil.
- Director's current account (`Assets:Receivables:Director:Umar`) and salary payable (`Liabilities:Employees:SalaryPayable-Umar`): monthly set-off booked.
- Exchange rate: a deviation of more than 2% from the previous month goes on the list.
- Review agent (separate, did not make the entries): VAT treatment per account, period cut-off, prepayments, provisions.

## 4. Running by hand (if the scheduled task does not run)

On any computer with Python 3.11 or later:

```
git clone https://github.com/umarxcl/boekhouding
cd boekhouding
pip install -r requirements.txt
python3 importers/wio.py <export.csv> --out <new-entries>.beancount --exceptions exceptions.json
bean-check xcl/main.beancount
```

Then append the new entries to the month file (or use `scripts/split_maanden.py` for months that have no file yet; it refuses to overwrite existing month files without `--force`, because they contain review edits).

Or ask Claude in the project: "Run the monthly run for XCL with the export in Drive."

## 5. Recovery

- Ledger lost: `git clone` from GitHub (full history).
- GitHub lost: the latest monthly reports are in Sheets; the entries can be reconstructed from the Wio exports in Drive with the importer (review edits from the history in Sheets).
- Drive lost: bank exports can be downloaded again from Wio (7 years); attachments from Gmail, Dropbox and supplier portals. Hence: annual backup of the Drive folder Boekhouding to a second location (task in January).
- Claude not available: any accountant can read the ledger via `bean-query ... "select date, account, position, narration"` (CSV) or via Fava (`fava xcl/main.beancount`, web interface).

## 6. Retention periods

UAE: 7 years (Corporate Tax law; VAT 5 years, 15 for real estate). Netherlands: 7 years. Closed years remain in the repository and in Drive; nothing is deleted.

## 7. Access

- GitHub: Umar (owner), Claude via the GitHub connection in claude.ai.
- Drive and Sheets: Umar (owner), Claude via the Google connection.
- No bank login details in the system; exports come manually from the Wio app.

## 8. XCL catch-up January to October 2026 (2-11-2026)

- Bank export: `data/wio_2025-11-02_2026-11-02.csv` (listed in `.gitignore`; the original is in Drive, not in git).
- Import: `python3 importers/wio.py data/<export>.csv --since 2026-01-01 --until 2026-10-31 --documents importers/documenten_xcl.yaml --out <temp>.beancount --exceptions <temp>.json`, then `python3 scripts/split_maanden.py <temp>.beancount` to write `xcl/2026/MM.beancount` per month (balance assertions of the first day of the following month go into the last month). The month files now exist and contain review edits; a rerun needs `--force` and would lose those edits.
- `importers/documenten_xcl.yaml` links bank lines (Wio ref) to receipts in Drive (`document` and `drive-id`). Receipt available = business; without a receipt = private via `Assets:Receivables:Director:Umar` with flag `!`.
- Sales invoices: `python3 scripts/facturen.py` writes `xcl/2026/facturen.beancount` (rates from `shared/prices.beancount`). The script owns that file: corrections to an invoice are made in the script's data, one-off journal entries (write-offs, reclassifications) go in `xcl/2026/adjustments.beancount`. It refuses to overwrite a file that differs from its output (`--check` compares only, `--force` overwrites).
- Approval: the open items with flag `!` are in the Google Sheet 'Boekhouding – Goedkeuring' (tabs per quarter).

## 9. Chart of accounts document

`python3 scripts/chart_of_accounts_md.py` regenerates `docs/chart_of_accounts.md` from the metadata in `accounts.beancount` (note, vat, ct, related-party, ifrs, rgs). Change explanations in `accounts.beancount`, then regenerate.

## 9. Month-end close (first run: October 2026, prepared on 3-11-2026)

1. `python3 scripts/month_end.py --through YYYY-MM` writes `xcl/2026/month_end.beancount` (salary accrual, end-of-service accrual, private share of car costs) from `xcl/parameters.yaml`. Change a parameter only together with an entry in `docs/besluitenlog.md`.
2. `bash scripts/check.sh` (ledgers, open flags, invoices file, month-end file, suspense account).
3. `python3 scripts/reports.py --month YYYY-MM` writes trial balance, income statement, balance sheet, director position and open items to `reports/xcl/YYYY-MM/`.
4. Independent review by a separate agent that did not make the entries.
5. Seal: git tag `xcl-YYYY-MM` only when all of this holds: no `!` in the month, suspense account nil, CBUAE rate of the month-end published and FX difference booked, review findings processed.

Deliberately NOT booked by the script:
- Set-off of the director's current account against the salary payable: only after the addendum is signed, on its effective date (Schedule 1). Until then both are shown gross, plus a pro forma net in `director_position.csv`.
- Annual leave accrual: needs the leave days actually taken (`leave.enabled` in `parameters.yaml`).
- FX difference on EUR items: see section 10.
- Corporate tax: nil for 2026 under Small Business Relief (a loss in an SBR year is forfeited).

## 10. Known gap: FX on EUR items (found 3-11-2026)

EUR amounts are booked in AED at the CBUAE rate of the invoice date, but EUR sold at Wio is converted at the Wio rate (about 2.5 to 4.5% below the CBUAE reference rate in 2026). The difference (realised on conversions, unrealised on the EUR balance) is not booked anywhere: AED 11,898.79 loss at 31-10-2026, valued at the rate of 30-9-2026 (October not yet published). The balance sheet report shows it as an explicit reconciling line. Sensitivity to the October rate is small (net EUR exposure about EUR 1,026, so about AED 50 per 0.05 of rate). The fix is a design change (EUR lots with cost basis so conversions realise the difference, plus a month-end revaluation); until it is built, a month cannot be sealed.
