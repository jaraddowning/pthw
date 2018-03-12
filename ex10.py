tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
\v
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print u"\u00a9 '\N{COPYRIGHT SIGN}'"
print u"\u0024 \u06de \u0fca \u21a2 \u2318 \u234b \u2615"

while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,
