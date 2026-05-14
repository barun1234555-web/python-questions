my_tuple = (23, 89, 12, 45, 67)

max_val = my_tuple[0]
for num in my_tuple:
    if num > max_val:
        max_val = num

print(f"Maximum element is: {max_val}")