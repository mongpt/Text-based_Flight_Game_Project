def helpMenu():
  from tabulate import tabulate
  print( "\nHOW TO PLAY" )
  print( tabulate( [["GOAL: Find the correct number to arrive at your destination!"],
  [" Step 1: Choose a country and an airport where you want to fly to!"],
  [" Step 2: Engine will generate a random number(between 1 and the distance to your destination)."],
  [" Step 3: When you guess the correct number, you can land to your destination. "],
  ["Whenever you put a new number, it will be counted as a move.\n"],
  ["The lower the number of moves, the higher score you can get."]], tablefmt = "double_outline"))
