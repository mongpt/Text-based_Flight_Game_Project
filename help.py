def helpMenu():
    from tabulate import tabulate
    print("\nHOW TO PLAY")
    print(tabulate([["* Step 1: You have to input your name"],
        ["* Step 2: Select destination airport by entering a number in Distance(km) column"],
        ["* Step 3:"],
        ["    - System then generates a random number to let you guess"],
        ["    - Then try to input a number in range of 1 <= input <= distance)"],
        ["    - Every time you entered a number, it counts 1 move"],
        ["    - Turn left: you must input a number that smaller than the previous one"],
        ["    - Turn right: you must input a number that greater than the previous one"],
        ["    - Repeat until you guessed the right number, means you have landed"],
        ["    - After that you will see your points (distance / moves) and the top 5 players"],
        ["    - The longer the distance, the more points you get"]], tablefmt="double_outline"))
