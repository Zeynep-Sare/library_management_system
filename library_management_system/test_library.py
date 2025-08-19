import pytest
from book import Book
from library import Library

def test_add_book_and_find_book():
    lib = Library()
    book =  Book("1984", "George Orwell", "1234567890", "Dorlion", "1949", "328")
    lib.add_book(book)

    found = lib.find_book("1234567890")
    assert found is not None
    assert found.title == "1984"

def test_remove_book():
    lib = Library()
    book = Book("1984", "George Orwell", "1234567890", "Dorlion", "1949", "328")
    lib.add_book(book)
    lib.remove_book("1234567890") is None
    assert len(lib.deleted_books) == 1

def restore_book():
    lib = Library
    book = Book("1984", "George Orwell", "1234567890", "Dorlion", "1949", "328")
    lib.add_book(book)

    lib.remove_book("1234567890")
    lib.restore_book("1234567890")

    restored = lib.find_book("1234567890")
    assert restored is not None
    assert restored.title == "1984"


