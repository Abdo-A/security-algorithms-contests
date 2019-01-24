temp = input()
temp = temp.split()
inputSize = int(temp[0])
outputSize = int(temp[1])

permutationBox = input()
permutationBox = permutationBox.split()

# converting items in the table to be numbers
for i, item in enumerate(permutationBox):
    permutationBox[i] = int(permutationBox[i])

impossible = False

# checking for error
passedNumbersArrayCheck = []

for i, item in enumerate(permutationBox):
    for item in passedNumbersArrayCheck:
        if item == permutationBox[i]:
            impossible = True

    passedNumbersArrayCheck.append(permutationBox[i])


# getting reversePermutationBox
reversePermutationBox = [None] * inputSize
if(not impossible):

    for i, item in enumerate(permutationBox):
        reversePermutationBox[i] = permutationBox.index(i+1)+1

    reversePermutationBoxString = ' '.join(
        str(n) for n in reversePermutationBox)

    print(reversePermutationBoxString)
else:
    print("IMPOSSIBLE")
