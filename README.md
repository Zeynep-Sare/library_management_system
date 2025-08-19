# 📘 Library_management_system

Python & FastAPI tabanlı kütüphane yönetim sistemi (3 aşamalı proje)

Bu proje, Python dili kullanılarak geliştirilmiş bir Kütüphane Yönetim Sistemi uygulamasıdır.
3 aşamalı proje kapsamında:
--Temel OOP (Nesne Tabanlı Programlama)
--API entegrasyonu (OpenLibrary)
--FastAPI ile REST API geliştirme
--Otomatik testler uygulamaları yapılmıştır

---

## 🚀 Proje İçeriği
🚀 Özellikler
📖 Kitap ekleme → ISBN numarasına göre OpenLibrary API’den kitap bilgilerini alır ve kütüphaneye ekler.

❌ Kitap silme → ISBN’e göre kitap silinir.

🔎 Kitap arama → ISBN ile kitap bulunur.

📚 Kitap listeleme → Tüm kitaplar listelenir.

↩️ Silinen kitabı geri yükleme

🧩 Veri modelleri → Book ve Library sınıfları ile nesne tabanlı yapı.

🌐 REST API → FastAPI framework kullanılarak uç noktalar sağlanır.

🧪 Testler → pytest kullanılarak birim testler ve API testleri yazılmıştır.

---

## 🛠️ Kullanılan Teknolojiler
- Python 3.10+  
- FastAPI  
- HTTPX (OpenLibrary API entegrasyonu için)  
- Pytest & Pytest (testler için)  
- Uvicorn (API sunucusu için)  

---

## 📂 Proje Dosya Yapısı
├── app.py                  # FastAPI uç noktaları

├── book.py                 # Book sınıfı

├── library.py              # Library sınıfı

├── main.py                 # Konsol uygulaması

├── requirements.txt        # Bağımlılıklar

│
├── test_book.py            # Book sınıfı testleri

├── test_library.py         # Library sınıfı testleri

├── test_library_api.py     # API fonksiyon testleri

├── test_api.py             # FastAPI endpoint testleri

├── test_library_save_load.py # JSON kaydetme/yükleme testleri

├── isbn_test.py            # ISBN testleri

Sanal Ortam için:
python -m venv venv
venv\Scripts\activate

Gereksinimleri yüklemek için:
pip install -r requirements.txt

FastAPI sunucusunu başlatmak için:
uvicorn app:app --reload
Tarayıcıda aç:  http://127.0.0.1:8000/docs

Testleri çalıştırmak için:
pytest -v
