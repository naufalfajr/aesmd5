from base64 import b64encode, b64decode
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad

# AES encryption function

def aes_enc(plain_text, key):
    # turn string into byte
    key = key.encode()
    plain_text = plain_text.encode()
    
    # create cipher config
    cipher_config = AES.new(key, AES.MODE_ECB)

    # return cipher text
    cipher_text = cipher_config.encrypt(pad(plain_text, 16))

    return b64encode(cipher_text).decode()

def aes_dec(cipher_text, key):
    key = key.encode()
    cipher_text = b64decode(cipher_text)

    # create cipher config
    cipher_config = AES.new(key, AES.MODE_ECB)

    # return cipher text
    plain_text = unpad(cipher_config.decrypt(cipher_text), 16)

    return plain_text.decode()

def main():
    # iv = 'messagedigestaes'
    plaintext = 'komputer'
    key = 'semogasayasukses'
    
    cipher = aes_enc(plaintext,key)
    plaintext = aes_dec(cipher,key)
    print(cipher)
    print(plaintext)

if __name__ == "__main__":
    main()