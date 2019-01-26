from helpers import XORbinary, HexToBinary, BinaryToHex, ShiftLeftString

numbers = input().split()
n1Hex = numbers[0]
n2Hex = numbers[1]
n1Bin = HexToBinary(n1Hex)
n2Bin = HexToBinary(n2Hex)
# print(n1Bin)
# print(n2Bin)

# Addition
AdditionResult = BinaryToHex(XORbinary(n1Bin, n2Bin, 8))

# Multiplication
shiftsList = []
shiftsList.append(n1Bin)
for i in range(8):
    if(i == 0):
        continue
    shouldXOR = False
    if(shiftsList[0][0] == '1'):
        shouldXOR = True
    shiftsList.insert(0, ShiftLeftString(shiftsList[0]))
    if(shouldXOR):
        shiftsList[0] = XORbinary(shiftsList[0], '00011011', 8)


n2BinList = list(n2Bin)
finalResult = '00000000'

for i in range(8):
    if(n2BinList[i] == '1'):
        # print("XOR between", finalResult, "and", shiftsList[i])
        finalResult = XORbinary(finalResult, shiftsList[i], 8)
        # print(finalResult)

MultiplicationResult = BinaryToHex(finalResult)

# print(shiftsList)
print(AdditionResult, MultiplicationResult)
