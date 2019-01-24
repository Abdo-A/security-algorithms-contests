numbers = input().split()
n1 = int(numbers[0])
n2 = int(numbers[1])

if(n2 > n1):
    temp = n1
    n1 = n2
    n2 = temp

while(1):
    remainder = n1 % n2
    if(remainder == 0):
        break
    n1 = n2
    n2 = remainder

print(n2)
