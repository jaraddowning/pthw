# import module argv from the python system
from sys import argv

# using the argv method, tell it to expect two variables one from the cli
# and this script
script, filename = argv

# Open the file captured from the cli for processing
txt = open(filename)

# Display the contents of the filename and file
print "Here's your file %r:" % filename
print txt.read()

# close the file to remove it from memory
txt.close()

# the same as above but getting the filename from user imput during the running
# of the script
print "Type the filename again: "
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
txt_again.close()
