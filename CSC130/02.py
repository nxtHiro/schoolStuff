###########################################################################################
# Name: Marco Flores
# Date: 2017-10-16
# Description: CSC130 Easy Does It... Reloaded
###########################################################################################

# Gets and returns the user's name
def takeName() :
    name = input("Please enter your name: ")
    return name

# Gets and returns the user's age
def takeAge(name) :
    age = input("How old are you, {}? ".format(name))
    return age

# Takes provided name and age and prints the final requested statement
def printFinalOutput(name, age) :
    print("Hi, {}. You are {} years old. Twice your age is {}.".format(name, age, age*2))


###############################################
# MAIN PART OF THE PROGRAM
# implement the main part of your program below
# comments have been added to assist you
###############################################

# prompt for a name
name = takeName()

# prompt for an age
age = takeAge(name)

# display the final output
printFinalOutput(name, age)
