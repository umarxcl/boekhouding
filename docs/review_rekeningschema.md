# Review rekeningschema XCL en MZML Holding Limited

Stand: 2 november 2026. Onafhankelijke review van `xcl/accounts.beancount` en `mzml_ltd/accounts.beancount`, met `opening.beancount` (beide), `docs/besluitenlog.md` en `importers/rules_xcl.yaml` als context. Er is niets gewijzigd in de bestaande bestanden; dit document is het enige resultaat.

Rol van de reviewer: accountant met NL- en UAE-praktijk, zonder betrokkenheid bij de opbouw. Toetsing tegen FTA (Corporate Tax en VAT), IFZA, IFRS for SMEs, UAE-arbeidsrecht en RGS.

**Beperkingen van deze review**

- Arbeidscontract, villacontract, vendor-loanovereenkomsten en SPA's zijn niet ingezien. Waar de uitkomst daarvan afhangt, staat dat erbij.
- Het officiële RGS-bestand (referentiegrootboekschema.nl) was vanuit deze omgeving niet te downloaden (proxy 403); twee pagina's van boekhoudplaza.nl werden geblokkeerd. RGS-codes zijn daarom gemarkeerd: **[b]** = bevestigd in een geraadpleegde bron, **[v]** = uit vakkennis, te verifiëren tegen het officiële RGS 3.7/3.8-bestand vóór gebruik.
- De regelnamen van het CT-accounting schedule komen uit de FTA-returnhandleiding zoals ik die ken; de geraadpleegde secundaire bronnen bevestigen de opbouw maar niet elke regel letterlijk. Controleer de exacte labels eenmalig in EmaraTax.

---

## Samenvatting in tien punten

1. Het schema is netjes, consistent en goed uitgelegd, maar het is gebouwd als **boekhoudschema**, niet als **aangifteschema**. Voor btw en CT ontbreekt de laag die van rekening naar aangifterubriek leidt.
2. De btw-codes sluiten **niet** aan op de VAT 201. "geen-aftrek" gooit vier verschillende situaties op één hoop (geblokkeerd, vrijgesteld, buitenland, geen TRN-factuur) en **reverse charge ontbreekt volledig**, terwijl XCL na registratie op elk software-, AI- en NL-adviesabonnement art. 48 moet toepassen (VAT 201 vak 3 en vak 10).
3. Minstens zes btw-codes zijn inhoudelijk onjuist: autohuur (geblokkeerd, art. 53 UR), taxi/metro (vrijgesteld), bankkosten Wio (5%, Wio stuurt zelf een btw-factuur), FTA-certificaten (overheidsheffing), zakelijke verzekering (5%), buitenlands advies (verlegd, niet 5%).
4. **Valuta-opzet is een IFRS-fout in wording**: opbrengst- en kostenrekeningen staan in EUR, deelnemingen in EUR. Resultaatposten horen in de functionele valuta tegen de koers van de transactiedatum; deelnemingen tegen kostprijs zijn niet-monetair en mogen niet mee herwaarderen.
5. **Verbonden partijen** zijn te smal gedefinieerd. Niet alleen Point Sixteen: ook MDI (gemeenschappelijke zeggenschap) en vrijwel zeker Ekmekci (bestuur via MZML Ltd na de bestuurswissel) zijn related parties in de zin van art. 35 CT-wet. Umar zelf is connected person (art. 36).
6. Alle zes door de bouwer genoemde gaten zijn terecht. Er komen er negen bij: verlofverplichting, waarborgsommen, CT-last in de P&L, kapitaalbijdrage in het eigen vermogen, bijzondere waardevermindering deelnemingen, NL-dividendbelasting, crediteuren en overlopende passiva bij MZML Ltd, binnenlandse omzet (5%) bij XCL, en het splitsen van representatie voor de 50%-regel.
7. **SBR is verlengd** tot boekjaren die eindigen op of vóór 31-12-2029 (Ministerial Decision 131 van 2026, volgens berichtgeving augustus 2026). Dat verandert de afweging rond route a: een verlies in een SBR-jaar gaat verloren.
8. **Route a (loon AED 40.000 opbouwen, deels niet betalen)** is boekhoudkundig verdedigbaar maar arbeidsrechtelijk kwetsbaar (loon moet maandelijks worden betaald; inhoudingen zijn wettelijk beperkt) en de besluitenlog spreekt zichzelf tegen over het loon vanaf 25-10-2026.
9. **Koersbron**: voor btw schrijft art. 69 btw-wet de koers van de Centrale Bank (CBUAE) op de leveringsdatum voor. "ECB met bron" is daarvoor niet voldoende.
10. **IFZA**: de vereenvoudigde jaarrekening bij verlenging is op **kasbasis** en in het verplichte IFZA-sjabloon. Het grootboek moet dus naast accrual ook een kasbasisoverzicht kunnen leveren. Let op de timing: de licentie verlengt rond 15-12-2026, vóór het einde van het eerste boekjaar.

---

## A. Oordeel per toetsingspunt

### A1. UAE Corporate Tax-aangifte

**Wat de aangifte vraagt.** De CT-aangifte bestaat uit: gegevens belastingplichtige, keuzes (o.a. SBR, realisatiebasis, overgangsregels), een accounting schedule (winst-en-verliesrekening en balans uit de jaarrekening), correcties en vrijgestelde inkomsten (o.a. dividend en deelnemingsvrijstelling per deelneming), overige correcties (niet-aftrekbare kosten waaronder entertainment, giften aan niet-gekwalificeerde instellingen, niet-aftrekbare rente, transfer-pricingcorrecties), schedules voor renteaftrekbeperking, en schedules voor transacties met related parties en connected persons ([PwC, CT Returns Guide](https://www.pwc.com/m1/en/services/tax/middle-east-tax-news-alerts/2024/uae-corporate-tax-returns-guide.html)). De TP-disclosure geldt boven AED 40 mln aan related-partytransacties, en voor connected persons zodra aan één connected person meer dan AED 500.000 aan betalingen of voordelen is verstrekt (zelfde bron).

**Relevante materiële regels.**
- Entertainment voor klanten, aandeelhouders, leveranciers en zakenpartners: 50% niet aftrekbaar (art. 32 CT-wet; [Alpha Partners](https://www.alphapartners.co/blog/uae-corporate-tax-list-of-non-deductible-expenses-explained)).
- Boetes (ook verkeersboetes) en giften aan niet-gekwalificeerde instellingen: niet aftrekbaar (art. 33; [Fidinam](https://www.fidinam.com/en/blog/tax-motor-vehicle-expenditure-uae), Alpha Partners).
- Betalingen aan connected persons (eigenaar, bestuurder, officer) alleen aftrekbaar voor zover marktconform en volledig zakelijk (art. 36); FTA-verduidelijking CTP010 (april 2026) over wie director/officer is ([Grant Thornton](https://www.grantthornton.ae/insights/alerts/tax-alert-fta-clarifies-director-and-officer-under-article-36/)). Umar is enig aandeelhouder én manager: connected person zonder twijfel.
- Specifieke renteaftrekbeperking: rente op leningen van related parties om een belang in een related party te verwerven is niet aftrekbaar, tenzij het geen belastingvoordeel oplevert; geen voordeel wordt aangenomen als de geldgever minimaal 9% belasting betaalt ([Deloitte](https://www.deloitte.com/middle-east/en/services/tax/perspectives/interest-deduction-limitation-rules-guide.html)). Dit raakt de vendor loans van MZML Ltd direct.
- SBR: bij keuze wordt het belastbaar inkomen op nul gesteld, alleen de omzet moet worden aangegeven; TP-documentatie is niet verplicht maar het arm's-lengthbeginsel blijft gelden; **fiscale verliezen van een SBR-jaar kunnen niet worden gebruikt of voortgewenteld** ([BCL](https://bcl.ae/blogs/small-business-relief-uae-tax-return-guide/)). SBR is verlengd tot boekjaren eindigend op of vóór 31-12-2029 ([Osome](https://osome.com/ae/blog/small-business-relief-extended-2029/); [Entrepreneur Middle East](https://mena.entrepreneur.com/business-news/uae-extends-small-business-tax-relief-through-2029)); verifieer de tekst van MD 131/2026 op mof.gov.ae.

**Kan het schema dit leveren?** Voor 2026 met SBR: ja, want alleen de omzet is nodig. Voor elke aangifte zonder SBR (bewuste keuze om het verlies van 2026 veilig te stellen, omzet boven AED 3 mln, of na 2029): **nee, onvoldoende**.

| CT-rubriek | Huidig schema | Oordeel |
|---|---|---|
| Operating revenue | `Income:Omzet:*` | Voldoende; wel in AED vastleggen (zie A3) |
| Salaries, wages and related charges | `Expenses:Personeel:*` | Voldoende, mits verlof en EOSG goed geboekt |
| Depreciation and amortisation | ontbreekt | **Gat**: geen vaste activa, geen afschrijving |
| Fines and penalties | `Expenses:Overheid:Boetes` | Goed |
| Donations, grants and gifts | ontbreekt | Klein gat (alleen nodig als XCL ooit doneert) |
| Client entertainment (50%) | `Expenses:Representatie` mengt klant, personeel en geschenken | **Gat**: splitsen |
| Interest income/expenditure | XCL: geen; MZML Ltd: `Expenses:Rente:Vendor-loan` | MZML Ltd: markeren voor art. 31 |
| Net FX gains/losses | `Income:Koersresultaat`, `Expenses:Koersverschil` | Goed |
| Dividends received / participation exemption | MZML Ltd `Income:Dividend` | Goed, maar bronbelasting en waardevermindering ontbreken |
| Income tax expense | alleen balansrekening `Liabilities:CT:Te-betalen` | **Gat**: P&L-rekening ontbreekt |
| Related party / connected person schedule | geen markering | **Gat**: metadata `verbonden:` nodig |
| Balans (PPE, financial assets, current/non-current) | grotendeels | Gat bij vaste activa en lening aandeelhouder |

Conclusie A1: **onvoldoende voor een volledige aangifte; voldoende voor SBR 2026**. Oplossing: per rekening metadata `ct:` (fiscale behandeling) en `verbonden:` (art. 35/36), plus de rekeningen in deel B.

### A2. UAE VAT 201

**Rubrieken.** Vak 1 standaardtarief per emiraat (1b Dubai), vak 2 toeristenrestitutie, vak 3 leveringen onder reverse charge (o.a. geïmporteerde diensten), vak 4 nultarief, vak 5 vrijgesteld, vak 6 en 7 invoer van goederen, vak 9 aftrekbare voorbelasting (standard rated expenses), vak 10 aftrek van de verlegde btw uit vak 3, 6 en 7, vak 11 tot en met 14 totalen ([Business Dubai, VAT 201 per vak](https://www.businessdubai.ae/blogs/uae-vat-return-filing)). Het weglaten van een reverse-chargepost is een fout, ook als het netto-effect nul is (zelfde bron).

**Reverse charge (art. 48 btw-wet).** Een geregistreerde ondernemer die diensten afneemt van een leverancier zonder vestiging in de UAE berekent zelf 5% (vak 3) en trekt die bij volledige aftrek direct weer af (vak 10). Vanaf 1-1-2026 hoeft daarvoor geen self-invoice meer te worden opgemaakt; de leveranciersfactuur volstaat als bewijs ([ClearTax, wijzigingen 2026](https://www.cleartax.com/ae/new-vat-rules-uae-2026)). Voor XCL betreft dit na registratie: Anthropic, OpenAI, Fireflies, xAI, Dropbox, Figma, Netlify, TransIP, Fiskl, LinkedIn, Microsoft, Google (tenzij de leverancier na opgave van de TRN alsnog UAE-btw rekent), en NL-adviseurs (Newings, Lemon & Lemon). Geïmporteerde diensten tellen bovendien mee voor de registratiedrempel van AED 375.000, net als nultariefomzet ([Hawksford](https://www.hawksford.com/insights-and-guides/vat-registration-uae)).

**Geblokkeerde voorbelasting (art. 53 Uitvoeringsregeling).** Entertainment (ook voor eigen personeel, op enkele uitzonderingen na) en motorvoertuigen die beschikbaar zijn voor privégebruik; het criterium is beschikbaarheid, niet feitelijk gebruik (Business Dubai).

**Aansluiting huidige btw-codes.**

| Huidige code | Probleem |
|---|---|
| `0-export` | Goed voor NL-klanten (vak 4), maar ook gezet op `Income:Omzet:Overig`, waar een UAE-klant 5% (vak 1b) zou zijn |
| `5-voorbelasting` | Gezet op rekeningen waar geen of geblokkeerde btw speelt (autohuur, taxi, FTA-certificaten, NL-advies in EUR) |
| `geen-aftrek` | Vier situaties door elkaar: geblokkeerd (representatie), vrijgesteld (woninghuur), verlegd (software, AI), buitenland (NL-hotel). Voor de VAT 201 moet dat onderscheid er zijn |
| `nvt` | Ook op bankkosten Wio, terwijl Wio maandelijks een btw-factuur stuurt (expliciete fees zijn 5%) |
| ontbreekt | Reverse charge (vak 3 en 10), vrijgestelde inkoop, buiten reikwijdte (overheid), binnenlandse omzet 5% |

**Registratiedatum.** De codes beschrijven de behandeling ná registratie. Vóór de registratiedatum is alle btw kostprijs en is er geen reverse charge. Omdat de FTA bij een (late) verplichte registratie een registratiedatum met terugwerkende kracht vaststelt, moet de importer de btw-status per boeking op datum kunnen omzetten. Dat hoort niet in het rekeningschema maar in de importer (metadata per posting).

**Koers.** Bedragen in vreemde valuta moeten voor btw worden omgerekend tegen de door de CBUAE gepubliceerde koers op de leveringsdatum (art. 69 btw-wet; FTA VATP004), ook voor reverse charge ([EY](https://globaltaxnews.ey.com/news/2018-5894-uae-publishes-public-clarification-on-use-of-exchange-rates-for-vat-purposes)).

Conclusie A2: **onvoldoende**. Nieuwe codeset in B2, twee nieuwe btw-rekeningen in B3.

### A3. IFZA-jaarrekening en IFRS for SMEs

**IFZA.** Sinds 30-9-2025 moet elke IFZA-licentiehouder bij verlenging een jaarrekening indienen over het laatst afgesloten boekjaar. Vereenvoudigd mag bij omzet tot en met AED 3 mln én maximaal 9 werknemers; dan op **kasbasis** en uitsluitend in het **IFZA-sjabloon**; ondertekend door manager, director of aandeelhouder. Daarboven een gecontroleerde jaarrekening ([IFZA FAQ](https://cdn.ifza.com/marketing/FAQs%20Update_.pdf); [Uniwide](https://www.uniwide.com/ifza-requires-submission-of-financial-statements-for-license-renewal/)). XCL valt in de vereenvoudigde route. Gevolgen:

- Het schema moet een kasbasisoverzicht kunnen afleiden (ontvangsten en uitgaven per categorie uit de bankrekeningen). In Beancount kan dat door alleen transacties met een `Assets:Bank:*`-posting te rapporteren; vooruitbetalingen, voorzieningen en loonschuld vallen er dan vanzelf uit. Dit vraagt geen extra rekeningen, wel een rapport.
- Timing: de licentie (15-12-2025 tot en met 14-12-2026) verlengt vóór het einde van het eerste boekjaar (31-12-2026). Er is dan nog geen "afgesloten boekjaar". Vraag IFZA of RD Advisory nu al wat bij deze verlenging wordt verwacht.
- Het sjabloon zelf kon ik niet inzien (alleen als link in de FAQ). Haal het op en leg de regels naast `ifrs:`.

**IFRS for SMEs (editie 2015 voor boekjaar 2026; de derde editie geldt vanaf boekjaren die op of na 1-1-2027 beginnen).**

| Onderwerp | Bevinding |
|---|---|
| Niet-gestort kapitaal | IFRS for SMEs 22.7(a): bij uitgifte vóór ontvangst van het geld wordt de vordering **in mindering op het eigen vermogen** gepresenteerd, niet als actief ([IFRS Foundation, AP30C](https://www.ifrs.org/content/dam/ifrs/meetings/2023/december/iasb/ap30c-requirement-to-offset-equity-instruments.pdf)). `Assets:Nog-te-storten-kapitaal` mag blijven als boekhoudrekening, maar het `ifrs:`-label moet dat zeggen. Bij beide entiteiten |
| End of service gratuity | 21 dagen **basisloon** per jaar in de eerste vijf jaar (art. 51 lid 2 FDL 33/2021), berekend op het **laatste** basisloon (art. 51 lid 5) ([Khaleej Times](https://www.khaleejtimes.com/uae/legal/uae-how-is-gratuity-calculated-if-salary-changes-during-course-of-service)). Opbouw vanaf dag één, ook vóór het recht na een jaar onvoorwaardelijk wordt; toelagen tellen niet mee ([auditfirmsdubai](https://auditfirmsdubai.ae/en/resources/blog/end-of-service-gratuity-provision-uae)). IFRS for SMEs 28.19 staat de vereenvoudigde berekening toe (alsof de werknemer op balansdatum vertrekt). Rekening is aanwezig; de waardering moet bij elke afsluiting opnieuw op het dan geldende basisloon (bij AED 22.000 i.p.v. 40.000 daalt de voorziening). Het basisloon staat in het contract; dat heb ik niet gezien |
| Verlofverplichting | Ontbreekt. Opgebouwde niet-opgenomen vakantiedagen (30 kalenderdagen per jaar) zijn een kortlopende personeelsverplichting (Section 28.6) |
| Loon in natura woning | Goed als personeelskosten (Section 28) met vooruitbetaling als overlopend actief. Huurovereenkomst villa: operationele lease, lineair (Section 20) |
| Vooruitontvangen omzet | Ontbreekt (bekend gat). Contractverplichting volgens Section 23; INV-0008 Inclusionair. **Niet-monetair**: vastleggen in AED tegen de ontvangstkoers, niet herwaarderen |
| Vaste activa | Ontbreekt (bekend gat). Section 17: kostprijs min cumulatieve afschrijving, aparte rekeningen voor beide |
| Deelnemingen MZML Ltd | Kostprijsmodel is toegestaan voor geassocieerde deelnemingen (Section 14.4(a)) en joint ventures (Section 15.9(a)), mits voor alle deelnemingen van die soort dezelfde grondslag. P16 (50%, gezamenlijke zeggenschap met Moesker Beheer): joint venture. The Ocean (30%): geassocieerd. Ekmekci (18,80%): onder 20%, dus alleen geassocieerd als er invloed van betekenis is (bestuur via MZML Ltd na de bestuurswissel geeft die); zo niet, dan Section 11 en moet reële waarde worden gebruikt als die betrouwbaar te bepalen is (de Newings-waardering suggereert dat). Classificatie per deelneming vastleggen. Bijzondere waardevermindering (Section 27) heeft geen rekening |
| Valuta (Section 30) | Resultaatposten horen in de functionele valuta tegen de koers op de transactiedatum. Nu staan `Income:Omzet:Managementfee:*`, diverse `Expenses:*` en `Equity:Resultaat` ook in EUR. Gevolg: rapportage in AED rekent met één koers om, niet met de transactiekoers. Monetaire posten (bank, debiteuren, crediteuren, leningen) in EUR zijn prima en worden geherwaardeerd; niet-monetaire posten (deelnemingen, vooruitbetaald, vooruitontvangen) niet |
| Functionele valuta MZML Ltd | Alle activa en passiva van MZML Ltd zijn in EUR. Met AED als functionele valuta ontstaat jaarlijks een koersresultaat op de vendor loans zonder tegenhanger (de deelnemingen worden niet geherwaardeerd). Overweeg EUR als functionele valuta (Section 30.2 tot 30.5) met AED als presentatievaluta; leg de keuze vast. Dit is een grondslagkeuze, geen schemakwestie, maar bepaalt welke rekeningen in welke valuta staan |
| CT-last | P&L-rekening ontbreekt; latente belastingen (Section 29) pas relevant na SBR |

Conclusie A3: **op hoofdlijnen goed, met vier materiële gaten** (valuta, verlof, vaste activa, vooruitontvangen) en twee presentatiepunten (niet-gestort kapitaal, waardevermindering deelnemingen).

### A4. RGS 3.x en vergelijkbaarheid met de NL-administraties

De opbouw (kostensoorten, balans naar liquiditeit) volgt al grotendeels de RGS-logica. Afwijkingen die vóór januari 2027 opgelost moeten worden:

1. **Omslagrekeningen.** RGS werkt met omslagcodes voor rekeningen die van debet naar credit kunnen wisselen (rekening-courant, btw). `Assets:Rekening-courant:Umar` en de btw-rekeningen hebben dat nodig: metadata `rgs:` (debetsaldo) en `rgs-omslag:` (creditsaldo).
2. **Vaste activa per mutatiesoort.** RGS splitst kostprijs en cumulatieve afschrijving (en op niveau 5 beginbalans, investeringen, afschrijvingen). Beancount kan dat met twee rekeningen per activagroep.
3. **Verbonden partijen apart.** RGS onderscheidt vorderingen en schulden op groepsmaatschappijen (BVorVog/BFvaVog), overige verbonden maatschappijen (BVorVov/BFvaVov) en participanten/deelnemingen (BVorVop/BFvaVop) [b]. Het schema zet nu alle debiteuren onder één noemer.
4. **Btw per soort.** RGS kent aparte codes voor btw hoog/laag/overig, verlegd, en afdracht (BSchBepBla, BSchBepBlo, BSchBepBlw, BSchBepBaf) [b]. De UAE-btw past daar goed in: 5% op BSchBepBlo, verlegd op BSchBepBlw.
5. **Grondslagverschillen NL GAAP en IFRS for SMEs** die RGS niet oplost en die in een gezamenlijke rapportage zichtbaar moeten blijven: niet-gestort kapitaal (NL: vordering BVorVao [b]; IFRS for SMEs: minpost eigen vermogen), deelnemingen met invloed van betekenis (NL: nettovermogenswaarde, art. 2:389 BW; IFRS for SMEs: kostprijs toegestaan), oprichtingskosten (NL: activeren mogelijk, BIvaKou [b]; IFRS: altijd last).
6. **Loon in natura.** In RGS horen woning en auto ter beschikking aan een werknemer bij de loonkosten (WPer), niet bij huisvesting (WBedHui) of autokosten (WBedAut). Het schema doet dat voor de woning goed, voor de auto niet (zie C4).
7. **Holdingkosten.** RGS heeft een eigen code voor holdingkosten (WBedOrgHol) [b]; bruikbaar voor de RAK ICC-kosten van MZML Ltd en later MZML Holding B.V.

**Mapping per hoofdgroep** (per rekening in B5):

| Hoofdgroep schema | RGS niveau 2/3 | Status |
|---|---|---|
| `Assets:Bank` | BLimBan | [b] |
| `Assets:Vaste-activa` (nieuw) | BMvaBei (inventaris), BMvaObe (andere vaste bedrijfsmiddelen) | [b] |
| `Assets:Deelnemingen` (MZML Ltd) | BFvaDio, BFvaAnd; Ekmekci zonder invloed: BFvaOve | [b] codes; keuze per deelneming [v] |
| `Assets:Waarborgsommen` (nieuw) | BFvaOvr (langlopend) | [b] |
| `Assets:Debiteuren` derden | BVorDeb | [b] |
| `Assets:Debiteuren` verbonden | BVorVov | [b] code; NL-classificatie met Hans afstemmen [v] |
| `Assets:Vooruitbetaald` | BVorOva | [b] |
| `Assets:Rekening-courant` | BVorOvr (Umar), BVorVov (MZML Ltd/XCL); omslag naar BSchOvs resp. schulden verbonden | [b] niveau 3; niveau 4 [v] |
| `Assets:Nog-te-storten-kapitaal` | BVorVao | [b] |
| `Assets:Btw` | BVorVbk | [b] |
| `Liabilities:Crediteuren` | BSchCre | [b] |
| `Liabilities:Vooruitontvangen` (nieuw) | BSchVobVob | [b] |
| `Liabilities:Btw` | BSchBepBlo, BSchBepBlw, BSchBepBaf | [b] |
| `Liabilities:CT` | BSchBep, niveau 4 vennootschapsbelasting | [v] |
| `Liabilities:Overlopend` | BSchOpa | [b] |
| `Liabilities:Personeel:Loonschuld` en `:Verlof` | BSchOvs of BSchSal, niveau 4 | [v] |
| `Liabilities:Personeel:End-of-service` | BVrz, niveau 3 overige voorzieningen (pensioenachtig: BVrzVvp) | [v] |
| `Liabilities:Lening-aandeelhouder`, `Liabilities:Vendor-loan` | BLas, niveau 3 schulden aan aandeelhouders resp. verbonden maatschappijen; kortlopend deel BSch | [v] |
| `Equity:Aandelenkapitaal` | BEivGok | [v] |
| `Equity:Resultaat` | BEivOvr (BEivOvrAlr) | [b] |
| `Equity:Kapitaalbijdrage` (nieuw) | BEivAgi | [v] |
| `Income:Omzet` | WOmzNod (diensten); niveau 4 naar land | [b] niveau 3 |
| `Income:Overig` | WOvb | [b] |
| `Income:Koersresultaat`, `Expenses:Koersverschil` | WFbe, niveau 3 koersverschillen | [v] |
| `Income:Dividend` (MZML Ltd) | WFbe of resultaat deelnemingen | [v] |
| `Expenses:Personeel` loon en natura | WPerLes | [v] |
| `Expenses:Personeel` overig (visa, opleiding) | WBedOvp | [b] |
| `Expenses:Afschrijvingen` (nieuw) | WAfs | [b] niveau 2 |
| `Expenses:Auto` | WBedAut | [b] |
| `Expenses:Reis`, `Expenses:Representatie`, `Expenses:Marketing` | WBedVkk (relatiegeschenken WBedVkkRel) | [b] niveau 3 |
| `Expenses:Telecom`, `Expenses:Software`, `Expenses:Kantoor` | WBedKan | [b] niveau 3 |
| `Expenses:Overheid`, `Expenses:Advies`, `Expenses:Verzekering` | WBedAlk (algemene kosten); RAK ICC: WBedOrgHol | [b] WBedOrgHol; WBedAlk [v] |
| `Expenses:Bank` | WBedAlk of WFbe | [v] |
| `Expenses:Rente` (MZML Ltd) | WFbeRlsRil (rente lening verbonden) | [b] |
| `Expenses:Vennootschapsbelasting` (nieuw) | WBel | [v] |

Bronnen RGS: [boekhoudplaza, RGS balanscodes](https://www.boekhoudplaza.nl/rgs_rekeningen/B&KB=B/Balans.htm); [boekhoudplaza, RGS MKB 3.5.1 voorstel](https://www.boekhoudplaza.nl/upload/boekhoudplaza/rgs/versie351/RGS%20MKB%20versie%203.5.1_Voorstel_V1.pdf); [boekhoudplaza, conversie 3.3 naar 3.4](https://boekhoudplaza.nl/upload/boekhoudplaza/rgs/versie34/20220222_Verslag%20boekhoudplaza%20conversie%203.3%20naar%203.4.pdf); [referentiegrootboekschema.nl](https://www.referentiegrootboekschema.nl/) (3.9 in bèta). Aanbeveling: download het officiële RGS-bestand (de versie die AFAS/Hans voor 2027 gebruikt) in Drive, en laat `scripts/check.sh` elk `rgs:`-veld daartegen valideren. Codes met [v] pas daarna invullen.

Conclusie A4: **goed vertrekpunt, mapping uitvoerbaar**, met de zeven bovengenoemde aandachtspunten.

### A5. Vergelijking met gangbare UAE-rekeningschema's

Gangbare UAE-schema's voor kleine vennootschappen bevatten naast het standaardwerk vaste posten voor input VAT en output VAT, accrued expenses, een voorziening end of service benefits, share capital, retained earnings en owner's drawings ([Tally, UAE CoA-template](https://tallysolutions.com/mena/uae-vat/setting-up-a-chart-of-accounts-for-uae-trading-company-practical-template/)). Bij consultancy-FZCO's en holdings zie je in de praktijk ook: leave salary provision, air ticket provision (alleen als het contract een jaarlijks ticket geeft), security deposits, advances from customers, due to/from related parties per partij, shareholder current account, VAT reverse charge payable/receivable, corporate tax payable en expense, en bij holdings investment in associates/JV met impairment.

| Wat | Status in dit schema |
|---|---|
| Input/output VAT | Aanwezig; reverse charge ontbreekt |
| Accrued expenses | Aanwezig (XCL); ontbreekt bij MZML Ltd |
| EOSB provision | Aanwezig (XCL) |
| Leave salary provision | Ontbreekt |
| Air ticket provision | Alleen nodig als het contract een ticket geeft; niet beoordeeld |
| Security deposits | Ontbreekt (villa, huurauto) |
| Advances from customers | Ontbreekt |
| Related parties per partij | Deels (rekening-courant MZML Ltd); debiteuren niet gemarkeerd |
| Shareholder current account | Aanwezig als `Rekening-courant:Umar`. Let op: in de UAE wordt dit vaak in het eigen vermogen gepresenteerd; onder IFRS is het een vordering of schuld. Het schema doet het goed |
| Shareholder loan | Ontbreekt (EUR 25.000) |
| Fixed assets en depreciation | Ontbreekt |
| CT payable en expense | Alleen payable |
| Holding: impairment, WHT | Ontbreekt |

**Overbodig of samen te voegen.** Weinig. `Assets:Bank:Nog-te-openen` (MZML Ltd) is overbodig: open de bankrekening in het schema op de werkelijke openingsdatum. `Expenses:Bank:Wisselkosten` en `Expenses:Bank:Kosten` kunnen blijven (beide 5%, zie B5), maar hebben dezelfde behandeling. `Expenses:Personeel:Huisvesting` en `:Huisvesting-nuts` **niet** samenvoegen: de btw-behandeling verschilt (huur vrijgesteld, SEWA 5% geblokkeerd). De fijnmazige omzetrekeningen per klant zijn nuttig voor de related-partyschedules; houden.

Conclusie A5: **completer dan een gemiddeld startschema op naamgeving en uitleg, minder compleet op de standaard UAE-posten** (verlof, borg, vooruitontvangen, reverse charge, CT-last).

---

## B. Concrete wijzigingen

### B1. Structurele afspraken (metadata en valuta)

1. **Nieuwe metadatavelden** op elke rekening:
   - `rgs:` RGS-referentiecode (en `rgs-omslag:` waar het saldo kan omslaan).
   - `ct:` fiscale behandeling: `aftrekbaar`, `50-niet-aftrekbaar` (art. 32), `niet-aftrekbaar` (art. 33), `marktwaarde-toets` (art. 36), `vrijgesteld` (art. 22/23), `rente-art30-31`, `nvt`.
   - `verbonden:` `related-party` (art. 35), `connected-person` (art. 36) of weglaten.
   - `btw:` met de nieuwe codeset uit B2; per boeking overschrijfbaar met dezelfde sleutel op de posting (bijvoorbeeld Google rekent na TRN-opgave toch 5%: dan `5-voorbelasting` in plaats van `verlegd`).
   - `scripts/rekeningschema_md.py` uitbreiden met deze velden; `BTW`-woordenboek vervangen door de codeset uit B2.
2. **Valutaregel**: `Income:*`, `Expenses:*` en `Equity:*` alleen in AED (XCL; MZML Ltd: AED of EUR afhankelijk van de functionele-valutakeuze). Een EUR-factuur boek je als `Assets:Debiteuren:Ekmekci 7716.00 EUR @ <CBUAE-koers> AED` tegen `Income:Omzet:Managementfee:Ekmekci` in AED. Herwaardering alleen op monetaire balansrekeningen.
3. **Niet-monetaire EUR-posten tegen historische kostprijs** (deelnemingen MZML Ltd): vastleggen als `165743.00 EUR {<koers 31-12-2025> AED}` met de vendor loan als `-165743.00 EUR @ <koers> AED`, zodat `cost()` de historische AED-waarde geeft en een prijswijziging de deelneming niet raakt. Dit vraagt een aanpassing van `mzml_ltd/opening.beancount` door de bouwer (niet door mij gedaan).
4. **leafonly**: rekeningen die een onderverdeling krijgen (`Expenses:Representatie`, `Expenses:Personeel:Visa-medisch`) hernoemen zolang er nog geen boekingen op staan; anders breekt de plugin.

### B2. Nieuwe btw-codeset (vervangt de huidige vier)

| Code | Betekenis | VAT 201 | Grondslag |
|---|---|---|---|
| `0-export` | Export van diensten aan afnemer buiten de UAE | vak 4 | art. 31 UR |
| `5-binnenland` | Omzet aan UAE-afnemer, 5% | vak 1b (Dubai) | art. 2 btw-wet |
| `5-voorbelasting` | UAE-kosten met TRN-factuur, aftrekbaar | vak 9 | art. 54 btw-wet |
| `verlegd` | Dienst van buitenlandse leverancier: 5% zelf berekenen en aftrekken | vak 3 en vak 10 | art. 48 btw-wet |
| `geblokkeerd` | Btw op factuur, niet aftrekbaar (entertainment, auto beschikbaar voor privé, privévoorzieningen personeel) | geen | art. 53 UR |
| `vrijgesteld` | Vrijgestelde inkoop zonder btw (woninghuur, lokaal personenvervoer, levensverzekering, financiële diensten op marge) | geen | art. 46 btw-wet |
| `buiten-reikwijdte` | Overheidsheffingen zonder btw (visum, Emirates ID, Salik, RTA-parkeren, FTA-certificaten) | geen | |
| `0-inkoop` | Nultarief-inkoop (internationale vluchten) | geen | |
| `buitenland` | Kosten die in het buitenland zijn verbruikt (hotel NL), geen UAE-btw en geen verlegging | geen | plaats van levering buiten UAE |
| `nvt` | Geen btw-gevolg (lonen, voorzieningen, interne boekingen, koersverschillen) | geen | |

Regel in de importer, niet in het schema: vóór de registratiedatum wordt elke code behalve `0-export`/`5-binnenland` behandeld als "kostprijs, geen aangifte"; vanaf de registratiedatum gelden de codes. Omzet met `0-export` telt ook vóór registratie mee voor de drempel, net als `verlegd`-inkoop.

### B3. Toe te voegen rekeningen XCL

```beancount
; --- Vaste activa
2025-12-15 open Assets:Vaste-activa:Inventaris:Kostprijs    AED
  nl: "Aanschafprijs van laptop, telefoon en andere apparatuur vanaf de activeringsgrens (voorstel AED 2.500 per stuk)"
  btw: "5-voorbelasting"
  ifrs: "Materiële vaste activa"
  ct: "aftrekbaar"
  rgs: "BMvaBei"

2025-12-15 open Assets:Vaste-activa:Inventaris:Afschrijving AED
  nl: "Opgebouwde afschrijving op de apparatuur (lineair; voorstel 3 jaar laptop, 2 jaar telefoon)"
  btw: "nvt"
  ifrs: "Materiële vaste activa (cumulatieve afschrijving)"
  ct: "aftrekbaar"
  rgs: "BMvaBei"

2025-12-15 open Assets:Waarborgsommen                       AED
  nl: "Borg villa Sharjah en huurauto; terug te ontvangen bij einde huur"
  btw: "nvt"
  ifrs: "Overige vorderingen"
  ct: "nvt"
  rgs: "BFvaOvr"

2025-12-15 open Assets:Kruisposten                          AED,EUR
  nl: "Geld onderweg tussen eigen rekeningen (bijv. ING naar Wio); moet bij maandafsluiting nul zijn"
  btw: "nvt"
  ifrs: "n.v.t."
  rgs: "BVorTus"
  rgs-omslag: "BSchTus"

2025-12-15 open Assets:Btw:Voorbelasting-verlegd            AED
  nl: "Btw die XCL over buitenlandse diensten zelf berekent en tegelijk aftrekt (VAT 201 vak 10)"
  btw: "verlegd"
  ifrs: "Belastingvordering (gesaldeerd met Liabilities:Btw:Verlegd)"
  rgs: "BVorVbk"

; --- Passiva
2025-12-15 open Liabilities:Btw:Verlegd                     AED
  nl: "Btw over buitenlandse diensten (software, AI, NL-advies) die XCL zelf aangeeft (VAT 201 vak 3)"
  btw: "verlegd"
  ifrs: "Belastingschuld (gesaldeerd met Assets:Btw:Voorbelasting-verlegd)"
  rgs: "BSchBepBlw"

2025-12-15 open Liabilities:Vooruitontvangen:Omzet          AED
  nl: "Door klanten vooruitbetaald voor diensten die nog geleverd moeten worden (bijv. INV-0008 Inclusionair); in AED tegen de ontvangstkoers, niet herwaarderen"
  btw: "nvt"
  ifrs: "Contractverplichting (vooruitontvangen omzet)"
  ct: "nvt"
  rgs: "BSchVobVob"

2025-12-15 open Liabilities:Lening-aandeelhouder:Umar       EUR
  nl: "Lening van Umar privé aan XCL (EUR 25.000 op 26-1-2026), renteloos; voorwaarden schriftelijk vastleggen"
  btw: "nvt"
  ifrs: "Schuld aan aandeelhouder (kort- of langlopend volgens de leningsvoorwaarden)"
  ct: "marktwaarde-toets"
  verbonden: "connected-person"
  rgs: "BLas"

2025-12-15 open Liabilities:Personeel:Verlof                AED
  nl: "Opgebouwde, nog niet opgenomen vakantiedagen van Umar (30 kalenderdagen per jaar), gewaardeerd op het basisloon"
  btw: "nvt"
  ifrs: "Personeelsverplichtingen (kortlopend)"
  ct: "aftrekbaar"
  verbonden: "connected-person"
  rgs: "BSchOvs"

; --- Eigen vermogen
2025-12-15 open Equity:Kapitaalbijdrage                     AED
  nl: "Inbreng van de aandeelhouder buiten aandelen om, bijv. een kwijtgescholden loonschuld of het voordeel van een renteloze lening"
  btw: "nvt"
  ifrs: "Overige reserves (kapitaalbijdrage aandeelhouder)"
  rgs: "BEivAgi"

; --- Opbrengsten
2025-12-15 open Income:Omzet:Binnenland                     AED
  nl: "Omzet aan klanten in de UAE (5% btw, alleen na registratie)"
  btw: "5-binnenland"
  ifrs: "Netto-omzet"
  ct: "aftrekbaar"
  rgs: "WOmzNod"

; --- Kosten
2025-12-15 open Expenses:Personeel:Verlof                   AED
  nl: "Dotatie aan de verlofverplichting"
  btw: "nvt"
  ifrs: "Personeelskosten"
  ct: "marktwaarde-toets"
  verbonden: "connected-person"
  rgs: "WPerLes"

2025-12-15 open Expenses:Personeel:Zorgverzekering          AED
  nl: "Verplichte zorgverzekering werknemer (Dubai); alleen de werknemer, niet het gezin"
  btw: "5-voorbelasting"
  ifrs: "Personeelskosten"
  ct: "marktwaarde-toets"
  verbonden: "connected-person"
  rgs: "WBedOvp"

2025-12-15 open Expenses:Afschrijvingen:Inventaris          AED
  nl: "Afschrijving op laptop, telefoon en apparatuur"
  btw: "nvt"
  ifrs: "Afschrijvingen"
  ct: "aftrekbaar"
  rgs: "WAfs"

2025-12-15 open Expenses:Representatie:Klanten              AED
  nl: "Zakelijke lunches en diners met klanten, aandeelhouders of zakenpartners (50% niet aftrekbaar voor CT)"
  btw: "geblokkeerd"
  ifrs: "Overige bedrijfskosten"
  ct: "50-niet-aftrekbaar"
  rgs: "WBedVkk"

2025-12-15 open Expenses:Representatie:Relatiegeschenken    AED
  nl: "Relatiegeschenken (geen entertainment; aftrekbaar als zakelijk)"
  btw: "geblokkeerd"
  ifrs: "Overige bedrijfskosten"
  ct: "aftrekbaar"
  rgs: "WBedVkkRel"

2025-12-15 open Expenses:Vennootschapsbelasting             AED
  nl: "UAE vennootschapsbelasting over het boekjaar (bij SBR nihil)"
  btw: "nvt"
  ifrs: "Belastinglast"
  ct: "niet-aftrekbaar"
  rgs: "WBel"

2025-12-15 open Expenses:Donaties                           AED
  nl: "Giften; alleen aftrekbaar aan een Qualifying Public Benefit Entity"
  btw: "nvt"
  ifrs: "Overige bedrijfskosten"
  ct: "niet-aftrekbaar"
  rgs: "WBedAlk"
```

Alle nieuwe resultaatrekeningen voeren alleen AED (B1.2); de bestaande kostenrekeningen met AED,EUR worden in dezelfde ronde omgezet.

Optioneel, alleen als het contract erin voorziet: `Liabilities:Personeel:Vliegticket` en `Expenses:Personeel:Vliegticket`.

### B4. Toe te voegen of te wijzigen rekeningen MZML Ltd

```beancount
2025-12-15 open Assets:Waardevermindering:Ekmekci         EUR
  nl: "Bijzondere waardevermindering op de deelneming Ekmekci (tegenrekening, negatief saldo)"
  ifrs: "Financiële vaste activa (bijzondere waardevermindering)"
  rgs: "BFvaAnd"

2025-12-15 open Assets:Waardevermindering:Point-Sixteen   EUR
  nl: "Bijzondere waardevermindering op de deelneming Point Sixteen"
  ifrs: "Financiële vaste activa (bijzondere waardevermindering)"
  rgs: "BFvaDio"

2025-12-15 open Assets:Waardevermindering:The-Ocean       EUR
  nl: "Bijzondere waardevermindering op de deelneming The Ocean"
  ifrs: "Financiële vaste activa (bijzondere waardevermindering)"
  rgs: "BFvaAnd"

2025-12-15 open Liabilities:Crediteuren                   AED,EUR
  nl: "Ontvangen facturen (RAK ICC, registered agent, adviseurs) die nog betaald moeten worden"
  ifrs: "Handelsschulden"
  rgs: "BSchCre"

2025-12-15 open Liabilities:Overlopend                    AED,EUR
  nl: "Kosten die bij het boekjaar horen maar nog niet gefactureerd zijn (bijv. verlenging RAK ICC)"
  ifrs: "Overlopende passiva"
  rgs: "BSchOpa"

2025-12-15 open Equity:Kapitaalbijdrage                   AED
  nl: "Inbreng buiten aandelen om, bijv. het voordeel van een renteloze vendor loan als die tegen contante waarde wordt gewaardeerd"
  ifrs: "Overige reserves (kapitaalbijdrage)"
  rgs: "BEivAgi"

2025-12-15 open Expenses:Waardevermindering-deelnemingen  AED
  nl: "Last uit bijzondere waardevermindering van een deelneming"
  btw: "nvt"
  ifrs: "Bijzondere waardeverminderingen"
  ct: "vrijgesteld"
  rgs: "WFbe"

2025-12-15 open Expenses:Bronbelasting                    AED
  nl: "Ingehouden Nederlandse dividendbelasting die niet terug te krijgen is (tarief volgens verdrag NL-VAE, door Dinesh te bevestigen)"
  btw: "nvt"
  ifrs: "Belastinglast"
  ct: "niet-aftrekbaar"
  rgs: "WBel"

2025-12-15 open Expenses:Vennootschapsbelasting           AED
  nl: "UAE vennootschapsbelasting (verwacht nihil)"
  btw: "nvt"
  ifrs: "Belastinglast"
  ct: "niet-aftrekbaar"
  rgs: "WBel"
```

Wijzigingen bestaande MZML Ltd-rekeningen:

| Rekening | Wijziging |
|---|---|
| `Assets:Bank:Nog-te-openen` | Verwijderen; openen op de werkelijke datum met de echte naam |
| `Assets:Deelnemingen:*` | Valuta: EUR met kostprijs in AED (B1.3) of AED; `ifrs:` per deelneming: P16 "joint venture tegen kostprijs (15.9(a))", The Ocean "geassocieerde deelneming tegen kostprijs (14.4(a))", Ekmekci afhankelijk van invloed (14.4(a) of Section 11); `rgs:` BFvaDio (P16), BFvaAnd (Ocean), BFvaAnd of BFvaOve (Ekmekci); `ct: "vrijgesteld"` |
| `Assets:Nog-te-storten-kapitaal` | `ifrs: "In mindering op eigen vermogen (IFRS for SMEs 22.7(a))"`; `rgs: "BVorVao"` |
| `Assets:Rekening-courant:Umar` | `ifrs:` "Vordering op of schuld aan bestuurder"; `rgs: "BVorOvr"`, `rgs-omslag: "BSchOvs"`; `verbonden: "connected-person"` |
| `Assets:Te-ontvangen-dividend` | `rgs: "BVorVop"`; `verbonden: "related-party"` |
| `Liabilities:Vendor-loan:*` | `ct: "rente-art30-31"`; `verbonden: "related-party"`; `rgs: "BLas"` [v]; nl-tekst aanvullen met looptijd en kortlopend deel zodra de overeenkomst is ingezien |
| `Liabilities:Rekening-courant:MZML-BV`, `:XCL` | `verbonden: "related-party"`; `rgs:` schulden aan verbonden maatschappijen [v] |
| `Liabilities:Te-betalen-rente` | `rgs: "BSchOpa"` |
| `Income:Dividend` | nl-tekst corrigeren: de deelnemingsvrijstelling geldt vanaf het eerste boekjaar als de voorwaarden zijn vervuld (minimaal 5%, 12 maanden houden of de intentie daartoe, onderworpen aan minimaal 9% belasting) ([TaxGuru](https://taxguru.in/chartered-accountant/uae-corporate-tax-exempt-income-participation-pe-transport-rules.html)), niet "vanaf 1-1-2027"; `ct: "vrijgesteld"`; bruto boeken, bronbelasting apart |
| `Expenses:Rente:Vendor-loan` | `ct: "rente-art30-31"`; `rgs: "WFbeRlsRil"` [b]; `verbonden: "related-party"` |
| `Expenses:Overheid:RAK-ICC` | `rgs: "WBedOrgHol"` [b] |
| `Expenses:Oprichting` | `ifrs:` "Overige bedrijfskosten (oprichtingskosten, Section 18.15)"; RGS-afwijking noteren (NL kan activeren) |
| `Income:Koersresultaat`, `Expenses:Koersverschil` | Herwaardering alleen op vendor loans en rekening-courant, nooit op deelnemingen |

### B5. Bestaande XCL-rekeningen: gewijzigde btw-code, metadata en RGS

| Rekening | btw nu | btw voorstel | ct | verbonden | rgs | Overige wijziging |
|---|---|---|---|---|---|---|
| `Assets:Bank:Wio-AED`, `Wio-EUR` | | | | | BLimBan [b] | |
| `Assets:Debiteuren:Ekmekci` | | | | related-party | BVorVov [b] | Zie C5 |
| `Assets:Debiteuren:MDI` | | | | related-party | BVorVov [b] | |
| `Assets:Debiteuren:Point-Sixteen` | | | | related-party | BVorVov [b] | |
| `Assets:Debiteuren:Inclusionair`, `:Overig` | | | | | BVorDeb [b] | |
| `Assets:Vooruitbetaald:*` | | | | | BVorOva [b] | Niet-monetair: AED |
| `Assets:Rekening-courant:Umar` | | | marktwaarde-toets | connected-person | BVorOvr [b], omslag BSchOvs | ifrs: "Vordering op of schuld aan bestuurder" |
| `Assets:Rekening-courant:MZML-Ltd` | | | | related-party | BVorVov [b] | |
| `Assets:Nog-te-storten-kapitaal` | | | | connected-person | BVorVao [b] | ifrs: "In mindering op eigen vermogen (22.7(a))" |
| `Assets:Btw:Voorbelasting` | | | | | BVorVbk [b] | |
| `Liabilities:Crediteuren` | | | | | BSchCre [b] | |
| `Liabilities:Personeel:Loonschuld-Umar` | | | marktwaarde-toets | connected-person | BSchOvs [v] | |
| `Liabilities:Personeel:End-of-service` | | | marktwaarde-toets | connected-person | BVrz [v] | nl: "op het laatste basisloon" |
| `Liabilities:Btw:Af-te-dragen` | | | | | BSchBepBaf [b] | |
| `Liabilities:CT:Te-betalen` | | | | | BSchBep [v] | |
| `Liabilities:Overlopend` | | | | | BSchOpa [b] | |
| `Equity:Aandelenkapitaal` | | | | | BEivGok [v] | |
| `Equity:Resultaat` | | | | | BEivOvrAlr [b] | Alleen AED |
| `Income:Omzet:Managementfee:Ekmekci` | 0-export | 0-export | aftrekbaar | related-party | WOmzNod [b] | Valuta AED |
| `Income:Omzet:Managementfee:MDI` | 0-export | 0-export | aftrekbaar | related-party | WOmzNod [b] | Valuta AED |
| `Income:Omzet:Managementfee:Point-Sixteen` | 0-export | 0-export | aftrekbaar | related-party | WOmzNod [b] | Valuta AED; zie C5 |
| `Income:Omzet:Advies:Inclusionair` | 0-export | 0-export | aftrekbaar | | WOmzNod [b] | |
| `Income:Omzet:Overig` | 0-export | **per factuur; standaard 5-binnenland** | aftrekbaar | | WOmzNod [b] | Valuta AED |
| `Income:Koersresultaat` | nvt | nvt | aftrekbaar | | WFbe [v] | |
| `Income:Overig` | nvt | nvt | aftrekbaar | | WOvb [b] | Valuta AED |
| `Expenses:Personeel:Loon-Umar` | nvt | nvt | marktwaarde-toets | connected-person | WPerLes [v] | |
| `Expenses:Personeel:Huisvesting` | geen-aftrek | **vrijgesteld** | marktwaarde-toets | connected-person | WPerLes [v] | |
| `Expenses:Personeel:Huisvesting-nuts` | geen-aftrek | **geblokkeerd** | marktwaarde-toets | connected-person | WPerLes [v] | SEWA rekent 5%; privévoorziening werknemer |
| `Expenses:Personeel:End-of-service` | nvt | nvt | marktwaarde-toets | connected-person | WPerLes of WPerPen [v] | |
| `Expenses:Personeel:Visa-medisch` | geen-aftrek | **buiten-reikwijdte** | aftrekbaar | | WBedOvp [b] | Hernoemen naar `Visa-overheid`; zorgverzekering naar nieuwe rekening |
| `Expenses:Overheid:Licentie-IFZA` | nvt | **per factuur** (IFZA-factuur controleren op btw) | aftrekbaar | | WBedAlk [v] | Altijd via `Assets:Vooruitbetaald:Licentie` (importerregel zet nu direct op kosten) |
| `Expenses:Overheid:Certificaten` | 5-voorbelasting | **buiten-reikwijdte** (FTA/IFZA-heffingen); 5% alleen op een TRN-factuur van een dienstverlener | aftrekbaar | | WBedAlk [v] | |
| `Expenses:Overheid:Boetes` | nvt | buiten-reikwijdte | niet-aftrekbaar | | WBedAlk [v] | |
| `Expenses:Auto:Huur` | 5-voorbelasting | **geblokkeerd** | aftrekbaar (als loon in natura) | connected-person | WBedAut [b] | Zie C4 |
| `Expenses:Auto:Brandstof-tol` | 5-voorbelasting | **brandstof: zakelijk deel 5-voorbelasting of conservatief geblokkeerd; Salik en RTA-parkeren buiten-reikwijdte** | aftrekbaar | | WBedAut [b] | Splitsen in `:Brandstof` en `:Tol-parkeren` |
| `Expenses:Reis:Vervoer` | 5-voorbelasting | **vrijgesteld** (taxi, metro, bus: lokaal personenvervoer); 5% alleen als de bon btw toont | aftrekbaar | | WBedVkk [v] | |
| `Expenses:Reis:Vliegtickets` | nvt | 0-inkoop | aftrekbaar | | WBedVkk [v] | |
| `Expenses:Reis:Verblijf` | geen-aftrek | **buitenland** (NL); UAE-hotel op zakenreis: 5-voorbelasting | aftrekbaar | | WBedVkk [v] | |
| `Expenses:Representatie` | geen-aftrek | geblokkeerd | 50-niet-aftrekbaar | | WBedVkk [b] | Opsplitsen volgens B3 |
| `Expenses:Telecom` | 5-voorbelasting | 5-voorbelasting, zakelijk deel | aftrekbaar | | WBedKan [b] | Privégebruik: pro rata |
| `Expenses:Software:AI` | geen-aftrek | **verlegd** | aftrekbaar | | WBedKan [b] | |
| `Expenses:Software:Overig` | geen-aftrek | **verlegd**; UAE-leverancier met TRN: 5-voorbelasting | aftrekbaar | | WBedKan [b] | |
| `Expenses:Kantoor:Benodigdheden` | 5-voorbelasting | 5-voorbelasting | aftrekbaar | | WBedKan [b] | Apparatuur boven de grens naar vaste activa |
| `Expenses:Kantoor:Boeken-opleiding` | geen-aftrek | **per factuur**: congres in UAE 5-voorbelasting, buitenlandse online cursus verlegd | aftrekbaar | | WBedOvp [b] | |
| `Expenses:Marketing` | geen-aftrek | **verlegd** (LinkedIn e.d.) | aftrekbaar | | WBedVkk [b] | |
| `Expenses:Advies:Corporate-services` | 5-voorbelasting | 5-voorbelasting; doorbelaste overheidsheffingen buiten-reikwijdte | aftrekbaar | | WBedAlk [v] | |
| `Expenses:Advies:Fiscaal-juridisch` | 5-voorbelasting | **UAE-adviseur 5-voorbelasting; NL-adviseur verlegd** | aftrekbaar | | WBedAlk [v] | |
| `Expenses:Verzekering` | geen-aftrek | **5-voorbelasting** (schadeverzekering); levensverzekering vrijgesteld | aftrekbaar | | WBedAlk [v] | |
| `Expenses:Bank:Kosten` | nvt | **5-voorbelasting** (Wio-btw-factuur) | aftrekbaar | | WBedAlk [v] | ifrs: "Overige bedrijfskosten" (geen rente in de zin van art. 29) |
| `Expenses:Bank:Wisselkosten` | nvt | **5-voorbelasting** (expliciete fee) | aftrekbaar | | WBedAlk [v] | idem |
| `Expenses:Koersverschil` | nvt | nvt | aftrekbaar | | WFbe [v] | |
| `Expenses:Overig` | geen-aftrek | per factuur | aftrekbaar | | WBedAlk [v] | |
| `Expenses:Onbekend` | nvt | nvt | nvt | | geen (moet nul zijn) | |

### B6. Te verwijderen of samen te voegen

- `Assets:Bank:Nog-te-openen` (MZML Ltd): verwijderen.
- `Expenses:Representatie` (XCL): vervangen door `:Klanten` en `:Relatiegeschenken` (en eventueel `:Personeel`, ct aftrekbaar, btw geblokkeerd).
- `Expenses:Personeel:Visa-medisch`: hernoemen naar `Visa-overheid`; zorgverzekering naar eigen rekening.
- `Expenses:Auto:Brandstof-tol`: splitsen in `Brandstof` en `Tol-parkeren` (andere btw).
- Geen rekeningen samenvoegen; de fijnmazigheid is functioneel.

### B7. Importerregels (gevolg van het voorgaande, kort)

- Ontbrekende regel voor inkomende overboekingen van Umar (EUR 25.000 op 26-1-2026): naar `Liabilities:Lening-aandeelhouder:Umar` met vlag `!`, eerst vaststellen of een deel kapitaalstorting is (C8).
- `ifza` naar `Assets:Vooruitbetaald:Licentie` in plaats van direct naar kosten.
- Software- en AI-regels: btw-code `verlegd` vanaf de registratiedatum, met override als de factuur UAE-btw toont.
- Koers per boeking uit de CBUAE-reeks (C7); Wio-wissels alleen voor de werkelijke conversie.

---

## C. Risico's in de besluitenlog

**C1. Route a: loon AED 40.000 opbouwen vanaf 15-12-2025, niet-betaald deel als renteloze schuld.**
- *Ingangsdatum.* 15-12-2025 is de oprichtingsdatum. Een dienstverband kan pas lopen vanaf de datum in het arbeidscontract en de werkvergunning. Als het visum later is afgegeven, is loon over de tussenliggende periode geen loon uit dienstbetrekking. Controleer contract- en visumdatum.
- *Arbeidsrecht.* Loon moet periodiek worden betaald; een werkgever mag niet eenzijdig verlagen of inhouden, en de totale inhoudingen zijn begrensd op 50% van het loon ([Addleshaw Goddard, 2026](https://www.addleshawgoddard.com/en/insights/insights-briefings/2026/employment/safeguarding-payroll-turbulent-times-lawful-salary-deductions-reductions-uae-labour-law/)). Een structureel niet-betaald deel is een overtreding, ook met instemming van de werknemer, tenzij het als schriftelijk afgesproken uitgestelde betaling of tijdelijke verlaging is vastgelegd. De nieuwe WPS-regeling (Ministerial Resolution 340 van 2026, per 1-6-2026) geldt voor bij MOHRE gelicentieerde werkgevers; of en hoe IFZA dit toepast is onduidelijk ([Morgan Lewis](https://www.morganlewis.com/pubs/2026/05/uae-introduces-new-wage-protection-system-resolution-effective-1-june-2026)). Vraag het IFZA of RD Advisory.
- *Interne tegenspraak.* De log zegt "salaris AED 22.000 vanaf 25-10-2026" en tegelijk "route a, AED 40.000 over 2026". In het projectgeheugen staat dat het contract op AED 40.000 doorloopt tot het addendum (dat wacht op de freezonekeuze van 5-11-2026). Leg vast welk loon voor november en december 2026 wordt **opgebouwd**: als het contract nog 40.000 zegt, is 22.000 een betaling op een hoger opgebouwd loon, geen nieuw loon.
- *IFRS.* Opbouw is juist zolang er een contractuele verplichting is. Scheldt Umar later een deel kwijt, dan is dat een transactie met de eigenaar in die hoedanigheid en gaat het naar het eigen vermogen (`Equity:Kapitaalbijdrage`), niet naar de winst.
- *CT.* Loon aan een connected person is alleen aftrekbaar voor zover marktconform (art. 36). Onder SBR doet dat er voor 2026 niet toe, maar het opgebouwde loon maakt XCL in 2026 verliesgevend en **een verlies in een SBR-jaar vervalt** ([BCL](https://bcl.ae/blogs/small-business-relief-uae-tax-return-guide/)). Met de verlenging van SBR tot 2029 is de waarde van een voorwaarts te verrekenen verlies beperkt, maar maak die afweging expliciet vóór de aangifte (uiterlijk 30-9-2027). Zonder SBR is de connected-personschedule verplicht, want de betalingen en voordelen aan Umar overschrijden AED 500.000 ([PwC](https://www.pwc.com/m1/en/services/tax/middle-east-tax-news-alerts/2024/uae-corporate-tax-returns-guide.html)).
- *Gratuity.* De voorziening hangt aan het basisloon in het contract, niet aan AED 40.000 totaal, en wordt bij de verlaging naar het nieuwe basisloon herrekend (art. 51 lid 5).

**C2. Rekening-courant directeur, maandelijks verrekend met de loonschuld.**
- *IFRS.* Salderen van een vordering en een schuld mag alleen bij een juridisch afdwingbaar recht en de intentie om netto af te wikkelen. Leg een verrekeningsafspraak schriftelijk vast (XCL vertegenwoordigd door Umar, Umar als werknemer; zelfcontractering, dus extra belangrijk om het te documenteren).
- *Arbeidsrecht.* Privé-uitgaven met de bedrijfspas behandelen als voorschot op loon is verdedigbaar, maar verrekenen met loon is een inhouding (begrensd, zie C1). Zolang het loon toch niet volledig wordt uitbetaald, is het risico vooral formeel; maak er een schriftelijke voorschotregeling van.
- *CT.* Een debetsaldo is een renteloze lening aan een connected person. In niet-SBR-jaren kan de FTA een zakelijke rente bijtellen (art. 34/36). Neerwaartse correcties (bijvoorbeeld zakelijke rente op de loonschuld) vereisen FTA-goedkeuring en zijn dus niet zomaar aftrekbaar.

**C3. Woning als loon in natura tot 14-2-2027.**
- *IFRS:* juist (personeelskosten, vooruitbetaald actief voor het niet-verstreken deel).
- *Btw:* woninghuur is vrijgesteld, er is geen btw om af te trekken; SEWA rekent 5%, maar dat is een privévoorziening voor de werknemer en daarmee geblokkeerd tenzij er een wettelijke plicht is. Code `geen-aftrek` was qua uitkomst goed, qua vak-indeling niet.
- *CT:* aftrekbaar als beloning, binnen de marktwaardetoets van art. 36 voor het totale pakket (loon plus woning plus auto).
- *Contract:* "geen woonvergoeding vanaf 25-10-2026" botst met "villa via XCL tot 14-2-2027". Het addendum moet de woning tot 14-2-2027 uitdrukkelijk als loon in natura noemen. Woonvoordelen tellen niet mee voor de gratuity.

**C4. Auto via XCL is "zakelijk", ook de als privé gelabelde betalingen.**
- *Btw:* voorbelasting op huur van een auto die beschikbaar is voor privégebruik is geblokkeerd; beschikbaarheid is het criterium (art. 53 UR; [Business Dubai](https://www.businessdubai.ae/blogs/uae-vat-return-filing)). De huidige code `5-voorbelasting` op `Expenses:Auto:Huur` is fout.
- *CT:* gemengd gebruik is alleen voor het zakelijke deel aftrekbaar (art. 28; [Fidinam](https://www.fidinam.com/en/blog/tax-motor-vehicle-expenditure-uae)). Beter: het privégebruik expliciet als loon in natura aan Umar behandelen (dan aftrekbaar als beloning, binnen de marktwaardetoets). Het besluit "alles zakelijk" zonder die kwalificatie is fiscaal zwakker dan nodig. Verkeersboetes zijn nooit aftrekbaar.

**C5. Alle omzet 2026 0% export.**
- De voorwaarden voor nultarief zijn dat de afnemer zijn woonplaats (vestiging) buiten de UAE heeft en op het moment van de dienst buiten de UAE is. Woonplaats van een bedrijf is waar het juridisch gevestigd is en significante managementbeslissingen neemt, of een vaste inrichting met personeel heeft ([Crowe](https://www.crowe.com/ae/news/zero-rating-on-export-of-services-in-the-uae)).
- **Risico na de bestuurswissel**: als MZML Holding Limited (UAE) statutair bestuurder wordt van Ekmekci, Point Sixteen en The Ocean, en de bestuursbeslissingen feitelijk in Sharjah worden genomen, kan de FTA stellen dat die afnemers een vestiging in de UAE hebben. Dan is de fee aan hen 5% (vak 1b) in plaats van 0%. Dit is dezelfde feitenvraag als de Nederlandse plaats-van-werkelijke-leiding-toets, maar met omgekeerd belang. Laat Dinesh en Davie dit samen bekijken vóór de bestuurswissel; documenteer per factuur waar de afnemer is gevestigd en waar de beslissingen vallen.
- *Verbonden partijen:* MDI (gemeenschappelijke zeggenschap via Umar, voor zover ik uit de projectstukken afleid) en Ekmekci/P16/The Ocean (zeggenschap of invloed van betekenis via het bestuur van MZML Ltd) zijn related parties in de zin van art. 35. Niet alleen Point Sixteen apart markeren.
- *Alternatief voor registratie:* wie uitsluitend nultariefleveringen doet, kan een uitzondering op registratie aanvragen ([Hawksford](https://www.hawksford.com/insights-and-guides/vat-registration-uae)). Voor XCL (alleen exportomzet, weinig UAE-voorbelasting) kan dat eenvoudiger zijn dan registratie met maandelijkse of driemaandelijkse aangiften en reverse charge. Afweging nu maken, want Umar werkt op dit moment aan de registratie. Komt er binnenlandse omzet bij, dan vervalt die route.

**C6. SBR 2026.**
Juist voor 2026 als het verlies er niet toe doet; zie C1. Nieuw sinds de besluitenlog: SBR loopt door tot boekjaren eindigend op of vóór 31-12-2029 (MD 131/2026 volgens [Osome](https://osome.com/ae/blog/small-business-relief-extended-2029/) en [Entrepreneur Middle East](https://mena.entrepreneur.com/business-news/uae-extends-small-business-tax-relief-through-2029)). Voor MZML Ltd: SBR of niet maakt weinig uit zolang dividend vrijgesteld is; rente op de vendor loans valt onder de specifieke renteaftrekbeperking, met als veilige haven dat MZML Holding B.V. in Nederland minimaal 9% belasting betaalt over die rente ([Deloitte](https://www.deloitte.com/middle-east/en/services/tax/perspectives/interest-deduction-limitation-rules-guide.html)). Documenteer dat.

**C7. Koersen "alleen waargenomen: Wio-wissels of ECB met bron".**
Voor btw moet de CBUAE-koers op de leveringsdatum worden gebruikt (art. 69 btw-wet; FTA VATP004; [EY](https://globaltaxnews.ey.com/news/2018-5894-uae-publishes-public-clarification-on-use-of-exchange-rates-for-vat-purposes)). De CBUAE publiceert dagkoersen en maandoverzichten. Voorstel: CBUAE als enige bron voor omrekening van facturen (omzet, kosten, reverse charge) en voor herwaardering per maandeinde; Wio-koersen alleen voor de werkelijke conversie op de bank (het verschil is koersresultaat). ECB laten vallen voor de UAE-entiteiten; voor de NL-bv's is het niet relevant (EUR).

**C8. Kapitaal als "nog te storten".**
Boekhoudkundig juist als vordering, maar presenteren als minpost op het eigen vermogen (IFRS for SMEs 22.7(a)). Controleer of de EUR 25.000 van 26-1-2026 (ongeveer AED 107.000) bedoeld was als kapitaalstorting van AED 48.000 plus een lening. Zo ja, dan klopt de openingsboeking niet en is de lening kleiner. Voor MZML Ltd vereist RAK ICC geen storting; laat de vordering staan tot de bankrekening er is.

**C9. Kosten MZML Ltd betaald door MZML Holding B.V. (NL), en via XCL ("Decisive Zone").**
Twee financiers voor dezelfde holding, beide renteloos, en een UAE-werkmaatschappij die kosten van de UAE-holding betaalt: dat schuurt met de staande regel dat de scheiding XCL/MZML structureel is. Fiscaal: renteloze financiering tussen related parties (arm's length, art. 34; aan NL-zijde zakelijkheid bij MZML Holding B.V.). Advies: één financier, bij voorkeur zo snel mogelijk de eigen bankrekening van MZML Ltd, en de rekening-courant met XCL afwikkelen.

**C10. MZML Ltd als statutair bestuurder van de NL-bv's tegen nul vergoeding.**
Geen schemapunt, wel een fiscaal risico: een gratis dienst aan related parties kan onder art. 34 (arm's length) tot een correctie bij MZML Ltd leiden zodra SBR niet meer geldt. Het schema hoeft er nu geen rekening voor te hebben; neem het op in de TP-onderbouwing.

**C11. Btw-registratie en drempel.**
Geïmporteerde diensten tellen mee voor de drempel van AED 375.000, net als nultariefomzet (Hawksford). De registratiedatum die de FTA vaststelt, bepaalt vanaf wanneer reverse charge en voorbelasting gelden; houd rekening met terugwerkende kracht. De boete voor te late registratie is AED 10.000 (Hawksford).

**C12. IFZA-verlenging december 2026.**
De vereenvoudigde jaarrekening is op kasbasis in het IFZA-sjabloon; het eerste boekjaar is bij de verlenging nog niet afgesloten (A3). Dit staat niet in de besluitenlog en wel op het kritieke pad.

---

## Bevestiging van de door de bouwer genoemde gaten

| Gat | Oordeel | Uitwerking |
|---|---|---|
| Vooruitontvangen omzet | Bevestigd | `Liabilities:Vooruitontvangen:Omzet` in AED (niet-monetair) |
| Lening aandeelhouder EUR 25.000 | Bevestigd, met kanttekening | Eerst vaststellen of een deel kapitaalstorting is (C8) |
| Vaste activa | Bevestigd | Kostprijs en afschrijving apart, plus afschrijvingskosten |
| Omzet verbonden partij P16 apart | Bevestigd maar te smal | Ook MDI en Ekmekci; via metadata `verbonden:` op debiteur en omzet, niet via extra rekeningen |
| CT-voorziening | Deels weerlegd | De balansrekening bestaat al; de P&L-rekening ontbreekt |
| Reverse charge | Bevestigd, en zwaarder dan gedacht | Twee rekeningen plus nieuwe btw-codes; raakt ook NL-advies, LinkedIn en congressen |

Aanvullende gaten uit deze review: verlofverplichting, waarborgsommen, kruisposten, kapitaalbijdrage, binnenlandse omzet, representatie splitsen, zorgverzekering apart, bijzondere waardevermindering deelnemingen, NL-dividendbelasting, crediteuren en overlopende passiva MZML Ltd, valuta-opzet resultaatrekeningen en deelnemingen.

---

## Bronnen

- PwC, UAE Corporate Tax "Tax Returns" Guide: https://www.pwc.com/m1/en/services/tax/middle-east-tax-news-alerts/2024/uae-corporate-tax-returns-guide.html
- BCL, Small Business Relief return guide: https://bcl.ae/blogs/small-business-relief-uae-tax-return-guide/
- Osome, SBR verlengd tot 2029: https://osome.com/ae/blog/small-business-relief-extended-2029/
- Entrepreneur Middle East, SBR tot 2029: https://mena.entrepreneur.com/business-news/uae-extends-small-business-tax-relief-through-2029
- Grant Thornton, CTP010 director en officer (art. 36): https://www.grantthornton.ae/insights/alerts/tax-alert-fta-clarifies-director-and-officer-under-article-36/
- Deloitte, interest deduction limitation rules: https://www.deloitte.com/middle-east/en/services/tax/perspectives/interest-deduction-limitation-rules-guide.html
- Alpha Partners, niet-aftrekbare kosten: https://www.alphapartners.co/blog/uae-corporate-tax-list-of-non-deductible-expenses-explained
- Fidinam, motorvoertuigen CT en btw: https://www.fidinam.com/en/blog/tax-motor-vehicle-expenditure-uae
- TaxGuru, deelnemingsvrijstelling art. 23: https://taxguru.in/chartered-accountant/uae-corporate-tax-exempt-income-participation-pe-transport-rules.html
- Business Dubai, VAT 201 per vak en art. 53: https://www.businessdubai.ae/blogs/uae-vat-return-filing
- ClearTax, btw-wijzigingen per 1-1-2026: https://www.cleartax.com/ae/new-vat-rules-uae-2026
- Hawksford, btw-registratie UAE: https://www.hawksford.com/insights-and-guides/vat-registration-uae
- EY, FTA VATP004 wisselkoersen: https://globaltaxnews.ey.com/news/2018-5894-uae-publishes-public-clarification-on-use-of-exchange-rates-for-vat-purposes
- Crowe, nultarief export van diensten: https://www.crowe.com/ae/news/zero-rating-on-export-of-services-in-the-uae
- IFZA FAQ jaarrekening bij verlenging: https://cdn.ifza.com/marketing/FAQs%20Update_.pdf
- Uniwide, IFZA financial statements: https://www.uniwide.com/ifza-requires-submission-of-financial-statements-for-license-renewal/
- Khaleej Times, gratuity op laatste basisloon (art. 51): https://www.khaleejtimes.com/uae/legal/uae-how-is-gratuity-calculated-if-salary-changes-during-course-of-service
- auditfirmsdubai, EOSG-voorziening: https://auditfirmsdubai.ae/en/resources/blog/end-of-service-gratuity-provision-uae
- Addleshaw Goddard, inhoudingen op loon UAE (2026): https://www.addleshawgoddard.com/en/insights/insights-briefings/2026/employment/safeguarding-payroll-turbulent-times-lawful-salary-deductions-reductions-uae-labour-law/
- Morgan Lewis, WPS-resolutie per 1-6-2026: https://www.morganlewis.com/pubs/2026/05/uae-introduces-new-wage-protection-system-resolution-effective-1-june-2026
- IFRS Foundation, AP30C (IFRS for SMEs 22.7(a)): https://www.ifrs.org/content/dam/ifrs/meetings/2023/december/iasb/ap30c-requirement-to-offset-equity-instruments.pdf
- Tally, UAE chart of accounts-template: https://tallysolutions.com/mena/uae-vat/setting-up-a-chart-of-accounts-for-uae-trading-company-practical-template/
- boekhoudplaza, RGS balanscodes: https://www.boekhoudplaza.nl/rgs_rekeningen/B&KB=B/Balans.htm
- boekhoudplaza, RGS MKB 3.5.1 voorstel: https://www.boekhoudplaza.nl/upload/boekhoudplaza/rgs/versie351/RGS%20MKB%20versie%203.5.1_Voorstel_V1.pdf
- boekhoudplaza, conversie RGS 3.3 naar 3.4: https://boekhoudplaza.nl/upload/boekhoudplaza/rgs/versie34/20220222_Verslag%20boekhoudplaza%20conversie%203.3%20naar%203.4.pdf
- boekhoudplaza, toelichting btw-afdracht (BSchBepBaf): https://boekhoudplaza.nl/rgs_rap_toelichting/1019&bra=1/BTW_afdracht.htm
- Referentie Grootboekschema (RGS 3.9 bèta): https://www.referentiegrootboekschema.nl/

Uit vakkennis, niet in een geraadpleegde bron teruggevonden (vóór gebruik verifiëren): artikelnummers 29 tot en met 36 CT-wet (FDL 47/2022), art. 46 en 48 btw-wet (FDL 8/2017), art. 31 en 53 UR (Cabinet Decision 52/2017), IFRS for SMEs 14.4, 15.9, 18.15, 28.6 en 28.19, de exacte regelnamen van het CT-accounting schedule, en alle RGS-codes met [v].

Niet bereikbaar tijdens de review: officiële RGS-download (referentiegrootboekschema.nl, proxy 403) en twee boekhoudplaza-pagina's voor de codes BSch en W (toestemming niet tijdig gegeven).
