# Encryption and Decryption of Text, demonstrates the text in the image of readme.
# crypto.py must be in the same directory as this file.

from crypto import encrypt, decrypt

text = 'Hello World' # Text to Encrypt
text_key = 'Secret'  # Text Key
num_key = 1729 # Numeric Key

# Encrypting Text
encrypted_text = encrypt(text, text_key, num_key)
print(encrypted_text)

# Decrypting Text
decrypted_text = decrypt(encrypted_text, text_key, num_key)
print(decrypted_text)