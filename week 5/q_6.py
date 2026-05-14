my_tuple = (23, 89, 12, 45, 67)

min_val = my_tuple[0]
for num in my_tuple:
    if num < min_val:
        min_val = num

print(f"Minimum element is: {min_val}")