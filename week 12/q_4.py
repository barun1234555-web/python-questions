username = input("Enter Username: ")

if len(username) >= 5 and len(username) <= 15 and username[0].isalpha():
    print("Valid Username")
else:
    print("Invalid Username")