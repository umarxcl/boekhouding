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

## Review rekeningschema 2-11-2026 (docs/review_rekeningschema.md), verwerkt

| Datum | Wijziging | Gevolg |
|---|---|---|
| 2026-11-02 | Resultaat- en eigenvermogensrekeningen alleen in AED; EUR-posten omgerekend tegen de CBUAE-koers van de dag (art. 69 btw-wet); ECB vervalt als bron | Importer rekent EUR-regels om; shared/prices.beancount uit CBUAE-maandoverzichten |
| 2026-11-02 | Deelnemingen MZML Ltd in EUR met kostprijs in AED (koers CBUAE 30-12-2025: 4.319572), nooit herwaarderen; vendor loans wel | mzml_ltd/opening.beancount |
| 2026-11-02 | Nieuwe btw-codeset (10 codes, elk gekoppeld aan een VAT 201-vak) en metadata ct, verbonden, rgs op elke rekening | accounts.beancount beide entiteiten; docs/rekeningschema.md |
| 2026-11-02 | Reverse charge op buitenlandse diensten (software, AI, NL-advies, LinkedIn) vanaf de btw-registratiedatum | Assets:Btw:Voorbelasting-verlegd en Liabilities:Btw:Verlegd |
| 2026-11-02 | Btw-codes gecorrigeerd: autohuur en brandstof geblokkeerd (auto privé beschikbaar), taxi/metro vrijgesteld, woninghuur vrijgesteld, SEWA geblokkeerd, bankkosten 5%, FTA/IFZA-heffingen buiten reikwijdte, verzekering 5% | accounts.beancount XCL |
| 2026-11-02 | Nieuwe rekeningen XCL: vaste activa en afschrijving, waarborgsommen, kruisposten, vooruitontvangen omzet, lening aandeelhouder, verlofverplichting, zorgverzekering, auto privégebruik als loon in natura, binnenlandse omzet, representatie gesplitst, vennootschapsbelasting, donaties, kapitaalbijdrage | accounts.beancount XCL |
| 2026-11-02 | Nieuwe rekeningen MZML Ltd: waardevermindering per deelneming, crediteuren, overlopend, kapitaalbijdrage, bronbelasting, vennootschapsbelasting; Bank:Nog-te-openen verwijderd | accounts.beancount MZML Ltd |
| 2026-11-02 | IFZA-licentie eerst op vooruitbetaald, maandelijks naar kosten; geld van Umar privé naar XCL als lening aandeelhouder met vlag (kapitaalstorting eerst vaststellen) | rules_xcl.yaml |
| 2026-11-02 | Inhaalslag XCL jan-okt 2026: bank is waarheid, Cashflow-Sheet en Fiskl alleen hints; bon in Drive = zakelijk, zonder bon = privé (rekening-courant, vlag !); INV-0008 Inclusionair als vooruitontvangen, omzet 31-10-2026 (leverdatum nog te bevestigen); CBUAE-koersen alleen waargenomen, oktober ontbreekt | rules_xcl.yaml, documenten_xcl.yaml, facturen.beancount |

## Besluiten die Umar nog moet nemen (uit de review, sectie C)

- Btw: doorgaan met registratie, of de uitzondering voor uitsluitend nultarief-leveringen aanvragen (vraag aan Davie; let op dat geïmporteerde diensten meetellen).
- Route a: uitgestelde betaling van loon schriftelijk vastleggen (addendum), inclusief verrekeningsafspraak en voorschotregeling voor de rekening-courant; welk loon wordt opgebouwd in november en december 2026.
- Verlies 2026 onder SBR vervalt; afweging SBR versus standaardregime vóór de aangifte; SBR zou zijn verlengd tot boekjaren t/m 2029 (MD 131/2026, te verifiëren).
- Auto: privégebruik als loon in natura (Expenses:Personeel:Auto-prive), percentage vaststellen.
- 0% export na de bestuurswissel: toetsen door Dinesh en Davie vóór de bestuurswissel (vestigingsplaats van de NL-bv's voor de btw).
- EUR 25.000 van 26-1-2026: kapitaalstorting (AED 48.000) plus lening, of alleen lening.
- MZML Ltd: één financier (bankrekening) in plaats van voorschotten van MZML B.V. en XCL.

## Besluiten Umar 2-11-2026 (avond)

| Datum | Besluit | Gevolg in het grootboek |
|---|---|---|
| 2026-11-02 | Boekhouding in het Engels | Hernoemronde van rekeningnamen, uitleg, rapporten en documentatie (volgt) |
| 2026-11-02 | Btw-registratie is verplicht; geen uitzondering aanvragen | Reverse charge en voorbelasting vanaf de registratiedatum |
| 2026-11-02 | Addendum v1 is NIET getekend; geen overstap naar SRTIP | Contractloon AED 40.000 loopt door tot de tekendatum van een nieuw addendum; geen terugwerkende kracht |
| 2026-11-02 | Villa (Nesma house) staat op naam van Umar | Alle huurbetalingen, commissie en borg door XCL zijn betalingen namens Umar: Assets:Rekening-courant:Umar, verrekend met de loonschuld; geen loon in natura, geen vooruitbetaalde huur bij XCL |
| 2026-11-02 | Auto: privédeel 30% via de schuldroute | 30% van de autokosten maandelijks naar Assets:Rekening-courant:Umar; geen loon in natura |
| 2026-11-02 | EUR 25.000 van 26-1-2026: AED 48.000 kapitaalstorting, rest renteloze lening | Kapitaal volgestort; Liabilities:Lening-aandeelhouder:Umar EUR 13.685,85; aandeelhoudersbesluit op te stellen |
| 2026-11-02 | MZML Ltd: bankrekening in januari 2027; tot dan voorschotten als schuld aan de betalende partij | Liabilities:Rekening-courant:MZML-BV en :XCL |

## Besluiten en bevindingen 3-11-2026

| Datum | Besluit | Gevolg in het grootboek |
|---|---|---|
| 2026-11-03 | Antwoorden Goedkeuring-Sheet verwerkt (docs/goedkeuring/2026-11-03.yaml) | 120 boekingen aangepast; open posten XCL van 113 naar 9 |
| 2026-11-03 | NLBC UAE is zakelijk lidmaatschap; factuur INVM000102 in Gmail | Expenses:Marketing |
| 2026-11-03 | Bonnen in Gmail gevonden: Emirates D2CWJ6 (11-5), ACUNS lidmaatschap en Annual Meeting | Vlag weg, verwijzing in metadata `document` |
| 2026-11-03 | Emirates AED 122, 57, 11 (augustus): geen bon in Gmail | Privé (rekening-courant) |
| 2026-11-03 | Herinnering: doorbelastingsfactuur aan Point Sixteen (koerier AED 516,68) opstellen bij de start van de facturatiemodule | Assets:Debiteuren:Point-Sixteen, vlag ! tot de factuur er is |
| 2026-11-03 | neWings 2026-0098 (herwaardering Ekmekci en The Ocean, sept 2026) is voor MZML Holding B.V. zelf (besluit Umar); factuur blijft op MZML B.V. | Assets:Rekening-courant:MZML-BV AED 3.831,22; MZML B.V. betaalt XCL terug (Hans boekt in AFAS) |
