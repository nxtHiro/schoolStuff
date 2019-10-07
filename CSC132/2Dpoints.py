######################################################################################################################
# Name: Kaleb Crysel
# Date: March 10, 2018
# Description: Class to simulate points in an x,y plane
######################################################################################################################

# the 2D point class
class Point(object):
	# Each point must have an x and y component (x and y default to 0 if none are specified)
    def __init__(self, x = 0, y = 0):
        self.x = float(x)
        self.y = float(y)

    # x coord accessor--returns the x coord of the specified instance
    @property
    def x(self):
        return self._x

    # y point coord--returns the y coord of the specified instance
    @property
    def y(self):
        return self._y

    # x coord mutator--redefines the x coord for the specified instance to the given value
    @x.setter
    def x(self, x):
        self._x = x

    # y coord mutator--redefines the y coord for the specified instance to the given value
    @y.setter
    def y(self, y):
        self._y = y

    # calculate the distance between two points (pythagorean thm) and return the result
    def dist(self, end):
        return (((end.y - self.y)**2)+((end.x - self.x)**2))**(0.5)

    # calculate the midpoint (midpoint formula) and pass the resulting 'x' and 'y' through Point() class
    def midpt(self, end):
        return Point(((self.x + end.x)/2), ((self.y + end.y)/2))

    # format what is printed when an instance is referred to
    def __str__(self):
        return "({},{})".format(self.x, self.y)

##########################################################
# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# create some points
p1 = Point()
p2 = Point(3, 0)
p3 = Point(3, 4)
# display them
print "p1:", p1
print "p2:", p2
print "p3:", p3
# calculate and display some distances
print "distance from p1 to p2:", p1.dist(p2)
print "distance from p2 to p3:", p2.dist(p3)
print "distance from p1 to p3:", p1.dist(p3)
# calculate and display some midpoints
print "midpt of p1 and p2:", p1.midpt(p2)
print "midpt of p2 and p3:", p2.midpt(p3)
print "midpt of p1 and p3:", p1.midpt(p3)
# just a few more things...
p4 = p1.midpt(p3)
print "p4:", p4
print "distance from p4 to p1:", p4.dist(p1)
