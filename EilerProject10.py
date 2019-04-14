import EratostheneSieve
def sumOfCommonNumbers(number):
    ourList = list(EratostheneSieve.Sieve(number))
    return sum(ourList)
print(sumOfCommonNumbers(2000000))
#Summary - I should to add Eratosthene sieve