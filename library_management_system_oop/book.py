class Book:
    def __init__(self, title, author, isbn, publication_year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year
        self.is_available = True


    def __str__(self):
        availability = "Available" if self.is_available else "Checked Out"
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}, Year: {self.publication_year}) - {availability}"