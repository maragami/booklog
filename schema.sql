CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
);

CREATE TABLE books (
    id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT,
    user_id INTEGER REFERENCES users
);

CREATE TABLE reviews (
    id INTEGER PRIMARY KEY,
    book_id INTEGER REFERENCES books,
    user_id INTEGER REFERENCES users,
    rating INTEGER,
    comment TEXT
);

CREATE TABLE categories (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE
);

CREATE TABLE book_categories (
    book_id INTEGER REFERENCES books,
    category_id INTEGER REFERENCES categories
);

INSERT INTO categories (name) VALUES ("Fantasia");
INSERT INTO categories (name) VALUES ("Scifi");
INSERT INTO categories (name) VALUES ("Historia");
INSERT INTO categories (name) VALUES ("Tietokirja");
INSERT INTO categories (name) VALUES ("Jännitys");
INSERT INTO categories (name) VALUES ("Manga");
INSERT INTO categories (name) VALUES ("Kauhu");
INSERT INTO categories (name) VALUES ("Romantiikka");