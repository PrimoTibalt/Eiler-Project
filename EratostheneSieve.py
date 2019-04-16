import math
def Sieve(maxNum):
    '''return list with maxNum of privary numbers'''
    arrayOfNumbers = list(range(maxNum+1))
    for i in range(math.floor((maxNum+1)/2)):
        if(arrayOfNumbers[i] != 0):
            if i % 2 == 0:
                arrayOfNumbers[i * 2] = 0
            elif i % 3 == 0 and maxNum / i > 3:
                arrayOfNumbers[i * 3] = 0
            elif i % 5 == 0 and maxNum / i > 5:
                arrayOfNumbers[i * 5] = 0
            elif i % 7 == 0 and maxNum / i > 7:
                arrayOfNumbers[i * 7] = 0
    return set(arrayOfNumbers)