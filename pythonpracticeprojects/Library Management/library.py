from book import Book

class Library():
    def __init__(self):
        self.books = [] #to store all books available in the library 
        self.users = [] #to store memberships of users
        
    def add_books(self, book):
        self.books.append(book)
        
    def register_user(self, user):
        if any(curr_user.user_id == user.user_id for curr_user in self.users):
            print("User with the same ID already exists! Try another ID.")
            return
        self.users.append(user)
        print(f"New user {user.name} added successfully!")
        
    def search_book_by_title(self, title):
        found_books = [book for book in self.books if title.lower() in book.title.lower()]
        return found_books
    
    def list_books(self):
        if self.books:
            print("\n--- Books in the library ---")
            for book in self.books:
                print(book.display_info()) 
        else:
            print("No books available in library")
    
    def add_new_book(self):
        book_id = int(input("Enter book ID: "))
        if any(book.book_id == book_id for book in self.books):
            print("Book with the same ID already exists, please try another ID.")
            return

        title = input("Enter book title: ")
        author = input("Enter author name: ")
        quantity = int(input("Enter the quantity of books: "))
        
        new_book = Book(book_id, title, author, quantity)
        self.add_books(new_book) 
        print("Book added successfully!")
        print(new_book.display_info()) 