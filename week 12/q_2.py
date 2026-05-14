import re

password = input("Enter password: ")
pattern = r"^[A-Za-z0-9@#$]+$"

if re.match(pattern, password):
    print("Valid: Contains only allowed characters.")
else:
    print("Invalid: Contains restricted characters.")