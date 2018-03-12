from sys import argv

wasted = raw_input("Enter coordinates:")
script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

print "Submarine sunk %s" % wasted
