from math import radians
from os import read
from random import randint
from binascii import hexlify, unhexlify

def generateRandomInt():
    return randint(0, 255)

def readBinary(path: str):
    data:bytes
    with open(path, "rb") as file:
        data = file.read()       
    return data

def writeBinary(data: bytes, path: str):
    with open(path, 'wb') as file:
        file.write(data)
    return 0

def bytesToIntArray(data: bytes):
    dataArray: list = []
    for d in data:
        dataArray.append(d)
    return dataArray
    
def intBytesToCharBytes(data: list):
    fromArray: list = []
    for a in data:
        fromArray.append(a.to_bytes(1, "big"))
    return fromArray

def fromListOfBytesToBytes(data: list):
    return b''.join(data)

def main():
    data: bytes = bytesToIntArray(readBinary("ANDRES HERNANDEZ MATA - Encrypted.lock"))
    key: bytes = readBinary("ANDRES HERNANDEZ MATA - Key.lock")
    unencrypted: list = []
    i = 0
    for i in range(1, 1128):
        unencrypted.append((data[i] - int(key.decode())) % 256)
        i+=1
    with open('ANDRES HERNANDEZ MATA - ROT.txt', 'wb') as file:
        file.write(fromListOfBytesToBytes(intBytesToCharBytes(unencrypted)))

if __name__ == "__main__":
    main()