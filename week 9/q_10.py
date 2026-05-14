try:
    with open("students.txt", "r") as file:
        # enumerate starts at 1
        for line_no, line in enumerate(file, 1):
            if line_no % 2 == 0:
                print(f"Line {line_no}: {line.strip()}")
except FileNotFoundError:
    print("File not found.")