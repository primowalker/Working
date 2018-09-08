
print "Simple for loop using a range variable"
print
for x in range(10):
    print "Burp!"
    
print
print "Counting by 5s"
for x in range(0,10,5):
    print str(x) + " Errruppppp!"
    
print
print "The White Knight (from Alice in Wonderland) counts backwards:"
for x in range (10, 0, -1):
    print str(x) + " Feed your head"
    
print
print "Breaking up is hard to do. Well, actually, it's pretty easy when you're a string."
word = raw_input("Enter a word: ")
for letter in word:
    print letter