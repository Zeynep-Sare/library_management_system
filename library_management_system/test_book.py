import pytest
from book import Book

#nesne oluşturduk
def test_book_creation():
    book = Book(
        title="1984",
        author="George Orwell",
        isbn="1234567890",
        publisher="Dorlion",
        year="1949",
        pages="328"
    )
#test etme kısmı
    assert book.title == "1984"
    assert book.author == "George Orwell"
    assert book.isbn == "1234567890"
    assert book.publisher == "Dorlion"
    assert book.year == "1949"
    assert book.pages == "328"

def test_book_str():
    book = Book(
        title="1984",
        author="George Orwell",
        isbn="1234567890",
        publisher="Dorlion",
        year="1949",
        pages="328"
    )

    result = str(book)
    assert "1984 by George Orwell" in result
    assert "Isbn: 1234567890" in result
    assert "Publisher: Dorlion" in result
    assert "Year: 1949" in result
    assert "Pages: 328" in result

