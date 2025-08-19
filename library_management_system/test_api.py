import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_add_book_valid_isbn():
    response = client.post("/books", json={"isbn": "9780140449136"})
    assert response.status_code == 200
    data = response.json()
    assert "book" in data
    assert "Crime and punishment" in data["book"]

def test_add_book_invalid_isbn():
    response = client.post("/books", json={"isbn": "0000000000"})
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Kitap bulunamadı"

def test_list_book():
    response = client.get("/books")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
