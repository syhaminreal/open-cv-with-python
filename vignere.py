def vigenere_cipher(text, key, mode):
    result = ""  # Initialize an empty string to store the encrypted/decrypted text
    key = key.upper()  # Convert the key to uppercase for consistency
    
    for i, char in enumerate(text):
        if char.isalpha():  # Check if the character is a letter
            key_shift = ord(key[i % len(key)]) - ord('A')  # Calculate the shift from the key
            
            if char.isupper():
                shifted_char = chr((ord(char) - ord('A') + mode * key_shift) % 26 + ord('A'))
            else:
                shifted_char = chr((ord(char) - ord('a') + mode * key_shift) % 26 + ord('a'))
            result += shifted_char
        else:
            result += char  # Keep non-letter characters as they are
    
    return result

    # Example usage
plaintext = input("Enter the text:")  # The text you want to encrypt/decrypt
key = input("Enter the key:")  # The encryption/decryption key
mode = 1 # 1 for encryption, -1 for decryption

# Encrypt the plaintext using Vigenère cipher
encrypted_text = vigenere_cipher(plaintext, key, mode)
print("Encrypted:", encrypted_text)

# Decrypt the encrypted text using Vigenère cipher
decrypted_text = vigenere_cipher(encrypted_text, key, -mode)
print("Decrypted:", decrypted_text)

