def stats(carry_yards, rec_yards, carries, catches):
    yards = carry_yards + rec_yards
    yards_per_carry = carry_yards / carries
    yards_per_rec = rec_yards / catches
    rec_points = rec_yards / 20.0
    run_points = carry_yards / 10.0
    print "Your player had %d total yards." % (yards)
    print "That's %.2r yards per carry and %r yards per reception." % (yards_per_carry, yards_per_rec)
    print "Your player got a total of %r points." % (rec_points + run_points)

stats(123, 49, 8, 4)

cyds = raw_input("Total yards on the ground: ")
ryds = raw_input("Total yards in the air: ")
runs = raw_input("Number of runs: ")
airs = raw_input("Number of catches: ")

# This doesn't work, I'ma gonna need to find out why something about int()
stats(int(cyds), int(ryds), int(runs), int(airs))
