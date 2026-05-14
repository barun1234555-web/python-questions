a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a == b:
    print(f"Equal number found: {a}")
elif a == c:
    print(f"Equal number found: {a}")
elif b == c:
    print(f"Equal number found: {b}")
else:
    print("No two numbers are equal.")