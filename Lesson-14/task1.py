class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Book(Product):
    def __init__(self, name, price, quantity, author):
        super().__init__(name, price, quantity)
        self.author = author

    def read(self):
        print(f"Book Title: {self.name}")
        print(f"Author: {self.author}")
        print(f"Price: ₴{self.price}")
        print(f"Quantity Available: {self.quantity}")

book1 = Book("Supernatural: Nevermore", 388, 336, "Tim Waggoner")
book2 = Book("Gulliver's Travels", 88, 144, "Jonathan Swift")


book1.read()
book2.read()