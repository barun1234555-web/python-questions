my_tuple = (1, 2, 2, 3, 4, 4, 4, 5)

unique_tuple = tuple(set(my_tuple))

print(f"Original: {my_tuple}")
print(f"After removing duplicates: {unique_tuple}")