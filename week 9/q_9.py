search_word = input("Enter the word to search: ")
count = 0

try:
    with open("students.txt", "r") as file:
        for line in file:
            words = line.split()
            for word in words:
                if word.strip(".,!").lower() == search_word.lower():
                    count += 1
    print(f"The word '{search_word}' appears {count} times.")
except FileNotFoundError:
    print("File not found.")