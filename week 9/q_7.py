new_data = input("Enter data to append: ")

with open("students.txt", "a") as file:
    file.write(new_data + "\n")

print("Data appended successfully.")