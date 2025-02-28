from OpenLibraryAPI import OpenLibraryAPI

def main():
    print('hello')
    api = OpenLibraryAPI()
    print(api.get_book("9781649377159"))
    print(api.get_authors("OL7825177A"))

if __name__ == "__main__":
    main()