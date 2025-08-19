import json
from book import Book
import httpx

class Library:
    def __init__(self):
        self.books = []
        self.deleted_books = []

    def add_book(self, isbn: str):
        """ISBN'e göre Open Library API'den kitap bilgisi alıp kütüphaneye ekler"""
        url = f"https://openlibrary.org/isbn/{isbn}.json"

        try:
            response = httpx.get(url, follow_redirects=True, timeout=10)

            if response.status_code == 200:
                data = response.json()
                title = data.get("title", "Bilinmiyor")
                publisher = data.get("publishers", ["Bilinmiyor"])[0]
                year = data.get("publish_date", "Bilinmiyor")
                pages = data.get("number_of_pages", "Bilinmiyor")

                # Yazar(lar) bilgisi
                authors = []
                if "authors" in data:
                    for author_key in data["authors"]:
                        author_url = f"https://openlibrary.org{author_key['key']}.json"
                        author_resp = httpx.get(author_url)
                        if author_resp.status_code == 200:
                            author_data = author_resp.json()
                            author_name = author_data.get("personal_name") or author_data.get("name", "Bilinmiyor")
                            authors.append(author_name)

                author = ", ".join(authors) if authors else "Bilinmiyor"

                # Book nesnesi oluştur ve ekle
                book = Book(title, author, isbn, publisher, year, pages)
                self.books.append(book)
                print(f"{title} ({author}) kütüphaneye eklendi.")
                return book  # ✅ eklendi
            else:
                print("Kitap bulunamadı.")
                return None

        except Exception:
            print("API bağlantı hatası.")
            return None

    def remove_book(self,isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                self.deleted_books.append(book)
                print(f"{book.title} kütüphaneden silindi ve çöp kutusuna taşınmıştır")
                return book
        return  None

    def restore_book(self,book,isbn):
        for book in self.deleted_books:
            if book.isbn == isbn:
                self.books.append(book)
                self.deleted_books.remove(book)
                print(f"{book.title} geri yüklendi !")
                return book
        return None
        #print(f"{book.title} bulunamadı")

    def find_book(self,isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
            return None

    def list_books(self):
        if not self.books:
            print("kütüphanede henüz kitap bilgisi bulunmuyor")
            return []
        for book in self.books:
            print(book)
        return self.books

    def save_books(self,filename):
        with open(filename,"w",encoding="utf-8")as f:
            json.dump([book.__dict__ for book in self.books],f,ensure_ascii=False, indent=4)

    def load_books(self,filename):
        try:
            with open(filename,"r",encoding="utf-8")as f:
                data = json.load(f)
                self.books = [Book(**item)for item in data]
        except FileNotFoundError:
            print("dosya bulunamadı , boş kütüphane ile başlıyoruz")
