# Original list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# List comprehension to pick even numbers
even_numbers = [num for num in numbers if num % 2 == 0]

print(f"Original list: {numbers}")
print(f"Even numbers: {even_numbers}")