###########################################################################################
# Name: Marco Flores
# Date: 2017-10-13
# Description: CSC130 Easy Does It
###########################################################################################

# prompt the user for a name and an age
name = input("Enter your name: ")
age = input("How old are you, {}? ".format(name))

# display the final output
print "Hi, {}. You are {} years old. Twice your age is {}.".format(name, age, age*2)
