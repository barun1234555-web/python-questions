try:
    with open("students.txt", "r") as source:
        content = source.read()
        
    with open("backup.txt", "w") as destination:
        destination.write(content)
        
    print("File copied to backup.txt.")
except FileNotFoundError:
    print("Source file not found.")