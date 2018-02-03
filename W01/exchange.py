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
    amountUSDollars = raw_input("How many US Dollars do you want to exchange?  (done = ends)\n")
    if amountUSDollars == 'done':
        print 'Thank You'
        break
    #   verify if the amount to be converted is a number
    else:
        if amountUSDollars.isdigit() == True:
            print '%s dollars' % amountUSDollars
        else:
            print "\n please enter an integer\n"
            continue
            # prompt the user with the name of the currency to be converted from US Dollars
        currencyToBeConverted = raw_input("Please enter the name of the currency you want to convert US Dolars to \n"
                                          "(to be equivalent to 1 US dollar) \n")
            # prompt the user with the exchange rate
        exchangeRate = raw_input("What is is the exchange rate?\n")
            # verify if the exchange rate is a number. If not, go back to the beginning
        if exchangeRate.isdigit() == True:
            print "1 Dollar equals %s x %s" % (exchangeRate, currencyToBeConverted)  # delete this line when code is finished
        else:
            print "\n please enter an integer\n"
            continue
        newCurrencyAmount = float(exchangeRate) * float(amountUSDollars)
        print "You can exchange %r U.S. dollars for %r %r" % (amountUSDollars, newCurrencyAmount, currencyToBeConverted)