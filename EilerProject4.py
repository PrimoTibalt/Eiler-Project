import math
def numberPolindrom():
    maxNumber = 12321
    for i in range (110,1000):
        for j in range (111, 1000):
            number = i*j
            number = str(number)
            for m in range(math.ceil(len(number)/2)):
                if int(number[m]) == int(number[len(number) - m - 1]):
                    if (m == math.ceil(len(number) / 2) - 1) and maxNumber < int(number):
                        maxNumber = int(number)
                else:
                    break;
    print(maxNumber)


numberPolindrom()