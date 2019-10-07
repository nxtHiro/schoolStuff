###########################################################################################
# Name: Marco Flores
# Date: 2017-10-27
# Description: 05 A Fantastically Fabulous List
###########################################################################################

# function that:
# (1) prompts the user for a list size
# (2) prompts the user for the integers to store in the list (corresponding to the list size)
# (3) creates the list
# (4) returns the list
def fillList():
# defines list to be filled
    list = []
# takes list size in as input
    entries = input("How many integers would you like to add to the list? ")
# takes integers in as input and appends to list
    for i in range(entries):
        list.append(input("Enter an integer: "))
# returns list
    return list



###############################################
# MAIN PART OF THE PROGRAM
# implement the main part of your program below
# comments have been added to assist you
###############################################
# create the list
nums = fillList()
# prints the original list
print("The original list is: {}".format(nums))

# prints the length of the list
print("The length of the list is {}.".format(len(nums)))

# prints the minimum value in the list
print("The minimum value in the list is {}.".format(min(nums)))

# prints the maximum value in the list
print("The maximum value in the list is {}.".format(max(nums)))

# reverses then prints the list
nums.reverse()
print("The reversed list: {}".format(nums))

# sorts then prints the list
nums.sort()
print("The sorted list: {}".format(nums))


# display information about the list using the list functions discussed in class
# there is no need to write/call your own functions here
