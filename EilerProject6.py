import math
def diffBeetwSumSecondAndSecondSum():
    sumSecond = 0
    secondSum = 0
    for i in range (1, 101):
        sumSecond += i**2
        secondSum += i
    diff = sumSecond - secondSum ** 2
    return  math.fabs(diff)

print(diffBeetwSumSecondAndSecondSum())
