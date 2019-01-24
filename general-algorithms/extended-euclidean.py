from helpers import GetNumberInDomain
from helpers import ExtendedEuclidean

numbers = input().split()
domain = int(numbers[0])
n = int(numbers[1])

additiveInverse = 0
multiplicativeInverse = 0

# Get Multiplicative Inverse
multiplicativeInverse = ExtendedEuclidean(domain, n)
if(multiplicativeInverse):
    multiplicativeInverse = GetNumberInDomain(domain, multiplicativeInverse)

# Get Additive Inverse
additiveInverse = GetNumberInDomain(domain, n-2*n)


if(not multiplicativeInverse):
    print('IMPOSSIBLE')
else:
    print(additiveInverse, multiplicativeInverse)
