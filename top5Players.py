def top5Players():
    from tabulate import tabulate
    # connect to database
    import mysql.connector
    myDb = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='root',
        autocommit=True
    )
    myCursor = myDb.cursor()
    myCursor.execute("select row_number() over(order by points desc),name,distance,moves,points from users limit 5;")
    result = myCursor.fetchall()
    print("\nTop 5 players:")
    print(tabulate(result, headers=["Rank", "Name", "Airport Code", "Attempts", "Points"], tablefmt="double_outline"))
