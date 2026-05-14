a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a > b: a, b = b, a
if a > c: a, c = c, a
if b > c: b, c = c, b

print(f"Ascending order: {a}, {b}, {c}")