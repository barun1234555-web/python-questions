def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

n_terms = int(input("Enter number of Fibonacci terms: "))
a, b = 0, 1
fib_primes = []

for _ in range(n_terms):
    if is_prime(a):
        fib_primes.append(a)
    a, b = b, a + b

print(f"Prime Fibonacci numbers: {fib_primes}")