#
# doubleInt.py
#
# This script is based on several from 'Core Python Computing'
# It shows how to get input from the user using the built-in
# raw_input function, how to do a type conversion and how
# to modify the user's input, in this case by doubling a number.
#

#
# We make a variable called user and give it the string value
# of whatever the user types in from the keyboard.
#

user = raw_input('Please enter your name: ')

#
# Now we do the same for a number. Note that raw_input
# returns the string value of a number, which we cannot
# use for math purposes. We'll fix that later.
#

num = raw_input('Please enter an integer: ')

#
# Now we print out a friendly greeting and display the value
# of the number that the user entered doubled (note * 2).
# Because we cannot do math on strings (remember, raw_input
# returns strings), we have to convert num to a number
# format. We will use the int function for this. Notice
# in the print command we use %d. This is a format operator.
# it will place a string version of a number (in this case
# a double length number) at the location of the %.
#
print 'Dear  %s , you entered the number:  %s . Doubling it gives us  %d .' % (user, num, (int(num) * 2))

dummy = raw_input()