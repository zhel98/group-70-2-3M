create_books_table = """
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER NOT NULL UNIQUE,
    title TEXT NOT NULL,
    author TEXT NOT NULL
)
"""

create_books_detail_table = """
CREATE TABLE IF NOT EXISTS books_detail (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER NOT NULL UNIQUE REFERENCES books(book_id),
    genre TEXT NOT NULL
)
"""

insert_book = """
INSERT INTO books (book_id, title, author)
VALUES (?, ?, ?)
"""

insert_book_detail = """
INSERT INTO books_detail (book_id, genre)
VALUES (?, ?)
"""

select_book_id = "SELECT 1 FROM books WHERE book_id = ?"

get_books = """
SELECT books.book_id, books.title, books.author, books_detail.genre
FROM books
INNER JOIN books_detail ON books.book_id = books_detail.book_id
ORDER BY books.book_id
"""
