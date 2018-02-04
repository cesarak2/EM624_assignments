# Author:  Cesar Krischer

# Exercise 1, in class, 01/30/18

#     This program prompts the user a value for the
#     temperature (in Celsius ) and converts is to
#     the temperature in Fahrenheit

# The program is written as a loop (using while True), so that the user
#     must enter the word 'done" (without quotes) to signal
#     that they want to end

# print "\n run by Cesar K."

while True:
    #  get number from user
    celsius = raw_input("What is the temperature in Celsius you want to convert?  (done = ends)")
    if celsius == 'done':
        print 'Thank You'
        break
    else:
        #  calculates T Fahrenheit from T Celsius
        fahrenheit=float (celsius)*1.8+32
        # calculate and print sum
        # use int() built-in fuction to convert raw input to integer

        print "\nThe equivalent of %s degree Celsius is %s Fahrenheit\n" % (celsius, fahrenheit)
        # print '\nThe equivalent of ', celsius, 'degree Celsius is ', fahrenheit


#print '\nThanks for using this tool!\n'
