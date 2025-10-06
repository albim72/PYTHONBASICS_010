class Book:
    __cover_color = "blue" #private class

    def __init__(self, title, author, price, pages,bookstore_no):
        self.title = title
        self.author = author
        self.price = price
        self.pages = pages
        self.bookstore_no = bookstore_no
        self.binding = "softcover"
        self.new_book()

    def __repr__(self):
        return f"{self.__class__.__name__}({self.title}, {self.author}, {self.pages})"

    def new_book(self):
        """
        called when the new object of class book is created
        :return:
        """
        print("New book created - instance of Book class")

    def get_binding(self):
        return self.binding

    def set_binding(self, binding):
        self.binding = binding

    def apply_discount(self,percent=10):
        self.price = self.price - (self.price * percent / 100)
        return self.price

    def cover_color(self):
        return self.__cover_color



b1 = Book("Python for Beginners", "Marcin Albiniak", 122, 320, 556)
print(b1)
print(b1.get_binding())
b1.set_binding("paperback")
print(b1.get_binding())
print(f"price after discount: {b1.apply_discount(12)}")
