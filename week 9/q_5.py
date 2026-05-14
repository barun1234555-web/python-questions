names = ["Alice", "Bob", "Charlie", "David", "Eve"]

# Writing to file
with open("students.txt", "w") as file:
    for name in names:
        file.write(name + "\n")

# Reading and displaying
print("Student Names from file:")
with open("students.txt", "r") as file:
    print(file.read())