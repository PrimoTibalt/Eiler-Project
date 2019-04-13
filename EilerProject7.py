
from EilerProject3 import IsItCommon

def CommonNumberByNumber(number):
    searchNum = 1
    numOfCommon = 1
    while(numOfCommon < number):
        if IsItCommon(searchNum) :
            numOfCommon += 1
            if numOfCommon == number :
                return searchNum
        searchNum += 1


print(CommonNumberByNumber(1001))
