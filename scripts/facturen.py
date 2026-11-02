#!/usr/bin/env python3
"""Schrijft xcl/2026/facturen.beancount: de verkoopfacturen INV-0001 t/m INV-0012 (Fiskl-export) op factuurdatum.

Bron: Fiskl-export (Sheet '2026-10-18-invoices-detail-01-Jan-26-to-18-Oct-26' en de CSV van 2-11-2026 in Drive,
Boekhouding/XCL/Verkoop 2026). EUR-facturen: debiteur in EUR tegen de CBUAE-koers van de factuurdatum (laatste publicatiedag
als dat een weekenddag is) naar omzet in AED. Ontvangsten staan in de maandbestanden (Wio-import), op dezelfde debiteurenrekening.
INV-0008 (Inclusionair, AED 89.120) is een vooruitbetaling: factuur op Liabilities:Vooruitontvangen:Omzet, omzet op 31-10-2026.
Koersen komen uit shared/prices.beancount; een ontbrekende koers laat de factuur op '!' met voorlopige koers.
"""
from __future__ import annotations

import re
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# (nummer, factuurdatum, klant, debiteur, omzetrekening, valuta, bedrag, koersdatum, omschrijving, pdf-naam, drive-id)
FACTUREN = [
    ("INV-0001", "2026-01-21", "Ekmekci Group B.V.", "Ekmekci", "Managementfee:Ekmekci", "EUR", "7766.00", "2026-01-21", "Managementfee januari 2026 (6.666) + bijdrage ZVW (300) + bijdrage auto (800)", "INV-0001.pdf", "1_0Q03MTXoktexndqjF8upWHeJZ6uqrt-"),
    ("INV-0002", "2026-01-24", "MDI Consultants B.V.", "MDI", "Managementfee:MDI", "EUR", "4500.00", "2026-01-23", "Managementfee Q1 2026", None, None),
    ("INV-0003", "2026-02-17", "Ekmekci Group B.V.", "Ekmekci", "Managementfee:Ekmekci", "EUR", "7716.00", "2026-02-17", "Managementfee februari 2026 (6.666) + bijdrage auto (800) + bijdrage ZVW (250)", "INV-0003.pdf", "1tk2Mjwb3HLQrfW665DNj0lQy9E3k0CBW"),
    ("INV-0004", "2026-03-17", "Ekmekci Group B.V.", "Ekmekci", "Managementfee:Ekmekci", "EUR", "7716.00", "2026-03-17", "Managementfee maart 2026 (6.666) + bijdrage auto (800) + bijdrage ZVW (250)", "INV-0004.pdf", "1VLLpoaUHG3SC2eh5qMAm0yAwDa6RpPl1"),
    ("INV-0005", "2026-04-17", "Ekmekci Group B.V.", "Ekmekci", "Managementfee:Ekmekci", "EUR", "7716.00", "2026-04-17", "Managementfee april 2026 (6.666) + bijdrage auto (800) + bijdrage ZVW (250)", "INV-0005.pdf", "1Bqhu47oKCZ9ar0Pbgo9ozhIA7_PZcae1"),
    ("INV-0006", "2026-05-17", "Ekmekci Group B.V.", "Ekmekci", "Managementfee:Ekmekci", "EUR", "7716.00", "2026-05-15", "Managementfee mei 2026 (6.666) + bijdrage auto (800) + bijdrage ZVW (250)", "INV-0006.pdf", "1_eWCQnypIiuMBbj1FggWHUE-Uqe7KmxP"),
    ("INV-0007", "2026-06-19", "Ekmekci Group B.V.", "Ekmekci", "Managementfee:Ekmekci", "EUR", "7716.00", "2026-06-19", "Managementfee juni 2026 (6.666) + bijdrage auto (800) + bijdrage ZVW (250)", "INV-0007.pdf", "1yafw7NJ0p9uBQ6QCEGj3OPRwxrYH0Ozw"),
    ("INV-0009", "2026-07-17", "Ekmekci Group B.V.", "Ekmekci", "Managementfee:Ekmekci", "EUR", "7716.00", "2026-07-17", "Managementfee juli 2026 (6.666) + bijdrage auto (800) + bijdrage ZVW (250)", "INV-0009.pdf", "1xvg9AfD3yn8GzmqjzsgPUFMGPhv7d8N_"),
    ("INV-0010", "2026-08-17", "Ekmekci Group B.V.", "Ekmekci", "Managementfee:Ekmekci", "EUR", "7716.00", "2026-08-17", "Managementfee augustus 2026 (6.666) + bijdrage auto (800) + bijdrage ZVW (250)", "INV-0010.pdf", "1GTqXv8-RRvMWha5liGQR46w-7Jm-tGUe"),
    ("INV-0011", "2026-09-17", "Ekmekci Group B.V.", "Ekmekci", "Managementfee:Ekmekci", "EUR", "7716.00", "2026-09-17", "Managementfee (Fiskl-omschrijving 'Aug 2026', factuur van 17-9) (6.666) + bijdrage auto (800) + bijdrage ZVW (250)", "INV-0011.pdf", "1u3bJmvXy_rpKKJAY04B8V1WXS38kxysK"),
    ("INV-0012", "2026-10-17", "Ekmekci Group B.V.", "Ekmekci", "Managementfee:Ekmekci", "EUR", "7716.00", None, "Fiskl-omschrijving 'Managementfee feb 2026' (6.916) + bijdrage auto (800), factuurdatum 17-10", "INV-0012.pdf", "1yFFqHPItxSHUQauS94BJvMgSnrOi4Py_"),
]
INV0008 = dict(nr="INV-0008", datum="2026-06-29", klant="Inclusionair", bedrag=Decimal("89120.00"),
               pdf="INV-0008.pdf", drive="1Jq9HuJLTda91Oxp5sIAHqgERFzToR19p")
# INV-0002.pdf staat niet in Drive Verkoop 2026 (gecontroleerd 2-11-2026): geen document-metadata.
FALLBACK_RATE_DATE = "2026-09-30"  # laatst bekende CBUAE-koers voor INV-0012 (oktoberoverzicht nog niet gepubliceerd)


def q2(x: Decimal) -> Decimal:
    return x.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def prices() -> dict[str, Decimal]:
    out = {}
    for line in (ROOT / "shared/prices.beancount").read_text(encoding="utf-8").splitlines():
        m = re.match(r"^(\d{4}-\d{2}-\d{2})\s+price\s+EUR\s+([\d.]+)\s+AED", line)
        if m:
            out[m.group(1)] = Decimal(m.group(2))
    return out


def fmt(x: Decimal, cur: str) -> str:
    return f"{q2(x):,.2f} {cur}"


def main() -> None:
    px = prices()
    out = ["; Verkoopfacturen XCL 2026 (Fiskl, INV-0001 t/m INV-0012), geboekt op factuurdatum.",
           "; Gegenereerd door scripts/facturen.py; ontvangsten staan in de maandbestanden (Wio-import) op dezelfde debiteurenrekening.",
           "; Alle omzet 2026 is 0% export (btw verlegd naar de klant, besluit 21-10-2026).", ""]
    entries: list[tuple[str, str]] = []
    for nr, datum, klant, deb, omz, cur, bedrag, kd, omschr, pdf, did in FACTUREN:
        amount = Decimal(bedrag)
        flag, extra = "*", []
        if kd is None:
            kd, flag = FALLBACK_RATE_DATE, "!"
            rate = px[kd]
            extra.append(f'  nl: "Voorlopige koers: het CBUAE-overzicht van oktober 2026 is nog niet gepubliceerd; koers van {kd} gebruikt, corrigeren zodra de koers van 16-10-2026 (laatste publicatiedag voor 17-10) bekend is. Ook: Fiskl noemt de omschrijving Managementfee feb 2026 (6.916) op een factuur van oktober; klopt dit?"')
            extra.append(f'  koers: "VOORLOPIG CBUAE {rate} AED per EUR (koers van {kd})"')
        else:
            rate = px[kd]
            extra.append(f'  koers: "CBUAE {rate} AED per EUR (koers van {kd})"')
        aed = q2(amount * rate)
        lines = [f'{datum} {flag} "{klant}" "Factuur {nr}: {omschr}"', f'  factuur: "{nr}"']
        if pdf:
            lines += [f'  document: "{pdf}"', f'  drive-id: "{did}"']
        else:
            lines += ['  nl-document: "INV-0002.pdf ontbreekt in Drive Verkoop 2026; bron is de Fiskl-export"']
        lines += extra
        lines += [f"  Assets:Debiteuren:{deb:<30} {fmt(amount, cur):>16} @@ {fmt(aed, 'AED')}",
                  f"  Income:Omzet:{omz:<34} {fmt(-aed, 'AED'):>16}"]
        entries.append((datum, "\n".join(lines)))
    i = INV0008
    entries.append((i["datum"], "\n".join([
        f'{i["datum"]} * "{i["klant"]}" "Factuur {i["nr"]}: Development and digital delivery Leergang (vooruitbetaling, diensten geleverd eind oktober 2026)"',
        f'  factuur: "{i["nr"]}"', f'  document: "{i["pdf"]}"', f'  drive-id: "{i["drive"]}"',
        '  nl: "Vooruitfactuur: de omzet wordt op 31-10-2026 genomen (diensten geleverd eind oktober 2026, volgens Umar); Fiskl noemt als leverdatum 24-5-2026"',
        f"  Assets:Debiteuren:Inclusionair{'':<18} {fmt(i['bedrag'], 'AED'):>16}",
        f"  Liabilities:Vooruitontvangen:Omzet{'':<13} {fmt(-i['bedrag'], 'AED'):>16}"])))
    entries.append(("2026-10-31", "\n".join([
        f'2026-10-31 ! "{i["klant"]}" "Omzet INV-0008 genomen: diensten Leergang geleverd eind oktober 2026"',
        f'  factuur: "{i["nr"]}"', f'  document: "{i["pdf"]}"', f'  drive-id: "{i["drive"]}"',
        '  nl: "Leverdatum bevestigen: Umar zegt eind oktober 2026, Fiskl noemt 24-5-2026 als datum van verkoop. Bij 24-5 verschuift de omzet naar mei"',
        f"  Liabilities:Vooruitontvangen:Omzet{'':<13} {fmt(i['bedrag'], 'AED'):>16}",
        f"  Income:Omzet:Advies:Inclusionair{'':<15} {fmt(-i['bedrag'], 'AED'):>16}"])))
    entries.sort(key=lambda t: t[0])
    out.append("\n\n".join(e for _, e in entries))
    (ROOT / "xcl/2026/facturen.beancount").write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"xcl/2026/facturen.beancount: {len(entries)} boekingen")


if __name__ == "__main__":
    main()
