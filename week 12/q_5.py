phone = input("Enter phone number: ")

if phone.isdigit() and len(phone) == 10:
    print("Valid Phone Number")
else:
    print("Invalid Phone Number (must be exactly 10 digits)")