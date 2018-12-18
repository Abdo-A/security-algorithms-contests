key = input()
plainText = input()

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

vigenereCiphertext = ""
vernamCiphertext = ""

# Making key array that has the same length as plaintext
keyPointer = 0
keyArray = []
for plainTextLetter in plainText:
    keyArray.append(key[keyPointer])
    keyPointer += 1
    keyPointer = keyPointer % len(key)


######## vigenere ########

# Calculating vigenere cipher text
for plainTextLetter, keyLetter in zip(plainText, keyArray):

    plainTextLetterIndex = alphabet.index(plainTextLetter)

    keyLetterIndex = alphabet.index(keyLetter)

    cipherTextLetterIndex = (plainTextLetterIndex+keyLetterIndex) % 26

    cipherTextLetter = alphabet[cipherTextLetterIndex]

    vigenereCiphertext += cipherTextLetter


######## vernam ########

# Making an array of ascii codes of both plainText and keyArray
vernamCiphertextArray = []
for plainTextLetter, keyLetter in zip(plainText, keyArray):
    plainTextLetterASCII = ord(plainTextLetter)
    keyLetterASCII = ord(keyLetter)

    cipherTextLetterDecimal = plainTextLetterASCII ^ keyLetterASCII
    cipherTextLetterHEXA = hex(cipherTextLetterDecimal).split('x')[-1].upper()

    if len(cipherTextLetterHEXA) == 1:
        cipherTextLetterHEXA = "0"+cipherTextLetterHEXA

    vernamCiphertextArray.append(cipherTextLetterHEXA)
    vernamCiphertext = ''.join(vernamCiphertextArray)


######## one time pad decision ########
oneTimePadDecision = "NO"
if len(key) == len(plainText):
    oneTimePadDecision = "YES"


print("Vigenere: "+vigenereCiphertext)
print("Vernam: "+vernamCiphertext)
print("One-Time Pad: "+oneTimePadDecision)
