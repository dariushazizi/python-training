import die_module as dm
#normal die:
die = dm.Die()
die.roll_die(2)

#more sided dies:
die10 = dm.Die(10)
die10.roll_die(10)
die20 = dm.Die(20)
die20.roll_die(10)