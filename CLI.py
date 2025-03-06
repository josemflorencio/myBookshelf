import argparse
from BookCollection import BookCollection


class CLI:
    def __init__(self):
        book_collection = BookCollection()

        self.parser = argparse.ArgumentParser(description='Book Collection Manager')
        self.subparser = self.parser.add_subparsers(dest='command', help='Available commands')

        # Add the get command
        self.get_parser = self.subparser.add_parser('get', help='Get a book by ISBN')
        self.get_parser.add_argument("isbn", help='The ISBN of the book you want to get')
        self.args = self.parser.parse_args()

        # Handle the get command
        if self.args.command == 'get':
            print(f"Getting book with ISBN: {self.args.isbn}")
            book_info = book_collection.get_book(self.args.isbn)
            info = {
                'isbn': book_info[0],
                'title': book_info[1],
                'author': book_info[2],
                'cover': book_info[3]
            }
            display = f"Title: {info['title']}\nAuthor: {info['author']}\nCover: {info['cover']}"
            if book_info is None:
                print("Book not found")
            else:
                print("Book info:\n" + display)
