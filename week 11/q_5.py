n = int(input("Enter N: "))
# Generator expression
cubes = (x**3 for x in range(1, n + 1))

print(f"Cubes from 1 to {n}:")
for val in cubes:
    print(val, end=" ")