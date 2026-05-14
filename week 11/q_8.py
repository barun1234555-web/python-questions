def even_generator():
    for i in range(1, 101):
        if i % 2 == 0:
            yield i

print("Even numbers between 1 and 100:")
for num in even_generator():
    print(num, end=" ")