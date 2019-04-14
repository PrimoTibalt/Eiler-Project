import math
def sumOfEspecialPiffagor(number):
    for i in range(1,400):
        for j in range(1,400):
            if i + j + math.sqrt(i**2 + j**2) == number:
                return i*j*math.sqrt(i**2 + j**2)

print(sumOfEspecialPiffagor(1000))