from helpers import HexToBinary
from helpers import BinaryToHex
from helpers import HexToBinary
from helpers import HexToDecimal
from helpers import DecimalToHex
from helpers import permutationBox


PC1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44,
       36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]

PC2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2,
       41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

keyRotations = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

keyInitialInputHex = input()

keyInputHex = permutationBox(56, PC1, 64, keyInitialInputHex)

key = keyInputHex


for i in range(16):

    keyLeft = key[0:7]
    keyRight = key[7:14]

    keyLeftBinary = HexToBinary(keyLeft)
    keyRightBinary = HexToBinary(keyRight)

    # print("before")
    # print(keyLeftBinary)

    # shift
    for i in range(keyRotations[i]):
        keyLeftBinary = keyLeftBinary[1:28]+keyLeftBinary[0]
        keyRightBinary = keyRightBinary[1:28]+keyRightBinary[0]

    # print("after")
    # print(keyLeftBinary)

    key = BinaryToHex(keyLeftBinary) + BinaryToHex(keyRightBinary)

    # print("BinaryToHex(keyLeftBinary) ")
    # print(BinaryToHex(keyLeftBinary))

    # print("key")
    # print(key)

    usedKey = permutationBox(48, PC2, 56, key)
    print(usedKey)
