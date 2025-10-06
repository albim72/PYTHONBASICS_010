from book import Book

class Library:
    def __init__(self):
        self.books = [] #empty list of the books

    def add_book(self, book:Book):
        """Adds a book to the library"""
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def list_books(self):
        """displays the list of books in the library"""
        if not self.books:
            print("The library is empty.")
        else:
            print("The library contains the following books:")
            for book in self.books:
                print(f"- {book.info()}")
