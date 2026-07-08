class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def show_info(self):
        print(f"Laptop Brand: {self.brand}, Price: ₹{self.price}")

laptop1 = Laptop("Dell", 45000)
laptop2 = Laptop("HP", 55000)

laptop1.show_info()
laptop2.show_info()