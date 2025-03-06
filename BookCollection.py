from booksDB import booksDB
from OpenLibraryAPI import OpenLibraryAPI


class BookCollection:
    def __init__(self):
        self.db = booksDB()
        self.api = OpenLibraryAPI()

    def get_book(self, isbn):
        book = self.db.get_book(isbn)
        if book is None:
            return None
        return book
