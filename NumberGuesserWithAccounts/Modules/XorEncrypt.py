from Modules.binary import XorBin,bin2int,int2bin

print()

def encrypt(msg,key):
    key = bin(key)[2::]
    NewEncrypedData = [None for i in range(len(msg))]
    for i in range(len(msg)):
        BinaryLetter = bin(ord(msg[i]))[2::]

        BinaryEncryptData = XorBin(BinaryLetter,key)

        NewEncrypedData[i] = chr(bin2int(BinaryEncryptData))
    
    return ''.join(NewEncrypedData)