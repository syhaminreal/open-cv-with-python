from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def generate_key():
    key = get_random_bytes(8)  # 8 bytes (64 bits) DES key
    return key

def encrypt(key, plaintext):
    cipher = DES.new(key, DES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), DES.block_size))
    return ciphertext

def decrypt(key, ciphertext):
    cipher = DES.new(key, DES.MODE_ECB)
    plaintext = unpad(cipher.decrypt(ciphertext), DES.block_size)
    return plaintext.decode()

if __name__ == '__main__':
    key = generate_key()
    print("DES Key:", key.hex())
    message = input("Enter a message to encrypt: ")
    
    ciphertext = encrypt(key, message)
    print("Encrypted message (in hex):", ciphertext.hex())
    
    decrypted_message = decrypt(key, ciphertext)
    print("Decrypted message:", decrypted_message)
