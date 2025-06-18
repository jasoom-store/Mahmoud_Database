import sqlite3
from abstract.database import Database

class SQLite_DB(Database):
    con = ''
    cur = ''

    @classmethod
    def __init__(cls, path : str) -> None:
        cls.con = sqlite3.connect(path)
        cls.cur = cls.con.cursor()
    

