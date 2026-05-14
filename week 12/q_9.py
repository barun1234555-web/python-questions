import re

pan = input("Enter PAN Card Number: ").upper()
pattern = r"^[A-Z]{5}[0-9]{4}[A-Z]{1}$"

if re.match(pattern, pan):
    print("Valid PAN Card Format")
else:
    print("Invalid PAN Card Format")