my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
odd_count = 0

for num in my_tuple:
    if num % 2 != 0:
        odd_count += 1

print(f"Number of odd numbers: {odd_count}")