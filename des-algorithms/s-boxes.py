from helpers import HexToBinary
from helpers import BinaryToDecimal
from helpers import DecimalToHex
from helpers import sBoxes

inputHex = input()
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

print(output)
