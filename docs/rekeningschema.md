# Rekeningschema in gewone taal

Automatisch gemaakt uit het grootboek (`scripts/rekeningschema_md.py`). Wijzig de uitleg in `accounts.beancount`, niet hier.


## XCL MANAGEMENT CONSULTANCIES - FZCO

| Rekening | Wat het is | Btw | CT | Verbonden | Jaarrekening | RGS |
|---|---|---|---|---|---|---|
| `Assets:Bank:Wio-AED` | Zakelijke betaalrekening Wio in dirham (pas voor zakelijke uitgaven) |  |  |  | Liquide middelen | BLimBan |
| `Assets:Bank:Wio-EUR` | Zakelijke rekening Wio in euro (ontvangst van de managementfees) |  |  |  | Liquide middelen | BLimBan |
| `Assets:Btw:Voorbelasting` | Btw op UAE-kosten die XCL mag terugvragen (alleen met TRN-factuur, alleen vanaf de registratiedatum) | 5% voorbelasting met TRN-factuur (vak 9) |  |  | Belastingvordering | BVorVbk |
| `Assets:Btw:Voorbelasting-verlegd` | Btw die XCL over buitenlandse diensten zelf berekent en tegelijk aftrekt (VAT 201 vak 10) | verlegd: zelf aangeven en aftrekken (vak 3 en 10) |  |  | Belastingvordering (gesaldeerd met Liabilities:Btw:Verlegd) | BVorVbk |
| `Assets:Debiteuren:Ekmekci` | Nog te ontvangen van Ekmekci Group B.V. (verstuurde facturen min ontvangsten) |  |  | related-party | Vorderingen op verbonden partijen | BVorVov |
| `Assets:Debiteuren:Inclusionair` | Nog te ontvangen van Inclusionair (Nederlandse bv), gefactureerd in AED |  |  |  | Handelsvorderingen | BVorDeb |
| `Assets:Debiteuren:MDI` | Nog te ontvangen van MDI Consultants B.V. |  |  | related-party | Vorderingen op verbonden partijen | BVorVov |
| `Assets:Debiteuren:Overig` | Nog te ontvangen van overige klanten |  |  |  | Handelsvorderingen | BVorDeb |
| `Assets:Debiteuren:Point-Sixteen` | Nog te ontvangen van Point Sixteen B.V. (fee vanaf besluit en managementovereenkomst) |  |  | related-party | Vorderingen op verbonden partijen | BVorVov |
| `Assets:Kruisposten` | Geld onderweg tussen eigen rekeningen; moet bij maandafsluiting nul zijn | geen btw-gevolg |  |  | n.v.t. | BVorTus |
| `Assets:Nog-te-storten-kapitaal` | Aandelenkapitaal dat de aandeelhouder nog niet heeft gestort; in de jaarrekening in mindering op het eigen vermogen |  |  | connected-person | In mindering op eigen vermogen (IFRS for SMEs 22.7(a)) | BVorVao |
| `Assets:Rekening-courant:MZML-Ltd` | Wat XCL heeft betaald voor MZML Holding Limited (af te wikkelen zodra MZML Ltd een bankrekening heeft) |  |  | related-party | Vordering op verbonden partij | BVorVov |
| `Assets:Rekening-courant:Umar` | Rekening-courant directeur: wat XCL aan Umar heeft voorgeschoten (privé-opnames en privé-uitgaven via de XCL-pas); maandelijks verrekend met de loonschuld volgens de schriftelijke verrekeningsafspraak |  | marktwaarde-toets | connected-person | Vordering op of schuld aan bestuurder | BVorOvr |
| `Assets:Vaste-activa:Inventaris:Afschrijving` | Opgebouwde afschrijving op apparatuur (lineair: laptop 3 jaar, telefoon 2 jaar) | geen btw-gevolg | aftrekbaar |  | Materiële vaste activa (cumulatieve afschrijving) | BMvaBei |
| `Assets:Vaste-activa:Inventaris:Kostprijs` | Aanschafprijs van laptop, telefoon en apparatuur vanaf AED 2.500 per stuk | 5% voorbelasting met TRN-factuur (vak 9) | aftrekbaar |  | Materiële vaste activa | BMvaBei |
| `Assets:Vooruitbetaald:Huisvesting` | Vooruitbetaalde villahuur: het deel van een kwartaalbetaling dat nog niet verstreken is |  |  |  | Overlopende activa | BVorOva |
| `Assets:Vooruitbetaald:Licentie` | Vooruitbetaalde IFZA-licentie en establishment card, gespreid over de licentieperiode |  |  |  | Overlopende activa | BVorOva |
| `Assets:Vooruitbetaald:Overig` | Overige vooruitbetalingen (jaarabonnementen, verzekeringen) |  |  |  | Overlopende activa | BVorOva |
| `Assets:Waarborgsommen` | Borg villa en huurauto; terug te ontvangen bij einde huur | geen btw-gevolg | nvt |  | Overige vorderingen | BFvaOvr |
| `Equity:Aandelenkapitaal` | Geplaatst kapitaal: 100 aandelen van AED 480 (resolutie bij oprichting) |  |  |  | Aandelenkapitaal | BEivGok |
| `Equity:Kapitaalbijdrage` | Inbreng van de aandeelhouder buiten aandelen om (bijv. een kwijtgescholden loonschuld) |  |  |  | Overige reserves (kapitaalbijdrage aandeelhouder) | BEivAgi |
| `Equity:Openingsbalans` | Technische tegenrekening voor de openingsbalans |  |  |  | n.v.t. |  |
| `Equity:Resultaat` | Winst of verlies van afgesloten boekjaren |  |  |  | Overige reserves | BEivOvrAlr |
| `Expenses:Advies:Corporate-services` | RD Advisory en andere PRO-diensten (servicefee 5% voorbelasting; doorbelaste overheidsheffingen buiten reikwijdte) | 5% voorbelasting met TRN-factuur (vak 9) | aftrekbaar |  | Overige bedrijfskosten | WBedAlk |
| `Expenses:Advies:Fiscaal-juridisch` | Fiscaal en juridisch advies (UAE-adviseur 5% voorbelasting; NL-adviseur verlegd) | 5% voorbelasting met TRN-factuur (vak 9) | aftrekbaar |  | Overige bedrijfskosten | WBedAlk |
| `Expenses:Afschrijvingen:Inventaris` | Afschrijving op laptop, telefoon en apparatuur | geen btw-gevolg | aftrekbaar |  | Afschrijvingen | WAfs |
| `Expenses:Auto:Brandstof` | Brandstof (ADNOC, ENOC); btw conservatief geblokkeerd zolang de auto privé beschikbaar is | btw niet aftrekbaar (art. 53) | aftrekbaar |  | Overige bedrijfskosten | WBedAut |
| `Expenses:Auto:Huur` | Huur van de bedrijfsauto (Ezhire e.d.); btw geblokkeerd omdat de auto ook privé beschikbaar is | btw niet aftrekbaar (art. 53) | aftrekbaar |  | Overige bedrijfskosten | WBedAut |
| `Expenses:Auto:Tol-parkeren` | Salik, RTA-parkeren en overheidsparkeren (geen btw) | heffing zonder btw | aftrekbaar |  | Overige bedrijfskosten | WBedAut |
| `Expenses:Bank:Kosten` | Bankkosten Wio (maandabonnement, overboekingskosten); Wio stuurt een btw-factuur | 5% voorbelasting met TRN-factuur (vak 9) | aftrekbaar |  | Overige bedrijfskosten | WBedAlk |
| `Expenses:Bank:Wisselkosten` | Wisselkoersopslag van Wio op buitenlandse kaartbetalingen | 5% voorbelasting met TRN-factuur (vak 9) | aftrekbaar |  | Overige bedrijfskosten | WBedAlk |
| `Expenses:Donaties` | Giften; alleen aftrekbaar aan een Qualifying Public Benefit Entity | geen btw-gevolg | niet-aftrekbaar |  | Overige bedrijfskosten | WBedAlk |
| `Expenses:Kantoor:Benodigdheden` | Kantoorbenodigdheden en kleine apparatuur onder AED 2.500 (Amazon.ae e.d.) | 5% voorbelasting met TRN-factuur (vak 9) | aftrekbaar |  | Overige bedrijfskosten | WBedKan |
| `Expenses:Kantoor:Boeken-opleiding` | Vakliteratuur, cursussen, congressen; btw per factuur (UAE-congres 5%, buitenlandse cursus verlegd) | verlegd: zelf aangeven en aftrekken (vak 3 en 10) | aftrekbaar |  | Overige bedrijfskosten | WBedOvp |
| `Expenses:Koersverschil` | Verlies op valutawissels en herwaardering van EUR-saldi en -vorderingen | geen btw-gevolg | aftrekbaar |  | Financiële lasten | WFbe |
| `Expenses:Marketing` | LinkedIn Premium, website, profilering (buitenlandse leveranciers: verlegd) | verlegd: zelf aangeven en aftrekken (vak 3 en 10) | aftrekbaar |  | Verkoopkosten | WBedVkk |
| `Expenses:Onbekend` | Tijdelijk: nog te beoordelen posten (moet leeg zijn bij maandafsluiting) | geen btw-gevolg | nvt |  | n.v.t. |  |
| `Expenses:Overheid:Boetes` | Boetes van FTA, IFZA of verkeer (niet aftrekbaar voor CT) | heffing zonder btw | niet-aftrekbaar |  | Overige bedrijfskosten (niet aftrekbaar) | WBedAlk |
| `Expenses:Overheid:Certificaten` | Certificaten en wijzigingen bij IFZA of FTA (heffingen zonder btw; de servicefee van een dienstverlener gaat naar Advies) | heffing zonder btw | aftrekbaar |  | Overige bedrijfskosten | WBedAlk |
| `Expenses:Overheid:Licentie-IFZA` | IFZA-licentie, establishment card en registratie (maandelijks deel via Vooruitbetaald:Licentie); btw per factuur | heffing zonder btw | aftrekbaar |  | Overige bedrijfskosten | WBedAlk |
| `Expenses:Overig` | Overige kosten die nergens anders passen (toelichting verplicht; btw per factuur) | heffing zonder btw | aftrekbaar |  | Overige bedrijfskosten | WBedAlk |
| `Expenses:Personeel:Auto-prive` | Privégebruik van de bedrijfsauto als loon in natura (deel van de autokosten) | geen btw-gevolg | marktwaarde-toets | connected-person | Personeelskosten | WPerLes |
| `Expenses:Personeel:End-of-service` | Dotatie aan de voorziening eindevergoeding | geen btw-gevolg | marktwaarde-toets | connected-person | Personeelskosten | WPerLes |
| `Expenses:Personeel:Huisvesting` | Woning Sharjah als loon in natura (villahuur, gespreid per maand) tot 14-2-2027; woninghuur is btw-vrijgesteld | vrijgestelde inkoop | marktwaarde-toets | connected-person | Personeelskosten | WPerLes |
| `Expenses:Personeel:Huisvesting-nuts` | SEWA en andere woningkosten bij de woning als loon in natura; btw geblokkeerd (privévoorziening werknemer) | btw niet aftrekbaar (art. 53) | marktwaarde-toets | connected-person | Personeelskosten | WPerLes |
| `Expenses:Personeel:Loon-Umar` | Brutosalaris Umar volgens arbeidscontract | geen btw-gevolg | marktwaarde-toets | connected-person | Personeelskosten | WPerLes |
| `Expenses:Personeel:Verlof` | Dotatie aan de verlofverplichting | geen btw-gevolg | marktwaarde-toets | connected-person | Personeelskosten | WPerLes |
| `Expenses:Personeel:Visa-overheid` | Visum, Emirates ID, medische keuring (overheidsheffingen, geen btw) | heffing zonder btw | aftrekbaar |  | Personeelskosten | WBedOvp |
| `Expenses:Personeel:Zorgverzekering` | Verplichte zorgverzekering van de werknemer (alleen de werknemer, niet het gezin) | 5% voorbelasting met TRN-factuur (vak 9) | marktwaarde-toets | connected-person | Personeelskosten | WBedOvp |
| `Expenses:Reis:Verblijf` | Hotels en verblijfkosten op zakenreis (NL: geen UAE-btw; UAE-hotel: 5% voorbelasting) | verbruikt buiten de UAE | aftrekbaar |  | Overige bedrijfskosten | WBedVkk |
| `Expenses:Reis:Vervoer` | Taxi, Uber, metro (lokaal personenvervoer is btw-vrijgesteld) | vrijgestelde inkoop | aftrekbaar |  | Overige bedrijfskosten | WBedVkk |
| `Expenses:Reis:Vliegtickets` | Zakelijke vluchten (internationaal vervoer: nultarief) | nultarief-inkoop | aftrekbaar |  | Overige bedrijfskosten | WBedVkk |
| `Expenses:Representatie:Klanten` | Zakelijke lunches en diners met klanten of zakenpartners (btw geblokkeerd; 50% niet aftrekbaar voor CT) | btw niet aftrekbaar (art. 53) | 50-niet-aftrekbaar |  | Overige bedrijfskosten | WBedVkk |
| `Expenses:Representatie:Relatiegeschenken` | Relatiegeschenken (geen entertainment; aftrekbaar als zakelijk) | btw niet aftrekbaar (art. 53) | aftrekbaar |  | Overige bedrijfskosten | WBedVkkRel |
| `Expenses:Software:AI` | AI-abonnementen van buitenlandse leveranciers (Anthropic, OpenAI, Fireflies, xAI): btw verlegd na registratie | verlegd: zelf aangeven en aftrekken (vak 3 en 10) | aftrekbaar |  | Overige bedrijfskosten | WBedKan |
| `Expenses:Software:Overig` | Overige software (Google, Dropbox, TransIP, Microsoft, Figma, Netlify): verlegd; UAE-leverancier met TRN: 5% voorbelasting | verlegd: zelf aangeven en aftrekken (vak 3 en 10) | aftrekbaar |  | Overige bedrijfskosten | WBedKan |
| `Expenses:Telecom` | Mobiel en internet (e&, du); 5% voorbelasting op het zakelijke deel | 5% voorbelasting met TRN-factuur (vak 9) | aftrekbaar |  | Overige bedrijfskosten | WBedKan |
| `Expenses:Vennootschapsbelasting` | UAE vennootschapsbelasting over het boekjaar (bij SBR nihil) | geen btw-gevolg | niet-aftrekbaar |  | Belastinglast | WBel |
| `Expenses:Verzekering` | Zakelijke schadeverzekeringen (5% voorbelasting); levensverzekering vrijgesteld | 5% voorbelasting met TRN-factuur (vak 9) | aftrekbaar |  | Overige bedrijfskosten | WBedAlk |
| `Income:Koersresultaat` | Winst op valutawissels en herwaardering van EUR-saldi en -vorderingen | geen btw-gevolg | aftrekbaar |  | Financiële baten | WFbe |
| `Income:Omzet:Advies:Inclusionair` | Adviesdiensten aan Inclusionair (Nederlandse bv) | omzet 0%, export (vak 4) | aftrekbaar |  | Netto-omzet | WOmzNod |
| `Income:Omzet:Binnenland` | Omzet aan klanten in de UAE (5% btw, alleen na registratie) | omzet 5% UAE (vak 1) | aftrekbaar |  | Netto-omzet | WOmzNod |
| `Income:Omzet:Managementfee:Ekmekci` | Managementfee aan Ekmekci Group B.V. (EUR 7.716 per maand) | omzet 0%, export (vak 4) | aftrekbaar | related-party | Netto-omzet | WOmzNod |
| `Income:Omzet:Managementfee:MDI` | Fee aan MDI Consultants B.V. (leergang ABN AMRO) | omzet 0%, export (vak 4) | aftrekbaar | related-party | Netto-omzet | WOmzNod |
| `Income:Omzet:Managementfee:Point-Sixteen` | Fee aan Point Sixteen B.V. (vanaf besluit en managementovereenkomst) | omzet 0%, export (vak 4) | aftrekbaar | related-party | Netto-omzet | WOmzNod |
| `Income:Omzet:Overig` | Overige omzet; btw-behandeling per factuur | omzet 5% UAE (vak 1) | aftrekbaar |  | Netto-omzet | WOmzNod |
| `Income:Overig` | Overige baten (terugbetalingen e.d.) | geen btw-gevolg | aftrekbaar |  | Overige baten | WOvb |
| `Liabilities:Btw:Af-te-dragen` | Btw die XCL moet afdragen over binnenlandse omzet (VAT 201 vak 1); bij alleen export nihil | omzet 5% UAE (vak 1) |  |  | Belastingschuld | BSchBepBaf |
| `Liabilities:Btw:Verlegd` | Btw over buitenlandse diensten (software, AI, NL-advies) die XCL zelf aangeeft (VAT 201 vak 3) | verlegd: zelf aangeven en aftrekken (vak 3 en 10) |  |  | Belastingschuld (gesaldeerd met Assets:Btw:Voorbelasting-verlegd) | BSchBepBlw |
| `Liabilities:CT:Te-betalen` | Vennootschapsbelasting UAE over het boekjaar (bij Small Business Relief nihil) |  |  |  | Belastingschuld | BSchBep |
| `Liabilities:Crediteuren` | Ontvangen inkoopfacturen die nog betaald moeten worden |  |  |  | Handelsschulden | BSchCre |
| `Liabilities:Lening-aandeelhouder:Umar` | Lening van Umar privé aan XCL (o.a. EUR 25.000 op 26-1-2026), renteloos; voorwaarden schriftelijk vastleggen; eerst vaststellen welk deel kapitaalstorting is |  | marktwaarde-toets | connected-person | Schuld aan aandeelhouder | BLas |
| `Liabilities:Overlopend` | Kosten die bij de maand horen maar nog niet gefactureerd of betaald zijn |  |  |  | Overlopende passiva | BSchOpa |
| `Liabilities:Personeel:End-of-service` | Voorziening eindevergoeding (end of service gratuity): 21 dagen basisloon per dienstjaar in de eerste vijf jaar, berekend op het laatste basisloon |  | marktwaarde-toets | connected-person | Voorziening personeelsbeloningen | BVrz |
| `Liabilities:Personeel:Loonschuld-Umar` | Opgebouwd maar nog niet uitbetaald salaris van Umar (contractloon; schriftelijk uitgestelde betaling, route a) |  | marktwaarde-toets | connected-person | Schuld aan bestuurder | BSchOvs |
| `Liabilities:Personeel:Verlof` | Opgebouwde, nog niet opgenomen vakantiedagen (30 kalenderdagen per jaar) op het basisloon |  | aftrekbaar | connected-person | Personeelsverplichtingen (kortlopend) | BSchOvs |
| `Liabilities:Vooruitontvangen:Omzet` | Door klanten vooruitbetaald voor diensten die nog geleverd moeten worden (bijv. INV-0008 Inclusionair); in AED tegen de ontvangstkoers | geen btw-gevolg | nvt |  | Contractverplichting (vooruitontvangen omzet) | BSchVobVob |

## MZML HOLDING LIMITED

| Rekening | Wat het is | Btw | CT | Verbonden | Jaarrekening | RGS |
|---|---|---|---|---|---|---|
| `Assets:Deelnemingen:Ekmekci` | 75 aandelen Ekmekci Group B.V. (18,80%), gekocht 31-12-2025 tegen kostprijs |  | vrijgesteld | related-party | Financiële vaste activa, deelneming tegen kostprijs (Section 14.4(a) of Section 11, afhankelijk van invloed) | BFvaAnd |
| `Assets:Deelnemingen:Point-Sixteen` | 5.000 aandelen Point Sixteen B.V. (50%), gekocht 31-12-2025; joint venture tegen kostprijs |  | vrijgesteld | related-party | Financiële vaste activa, joint venture tegen kostprijs (Section 15.9(a)) | BFvaDio |
| `Assets:Deelnemingen:The-Ocean` | 720 aandelen The Ocean B.V. (30%), gekocht 31-12-2025; geassocieerde deelneming tegen kostprijs |  | vrijgesteld | related-party | Financiële vaste activa, geassocieerde deelneming tegen kostprijs (Section 14.4(a)) | BFvaAnd |
| `Assets:Nog-te-storten-kapitaal` | Aandelenkapitaal (AED 100.000) dat nog niet is gestort; RAK ICC vereist geen storting; in de jaarrekening in mindering op het eigen vermogen |  |  | connected-person | In mindering op eigen vermogen (IFRS for SMEs 22.7(a)) | BVorVao |
| `Assets:Rekening-courant:Umar` | Wat Umar privé heeft betaald voor MZML Ltd, of andersom |  | marktwaarde-toets | connected-person | Vordering op of schuld aan bestuurder | BVorOvr |
| `Assets:Te-ontvangen-dividend` | Vastgesteld maar nog niet ontvangen dividend van deelnemingen (bruto) |  |  | related-party | Vorderingen | BVorVop |
| `Assets:Waardevermindering:Ekmekci` | Bijzondere waardevermindering op de deelneming Ekmekci (tegenrekening, negatief saldo) |  |  |  | Financiële vaste activa (bijzondere waardevermindering) | BFvaAnd |
| `Assets:Waardevermindering:Point-Sixteen` | Bijzondere waardevermindering op de deelneming Point Sixteen |  |  |  | Financiële vaste activa (bijzondere waardevermindering) | BFvaDio |
| `Assets:Waardevermindering:The-Ocean` | Bijzondere waardevermindering op de deelneming The Ocean |  |  |  | Financiële vaste activa (bijzondere waardevermindering) | BFvaAnd |
| `Equity:Aandelenkapitaal` | Geplaatst kapitaal: 100 aandelen van AED 1.000 (register of members RAK ICC) |  |  |  | Aandelenkapitaal | BEivGok |
| `Equity:Kapitaalbijdrage` | Inbreng buiten aandelen om (bijv. het voordeel van een renteloze vendor loan als die tegen contante waarde wordt gewaardeerd) |  |  |  | Overige reserves (kapitaalbijdrage) | BEivAgi |
| `Equity:Openingsbalans` | Technische tegenrekening voor de openingsbalans |  |  |  | n.v.t. |  |
| `Equity:Resultaat` | Winst of verlies van afgesloten boekjaren |  |  |  | Overige reserves | BEivOvrAlr |
| `Expenses:Advies` | Fiscaal, juridisch en corporate-services advies | geen btw-gevolg | aftrekbaar |  | Overige bedrijfskosten | WBedAlk |
| `Expenses:Bank` | Bankkosten (vanaf opening rekening) | geen btw-gevolg | aftrekbaar |  | Financiële lasten | WBedAlk |
| `Expenses:Bronbelasting` | Ingehouden Nederlandse dividendbelasting die niet terug te krijgen is (verdragstarief NL-VAE, door Dinesh te bevestigen) | geen btw-gevolg | niet-aftrekbaar |  | Belastinglast | WBel |
| `Expenses:Koersverschil` | Koersverlies bij herwaardering van vendor loans en rekening-courant | geen btw-gevolg | aftrekbaar |  | Financiële lasten | WFbe |
| `Expenses:Onbekend` | Tijdelijk: nog te beoordelen (moet leeg zijn bij afsluiting) | geen btw-gevolg | nvt |  | n.v.t. |  |
| `Expenses:Oprichting` | Oprichtingskosten (eenmalig, boekjaar 1; IFRS for SMEs 18.15: niet activeren; NL kan activeren) | geen btw-gevolg | aftrekbaar |  | Overige bedrijfskosten (oprichtingskosten) | WBedAlk |
| `Expenses:Overheid:Certificaten` | Certificate of incumbency, good standing, CT-certificaat | geen btw-gevolg | aftrekbaar |  | Overige bedrijfskosten | WBedAlk |
| `Expenses:Overheid:RAK-ICC` | Jaarlijkse verlenging RAK ICC inclusief registered agent | geen btw-gevolg | aftrekbaar |  | Overige bedrijfskosten | WBedOrgHol |
| `Expenses:Rente:Vendor-loan` | Rente op de vendor loans aan MZML Holding B.V. (als afgesproken); specifieke renteaftrekbeperking, veilige haven als MZML B.V. in NL minimaal 9% betaalt | geen btw-gevolg | rente-art30-31 | related-party | Financiële lasten | WFbeRlsRil |
| `Expenses:Vennootschapsbelasting` | UAE vennootschapsbelasting (verwacht nihil) | geen btw-gevolg | niet-aftrekbaar |  | Belastinglast | WBel |
| `Expenses:Waardevermindering-deelnemingen` | Last uit bijzondere waardevermindering van een deelneming | geen btw-gevolg | vrijgesteld |  | Bijzondere waardeverminderingen | WFbe |
| `Income:Dividend` | Dividend van deelnemingen, bruto (deelnemingsvrijstelling CT geldt vanaf het eerste boekjaar als aan de voorwaarden is voldaan: minimaal 5%, 12 maanden houden of de intentie daartoe, minimaal 9% belasting bij de deelneming) | geen btw-gevolg | vrijgesteld | related-party | Opbrengst deelnemingen | WFbe |
| `Income:Koersresultaat` | Koerswinst bij herwaardering van vendor loans en rekening-courant (nooit op deelnemingen) | geen btw-gevolg | aftrekbaar |  | Financiële baten | WFbe |
| `Liabilities:CT:Te-betalen` | Vennootschapsbelasting UAE (verwacht nihil) |  |  |  | Belastingschuld | BSchBep |
| `Liabilities:Crediteuren` | Ontvangen facturen (RAK ICC, registered agent, adviseurs) die nog betaald moeten worden |  |  |  | Handelsschulden | BSchCre |
| `Liabilities:Overlopend` | Kosten die bij het boekjaar horen maar nog niet gefactureerd zijn (bijv. verlenging RAK ICC) |  |  |  | Overlopende passiva | BSchOpa |
| `Liabilities:Rekening-courant:MZML-BV` | Kosten van MZML Ltd die MZML Holding B.V. (NL) heeft voorgeschoten (oprichting, certificaten, RAK ICC) |  |  | related-party | Kortlopende schuld aan verbonden partij | BSchOvs |
| `Liabilities:Rekening-courant:XCL` | Kosten van MZML Ltd die XCL heeft voorgeschoten (af te wikkelen zodra er een bankrekening is; één financier is het doel) |  |  | related-party | Kortlopende schuld aan verbonden partij | BSchOvs |
| `Liabilities:Te-betalen-rente` | Opgelopen maar nog niet betaalde rente op de vendor loans (als rente is afgesproken) |  |  | related-party | Overlopende passiva | BSchOpa |
| `Liabilities:Vendor-loan:MZML-BV:Ekmekci` | Koopsom aandelen Ekmekci, schuldig gebleven aan MZML Holding B.V. (voorwaarden, looptijd en kortlopend deel: overeenkomst in Dropbox, nog in te zien) |  | rente-art30-31 | related-party | Langlopende schuld aan verbonden partij | BLas |
| `Liabilities:Vendor-loan:MZML-BV:Point-Sixteen` | Koopsom aandelen Point Sixteen, schuldig gebleven aan MZML Holding B.V. |  | rente-art30-31 | related-party | Langlopende schuld aan verbonden partij | BLas |
| `Liabilities:Vendor-loan:MZML-BV:The-Ocean` | Koopsom aandelen The Ocean, schuldig gebleven aan MZML Holding B.V. |  | rente-art30-31 | related-party | Langlopende schuld aan verbonden partij | BLas |
