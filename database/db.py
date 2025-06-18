class DB:
    @staticmethod
    def run(db : dict):
        match db['type']:
            case 'MYSQL':
                keys = ['host', 'user', 'pass', 'name']

                for k in keys:
                    if k not in db:
                        return False
                
                from database.mysql_db import MYSQL_DB
                return MYSQL_DB(db)

            case 'SQLITE':
                if 'path' not in db:
                    return False

                from database.sqlite_db import SQLite_DB
                return SQLite_DB(db['path'])
        # try:
            
                    

        #     # if db['type'] == 'MYSQL':
        #     # elif db['type'] == 'SQLITE':
        # except:
        #     return False

