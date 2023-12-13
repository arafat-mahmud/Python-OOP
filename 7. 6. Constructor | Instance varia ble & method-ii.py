class Book:
    def __init__(self, name,author):
        self.name = name
        self.authour = author
        self.price = 0

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price
    
    def details(self):
        print("Book Name:", self.name,
              "\nAuthor:", self.authour, 
              "\nprice: $", self.price)

b1 = Book("Rich dad poor dad", "Time Story")
b1.details()    # initial price because book price !=
b1.set_price(560)
#print(b1.get_price())
"""x=b1.get_price()
print(x)"""
b1.details()
