nums = [5, 12, 20, 33, 50, 55, 61]
div_by_5 = list(filter(lambda x: x % 5 == 0, nums))

print(f"Numbers divisible by 5: {div_by_5}")