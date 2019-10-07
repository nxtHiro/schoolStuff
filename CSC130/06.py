###########################################################################################
# Name: Marco Flores
# Date: 2017-11-01
# Description: 06 Random List Statistics
###########################################################################################

from random import randint

# function that prompts the user for a list size, minimum and maximum values, creates the list, and returns it
# you must use the list functions discussed in class to add integers to the list

def fillList():
    # prompts user for input for the length of the list
    listLen = input("How many random integers would you like to add to the list? ")
    # takes input from the user for the minimum boundary for list generation
    minVal = input("What would you like the minimum value to be? ")
    # takes input from the user for the maximum boundary for list generation
    maxVal = input("What would you like the maximum value to be? ")
    # declares the list
    list = []
    # generates a list of variable length from random integers
    for i in range(listLen):
        list.append(randint(minVal, maxVal))
    # returns list
    return list

# function that receives the list as a parameter, and calculates and returns the mean
def calcMean(list):
    # declares the sum variable for use in calculating the mean
    sum = 0
    # calculates the sum of all values in the list
    for i in range(len(list)):
        sum += list[i]
    # calculates the mean by dividing the sum by the number of entries in the list
    mean = sum/float(len(list))
    # returns the mean
    return mean

# function that receives the list as a parameter, and calculates and returns the median
def calcMedian(list):
    # declares the median variable
    median = 0
    # sorts the list so that the median can be found
    list.sort()
    # calculates the median in the case where the list has an even length
    if (len(list)%2 == 0):
        median = (list[len(list)/2] + list[len(list)/2 -1])/2.0
    # calculates the median in the case where the list has an odd length
    else:
        median = list[len(list)/2]
    # returns the median
    return median

# function that receives the list as a parameter, and calculates and returns the range
def calcRange(list):
    # calculates the range
    range = max(list)- min(list)
    # returns the range
    return range

###############################################
# MAIN PART OF THE PROGRAM
# implement the main part of your program below
# comments have been added to assist you
###############################################
# create the list
nums = fillList()

# display the list
print("The list: {}".format(nums))
# there is no need to write/call your own function for this part

# calculate and display the mean
print("The mean of the list is {}.".format(calcMean(nums)))

# calculate and display the median
print("The median of the list is {}.".format(calcMedian(nums)))

# calculate and display the range
print("The range of the list is {}.".format(calcRange(nums)))
