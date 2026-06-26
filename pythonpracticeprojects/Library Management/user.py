class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = [] #List to store borrowed books
        
    def borrow_books(self, book):
        if book.check_availability():
            self.borrowed_books.append(book)
            book.update_quantity(-1)
            return f"{self.user_id}:{self.name} borrowed '{book.title}'"
        else:
            return f"{book.title} is not available"
        
    def returning_books(self,book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.update_quantity(1)
            return f"{self.user_id}:{self.name} has returned '{book.title}'"
        else:
            return f"{book.title} is not been borrowed by {self.name}"
            
    def view_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name}'s Borrowed books: ")
            for book in self.borrowed_books:
                print(f"- {book.title}")
        
        else:
            print(f"{self.name} has not borrowed any books.")
            