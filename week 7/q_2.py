line_count = 0
try:
    with open("sample.txt", "r") as file:
        for line in file:
            line_count += 1
    print(f"Total number of lines: {line_count}")
except FileNotFoundError:
    print("The file was not found.")