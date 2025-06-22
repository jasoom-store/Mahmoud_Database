from abstract.model import Model
from config import config

class Users(Model):
    table_name = config.table_hix +'users'
    pk = 'user_id'
    table_schema = {
        'user_id': {
            'type': Model.con().types['int'],
            'ln': 6,
            'ai': True,
            'pk': True,
        },
        'username': {
            'type': Model.con().types['str'],
            'ln': 50
        }
    }
