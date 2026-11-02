# Runbook

Doel: iemand zonder voorkennis (Umar zelf, een vervanger, of een boekhouder) kan hiermee het systeem begrijpen, draaien en herstellen. Stand: 2 november 2026, fase 1 (geen eigen server; runs als geplande Claude-taken).

## 1. Onderdelen

| Onderdeel | Waar | Eigenaar |
|---|---|---|
| Grootboek | GitHub `umarxcl/boekhouding` (privé) | Umar |
| Privé-grootboek | GitHub `umarxcl/boekhouding-prive` (privé, strenger) | Umar |
| Bijlagen en bankexports | Google Drive, map Boekhouding (eigenaar mail@umarmirza.nl) | Umar |
| Goedkeuring en rapporten | Google Sheet "Boekhouding – Goedkeuring" en de bestaande Sheet "Cashflow" | Umar |
| Uitvoering | Claude (geplande taken in het project Boekhouding NL & UAE) | Claude |

## 2. Maandcyclus

1. Umar zet twee keer per maand de Wio-export (CSV, beide rekeningen in één bestand) in Drive, map `Boekhouding/Bankexports/Wio/`. Bestandsnaam zoals Wio hem geeft; de importer leest de data uit de inhoud.
2. De run haalt het grootboek op, leest nieuwe exports in (`importers/wio.py`), slaat bekende referentienummers over, categoriseert met `importers/rules_xcl.yaml`, koppelt bijlagen uit Drive, en schrijft `xcl/2026/MM.beancount`.
3. Alles wat onzeker is krijgt vlag `!` en komt in de Sheet "Goedkeuring", tab van die maand, met één regel uitleg.
4. Umar vult per regel "akkoord" of een opmerking in. Een opmerking kan een andere rekening zijn ("privé"), een bon ("staat in Drive onder ..."), of een vraag.
5. De run verwerkt de antwoorden, haalt de vlaggen weg, voegt nieuwe regels toe aan `rules_xcl.yaml` als Umar dat aangeeft, boekt loon, huisvesting, voorzieningen en koersverschillen, controleert de banksaldi tegen het afschrift, en sluit de maand (git-tag).
6. Rapporten (balans, P&L, kasstroom, rekening-courant, btw-overzicht) gaan naar de Sheet; de Cashflow-Sheet krijgt de actuals; Umar krijgt één bericht.

## 3. Controles die elke run doet

- `bean-check` op beide grootboeken (sluitende boekingen, bestaande rekeningen, saldocontroles).
- Begin- en eindsaldo van elke export tegen het grootboek (de importer schrijft `balance`-regels).
- Geen `!` meer in een maand die gesloten wordt; `Expenses:Onbekend` moet nul zijn.
- Rekening-courant directeur en loonschuld: maandelijkse verrekening geboekt.
- Koers: afwijking groter dan 2% tegenover de vorige maand komt op de lijst.
- Controle-agent (apart, zonder de boekingen te hebben gemaakt): btw-behandeling per rekening, periodesloten, vooruitbetaalde posten, voorzieningen.

## 4. Handmatig draaien (als de geplande taak niet loopt)

Op elke computer met Python 3.11 of hoger:

```
git clone https://github.com/umarxcl/boekhouding
cd boekhouding
pip install -r requirements.txt
python3 importers/wio.py <export.csv> --out xcl/2026/MM.beancount --exceptions uitzonderingen.json
bean-check xcl/main.beancount
```

Of vraag Claude in het project: "Draai de maandrun voor XCL met de export in Drive."

## 5. Herstel

- Grootboek kwijt: `git clone` vanaf GitHub (volledige geschiedenis).
- GitHub kwijt: de laatste maandrapporten staan in Sheets; de boekingen zijn te reconstrueren uit de Wio-exports in Drive met de importer.
- Drive kwijt: de bankexports zijn opnieuw te downloaden bij Wio (7 jaar); bijlagen uit Gmail, Dropbox en leveranciersportalen. Daarom: jaarlijkse back-up van de Drive-map Boekhouding naar een tweede locatie (taak in januari).
- Claude niet beschikbaar: elke boekhouder kan het grootboek lezen via `bean-query ... "select date, account, position, narration"` (CSV) of via Fava (`fava xcl/main.beancount`, webinterface).

## 6. Bewaartermijnen

UAE: 7 jaar (Corporate Tax-wet; btw 5 jaar, voor onroerend goed 15). Nederland: 7 jaar. Afgesloten jaren blijven in de repository en in Drive; niets wordt verwijderd.

## 7. Toegang

- GitHub: Umar (eigenaar), Claude via de GitHub-koppeling in claude.ai.
- Drive en Sheets: Umar (eigenaar), Claude via de Google-koppeling.
- Geen bankinloggegevens in het systeem; exports komen handmatig uit de Wio-app.

## 8. Inhaalslag XCL januari t/m oktober 2026 (2-11-2026)

- Bankexport: `data/wio_2025-11-02_2026-11-02.csv` (staat in `.gitignore`; het origineel staat in Drive, niet in git).
- Importeren: `python3 importers/wio.py data/<export>.csv --since 2026-01-01 --until 2026-10-31 --documents importers/documenten_xcl.yaml --out <tijdelijk>.beancount --exceptions <tijdelijk>.json`, daarna `python3 scripts/split_maanden.py <tijdelijk>.beancount` om per maand `xcl/2026/MM.beancount` te schrijven (saldoregels van het volgende maand-begin komen in de laatste maand).
- `importers/documenten_xcl.yaml` koppelt bankregels (Wio-ref) aan bonnen in Drive (`document` en `drive-id`). Bon aanwezig = zakelijk; zonder bon = privé via `Assets:Rekening-courant:Umar` met vlag `!`.
- Verkoopfacturen: `python3 scripts/facturen.py` schrijft `xcl/2026/facturen.beancount` (koersen uit `shared/prices.beancount`).
- Goedkeuring: de open posten met vlag `!` staan in de Google Sheet 'Boekhouding – Goedkeuring' (tabs per kwartaal).
