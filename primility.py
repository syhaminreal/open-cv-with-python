def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True

    # Check for divisibility by 2 or 3
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Check for divisibility by numbers of the form 6k ± 1
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

if __name__ == "__main__":
    num = int(input("Enter a number to check for primality: "))

    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")