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
        print '\nThank You'
        break
    #   verify if the amount to be converted is a number
    else:
        if amountUSDollars.isdigit() == False:
            print "\n please enter an integer\n"
            continue
            # prompt the user with the name of the currency to be converted from US Dollars
        currencyToBeConverted = raw_input("\nPlease enter the name of the currency you are converting US Dolars to \n")
            # prompt the user with the exchange rate
        exchangeRate = raw_input("\nWhat is is the exchange rate?\n")
            # verify if the exchange rate is a number. If not, go back to the beginning
        if exchangeRate.isdigit() == False:
            print "\n please enter an integer\n"
            continue
            # set the result in a new variable called newCurrencyAmount and calculate its
            # value by forcing the exchangeRate and amountUSDollars to be float numbers and
            # then multiplying them.
        newCurrencyAmount = float(exchangeRate) * float(amountUSDollars)
        # print the result
        print "\nYou can exchange %r U.S. dollars for %r %r\n" % (amountUSDollars, newCurrencyAmount, currencyToBeConverted)