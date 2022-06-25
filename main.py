import aes
import md5
import time

def main():
    plaintext = 'passwordpassword'
    key = 'informatika12345'
    iv = 'aesencryptionmd5'

    print('==== AES >< MD5 ====')
    
    print('\nDoing AES Encryption')
    print('\nPlaintext : ', plaintext)

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
    print(f'Time taken to do the AES + MD5 process is : {time_elapsed}\n')

if __name__ == '__main__':
    main()
