# Pylint-analyysi ja huomiot

Tässä raportissa käydään läpi projektin Pylint-tarkastuksessa nousseet huomautukset. Pylint-arvosana projektille on tällä hetkellä 7.06/10.

Päätin jättää seuraavat asiat korjaamatta alla olevista syistä:

## Dokumentaatio (Docstrings)
- Virheet:`C0114` (Missing module docstring) ja `C0116` (Missing function docstring).
- Syy: En lisännyt docstring-tekstejä jokaiseen väliin, koska pyrin nimeämään muuttujat ja funktiot niin selkeästi, että koodi on luettavissa ilman niitäkin. Lyhyissä harjoitustöissä koin, että kommentointi koodin sisällä riittää selittämään logiikan.

## Koodin muotoilu ja tyyli
- Virheet: `C0303` (Trailing whitespace) ja `C0304` (Missing final newline).
- Syy: Nämä ovat pieniä "kauneusvirheitä", kuten ylimääräisiä välilyöntejä rivien lopussa. Siivosin niitä sieltä täältä, mutta osa jäi, koska ne eivät vaikuta sovelluksen toimintaan mitenkään.

## Rakenteelliset valinnat
- Virhe: `W0102` (Dangerous default value []).
- Syy: Käytin `db.py`-tiedostossa tyhjää listaa oletusarvona. Tiedostan riskin, mutta tässä projektissa parametrit annetaan aina suoraan, joten oletusarvo ei pääse muuttumaan vahingossa.
- Virhe: `R1705` (Unnecessary "else" after "return").
- Syy: Pylintin mielestä `else` on turha `returnin` jälkeen, mutta jätin sen joihinkin kohtiin, koska se tekee koodin rakenteesta (jos-niin-muuten) mielestäni selkeämmän lukea.

## SQLite-objektit
- Virhe: `E0237` (Assigning to attribute not defined in class slots).
- Syy: Tämä näyttää olevan Pylintin virhetulkinta siitä, miten SQLite käsittelee tietokannasta haettuja rivejä. Koodi toimii testatusti kuitenkin oikein.