import mysql.connector
from abstract.database import Database

class MYSQL_DB(Database):
    types = {
        # STR
        'str'      : 'VARCHAR',
        'string'   : 'TEXT',

        # 
        'bool'     : 'BOOL',
        'float'    : 'DOUBLE',
        'varchar'  : 'VARCHAR',
        'char'     : 'CHAR',
        'json'     : 'JSON',

        # INT
        'tnyint'   : 'TINYINT', # 2
        'smlint'   : 'SMALLINT', # 4
        'midint'   : 'MEDIUMINT', # 6
        'int'      : 'INT', # 9
        'bigint'   : 'BIGINT', # 18
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
    def reset_auto_increment(cls, table_name : str) -> bool:
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
    def create_table(cls, table_name : str, data : dict) -> bool:
        pk = ""
        fk = ""

        sql = f'CREATE TABLE `{ table_name }` ( '

        for key in data:
            column = f"`{ key }` "
            
            if data[key]['type'] != '':
                # INT
                if data[key]['type'] == cls.types['int']:
                    if data[key]['ln'] <= 2:
                        column += cls.types['tnyint']
                    elif data[key]['ln'] <= 4:
                        column += cls.types['smlint']
                    elif data[key]['ln'] <= 6:
                        column += cls.types['midint']
                    elif data[key]['ln'] > 9:
                        column += cls.types['bigint']
                    else:
                        column += data[key]['type']
                # STR
                elif data[key]['type'] == cls.types['str']:
                    column += data[key]['type']
                else:
                    column += data[key]['type']

                # INT
                if data[key]['type'] == cls.types['json']:
                    pass
                else:
                    column += f"({ str(data[key]['ln']) })"

                if data[key]['type'] == cls.types['int']:
                    if 'si' in data[key] and data[key]['si']:
                        column += ' SIGNED'
                    else:
                        column += ' UNSIGNED'

                # if data[key]['type'] == cls.types['int']:
                #     column += ' ZEROFILL'

                if data[key]['type'] != cls.types['int']:
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
                
                # REMMBER: never use AUTO_INCREMENT without PK
                if (
                    'ai' in data[key] and data[key]['ai']
                    and 'pk' in data[key] and data[key]['pk']
                ):
                    column += ' AUTO_INCREMENT'

                # REMMBER: never use UNIQUE with PRIMARY KEY
                if 'un' in data[key] and data[key]['un'] and not 'pk' in data[key]:
                    column += ' UNIQUE'
                
                if 'pk' in data[key] and data[key]['pk']:
                    column += ' PRIMARY KEY'
            
            column += ', '

            # if 'pk' in data[key] and data[key]['pk']:
            #     pk = f', PRIMARY KEY (`{ key }`)'

            if 'fk' in data[key]:
                fk  = f", FOREIGN KEY `{ table_name }`(`{ key }`)"
                fk += f" REFERENCES `{ data[key]['fk'] }`(`{ key }`)"

            sql += column
        sql  = sql[:-2] + pk + fk + ' )'

        # return sql
        try:
            cls.cur.execute(sql)
            cls.con.commit()
            return True
        except:
            return False
        
