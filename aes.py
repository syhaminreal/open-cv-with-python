from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def generate_key():
    key = get_random_bytes(16)  # 16 bytes (128 bits) AES key
    return key

def encrypt(key, plaintext):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    return ciphertext, cipher.iv

def decrypt(key, ciphertext, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext.decode()

if __name__ == '__main__':
    key = generate_key()
    print("AES Key:", key.hex())
    message = input("Enter a message to encrypt: ")
    
    ciphertext, iv = encrypt(key, message)
    print("Encrypted message (in hex):", ciphertext.hex())
    print("Initialization Vector (IV):", iv.hex())
    
    decrypted_message = decrypt(key, ciphertext, iv)
    print("Decrypted message:", decrypted_message)
