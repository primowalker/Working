#
# import.py
#
# This little script, which is based on one from "Core Python Programming"
# demonstrates how to import modules into PYTHON. The
# syntax is 'import ' follwed by the name of the module.
# This script imports two modules, sys and string.
#
import sys
import string

#
# sys.platform tells you what type of system (WINDOWS, LINUX,MAC, etc.)
# that you are operating on (remember: a PYTHON script can run on different
# types of platforms). sys.version tells you what version of
# PYTHON you are using.
#

print sys.platform
print sys.version

#
# The following line creates a variable called up2space and
# gives it the value of that portion of the string returned
# by sys.version upto the first space.
#

up2space = string.find(sys.version, ' ')

#
# We create another variable called ver and give it the
# value of up2space.
#

ver = sys.version[:up2space]

print 'I am running PYTHON version %s on a %s platform.' % (ver, sys.platform)

dummy = raw_input()
