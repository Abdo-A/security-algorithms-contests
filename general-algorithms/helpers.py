def HexToBinary(hex):
    return bin(int(hex, 16))[2:].zfill(len(list(hex))*4)


def BinaryToHex(binary):
    numberOfLeadingZeros = 0
    thereIsRest = False
    for item in list(binary):
        if item != '0':
            thereIsRest = True
            break
        numberOfLeadingZeros += 0.25
    numberOfLeadingZeros = int(numberOfLeadingZeros)

    leadingZeros = ''
    for i in range(numberOfLeadingZeros):
        leadingZeros += '0'

    rest = ''
    if thereIsRest:
        rest = hex(int(binary, 2)).split('x')[-1].upper()

    return leadingZeros+rest


def BinaryToDecimal(decimal):
    return int(decimal, 2)


def DecimalToHex(decimal, expectedOutputSize=0):
    result = hex(decimal).split('x')[-1].upper()
    if len(result) == 11 or len(result) == 7:
        result = '0'+result

    if expectedOutputSize > 0:
        while(len(result) < expectedOutputSize):
            result = '0'+result

    return result


def HexToDecimal(hex):
    return int(hex, 16)
