class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self,book):
        self.books.append(book)
        print(f"Added: {book.title}")

    def add_user(self,user):
        self.users.append(user)
        print(f"Added user: {user.name}")

    def find_book(self,title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None
    
    def find_user(self,user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None
    
    def show_all_books(self):
        print("\nAll books in library:")
        for book in self.books:
            print(f"-{book}")

    def show_all_users(self):
        print("\nAll Users:")
        for user in self.users:
            borrowed = len(user.borrowed_books)
            print(f" - {user.name} (ID: {user.user_id}) - Borrowed: {borrowed} books")

    def borrow_book(self,user_id,book_title):
        user = self.find_user(user_id)
        book = self.find_book(book_title)

        if user and book:
            return user.borrow_book(book)
        elif not user:
            print(f"User {user_id} not found!")
        elif not book:
            print(f"Book '{book_title}' not found!")
        return False
    
    def return_book(self,user_id,book_title):
        user = self.find_user(user_id)
        book = self.find_book(book_title)

        if user and book:
            return user.return_book(book)
        elif not user:
            print(f"User {user_id} not found!")
        elif not book:
            print(f"Book '{book_title}' not found!")
        return False
            
    