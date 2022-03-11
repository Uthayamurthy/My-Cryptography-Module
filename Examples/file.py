# Encryption and Decryption of File, demonstrates using the given test.txt file.
# crypto.py must be in the same directory as this file.
# The text file can be of any format.

from crypto import encrypt_file, decrypt_file

filename = 'test.txt' # Text to Encrypt
text_key = 'Secret'  # Text Key
num_key = 1729 # Numeric Key

# Encrypting a text file
encrypt_file(filename, text_key, num_key, retain=False) # retain when True, the original file is retained. True by default.

encrypted_filename = 'encrypted_' + filename

# Decrypting a text file
decrypt_file(encrypted_filename, text_key, num_key) # retain when True, the original file is retained. True by default.