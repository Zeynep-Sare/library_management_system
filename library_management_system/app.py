from fastapi import FastAPI
from pydantic import BaseModel
from library import Library

app = FastAPI()
lib = Library()

# ISBN body'den alınacak
class ISBNRequest(BaseModel):
    isbn: str

@app.get("/")
def read_root():
    return {"message": "Kütüphane API'sine hoş geldiniz!"}

@app.get("/books")
def list_books():
    return [str(book) for book in lib.list_books()]

@app.post("/books")
def add_book(req: ISBNRequest):
    book = lib.add_book(req.isbn)
    if book:
        return {"message": "Kitap eklendi", "book": str(book)}
    return {"message": "Kitap bulunamadı"}

@app.get("/books/{isbn}")
def find_book(isbn: str):
    book = lib.find_book(isbn)
    if book:
        return {"book": str(book)}
    return {"message": "Kitap bulunamadı"}

@app.delete("/books/{isbn}")
def remove_book(isbn: str):
    book = lib.remove_book(isbn)
    if book:
        return {"message": "Kitap silindi", "book": str(book)}
    return {"message": "Kitap bulunamadı"}
