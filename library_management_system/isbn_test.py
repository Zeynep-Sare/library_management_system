import httpx

isbn = input("ISBN numarasını girin: ")
url = f"https://openlibrary.org/isbn/{isbn}.json"

try:
    response = httpx.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()

    print("\n--- Kitap Bilgileri ---")
    print("Başlık:", data.get("title", "Bilinmiyor"))
    publishers = data.get("publishers")
    print("Yayınevi:", publishers[0] if publishers else "Bilinmiyor")
    print("Basım yılı:", data.get("publish_date", "Bilinmiyor"))
    print("Sayfa sayısı:", data.get("number_of_pages", "Bilinmiyor"))

except httpx.RequestError:
    print("İnternet bağlantısı yok veya API'ye ulaşılamıyor.")
except httpx.HTTPStatusError:
    print("Kitap bulunamadı.")
