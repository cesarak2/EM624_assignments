# Author: Cesar Krischer

# This program will open the city_data.txt file that contains detailed
# information about the users of the service in NY.


# JUNE AND JANUARY

# CitiBike = open ("citi_bike.txt", 'r') alternative for the function
def importFile(filepath):
    return open(filepath, 'r')


def printDetailsMonth (listCiti):
    print "The following data is from"
    print


CitiBike = importFile("citi_bike.txt")

print CitiBike.read()



print CitiBike.read()

dataCitiBike = []

lineContentTXT = CitiBike.readline()

# def storeFileInList (file)
while lineContentTXT:
    subList = lineContentTXT.strip().split()
    dataCitiBike.append(subList)
    lineContentTXT = CitiBike.readline() # to exit the loop
CitiBike.close()



last = len(dataCitiBike)
last = int(last)-1
print dataCitiBike[last][0]
print last
# print "The file CitiBike.csv has %s lines, of which %s is/are from 1/15/2014" % (nLinesCSVFile, countLinesMatchDate)

