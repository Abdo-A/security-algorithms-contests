

from helpers import DecimalToHex, HexToBinary, GetNumberInDomain

numbers = input().split()
number = int(numbers[0])
power = int(numbers[1])
domain = int(numbers[2])


powerBinary = HexToBinary(DecimalToHex(power))
reversedPowerBinaryList = list(powerBinary)
reversedPowerBinaryList.reverse()

# print(powerBinary)


# Dividing the power into its binary factors
valuesListForPower = []
digitValue = 1
for i in range(len(reversedPowerBinaryList)):
    # print('I am a ', reversedPowerBinaryList[i], 'my value is ', digitValue)
    if(reversedPowerBinaryList[i] == '1'):
        valuesListForPower.append(digitValue)
    digitValue = digitValue*2

# print(valuesListForPower)

# Getting the values for the power of these factors
powersValuesListForPower = []
currentPower = 1
while(currentPower <= valuesListForPower[len(valuesListForPower)-1]):
    if(currentPower == 1):
        currentPowerValue = GetNumberInDomain(domain, number)
    else:
        currentPowerValue = GetNumberInDomain(domain, currentPowerValue)
        # print("currentPowerValue", currentPowerValue)
        # print("currentPowerValue*currentPowerValue",
        #       currentPowerValue*currentPowerValue)
        currentPowerValue = GetNumberInDomain(
            domain, currentPowerValue*currentPowerValue)

    for i in range(len(valuesListForPower)):
        if(currentPower == valuesListForPower[i]):
            powersValuesListForPower.append(currentPowerValue)

    # print("currentPower", currentPower)
    # print("currentPowerValue", currentPowerValue)
    currentPower = currentPower*2

# Multiplying powersValuesListForPower to get the result
result = 1
for x in powersValuesListForPower:
    result = GetNumberInDomain(domain, result*x)

print(result)
