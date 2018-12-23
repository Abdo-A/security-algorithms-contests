############################## HELPERS START ##############################

from helpers import HexToBinary
from helpers import BinaryToDecimal
from helpers import BinaryToHex
from helpers import DecimalToHex
from helpers import sBoxes


def permutationBox(outputSize, permutationBox, inputSize, inputHex):

    inputBinaryArray = list(HexToBinary(inputHex))

    outputBinaryArray = [None] * outputSize

    # converting items in both tables to be numbers
    for i, item in enumerate(permutationBox):
        permutationBox[i] = int(permutationBox[i])

    for i, item in enumerate(inputBinaryArray):
        inputBinaryArray[i] = int(inputBinaryArray[i])

    for i, number in enumerate(permutationBox):
        outputBinaryArray[i] = inputBinaryArray[number-1]

    outputBinary = ''.join(str(n) for n in outputBinaryArray)

    outputHex = BinaryToHex(outputBinary)

    return outputHex


# print(permutationBox(8, [1, 1, 1, 1, 1, 1, 1, 1], 4, 'A'))

def sBox(inputHex):
    inputBinary = HexToBinary(inputHex)

    counter = 0

    output = []

    for i, bit in enumerate(inputBinary):
        if i % 6:
            continue

        row = BinaryToDecimal(inputBinary[i]+inputBinary[i+5])
        column = BinaryToDecimal(
            inputBinary[i+1]+inputBinary[i+2]+inputBinary[i+3]+inputBinary[i+4])

        singleOutputDecimal = sBoxes[counter][row][column]
        singleOutputHex = DecimalToHex(singleOutputDecimal)

        output.append(singleOutputHex)

        counter = counter+1

    output = ''.join(output)

    return output


############################## HELPERS END ##############################


inputHex = input()
keyHex = input()

EPTable = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17,
           16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]

straightBoxTable = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5,
                    18, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]

inputToXOR = permutationBox(48, EPTable, 32, inputHex)

XORoutputDecimal = int(HexToBinary(keyHex), 2) ^ int(
    HexToBinary(inputToXOR), 2)

XORoutputHex = DecimalToHex(XORoutputDecimal)

sBoxOutput = sBox(XORoutputHex)

finalOutput = permutationBox(32, straightBoxTable, 32, sBoxOutput)

print(finalOutput)
