key = int(input())
plainText = input()

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

ciphertext = ""

for plainTextLetter in plainText:

    plainTextLetterIndex = alphabet.index(plainTextLetter)

    cipherTextLetterIndex = (plainTextLetterIndex+key) % 26

    cipherTextLetter = alphabet[cipherTextLetterIndex]

    ciphertext += cipherTextLetter

print(ciphertext)
