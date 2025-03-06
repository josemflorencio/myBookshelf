import sqlite3

class booksDB:
    def __init__(self):
        self.conn = sqlite3.connect('books.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS books
            (isbn TEXT PRIMARY KEY, title TEXT, author TEXT, cover TEXT)''')

    def add_book(self, book):
        self.cursor.execute("INSERT INTO books VALUES (?, ?, ?, ?)", (book['isbn'], book['title'], book['authors'], book['cover']))
        self.conn.commit()
