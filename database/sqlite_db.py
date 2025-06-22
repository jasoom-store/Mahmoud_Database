import sqlite3
from abstract.database import Database

class SQLite_DB(Database):
    types = {
        'bool'    : 'BOOL',
        'float'   : 'REAL',

        # STR
        'str'     : 'TEXT',
        'string'  : 'TEXT',
        'varchar' : 'TEXT',
        'char'    : 'TEXT',
        'json'    : 'TEXT',

        # INT
        'int'     : 'INTEGER',
    }

    @classmethod
    def __init__(cls, path : str) -> None:
        cls.con = sqlite3.connect(path, check_same_thread = False)
        cls.cur = cls.con.cursor()
        cls.path = path
    
    # def __new__(cls, path):
    #     if not hasattr(cls, 'instance'):
    #         cls.instance = super(SQLite_DB, cls).__new__(cls)
    #     return cls.instance

    @classmethod
    def reset_auto_increment(cls, table_name : str) -> bool:
        try:
            sql = f"UPDATE SQLITE_SEQUENCE SET SEQ = 0 WHERE NAME = '{ table_name }'"
            cls.cur.execute(sql)
            cls.con.commit()

            return True
        except:
            return False
    
    # CREATE TABLE
    @classmethod
    def create_table(cls, table_name : str, data : dict) -> bool:
        fk = ""

        sql = f'CREATE TABLE `{ table_name }` ( '

        for key in data:
            column  = f"`{ key }` { data[key]['type'] }"

            if 'nu' in data[key] and data[key]['nu']:
                column += ' NULL'
            else:
                column += ' NOT NULL'

            if 'pk' in data[key] and data[key]['pk']:
                column += ' PRIMARY KEY'
            
            # REMMBER: never use UNIQUE with PRIMARY KEY
            if 'un' in data[key] and data[key]['un'] and not 'pk' in data[key]:
                column += ' UNIQUE'

            # REMMBER: never use AUTOINCREMENT without PK
            if (
                'ai' in data[key] and data[key]['ai']
                and 'pk' in data[key] and data[key]['pk']
            ):
                column += ' AUTOINCREMENT'

            # REMMBER: never use DEFAULT with ( FOREIGN KEY || UNIQUE || PRIMARY KEY )
            if (
                    'dv' in data[key]
                    and 'fk' not in data[key]
                    and 'un' not in data[key]
                    and 'pk' not in data[key]
                ):
                column += f" DEFAULT { data[key]['dv'] }"

            if 'fk' in data[key]:
                fk  = f", FOREIGN KEY `{ table_name }`(`{ key }`)"
                fk += f" REFERENCES `{ data[key]['fk'] }`(`{ key }`)"
            
            column += ', '

            sql += column
        sql  = sql[:-2] + fk + ' )'

        # return sql
        try:
            cls.cur.execute(sql)
            cls.con.commit()
            return True
        except:
            return False
    
    

