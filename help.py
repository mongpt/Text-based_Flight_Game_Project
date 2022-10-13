def helpMenu():
    from tabulate import tabulate
    print( "\nHOW TO PLAY" )
    print( tabulate( [["GOAL: Find the deactivation code of a timebomb to save your passengers!"],
    [" Step 1: Choose a country and an airport where you want to fly to!"],
    [" Step 2: Find the deactivation code of a timebomb with the given information."],
    [" Deactivaion code is from 1 to the number of your destination airport code. "],
    [" Step 3: If you find the correct deactivation code within 5 attempts, you can save the people's lives!"],
    [" Otherwise....today will be your last day..! "]], tablefmt = "double_outline") )
