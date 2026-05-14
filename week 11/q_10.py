n = int(input("Enter N: "))
# Generator expression to find evens, then sum them
even_sum = sum(x for x in range(1, n + 1) if x % 2 == 0)

print(f"Sum of even numbers from 1 to {n}: {even_sum}")