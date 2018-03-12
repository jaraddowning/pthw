zas_name = 'Zed A. Shaw'
zas_age = 35.0 # not a lie
zas_height = 74.0 # inches
zas_weight = 180.0 # lbs
zas_eyes = 'Blue'
zas_teeth = 'White'
zas_hair = 'Brown'
height_m = zas_height / 0.39370
weight_kg = zas_weight / 2.2046

print "Let's talk about %s." % zas_name
print "He's %d inches tall (or %.2f cm)." % (zas_height, height_m)
print "He's %d pounds heavy (or %.2f kg)." % (zas_weight, weight_kg)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (zas_eyes, zas_hair)
print "His teeth are usually %s depending on the coffee.\n" % zas_teeth
#print "\n"
#print ""

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (zas_age, zas_height, zas_weight, zas_age + zas_height + zas_weight)
