import mysql.connector
from abstract.database import Database

class MYSQL_DB(Database):
    types = {
        # STR
        'str'      : 'VARCHAR',
        'string'   : 'TEXT',
        'varchar'  : 'VARCHAR',
        'char'     : 'CHAR',

        # float
        'float'    : 'FLOAT', # 0 to 23
        'double'   : 'DOUBLE', # 24 to 53

        # tnyint | -128 to 127 | 255 | 2
        # smlint | -32768 to 32767 | 65535 | 4
        # midint | -8388608 to 8388607 | 16777215 | 6
        # int    | -2147483648 to 2147483647 | 4294967295 | 9
        # bigint | -9223372036854775808 to 9223372036854775807 | 18446744073709551615 | 18

        # INT
        'tnyint'   : 'TINYINT', # 2
        'smlint'   : 'SMALLINT', # 4
        'midint'   : 'MEDIUMINT', # 6
        'int'      : 'INT', # 9
        'bigint'   : 'BIGINT', # 18

        # Other
        'bool'     : 'BOOL',
        'json'     : 'JSON',
    }

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
    
    # def __new__(cls, db):
    #     if not hasattr(cls, 'instance'):
    #         cls.instance = super(MYSQL_DB, cls).__new__(cls)
    #     return cls.instance
    
    @classmethod
    def db_reset_auto_increment(cls, table_name : str) -> bool:
        try:
            sql = f"ALTER TABLE `{ table_name }` AUTO_INCREMENT = 1"
            cls.cur.execute(sql)
            cls.con.commit()

            return True
        except:
            return False

    # CREATE TABLE `{ table_name }` (
    #   `user_id` INT(6)
    # )
    # CREATE TABLE
    @classmethod
    def db_create_table(cls, table_name : str, data : dict) -> bool:
        fk = ""
        sql = f'CREATE TABLE `{ table_name }` ( '

        for key in data:
            column = f"`{ key }` "
            
            if data[key]['type'] != '':
                # INT
                if data[key]['type'] == cls.types['int']:
                    match data[key]['ln']:
                        case x if x <= 2:
                            column += cls.types['tnyint']
                        case x if x <= 4:
                            column += cls.types['smlint']
                        case x if x <= 6:
                            column += cls.types['midint']
                        case x if x <= 9:
                            column += cls.types['int']
                        case _:
                            column += cls.types['bigint']
                # Float
                elif data[key]['type'] == cls.types['float'] or data[key]['type'] == cls.types['double']:
                    match data[key]['ln']:
                        case x if x <= 23:
                            column += cls.types['float']
                        case _:
                            column += cls.types['double']
                else:
                    column += data[key]['type']

                # When type have no size
                if (
                    data[key]['type'] == cls.types['json']
                    or data[key]['type'] == cls.types['bool']
                ):
                    pass
                else:
                    column += f"({ str(data[key]['ln']) })"

                if data[key]['type'] == cls.types['int']:
                    if (
                        'zf' in data[key] and not data[key]['zf']
                        or 'si' in data[key]
                    ):
                        if 'si' in data[key] and data[key]['si']:
                            column += ' SIGNED'
                        else:
                            column += ' UNSIGNED'
                    else:
                        column += ' ZEROFILL'

                if 'nu' in data[key] and data[key]['nu']:
                    column += ' NULL'
                else:
                    column += ' NOT NULL'
                
                # REMMBER: never use DEFAULT with ( FOREIGN KEY || UNIQUE || PRIMARY KEY )
                if (
                    'dv' in data[key]
                    and 'fk' not in data[key]
                    and 'un' not in data[key]
                    and 'pk' not in data[key]
                ):
                    column += f" DEFAULT { data[key]['dv'] }"
                
                if 'ai' in data[key] and data[key]['ai']:
                    column += ' AUTO_INCREMENT'

                # REMMBER: never use UNIQUE with PRIMARY KEY
                if 'un' in data[key] and data[key]['un'] and not 'pk' in data[key]:
                    column += ' UNIQUE'
                
                if 'pk' in data[key] and data[key]['pk']:
                    column += ' PRIMARY KEY'
            
            column += ', '

            if 'fk' in data[key]:
                fk  = f", FOREIGN KEY `{ table_name }`(`{ key }`)"
                fk += f" REFERENCES `{ data[key]['fk'] }`(`{ key }`)"

            sql += column
        sql  = sql[:-2] + fk + ' )'

        try:
            cls.cur.execute(sql)
            cls.con.commit()
            return True
        except:
            return False
        
