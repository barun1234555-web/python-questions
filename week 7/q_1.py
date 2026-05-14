word_count = 0
try:
    with open("sample.txt", "r") as file:
        for line in file:
            words = line.split()
            word_count += len(words)
    print(f"Total number of words: {word_count}")
except FileNotFoundError:
    print("The file was not found.")