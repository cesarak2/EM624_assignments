# Ask the user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the user.
# [Hint: how does an even / odd number react differently when divided by 2?].
# Print a different message if the input number is a multiple of 4






# Author:  Cesar Krischer

#     W02 Exercise 1, in class, 02/06/18





while True:
    #
    inputFromUser = raw_input("Please type a number  (done = ends)\n")
    if inputFromUser == 'done':
        print '\nThank You'
        break
    #   verify if the amount to be converted is a number

    try:
        # evenNumberFromUser = numberFromUser % 2 == 0
        numberFromUser = float(inputFromUser)
    except:
        # print "please type a number \n"
        continue

    if numberFromUser % 4 == 0:
        print "you typed a multiple of 4 \n"
    elif numberFromUser % 2 == 0:
        print "you typed an even number \n"
    else:
        print "you typed an odd number"
