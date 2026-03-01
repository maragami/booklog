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


$ git clone git@github.com:maragami/booklog.git

Siirry hakemistoon:

$ cd booklog

Luo virtuaaliympäristö:

$ python3 -m venv venv

Aktivoi virtuaaliympäristö:

$ source venv/bin/activate

Asenna tarvittavat kirjastot:

$ pip install Flask

Luo tietokannan taulut:

$ sqlite3 database.db < schema.sql

Käynnistä sovellus:

$ flask run