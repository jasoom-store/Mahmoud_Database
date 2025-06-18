import sqlite3
from abstract.database import Database

class SQLite_DB(Database):
    con = ''
    cur = ''

    @classmethod
    def __init__(cls, path : str) -> None:
        cls.con = sqlite3.connect(path, check_same_thread = False)
        cls.cur = cls.con.cursor()
        cls.path = path
    
    # def __new__(cls, path):
    #     if not hasattr(cls, 'instance'):
    #         cls.instance = super(SQLite_DB, cls).__new__(cls)
    #     return cls.instance
    

