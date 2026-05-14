text = input("Enter string: ")

has_upper = any(c.isupper() for c in text)
has_lower = any(c.islower() for c in text)
has_digit = any(c.isdigit() for c in text)

if has_upper and has_lower and has_digit:
    print("The string contains all required types.")
else:
    print("Missing one or more requirements (Upper, Lower, or Digit).")