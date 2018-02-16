# marketingdata.txt
# Output: Skip a line, then print:
#     These are the first five lines in the file:
#     [5 lines of file]
#     [Skip a line]
#     The file has n1 lines



# countLines = 0
# with open("marketingdata.txt") as marketingData:
#     lineContent = marketingData.readline()
#     while lineContent:
#         # lineContent = lineContent.strip()
#         countLines += 1
#         lineContent = marketingData.readline()
#     print countLines
# marketingData.close()
#
# with open("marketingdata.txt") as marketingData:
#     printLine = 0
#     print "\nThese are the first five lines in the file: \n"
#     lineContent = marketingData.readline()
#     while lineContent:
#         lineContent.strip()
#         printLine += 1
#         if printLine <= 5:
#             print lineContent.strip()
#         lineContent = marketingData.readline()
#
# print countLines

# Part 1:
# processing a text file


# Set the counter of lines as 0
countLines = 0
print "\nThese are the first five lines in the file: \n"
# Importing the file as marketingData as read only.
with open("marketingdata.txt", 'r') as marketingData:
    # extracting the value of that line
    lineContent = marketingData.readline()
    # a loop between all lines to count the number of lines
    while lineContent:
        countLines += 1
        # Verifies if the loop is running in the first 5 lines. If yes, print the
        # content of that line without the break line using .strip()
        if countLines <= 5:
            print lineContent.strip()
        # read the next line. When there is no more lines, break the loop.
        lineContent = marketingData.readline()
    # print how many lines the file has.
    print "\nThe file has %s lines" % countLines

# Part 2:
# processing a csv file.
