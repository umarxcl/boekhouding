# Bookkeeping XCL and MZML Holding Limited

This is the general ledger of XCL MANAGEMENT CONSULTANCIES - FZCO (IFZA, Dubai) and MZML HOLDING LIMITED (RAK ICC). The Dutch B.V.s will be added from January 2027. The ledger is a set of text files in Beancount format (double-entry bookkeeping). Claude does the bookkeeping; Umar reads the figures in Google Sheets and approves one list per month. Nobody needs to read these files to understand the accounts: every account has a plain-language explanation (metadata `note:`) and every entry has a source and a reference.

The bookkeeping is kept in English (owner decision 2-11-2026). Account names were translated on 3-11-2026; the old Dutch names are in `docs/account_mapping_nl_en.md`.

## What is where

| Folder or file | Contents |
|---|---|
| `xcl/` | XCL ledger: chart of accounts (`accounts.beancount`), opening balance (`opening.beancount`), bank entries per month (`2026/MM.beancount`), sales invoices (`2026/facturen.beancount`, generated), manual journal entries (`2026/adjustments.beancount`) |
| `mzml_ltd/` | MZML Holding Limited ledger, same structure |
| `shared/` | Currencies and exchange rates (observed rates only, with source) |
| `importers/` | Bank export import: `wio.py`, the categorisation rules `rules_xcl.yaml` and the receipt links `documenten_xcl.yaml` |
| `scripts/` | Checks, invoice generation, month split, chart of accounts document |
| `docs/` | Runbook (how the system works and how to recover it), chart of accounts in plain language, account mapping, decision log |
| `tests/` | Sample export and importer test (`bash tests/test_importer.sh`) |

Attachments (invoices, receipts, statements) are not stored here but in Google Drive, folder Boekhouding. Every entry refers to them.

## Standing rules

1. Every entry balances (debit = credit). Otherwise Beancount rejects the whole file; `bean-check` must always be clean.
2. Every bank line has a Wio reference number (`wio-ref`). The same number is never imported twice.
3. An entry with flag `!` has not been reviewed yet. A month is only closed when it contains no `!` and the bank balances agree with the statement.
4. Closed months get a git tag (`xcl-2026-10`) and are not changed afterwards; a correction is a new entry in the current month (in `adjustments.beancount`) with a reference.
5. Exchange rates are never estimated: only actual Wio conversions or the CBUAE rate of the day, with source.
6. Generated files are never edited by hand: `facturen.beancount` comes from `scripts/facturen.py` (which refuses to overwrite hand edits), month files from the importer; manual corrections go in `adjustments.beancount`.
7. No bank login details, keys or passwords in this repository.

## Recovery without Claude

If the system stops: the figures are in Google Sheets (latest monthly report) and the attachments in Drive. Any accountant can read this ledger after exporting to CSV: `bean-query xcl/main.beancount "select date, account, position, narration"`. See `docs/runbook.md`.
