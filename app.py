import sqlite3
from flask import Flask
from flask import redirect, render_template, request, session
from werkzeug.security import check_password_hash, generate_password_hash
import config 
import db
import books

app = Flask(__name__)
app.secret_key = config.secret_key

@app.route("/")
def index():
    all_books = books.get_all_books()
    return render_template("index.html", books= all_books)

@app.route("/book/<int:book_id>")
def show_book(book_id):
    book = books.get_book(book_id)
    return render_template("show_book.html", book= book)

@app.route("/new_book")
def new_book():
    return render_template("new_book.html")

@app.route("/create_book", methods=["POST"])
def create_book():

    if "user_id" not in session:
        return redirect("/login")

    title = request.form["title"]
    author = request.form["author"]
    user_id = session["user_id"]

    if len(title.strip()) == 0:
        return "VIRHE: kirjan nimi puuttuu"

    if len(author.strip()) == 0:
        return "VIRHE: kirjailijan nimi puttuu"

    books.add_book(title, author, user_id)

    return redirect("/")

@app.route("/edit_book/<int:book_id>")
def edit_book(book_id):
    book = books.get_book(book_id)
    return render_template("edit_book.html", book= book)

@app.route("/update_book", methods=["POST"])
def update_book():
    book_id = request.form["book_id"]
    new_title = request.form["title"]
    new_author = request.form["author"]

    books.update_book(book_id, new_title, new_author)

    return redirect("/book/" + str(book_id))

@app.route("/remove_book/<int:book_id>", methods=["GET", "POST"])
def remove_book(book_id):
    if request.method == "GET":
        book = books.get_book(book_id)
        return render_template("remove_book.html", book= book)
    
    if request.method == "POST":
        if "remove" in request.form:
            books.remove_book(book_id)
            return redirect("/")
        else:
            return redirect("/book/" + str(book_id))
        
    
@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/create", methods=["POST"])
def create():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]

    if len(username) <= 2:
        return "VIRHE: tunnus on liian lyhyt"
    if password1 != password2:
        return "VIRHE: salasanat eivät ole samat"
    password_hash = generate_password_hash(password1)

    try:
        sql = "INSERT INTO users (username, password_hash) VALUES (?, ?)"
        db.execute(sql, [username, password_hash])
    except sqlite3.IntegrityError:
        return "VIRHE: tunnus on jo varattu"

    return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
        
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        sql = "SELECT id, password_hash FROM users WHERE username = ?"
        result = db.query(sql, [username])[0]

        if len(result) == 0:
            return "VIRHE: väärä tunnus tai salasana"
        user_id = result["id"]
        password_hash = result["password_hash"]

        if check_password_hash(password_hash, password):
            session["user_id"] = user_id
            session["username"] = username
            return redirect("/")
        else:
            return "VIRHE: väärä tunnus tai salasana"
        

@app.route("/logout")
def logout():
    del session["user_id"]
    del session["username"]
    return redirect("/")