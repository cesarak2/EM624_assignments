# Author: Cesar Krischer

# This program will open the city_data.txt file that contains detailed
# information about the users of the service in NY.


# JUNE AND JANUARY

# CitiBikeTXT = open ("citi_bike.txt", 'r') # alternative for the function
def importFile(filepath):
    return open(filepath, 'r')


def storeFileInList(filetoberead, fileType):
    # starts a list that will contain all values (each row being a list withing the list)
    listFromFile = []
    # read the first line
    lineContentTXT = filetoberead.readline()
    # loop to read all the lines
    if fileType == "TXT":
        splitCharacter = " "
    else:
        splitCharacter = ","
    while lineContentTXT:
        # remove the spaces with strip and remove the breaks with split
        subList = lineContentTXT.strip().split(splitCharacter)
        # add the values to the list
        listFromFile.append(subList)
        # read the new line
        lineContentTXT = filetoberead.readline()  # to exit the loop
    # close the file
    filetoberead.close()
    # return the final list as a result of the function
    return listFromFile


def averageAttribute(chosenmonth, attribute, file):
    i = 0
    nValuesinMonth = 0
    monthAttributeSum = 0
    for line in file:
        if file[i][0].startswith(chosenmonth):
            monthAttributeSum += float(file[i][attribute])
            nValuesinMonth += 1
        i += 1
    print_detailsFunc = monthAttributeSum / nValuesinMonth
    print print_detailsFunc


def sumAttribute(chosenmonth, attribute, file):
    i = 0
    nValuesinMonth = 0
    monthAttributeSum = 0
    for line in file:
        if file[i][0].startswith(chosenmonth):
            monthAttributeSum += float(file[i][attribute])
            nValuesinMonth += 1
        i += 1
    print monthAttributeSum


def startEndPeriod(chosenmonth, file):
    i = 0
    datesUsed = []
    for line in file:
        if file[i][0].startswith(chosenmonth):
            datesUsed.append(file[i][0])
        i += 1
    finalDate = int(len(datesUsed)-1)
    if finalDate == -1:
        print "The requested month is not in the data"
        quit()
    else:
        return "\tThe following data is from %s to %s" % (datesUsed[0], datesUsed[finalDate])


def print_details(file, chosenmonth, attribute1, attributename1, attribute2, attributename2):
    print ""
    print startEndPeriod(chosenmonth, file)
    print "\nThe average for '%s' in that period (month %s) is:" % (attributename1, chosenmonth)
    averageAttribute(chosenmonth, attribute1, file)
    print "The sum for '%s' in that period is:" % attributename2
    sumAttribute(chosenmonth, attribute2, file)
    print ""

# def showthetopdays()



# Importing the file .txt
CitiBikeTXT = importFile("citi_bike.txt")
# Transforming the file into list
dataCitiBikeTXTList = storeFileInList(CitiBikeTXT, "TXT")

# Importing the file .csv
CitiBikeCSV = importFile("citi_bike.csv")
# Transforming the file into list
dataCitiBikeCSVList = storeFileInList(CitiBikeCSV, "CSV")

# def print_details(file, chosenmonth, attribute1, attributename1, attribute2, attributename2):
print_details(dataCitiBikeTXTList, "6", 3, "Miles traveled", 7, "24-Hour Passes Purchased (5 pm - 5 pm)")
print_details(dataCitiBikeCSVList, "1", 3, "Miles traveled", 7, "24-Hour Passes Purchased (5 pm - 5 pm)")


# listOrdered = dataCitiBikeTXTList[:]
# sorted(listOrdered, 2)
# for i in dataCitiBikeTXTList:
#     listOrdered.append()


# if file[i][0].startswith(chosenmonth):

def biggestvaluesdays(file, month, ndays, attribute):
    # creates a new list equals to the original file to avoid aliasing
    orderedList = file[:]
    orderedList = sorted(orderedList, reverse=True, key=lambda z: float(z[attribute]))
    i = 0
    j = 0
    while i <= len(orderedList)-1:
        if orderedList[i][0].startswith(month) and j < ndays:
            print orderedList[i][0], orderedList[i][attribute]
            j += 1
        i += 1
    print i, j


# def biggestvaluesdays(file, month, attribute):
#     dictAttribute = {}
#     i = 0
#     while i <= len(file)-1:
#         if file[i][0].startswith(month):
#             # print file[i][0], file[i][attribute]
#             dictAttribute[file[i][0]] = float(file[i][attribute])
#         i += 1
#     # print dictAttribute
#     if not dictAttribute == {}:
#         for key, value in sorted(dictAttribute.iteritems(), reverse=True, key=lambda (k, v): (v, k)): #https://www.saltycrane.com/blog/2007/09/how-to-sort-python-dictionary-by-keys/
#             print "%s: %s" % (key, value)
#     else:
#         print "No values found for this month"

biggestvaluesdays(dataCitiBikeTXTList, "6", 5, 3)
# biggestvaluesdays(dataCitiBikeTXTList, "6", 1)

# a = sorted(dataCitiBikeTXTList, reverse=True, key=lambda attribute: attribute[0])
# print "\nmanual values"
# print max.a[0]
# print a[0][0], a[0][1]
# print a[1][0], a[1][1]
# print a[2][0], a[2][1]
# print a[3][0], a[3][1]
# print a[4][0], a[4][1]
# print a


# a = 10
# for i in range(a):
#     print i


# Finishing the program
print "\tThis is the end of the files processing."