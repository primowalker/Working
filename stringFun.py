#
# stringFun.py
#
# This script demonstrates different things that you can do
# with strings.
#

#
# First, we make some variables and give them string values.
# PYTHON thinks that any sequence of characters surrounded by
# single or double quotes is a string. You must match the beginning
# and the end quote. Both quotes must be either single or
# double quotes. If you have one of each, PYTHON will raise an
# error.
#

string1 = 'In this class,'
string2 = 'I am learning to program in'
string3 = 'PYTHON.'

print 'string1 is: ', string1
print 'string2 is: ', string2
print 'string3 is: ', string3
print 'Put them altogether and you get:'
print string1, string2, string3
print

print 'Notice that when you give the print command several strings '
print 'separated by commas, which we did above, PYTHON inserts a space'
print 'after the end of each string.'
print
print 'If you use the concetenation operator (+) to join strings,'
print 'PYTHON does NOT add spaces after each string, like so:'
print string1 + string2 + string3
print

#
# We can take strings apart, too.
#

print 'PYTHON allows you to slice up a string. You use the square'
print 'brackets to do so. The first character position is NOT 1'
print 'but 0.'

print 'string1[0] is: ',string1[0]
print

print 'We can get more than one character at a time. Supposed we'
print 'wanted the characters at positions 2 - 5 in string2. We'
print 'would do this:'
print 'string2[2:5] is : ', string2[2:5]
print 'Notice that string2[5] is a space.'
print
print 'You can make more than one copy of a string by \"multiplying\"'
print 'it with the * character. If you wanted to make two copies'
print 'of string3:'
print 'string3 * 2 is:', string3 * 2
dummy = raw_input