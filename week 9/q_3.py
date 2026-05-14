try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    result = a * b
except ValueError:
    print("Error: Invalid input.")
else:
    # Runs only if no exception occurred
    print(f"Multiplication result: {result}")
finally:
    # Runs no matter what
    print("Execution complete.")