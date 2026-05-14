try:
    with open("sample.txt", "r") as file:
        data = file.read()
        char_count = len(data)
    print(f"Total number of characters: {char_count}")
except FileNotFoundError:
    print("The file was not found.")