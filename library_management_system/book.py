class Book:
    def __init__(self,title,author,isbn,publisher,year,pages):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publisher = publisher
        self.year = year
        self.pages = pages

    def __str__(self):
        return (f"{self.title} by {self.author} "
                f"( Isbn: {self.isbn}) | "
                f" Publisher: {self.publisher} | "
                f"Year: {self.year} | "
                f"Pages: {self.pages}")
