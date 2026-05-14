n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

if n1 == 0 or n2 == 0:
    print("Not a Multiple (division by zero)")
elif n1 % n2 == 0 or n2 % n1 == 0:
    print("Multiple")
else:
    print("Not a Multiple")