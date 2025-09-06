import random
def is_probably_prime(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    # Write n - 1 as 2^s * d, where d is odd
    s = 0
    d = n - 1
    while d % 2 == 0:
        s += 1
        d //= 2
    # Witness loop
    for _ in range(k):
        a = random.randint(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = (x ** 2) % n
            if x == n - 1:
                break
            else:
                return False  
    return True  

num = int(input("Enter the number:"))
print(f"{num} is probably prime:", is_probably_prime(num))