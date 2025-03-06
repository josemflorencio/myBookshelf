from OpenLibraryAPI import OpenLibraryAPI
from booksDB import booksDB
from MOCKDATA import MOCKDATA


def main():
    # Create an instance of the OpenLibraryAPI class and the booksDB class
    api = OpenLibraryAPI()
    db = booksDB()


if __name__ == "__main__":
    main()
