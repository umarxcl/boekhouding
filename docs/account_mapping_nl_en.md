# Account mapping Dutch to English (3-11-2026)

Owner decision 2-11-2026: the bookkeeping is kept in English. On 3-11-2026 every account was renamed, every metadata key and
generated text was translated, and nothing else changed: amounts, dates, commodities, cost bases, prices, balance assertions,
flags, `wio-ref` and `drive-id` values are identical before and after (verified with a full posting and balance comparison).
Use this table to read older documents that use the Dutch names, such as `docs/besluitenlog.md`,
`docs/review_rekeningschema.md` and `docs/goedkeuring/`.

## XCL MANAGEMENT CONSULTANCIES - FZCO (`xcl/`)

| Old name (Dutch) | New name (English) |
|---|---|
| `Assets:Vaste-activa:Inventaris:Kostprijs` | `Assets:FixedAssets:Equipment:Cost` |
| `Assets:Vaste-activa:Inventaris:Afschrijving` | `Assets:FixedAssets:Equipment:AccumulatedDepreciation` |
| `Assets:Bank:Wio-AED` | `Assets:Bank:Wio-AED` |
| `Assets:Bank:Wio-EUR` | `Assets:Bank:Wio-EUR` |
| `Assets:Kruisposten` | `Assets:Suspense` |
| `Assets:Debiteuren:Ekmekci` | `Assets:Receivables:Trade:Ekmekci` |
| `Assets:Debiteuren:MDI` | `Assets:Receivables:Trade:MDI` |
| `Assets:Debiteuren:Point-Sixteen` | `Assets:Receivables:Trade:PointSixteen` |
| `Assets:Debiteuren:Inclusionair` | `Assets:Receivables:Trade:Inclusionair` |
| `Assets:Debiteuren:Overig` | `Assets:Receivables:Trade:Other` |
| `Assets:Vooruitbetaald:Huisvesting` | `Assets:Prepayments:Housing` |
| `Assets:Vooruitbetaald:Licentie` | `Assets:Prepayments:Licence` |
| `Assets:Vooruitbetaald:Overig` | `Assets:Prepayments:Other` |
| `Assets:Waarborgsommen` | `Assets:Deposits` |
| `Assets:Rekening-courant:Umar` | `Assets:Receivables:Director:Umar` |
| `Assets:Rekening-courant:MZML-Ltd` | `Assets:Receivables:Related:MZML-Ltd` |
| `Assets:Rekening-courant:MZML-BV` | `Assets:Receivables:Related:MZML-BV` |
| `Assets:Nog-te-storten-kapitaal` | `Assets:ShareCapitalUnpaid` |
| `Assets:Btw:Voorbelasting` | `Assets:VAT:Input` |
| `Assets:Btw:Voorbelasting-verlegd` | `Assets:VAT:InputReverseCharge` |
| `Liabilities:Crediteuren` | `Liabilities:Payables:Trade` |
| `Liabilities:Lening-aandeelhouder:Umar` | `Liabilities:ShareholderLoan:Umar-EUR` |
| `Liabilities:Lening-aandeelhouder:Umar-AED` | `Liabilities:ShareholderLoan:Umar-AED` |
| `Liabilities:Personeel:Loonschuld-Umar` | `Liabilities:Employees:SalaryPayable-Umar` |
| `Liabilities:Personeel:End-of-service` | `Liabilities:Employees:EndOfService` |
| `Liabilities:Personeel:Verlof` | `Liabilities:Employees:LeaveAccrual` |
| `Liabilities:Btw:Af-te-dragen` | `Liabilities:VAT:Output` |
| `Liabilities:Btw:Verlegd` | `Liabilities:VAT:ReverseCharge` |
| `Liabilities:CT:Te-betalen` | `Liabilities:CorporateTax:Payable` |
| `Liabilities:Vooruitontvangen:Omzet` | `Liabilities:DeferredRevenue` |
| `Liabilities:Overlopend` | `Liabilities:Accruals` |
| `Equity:Aandelenkapitaal` | `Equity:ShareCapital` |
| `Equity:Kapitaalbijdrage` | `Equity:CapitalContribution` |
| `Equity:Openingsbalans` | `Equity:OpeningBalance` |
| `Equity:Resultaat` | `Equity:RetainedEarnings` |
| `Income:Omzet:Managementfee:Ekmekci` | `Income:Revenue:ManagementFees:Ekmekci` |
| `Income:Omzet:Managementfee:MDI` | `Income:Revenue:ManagementFees:MDI` |
| `Income:Omzet:Managementfee:Point-Sixteen` | `Income:Revenue:ManagementFees:PointSixteen` |
| `Income:Omzet:Advies:Inclusionair` | `Income:Revenue:Advisory:Inclusionair` |
| `Income:Omzet:Binnenland` | `Income:Revenue:Domestic` |
| `Income:Omzet:Overig` | `Income:Revenue:Other` |
| `Income:Koersresultaat` | `Income:FXGain` |
| `Income:Overig` | `Income:Other` |
| `Expenses:Personeel:Loon-Umar` | `Expenses:Staff:Salary-Umar` |
| `Expenses:Personeel:Huisvesting` | `Expenses:Staff:Housing` |
| `Expenses:Personeel:Huisvesting-nuts` | `Expenses:Staff:HousingUtilities` |
| `Expenses:Personeel:Auto-prive` | `Expenses:Staff:CarPrivateUse` |
| `Expenses:Personeel:End-of-service` | `Expenses:Staff:EndOfService` |
| `Expenses:Personeel:Verlof` | `Expenses:Staff:Leave` |
| `Expenses:Personeel:Zorgverzekering` | `Expenses:Staff:HealthInsurance` |
| `Expenses:Personeel:Visa-overheid` | `Expenses:Staff:VisaGovernment` |
| `Expenses:Overheid:Licentie-IFZA` | `Expenses:Government:IFZALicence` |
| `Expenses:Overheid:Certificaten` | `Expenses:Government:Certificates` |
| `Expenses:Overheid:Boetes` | `Expenses:Government:Fines` |
| `Expenses:Vennootschapsbelasting` | `Expenses:CorporateTax` |
| `Expenses:Auto:Huur` | `Expenses:Car:Rental` |
| `Expenses:Auto:Brandstof` | `Expenses:Car:Fuel` |
| `Expenses:Auto:Tol-parkeren` | `Expenses:Car:TollsParking` |
| `Expenses:Reis:Vervoer` | `Expenses:Travel:LocalTransport` |
| `Expenses:Reis:Vliegtickets` | `Expenses:Travel:Flights` |
| `Expenses:Reis:Verblijf` | `Expenses:Travel:Accommodation` |
| `Expenses:Representatie:Klanten` | `Expenses:Entertainment:Clients` |
| `Expenses:Representatie:Relatiegeschenken` | `Expenses:Entertainment:Gifts` |
| `Expenses:Telecom` | `Expenses:Telecom` |
| `Expenses:Software:AI` | `Expenses:Software:AI` |
| `Expenses:Software:Overig` | `Expenses:Software:Other` |
| `Expenses:Kantoor:Benodigdheden` | `Expenses:Office:Supplies` |
| `Expenses:Kantoor:Boeken-opleiding` | `Expenses:Office:BooksTraining` |
| `Expenses:Afschrijvingen:Inventaris` | `Expenses:Depreciation:Equipment` |
| `Expenses:Marketing` | `Expenses:Marketing` |
| `Expenses:Advies:Corporate-services` | `Expenses:Professional:CorporateServices` |
| `Expenses:Advies:Fiscaal-juridisch` | `Expenses:Professional:TaxLegal` |
| `Expenses:Verzekering` | `Expenses:Insurance` |
| `Expenses:Bank:Kosten` | `Expenses:Bank:Charges` |
| `Expenses:Bank:Wisselkosten` | `Expenses:Bank:FXCharges` |
| `Expenses:Koersverschil` | `Expenses:FXLoss` |
| `Expenses:Donaties` | `Expenses:Donations` |
| `Expenses:Overig` | `Expenses:Other` |
| `Expenses:Onbekend` | `Expenses:Suspense` |

## MZML HOLDING LIMITED (`mzml_ltd/`)

| Old name (Dutch) | New name (English) |
|---|---|
| `Assets:Deelnemingen:Ekmekci` | `Assets:Investments:Cost:Ekmekci` |
| `Assets:Deelnemingen:Point-Sixteen` | `Assets:Investments:Cost:PointSixteen` |
| `Assets:Deelnemingen:The-Ocean` | `Assets:Investments:Cost:TheOcean` |
| `Assets:Waardevermindering:Ekmekci` | `Assets:Investments:Impairment:Ekmekci` |
| `Assets:Waardevermindering:Point-Sixteen` | `Assets:Investments:Impairment:PointSixteen` |
| `Assets:Waardevermindering:The-Ocean` | `Assets:Investments:Impairment:TheOcean` |
| `Assets:Nog-te-storten-kapitaal` | `Assets:ShareCapitalUnpaid` |
| `Assets:Rekening-courant:Umar` | `Assets:Receivables:Director:Umar` |
| `Assets:Te-ontvangen-dividend` | `Assets:Receivables:Dividends` |
| `Liabilities:Crediteuren` | `Liabilities:Payables:Trade` |
| `Liabilities:Vendor-loan:MZML-BV:Ekmekci` | `Liabilities:VendorLoans:MZML-BV:Ekmekci` |
| `Liabilities:Vendor-loan:MZML-BV:Point-Sixteen` | `Liabilities:VendorLoans:MZML-BV:PointSixteen` |
| `Liabilities:Vendor-loan:MZML-BV:The-Ocean` | `Liabilities:VendorLoans:MZML-BV:TheOcean` |
| `Liabilities:Rekening-courant:MZML-BV` | `Liabilities:Payables:Related:MZML-BV` |
| `Liabilities:Rekening-courant:XCL` | `Liabilities:Payables:Related:XCL` |
| `Liabilities:Te-betalen-rente` | `Liabilities:InterestPayable` |
| `Liabilities:Overlopend` | `Liabilities:Accruals` |
| `Liabilities:CT:Te-betalen` | `Liabilities:CorporateTax:Payable` |
| `Equity:Aandelenkapitaal` | `Equity:ShareCapital` |
| `Equity:Kapitaalbijdrage` | `Equity:CapitalContribution` |
| `Equity:Openingsbalans` | `Equity:OpeningBalance` |
| `Equity:Resultaat` | `Equity:RetainedEarnings` |
| `Income:Dividend` | `Income:Dividends` |
| `Income:Koersresultaat` | `Income:FXGain` |
| `Expenses:Overheid:RAK-ICC` | `Expenses:Government:RAKICC` |
| `Expenses:Overheid:Certificaten` | `Expenses:Government:Certificates` |
| `Expenses:Oprichting` | `Expenses:FormationCosts` |
| `Expenses:Advies` | `Expenses:Professional:Advisory` |
| `Expenses:Rente:Vendor-loan` | `Expenses:Interest:VendorLoans` |
| `Expenses:Bank` | `Expenses:Bank:Charges` |
| `Expenses:Koersverschil` | `Expenses:FXLoss` |
| `Expenses:Waardevermindering-deelnemingen` | `Expenses:Impairment:Investments` |
| `Expenses:Bronbelasting` | `Expenses:WithholdingTax` |
| `Expenses:Vennootschapsbelasting` | `Expenses:CorporateTax` |
| `Expenses:Onbekend` | `Expenses:Suspense` |

## Metadata keys

| Old key | New key | Notes |
|---|---|---|
| `nl` | `note` | Plain-language explanation. Where an entry already had an English `note` from the owner review of 3-11-2026, the earlier Dutch `nl` text (the original importer or invoice-script note) became `initial-note`. |
| `antwoord` | `owner-answer` | Value kept verbatim (the owner's own words, often in Dutch). |
| `goedkeuring` | `approved` | Date of the owner's approval. |
| `bron` | `source` | |
| `koers` | `rate` | |
| `factuur` | `invoice` | |
| `verifieer` | `verify` | |
| `nl-document` | `document-note` | |
| `btw` | `vat` | Values translated, see below. |
| `verbonden` | `related-party` | Two accounts had the value `ja`; set to `related-party` (MZML-BV receivable) and `connected-person` (Umar AED loan), consistent with their siblings. |
| `rgs-omslag` | `rgs-negative` | RGS code to use when the balance changes sign. |
| `ct`, `ifrs`, `rgs`, `open`, `iban`, `document`, `drive-id`, `wio-*` | unchanged | `ct` and `ifrs` values translated; `document` values are Drive file names and stay as they are. |

## VAT codes (`vat`)

| Old | New | Meaning (VAT 201) |
|---|---|---|
| `0-export` | `zero-rated-export` | Zero-rated export of services (box 4) |
| `5-binnenland` | `standard-5` | Standard-rated 5% domestic supply (box 1) |
| `5-voorbelasting` | `input-5` | 5% input VAT with a tax invoice showing a TRN (box 9) |
| `verlegd` | `reverse-charge` | Reverse charge: self-assessed and recovered (boxes 3 and 10) |
| `geblokkeerd` | `blocked` | Input VAT not recoverable (art. 53 Executive Regulation) |
| `vrijgesteld` | `exempt` | Exempt purchase |
| `buiten-reikwijdte` | `out-of-scope` | Government fee outside the scope of VAT |
| `0-inkoop` | `zero-rated-purchase` | Zero-rated purchase |
| `buitenland` | `foreign` | Consumed outside the UAE |
| `nvt` | `n/a` | No VAT consequence |

## Corporate Tax treatment (`ct`)

| Old | New |
|---|---|
| `aftrekbaar` | `deductible` |
| `50-niet-aftrekbaar` | `50-non-deductible` |
| `niet-aftrekbaar` | `non-deductible` |
| `marktwaarde-toets` | `arms-length-test` |
| `vrijgesteld` | `exempt` |
| `rente-art30-31` | `interest-art30-31` |
| `nvt` | `n/a` |
