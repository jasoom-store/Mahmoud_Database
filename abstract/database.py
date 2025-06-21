from abc import ABCMeta, abstractmethod

class Database(metaclass=ABCMeta):
    # @property
    # @abstractmethod
    # def con(self):
    #     raise NotImplemented
    
    # @property
    # @abstractmethod
    # def cur(self):
    #     raise NotImplemented

    @abstractmethod
    def __init__() -> None:
        raise NotImplemented

    @classmethod
    def get_all(cls, table_name : str, where : str = '', limit : int = 0):
        sql  = f"SELECT * FROM `{ table_name }`"
        sql += f" WHERE { where }" if len(where) > 0 else ''
        sql += f" LIMIT { str(limit) }" if limit > 0 else ''

        try:
            cls.cur.execute(sql)
            
            columns = cls.cur.description

            result = [{
                columns[ind][0]: col for ind, col in enumerate(value)
            } for value in cls.cur.fetchall() ]

            return result
        except:
            return False

    @classmethod
    def get_by_pk(cls, table_name : str, pk : str, pk_value : str):
        sql = f"SELECT * FROM `{ table_name }`"  
        sql += f" WHERE `{ pk }` = { pk_value }"
        try:
            cls.cur.execute(sql)

            columns = cls.cur.description

            # result = {}
            # for ind, val in enumerate(cls.cur.fetchone()):
            #     result[columns[ind][0]] = val

            # { k: v for }

            return {
                columns[ind][0]: col
                for ind, col in enumerate(cls.cur.fetchone())
            }
        except:
            return False

    