__author__ = 'Karthik'
import sys
count = {}
file = open("test1.txt",'r')
counter = 0
firstLineFlag = 0
for line in file:
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

    counter = counter + 1
    count[counter] = int(line)
goodcount = len(count)
for key, val in count.iteritems():
    if val == 1:
        goodcount = goodcount - 1

print goodcount