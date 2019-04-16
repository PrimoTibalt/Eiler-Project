import math
def sumOfEspecialPiffagor(number):
    '''If Sum of especiaal Pifagors numbers is equivalent to number than return a * b * c'''
    for i in range(1,400):
        for j in range(1,400):
            if i + j + math.sqrt(i**2 + j**2) == number:
                return i*j*math.sqrt(i**2 + j**2)

print(sumOfEspecialPiffagor(1000))