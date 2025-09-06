import random

def is_prime_fermat(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    for _ in range(k):
        a = random.randint(2, n - 1)
        if pow(a, n - 1, n) != 1:
            return False
    return True

num = int(input("Enter the number: "))
print(f"{num} is prime:", is_prime_fermat(num))