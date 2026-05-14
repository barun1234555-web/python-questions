longest_word = ""
try:
    with open("sample.txt", "r") as file:
        for line in file:
            words = line.split()
            for word in words:
                # Cleaning punctuation if necessary
                clean_word = word.strip(".,!?;:")
                if len(clean_word) > len(longest_word):
                    longest_word = clean_word
    print(f"The longest word is: {longest_word}")
except FileNotFoundError:
    print("The file was not found.")