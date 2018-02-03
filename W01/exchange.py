# Author:  Cesar Krischer

# Exercise 1, homework, 01/30/18

#     This program converts a value of US dollars to
#     the currency the user decides. The program prompts the
#     user to set the amount and, name of the currency to be
#     converted and the exchange rate.

#     The program is written as a loop (using while True), so that the user
#     must enter the word 'done" (without quotes) to signal
#     that they want to end

while True:
    #  get the amount to be converted and allow the user to quit the program
    AmountUSDollars = raw_input("How many US Dollars do you want to exchange?  (done = ends)")
    if AmountUSDollars == 'done':
        print 'Thank You'
        break
    #   verify if the amount to be converted is a number
    else:
        if AmountUSDollars.isdigit() == False:
            print "please enter an integer"
            continue
        else:
            print "%s dolars" % AmountUSDollars


        # calculate and print sum
        # use int() built-in fuction to convert raw input to integer

        print "\nEXP The equivalent of %s degree Celsius is %s Fahrenheit\n" % (AmountUSDollars, AmountUSDollars)
        # print '\nThe equivalent of ', celsius, 'degree Celsius is ', fahrenheit
    else:
    print "not a number"

#print '\nThanks for using this tool!\n'
