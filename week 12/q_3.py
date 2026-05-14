import re

email = input("Enter Email: ")
pattern = r"^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$"

if re.match(pattern, email, re.IGNORECASE):
    print("Valid Email ID")
else:
    print("Invalid Email ID")