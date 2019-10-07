###########################################################################################
# Name: Marco Flores
# Date: 2017-10-18
# Description: CSC 130 Casual Statistics
###########################################################################################

# function that prompts the user to enter an integer and returns it
def integerInput() :
    return input("Please enter an integer: ")
# function that receives three integers as parameters and returns the minimum of the three
def calcMin(val1, val2, val3) :
    min = val1
    if (min > val2) :
        min = val2
    if (min > val3) :
        min = val3
    return min

# function that receives three integers as parameters and returns the maximum of the three
def calcMax(val1, val2, val3) :
    max = val1
    if (max < val2) :
        max = val2
    if (max < val3) :
        max = val3
    return max

# function that receives three integers as parameters, and calculates and returns the mean
def calcMean(val1, val2, val3) :
    return (val1+val2+val3)/3.0

# function that receives three integers as parameters, and calculates and returns the median
def calcMedian(val1, val2, val3) :
    minVal = calcMin(val1, val2, val3)
    maxVal = calcMax(val1, val2, val3)
    modeVal = calcMode(val1,val2,val3)
    if(modeVal == "undefined") :
        med = val2
        if (val1 != minVal and val1 != maxVal) :
            med= val1
        elif (val2 != minVal and val2 != maxVal) :
            med = val2
        elif (val3 != minVal and val3 != maxVal) :
            med = val3
        return med
    else :
        return modeVal

# function that receives three integers as parameters, and calculates and returns the mode
def calcMode(val1, val2, val3) :
    numOfVal1 = 1
    numOfVal2 = 1
    if(val1 == val2) :
        numOfVal1 += 1
    if(val1 == val3) :
        numOfVal1 += 1
    if(val2 == val3) :
        numOfVal2 += 1
    if(numOfVal1>numOfVal2) :
        mode = val1
    elif(numOfVal2>numOfVal1) :
        mode = val2
    else :
        mode = "undefined"
    return mode

# function that receives three integers as parameters, and calculates and returns the range
def calcRange(val1, val2, val3) :
    minVal = calcMin(val1, val2, val3)
    maxVal = calcMax(val1, val2, val3)
    return maxVal-minVal


###############################################
# MAIN PART OF THE PROGRAM
# implement the main part of your program below
# comments have been added to assist you
###############################################
# get three integers from the user
val1 = integerInput()
val2 = integerInput()
val3 = integerInput()

# determine and display the minimum value
minVal = calcMin(val1, val2, val3)
print("The minimum value is {}.".format(minVal))

# determine and display the maximum value
maxVal = calcMax(val1, val2, val3)
print("The maximum value is {}.".format(maxVal))

# calculate and display the mean
meanVal = calcMean(val1, val2, val3)
print("The mean is {}.".format(meanVal))

# calculate and display the median
medianVal = calcMedian(val1, val2, val3)
print("The median is {}. ".format(medianVal))

# calculate and display the mode
modeVal = calcMode(val1, val2, val3)
print("The mode is {}. ".format(modeVal))
# calculate and display the range
rangeVal = calcRange(val1, val2, val3)
print("The range is {}. ".format(rangeVal))
