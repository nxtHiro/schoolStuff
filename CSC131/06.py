#########################################################
# Name: Marco Flores
# Date: 2018-02-07
# Description: A Foolproof Game
#########################################################
from random import randint

# function for the coin flips
def coinFlip():
    a = randint(0, 1)
    b = randint(0, 1)
    return a, b

# defines and initializes the necessary variables
grpa = 0
grpb = 0
prof = 0
winperA = 0
winperB = 0
winperProf = 0
gameWinA = 0
gameWinB = 0
gameWinProf = 0
gameWinPercA = 0
gameWinPercB = 0
gameWinPercProf = 0

# takes input for the number of games and tosses per game
runs = input("How many games? ")
tosses = input("How many coin tosses? ")

# processes the games
for i in range(1, runs+1):
    # zeroes the stats for a specific game
    grpa = 0
    grpb = 0
    prof = 0
    winperA = 0
    winperB = 0
    winperProf = 0

    print "Game: {}".format(i-1)

    # processes results for the flips
    for j in range(tosses):
        a, b = coinFlip()
        if (a == 1 and b == 1):
            grpa += 1
        elif(a == 0 and b == 0):
            grpb += 1
        else:
            prof += 1
    # calculates win percentages
    winperA = grpa*1.0/tosses * 100
    winperB = grpb*1.0/tosses * 100
    winperProf = prof*1.0/tosses * 100

    # prints results of the game
    print " Group A: {} ({}%); Group B: {} ({}%); Prof: {} ({}%)".format(grpa, winperA, grpb, winperB, prof, winperProf)

    # adds a win to the winner of the game
    if (winperA > winperB and winperA > winperProf):
        gameWinA += 1
    elif (winperB > winperA and winperB > winperProf):
        gameWinB += 1
    elif (winperProf > winperA and winperProf > winperB):
        gameWinProf += 1

    # calculates game win percentages
    gameWinPercA = gameWinA*1.0/i * 100
    gameWinPercB = gameWinB*1.0/i * 100
    gameWinPercProf = gameWinProf*1.0/i * 100

    # prints wins and percentages
    print "Wins: Group A={} ({}%); Group B={} ({}%); Prof={} ({}%)".format(gameWinA, gameWinPercA, gameWinB, gameWinPercB, gameWinProf, gameWinPercProf)
