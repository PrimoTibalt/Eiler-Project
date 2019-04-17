def biggestCollatzSequence(maxNumber):
    higest = 0
    for number in range(1, maxNumber):
        copy = searchTheEnd(number, 1)
        if higest<copy:
            higest = copy

def searchTheEnd(number, iteration):
    while(number>1):
        number = int(number)
        if number % 2 == 0:
            number/=2
        else:
            number = 3*number + 1
        iteration += 1
    return iteration
biggestCollatzSequence(1000000)#не доделал