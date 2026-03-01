import db

def add_book(title, author, user_id):
    sql = """INSERT INTO books (title, author, user_id) VALUES (?, ?, ?)"""
    db.execute(sql, [title, author, user_id])

def get_all_books():
    sql = "SELECT id, title, author FROM books ORDER BY id DESC"
    return db.query(sql)

def get_book(book_id):
    sql = """SELECT books.id,
                    books.title,
                    books.author,
                    users.id user_id,
                    users.username
                FROM books, users
                WHERE books.user_id = users.id AND
                    books.id = ?"""
    return db.query(sql, [book_id])[0]

def update_book(book_id, new_title, new_author):
    sql = """UPDATE books SET title = ?,
                    author = ?
                WHERE id = ?"""
    
    db.execute(sql, [new_title, new_author, book_id])

def remove_book(book_id):
    sql = "DELETE FROM books WHERE id = ?"

    db.execute(sql, [book_id])

def find_book(query):
    sql = """SELECT id, title, author
             FROM books
             WHERE title LIKE ? OR author LIKE ?
             ORDER BY id DESC"""
    like = "%" + query + "%"
    return db.query(sql, [like, like])

def get_user_by_id(user_id):
    sql = "SELECT id, username FROM users WHERE id = ?"
    result = db.query(sql,[user_id])
    if len(result) > 0:
        return result[0]
    return None

def get_books_by_user(user_id):
    sql = "SELECT id, title, author FROM books WHERE user_id = ? ORDER BY id DESC"
    return db.query(sql,[user_id])