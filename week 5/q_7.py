my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
even_count = 0

for num in my_tuple:
    if num % 2 == 0:
        even_count += 1

print(f"Number of even numbers: {even_count}")