class User:
    def __init__(self,name,user_id):
        self.name = name 
        self.user_id = user_id
        self.borrowed_books = []


    def borrow_book(self,book):
        if book.borrow():
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed {book.title}")
            return True
        print(f"{book.title} is not available")
        return False
    
    def return_book(self,book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}")
            return True
        print(f"{self.name} doesn't have {book.title}")
        return False
    
    def show_books(self):
        if self.borrowed_books:
            print(f"{self.name}'s borrowed books:")
            for book in self.borrowed_books:
                print(f" - {book.title}")
        else:
            print(f"{self.name} has no borrowed books")
            