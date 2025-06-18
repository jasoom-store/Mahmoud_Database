import mysql.connector
from abstract.database import Database

class MYSQL_DB(Database):
    @classmethod
    def __init__(cls, db : dict) -> None:
        cls.con = mysql.connector.connect(
            host = db['host'],
            user = db['user'],
            password = db['pass'],
            database = db['name'],
            use_pure = True
        )
        cls.cur = cls.con.cursor()
    

        
