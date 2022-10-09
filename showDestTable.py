def showDestinationTable():
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
    myCursor.execute("select row_number() over(order by airport.name) + 9, airport.name, "
                     "country.name from airport, country where airport.iso_country = country.iso_country "
                     "and country.name = 'Finland' and (airport.type = 'medium_airport' or airport.type = 'large_airport');")
    result = myCursor.fetchall()
    print(tabulate(result, headers=["Distance(km)", "Airport Name", "Country"], tablefmt="double_outline"))






