password = input("Enter password: ")

has_upper = any(char.isupper() for char in password)
has_digit = any(char.isdigit() for char in password)
has_len = len(password) >= 8

if has_upper and has_digit and has_len:
    print("Valid Password")
else:
    print("Invalid Password. Must be 8+ chars, have 1 uppercase and 1 digit.")