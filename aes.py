from base64 import b64encode, b64decode
from pydoc import plain
from Cryptodome.Cipher import AES

# AES encryption function
def pad(plain_text):
    # byte size that used to pad
    number_of_bytes = AES.block_size - len(plain_text) % AES.block_size
    # char for padding
    ascii_char = chr(number_of_bytes)
    # string : char as many as byte size
    padding_str = number_of_bytes * ascii_char
    # plaintext + padding string = padded plaintext
    padded_plain_text = plain_text + padding_str
    return padded_plain_text

def unpad(plain_text):
    # get char that used to pad
    last_char = plain_text[len(plain_text) - 1:]
    # get byte size for padding
    bytes_to_remove = ord(last_char)
    # delete char in the end of plaintext as many as byte size
    return plain_text[:-bytes_to_remove]

def aes_enc(plain_text, key, iv):
    # turn string into byte
    iv = iv.encode()
    key = key.encode()
    plain_text = plain_text.encode()
    
    # create cipher config
    cipher_config = AES.new(key, AES.MODE_CBC, iv=iv)

    # return cipher text
    cipher_text = cipher_config.encrypt(plain_text)

    return b64encode(cipher_text).decode()

def aes_dec(cipher_text, key, iv):
    iv = iv.encode()
    key = key.encode()
    cipher_text = b64decode(cipher_text)

    # create cipher config
    cipher_config = AES.new(key, AES.MODE_CBC, iv=iv)

    # return cipher text
    plain_text = cipher_config.decrypt(cipher_text)

    return plain_text.decode()

def main():
    iv = 'aesencryptionmd5'
    plaintext = 'passwordpassword'
    key = 'informatika12345'
    
    cipher = aes_enc(pad(plaintext),key,iv)
    plaintext = unpad(aes_dec(cipher,key,iv))
    print(cipher)
    print(plaintext)

if __name__ == "__main__":
    main()