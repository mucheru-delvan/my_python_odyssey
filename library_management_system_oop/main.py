from book import Book
from user import User

book1 = Book("1984", "George Orwell", "1234567890")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "0987654321")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", "1122334455")
#print(book1)

user1 = User("Alice", "U001")
user1.borrow_book(book1)
user1.borrow_book(book2)
user1.return_book(book1)
user1.borrow_book(book3)
user1.show_books()