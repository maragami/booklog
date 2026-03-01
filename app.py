import sqlite3
from flask import Flask
from flask import redirect, render_template, request, session, abort
import secrets
from werkzeug.security import check_password_hash, generate_password_hash
import config 
import db
import books


app = Flask(__name__)
app.secret_key = config.secret_key

def check_csrf():
    if request.form["csrf_token"] != session["csrf_token"]:
        abort(403)

def check_login():
    if "user_id" not in session:
        abort(403)

@app.route("/")
def index():
    all_books = books.get_all_books()
    return render_template("index.html", books= all_books)

@app.route("/user/<int:user_id>")
def user_page(user_id):
    user = books.get_user_by_id(user_id)
    if user is None:
        return "Käyttäjää ei löytynyt", 404
    
    user_books = books.get_books_by_user(user_id)
    book_count = len(user_books)

    return render_template("user.html", user=user, books=user_books, count=book_count)

@app.route("/add_review/<int:book_id>", methods=["POST"])
def add_review(book_id):
    if "user_id" not in session:
        return redirect("/login")
    check_csrf()

    rating = request.form["rating"]
    comment = request.form["comment"]
    user_id = session["user_id"]

    books.add_review(book_id, user_id, rating, comment)

    return redirect("/book/" + str(book_id))

@app.route("/find_book")
def find_book():
    query = request.args.get("query")
    if query:
        results = books.find_book(query)
    else:
        query = ""
        results = []
    return render_template("find_book.html", query=query, results=results)

@app.route("/book/<int:book_id>")
def show_book(book_id):
    book = books.get_book(book_id)
    reviews= books.get_reviews(book_id)
    if not book:
        abort(404)
    return render_template("show_book.html", book= book, reviews=reviews)

@app.route("/new_book")
def new_book():
    check_login()
    return render_template("new_book.html")

@app.route("/create_book", methods=["POST"])
def create_book():
    check_login()
    check_csrf()

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
    check_login()
    book = books.get_book(book_id)
    if not book:
        abort(404)
    if book["user_id"] != session["user_id"]:
        abort(403)
    return render_template("edit_book.html", book= book)

@app.route("/update_book", methods=["POST"])
def update_book():
    check_login()
    check_csrf()
    book_id = request.form["book_id"]
    book = books.get_book(book_id)
    if not book:
        abort(404)
    if book["user_id"] != session["user_id"]:
        abort(403)

    new_title = request.form["title"]
    new_author = request.form["author"]

    books.update_book(book_id, new_title, new_author)

    return redirect("/book/" + str(book_id))

@app.route("/remove_book/<int:book_id>", methods=["GET", "POST"])
def remove_book(book_id):
    check_login()
    book = books.get_book(book_id)
    if not book:
        abort(404)
    if book["user_id"] != session["user_id"]:
        abort(403)
    
    if request.method == "GET":
        return render_template("remove_book.html", book= book)
    
    if request.method == "POST":
        check_csrf()
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
            session["csrf_token"] = secrets.token_hex(16)
            return redirect("/")
        else:
            return "VIRHE: väärä tunnus tai salasana"
        

@app.route("/logout")
def logout():
    if "user_id" in session:
        del session["user_id"]
        del session["username"]
    return redirect("/")