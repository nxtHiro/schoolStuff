###########################################################################################
# Name: Marco Flores
# Date: 2017-12-01
# Description: 01 How many Zeroes?
###########################################################################################

# imports time function from time library
from time import time
def counter(value):
# defines and initiates zero counter
    zeroes = 0
# for loop that counts zeroes through the modulo and division
    for i in range(1, value + 1):
        num = i
        while(num != 0):
            if (num % 10 == 0):
                zeroes += 1
            num /= 10
    return zeroes
# takes number to count zeroes of as input
number = input("What number do you want to count zeroes to? ")
# begins the timer
start_time = time()
# calls counter function
zeroes = counter(number)
# ends the timer as the loop stops running
end_time = time()
# prints the results of the counter
print ("The number of zeroes written from 1 to {} is {}.".format(number, zeroes))
# prints the timer value
print ("This took {} seconds.".format(end_time - start_time))
