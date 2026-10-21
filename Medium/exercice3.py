class Book :
    def __init__(self, title, author, year,is_checked_out=False):
        self.title = title
        self.author = author
        self.year = year
        self.is_checked_out = is_checked_out

    def checkout(self):
        if not self.is_checked_out:
            self.is_checked_out = True

    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year}) - {'Checked out' if self.is_checked_out else 'Available'}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book.title, "-", "Checked out" if book.is_checked_out else "Available")

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None
    def available_books(self):
        return [book for book in self.books if not book.is_checked_out]

b1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
b2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
library = Library()
library.add_book(b1)
library.add_book(b2)   
print("List of books in the library:")
library.list_books() 

b1.checkout()
print("\nAfter checking out 'The Great Gatsby':")   
library.list_books()
b1.return_book()
print("\nAfter returning 'The Great Gatsby':")  
library.list_books()
print(b1.__str__())
book = library.find_book("To Kill a Mockingbird")
if book:
    print(f"\nFound book: {book.title} by {book.author} ({book.year}) - {'Checked out' if book.is_checked_out else 'Available'}")   
else:
    print("\nBook not found.")

availableBooks = library.available_books()
print(f"\nAvailable books in the library: {len(availableBooks)}")
print([book.title for book in availableBooks])


