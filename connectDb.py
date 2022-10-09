def connectDatabase():
    import mysql.connector
    myDb = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            database='flight_game',
            user='root',
            password='root',
            autocommit=True
        )
    return myDb.cursor()

