import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

key = AESGCM.generate_key(bit_length=256)

aes = AESGCM(key)

nonce = os.urandom(12)
message = b"Hello My name is Tarok Halder"
ciphertext = aes.encrypt(nonce, message, None)

print("Original:", message)
print("Encrypted:", ciphertext.hex())

decrypted = aes.decrypt(nonce, ciphertext, None)

print("Decrypted:", decrypted.decode())
