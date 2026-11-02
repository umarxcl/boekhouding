# Rekeningschema in gewone taal

Automatisch gemaakt uit het grootboek (`scripts/rekeningschema_md.py`). Wijzig de uitleg in `accounts.beancount`, niet hier.


## XCL MANAGEMENT CONSULTANCIES - FZCO

| Rekening | Wat het is | Btw | Jaarrekening |
|---|---|---|---|
| `Assets:Bank:Wio-AED` | Zakelijke betaalrekening Wio in dirham (pas voor zakelijke uitgaven) |  | Liquide middelen |
| `Assets:Bank:Wio-EUR` | Zakelijke rekening Wio in euro (ontvangst van de managementfees) |  | Liquide middelen |
| `Assets:Btw:Voorbelasting` | Btw op UAE-kosten die XCL mag terugvragen (alleen met TRN-factuur, alleen na btw-registratie) |  | Belastingvordering |
| `Assets:Debiteuren:Ekmekci` | Nog te ontvangen van Ekmekci Group B.V. (verstuurde facturen min ontvangsten) |  | Handelsvorderingen |
| `Assets:Debiteuren:Inclusionair` | Nog te ontvangen van Inclusionair (Nederlandse bv), gefactureerd in AED |  | Handelsvorderingen |
| `Assets:Debiteuren:MDI` | Nog te ontvangen van MDI Consultants B.V. |  | Handelsvorderingen |
| `Assets:Debiteuren:Overig` | Nog te ontvangen van overige klanten |  | Handelsvorderingen |
| `Assets:Debiteuren:Point-Sixteen` | Nog te ontvangen van Point Sixteen B.V. (fee vanaf besluit) |  | Handelsvorderingen |
| `Assets:Nog-te-storten-kapitaal` | Aandelenkapitaal dat door de aandeelhouder nog niet op de bankrekening is gestort |  | Vordering op aandeelhouder (te verifiëren) |
| `Assets:Rekening-courant:MZML-Ltd` | Wat XCL heeft betaald voor MZML Holding Limited |  | Vordering op verbonden partij |
| `Assets:Rekening-courant:Umar` | Rekening-courant directeur: wat XCL aan Umar heeft voorgeschoten (privé-opnames en privé-uitgaven via de XCL-pas); wordt maandelijks verrekend met de loonschuld |  | Vordering op bestuurder |
| `Assets:Vooruitbetaald:Huisvesting` | Vooruitbetaalde villahuur: het deel van een kwartaalbetaling dat nog niet verstreken is |  | Overlopende activa |
| `Assets:Vooruitbetaald:Licentie` | Vooruitbetaalde IFZA-licentie en visumkosten, gespreid over de looptijd |  | Overlopende activa |
| `Assets:Vooruitbetaald:Overig` | Overige vooruitbetalingen (jaarabonnementen e.d.) |  | Overlopende activa |
| `Equity:Aandelenkapitaal` | Geplaatst kapitaal: 100 aandelen van AED 480 (resolutie bij oprichting) |  | Aandelenkapitaal |
| `Equity:Openingsbalans` | Technische tegenrekening voor de openingsbalans |  | n.v.t. |
| `Equity:Resultaat` | Winst of verlies van afgesloten boekjaren |  | Overige reserves |
| `Expenses:Advies:Corporate-services` | RD Advisory en andere PRO-diensten (visa, licentie, certificaten) | 5% voorbelasting aftrekbaar met TRN-factuur | Overige bedrijfskosten |
| `Expenses:Advies:Fiscaal-juridisch` | Fiscaal en juridisch advies (transfer pricing, contracten) | 5% voorbelasting aftrekbaar met TRN-factuur | Overige bedrijfskosten |
| `Expenses:Auto:Brandstof-tol` | Brandstof (ADNOC, ENOC), Salik, parkeren | 5% voorbelasting aftrekbaar met TRN-factuur | Overige bedrijfskosten |
| `Expenses:Auto:Huur` | Huur van de bedrijfsauto (Ezhire e.d.) | 5% voorbelasting aftrekbaar met TRN-factuur | Overige bedrijfskosten |
| `Expenses:Bank:Kosten` | Bankkosten Wio (maandabonnement, overboekingskosten) | geen btw-gevolg | Financiële lasten |
| `Expenses:Bank:Wisselkosten` | Wisselkoersopslag van Wio op buitenlandse kaartbetalingen | geen btw-gevolg | Financiële lasten |
| `Expenses:Kantoor:Benodigdheden` | Kantoorbenodigdheden en kleine apparatuur (Amazon e.d.) | 5% voorbelasting aftrekbaar met TRN-factuur | Overige bedrijfskosten |
| `Expenses:Kantoor:Boeken-opleiding` | Vakliteratuur, cursussen, congressen | geen voorbelasting | Overige bedrijfskosten |
| `Expenses:Koersverschil` | Verlies op valutawissels en herwaardering van de EUR-rekening | geen btw-gevolg | Financiële lasten |
| `Expenses:Marketing` | LinkedIn Premium, website, profilering | geen voorbelasting | Verkoopkosten |
| `Expenses:Onbekend` | Tijdelijk: nog te beoordelen posten (moet leeg zijn bij maandafsluiting) | geen btw-gevolg | n.v.t. |
| `Expenses:Overheid:Boetes` | Boetes van FTA of IFZA (niet aftrekbaar voor CT) | geen btw-gevolg | Overige bedrijfskosten (niet aftrekbaar) |
| `Expenses:Overheid:Certificaten` | Certificaten en wijzigingen bij IFZA of FTA (salary certificate, CT-certificaat) | 5% voorbelasting aftrekbaar met TRN-factuur | Overige bedrijfskosten |
| `Expenses:Overheid:Licentie-IFZA` | IFZA-licentie, establishment card en registratiekosten (maandelijks deel van de jaarkosten) | geen btw-gevolg | Overige bedrijfskosten |
| `Expenses:Overig` | Overige kosten die nergens anders passen (toelichting verplicht) | geen voorbelasting | Overige bedrijfskosten |
| `Expenses:Personeel:End-of-service` | Jaarlijkse dotatie aan de voorziening eindevergoeding | geen btw-gevolg | Personeelskosten |
| `Expenses:Personeel:Huisvesting` | Woning Sharjah als loon in natura (villahuur, gespreid per maand) tot 14-2-2027 | geen voorbelasting | Personeelskosten |
| `Expenses:Personeel:Huisvesting-nuts` | SEWA en andere woningkosten die bij de woning als loon in natura horen | geen voorbelasting | Personeelskosten |
| `Expenses:Personeel:Loon-Umar` | Brutosalaris Umar volgens arbeidscontract (AED 40.000 per maand tot addendum) | geen btw-gevolg | Personeelskosten |
| `Expenses:Personeel:Visa-medisch` | Visum, Emirates ID, medische keuring en verzekering van de werknemer | geen voorbelasting | Personeelskosten |
| `Expenses:Reis:Verblijf` | Hotels en verblijfkosten op zakenreis | geen voorbelasting | Overige bedrijfskosten |
| `Expenses:Reis:Vervoer` | Taxi, Uber, metro, treinen | 5% voorbelasting aftrekbaar met TRN-factuur | Overige bedrijfskosten |
| `Expenses:Reis:Vliegtickets` | Zakelijke vluchten (NL-bezoeken voor klanten) | geen btw-gevolg | Overige bedrijfskosten |
| `Expenses:Representatie` | Zakelijke lunches, diners en relatiegeschenken | geen voorbelasting | Overige bedrijfskosten |
| `Expenses:Software:AI` | AI-abonnementen: Anthropic, OpenAI, Fireflies, Grok | geen voorbelasting | Overige bedrijfskosten |
| `Expenses:Software:Overig` | Overige software: Google Workspace, Dropbox, TransIP, Microsoft, Figma, Netlify, Fiskl | geen voorbelasting | Overige bedrijfskosten |
| `Expenses:Telecom` | Mobiel en internet (e& / Etisalat, du) | 5% voorbelasting aftrekbaar met TRN-factuur | Overige bedrijfskosten |
| `Expenses:Verzekering` | Zakelijke verzekeringen | geen voorbelasting | Overige bedrijfskosten |
| `Income:Koersresultaat` | Winst op valutawissels en herwaardering van de EUR-rekening | geen btw-gevolg | Financiële baten |
| `Income:Omzet:Advies:Inclusionair` | Adviesdiensten aan Inclusionair (Nederlandse bv) | omzet 0% (export van diensten) | Netto-omzet |
| `Income:Omzet:Managementfee:Ekmekci` | Managementfee aan Ekmekci Group B.V. (EUR 7.716 per maand) | omzet 0% (export van diensten) | Netto-omzet |
| `Income:Omzet:Managementfee:MDI` | Fee aan MDI Consultants B.V. (leergang ABN AMRO) | omzet 0% (export van diensten) | Netto-omzet |
| `Income:Omzet:Managementfee:Point-Sixteen` | Fee aan Point Sixteen B.V. (vanaf besluit en managementovereenkomst) | omzet 0% (export van diensten) | Netto-omzet |
| `Income:Omzet:Overig` | Overige omzet | omzet 0% (export van diensten) | Netto-omzet |
| `Income:Overig` | Overige baten (terugbetalingen e.d.) | geen btw-gevolg | Overige baten |
| `Liabilities:Btw:Af-te-dragen` | Btw die XCL moet afdragen (bij 0%-export nihil; saldo met voorbelasting bepaalt de aangifte) |  | Belastingschuld |
| `Liabilities:CT:Te-betalen` | Vennootschapsbelasting UAE (bij Small Business Relief 2026 nihil) |  | Belastingschuld |
| `Liabilities:Crediteuren` | Ontvangen inkoopfacturen die nog betaald moeten worden |  | Handelsschulden |
| `Liabilities:Overlopend` | Kosten die bij de maand horen maar nog niet gefactureerd of betaald zijn |  | Overlopende passiva |
| `Liabilities:Personeel:End-of-service` | Voorziening eindevergoeding (end of service gratuity) volgens UAE-arbeidsrecht |  | Voorziening personeelsbeloningen |
| `Liabilities:Personeel:Loonschuld-Umar` | Opgebouwd maar nog niet uitbetaald salaris van Umar (contract AED 40.000 per maand; route a) |  | Schuld aan bestuurder |

## MZML HOLDING LIMITED

| Rekening | Wat het is | Btw | Jaarrekening |
|---|---|---|---|
| `Assets:Bank:Nog-te-openen` | Bankrekening MZML Ltd, aan te vragen januari 2027 |  | Liquide middelen |
| `Assets:Deelnemingen:Ekmekci` | 75 aandelen Ekmekci Group B.V. (18,80%), gekocht 31-12-2025 tegen kostprijs |  | Financiële vaste activa, deelnemingen tegen kostprijs |
| `Assets:Deelnemingen:Point-Sixteen` | 5.000 aandelen Point Sixteen B.V. (50%), gekocht 31-12-2025 |  | Financiële vaste activa, deelnemingen tegen kostprijs |
| `Assets:Deelnemingen:The-Ocean` | 720 aandelen The Ocean B.V. (30%), gekocht 31-12-2025 |  | Financiële vaste activa, deelnemingen tegen kostprijs |
| `Assets:Nog-te-storten-kapitaal` | Aandelenkapitaal (AED 100.000) dat nog niet is gestort; er is nog geen bankrekening |  | Vordering op aandeelhouder (te verifiëren) |
| `Assets:Rekening-courant:Umar` | Wat Umar privé heeft betaald voor MZML Ltd, of andersom |  | Vordering op bestuurder |
| `Assets:Te-ontvangen-dividend` | Vastgesteld maar nog niet ontvangen dividend van deelnemingen |  | Vorderingen |
| `Equity:Aandelenkapitaal` | Geplaatst kapitaal: 100 aandelen van AED 1.000 (register of members RAK ICC) |  | Aandelenkapitaal |
| `Equity:Openingsbalans` | Technische tegenrekening voor de openingsbalans |  | n.v.t. |
| `Equity:Resultaat` | Winst of verlies van afgesloten boekjaren |  | Overige reserves |
| `Expenses:Advies` | Fiscaal, juridisch en corporate-services advies | geen btw-gevolg | Overige bedrijfskosten |
| `Expenses:Bank` | Bankkosten (vanaf opening rekening) | geen btw-gevolg | Financiële lasten |
| `Expenses:Koersverschil` | Koersverlies op EUR-posities bij herwaardering | geen btw-gevolg | Financiële lasten |
| `Expenses:Onbekend` | Tijdelijk: nog te beoordelen (moet leeg zijn bij afsluiting) | geen btw-gevolg | n.v.t. |
| `Expenses:Oprichting` | Oprichtingskosten (eenmalig, boekjaar 1) | geen btw-gevolg | Overige bedrijfskosten |
| `Expenses:Overheid:Certificaten` | Certificate of incumbency, good standing, CT-certificaat | geen btw-gevolg | Overige bedrijfskosten |
| `Expenses:Overheid:RAK-ICC` | Jaarlijkse verlenging RAK ICC inclusief registered agent | geen btw-gevolg | Overige bedrijfskosten |
| `Expenses:Rente:Vendor-loan` | Rente op de vendor loans aan MZML Holding B.V. (als afgesproken) | geen btw-gevolg | Financiële lasten |
| `Income:Dividend` | Dividend van deelnemingen (deelnemingsvrijstelling CT vanaf 1-1-2027) | geen btw-gevolg | Opbrengst deelnemingen |
| `Income:Koersresultaat` | Koerswinst op EUR-posities bij herwaardering | geen btw-gevolg | Financiële baten |
| `Liabilities:CT:Te-betalen` | Vennootschapsbelasting UAE (verwacht nihil) |  | Belastingschuld |
| `Liabilities:Rekening-courant:MZML-BV` | Kosten van MZML Ltd die MZML Holding B.V. (NL) heeft voorgeschoten (oprichting, certificaten, RAK ICC) |  | Kortlopende schuld aan verbonden partij |
| `Liabilities:Rekening-courant:XCL` | Kosten van MZML Ltd die XCL heeft voorgeschoten |  | Kortlopende schuld aan verbonden partij |
| `Liabilities:Te-betalen-rente` | Opgelopen maar nog niet betaalde rente op de vendor loans (als rente is afgesproken) |  | Overlopende passiva |
| `Liabilities:Vendor-loan:MZML-BV:Ekmekci` | Koopsom aandelen Ekmekci, schuldig gebleven aan MZML Holding B.V. (voorwaarden: overeenkomst in Dropbox) |  | Langlopende schuld aan verbonden partij |
| `Liabilities:Vendor-loan:MZML-BV:Point-Sixteen` | Koopsom aandelen Point Sixteen, schuldig gebleven aan MZML Holding B.V. |  | Langlopende schuld aan verbonden partij |
| `Liabilities:Vendor-loan:MZML-BV:The-Ocean` | Koopsom aandelen The Ocean, schuldig gebleven aan MZML Holding B.V. |  | Langlopende schuld aan verbonden partij |
