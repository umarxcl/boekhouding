# Chart of accounts in plain language

Generated from the ledger (`scripts/chart_of_accounts_md.py`). Change the explanations in `accounts.beancount`, not here. Old Dutch account names: `docs/account_mapping_nl_en.md`.


## XCL MANAGEMENT CONSULTANCIES - FZCO

| Account | What it is | VAT | CT | Related party | Financial statements | RGS |
|---|---|---|---|---|---|---|
| `Assets:Bank:Wio-AED` | Wio business current account in dirham (card for business expenses) |  |  |  | Cash and cash equivalents | BLimBan |
| `Assets:Bank:Wio-EUR` | Wio business account in euro (receipt of the management fees) |  |  |  | Cash and cash equivalents | BLimBan |
| `Assets:Deposits` | Security deposits for villa and rental car; refundable at end of lease | no VAT consequence | n/a |  | Other receivables | BFvaOvr |
| `Assets:FixedAssets:Equipment:AccumulatedDepreciation` | Accumulated depreciation on equipment (straight-line: laptop 3 years, phone 2 years) | no VAT consequence | deductible |  | Property, plant and equipment (accumulated depreciation) | BMvaBei |
| `Assets:FixedAssets:Equipment:Cost` | Purchase cost of laptop, phone and equipment from AED 2,500 per item | 5% input VAT with tax invoice showing TRN (box 9) | deductible |  | Property, plant and equipment | BMvaBei |
| `Assets:Prepayments:Housing` | Prepaid villa rent: the part of a quarterly payment that has not yet elapsed |  |  |  | Prepayments | BVorOva |
| `Assets:Prepayments:Licence` | Prepaid IFZA licence and establishment card, spread over the licence period |  |  |  | Prepayments | BVorOva |
| `Assets:Prepayments:Other` | Other prepayments (annual subscriptions, insurance) |  |  |  | Prepayments | BVorOva |
| `Assets:Receivables:Director:Umar` | Director's current account: amounts XCL advanced to Umar (private withdrawals and private spending on the XCL card); set off monthly against salary payable under the written set-off agreement |  | arms-length-test | connected-person | Receivable from / payable to director | BVorOvr |
| `Assets:Receivables:Related:MZML-BV` | Receivable from MZML Holding B.V. (Netherlands): costs XCL paid on behalf of MZML Holding B.V., e.g. neWings invoice 2026-0098 | no VAT consequence | arms-length-test | related-party | Receivable from related party | BVorVov |
| `Assets:Receivables:Related:MZML-Ltd` | Amounts XCL paid on behalf of MZML Holding Limited (to be settled once MZML Ltd has a bank account) |  |  | related-party | Receivable from related party | BVorVov |
| `Assets:Receivables:Trade:Ekmekci` | Receivable from Ekmekci Group B.V. (invoices issued less receipts) |  |  | related-party | Receivables from related parties | BVorVov |
| `Assets:Receivables:Trade:Inclusionair` | Receivable from Inclusionair (Dutch B.V.), invoiced in AED |  |  |  | Trade receivables | BVorDeb |
| `Assets:Receivables:Trade:MDI` | Receivable from MDI Consultants B.V. |  |  | related-party | Receivables from related parties | BVorVov |
| `Assets:Receivables:Trade:Other` | Receivables from other customers |  |  |  | Trade receivables | BVorDeb |
| `Assets:Receivables:Trade:PointSixteen` | Receivable from Point Sixteen B.V. (fee from the board resolution and management agreement) |  |  | related-party | Receivables from related parties | BVorVov |
| `Assets:ShareCapitalUnpaid` | Share capital not yet paid up by the shareholder; deducted from equity in the financial statements |  |  | connected-person | Deducted from equity (IFRS for SMEs 22.7(a)) | BVorVao |
| `Assets:Suspense` | Money in transit between own accounts; must be nil at month-end close | no VAT consequence |  |  | n/a | BVorTus |
| `Assets:VAT:Input` | VAT on UAE costs that XCL may recover (only with a tax invoice showing a TRN, only from the registration date) | 5% input VAT with tax invoice showing TRN (box 9) |  |  | Tax receivable | BVorVbk |
| `Assets:VAT:InputReverseCharge` | VAT that XCL self-assesses on imported services and recovers at the same time (VAT 201 box 10) | reverse charge: self-assess and recover (boxes 3 and 10) |  |  | Tax receivable (offset against Liabilities:VAT:ReverseCharge) | BVorVbk |
| `Equity:CapitalContribution` | Contribution by the shareholder other than for shares (e.g. a waived salary payable) |  |  |  | Other reserves (shareholder capital contribution) | BEivAgi |
| `Equity:OpeningBalance` | Technical contra account for the opening balance |  |  |  | n/a |  |
| `Equity:RetainedEarnings` | Profit or loss of closed financial years |  |  |  | Retained earnings | BEivOvrAlr |
| `Equity:ShareCapital` | Issued share capital: 100 shares of AED 480 (resolution at incorporation) |  |  |  | Share capital | BEivGok |
| `Expenses:Bank:Charges` | Wio bank charges (monthly subscription, transfer fees); Wio issues a tax invoice | 5% input VAT with tax invoice showing TRN (box 9) | deductible |  | Other operating expenses | WBedAlk |
| `Expenses:Bank:FXCharges` | Wio foreign exchange mark-up on foreign card payments | 5% input VAT with tax invoice showing TRN (box 9) | deductible |  | Other operating expenses | WBedAlk |
| `Expenses:Car:Fuel` | Fuel (ADNOC, ENOC); input VAT conservatively blocked while the car is available for private use | input VAT not recoverable (art. 53) | deductible |  | Other operating expenses | WBedAut |
| `Expenses:Car:Rental` | Rental of the company car (Ezhire and similar); input VAT blocked because the car is also available for private use | input VAT not recoverable (art. 53) | deductible |  | Other operating expenses | WBedAut |
| `Expenses:Car:TollsParking` | Salik, RTA parking and government parking (no VAT) | government fee, outside the scope of VAT | deductible |  | Other operating expenses | WBedAut |
| `Expenses:CorporateTax` | UAE Corporate Tax for the financial year (nil under SBR) | no VAT consequence | non-deductible |  | Income tax expense | WBel |
| `Expenses:Depreciation:Equipment` | Depreciation of laptop, phone and equipment | no VAT consequence | deductible |  | Depreciation | WAfs |
| `Expenses:Donations` | Donations; deductible only when made to a Qualifying Public Benefit Entity | no VAT consequence | non-deductible |  | Other operating expenses | WBedAlk |
| `Expenses:Entertainment:Clients` | Business lunches and dinners with clients or business partners (input VAT blocked; 50% non-deductible for Corporate Tax) | input VAT not recoverable (art. 53) | 50-non-deductible |  | Other operating expenses | WBedVkk |
| `Expenses:Entertainment:Gifts` | Business gifts (not entertainment; deductible when business-related) | input VAT not recoverable (art. 53) | deductible |  | Other operating expenses | WBedVkkRel |
| `Expenses:FXLoss` | Loss on currency exchanges and on revaluation of EUR balances and receivables | no VAT consequence | deductible |  | Finance costs | WFbe |
| `Expenses:Government:Certificates` | Certificates and amendments at IFZA or FTA (fees without VAT; a service provider's fee goes to Professional) | government fee, outside the scope of VAT | deductible |  | Other operating expenses | WBedAlk |
| `Expenses:Government:Fines` | Fines from FTA, IFZA or traffic authorities (not deductible for Corporate Tax) | government fee, outside the scope of VAT | non-deductible |  | Other operating expenses (non-deductible) | WBedAlk |
| `Expenses:Government:IFZALicence` | IFZA licence, establishment card and registration (monthly share via Prepayments:Licence); VAT per invoice | government fee, outside the scope of VAT | deductible |  | Other operating expenses | WBedAlk |
| `Expenses:Insurance` | Business property and liability insurance (5% input VAT); life insurance exempt | 5% input VAT with tax invoice showing TRN (box 9) | deductible |  | Other operating expenses | WBedAlk |
| `Expenses:Marketing` | LinkedIn Premium, website, profile building (foreign suppliers: reverse charge) | reverse charge: self-assess and recover (boxes 3 and 10) | deductible |  | Selling and marketing expenses | WBedVkk |
| `Expenses:Office:BooksTraining` | Professional literature, courses, conferences; VAT per invoice (UAE conference 5%, foreign course reverse charge) | reverse charge: self-assess and recover (boxes 3 and 10) | deductible |  | Other operating expenses | WBedOvp |
| `Expenses:Office:Supplies` | Office supplies and small equipment below AED 2,500 (Amazon.ae and similar) | 5% input VAT with tax invoice showing TRN (box 9) | deductible |  | Other operating expenses | WBedKan |
| `Expenses:Other` | Other expenses that fit nowhere else (explanation required; VAT per invoice) | government fee, outside the scope of VAT | deductible |  | Other operating expenses | WBedAlk |
| `Expenses:Professional:CorporateServices` | RD Advisory and other PRO services (service fee 5% input VAT; government fees passed through are out of scope) | 5% input VAT with tax invoice showing TRN (box 9) | deductible |  | Other operating expenses | WBedAlk |
| `Expenses:Professional:TaxLegal` | Tax and legal advice (UAE adviser 5% input VAT; Dutch adviser reverse charge) | 5% input VAT with tax invoice showing TRN (box 9) | deductible |  | Other operating expenses | WBedAlk |
| `Expenses:Software:AI` | AI subscriptions from foreign suppliers (Anthropic, OpenAI, Fireflies, xAI): reverse charge after registration | reverse charge: self-assess and recover (boxes 3 and 10) | deductible |  | Other operating expenses | WBedKan |
| `Expenses:Software:Other` | Other software (Google, Dropbox, TransIP, Microsoft, Figma, Netlify): reverse charge; UAE supplier with TRN: 5% input VAT | reverse charge: self-assess and recover (boxes 3 and 10) | deductible |  | Other operating expenses | WBedKan |
| `Expenses:Staff:CarPrivateUse` | Private use of the company car as benefit in kind (share of car costs) | no VAT consequence | arms-length-test | connected-person | Staff costs | WPerLes |
| `Expenses:Staff:EndOfService` | Addition to the end-of-service gratuity provision | no VAT consequence | arms-length-test | connected-person | Staff costs | WPerLes |
| `Expenses:Staff:HealthInsurance` | Mandatory health insurance for the employee (employee only, not the family) | 5% input VAT with tax invoice showing TRN (box 9) | arms-length-test | connected-person | Staff costs | WBedOvp |
| `Expenses:Staff:Housing` | Residence in Sharjah as benefit in kind (villa rent, spread per month) until 14-2-2027; residential rent is VAT-exempt | exempt purchase | arms-length-test | connected-person | Staff costs | WPerLes |
| `Expenses:Staff:HousingUtilities` | SEWA and other residence costs as benefit in kind; input VAT blocked (private provision for the employee) | input VAT not recoverable (art. 53) | arms-length-test | connected-person | Staff costs | WPerLes |
| `Expenses:Staff:Leave` | Addition to the annual leave accrual | no VAT consequence | arms-length-test | connected-person | Staff costs | WPerLes |
| `Expenses:Staff:Salary-Umar` | Gross salary of Umar under the employment contract | no VAT consequence | arms-length-test | connected-person | Staff costs | WPerLes |
| `Expenses:Staff:VisaGovernment` | Visa, Emirates ID, medical test (government fees, no VAT) | government fee, outside the scope of VAT | deductible |  | Staff costs | WBedOvp |
| `Expenses:Suspense` | Temporary: items still to be reviewed (must be empty at month-end close) | no VAT consequence | n/a |  | n/a |  |
| `Expenses:Telecom` | Mobile and internet (e&, du); 5% input VAT on the business share | 5% input VAT with tax invoice showing TRN (box 9) | deductible |  | Other operating expenses | WBedKan |
| `Expenses:Travel:Accommodation` | Hotels and subsistence on business trips (Netherlands: no UAE VAT; UAE hotel: 5% input VAT) | consumed outside the UAE | deductible |  | Other operating expenses | WBedVkk |
| `Expenses:Travel:Flights` | Business flights (international transport: zero-rated) | zero-rated purchase | deductible |  | Other operating expenses | WBedVkk |
| `Expenses:Travel:LocalTransport` | Taxi, Uber, metro (local passenger transport is VAT-exempt) | exempt purchase | deductible |  | Other operating expenses | WBedVkk |
| `Income:FXGain` | Gain on currency exchanges and on revaluation of EUR balances and receivables | no VAT consequence | deductible |  | Finance income | WFbe |
| `Income:Other` | Other income (refunds and similar) | no VAT consequence | deductible |  | Other income | WOvb |
| `Income:Revenue:Advisory:Inclusionair` | Advisory services to Inclusionair (Dutch B.V.) | zero-rated export (box 4) | deductible |  | Revenue | WOmzNod |
| `Income:Revenue:Domestic` | Revenue from customers in the UAE (5% VAT, only after registration) | standard-rated 5% UAE (box 1) | deductible |  | Revenue | WOmzNod |
| `Income:Revenue:ManagementFees:Ekmekci` | Management fee charged to Ekmekci Group B.V. (EUR 7,716 per month) | zero-rated export (box 4) | deductible | related-party | Revenue | WOmzNod |
| `Income:Revenue:ManagementFees:MDI` | Fee charged to MDI Consultants B.V. (ABN AMRO leadership programme) | zero-rated export (box 4) | deductible | related-party | Revenue | WOmzNod |
| `Income:Revenue:ManagementFees:PointSixteen` | Fee charged to Point Sixteen B.V. (from the board resolution and management agreement) | zero-rated export (box 4) | deductible | related-party | Revenue | WOmzNod |
| `Income:Revenue:Other` | Other revenue; VAT treatment per invoice | standard-rated 5% UAE (box 1) | deductible |  | Revenue | WOmzNod |
| `Liabilities:Accruals` | Costs belonging to the month that have not yet been invoiced or paid |  |  |  | Accruals | BSchOpa |
| `Liabilities:CorporateTax:Payable` | UAE Corporate Tax for the financial year (nil under Small Business Relief) |  |  |  | Tax payable | BSchBep |
| `Liabilities:DeferredRevenue` | Amounts prepaid by customers for services still to be delivered (e.g. INV-0008 Inclusionair); in AED at the receipt rate | no VAT consequence | n/a |  | Contract liability (deferred revenue) | BSchVobVob |
| `Liabilities:Employees:EndOfService` | Provision for end-of-service gratuity: 21 days' basic salary per year of service in the first five years, based on the last basic salary |  | arms-length-test | connected-person | Provision for employee benefits | BVrz |
| `Liabilities:Employees:LeaveAccrual` | Accrued, untaken annual leave (30 calendar days per year) at basic salary |  | deductible | connected-person | Employee benefit obligations (current) | BSchOvs |
| `Liabilities:Employees:SalaryPayable-Umar` | Salary for Umar accrued but not yet paid (contract salary; deferred payment agreed in writing, route a) |  | arms-length-test | connected-person | Payable to director | BSchOvs |
| `Liabilities:Payables:Trade` | Purchase invoices received and not yet paid |  |  |  | Trade payables | BSchCre |
| `Liabilities:ShareholderLoan:Umar-AED` | Interest-free loan from Umar (private) to XCL in AED (e.g. AED 21,063.03 on 3-8-2026 from private funds); terms to be documented in writing | no VAT consequence | arms-length-test | connected-person | Loan from shareholder | BLas |
| `Liabilities:ShareholderLoan:Umar-EUR` | Loan from Umar (private) to XCL (including EUR 25,000 on 26-1-2026), interest-free; terms to be documented in writing; first determine which part is capital contribution |  | arms-length-test | connected-person | Loan from shareholder | BLas |
| `Liabilities:VAT:Output` | Output VAT XCL must pay on domestic supplies (VAT 201 box 1); nil with exports only | standard-rated 5% UAE (box 1) |  |  | Tax payable | BSchBepBaf |
| `Liabilities:VAT:ReverseCharge` | VAT on imported services (software, AI, Dutch advisers) that XCL self-assesses (VAT 201 box 3) | reverse charge: self-assess and recover (boxes 3 and 10) |  |  | Tax payable (offset against Assets:VAT:InputReverseCharge) | BSchBepBlw |

## MZML HOLDING LIMITED

| Account | What it is | VAT | CT | Related party | Financial statements | RGS |
|---|---|---|---|---|---|---|
| `Assets:Investments:Cost:Ekmekci` | 75 shares in Ekmekci Group B.V. (18.80%), acquired 31-12-2025 at cost |  | exempt | related-party | Non-current financial assets: investment at cost (Section 14.4(a) or Section 11, depending on influence) | BFvaAnd |
| `Assets:Investments:Cost:PointSixteen` | 5,000 shares in Point Sixteen B.V. (50%), acquired 31-12-2025; joint venture at cost |  | exempt | related-party | Non-current financial assets: joint venture at cost (Section 15.9(a)) | BFvaDio |
| `Assets:Investments:Cost:TheOcean` | 720 shares in The Ocean B.V. (30%), acquired 31-12-2025; associate at cost |  | exempt | related-party | Non-current financial assets: associate at cost (Section 14.4(a)) | BFvaAnd |
| `Assets:Investments:Impairment:Ekmekci` | Impairment of the investment in Ekmekci (contra account, negative balance) |  |  |  | Non-current financial assets (impairment) | BFvaAnd |
| `Assets:Investments:Impairment:PointSixteen` | Impairment of the investment in Point Sixteen |  |  |  | Non-current financial assets (impairment) | BFvaDio |
| `Assets:Investments:Impairment:TheOcean` | Impairment of the investment in The Ocean |  |  |  | Non-current financial assets (impairment) | BFvaAnd |
| `Assets:Receivables:Director:Umar` | Amounts Umar paid privately on behalf of MZML Ltd, or the other way round |  | arms-length-test | connected-person | Receivable from / payable to director | BVorOvr |
| `Assets:Receivables:Dividends` | Dividends declared by investees but not yet received (gross) |  |  | related-party | Receivables | BVorVop |
| `Assets:ShareCapitalUnpaid` | Share capital (AED 100,000) not yet paid up; RAK ICC does not require payment; deducted from equity in the financial statements |  |  | connected-person | Deducted from equity (IFRS for SMEs 22.7(a)) | BVorVao |
| `Equity:CapitalContribution` | Contribution other than for shares (e.g. the benefit of an interest-free vendor loan if measured at present value) |  |  |  | Other reserves (capital contribution) | BEivAgi |
| `Equity:OpeningBalance` | Technical contra account for the opening balance |  |  |  | n/a |  |
| `Equity:RetainedEarnings` | Profit or loss of closed financial years |  |  |  | Retained earnings | BEivOvrAlr |
| `Equity:ShareCapital` | Issued share capital: 100 shares of AED 1,000 (RAK ICC register of members) |  |  |  | Share capital | BEivGok |
| `Expenses:Bank:Charges` | Bank charges (once the account is opened) | no VAT consequence | deductible |  | Finance costs | WBedAlk |
| `Expenses:CorporateTax` | UAE Corporate Tax (expected nil) | no VAT consequence | non-deductible |  | Income tax expense | WBel |
| `Expenses:FXLoss` | Exchange loss on revaluation of vendor loans and current accounts | no VAT consequence | deductible |  | Finance costs | WFbe |
| `Expenses:FormationCosts` | Formation costs (one-off, financial year 1; IFRS for SMEs 18.15: expensed, not capitalised; Dutch GAAP may capitalise) | no VAT consequence | deductible |  | Other operating expenses (formation costs) | WBedAlk |
| `Expenses:Government:Certificates` | Certificate of incumbency, good standing, Corporate Tax certificate | no VAT consequence | deductible |  | Other operating expenses | WBedAlk |
| `Expenses:Government:RAKICC` | Annual RAK ICC renewal including registered agent | no VAT consequence | deductible |  | Other operating expenses | WBedOrgHol |
| `Expenses:Impairment:Investments` | Impairment loss on an investment | no VAT consequence | exempt |  | Impairment losses | WFbe |
| `Expenses:Interest:VendorLoans` | Interest on the vendor loans from MZML Holding B.V. (if agreed); specific interest limitation rule, safe harbour if MZML B.V. pays at least 9% tax in the Netherlands | no VAT consequence | interest-art30-31 | related-party | Finance costs | WFbeRlsRil |
| `Expenses:Professional:Advisory` | Tax, legal and corporate services advice | no VAT consequence | deductible |  | Other operating expenses | WBedAlk |
| `Expenses:Suspense` | Temporary: still to be reviewed (must be empty at close) | no VAT consequence | n/a |  | n/a |  |
| `Expenses:WithholdingTax` | Dutch dividend withholding tax that cannot be recovered (treaty rate Netherlands-UAE, to be confirmed by Dinesh) | no VAT consequence | non-deductible |  | Income tax expense | WBel |
| `Income:Dividends` | Dividends from investees, gross (Corporate Tax participation exemption applies from the first financial year if the conditions are met: at least 5%, held 12 months or intended to be, at least 9% tax at the investee) | no VAT consequence | exempt | related-party | Investment income (dividends) | WFbe |
| `Income:FXGain` | Exchange gain on revaluation of vendor loans and current accounts (never on investments) | no VAT consequence | deductible |  | Finance income | WFbe |
| `Liabilities:Accruals` | Costs belonging to the financial year that have not yet been invoiced (e.g. RAK ICC renewal) |  |  |  | Accruals | BSchOpa |
| `Liabilities:CorporateTax:Payable` | UAE Corporate Tax (expected nil) |  |  |  | Tax payable | BSchBep |
| `Liabilities:InterestPayable` | Interest accrued but not yet paid on the vendor loans (if interest has been agreed) |  |  | related-party | Accruals | BSchOpa |
| `Liabilities:Payables:Related:MZML-BV` | Costs of MZML Ltd advanced by MZML Holding B.V. (Netherlands) (incorporation, certificates, RAK ICC) |  |  | related-party | Current payable to related party | BSchOvs |
| `Liabilities:Payables:Related:XCL` | Costs of MZML Ltd advanced by XCL (to be settled once there is a bank account; the aim is a single funder) |  |  | related-party | Current payable to related party | BSchOvs |
| `Liabilities:Payables:Trade` | Invoices received (RAK ICC, registered agent, advisers) not yet paid |  |  |  | Trade payables | BSchCre |
| `Liabilities:VendorLoans:MZML-BV:Ekmekci` | Purchase price of the Ekmekci shares owed to MZML Holding B.V. (terms, maturity and current portion: agreement in Dropbox, still to be reviewed) |  | interest-art30-31 | related-party | Non-current loan from related party | BLas |
| `Liabilities:VendorLoans:MZML-BV:PointSixteen` | Purchase price of the Point Sixteen shares owed to MZML Holding B.V. |  | interest-art30-31 | related-party | Non-current loan from related party | BLas |
| `Liabilities:VendorLoans:MZML-BV:TheOcean` | Purchase price of the The Ocean shares owed to MZML Holding B.V. |  | interest-art30-31 | related-party | Non-current loan from related party | BLas |
