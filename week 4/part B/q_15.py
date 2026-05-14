# Given list
data = [15, 22, 33, 48, 55, 60, 71, 80]

# List comprehension: keep 'num' only if it is NOT odd
filtered_list = [num for num in data if num % 2 == 0]

print(f"Original list: {data}")
print(f"List after removing odds: {filtered_list}")