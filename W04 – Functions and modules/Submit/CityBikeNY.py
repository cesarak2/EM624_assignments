# Author: Cesar Krischer

# This program will open the city_data.txt file that contains detailed
# information about the users of the service in NY.


# JUNE AND JANUARY

# CitiBike = open ("citi_bike.txt", 'r') # alternative for the function
def importFile(filepath):
    return open(filepath, 'r')


def storeFileInList(filetoberead):
    # starts a list that will contain all values (each row being a list withing the list)
    listFromFile = []
    # read the first line
    lineContentTXT = filetoberead.readline()
    # loop to read all the lines
    while lineContentTXT:
        # remove the spaces with strip and remove the breaks with split
        subList = lineContentTXT.strip().split()
        # add the values to the list
        listFromFile.append(subList)
        # read the new line
        lineContentTXT = filetoberead.readline()  # to exit the loop
    # close the file
    filetoberead.close()
    # return the final list as a result of the function
    return listFromFile


def printDetailsMonth(listCiti):
    pass
    # print "The following data is from"






# Importing the file .txt
CitiBike = importFile("citi_bike.txt")
# Transforming the filo into list
dataCitiBikeList = storeFileInList(CitiBike)


# # Count the number of lines
# count = 0
# for line in dataCitiBikeList:
#     count +=1
# print "number of lines of the file is: %d" % count



last = len(dataCitiBikeList)
last = int(last) - 1
# print dataCitiBikeList
print last
print "First: ", dataCitiBikeList[0][0], "\t\t\tlast: ", dataCitiBikeList[last][0]
# print "The file CitiBike.csv has %s lines, of which %s is/are from 1/15/2014" % (nLinesCSVFile, countLinesMatchDate)


# Print all 1 columns from all lists
# i = 0
# for line in dataCitiBikeList:
#     print dataCitiBikeList[i][0]
#     i += 1


i = 0
for line in dataCitiBikeList:
    if dataCitiBikeList[i][0].startswith("6/"):
        print dataCitiBikeList[i][3]
    i += 1




    i = 0
    j = 0
    monthSumMileageTraveled = 0
    for line in dataCitiBikeList:
        if dataCitiBikeList[i][0].startswith("6/"):
            monthSumMileageTraveled += dataCitiBikeList[i][3]
            j += 1
        i += 1
    averageMileageTraveled = monthSumMileageTraveled / j





    # juneTraveledMiles = []
    # line = dataCitiBikeList
    # if line.startswith("6/"):
    #     print line