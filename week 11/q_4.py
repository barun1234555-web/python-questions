def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

n = int(input("Enter N: "))
for num in count_up_to(n):
    print(num, end=" ")