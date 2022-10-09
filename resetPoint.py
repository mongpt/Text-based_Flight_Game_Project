def resetPlayerPoints():
    print("Resetting...")
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
    myCursor.execute("drop table if exists users;")
    myCursor.execute("create table users(name varchar(10),distance int,moves int,points float);")
    myCursor.execute("insert into users(name, distance, moves, points)values('A', 10, 6, 1.67),"
                     "('B', 10, 7, 1.43),('C', 10, 8, 1.25),('D', 10, 9, 1.11),('E', 10, 10, 1);")
    print("Player table has been reset to the default values \n")