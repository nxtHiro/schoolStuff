######################################################################################################################
# Name: Marco Flores
# Date: 2018-02-20
# Description: 07 Sort Comparisons and Swaps... Reloaded
######################################################################################################################

from plot import plot

# creates the list
def getList():
	return [100, 5, 63, 29, 69, 74, 96, 80, 82, 12]
#	return [82, 65, 93, 0, 60, 31, 99, 90, 31, 70]
#	return [63, 16, 78, 69, 36, 36, 3, 66, 75, 100]
#	return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#	return [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#	return [2, 1, 4, 3, 6, 5, 8, 7, 10, 9]

# the bubble sort function
# input: a list of integers
# output: a number of comparisons and swaps
def bubbleSort(list):
	comparisons = 0
	swaps = 0
	temp = 0
	for j in range(1, len(list)):
		for i in range(1, len(list)-j+1):
			comparisons += 1
			if (list[i]<list[i-1]):
				swaps += 1
				temp = list[i]
				list[i] = list[i-1]
				list[i-1] = temp
	return [comparisons, swaps]

# the optimized bubble sort function
# input: a list of integers
# output: a number of comparisons and swaps
def optBubbleSort(list):
	comparisons = 0
	swaps = 0
	temp = 0
	swapMade = False
	for j in range(1, len(list)):
		swapMade = False
		for i in range(1, len(list)-j+1):
			comparisons += 1
			if (list[i]<list[i-1]):
				swapMade = True
				swaps += 1
				temp = list[i]
				list[i] = list[i-1]
				list[i-1] = temp
		if (not swapMade):
			break
	return comparisons, swaps

# the selection sort function
# input: a list of integers
# output: a number of comparisons and swaps
def selectionSort(list):
	comparisons = 0
	swaps = 0
	temp = 0
	for i in range(len(list)-1):
		minIndex = i
		for j in range(i+1, len(list)):
			comparisons += 1
			if (list[minIndex] > list[j]):
				minIndex = j
		temp = list[i]
		list[i] = list[minIndex]
		list[minIndex] = temp
		swaps += 1
	return [comparisons, swaps]

# the insertion sort function
# input: a list of integers
# output: a number of comparisons and swaps
def insertionSort(list):
	comparisons = 0
	swaps = 0
	i = 1
	n = len(list)
	temp = 0
	j = 0

	while (i < n):
		comparisons += 1
		if (list[i-1] > list[i]):
			comparisons += 1
			temp = list[i]
			j = i-1
			while (j >= 0 and list[j] > temp):
				comparisons += 1
				swaps += 1
				list[j+1] = list[j]
				j -= 1
			list[j+1] = temp
		i += 1
	return [comparisons, swaps]

# the main part of the program

# obtains list values
list = getList()
# prints the unsorted list
print "The list: {}".format(list)
# runs bubbleSort to sort and receive number of comparisons and swaps
bsc = bubbleSort(list)
# prints the list after the bubble sort
print "After bubble sort: {}".format(list)
# prints the number of comparisons and swaps
print "{} comparisons; {} swaps".format(bsc[0], bsc[1])


# obtains list values
list = getList()
# prints the unsorted list
print "The list: {}".format(list)
# runs optBubbleSort to sort and receive number of comparisons and swaps
obsc = optBubbleSort(list)
# prints the list after the optimized bubble sort
print "After optimized bubble sort: {}".format(list)
# prints the number of comparisons and swaps
print "{} comparisons; {} swaps".format(obsc[0], obsc[1])


# obtains list values
list = getList()
# prints the unsorted list
print "The list: {}".format(list)
# runs selectionSort to sort and receive number of comparisons and swaps
selsc = selectionSort(list)
# prints the list after the bubble sort
print "After selection sort: {}".format(list)
# prints the number of comparisons and swaps
print "{} comparisons; {} swaps".format(selsc[0], selsc[1])


# obtains list values
list = getList()
# prints the unsorted list
print "The list: {}".format(list)
# runs insertionSort to sort and receive number of comparisons and swaps
inssc = insertionSort(list)
# prints the list after the insertion sort
print "After insertion sort: {}".format(list)
# prints the number of comparisons and swaps
print "{} comparisons; {} swaps".format(inssc[0], inssc[1])

# calls the plot function to display the values in a graph
plot(bsc, obsc, selsc, inssc)
