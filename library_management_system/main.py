from book import Book
from library import Library
import httpx


def main():
    lib = Library()
    lib.load_books("books.json")
    kullanici_adi = input("lütfen adınızı giriniz:")
    print(f"Hosgeldiniz ,{kullanici_adi}.Kütüphane Yönetim Sistemi'ne giriş yaptınız.")
    while True:
        menu = """
        +-----------------------------------+
        |  Kütüphane Yönetim Sistemi        |
        +-----------------------------------+
        | 1. Kitap Ekle                     |
        | 2. Kitap Sil                      |
        | 3. Kitabı geri yükle              |
        | 4. Kitabı bul                     |
        | 5. Kitapları listele                |
        | 6. Cıkıs                          |
        +-----------------------------------+
        """
        print(menu)
        secim = input(f"{kullanici_adi}, lütfen secim yapin")

        if secim == "1":
            isbn = input("ISBN numarası: ")
            lib.add_book(isbn)

        elif secim == "2":
            isbn = input("Silmek istediğiniz kitabın isbn numarasını giriniz:")
            onay = input(f" isbn numarası {isbn} olan kitabı silmek istediğinizi onaylıyor musunuz? (e/h):").lower()
            if onay == "e":
                lib.remove_book(isbn)
            elif onay == "h":
                print("işlem iptal edildi")
            else:
                print("Geçersiz yanıt verdiniz. ")
        elif secim == "3":
            isbn = input("Geri getirmek istediğiniz kitabın isbn numarasını girin:")
            lib.restore_book(isbn)
        elif secim == "4":
            isbn = input("Aramak istediğiniz kitabın isbn numarası: ")
            found = lib.find_book(isbn)
            if found:
                print(found)
            else:
                print("kitap bulunamadı")
        elif secim == "5":
            lib.list_books()
        elif secim == "6":
            lib.save_books("books.json")
            print("Kütüphane kaydedildi. Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim! Lütfen 1-6 arasında bir sayı girin.")

if __name__ == "__main__":
    main()