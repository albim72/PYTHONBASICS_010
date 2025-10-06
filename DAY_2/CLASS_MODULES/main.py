from book import Book
from library import Library

def main():
    #create Library
    my_library = Library()

    #create some Books
    b1 = Book("Pythom basics","Ann Blue",87)
    b2 = Book("Python for Data Science","Jane White",111)
    b3 = Book("Python for Machine Learning","Bruce White",100)

    #add books to the libraary
    my_library.add_book(b1)
    my_library.add_book(b2)
    my_library.add_book(b3)

    #list all books
    my_library.list_books()


if __name__ == '__main__':
    main()
