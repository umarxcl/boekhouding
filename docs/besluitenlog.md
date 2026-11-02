# Besluitenlog boekhouding

Eén regel per besluit dat de boekingen of de werkwijze bepaalt. Bron is altijd het project Boekhouding NL & UAE (briefing v9) tenzij anders vermeld.

| Datum | Besluit | Gevolg in het grootboek |
|---|---|---|
| 2026-10-18 | Salaris AED 22.000 per maand vanaf 25-10-2026, geen woonvergoeding | Betalingen "Salary" verlagen `Liabilities:Personeel:Loonschuld-Umar` |
| 2026-10-18 | Route a: loon over 2026 op contractbasis (AED 40.000 per maand vanaf 15-12-2025); niet-betaald deel is rentevrije schuld | Maandelijkse boeking `Expenses:Personeel:Loon-Umar` tegen `Liabilities:Personeel:Loonschuld-Umar` |
| 2026-10-18 | Alle overboekingen naar Umar zonder "Salary" en alle privé-uitgaven via de XCL-pas zijn rekening-courant directeur, verrekend met de loonschuld | `Assets:Rekening-courant:Umar`; maandelijkse verrekeningsboeking |
| 2026-10-21 | Villa tot 14-2-2027 via XCL als loon in natura; kwartaalhuur gespreid | `Expenses:Personeel:Huisvesting` plus `Assets:Vooruitbetaald:Huisvesting` |
| 2026-10-21 | Auto via XCL is zakelijk, ook de betalingen die in de Cashflow-Sheet als privé staan | `Expenses:Auto:*` |
| 2026-10-21 | Accrual, IFRS for SMEs; SBR voor 2026; alle omzet 2026 0% export (Ekmekci, MDI, Inclusionair zijn NL-bv's) | btw-code `0-export` op alle omzetrekeningen |
| 2026-10-21 | Inhaalslag jan t/m sep 2026: Wio-export als waarheid, Sheet-labels als hint; privé per transactie op rekening-courant | Importer plus regels; geen samengevatte boekingen |
| 2026-11-02 | Beancount als grootboek, Google Workspace als werkomgeving, GitHub `umarxcl/boekhouding`; geen Zoho; fase 1 zonder VPS | Deze repository |
| 2026-11-02 | Kosten MZML Ltd betaald door MZML Holding B.V. (NL), naar herinnering van Umar; te verifiëren | `Liabilities:Rekening-courant:MZML-BV` |
| 2026-11-02 | Koersen alleen waargenomen (Wio-wissels of ECB met bron), nooit geschat | `shared/prices.beancount` |
| 2026-11-02 | Kapitaal XCL (AED 48.000) en MZML Ltd (AED 100.000) als nog te storten, totdat storting blijkt | `Assets:Nog-te-storten-kapitaal` met vlag `!` |

## Open punten die een boeking tegenhouden

- Btw-registratiedatum XCL (bepaalt vanaf wanneer voorbelasting wordt geboekt).
- Vendor-loanvoorwaarden (rente, looptijd): overeenkomst in Dropbox.
- Welke partij de MZML Ltd-kosten werkelijk betaalde (ING-export MZML B.V., RD-facturen F2025-9718, F2025-9730, F2026-1034).
- Overboekingen "N" en "M" van juli 2026 (AED 10.000).
- IFZA-licentiekosten 2025/2026: factuur en betaler (voor spreiding over de looptijd 15-12-2025 t/m 14-12-2026).
