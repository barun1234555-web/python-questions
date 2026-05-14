source_file = "sample.txt"
destination_file = "copy.txt"

try:
    with open(source_file, "r") as src, open(destination_file, "w") as dest:
        for line in src:
            dest.write(line)
    print("File copied successfully.")
except FileNotFoundError:
    print("Source file not found.")