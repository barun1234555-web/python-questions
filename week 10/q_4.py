class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance!")

    def display_balance(self):
        print(f"Current Balance: {self.balance}")

account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
account.display_balance()