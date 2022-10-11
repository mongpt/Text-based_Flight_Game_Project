"""
This module is main file of the program. It combines other modules to have a full game
"""
# Import module files
from help import *
from top5Players import *
from showDestTable import *
from generateNum import *
from gameEnd import *
from resetPoint import *
#from connectDb import *
from tabulate import tabulate

# Show menu of the first screen
print("\nWelcome to the FLIGHT GAME")
print("Select an option:")
print(tabulate([["1: Help"], ["2: Play"],["3: Top 5 Players"], ["4: Reset points"], ["Enter: quit game"]], tablefmt="double_outline"))
userChoice = input("Your selection: ")
while userChoice == "1" or userChoice == "2" or userChoice == "3" or userChoice == "4":
    if userChoice == "1": #show help menu
        helpMenu()
    elif userChoice == "2": #start to play game
        # get player's name
        playerName = input("What is your name? ")
        # display all destination airport to let player chooses one
        showDestinationTable()
        # ask to select destination
        destAirport = int(input("Select an airport by its number from the above table: "))
        # generate a random number from selected airport
        flightNumber = str(generateNumber(destAirport))
        #print("flight number is: ", flightNumber)
        # Flying: loop until the player input the same flight number
        print("Taking off...")
        print("Now you can guess the randomly generated number, which is between 1 and the number of distance to your destination airport.\n" 
              "If the game responses ‘’turn right’, you have to guess higher number.\n"
              "If the game responses ‘’turn left, you have to guess lower number.\n" 
        playerTry = input("Flying: ")
        moves = 1
        print(tabulate([[f"Your moves: {moves}"]], tablefmt="outline"))
        while playerTry != flightNumber:
            # compare the last input number to flightNumber to give player a suggestion
            if int(playerTry) < int(flightNumber):
                playerTry = input("Turn right: ")
            else:
                playerTry = input("Turn left: ")
            moves += 1
            print(tabulate([[f"Your moves: {moves}"]], tablefmt="outline"))

        print("Landed")
        print(tabulate([[f"Your moves: {moves}"]], tablefmt="outline"))
        # update player's name and new score to users table
        flightInfo = reachedDestination(playerName, destAirport, moves)
        finalPoints = flightInfo.calculatePoints()
        flightInfo.updateNewPoints()

        # Show player's score
        print("Well done", playerName, ", you got", finalPoints, "points")

        # show top 5 players
        top5Players()

    elif userChoice == "3": #show top 5 players from database
        top5Players()

    elif userChoice == "4": #Reset users table to default values
        resetPlayerPoints()

    print("Select an option:")
    print(tabulate([["1: Help"], ["2: Play"], ["3: Top 5 Players"], ["4: Reset points"], ["Enter: quit game"]], tablefmt="double_outline"))
    userChoice = input("Your selection: ")
