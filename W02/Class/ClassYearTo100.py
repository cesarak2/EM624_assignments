# Create a program that asks the user to enter their name and their age.
# Print out a message that tells the year they will turn 100 years old
# and the number of days from today till the first day of their 100th year.

# Author:  Cesar Krischer

#     W02 Exercise 2, in class, 02/06/18


import datetime

now = datetime.datetime.now()
now.year


while True:
    #
    nameUser = raw_input("Please enter your name (done = ends)\n")
    if nameUser == 'done':
        print '\nThank You'
        break
    #   verify if the amount to be converted is a number
    ageUser = raw_input("Please enter your age\n")

    try:
        ageUser = float(ageUser)
    except:
        # print "please type a number \n"
        continue
    userTurns100 = 100-ageUser+now.year

    print "%s, In %s you will turn 100 years old\n" % (nameUser, userTurns100)
    daysToEndCurrentYear = 365 - ((now.month - 1) * 30 + now.day)
    print(daysToEndCurrentYear)
