from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def generate_keypair():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def encrypt(public_key, message):
    key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(key)
    ciphertext = cipher.encrypt(message.encode())
    return ciphertext

def decrypt(private_key, ciphertext):
    key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(key)
    message = cipher.decrypt(ciphertext)
    return message.decode()

if __name__ == '__main__':
    private_key, public_key = generate_keypair()
    print("Public key: ", public_key.decode())
    print("Private key: ", private_key.decode())
    message = input("Enter a message to encrypt: ")
    encrypted_msg = encrypt(public_key, message)
    print("Encrypted message: ", encrypted_msg.hex())
    decrypted_msg = decrypt(private_key, encrypted_msg)
    print("Decrypted message: ", decrypted_msg)