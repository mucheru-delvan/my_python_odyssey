from book import Book
from user import User
from library_management import Library


def main():
    print("📚Welcome to the Library Management System📚\n")
    library = Library()


    book1 = Book("1984", "George Orwell", "1234567890")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "0987654321")
    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", "1122334455")
    book4 = Book("Harry Potter", "J.K. Rowling", "2233445566")
    book5 = Book("The Hobbit", "J.R.R. Tolkien", "3344556677")
    book6 = Book("Pride and Prejudice", "Jane Austen", "4455667788")
    book7 = Book("The Catcher in the Rye", "J.D. Salinger", "5566778899")   
    book8 = Book("The Lord of the Rings", "J.R.R. Tolkien", "6677889900")
    book9 = Book("Animal Farm", "George Orwell", "7788990011")
    book10 = Book("Moby Dick", "Herman Melville", "8899001122") 
    book11 = Book("War and Peace", "Leo Tolstoy", "9900112233")
    book12 = Book("The Odyssey", "Homer", "1011121314") 
    book13 = Book("Crime and Punishment", "Fyodor Dostoevsky", "1213141516")
    book14 = Book("The Divine Comedy", "Dante Alighieri", "1314151617")
    book15 = Book("Brave New World", "Aldous Huxley", "1415161718")
    #print(book1)

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)
    library.add_book(book5)
    library.add_book(book6)
    library.add_book(book7)
    library.add_book(book8)
    library.add_book(book9)
    library.add_book(book10)
    library.add_book(book11)
    library.add_book(book12)
    library.add_book(book13)
    library.add_book(book14)
    library.add_book(book15)    


    user1 = User("Alice","U001")
    user2 = User("Melvin","U002")
    user3 = User("Charlie","U003")
    user4 = User("Diana","U004")
    user5 = User("Eve","U005")




    library.add_user(user1)
    library.add_user(user2)
    library.add_user(user3)
    library.add_user(user4)
    library.add_user(user5) 



    library.borrow_book("U002","The Great Gatsby") 

    library.return_book("U002","The Great Gatsby")

    library.borrow_book("U003","To Kill a Mockingbird")

    

    library.show_all_books()
    library.show_all_users()

    library.borrow_book("U001","1984")
    library.borrow_book("U001","The Hobbit")
    library.borrow_book("U001","Moby Dick")
    user1.show_books()

if __name__ == "__main__":
    main()