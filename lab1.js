Theory (AES Algorithm in Simple Terms)

The Advanced Encryption Standard (AES) is a symmetric encryption algorithm widely used to secure sensitive data. "Symmetric" means the same secret key is used for both encryption and decryption. AES works on fixed-size data blocks (128 bits) and supports different key lengths — 128, 192, or 256 bits. In this code, a 128-bit key is generated using secure random bytes.

The code specifically uses AES in CBC (Cipher Block Chaining) mode. In CBC mode, each plaintext block is XORed with the previous ciphertext block before encryption, making patterns harder to detect. The process requires an Initialization Vector (IV), which ensures that the same plaintext encrypted multiple times results in different ciphertexts. Padding (via ) is also used because AES only encrypts data in fixed block sizes.pad

In practice, AES is considered highly secure and is widely adopted in applications like online banking, VPNs, disk encryption, and secure messaging. However, key management and secure storage of the IV are critical—losing the key or exposing it compromises the entire encryption system.