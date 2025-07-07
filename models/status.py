from abstract.model import Model
from config import config

class Status(Model):
    table_name = config.hix + 'status'
    pk = 'sts_id'
    table_schema = {
        'sts_id': {
            'type': Model.con().types['int'],
            'ln': 8,
            'ai': True,
            'pk': True,
        },
        'sts_name' : {
            'type': Model.con().types['str'],
            'ln': 50,
        },
    }

    @classmethod
    def get_state_id(cls, state : str):
        data = cls.con().db_get_all(cls.table_name, f'`sts_name` = "{ state }"', 1)
        if data:
            return data[0][cls.pk]
        return False