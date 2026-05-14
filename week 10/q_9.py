class Calculator:
    def add(self, a, b): return a + b
    def subtract(self, a, b): return a - b
    def multiply(self, a, b): return a * b
    def divide(self, a, b): 
        return a / b if b != 0 else "Cannot divide by zero"

calc = Calculator()
print(f"Add: {calc.add(10, 5)}, Divide: {calc.divide(10, 0)}")