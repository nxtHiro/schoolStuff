########################################
# Name: Jean Gourd
# Date: 2016-02-19
# Description: Audio test v2.
########################################
import RPi.GPIO as GPIO
from time import sleep
import pygame

# initialize the pygame library
pygame.init()

# set the GPIO pin numbers
# the switches (from L to R)
switches = [ 20, 16, 12, 26 ]
# the LEDs (from L to R)
leds = [6, 13, 19, 21 ]
# the sounds that map to each LED (from L to R)
sounds = [ pygame.mixer.Sound("one.wav"), pygame.mixer.Sound("two.wav"), pygame.mixer.Sound("three.wav"), pygame.mixer.Sound("four.wav") ]

# use the Broadcom pin mode
GPIO.setmode(GPIO.BCM)

# setup the input and output pins
GPIO.setup(switches, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(leds, GPIO.OUT)

print "Press the switches or Ctrl+C to exit..."

# we'll discuss this later, but this allows us to detect
# when Ctrl+C is pressed so that we can reset the GPIO pins
try:
	# keep going until the user presses Ctrl+C
	while (True):
		# initially note that no switch is pressed
		# this will help with switch debouncing
		pressed = False
		# so long as no switch is currently pressed...
		while (not pressed):
			# ...we can check the status of each switch
			for i in range(len(switches)):
				# if one switch is pressed
				while (GPIO.input(switches[i]) == True):
					# note its index
					val = i
					# note that a switch has now been pressed
					pressed = True

		# light the matching LED
		GPIO.output(leds[val], True)
		# play its corresponding sound
		sounds[val].play()
		# wait and turn the LED off again
		sleep(1)
		GPIO.output(leds[val], False)
		sleep(0.25)
# detect Ctrl+C
except KeyboardInterrupt:
	# reset the GPIO pins
	GPIO.cleanup()
	print "\nSionara!"

