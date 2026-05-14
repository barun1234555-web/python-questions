def word_generator(file_name):
    try:
        with open(file_name, 'r') as file:
            for line in file:
                yield len(line.split())
    except FileNotFoundError:
        print("File not found.")

total_words = sum(word_generator("sample.txt"))
print(f"Total word count: {total_words}")