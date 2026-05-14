vowels = "aeiouAEIOU"
vowel_count = 0

try:
    with open("sample.txt", "r") as file:
        for line in file:
            for char in line:
                if char in vowels:
                    vowel_count += 1
    print(f"Total number of vowels: {vowel_count}")
except FileNotFoundError:
    print("The file was not found.")