###########################################################################################
# Name: Marco Flores
# Date: 2017-12-18
# Description: Room Adventure Text Adventure Game
###########################################################################################

###########################################################################################
# the blueprint for a room
class Room(object):
	# the constructor
	def __init__(self, name):
		# rooms have a name, exits (e.g., south), exit locations (e.g., to the south is room n),
		# items (e.g., table), item descriptions (for each item), and grabbables (things that can
		# be taken into inventory)
		self.name = name
		self.exits = []
		self.exitLocations = []
		self.items = []
		self.itemDescriptions = []
		self.grabbables = []
	# getters and setters for the instance variables
	@property
	def name(self):
			return self._name
	@name.setter
	def name(self, val):
		self._name = val

	@property
	def exits(self):
		return self._exits

	@exits.setter
	def exits(self, value):
		self._exits = value

	@property
	def exitLocations(self):
		return self._exitLocations

	@exitLocations.setter
	def exitLocations(self, value):
		self._exitLocations = value

	@property
	def items(self):
		return self._items

	@items.setter
	def items(self, value):
		self._items = value

	@property
	def itemDescriptions(self):
		return self._itemDescriptions

	@itemDescriptions.setter
	def itemDescriptions(self, value):
		self._itemDescriptions = value

	@property
	def grabbables(self):
		return self._grabbables

	@grabbables.setter
	def grabbables(self, value):
		self._grabbables = value


	# adds an exit to the room
	# the exit is a string (e.g., north)
	# the room is an instance of a room
	def addExit(self, exit, room):
		# append the exit and room to the appropriate lists
		self._exits.append(exit)
		self._exitLocations.append(room)
	# adds an item to the room
	# the item is a string (e.g., table)
	# the desc is a string that describes the item (e.g., it is made of wood)
	def addItem(self, item, desc):
		# append the item and description to the appropriate lists
		self._items.append(item)
		self._itemDescriptions.append(desc)

	# adds a grabbable item to the room
	# the item is a string (e.g., key)
	def addGrabbable(self, item):
		# append the item to the list
		self._grabbables.append(item)

	# removes a grabbable item from the room
	# the item is a string (e.g., key)

	def delGrabbable(self, item):
		# remove the item from the list
		self._grabbables.remove(item)

	# returns a string description of the room
	# improved grammar of the print statements
	def __str__(self):
		# first, the room name
		s = "You are at the {}.\n".format(self.name)

		# next, the items in the room
		s += "You see "
		for i in range(len(self.items)):
			if (len(self.items) > 2 and i != len(self.items) - 1):
				s+= self.items[i] + ", "
			else:
				s += self.items[i] + " "
			if (i == len(self.items)-2):
				s += "and "
		s = s[:-1] + "."
		s += "\n"

		# next, the exits from the room
		s += "Exits are "
		for i in range(len(self.exits)):
			if (len(self.exits) > 2 and i != len(self.exits) - 1):
				s+= self.exits[i] + ", "
			else:
				s += self.exits[i] + " "
			if (i == len(self.exits)-2):
				s += "and "
		s = s[:-1] + "."
		return s

###########################################################################################
# creates the rooms
# added several rooms as well as a second floor
def createRooms():
	global currentRoom
	global r9
	global r10
	global r11
	r1 = Room("Foyer")
	r2 = Room("Living Room")
	r3 = Room("Kitchen")
	r4 = Room("Hallway")
	r5 = Room("End of the Hallway")
	r6 = Room("Dining Room")
	r7 = Room("Bathroom")
	r8 = Room("Man Cave")
	r9 = Room("Brewery")
	r10 = Room("Upstairs Hallway")
	r11 = Room("Entrance to a mystery room")

	r1.addItem("coatrack", "The brass coatrack seems to lack any sort of garments being hung from it.")
	r1.addItem("bench", "The bench has remarkable craftsmanship made up of oak and leather.")
	r1.addItem("mirror", "You check the mirror only to see yourself. You look mildly presentable.")
	r1.addExit("west", r2)
	r1.addExit("north", r4)

	r2.addGrabbable("remote")
	r2.addItem("chair", "The chair seems to be one of great age, but there seems to be a remote in the cushion of the chair.")
	r2.addItem("credenza", "You look upon the credenza to see a television. It is of decent size, despite its obvious age.")
	r2.addExit("east", r1)
	r2.addExit("north", r6)

	r3.addItem("oven", "The oven is off, there does however seem to be a large mass of dishes on the stovetop.")
	r3.addItem("refridgerator", "The refridgerator is chained shut. There are many magnets, most of which are for various pizza delivery services. One stands out to you as it has the last four digits circled: 5309.")
	r3.addExit("south", r4)
	r3.addExit("west", r6)

	r4.addItem("nothing of particular interest", "")
	r4.addExit("south", r1)
	r4.addExit("east", r5)
	r4.addExit("north", r3)

	r5.addItem("stairs", "The stairs appear to be rather sturdy.")
	r5.addExit("west", r4)
	r5.addExit("upstairs", r10)

	r6.addItem("table", "The table is made of oak and has several placemats on top of it.")
	r6.addItem("chairs", "The chairs match the table in the room.")
	r6.addExit("south", r2)
	r6.addExit("east", r3)

	r7.addItem("sink", "The sink is cluttered with magazines, toothbrushes, and various other hygene products.")
	r7.addItem("toilet", "The toilet seems to be acceptably clean.")
	r7.addExit("south", r10)

	r8.addItem("pc", "The PC has LEDs and is very obviously a powerful machine.")
	r8.addItem("pizza boxes", "The pizza boxes clutter the room.")
	r8.addExit("east", r10)

	r9.addExit("west", r11)

	r10.addItem("nothing of particular interest", "")
	r10.addExit("north", r7)
	r10.addExit("west", r8)
	r10.addExit("downstairs", r5)

	r11.addItem("keypad", "There is a keypad on what appears to be a sealed door to the east.")
	r11.addExit("west", r10)

	currentRoom = r1

# displays an appropriate "message" when the player dies
# yes, this is intentionally obfuscated!
def death():
	print " " * 17 + "u" * 7
	print " " * 13 + "u" * 2 + "$" * 11 + "u" * 2
	print " " * 10 + "u" * 2 + "$" * 17 + "u" * 2
	print " " * 9 + "u" + "$" * 21 + "u"
	print " " * 8 + "u" + "$" * 23 + "u"
	print " " * 7 + "u" + "$" * 25 + "u"
	print " " * 7 + "u" + "$" * 25 + "u"
	print " " * 7 + "u" + "$" * 6 + "\"" + " " * 3 + "\"" + "$" * 3 + "\"" + " " * 3 + "\"" + "$" * 6 + "u"
	print " " * 7 + "\"" + "$" * 4 + "\"" + " " * 6 + "u$u" + " " * 7 + "$" * 4 + "\""
	print " " * 8 + "$" * 3 + "u" + " " * 7 + "u$u" + " " * 7 + "u" + "$" * 3
	print " " * 8 + "$" * 3 + "u" + " " * 6 + "u" + "$" * 3 + "u" + " " * 6 + "u" + "$" * 3
	print " " * 9 + "\"" + "$" * 4 + "u" * 2 + "$" * 3 + " " * 3 + "$" * 3 + "u" * 2 + "$" * 4 + "\""
	print " " * 10 + "\"" + "$" * 7 + "\"" + " " * 3 + "\"" + "$" * 7 + "\""
	print " " * 12 + "u" + "$" * 7 + "u" + "$" * 7 + "u"
	print " " * 13 + "u$\"$\"$\"$\"$\"$\"$u"
	print " " * 2 + "u" * 3 + " " * 8 + "$" * 2 + "u$ $ $ $ $u" + "$" * 2 + " " * 7 + "u" * 3
	print " u" + "$" * 4 + " " * 8 + "$" * 5 + "u$u$u" + "$" * 3 + " " * 7 + "u" + "$" * 4
	print " " * 2 + "$" * 5 + "u" * 2 + " " * 6 + "\"" + "$" * 9 + "\"" + " " * 5 + "u" * 2 + "$" * 6
	print "u" + "$" * 11 + "u" * 2 + " " * 4 + "\"" * 5 + " " * 4 + "u" * 4 + "$" * 10
	print "$" * 4 + "\"" * 3 + "$" * 10 + "u" * 3 + " " * 3 + "u" * 2 + "$" * 9 + "\"" * 3 + "$" * 3 + "\""
	print " " + "\"" * 3 + " " * 6 + "\"" * 2 + "$" * 11 + "u" * 2 + " " + "\"" * 2 + "$" + "\"" * 3
	print " " * 11 + "u" * 4 + " \"\"" + "$" * 10 + "u" * 3
	print " " * 2 + "u" + "$" * 3 + "u" * 3 + "$" * 9 + "u" * 2 + " \"\"" + "$" * 11 + "u" * 3 + "$" * 3
	print " " * 2 + "$" * 10 + "\"" * 4 + " " * 11 + "\"\"" + "$" * 11 + "\""
	print " " * 3 + "\"" + "$" * 5 + "\"" + " " * 22 + "\"\"" + "$" * 4 + "\"\""
	print " " * 5 + "$" * 3 + "\"" + " " * 25 + "$" * 4 + "\""
	print "You fell to your death."

###########################################################################################
# main
# START THE GAME!!!
print ("Welcome to the Mansion, may you enjoy your adventure. Your goal is to find the source of the noise and smoke coming from the Mansion. Press enter to begin.")
start = raw_input()
if start == start:
	gameStart = True
inventory = []
createRooms()
# play forever after initiating the game (well, at least until the player dies or asks to quit)
while (gameStart):
	# set the status so the player has situational awareness
	# the status has room and inventory information
	status = "{}\nYou are carrying ".format(currentRoom)
	# prints contents of the list without the list format
	for i in range(len(inventory)):
		if (len(inventory) > 2 and i != len(inventory) - 1):
			status+= inventory[i] + ", "
		else:
			status += inventory[i] + " "
		if (i == len(inventory)-2):
			status += "and "
	# if list is empty prints that the user is carrying nothing
	if (len(inventory) == 0):
		status += "nothing.\n"
	else:
		status = status[:-1] + "."
	# if the current room is None, then the player is dead
	# this only happens if the player goes south when in room 4
	# exit the game
	if (currentRoom == None):
		death()
		break
	# display the status
	print "========================================================="
	print status
	# prompt for player input
	# the game supports a simple language of <verb> <noun>
	# valid verbs are go, look, and take
	# valid nouns depend on the verb
	# we use raw_input here to treat the input as a string instead of
	# an expression
	action = raw_input("What to do? ")
	# set the user's input to lowercase to make it easier to compare
	# the verb and noun to known values
	action = action.lower()
	# exit the game if the player wants to leave (supports quit,
	# exit, and bye)
	if (action == "quit" or action == "exit" or action == "bye"):
		break
	# set a default response
	response = "I don't understand.  Try verb noun.  Valid verbs are go, look, and take"
	# assigns default value to verb
	verb = 0
	# split the user input into words (words are separated by spaces)
	# and store the words in a list
	words = action.split()
	# the game only understands two word inputs
	if (len(words) == 2):
		# isolate the verb and noun
		verb = words[0]
		noun = words[1]
	# the verb is: go
	if (verb == "go"):
		# set a default response
		response = "Invalid exit."
		# check for valid exits in the current room
		for i in range(len(currentRoom.exits)):
			# a valid exit is found
			if (noun == currentRoom.exits[i]):
				# change the current room to the one that is
				# associated with the specified exit
				currentRoom, lastRoom = currentRoom.exitLocations[i], currentRoom
				# set the response (success)
				response = "Room changed."
				# no need to check any more exits
				break
	# the verb is: look
	elif (verb == "look"):
		# set a default response
		response = "I don't see that item."
		# check for valid items in the current room
		for i in range(len(currentRoom.items)):
			# a valid item is found
			if (noun == currentRoom.items[i]):
				# set the response to the item's description
				response = currentRoom.itemDescriptions[i]
				# keypad puzzle
				if (noun == "keypad"):
					i = input("There seems to have been an optical scanner in the keypad. The keypad is now saying \"unrecognized visitor, enter keycode or prepare to be ejected\".\n")
					if (i == 5309):
						print "\nAccess granted"
						r11.addExit("east", r9)
					else:
						death()
						exit(0)
				# no need to check any more items
				break
	# the verb is: take
	elif (verb == "take"):
		# set a default response
		response = "I don't see that item."
		# check for valid grabbable items in the current room
		for grabbable in currentRoom.grabbables:
			# a valid grabbable item is found
			if (noun == grabbable):
			# add the grabbable item to the player's inventory
				inventory.append(grabbable)
				# remove the grabbable item from the room
				currentRoom.delGrabbable(grabbable)
				# set the response (success)
				response = "Item grabbed."
				# no need to check any more grabbable items
				break
	# Addition of the keyword use
	# the verb is: use
	elif (verb == "use"):
		# set a default response
		response = "That item is not in your inventory."
		for i in range(len(inventory)):
			# a valid grabbable is found
			if (noun == inventory[i]):
				response = "You used the {}.".format(inventory[i])
				# usage behavior for remote adding access to the keypad room
				if (noun == "remote"):
					print "\nYou hear a rumbling upstairs."
					r10.addExit("east", r11)
	# victory screen
	if (currentRoom == r9):
		print "Congratulations! You have located the origin of the smoke and noise."
		exit(0)
	# display the response
	print "\n{}".format(response)
