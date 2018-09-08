#
# gradeCounter.py
#
# This little script gets ten grades from the user.
# It then averages them and prints out the class average.
# This script does NO error checking.
#
# Firt we create two variables, total and gradeCounter.
# total keeps the accumulated grade totals. gradeCounter
# acts as a loop counter. We give them their starting
# values.
#
total = 0
gradeCounter = 1
#
# We create a loop. The idea here is that we will get ten
# grades and average them. We use a loop to get the grades
# ten times. We can modify how many grades we want by
# changing the number in the next line from 10 to some other
# number. Notice the last line. We add 1 to gradeCounter
# every time we go through the loop. The loop stops when
# the value of gradeCounter reaches 11 (one greater than
# the last number of the next line)
#
while gradeCounter <= 10:
#
# We create a variable called grade to hold the value that
# the user types in. Notice that the body of the loop is
# indented. PYTHON requires that you do this.
#
	grade = raw_input("Enter a numerical grade (an integer): " )
#
# Next, we change the type of grade to an integer.
#
	grade = int(grade)
#
# We add grade to total and assign the value back to total.
#
	total  += grade
#
# We add 1 to gradeCounter. The loop goes back to the first line
# and does the comparison again. If the comparison is true (if
# the value of gradeCounter is less than or equal to 10), the
# loop runs again. If it is false (if the value of gradeCounter
# is greater tahn 10), we go to the next line of code.
#
	gradeCounter = gradeCounter + 1
	
average = total / 10
print "total = " + str(total)
print "Class average is",average

dummy = raw_input