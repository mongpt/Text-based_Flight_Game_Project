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
        print("There is an active bomb in the plane. Now you have only 5 times to guess the deactivation code")
        moves = 1
        playerTry = input(f"Input code # {moves}: ")
        #moves = 1
        #print(tabulate([[f"Your moves: {moves}"]], tablefmt="outline"))
        while playerTry != flightNumber and moves < 6:
            # compare the last input number to flightNumber to give player a suggestion
            print(f"Incorrect code. You have only {6 - moves} tries left")
            if int(playerTry) < int(flightNumber):
                playerTry = input("Try bigger code: ")
            else:
                playerTry = input("Try smaller code: ")
            moves += 1
            #print(tabulate([[f"Your moves: {moves}"]], tablefmt="outline"))

        if playerTry == flightNumber:
            #print(tabulate([[f"Your tries: {moves}"]], tablefmt="outline"))
            # update player's name and new score to users table
            flightInfo = reachedDestination(playerName, destAirport, moves)
            finalPoints = flightInfo.calculatePoints()
            flightInfo.updateNewPoints()

            print(f"Congratulation! {playerName}. Our lives have been saved")
            # Show player's score
            print("You got", finalPoints, "points")

            # show top 5 players
            top5Players()
        else:
            print("BOOM")

    elif userChoice == "3": #show top 5 players from database
        top5Players()

    elif userChoice == "4": #Reset users table to default values
        resetPlayerPoints()

    print("Select an option:")
    print(tabulate([["1: Help"], ["2: Play"], ["3: Top 5 Players"], ["4: Reset points"], ["Enter: quit game"]], tablefmt="double_outline"))
    userChoice = input("Your selection: ")
