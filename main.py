from ast import If
import aes
import md5
import md5salt
import sha256
import time

def main():
    # plaintext = 'passwordpassword'
    # key = 'informatika12345'
    # iv = 'aesencryptionmd5'

    print('==== AES >< MD5 ====')
    plaintext = input("Insert plaintext: ")
    print('\nPlaintext : ', plaintext)
    option = int(input("\n1. MD5 + AES\n2. SHA256\n3. MD5 + salt\nChoose(1, 2 or 3): "))
    
    if option == 1 :
        key = input("Insert key (key must be 16 char long): ")
        print('\nKey : ', key)
        iv = "aesencryptionmd5"
        print('\nDoing AES Encryption')

        time1 = time.process_time()
        for i in range(1000000):
            ciphertext = aes.aes_enc(aes.pad(plaintext), key, iv)
        time2 = time.process_time()

        print('\nCiphertext : ', ciphertext)

        print('\nDoing MD5 Hashing')
        print('\nPlaintext : ', ciphertext)
        
        time3 = time.process_time()
        for i in range(1000000):
            hash = md5.hashing(ciphertext)
        time4 = time.process_time()

        print('\nHash : '+ hash + '\n')

        time_elapsed = ((time2-time1)+(time4-time3))
        print(f'Time taken to do the AES + MD5 process is : {time_elapsed/1000000}\n')
    
    elif option == 2:
        time1 = time.process_time()
        for i in range(1000000):
            hash = sha256.hashing(plaintext)
        time2 = time.process_time()

        print('\nHash : '+ hash + '\n')

        time_elapsed = time2-time1
        print(f'Time taken to do the SHA256 process is : {time_elapsed/1000000}\n')
    
    elif option == 3:
        time1 = time.process_time()
        for i in range(1000000):
            hash = md5salt.hashing(plaintext)
        time2 = time.process_time()

        print('\nHash : '+ hash + '\n')
        
        time_elapsed = time2-time1
        print(f'Time taken to do the SHA256 process is : {time_elapsed/1000000}\n')

if __name__ == '__main__':
    main()
