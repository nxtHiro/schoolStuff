###########################################################################################
# Name: Marco Flores
# Date: 2017-10-26
# Description: 04 99 Bottles of Beer on the Wall using recursive logic
###########################################################################################

# the algorithm implemented iteratively
# def passSomeBeers(n):
#	while (n > 0):
#		print "{} bottles of beer on the wall.".format(n)
#		print "{} bottles of beer.".format(n)
#		print "Take one down, pass it around."
#		n = n - 1
#		print "{} bottles of beer on the wall.".format(n)
#		print

# the algorithm implemented recursively
def passSomeBeers(n):
	if(n > 0):
		if(n==1):
			print "{} bottle of beer on the wall.".format(n)
			print "{} bottle of beer.".format(n)
			print "Take one down, pass it around."
			n = n - 1
			print "{} bottles of beer on the wall.".format(n)
			passSomeBeers(n)
		elif(n==2):
			print "{} bottles of beer on the wall.".format(n)
			print "{} bottles of beer.".format(n)
			print "Take one down, pass it around."
			n = n - 1
			print "{} bottle of beer on the wall.".format(n)
			passSomeBeers(n)
		else:
			print "{} bottles of beer on the wall.".format(n)
			print "{} bottles of beer.".format(n)
			print "Take one down, pass it around."
			n = n - 1
			print "{} bottles of beer on the wall.".format(n)
			passSomeBeers(n)

###############################################
# MAIN PART OF THE PROGRAM
###############################################
# calls the passSomeBeers function
passSomeBeers(99)
