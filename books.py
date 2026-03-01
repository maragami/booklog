import db

def add_book(title, author, user_id):
    sql = "INSERT INTO books (title, author, user_id) VALUES (?, ?, ?)"
    db.execute(sql, [title, author, user_id])

    sql_get_id = "SELECT id FROM books WHERE user_id = ? ORDER BY id DESC LIMIT 1"
    result = db.query(sql_get_id, [user_id])

    return result[0][0]

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
    result = db.query(sql, [book_id])
    return result[0] if result else None

def update_book(book_id, new_title, new_author):
    sql = """UPDATE books SET title = ?,
                    author = ?
                WHERE id = ?"""
    
    db.execute(sql, [new_title, new_author, book_id])

def remove_book(book_id):
    sql_categories = "DELETE FROM book_categories WHERE book_id = ?"
    db.execute(sql_categories, [book_id])

    sql_reviews = "DELETE FROM reviews WHERE book_id = ?"
    db.execute(sql_reviews, [book_id])

    sql_book = "DELETE FROM books WHERE id = ?"
    db.execute(sql_book, [book_id])

def find_book(query):
    sql = """SELECT id, title, author
             FROM books
             WHERE title LIKE ? OR author LIKE ?
             ORDER BY id DESC"""
    like = "%" + query + "%"
    return db.query(sql, [like, like])

def get_user_by_id(user_id):
    sql = """SELECT id, username, image IS NOT NULL AS has_image 
            FROM users WHERE id = ?"""
    result = db.query(sql,[user_id])
    return result[0] if result else None

def get_books_by_user(user_id):
    sql = "SELECT id, title, author FROM books WHERE user_id = ? ORDER BY id DESC"
    return db.query(sql,[user_id])

def add_review(book_id, user_id, rating, comment):
    sql = "INSERT INTO reviews (book_id, user_id, rating, comment) VALUES (?, ?, ?, ?)"
    db.execute(sql, [book_id, user_id, rating, comment])

def get_reviews(book_id):
    sql = """SELECT reviews.rating, reviews.comment, users.username
             FROM reviews, users
             WHERE reviews.user_id = users.id AND reviews.book_id = ?
             ORDER BY reviews.id DESC"""
    return db.query(sql,[book_id])

def get_categories():
    sql = "SELECT id, name FROM categories ORDER BY name"
    return db.query(sql)

def add_category_to_book(book_id, category_id):
    sql = "INSERT INTO book_categories (book_id, category_id) VALUES (?, ?)"
    db.execute(sql, [book_id, category_id])

def get_book_categories(book_id):
    sql = """SELECT categories.name
            FROM categories, book_categories
            WHERE categories.id = book_categories.category_id
            AND book_categories.book_id = ?
            ORDER BY categories.name"""
    return db.query(sql, [book_id])

def update_image(user_id, image):
    sql = "UPDATE users SET image = ? WHERE id = ?"
    db.execute(sql, [image, user_id])


def get_image(user_id):
    sql = "SELECT image FROM users WHERE id = ?"
    result = db.query(sql, [user_id])
    return result[0]["image"] if result and result[0]["image"] else None
