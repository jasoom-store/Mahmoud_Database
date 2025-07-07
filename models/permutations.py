from abstract.model import Model
from config import config

class Permutations(Model):
    table_name = config.hix + 'permutations'
    pk = 'per_id'
    table_schema = {
        'per_id': {
            'type': Model.con().types['int'],
            'ln': 8,
            'ai': True,
            'pk': True,
        },
        'per_name' : {
            'type': Model.con().types['str'],
            'ln': 50,
        },
    }

    @classmethod
    def get_permutation_id(cls, permutation : str):
        data = cls.con().db_get_all(cls.table_name, f'`per_name` = "{ permutation }"', 1)
        if data:
            return data[0][cls.pk]
        return False