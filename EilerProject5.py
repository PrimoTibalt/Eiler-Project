def minNumberToDivide():
    minNumber = 0
    number = 2520
    while(True):
        for i in [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]:
            if number % i == 0:
                if i == 20:
                    minNumber = number
                continue
            else:
                number += 20
                break
        if minNumber != 0:
            break
    print(minNumber)

minNumberToDivide()
