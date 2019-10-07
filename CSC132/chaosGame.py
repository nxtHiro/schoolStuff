######################################################################################################################
# Name: Marco Flores
# Date: 26-03-2018
# Description: 2D Points...Plotted
####################################################################################################################
from Tkinter import *
from random import randint

# the 2D point class
class Point(object):
# constuctor of the point class
def __init__(self, x = 0, y = 0):
  self.x = float(x)
  self.y = float(y)

# getter for the x coordinate
@property
def x(self):
    return self._x

# setter for the x coordinate
@x.setter
def x(self, x):
  self._x = x

# getter for the y coordinate
@property
def y(self):
    return self._y

# setter for the y coordinate
@y.setter
def y(self, y):
    self._y = y

# calculates the distance between two points and returns the value
def dist(self, point2):
    return (((point2.y - self.y)**2)+((point2.x - self.x)**2))**(0.5)

# calculates the midpoint and returns the value as an instance of the Point class
def midpt(self, end):
    return Point(((self.x + end.x)/2), ((self.y + end.y)/2))

# overloads the string function for the point class to represent a point in the format (x, y)
def __str__(self):
    return "({},{})".format(self.x, self.y)

# the coordinate system class: (0,0) is in the top-left corner
# inherits from the Canvas class of Tkinter
class CoordinateSystem(Canvas):
# constructs an instance of the CoordinateSystem class using the Canvas constructor
def __init__(self, parent):
    Canvas.__init__(self, parent, bg = "white")
    self.setupGUI()
# sets the canvas to fill the screen
def setupGUI(self):
  self.pack(fill=BOTH, expand = 1)
# plots the number of points requested
def plotPoints(self, pointNumbers):
  # list containing the color possibilities
  colors = ["black", "red", "green", "blue", "cyan", "yellow", "magenta"]
  # generates and plots the points
  for i in range(pointNumbers):
    p = Point(randint(0,WIDTH), randint(0,HEIGHT))
    self.create_oval(p.x, p.y, p.x, p.y, outline = colors[randint(0, len(colors)-1)])

##########################################################
# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# the default size of the canvas is 800x800
WIDTH = 800
HEIGHT = 800
# the number of points to plot
NUM_POINTS = 5000

# create the window
window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("2D Points...Plotted")
# create the coordinate system as a Tkinter canvas inside the window
s = CoordinateSystem(window)
# plot some random points
s.plotPoints(NUM_POINTS)
# wait for the window to close
window.mainloop()
