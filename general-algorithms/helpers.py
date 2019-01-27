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


def XORbinary(n1, n2, expectedOutputSize=0):
    result = ''
    for i in range(len(n1)):
        if((n1[i] == '0' and n2[i] == '0') or (n1[i] == '1' and n2[i] == '1')):
            result = result+'0'
        else:
            result = result+'1'
    if expectedOutputSize > 0:
        while(len(result) < expectedOutputSize):
            result = '0'+result
    return result


def ShiftLeftString(s):
    s = list(s)
    newS = ''
    for i in range(len(s)):
        if(i > 0):
            newS = newS+s[i]
    newS = newS+'0'
    return newS


def GetNumberInDomain(domain, number):
    if(number < domain and number >= 0):
        return number
    elif(number >= domain):
        # while(not(number < domain and number >= 0)):
            # print('stuck in condition 2')
            # number = number-domain
            # print("number", number)
        number = number % domain
        return number
    elif(number < 0):
        while(not(number < domain and number >= 0)):
            print('stuck in condition 3')
            number = number+domain
        return number


def ExtendedEuclidean(domain, number):
    A1, A2, A3, B1, B2, B3 = 1, 0, domain, 0, 1, number
    MI = False
    # print(A1, A2, A3, B1, B2, B3)
    while(1):
        A1Last = A1
        A2Last = A2
        A3Last = A3
        B1Last = B1
        B2Last = B2
        B3Last = B3
        A1, A2, A3 = B1Last, B2Last, B3Last
        B3 = A3Last % B3Last
        remainder = A3Last//B3Last
        B1 = A1Last-(remainder*A1)
        B2 = A2Last-(remainder*A2)
        # print(remainder, A1, A2, A3, B1, B2, B3)
        if(B3 == 1):
            MI = B2
            break
        elif(B3 == 0):
            break
    return MI
