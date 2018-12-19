key = input()
plainText = input()
cipherText = ""


Matrix = [[0 for x in range(5)] for y in range(5)]

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

key = list(key)
plainText = list(plainText)

# Making sure to couple I and J
for i, letter in enumerate(key):
    if key[i] == "J":
        key[i] = "I"

for i, letter in enumerate(plainText):
    if plainText[i] == "J":
        plainText[i] = "I"


# Filling the matrix with the key
for i, row in enumerate(Matrix):
    for j, item in enumerate(row):
        while len(key) > 0 and key[0] not in alphabet:
            key.pop(0)

        if len(key) != 0 and key[0] in alphabet:
            Matrix[i][j] = key[0]
            alphabet.remove(Matrix[i][j])
            key.pop(0)


# Finishing filling the matrix
for i, row in enumerate(Matrix):
    for j, item in enumerate(row):
        if not Matrix[i][j]:
            Matrix[i][j] = alphabet[0]
            alphabet.pop(0)


# Improving plainText
for i, letter in enumerate(plainText):
    if i+1 < len(plainText) and plainText[i] == plainText[i+1] and not len(plainText[0: i]) % 2:
        if plainText[i] == 'X':
            plainText.insert(i+1, 'Q')
        else:
            plainText.insert(i+1, 'X')

if not len(plainText) % 2 == 0:
    if(plainText[len(plainText)-1] == "X"):
        plainText.append('Q')
    else:
        plainText.append('X')


# Making the couples array
plainTextCouplesArray = []
coupleTempArray = []
while(len(plainText) > 0):
    coupleTempArray.append(plainText[0])
    plainText.pop(0)

    if(len(plainText) > 0):
        coupleTempArray.append(plainText[0])
        plainText.pop(0)

    plainTextCouplesArray.append(coupleTempArray)
    coupleTempArray = []


# Converting the couples array to a string
plainTextCouples = ""

for plainTextCouple in plainTextCouplesArray:
    plainTextCouples += "".join(str(x) for x in plainTextCouple)


plainTextCouples = list(plainTextCouples)

rows = []
columns = []

for i, letter in enumerate(plainTextCouples):

    for lettersList in Matrix:
        if plainTextCouples[i] in lettersList:
            rows.append(Matrix.index(lettersList))
            columns.append(lettersList.index(plainTextCouples[i]))


for i, letterInfo in enumerate(plainTextCouples):

    if i % 2:
        continue
    row1 = rows[i]
    column1 = columns[i]

    otherLetterInfo = plainTextCouples[i+1]
    row2 = rows[i+1]
    column2 = columns[i+1]

    if(row1 == row2):
        cipherText += Matrix[row1][(column1+1) % 5]
        cipherText += Matrix[row2][(column2+1) % 5]
    elif(column1 == column2):
        cipherText += Matrix[(row1+1) % 5][column1]
        cipherText += Matrix[(row2+1) % 5][column2]
    else:
        cipherText += Matrix[row1][column2]
        cipherText += Matrix[row2][column1]


print(cipherText)
