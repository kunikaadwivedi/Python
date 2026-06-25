from book import Book 
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = [] #List to store borrowed books
        
    def borrow_books(self, Book):
        if Book.check_availability():
            self.borrowed_books.append(Book)
            Book.update_quantity(-1)
            return f"{self.user_id}:{self.name} borrowed '{Book.title}'"
            
            