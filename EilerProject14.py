def biggestCollatzSequenceV2(maxNumber):
    itrList = []
    for number in range(1, maxNumber):
        iteration = 1
        while (number != 1):
            if number % 2 == 0:
                number >>= 1
            else:
                number = 3 * number + 1
            iteration += 1
        itrList.append(iteration)
    return max(itrList)


def biggestCollatzSequence(maxNumber):
    higest = 0
    for number in range(1, maxNumber):
        copy = searchTheEnd(number, 1)
        if higest<copy:
            higest = copy
    return higest

def searchTheEnd(number, iteration):
    while (number != 1):
        if number % 2 == 0:
            number >>= 1
        else:
            number = 3 * number + 1
        iteration += 1
    return iteration
print(biggestCollatzSequence(1000000))
