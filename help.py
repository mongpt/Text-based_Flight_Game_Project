def helpMenu():
    from tabulate import tabulate
    print( "\nHOW TO PLAY" )
    print( tabulate( [["GOAL: Find deactivation code to save your flight and passengers!"],
    [" Step 1: Choose a country and an airport where you want to fly to!"],
    [" Step 2: Find a deactivation code of the timebomb."],
    [" Step 3: If you find the correct deactivation code within 5 attempts, you can save people's life!"]], tablefmt = "double_outline"))
