import requests
from PIL import Image
from io import BytesIO


class OpenLibraryAPI:
    baseurl = "https://openlibrary.org/isbn/"

    def get_book(self, isbn: str):
        info = {}
        #get the book info
        response = requests.get(self.baseurl + f"{isbn}.json")

        #error handling
        if response.status_code != 200:
            return None
        #parse the response
        response = response.json()
        author_key = response.get('authors')[0].get('key').lstrip('/authors')
        info['authors'] = self.get_authors(author_key)
        info['title'] = response.get('title')
        info['cover'] = self.get_covers(response.get('covers')[0])
        info['isbn'] = isbn

        return info

    def get_authors(self, key: str):
        url = f"https://openlibrary.org/authors/{key}.json"

        response = requests.get(url).json()

        return response.get('name')

    def get_covers(self, cover_id: str):
        url = f"https://covers.openlibrary.org/b/id/{cover_id}-M.jpg"
        response = requests.get(url)

        return response.url
