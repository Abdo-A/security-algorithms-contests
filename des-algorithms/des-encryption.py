from helpers import keyGeneration
from helpers import permutationBox
from helpers import HexToBinary
from helpers import DecimalToHex
from helpers import fFunction
from helpers import IP
from helpers import IP_1


initialKey = input()
initialInput = input()
numberOfEncryptions = int(input())


# loop 1
for i in range(numberOfEncryptions):
    input = permutationBox(64, IP, 64, initialInput)

    keys = keyGeneration(initialKey)

    for i in range(16):
        inputLeft = input[0:8]
        inputRight = input[8:16]

        fFunctionOutput = fFunction(inputRight, keys[i])

        XORoutputDecimal = int(HexToBinary(fFunctionOutput), 2) ^ int(
            HexToBinary(inputLeft), 2)

        XORoutputHex = DecimalToHex(XORoutputDecimal, 8)

        inputLeft = inputRight

        inputRight = XORoutputHex

        output = inputLeft+inputRight

        input = output

    temp = inputRight
    inputRight = inputLeft
    inputLeft = temp
    output = inputLeft+inputRight

    finalOutput = permutationBox(64, IP_1, 64, output)

    initialInput = finalOutput


if(numberOfEncryptions == 0):
    print(initialInput)
else:
    print(finalOutput)
