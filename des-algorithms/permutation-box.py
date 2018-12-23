from helpers import HexToBinary
from helpers import BinaryToHex

outputSize = int(input())

permutationBox = input()
permutationBox = permutationBox.split()

inputSize = int(input())
inputHex = input()
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

print(outputHex)
