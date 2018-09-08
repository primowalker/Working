#
# formatStrings.py
#
#
# This script shows different ways to format numerical types
# for printing.
#

print 'We create a variable called integerValue to hold, what else,an integer value.'
print 'We assign it the value 4237.'
print
integerValue = 4237
print "Integer", integerValue
print "Decimal integer %d" % integerValue
print "Hexadecimal integer %x\n" % integerValue
print
print 'We create a floating point variable and give it the value 123456.789'
print
floatValue = 123456.789
print "Float", floatValue
print "Default float %f" % floatValue
print "Default exponential %e\n" % floatValue
print
print "Right justify integer (%8d)" % integerValue
print "Left justify integer (%-8d)\n" % integerValue
print
print 'We create a string variable called stringValue'
print 'and assign it the value \"String formatting\".'
print
stringValue = "String formatting"
print "Force eight digits in integer (pad with zeroes) %.8d" % integerValue
print "Show five digits after decimal in float %.5f" % floatValue
print "Get the first fifteen and five characters in string:"
print "(%.15s) (%.5s)" % (stringValue, stringValue)

dummy=raw_input()