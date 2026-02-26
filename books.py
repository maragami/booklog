import db

def add_book(title, author, user_id):
    sql = "INSERT INTO books (title, author, user_id) VALUES (?, ?, ?)"
    db.execute(sql, [title, author, user_id])

def get_all_books():
    sql = "SELECT id, title, author FROM books ORDER BY id DESC"
    return db.query(sql)