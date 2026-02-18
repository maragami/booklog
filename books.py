import db

def add_book(title, author, user_id):
    sql = "INSERT INTO books (title, author, user_id) VALUES (?, ?, ?)"
    db.execute(sql, [title, author, user_id])