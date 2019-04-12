def EvenFibonachi(number):
    sum = 0
    lastNum = 1
    secondNum = 0
    for i in range(0,number + 1):
        if lastNum + secondNum == i:
            secondNum = lastNum
            lastNum = i
            if i % 2 == 0:
                sum += i
    return sum
def EvenFibonachiV2(number):
    sum = 0
    lastNum = 1
    secondNum = 0
    while(True):
        buble = secondNum
        secondNum = lastNum
        lastNum += buble
        if lastNum <= number and lastNum % 2 == 0 :
            sum+=lastNum
        elif lastNum >= number :
            return sum


print(EvenFibonachi(4000000))
print(EvenFibonachiV2(4000000))
