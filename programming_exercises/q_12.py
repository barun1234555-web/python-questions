char = input("Enter a character: ").lower()

if char.isalpha() and len(char) == 1:
    if char in 'aeiou':
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Please enter a single alphabet letter.")