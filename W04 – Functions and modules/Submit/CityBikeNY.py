# Author: Cesar Krischer

# This program will open the city_data.txt and citi_data.csv files
# that contains detailed information about the users of the Citi Bike
# service in NY.

# The functions made for this program are:
#     storeFileinList: checks if the file is .txt or .csv and store it
#             in a list of lists.
#     averageAttribute: for a chosen month and attribute, returns its average
#     sumAttribute: for a chosen month and attribute, returns its sum
#     startEndPeriod: check the first and last day of that month
#     print_details: it uses the other functions to return the information of interest.
#     biggestvaluesdays
# import os
# print os.getcwd()
# print "\n"

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
    # set the counters
    i = 0
    nValuesinMonth = 0
    monthAttributeSum = 0
    # for all lines, check if it the date starts with the chosen month
    # and add its value to the variable sum.
    for line in file:
        if file[i][0].startswith(chosenmonth):
            monthAttributeSum += float(file[i][attribute])
            nValuesinMonth += 1
        i += 1
    # set a variable with the results and print it
    print_detailsFunc = monthAttributeSum / nValuesinMonth
    print print_detailsFunc


def sumAttribute(chosenmonth, attribute, file):
    # set the counters
    i = 0
    nValuesinMonth = 0
    monthAttributeSum = 0
    # for all lines, check if it the date starts with the chosen month
    # and add its value to the variable sum.
    for line in file:
        if file[i][0].startswith(chosenmonth):
            monthAttributeSum += float(file[i][attribute])
            nValuesinMonth += 1
        i += 1
    print monthAttributeSum


def startEndPeriod(chosenmonth, file):
    # set the counter
    i = 0
    datesUsed = []
    # for all lines, check if it the date starts with the chosen month
    # and append it to the list with all dates. It assumes the date is ordered.
    for line in file:
        if file[i][0].startswith(chosenmonth):
            datesUsed.append(file[i][0])
        i += 1
    finalDate = int(len(datesUsed)-1)
    # if the kist with the dates is empty, close the program.
    if finalDate == -1:
        print "The requested month is not in the data"
        quit()
    # if the list with the dates has values, print the first and the last.
    else:
        return "\tThe following data is from %s to %s" % (datesUsed[0], datesUsed[finalDate])


def print_details(file, chosenmonth, attribute1, attributename1, attribute2, attributename2):
    print ""
    # print the range of dates
    print startEndPeriod(chosenmonth, file)
    # print the average for that attribute
    print "\nThe average for '%s' in that period (month %s) is:" % (attributename1, chosenmonth)
    averageAttribute(chosenmonth, attribute1, file)
    # print the sum for that attribute
    print "The sum for '%s' in that period is:" % attributename2
    sumAttribute(chosenmonth, attribute2, file)


def biggestvaluesdays(file, chosenmonth, ndays, attribute):
    # creates a new list equals to the original file to avoid aliasing
    orderedList = file[:]
    # orders the list
    orderedList = sorted(orderedList, reverse=True, key=lambda z: float(z[attribute])) # https://wiki.python.org/moin/HowTo/Sorting
    # set the counters (i for lines in the file, j for how many days to print
    i = 0
    j = 0
    while i <= len(orderedList)-1:
        # it will verify the condition while there are lines in the file AND the number
        # of days to print is not yet satisfied
        if orderedList[i][0].startswith(chosenmonth) and j < ndays:
            # prints the day and attribute in decreasing order
            print orderedList[i][0], orderedList[i][attribute]
            j += 1
        i += 1

# import os
# wd = os.getcwd()
# Importing the file .txt and .csv
CitiBikeTXT = open ("citi_bike.txt", 'r') # alternative for the function
CitiBikeCSV = open ("citi_bike.csv", 'r') # alternative for the function

# Transforming the files into lists
dataCitiBikeTXTList = storeFileInList(CitiBikeTXT, "TXT")
dataCitiBikeCSVList = storeFileInList(CitiBikeCSV, "CSV")


# For JUNE
# print the range of dates, average for miles traveled, the sum for 24-h purchased
# Arguments: (file, chosen month, attribute 1, name of attribute 1, attribute 2, name of attribute 2)
print_details(dataCitiBikeTXTList, "6", 3, "Miles traveled (5 pm to 5 pm)", 7, "24-Hour Passes Purchased (5 pm - 5 pm)")
# extract the 5 days with biggest occurrence for June.
# Arguments: (file, chosen month, number of days to print, attribute):
print "The days that had more 'Trips over the past 24-hours (5 pm to 5 pm)'"
biggestvaluesdays(dataCitiBikeTXTList, "6", 5, 1)

# For JANUARY
# print the range of dates, average for miles traveled, the sum for 24-h purchased
print_details(dataCitiBikeCSVList, "1", 3, "Miles traveled (5 pm to 5 pm)", 7, "24-Hour Passes Purchased (5 pm - 5 pm)")
# extract the 5 days with biggest occurrence for January.
print "The days that had more 'Trips over the past 24-hours (5 pm to 5 pm)'"
biggestvaluesdays(dataCitiBikeCSVList, "1", 5, 1)

# Finishing the program
print "\n\tThis is the end of the files processing."

# notes for improvement:
#     merge the functions sum and average
#     in the startEndPeriod function, order list of date before using it
#             to avoid a wrong result in case the date is not ordered
#     create a dictionary with all attributes names and use it to avoid
#             having to write it as an argument of the functions.