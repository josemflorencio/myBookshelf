from OpenLibraryAPI import OpenLibraryAPI
from booksDB import booksDB
from MOCKDATA import MOCKDATA
from BookCollection import BookCollection
from CLI import CLI


def main():
    # Create an instance of the OpenLibraryAPI class and the booksDB class
    books = BookCollection()
    cli = CLI()


if __name__ == "__main__":
    main()
