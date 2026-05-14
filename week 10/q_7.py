class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print(f"Book: '{self.title}' by {self.author}, Price: ${self.price}")

b = Book("The Great Gatsby", "F. Scott Fitzgerald", 15)
b.display_details()