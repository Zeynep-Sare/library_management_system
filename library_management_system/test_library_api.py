import pytest
from library import Library

def test_add_book_valid_isbn():
    lib = Library()
    isbn = "9780140449136"
    lib.add_book(isbn)

    found = lib.find_book(isbn)
    assert found is not None
    assert "Crime" in found.title or "Punishment" in found.title

def test_add_book_invalid_isbn(capfd):
    lib = Library()
    isbn = "0000000000"
    lib.add_book(isbn)

    found = lib.find_book(isbn)
    assert found is None

    captured = capfd.readouterr()
    assert "Kitap bulunamadı" in captured.out

#capfd konsola yazılan mesajı yakalar



