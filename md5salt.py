from hashlib import md5
import secrets
import string

def hashing(plain_text):
    # generate 8 byte random salt and add it to plaintext
    salt = ''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(8))
    # salt = 'informatika12345'
    plain_text = plain_text + salt
    # encode the plaintext
    plain_text = plain_text.encode()
    
    # do the md5 hashing
    hash = md5(plain_text)

    # return the hex value
    return hash.hexdigest()

def main():
    plaintext = "oya jelek"
    hash = hashing(plaintext)

    print(plaintext)
    print(hash)

if __name__ == "__main__":
    main()
