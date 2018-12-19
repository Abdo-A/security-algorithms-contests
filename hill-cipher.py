# Taking key
keySize = int(input())
key = input()

keyArray = key.split()
for i, letter in enumerate(keyArray):
    keyArray[i] = int(keyArray[i]) % 26


# Taking plainText

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

plainText = input()
plainTextArray = list(plainText)
for i, letter in enumerate(plainTextArray):
    plainTextArray[i] = alphabet.index(letter)

cipherTextArray = []

# Getting the width of the matrix
number = 100000
while number > 0:
    number = number-1
    if number**2 == keySize:
        break
matrixWidth = number

# Polishing keyArray
keyArray2d = []
for i, number in enumerate(keyArray):
    if i % matrixWidth == 0:
        tempArr = []
        for x in range(matrixWidth):
            tempArr.append(keyArray[i+x])
        keyArray2d.append(tempArr)

# Polishing plainTextArray

while len(plainTextArray) % matrixWidth != 0:
    plainTextArray.append(23)

plainTextArray2d = []
for i, number in enumerate(plainTextArray):
    if i % matrixWidth == 0:
        tempArr = []
        for x in range(matrixWidth):
            tempArr.append(plainTextArray[i+x])
        plainTextArray2d.append(tempArr)


# Calculating cipherText
for i, plainTextArray in enumerate(plainTextArray2d):
    for j, plainTextNumber in enumerate(plainTextArray):
        cipherTextNumber = 0
        for x in range(matrixWidth):
            cipherTextNumber += keyArray2d[j][x]*plainTextArray[x]
        cipherTextArray.append(cipherTextNumber % 26)

# print(matrixWidth)
# print(keyArray)
# print(keyArray2d)
# print(plainTextArray)
# print(plainTextArray2d)

# Converting cipher numbers to text
for i, letter in enumerate(cipherTextArray):
    cipherTextArray[i] = alphabet[letter]

cipherText = ''.join(cipherTextArray)
print(cipherText)
