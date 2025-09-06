def rail_fence_encrypt(plaintext, rails):
    rail_matrix = [['\n' for _ in range(len(plaintext))] for _ in range(rails)]
    direction = -1  # Direction for moving up or down
    row, col = 0, 0  # Initial position

    for char in plaintext:
        # Change direction if we reach the top or bottom rail
        if row == 0 or row == rails - 1:
            direction *= -1

        # Place the character in the current position
        rail_matrix[row][col] = char
        col += 1
        row += direction

    # Collect characters row by row to form the ciphertext
    ciphertext = []
    for r in rail_matrix:
        for char in r:
            if char != '\n':
                ciphertext.append(char)

    return ''.join(ciphertext)

def rail_fence_decrypt(ciphertext, rails):
    rail_matrix = [['\n' for _ in range(len(ciphertext))] for _ in range(rails)]
    direction = -1  # Direction for moving up or down
    row, col = 0, 0  # Initial position

    for _ in range(len(ciphertext)):
        # Change direction if we reach the top or bottom rail
        if row == 0 or row == rails - 1:
            direction *= -1

        # Mark the current position in the matrix
        rail_matrix[row][col] = '*'
        col += 1
        row += direction

    # Fill the matrix with ciphertext characters
    index = 0
    for r in rail_matrix:
        for j in range(len(r)):
            if r[j] == '*' and index < len(ciphertext):
                r[j] = ciphertext[index]
                index += 1

    # Read off the matrix column by column to form the plaintext
    plaintext = []
    col = 0
    for _ in range(len(ciphertext)):
        for r in rail_matrix:
            if r[col] != '\n':
                plaintext.append(r[col])
        col += 1

    return ''.join(plaintext)

# Example usage
plaintext = input("Enter the plain text:")  # The text you want to encrypt/decrypt
rails = int(input("Enter the no of rails/depth:"))  # Number of rails

# Encrypt the plaintext using Rail Fence cipher
encrypted_text = rail_fence_encrypt(plaintext, rails)
print("Encrypted:", encrypted_text)

# Decrypt the encrypted text using Rail Fence cipher
decrypted_text = rail_fence_decrypt(encrypted_text, rails)
print("Decrypted:", decrypted_text)