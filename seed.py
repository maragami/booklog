#tämä skripti testaa miten sovellus hidastuu täyttämällä tietokantaa tuhansilla kirjoilla
import sqlite3

db = sqlite3.connect("database.db")

db.execute("DELETE FROM books")

for i in range(1, 10001):
    db.execute("INSERT INTO books (title, author, user_id) VALUES (?, ?, ?)", 
               ["Testikirja " + str(i), "Kirjailija " + str(i), 1])

db.commit()
db.close()
print("10 000 kirjaa luotu!")
