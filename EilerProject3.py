import math
def CommonDivider(number):
    higestDiv = 1
    if number % 2 != 0:
        number -= 1
    else:
        higestDiv = 2
    for i in range(2,math.ceil(number / 3)):
        if i % 2 > 0 and i % 3 > 0 and i % 5 > 0 and (number+1) % i == 0 and IsItCommon(i) :
            higestDiv = i
            print(i)


def IsItCommon(number):
    for i in range(2,math.ceil(number / 2)+1):
        if number % i == 0:
            return False
    return True

#CommonDivider(600851475143)