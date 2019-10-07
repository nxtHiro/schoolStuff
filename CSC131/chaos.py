###################################################################
# The Chaos Game
# Implements the chaos game as described in class.
# Author: Dr. Jean Gourd
# Last updated: 2017-01-12
#
# Copyright (c) 2007-2018, Jean Gourd
# www.jeangourd.com
#
# Please feel free to use this code.  In fact, play around with it!
# I only ask that you leave my copyright notice within your source.
# Hey, it's not such a huge thing to ask, right?
###################################################################
# Any Python contained herein is free software; you can
# redistribute it and/or modify it under the terms of the GNU
# General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# This is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# To obtain a copy of the GNU General Public License, write to the
# Free Software Foundation, Inc., 51 Franklin St, Fifth Floor,
# Boston, MA 02110-1301 USA
###################################################################

import os
from datetime import datetime
from Tkinter import *
from random import randint
from math import pi, cos, sin

# the current version of The Chaos Game
TITLE = "The Chaos Game"
VERSION = 0.9
LAST_UPDATED = datetime.fromtimestamp(os.path.getmtime(__file__))
AUTHOR = "Dr. Jean Gourd"
WINDOW_TITLE = "{} v{} ({}) -- {}".format(TITLE, VERSION, LAST_UPDATED, AUTHOR)

# define some constants dealing with the window (GUI) size
window = Tk()
USE_EXTENDED_MONITOR = False	# set this to True if you have an extended (second) monitor
SCREEN_WIDTH = window.winfo_screenwidth()
SCREEN_HEIGHT = window.winfo_screenheight()
WIDTH_EXTRA = 8;
HEIGHT_EXTRA = 27;
CONTROLS = 25 + 22 + 25 + 22 + 25 + 22;
WIDTH = int(0.75 * SCREEN_WIDTH) - WIDTH_EXTRA;
HEIGHT = int(0.75 * SCREEN_HEIGHT) + CONTROLS - HEIGHT_EXTRA;
if (USE_EXTENDED_MONITOR):
	WIDTH /= 2
MINX = 10;
MAXX = WIDTH - 10;
MINY = 10;
MAXY = HEIGHT - 10 - (25 + 22 + 25 + 22 + 25);
MIDX = (MINX + MAXX) / 2;
MIDY = (MINY + MAXY) / 2;

# define some constants
POINT_COLORS = [ "black", "green", "blue", "purple", "orange", "yellow", "indigo", "violet" ]

# returns an x value that is some fraction d of the distance between MINX and MAXX
# e.g., MINX = 0, MAXX = 100, d = 0.75 --> 75
def FRACX(d):
	return int((MAXX - MINX) * d) + MINX

# returns a y value that is some fraction d of the distance between MINY and MAXY
# e.g., MINY = 50, MAXY = 550, d = 0.5 --> 300
def FRACY(d):
	return int((MAXY - MINY) * d) + MINY

# defines the specifics for a fractal
class Fractal():
	def __init__(self, name, n, r, theta, vertices):
		self.name = name		# its name
		self.n = n			# the number of points to plot (for best results)
		self.r = r			# the distance to each randonly chosen vertex to plot a new point
		self.theta = theta		# the angle to rotate around each randomly chosen vertex
		self.vertices = vertices	# the vertices

	def __str__(self):
		return self.name

# the chaos game!
class ChaosGame(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent, bg="white")

		# initialize some constants and variables
		self.DEFAULT_N = 10000					# the default number of points to plot
		self.PREDEFINED_FRACTALS = []				# the predefined fractals
		self.DEFAULT_FRACTAL = 1				# the default fractal is the first predefined one
		self.current_fractal_index = self.DEFAULT_FRACTAL	# the current fractal index
		self.current_fractal = None				# the current fractal
		self.user_defined_mode = False				# user defined mode
		self.user_defined_vertices = []				# user defined vertices

	# play the chaos game
	def play(self):
		self.setupFractals()
		self.setupGUI()

	# sets up the fractals and their specifics
	def setupFractals(self):
		# format is name, n, [ r for each vertex ], [ theta for each vertex ], [ (vertex points, each in a tuple) ]
		self.PREDEFINED_FRACTALS.append(Fractal("0: User defined", None, None, None, None))
		self.PREDEFINED_FRACTALS.append(Fractal("1: Sierpinski Triangle (n=3 r=0.5 theta=0)", 50000, [ 0.5, 0.5, 0.5 ], [ 0, 0, 0 ], [ (MIDX, MINY), (MINX, MAXY), (MAXX, MAXY) ]))
		self.PREDEFINED_FRACTALS.append(Fractal("2: Sierpinski Triangle (n=3 r=0.5 theta=180,0,0)", 50000, [ 0.5, 0.5, 0.5 ], [ 180, 0, 0 ], [ (MIDX, FRACY(0.33375)), (FRACX(0.11125), MAXY), (FRACX(0.88875), MAXY) ]))
		self.PREDEFINED_FRACTALS.append(Fractal("3: Sierpinski Triangle (n=3 r=0.5 theta=-90,0,0)", 35000, [ 0.5, 0.5, 0.5 ], [ -90, 0, 0 ], [ (MIDX, FRACY(0.25125)), (FRACX(0.11125), FRACY(0.9175)), (FRACX(0.88875), FRACY(0.9175)) ]))
		self.PREDEFINED_FRACTALS.append(Fractal("4: Sierpinski Tree (n=3 r=0.5 theta=0,20,-20)", 50000, [ 0.5, 0.5, 0.5 ], [ 0, 20, -20 ], [ (MIDX, MINY), (MINX, FRACY(0.7)), (MAXX, FRACY(0.7)) ]))
		self.PREDEFINED_FRACTALS.append(Fractal("5: Snowflake (n=3 r=0.5 theta=180)", 50000, [ 0.5, 0.5, 0.5 ], [ 180, 180, 180 ], [ (MIDX, FRACY(0.35625)), (FRACX(0.33375), FRACY(0.64375)), (FRACX(0.66625), FRACY(0.64375)) ]))
		self.PREDEFINED_FRACTALS.append(Fractal("6: Koch (n=4 r=0.66 theta=0,-60,60,0)", 10000, [ 0.66, 0.66, 0.66, 0.66 ], [ 0, -60, 60, 0 ], [ (MINX, MIDY), (FRACX(0.36), FRACY(0.3)), (FRACX(0.64125), FRACY(0.3)), (MAXX, MIDY) ]))
		self.PREDEFINED_FRACTALS.append(Fractal("7: Square (n=4 r=0.25 theta=0)", 50000, [ 0.25, 0.25, 0.25, 0.25 ], [ 0, 0, 0, 0 ], [ (MIDX, MINY), (MINX, MIDY), (MAXX, MIDY), (MIDX, MAXY) ]))
		self.PREDEFINED_FRACTALS.append(Fractal("8: Square (n=4 r=0.5 theta=0)", 35000, [ 0.5, 0.5, 0.5, 0.5 ], [ 0, 0, 0, 0 ], [ (MIDX, MINY), (MINX, MIDY), (MAXX, MIDY), (MIDX, MAXY) ]))
		self.PREDEFINED_FRACTALS.append(Fractal("9: Square (n=4 r=0.75 theta=0)", 10000, [ 0.75, 0.75, 0.75, 0.75 ], [ 0, 0, 0, 0 ], [ (MIDX, MINY), (MINX, MIDY), (MAXX, MIDY), (MIDX, MAXY) ]))
		self.PREDEFINED_FRACTALS.append(Fractal("A: Pentagon (n=5 r=0.618 theta=0)", 50000, [ 0.618, 0.618, 0.618, 0.618, 0.618 ], [ 0, 0, 0, 0, 0 ], [ (MIDX + MIDX * cos(2 * i * pi / 5 + 60), FRACY(0.5375) + MIDY * sin(2 * i * pi / 5 + 60)) for i in range(1, 6) ]))
		self.PREDEFINED_FRACTALS.append(Fractal("B: Hexagon (n=6 r=0.665 theta=0)", 50000, [ 0.665, 0.665, 0.665, 0.665, 0.665, 0.665 ], [ 0, 0, 0, 0, 0, 0 ], [ (MIDX, MINY), (MINX, FRACY(0.25)), (MAXX, FRACY(0.25)), (MINX, FRACY(0.75)), (MAXX, FRACY(0.75)), (MIDX, MAXY) ]))
		self.PREDEFINED_FRACTALS.append(Fractal("C: Octagon (n=8 r=0.705 theta=0)", 75000, [ 0.705, 0.705, 0.705, 0.705, 0.705, 0.705, 0.705, 0.705 ], [ 0, 0, 0, 0, 0, 0, 0, 0 ], [ (FRACX(0.2925), MINY), (FRACX(0.7075), MINY), (MINX, FRACY(0.2925)), (MAXX, FRACY(0.2925)), (MINX, FRACY(0.7075)), (MAXX, FRACY(0.7075)), (FRACX(0.2925), MAXY), (FRACX(0.7075), MAXY) ]))
		self.PREDEFINED_FRACTALS.append(Fractal("D: Sierpinski Carpet (n=8 r=0.66 theta=0)", 100000, [ 0.66, 0.66, 0.66, 0.66, 0.66, 0.66, 0.66, 0.66 ], [ 0, 0, 0, 0, 0, 0, 0, 0 ], [ (FRACX(0.1), FRACY(0.1)), (MIDX, FRACY(0.1)), (FRACX(0.9), FRACY(0.1)), (FRACX(0.1), MIDY), (FRACX(0.9), MIDY), (FRACX(0.1), FRACY(0.9)), (MIDX, FRACY(0.9)), (FRACX(0.9), FRACY(0.9)) ]))
		# the starfish needs a bit more setup
		rs = [ 0.038461538 for _ in range(11) ]
		rs.insert(0, 0.8)
		ts = [ -38 for _ in range(11) ]
		ts.insert(0, 0)
		vs = [ (MIDX, MIDY) for _ in range(11) ]
		vs.insert(0, (FRACX(0.1), FRACY(0.2)))
		self.PREDEFINED_FRACTALS.append(Fractal("Starfish (n=11 r=0.8,0.038,... theta=0,-38,...)", 75000, rs, ts, vs))
		self.PREDEFINED_FRACTALS.append(Fractal("Sierpinski Tetrahedron (n=4 r=0.5 theta=0)", 35000, [ 0.5, 0.5, 0.5, 0.5 ], [ 0, 0, 0, 0 ], [ (FRACX(0.565820312), FRACY(0.020833333)), (FRACX(0.196679687), FRACY(0.639583333)), (FRACX(0.790820312), FRACY(0.963020833)), (FRACX(0.744726562), FRACY(0.348958333)) ]))

		# set the current fractal
		self.current_fractal = self.PREDEFINED_FRACTALS[self.DEFAULT_FRACTAL]

	# sets up the GUI
	def setupGUI(self):
		# first, the canvas used to plot the points
		self.c = Canvas(self, bg="white", height=HEIGHT - 100, width=WIDTH)
		self.c.bind("<Button-1>", self.click)
		self.c.grid(row=0, columnspan=7, sticky=E+W+N+S)
	
		# set the labels
		# n
		self.l1 = Label(self, text="n: 10000", bg="white")
		self.l1.grid(row=1, column=0, sticky=W)
		# rs
		self.l2 = Label(self, text="r: 0.5,0.33,...", bg="white")
		self.l2.grid(row=1, column=1, sticky=W)
		# thetas
		self.l3 = Label(self, text="theta: 0,90,...", bg="white")
		self.l3.grid(row=1, column=2, sticky=W)
		# point color
		self.l4 = Label(self, text="Point color:", bg="white")
		self.l4.grid(row=1, column=3, sticky=W)
		# point size
		self.l5 = Label(self, text="Point size:", bg="white")
		self.l5.grid(row=1, column=4, sticky=W)
		# vertex size
		self.l6 = Label(self, text="Vertex size:", bg="white")
		self.l6.grid(row=1, column=5, columnspan=2, sticky=W)
		# fractal label
		self.l7 = Label(self, text="Predefined fractals:", bg="white")
		self.l7.grid(row=3, columnspan=6, sticky=W)

		# the text boxes (entries)
		# n
		self.n = Entry(self)
		self.n.grid(row=2, column=0, sticky=W)
		# rs
		self.r = Entry(self)
		self.r.grid(row=2, column=1, sticky=W)
		# thetas
		self.theta = Entry(self)
		self.theta.grid(row=2, column=2, sticky=W)
		# point color list
		self.om1_sel = StringVar(self)
		self.om1_sel.set(POINT_COLORS[0])	# default to the first color (black)
		self.om1 = OptionMenu(self, self.om1_sel, *POINT_COLORS)
		self.om1.grid(row=2, column=3, sticky=W)
		# point size
		self.psize = Entry(self)
		self.psize.insert(0, "1")
		self.psize.grid(row=2, column=4, sticky=W)
		# vertex size
		self.vsize = Entry(self)
		self.vsize.insert(0, "5")
		self.vsize.grid(row=2, column=5, columnspan=2,sticky=W)
		# fractal list
		self.om2 = None
		self.om2_sel = StringVar(self)
		self.om2_sel.trace("w", self.updateFractal)				# callback when the fractal is changed
		self.om2_sel.set(self.PREDEFINED_FRACTALS[self.DEFAULT_FRACTAL])	# default to the first fractal (Sierpinski triangle)
		self.om2 = OptionMenu(self, self.om2_sel, *self.PREDEFINED_FRACTALS)
		self.om2.grid(row=4, columnspan=4, sticky=W)
		# draw individual points checkbox
		self.point_draw_type = IntVar()
		self.cb = Checkbutton(self, text="Draw points separately", bg="white", variable=self.point_draw_type)
		self.cb.grid(row=4, column=4, sticky=W)
		# go button
		self.b1 = Button(self, text="GO", command=self.go)
		self.b1.grid(row=4, column=5, sticky=W)
		# clear button
		self.b2 = Button(self, text="Clear", command=self.clear)
		self.b2.grid(row=4, column=6, sticky=W)

		self.pack(fill=BOTH, expand=1)

	# callback when the user selects a different predefined fractal
	def updateFractal(self, *args):
		# clear the canvas
		self.clear()

		# set the current fractal index and fractal
		if (self.om2 != None):
			self.current_fractal_index = self.om2["menu"].index(self.om2_sel.get())
		else:
			self.current_fractal_index = self.DEFAULT_FRACTAL
		self.current_fractal = self.PREDEFINED_FRACTALS[self.current_fractal_index]

		# set the user defined mode
		self.user_defined_mode = True if (self.current_fractal_index == 0) else False

		# update the n textbox
		self.n.delete(0, "end")
		self.n.insert(0, self.DEFAULT_N if (self.user_defined_mode) else self.current_fractal.n)

		# format the rs (comma separated)
		self.r.delete(0, "end")
		if (not self.user_defined_mode):
			self.r.insert(0, ",".join(str(r) for r in self.current_fractal.r))

		# format the thetas (comma separated)
		self.theta.delete(0, "end")
		if (not self.user_defined_mode):
			self.theta.insert(0, ",".join(str(r) for r in self.current_fractal.theta))

		# plot the vertices in red
		if (not self.user_defined_mode):
			for p in self.current_fractal.vertices:
				self.plot(p[0], p[1], int(self.vsize.get()), "red")
			# and display them on the canvas right away
			self.c.update()

	# clears the canvas (also a callback for the clear button)
	def clear(self):
		self.c.delete("all")
		if (self.user_defined_mode):
			self.user_defined_vertices = []
#			self.current_fractal.vertices = None

	# starts the chaos game (a callback to the go button)
	def go(self):
		vertices = self.current_fractal.vertices if (not self.user_defined_mode) else self.user_defined_vertices
		if (len(vertices) < 2):
			return

		# no vertices in user defined mode?  get outta here!
		if (self.user_defined_mode and len(vertices) == 0):
			return

		# clear the canvas
		self.c.delete("all")

		# plot the vertices in red
		for p in (vertices):
			self.plot(p[0], p[1], int(self.vsize.get()), "red")
		# and display them on the canvas right away
		self.c.update()

		# fix r if necessary
		# first, handle the case that it is empty
		if (len(self.r.get()) == 0):
			self.r.insert(0, ",".join("0.5" for i in range(len(vertices))))
		# second, handle the case that it has a trailing comma
		while (self.r.get()[-1] == ","):
			self.r.delete(len(self.r.get()) - 1, "end")
		# third, handle the case that it has fewer elements than there are vertices
		while (len(self.r.get().split(",")) < len(vertices)):
			self.r.insert("end", ",0.5")
		# fourth, handle the case that it has more elements than there are vertices
		while (len(self.r.get().split(",")) > len(vertices)):
			self.r.delete(self.r.get().rfind(","), "end")

		# fix theta if necessary
		# first, handle the case that it is empty
		if (len(self.theta.get()) == 0):
			self.theta.insert(0, ",".join("0" for i in range(len(vertices))))
		# second, handle the case that it has a trailing comma
		while (self.theta.get()[-1] == ","):
			self.theta.delete(len(self.theta.get()) - 1, "end")
		# third, handle the case that it has fewer elements than there are vertices
		while (len(self.theta.get().split(",")) < len(vertices)):
			self.theta.insert("end", ",0")
		# fourth, handle the case that it has more elements than there are vertices
		while (len(self.theta.get().split(",")) > len(vertices)):
			self.theta.delete(self.theta.get().rfind(","), "end")

		# generate the points (i.e., play the game!)
		for i in range(int(self.n.get())):
			# pick a random vertex
			vi = randint(0, len(vertices) - 1)
			# the first time, there is no midpoint (just pick another vertex)
			if (i == 0):
				p = vertices[randint(0, len(vertices) - 1)]
				# make sure that both points aren't the same vertex
				while (p == vertices[vi]):
					p = vertices[randint(0, len(vertices) - 1)]

			# calculate the intermediate (new) point
			m = self.interPoint(p, vi)
			# plot it
			if (m == None):
				break
			self.plot(m[0], m[1], int(self.psize.get()), self.om1_sel.get())
			# refresh the canvas to show the new point right away if specified
			if (self.point_draw_type.get()):
				self.update()

			# the new point becomes the point of reference for the next iteration
			p = m

	# calculates the intermediate (usually the midpoint) point of two points
	def interPoint(self, p, vi):
		vertices = self.current_fractal.vertices if (not self.user_defined_mode) else self.user_defined_vertices

		# get the point and vertex components (x, y)
		px, py = int(p[0]), int(p[1])
		vx, vy = int(vertices[vi][0]), int(vertices[vi][1])

		# get the matching r for the current vertex
		r = float(self.r.get().split(",")[vi])

		# and the matching theta for the current vertex
		theta = float(self.theta.get().split(",")[vi])

		# calculate the intermediate point components (x, y)
		mx = abs(px - vx) * (r if (px < vx) else (1.0 - r)) + min(px, vx)
		my = abs(py - vy) * (r if (py < vy) else (1.0 - r)) + min(py, vy)

		# return the optionally rotated point
		return self.rotate(mx, my, vx, vy, theta)

	# returns a point rotated a specified angle around a vertex
	def rotate(self, px, py, vx, vy, theta):
		# convert theta to radians
		t = theta * pi / 180

		# calculate the point components (x, y)
		x = ((px - vx) * cos(t) - (py - vy) * sin(t)) + vx
		y = ((py - vy) * cos(t) + (px - vx) * sin(t)) + vy

		return (x, y)

	# plots a point (x, y) of radius r in a specified color
	def plot(self, x, y, r, color):
		self.c.create_oval(x, y, x + r, y + r, outline=color, fill=color)

	# callback when the user clicks on the canvas
	def click(self, e):
		if (self.user_defined_mode):
			self.user_defined_vertices.append((e.x, e.y))
			self.plot(e.x, e.y, int(self.vsize.get()), "red")

# MAIN
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title(WINDOW_TITLE)

p = ChaosGame(window)
p.play()

window.mainloop()
