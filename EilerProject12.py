import math
def howMuchDividers():
    i=3
    listOfThreeAngle = [[1,1], [3,2]]
    while(True):
        nextNum = sum(range(i))
        print(nextNum)
        i+=1
        numOfDivider = 0
        for clone in range(1, len(listOfThreeAngle)):
            if nextNum % listOfThreeAngle[-clone][0] == 0:
                numOfDivider = nextNum / listOfThreeAngle[-clone][0] * listOfThreeAngle[-clone][1]
                listOfThreeAngle.append([nextNum, int(numOfDivider)])
        if (numOfDivider >= 500):
            return nextNum
        if numOfDivider > 0:
            continue
        for divider in range(3,math.ceil(nextNum/2)+1):
            if nextNum % divider == 0:
                numOfDivider+=1
                if(numOfDivider >= 500):
                    return nextNum
print(howMuchDividers())