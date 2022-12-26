# this file is for xor 2 plaintext
def xorstr(s1,s2):
    str = []
    for a,b in zip(s1,s2):
        str.append(chr(ord(a) ^ ord(b)))
    
    str = "".join(str)
    return str

def main():
    s1 = "123"
    s2 = "abc"
    s3 = xorstr(s1,s2)
    
    print(s3)

if __name__ == "__main__":
    main()