class reachedDestination:
    def __init__(self, player, distance, move):
        self.pName = player
        self.aDist = distance
        self.pMove = move

    def calculatePoints(self):
        return round(self.aDist / self.pMove, 2)

    def updateNewPoints(self):
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
        pPoints = self.calculatePoints()
        myCursor.execute(f"insert into users(name, distance, moves, points) values('{self.pName}',{self.aDist},{self.pMove},{pPoints});")


'''
x = reachedDestination('mong', 10, 9)
x.calculatePoints()
x.updateNewPoints()
'''