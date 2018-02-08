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

    value = raw_input ("\nEnter the price as cents, a multiple of five cents\n"
                       "or 'done' (without quotes) if you are finished:\n")
    if value == "done":
        break