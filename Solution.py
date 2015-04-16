__author__ = 'Karthik'
import sys

firstLineFlag = 0
numberCheck = 0

numList = []

def calculateProfit(numList):

    temp = 0
    greaterValueIndex = 0
    for index, num in enumerate(numList):
        #print index, num
        if num > temp:
            temp = num
            greaterValueIndex = index

    if greaterValueIndex == 0:
        return 0

    #if the value of index is equal to the length - 1 of the list, then sell share on last day
    count = 0
    total = 0
    if greaterValueIndex == len(numList) - 1:
        for num in numList:
            if count == len(numList):
                break
            if 1 <= int(num) <= 100000:
                total = total + num
                count = count + 1

        total = numList[(len(numList)-1)]*(count) - total
        return total

    temp = 0
    total = 0
    sellFlag = 0
    firstNumberCheck = 0
    grandTotal = 0
    for num in numList:
        if num > temp and firstNumberCheck == 0 and 1 <= int(num) <= 100000:
            temp = num
            total = total + num
            firstNumberCheck = -1

        elif num > temp and firstNumberCheck == -1 and 1 <= int(num) <= 100000:
            #Sell shares
            total = num - temp
            grandTotal = grandTotal + total
            temp = 0
            firstNumberCheck = 0
        else:
            total = total + num

    return grandTotal


for line in sys.stdin:
    line = line.replace("\n","")
    #print line
    #Check the constraint for test cases
    if firstLineFlag == 0:
        if 1 <= int(line) <= 10:
            firstLineFlag = -1
            continue
        else:
            print "Test cases constraint is violated... Program exiting"
            sys.exit()

    if numberCheck == 0:
        if 1 <= int(line) <= 50000:
            numberCheck = -1
            continue

    #print "Number of changes in next few minutes", line
    numList = [int(i) for i in line.split(' ')]
    numberCheck = 0
    total = calculateProfit(numList)
    print total

