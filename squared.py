#
# squared.py
# Bernard Sypniewski
#
# First, we make a funtion to square an number that is entered from the keyboard.
# The syntax is def followed by the name of the function (our choice) followed
# by whatever parameters we need in parentheses followed by a colon.
#
def squared(num):
#
# Notice the indentation of the following two lines of code. PYTHON is unusual
# in that it REQUIRES the use of indentation to indicate blocks of code. 
#
    sq = num * num
#
# The keyword return passes the value of sq back to the calling code, in this case,
# te last line of code. The line containing a return should be the last line in the
# function.
#
    return sq
#
# I have written the code you would use to run this function in comments.
# You can do this in order to test out the function to see whether it works
# correctly. When you are satisfied, you delete the commented lines.
#
# Notice that the next line changes indentation back to the original.
#
#num2sq = raw_input("Enter an integer to square: ")
#
# When num2sq gets its value from the raw_input call, it gets a string value.
# We know that we cannot do math on a string, we convert num2sq to an
# integer with the int() function.
#
#print num2sq, " squared is ", squared(int(num2sq))