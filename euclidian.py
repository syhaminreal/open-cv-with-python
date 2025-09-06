def original_euclidean_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = int(input("Enter the 1st number (Greater than the 2nd number): "))
num2 = int(input("Enter the 2nd number: "))

if num1 < num2:
    print("The 1st number should be greater than the 2nd number.")
else:
    gcd = original_euclidean_gcd(num1, num2)
    print(f"GCD of {num1} and {num2}: {gcd}")