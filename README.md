# BookLog

- Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
- Käyttäjä pystyy lisäämään sovellukseen kirjoja. Lisäksi käyttäjä pystyy muokkaamaan ja poistamaan lisäämiään kirjoja.
- Käyttäjä näkee sovellukseen lisätyt kirjat. Käyttäjä näkee sekä itse lisäämänsä että muiden käyttäjien lisäämät kirjat.
- Käyttäjä pystyy etsimään kirjoja hakusanalla (nimi tai kirjailija)
- Sovelluksessa on käyttäjäsivut, jotka näyttävät jokaisesta käyttäjästä käyttäjän lisätyt kirjat, arvostelut sekä yksinkertaisa tilastoja esim. kirjojen määrä.
- Käyttäjä pystyy valitsemaan kirjalle yhden tai useamman luokittelun. Mahdolliset luokat ovat tietokannassa.
- Käyttäjä voi antaa kirjalle tähtiarvion sekä kirjoittaa kirjallisen arvostelun.
- Käyttäjä voi muokata tai poistaa oman arvostelunsa.
- kirjasivulla pitäisi näkyä arvostelut ja keskimääräinen tähditys.
- Sovelluksessa on pääasiallisen tietokohteen lisäksi toissijainen tietokohde (arvostelu), joka liittyy kirjaan.
- Käyttäjä pystyy lisäämään toissijaisia tietokohteita (arvosteluja) omiin ja muiden käyttäjien kirjoihin.


### Sovelluksen asennus

Kloonaa repositorio omalle koneellesi:


```bash
$ git clone git@github.com:maragami/booklog.git
```
Siirry hakemistoon:
```bash
$ cd booklog
```
Luo virtuaaliympäristö:
```bash
$ python3 -m venv venv
```
Aktivoi virtuaaliympäristö:
```bash
$ source venv/bin/activate
```
Asenna tarvittavat kirjastot:
```bash
$ pip install Flask
```
Luo tietokannan taulut:
```bash
$ sqlite3 database.db < schema.sql
```
Käynnistä sovellus:
```bash
$ flask run
```

## Suuren tietomäärän testaaminen
Sovellusta on testattu 10 000 kirjan tietomäärällä suorituskyvyn varmistamiseksi. Voit generoida testidatan ajamalla:

```bash
python3 seed.py
```

### Laadunvarmistus
- Koodin tyyli on tarkistettu Pylintillä.
- Erillinen raportti huomioista löytyy tiedostosta `pylint-report.md`.
- Lomakkeet on varustettu `<label>`-elementeillä saavutettavuuden parantamiseksi.