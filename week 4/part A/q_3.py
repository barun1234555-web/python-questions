text = input("Enter a string: ").lower()

if text == text[::-1]:
    print("It is a Palindrome")
else:
    print("It is not a Palindrome")