class Mobile:
    def __init__(self, company, ram, storage):
        self.company = company
        self.ram = ram
        self.storage = storage

    def print_specs(self):
        print(f"Mobile Specs -> Brand: {self.company}, RAM: {self.ram}GB, Storage: {self.storage}GB")

phone = Mobile("Samsung", 12, 256)
phone.print_specs()