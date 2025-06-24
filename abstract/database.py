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

    con = NotImplemented
    cur = NotImplemented

    @abstractmethod
    def __init__() -> None:   
        raise NotImplemented

    @classmethod
    @abstractmethod
    def db_reset_auto_increment(cls, table_name : str) -> bool:   
        raise NotImplemented

    @classmethod
    @abstractmethod
    def db_create_table(cls, table_name : str, table_schema : dict) -> bool:   
        raise NotImplemented

    @classmethod
    def db_get_all(cls, table_name : str, where : str = '', limit : int = 0):
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
    def db_get_by_pk(cls, table_name : str, pk : str, pk_value : str):
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

    #Select * from MAIN where `date` between '01.03.2020' and '05.03.2020';
    @classmethod
    def db_get_some(cls, table_name : str, pk : str, pk_1 : str, pk_2 : str):

        sql = f'SELECT * FROM `{ table_name }` WHERE `{ pk }` BETWEEN { pk_1 } AND { pk_2 }'
        try:
            cls.cur.execute(sql)

            columns = cls.cur.description

            result = [{
                columns[ind][0]: col for ind, col in enumerate(value)
            } for value in cls.cur.fetchall() ]

            return result

        except:
            return False

    # add data to database
    @classmethod
    def db_add_data(cls, table_name : str, data : dict):
        """
        add data to database :
        it takes 2 arguement 
        1 -> table_name as string 
        2 -> data as dictionary
        """
        try:
            sql = f'INSERT INTO `{ table_name }` ('
            for colume in data:
                if type(data[colume]) == str or type(data[colume]) == int:
                    sql += f'{ colume }, '
            sql = sql[:-2]
            sql += ") VALUES ("
            for colume in data :
                if type(data[colume]) == str:
                    sql += f"'{data[colume]}', "
                elif type(data[colume]) == int:
                    sql += f'{str(data[colume])}, '
            sql = sql[:-2]
            sql += ')'

            cls.cur.execute(sql)
            cls.con.commit()
            return True
        except:
            return False
        
    # drop table
    @classmethod
    def db_delete_table(cls, table_name : str):
        """
        function for drop table, it takes name  of table as an arguement
        """
        try:
            sql = f'DROP TABLE `{ table_name }`'
            cls.cur.execute(sql)
            cls.con.commit()
            return True
        except:
            return False
        

    # delete all rows in the table
    @classmethod
    def db_delete_all(cls, table_name : str):
        """
        function all rows in the table, 
        it takes name  of table as an arguement
        """
        try:
            sql = f'DELETE FROM "{ table_name }"'
            cls.cur.execute(sql)
            cls.con.commit()
            return True
        except:
            return False

    # delete one row by condition
    @classmethod
    def db_delete_one(cls, table_name : str, where : str):
        """
        function delete one row, 
        it takes name  of table as an arguement, 
        second arguement is a condition
        """
        try:
            sql = f'DELETE FROM `{ table_name }`'
            sql += f' WHERE { where }'
            cls.cur.execute(sql)
            cls.con.commit()
            return True
        except:
            return False
        

    # delete by PRIMARY KEY
    @classmethod
    def db_delete_by_pk(cls, table_name : str, pk : int):
        """
        function for delete a row with condition, 
        it takes name  of table as a first arguement
        then primary key as a second arguement
        """
        try:
            sql = f'DELETE FROM `{ table_name }`'
            sql += f' WHERE id = { pk }'
            cls.cur.execute(sql)
            cls.con.commit()
            return True
        except:
            return False
        
    #update data
    @classmethod
    def db_update_data(cls, table_name : str, data : dict, pk : str, value_pk : str):
        try:
            sql = f'UPDATE `{ table_name }` SET '
            for colume in data:
                if type(data[colume]) == str or type(data[colume]) == int:
                    sql += f'`{colume}` = ' 
                if type(data[colume]) == str :
                    sql+= f"'{data[colume]}', "
                else:
                    sql+= f'{data[colume]} , '
                        
            sql = sql[:-2]  
            sql += f' WHERE `{pk}` = '
            if type(value_pk) == str:
                sql += f"'{ value_pk }'"
            elif type(value_pk) == int:
                sql += f'{ str(value_pk) }'

            cls.cur.execute(sql)
            cls.con.commit()
            
            return True
        except:
            return False

    # SELECT * FROM users ORDER BY id DESC LIMIT 1;
    @classmethod
    def db_get_last_pk(cls, table_name : str, pk : str):
        sql = f'SELECT `{ pk }` FROM `{ table_name }` ORDER BY `{ pk }` DESC LIMIT 1'
        try:
            cls.cur.execute(sql)
            return cls.cur.fetchone()[0]
        except:
            return False
    
