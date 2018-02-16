# marketingdata.txt
# Output: Skip a line, then print:
#     These are the first five lines in the file:
#     [5 lines of file]
#     [Skip a line]
#     The file has n1 lines



countLines = 0
with open("marketingdata.txt") as marketingData:
    lineContent = marketingData.readline()
    while lineContent:
        # lineContent = lineContent.strip()
        countLines += 1
        lineContent = marketingData.readline()
    print countLines
marketingData.close()

with open("marketingdata.txt") as marketingData:
    printLine = 0
    print "\nThese are the first five lines in the file: \n"
    lineContent = marketingData.readline()
    while lineContent:
        lineContent.strip()
        printLine += 1
        if printLine <= 5:
            print lineContent.strip()
        lineContent = marketingData.readline()

print countLines