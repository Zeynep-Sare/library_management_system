import os
from book import Book
from library import Library

def test_library_save_load(tmp_path):
    file_path = tmp_path / "books.json"

    #kütüphane oluşturup kitap ekledik ve kaydettik
    lib = Library()
    book = Book("1984", "George Orwell", "1234567890", "Dorlion", "1949", "328")
    lib.add_book(book)
    lib.save_books(file_path)

    #dosyanın olup olmadığını anlamak için yazdık
    assert file_path.exists()

    #kütüphane oluşturuyoruz yeniden ama bu sefer yükleme kısmı için
    new_lib = Library()
    new_lib.load_books(file_path)

    #yüklendi mi diye kontrol ediyoruz
    load_book = new_lib.find_book("1234567890")
    assert load_book is not None
    assert load_book.title == "1984"
