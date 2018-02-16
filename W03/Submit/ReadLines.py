# Author:  Cesar Krischer

# Exercise 3
# Count Lines in a .txt and .csv files

# This program is divided in two parts:
# Part 1: counts the number of lines in a .txt file and prints
# the first 5 of them.
#   The program imports the file using the open function and with a while
#   statement reads all line using .readline(). An if statement verifies
#   if the line is one of the first 5 and print it accordingly.


# Part 2: counts the number of lines in a .csv file and also counts how
# many lines matches the criteria.
#   The program imports the file using the open function and with a while
#   statement reads all line using .readline(). An if statement verifies
#   if the line matches the criteria.



# Part 1:
# processing a text file


# Set the counter of lines as 0
nLinesTXTFile = 0

# Importing the file as marketingData as read only.
with open("marketingdata.txt", 'r') as marketingData:
    print "\nThese are the first five lines in the file marketingdata.txt: \n"
    # extracting the value of that line
    lineContent = marketingData.readline()
    # a loop between all lines to count the number of lines
    while lineContent:
        nLinesTXTFile += 1
        # Verifies if the loop is running in the first 5 lines. If yes, print the
        # content of that line without the break line using .strip()
        if nLinesTXTFile <= 5:
            print lineContent.strip()
        # read the next line. When there is no more lines, break the loop.
        lineContent = marketingData.readline()
    # print how many lines the file has.
    print "\nThe file marketingdata.txt has %s lines\n" % nLinesTXTFile
marketingData.close()


# Part 2:
# processing a csv file.

# Set the counter of lines as 0
nLinesCSVFile = 0
# Set the counter of lines matching the criteria as 0
countLinesMatchDate = 0
# Importing the file as CitiBike as read only.
with open ("CitiBike.csv", 'r') as CitiBike:
    # extracting the value of that line
    lineContentCSV = CitiBike.readline()
    # a loop ro real all lines to count the number of them
    while lineContentCSV:
        nLinesCSVFile += 1
        # If the the line matches the criteria, the counter increases one unit
        if "1/15/2014" in lineContentCSV:
            countLinesMatchDate += 1
            # print lineContentCSV.strip(), "\n" # add this line to show the lines that match the criteria
        # read the next line. When there is no more lines, break the loop.
        lineContentCSV = CitiBike.readline()
    # Print the final statement
    print "The file CitiBike.csv has %s lines, of which %s is/are from 1/15/2014" % (countLinesCSV, countLinesCSVDate)
CitiBike.close()