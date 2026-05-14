nums = [23, 45, 12, 67, 8, 90, 34]

largest = nums[0]
smallest = nums[0]

for x in nums:
    if x > largest:
        largest = x
    if x < smallest:
        smallest = x

print(f"List: {nums}")
print(f"Largest element: {largest}")
print(f"Smallest element: {smallest}")