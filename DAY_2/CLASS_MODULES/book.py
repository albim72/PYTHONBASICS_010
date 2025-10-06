class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        
    def info(self):
        return f"{self.title} by {self.author} costs {self.price}"
