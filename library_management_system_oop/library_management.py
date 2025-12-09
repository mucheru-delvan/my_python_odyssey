class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self,book):
        self.books.append(book)
        print(f"Added: {book.title}")