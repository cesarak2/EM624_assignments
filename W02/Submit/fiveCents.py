# Author: Cesar Krischer

# Exercise 2
# Five Cents

# The program is written as a loop (using while True), so that the user
# must enter the word 'done" (without quotes) to signal that they want to end

# Prompt the user for a price in cents, that is a multiple of five cents.
# If the user enters 'done' (without quotes), print goodbye and stop
# If the user enters a price, print the price and repeat the prompt (program is a loop)
# If the value is not a multiple of 5 cents, repeat the prompt.

while True:
    # ask for the price that should be multiple of 5 cents
    value = raw_input("\nEnter the price as cents, a multiple of five cents\n"
                      "or 'done' (without quotes) if you are finished:\n")
    # break the loop and exit the program if the user types "done"
    if value == "done":
        print "Good-bye!"
        break
    # verify if the user entry is a number and assign it to a new variable
    try:
        money = float(value)
    except:
        print "please type a valid number"
        continue
    # verify if the user entry is a multiple of 5 and print it, otherwise repeat the loop.
    if money % 5 == 0:
        print "You entered %s cents" % money
    else:
        continue