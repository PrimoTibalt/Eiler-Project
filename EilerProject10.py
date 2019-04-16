import EratostheneSieve
def sumOfCommonNumbers(number):
    '''Sum of number of prime numbers'''
    ourList = list(EratostheneSieve.Sieve(number))
    return sum(ourList)
print(sumOfCommonNumbers(2000000))
