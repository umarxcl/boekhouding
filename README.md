# Boekhouding XCL en MZML Holding Limited

Dit is het grootboek van XCL MANAGEMENT CONSULTANCIES - FZCO (IFZA, Dubai) en MZML HOLDING LIMITED (RAK ICC). Vanaf januari 2027 komen de Nederlandse bv's erbij. Het grootboek is een set tekstbestanden in het formaat van Beancount (dubbel boekhouden). Claude boekt erin; Umar leest de cijfers in Google Sheets en keurt één lijst per maand goed. Niemand hoeft deze bestanden te kunnen lezen om de boekhouding te begrijpen: elke rekening heeft een uitleg in gewone taal (veld `nl:`) en elke boeking een bron en een referentie.

## Waar wat staat

| Map of bestand | Wat erin zit |
|---|---|
| `xcl/` | Grootboek XCL: rekeningschema (`accounts.beancount`), openingsbalans (`opening.beancount`), boekingen per maand (`2026/MM.beancount`) |
| `mzml_ltd/` | Grootboek MZML Holding Limited, zelfde opbouw |
| `shared/` | Valuta's en koersen (alleen waargenomen koersen, met bron) |
| `importers/` | Inlezen van bankexports: `wio.py` en de categoriseringsregels `rules_xcl.yaml` |
| `scripts/` | Controles en maandafsluiting |
| `docs/` | Runbook (hoe het systeem werkt en hoe je het herstelt), rekeningschema in gewone taal, besluitenlog |
| `tests/` | Voorbeeldexport en controletests |

Bijlagen (facturen, bonnen, afschriften) staan niet hier maar in Google Drive, map Boekhouding. Elke boeking verwijst ernaar.

## Vaste regels

1. Elke boeking sluit (debet = credit). Beancount weigert anders het hele bestand; `bean-check` moet altijd groen zijn.
2. Elke bankregel heeft een Wio-referentienummer (`wio-ref`). Hetzelfde nummer wordt nooit twee keer ingelezen.
3. Een boeking met vlag `!` is nog niet beoordeeld. Een maand wordt pas afgesloten als er geen `!` meer in staat en de banksaldi kloppen met het afschrift.
4. Afgesloten maanden krijgen een git-tag (`xcl-2026-10`) en worden niet meer gewijzigd; een correctie is een nieuwe boeking in de lopende maand met verwijzing.
5. Koersen worden nooit geschat: alleen werkelijke Wio-wissels of de ECB-koers van de dag, met bron.
6. Geen bankinloggegevens, sleutels of wachtwoorden in deze repository.

## Herstel zonder Claude

Als het systeem stilvalt: de cijfers staan in Google Sheets (laatste maandrapport) en de bijlagen in Drive. Dit grootboek kan elke boekhouder lezen na export naar CSV: `bean-query xcl/main.beancount "select date, account, position, narration"`. Zie `docs/runbook.md`.
