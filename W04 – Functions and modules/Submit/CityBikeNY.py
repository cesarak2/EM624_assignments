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
    print "The following data is from"
    print




# Importing the file .txt
CitiBike = importFile("citi_bike.txt")
# Transforming the filo into list
dataCitiBikeList = storeFileInList(CitiBike)



last = len(dataCitiBikeList)
last = int(last) - 1
# print dataCitiBikeList
print last
print dataCitiBikeList[last][0]
# print "The file CitiBike.csv has %s lines, of which %s is/are from 1/15/2014" % (nLinesCSVFile, countLinesMatchDate)




