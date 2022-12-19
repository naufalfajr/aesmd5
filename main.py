import aes
import md5
import md5salt
import sha256
import time

def main():
    print('==== AES >< MD5 ====')
    plaintext = input("Insert plaintext: ")
    option = int(input("\n1. MD5 + AES\n2. SHA256\n3. MD5 + salt\n4. MD5\nChoose(1, 2, 3 or 4): "))
    rep = 100000 # how many times process repeated

    if option == 1 :
        key = "semogasayasukses" # input("Insert key (key must be 16 char long): ")
        # iv = "messagedigestaes"

        time1 = time.process_time()
        # padded_plaintext = aes.pad(plaintext)
        # print(padded_plaintext)
        for i in range(rep):
            ciphertext = aes.aes_enc(plaintext, key)
        time2 = time.process_time()

        print('\nCiphertext : ', ciphertext)
        
        time3 = time.process_time()
        for i in range(rep):
            hash = md5.hashing(ciphertext)
        time4 = time.process_time()

        print('\nHash : '+ hash + '\n')

        time_elapsed = ((time2-time1)+(time4-time3))
        print(f'Time taken to do the AES + MD5 process is : {time_elapsed/rep}\n')
    
    elif option == 2:
        time1 = time.process_time()
        for i in range(rep):
            hash = sha256.hashing(plaintext)
        time2 = time.process_time()

        print('\nHash : '+ hash + '\n')

        time_elapsed = time2-time1
        print(f'Time taken to do the SHA256 process is : {time_elapsed/rep}\n')
    
    elif option == 3:
        time1 = time.process_time()
        for i in range(rep):
            hash = md5salt.hashing(plaintext)
        time2 = time.process_time()

        print('\nHash : '+ hash + '\n')
        
        time_elapsed = time2-time1
        print(f'Time taken to do the MD5 + salt process is : {time_elapsed/rep}\n')
    
    elif option == 4:
        time1 = time.process_time()
        for i in range(rep):
            hash = md5.hashing(plaintext)
        time2 = time.process_time()

        print('\nHash : '+ hash + '\n')
        
        time_elapsed = time2-time1
        print(f'Time taken to do the MD5 process is : {time_elapsed/rep}\n')

    else:
        print('wrong input, quitting.....\n')

if __name__ == '__main__':
    main()
