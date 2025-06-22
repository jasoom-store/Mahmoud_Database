from abc import ABCMeta, abstractmethod
from database.db import DB

from config import config

class Model(metaclass=ABCMeta):
    database = config.database
    table_name: str = NotImplemented
    pk: str = NotImplemented
    table_schema: dict = NotImplemented

    @classmethod
    def con(cls):
        return DB.run(cls.database)

    @classmethod
    def get_all(cls, where : str = '', limit : str = ''):
        return cls.con().get_all(cls.table_name, where, limit)

    # @classmethod
    # def get_all_no_id(cls, where : str = '', limit : str = ''):
    #     return cls.con().get_all_no_id(cls.table_name, cls.table_schema, cls.pk, where, limit)

    @classmethod
    def get_some(cls, frm : int, to : int):
        return cls.con().get_some(cls.table_name, cls.pk, frm, to)

    # @classmethod
    # def get_all_join(cls, anther_table):
    #     return cls.con().get_all_join(cls, anther_table)
    
    @classmethod
    def get_by_pk(cls, val : int):
        return cls.con().get_by_pk(cls.table_name, cls.pk, str(val))
    
    @classmethod
    def get_last_pk(cls):
        return cls.con().get_last_pk(cls.table_name, cls.pk)
    
    # DELETE
    @classmethod
    def delete_by_pk(cls, val) -> bool:
        return cls.con().delete_by_pk(cls.table_name, cls.pk, str(val))
    
    @classmethod
    def delete_all(cls) -> bool:
        return cls.con().delete_all(cls.table_name)
    
    @classmethod
    def delete_table(cls) -> bool:
        return cls.con().delete_table(cls.table_name)
    
    # ADD DATA
    @classmethod
    def add_data(cls, data : dict) -> bool:
        return cls.con().add_data(cls.table_name, data)
        # return 'test'
    
    # UPDATE DATA
    @classmethod
    def update_data(cls, val : int, data : dict) -> bool:
        return cls.con().update_data(cls.table_name, cls.pk, str(val), data)
    
    # CREATE TABLE
    @classmethod
    def create_table(cls) -> bool:
        return cls.con().create_table(cls.table_name, cls.table_schema)