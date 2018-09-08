#
# time.py
# Bernard Sypniewski
#
# We import from two modules.
#
import time
from datetime import date, timedelta
#
# The first function, time.clock, prints out CPU time of the
# current process in seconds expressed as a floating point
# number. This can be used to test the efficiency of code.
# 
print "The current CPU time in seconds is: ", time.clock()
#
# The following functions are useful for working with dates. PYTHON
# allows us to add or subtract dates so that we can find out the span of
# time between them. This is not easy to code in most languages. In PYTHON,
# it's a snap. timedelta retuens a string with a particular type of formatting.
# Used by itself, we can express days as floating point numbers and
# PYTHON will figure out the fractional part in minutes and seconds. However,
# when we use a fractional part in addition or subtraction, we always get
# an answer in whole days.
#
# We subtract one date from another to find the length of time between those
# dates and assign the resulting value to the variable days. We print it out.
#
days = date(2005, 12, 17) - date(2004, 11, 29)
print "The value of the variable days is: ", days
#
 # Let's see what type days is.
 #
print "The type of the variable days is: ", type(days)
#
# This type won't concatenate with a string (I've tried) so we have to convert
# it to a string with the str() built-in function.
#
print "There are " + str(days) + " days between Nov. 29, 2004 and Dec. 17, 2005."
#
# For some reason the result from timedelta() doesn't give us the same problem.
#
print "The type of timedelta(18.8) is: ", type(timedelta(18.8))
print "18.8 days in days, minutes, seconds: ", timedelta(18.8)
#
# Notice that the result of adding a timedelta to a date returns a date which will concatenate
# with a string.
#
print "The type of date(2007, 9, 29) + timedelta(10.7) is: ", type(date(2007, 9, 29) + timedelta(10.7))
print "10.7 days after Sep. 29, 2007 is: ", date(2007, 9, 29) + timedelta(10.7)