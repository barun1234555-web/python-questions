a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

# Pythonic way: a, b = b, a
# Mathematical way:
a = a + b
b = a - b
a = a - b

print(f"After swapping: a = {a}, b = {b}")