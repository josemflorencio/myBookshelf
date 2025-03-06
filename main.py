from OpenLibraryAPI import OpenLibraryAPI
from booksDB import booksDB


def main():
    print('hello')
    # Create an instance of the OpenLibraryAPI class
    api = OpenLibraryAPI()
    print(api.get_book("9781649377159"))
    print(api.get_authors("OL7825177A"))
    print(api.get_covers("14839882"))

    db = booksDB()
    print(db.add_book(api.get_book("9781649377159")))

if __name__ == "__main__":
    main()