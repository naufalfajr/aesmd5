from hashlib import sha256

def hashing(plain_text):
    # encode the plaintext
    plain_text = plain_text.encode()
    
    # do the md5 hashing
    hash = sha256(plain_text)

    # return the hex value
    return hash.hexdigest()

def main():
    plaintext = "oya jelek"
    hash = hashing(plaintext)

    print(plaintext)
    print(hash)

if __name__ == "__main__":
    main()