import os

def reverse_str(s):
    rs = ''
    for c in s:
        rs = c+rs
    return rs


def conv_str(some_list):
    c = ''
    for x in some_list:
        x = str(x)
        c += x
    return c


def encrypt(text, text_key, num_key, seperator='.'):
    encrypted_list = []

    keya = ''
    keyb = num_key

    for index, char in enumerate(text_key):
        index = int(index) + 1
        keya += str(int(ord(char) / index))
    
    keya = int(keya)

    for index, char in enumerate(text):
        index = int(index) + 1
        ascii_char = ord(char)
        encrypted_char = (ascii_char + keya) * (keyb + index) 
        encrypted_list.append(encrypted_char)
        encrypted_list.append(seperator)
    encrypted_string = reverse_str(conv_str(encrypted_list))
    return encrypted_string

def decrypt(encrypted_text, text_key, num_key, seperator='.'):
    try:
        keya = ''
        keyb = num_key

        for index, char in enumerate(text_key):
            index = int(index) + 1
            keya += str(int(ord(char) / index))
        
        keya = int(keya)

        rs = reverse_str(encrypted_text)
        list_to_decrypt = rs.split(seperator)
        decrypted_list = []

        for index, num in enumerate(list_to_decrypt):
            index = int(index) + 1
            if num == '':
                continue
            num = num.strip()
            encrypted_char = int(num)
            ascii_code = (encrypted_char/(keyb+index)) - keya
            ascii_code = int(round(ascii_code))
            char = chr(ascii_code)
            decrypted_list.append(char)
        decrypted_text = conv_str(decrypted_list)
        return decrypted_text
    except Exception as e:
        print('Failed to decrypt, check whether the keys are valid.')

def encrypt_file(filename, text_key, num_key, retain=True):
    encrypted_list = []
    with open(filename, 'r') as file:        
        for line in file:
            line = line.strip()
            encrypted_line = encrypt(line, text_key, num_key)
            encrypted_list.append(encrypted_line + '\n')
    with open(f'encrypted_{filename}', 'w') as encrypted_file:
        encrypted_file.writelines(encrypted_list)
    if not retain:
        os.remove(filename)

def decrypt_file(encrypted_filename, text_key, num_key, retain=True):
    decrypted_list = []
    
    with open(encrypted_filename, 'r') as file:
        filename = encrypted_filename.split('_')[1]
        for line in file:
            decrypted_line = decrypt(line, text_key, num_key)
            decrypted_list.append(decrypted_line + '\n')

    with open(filename, 'w') as decrypted_file:
                decrypted_file.writelines(decrypted_list)
    if not retain:
        os.remove(encrypted_filename)