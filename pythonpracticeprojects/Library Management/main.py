from book import Book 
from user import User
from library import Library
def main():
    
    b1 = Book(234, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", 17)
    b2 = Book(756, "Twisted Lies", "Ana Huang", 9)
    b3 = Book(532, "Fourth Wing", "Rebecca Yarros", 11)
    print(b1.display_info())
    print(b2.display_info())
    print(b3.display_info())
    
if __name__ == "__main__":
    main()