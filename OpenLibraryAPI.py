import requests
from PIL import Image
from io import BytesIO


class OpenLibraryAPI:
    baseurl = "https://openlibrary.org/isbn/"

    def get_book(self, isbn: str):
        info = {}

        response = requests.get(self.baseurl + f"{isbn}.json").json()

        author_key = response.get('authors')[0].get('key').lstrip('/authors')

        info['authors'] = self.get_authors(author_key)
        info['title'] = response.get('title')
        info['cover'] = response.get('covers')
        info['isbn'] = isbn

        return info

    def get_authors(self, key: str):
        url = f"https://openlibrary.org/authors/{key}.json"

        response = requests.get(url).json()

        return response.get('name')

    def get_covers(self, cover_id: str):
        url = f"https://covers.openlibrary.org/b/id/{cover_id}-M.jpg"
        response = requests.get(url)

        img = Image.open(BytesIO(response.content))
        img.show()

        return response.text
