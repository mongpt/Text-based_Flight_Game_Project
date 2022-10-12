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
    #Select Country
    country = ["Argentina", "Bangladesh", "Denmark", "Estonia", "Finland", "Nepal", "Norway", "South Korea", "Sweden", "Vietnam"]
    print(tabulate([["1. Argentina"], ["2. Bangladesh"], ["3. Denmark"], ["4. Estonia"], ["5. Finland"], ["6. Nepal"],
                      ["7. Norway"], ["8. South Korea"], ["9. Sweden"], ["10.Vietnam"]], tablefmt="double_outline" ) )
    destCountry = int(input( "Enter the number of the country where you want to fly: " ))
    country_pick = country[destCountry-1]
    myCursor = myDb.cursor()
    myCursor.execute("select row_number() over(order by airport.name) + 9, airport.name, "
                     "country.name from airport, country where airport.iso_country = country.iso_country "
                     f"and country.name = '{country_pick}' and (airport.type = 'medium_airport' or airport.type = 'large_airport');")

    result = myCursor.fetchall()
    print(tabulate(result, headers=["Airport Code", "Airport Name", "Country"], tablefmt="double_outline"))



