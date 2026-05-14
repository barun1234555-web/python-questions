password = input("Enter password: ")

if " " in password:
    print("Password Rejected: Cannot contain spaces.")
else:
    print("Password accepted (no spaces found).")