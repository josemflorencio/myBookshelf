import sqlite3

class booksDB:
    def __init__(self):
        self.conn = sqlite3.connect('books.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS books
            (isbn TEXT PRIMARY KEY, title TEXT, author TEXT, cover TEXT)''')