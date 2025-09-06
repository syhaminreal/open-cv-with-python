def mod_exp(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent //= 2
        base = (base * base) % modulus
    return result
def diffie_hellman_key_exchange(p, g, a, b):
    A = mod_exp(g, a, p)
    B = mod_exp(g, b, p)
    shared_secret_A = mod_exp(B, a, p)
    shared_secret_B = mod_exp(A, b, p)
    return shared_secret_A, shared_secret_B
p = int(input("Enter the prime no, greater prime is preferred:"))  # Prime number
g = int(input(f"Enter the primitive root of {p}, i.e G:"))  # Primitive root modulo p
a = int(input("Enter private secret for party A:"))   # Private secret for party A
b = int(input("Enter private secret for party B:"))   # Private secret for party B
shared_secret_A, shared_secret_B = diffie_hellman_key_exchange(p, g, a, b)
print("Shared secret for party A:", shared_secret_A)
print("Shared secret for party B:", shared_secret_B)