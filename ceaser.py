def caesar_cipher(text, shift):
    result = ""  # Initialize an empty string to store the encrypted/decrypted text
    
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            # Determine whether the character is uppercase or lowercase
            if char.isupper():
                # Calculate the shifted character for uppercase letters
                shifted_char = chr((ord(char) - ord('A' ) + shift) % 26 + ord('A'))
            else:
                # Calculate the shifted character for lowercase letters
                shifted_char = chr((ord(char) - ord('a' ) + shift) % 26 + ord('a'))
            result += shifted_char  # Add the shifted character to the result
        else:
            result += char  # Keep non-letter characters as they are
    
    return result

    # Example usage
plaintext = input("Enter the plain text:")  # The text you want to encrypt/decrypt
shift = int(input("Enter the no of shift:"))  # The shift value (key) for encryption/decryption

# Encrypt the plaintext using Caesar cipher
encrypted_text = caesar_cipher(plaintext, shift)
print("Encrypted:", encrypted_text)

# Decrypt the encrypted text using Caesar cipher
decrypted_text = caesar_cipher(encrypted_text, -shift)
print("Decrypted:", decrypted_text)