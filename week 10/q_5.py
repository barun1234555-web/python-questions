class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_info(self):
        print(f"Car: {self.brand} {self.model}, Price: ${self.price}")

my_car = Car("Tesla", "Model S", 80000)
my_car.display_info()