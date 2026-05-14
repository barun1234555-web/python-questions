nums = [10, 15, 21, 30, 45, 50]
odds = list(filter(lambda x: x % 2 != 0, nums))

print(f"Original: {nums}")
print(f"Odd numbers: {odds}")