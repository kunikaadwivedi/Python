from book import Book 
from user import User
from library import Library

def main():
    library = Library()
    
    b1 = Book(234, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", 17)
    b2 = Book(756, "Twisted Lies", "Ana Huang", 9)
    b3 = Book(532, "Fourth Wing", "Rebecca Yarros", 11)

    library.add_books(b1)
    library.add_books(b2)
    library.add_books(b3)

    # Registering users
    user1 = User(1, "Geek_1")
    user2 = User(2, "Geek_2")
    
    library.register_user(user1)
    library.register_user(user2)

    # Menu
    while True:
        print("\nWelcome to the Library Management System of KIKU")
        print("1. View all books")
        print("2. Add books")
        print("3. Search for a book by title")
        print("4. Borrow a book")
        print("5. Return a book")
        print("6. View borrowed books")
        print("7. Add new User")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            library.list_books()

        elif choice == '2':
            library.add_new_book()

        elif choice == '3':
            title = input("Enter the book title to search: ")
            found_books = library.search_book_by_title(title)
            if found_books:
                for book in found_books:
                    # FIXED: Added print() since display_info() returns a string
                    print(book.display_info()) 
            else:
                print(f"No books found with the title '{title}'.")

        elif choice == '4':
            user_id = int(input("Enter your user ID: "))
            book_id = int(input("Enter the book ID to borrow: "))
            user = next((u for u in library.users if u.user_id == user_id), None)
            book = next((b for b in library.books if b.book_id == book_id), None)
            if user and book:
                # FIXED: Added print() to capture the return message from the method
                print(user.borrow_books(book))
            else:
                print("Invalid user or book ID.")

        elif choice == '5':
            user_id = int(input("Enter your user ID: "))
            book_id = int(input("Enter the book ID to return: "))
            user = next((u for u in library.users if u.user_id == user_id), None)
            book = next((b for b in library.books if b.book_id == book_id), None)
            if user and book:
                # FIXED: Added print() to capture the return message from the method
                print(user.returning_books(book))
            else:
                print("Invalid user or book ID.")

        elif choice == '6':
            user_id = int(input("Enter your user ID: "))
            user = next((u for u in library.users if u.user_id == user_id), None)
            if user:
                user.view_borrowed_books()
            else:
                print("Invalid user ID.")

        elif choice == '7':
            id = int(input("Enter user id: "))
            name = input("Enter user's name: ")
            user = User(id, name)
            library.register_user(user)

        elif choice == '8':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")

    
if __name__ == "__main__":
    main()