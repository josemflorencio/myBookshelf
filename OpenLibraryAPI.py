import requests

class OpenLibraryAPI:
    baseurl = "https://openlibrary.org/isbn/"
    def get_book(self, isbn: str):

        info = {}

        print(self.baseurl+".json")
        response = requests.get(self.baseurl+f"{isbn}.json").json()

        author_key = response.get('authors')[0].get('key').lstrip('/authors')
        print(author_key)

        info['authors'] = self.get_authors(author_key)
        info['title'] = response.get('title')
        info['cover'] = response.get('covers')
        info['isbn'] = isbn

        return info

    def get_authors(self, key: str):
        url = f"https://openlibrary.org/authors/{key}.json"

        print(url)
        response = requests.get(url).json()

        return response.get('name')
    def get_covers(self):
        return