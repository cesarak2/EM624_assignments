# Author: Cesar Krischer

# This program will open the city_data.txt file that contains detailed
# information about the users of the service in NY.


# JUNE AND JANUARY

# CitiBikeTXT = open ("citi_bike.txt", 'r') # alternative for the function
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


def averageAttribute(chosenmonth, attribute):
    i = 0
    nValuesinMonth = 0
    monthAttributeSum = 0
    for line in dataCitiBikeTXTList:
        if dataCitiBikeTXTList[i][0].startswith(chosenmonth):
            monthAttributeSum += float(dataCitiBikeTXTList[i][attribute])
            nValuesinMonth += 1
        i += 1
    print_detailsFunc = monthAttributeSum / nValuesinMonth
    print print_detailsFunc


def sumAttribute(chosenmonth, attribute):
    i = 0
    nValuesinMonth = 0
    monthAttributeSum = 0
    for line in dataCitiBikeTXTList:
        if dataCitiBikeTXTList[i][0].startswith(chosenmonth):
            monthAttributeSum += float(dataCitiBikeTXTList[i][attribute])
            nValuesinMonth += 1
        i += 1
    print monthAttributeSum


def startEndPeriod(chosenmonth):
    i = 0
    datesUsed = []
    for line in dataCitiBikeTXTList:
        if dataCitiBikeTXTList[i][0].startswith(chosenmonth):
            datesUsed.append(dataCitiBikeTXTList[i][0])
        i += 1
    finalDate = int(len(datesUsed)-1)
    if finalDate == -1:
        print "The requested month is not in the data"
        quit()
    else:
        print "The following data is from %s to %s" % (datesUsed[0], datesUsed[finalDate])




# Importing the file .txt
CitiBikeTXT = importFile("citi_bike.txt")
# Transforming the file into list
dataCitiBikeTXTList = storeFileInList(CitiBikeTXT)

# Importing the file .csv
CitiBikeCSV = importFile("citi_bike.csv")
# Transforming the file into list
dataCitiBikeCSVList = storeFileInList(CitiBikeCSV)




def print_details(chosenmonth, attribute1, attributename1, attribute2, attributename2):
    # print "\n"
    print startEndPeriod(chosenmonth)
    print "\nThe average for %s in that period (month %s) is:" % (attributename1, chosenmonth)
    averageAttribute(chosenmonth, attribute1)
    print "The sum for %s in that period is:" % attributename2
    sumAttribute(chosenmonth, attribute2)


print_details("6", 3, "Miles traveled", 7, "24-Hour Passes Purchased (5 pm - 5 pm)")
# print_details("2", 3, "Miles traveled", 7, "24-Hour Passes Purchased (5 pm - 5 pm)")



# startEndPeriod("6")
# averageAttribute("6", 3)
# sumAttribute("6", 3)



# print_details("6", 7)
# print_details("7", 7)

# print float(monthsYear["June"]) + 7

    # juneTraveledMiles = []
    # line = dataCitiBikeTXTList
    # if line.startswith("6/"):
    #     print line



# print "This is the end of the files processing."