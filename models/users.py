# import random
from abstract.model import Model
from config import config

from models.status import Status

class Users(Model):
    table_name = config.hix + 'users'
    pk = 'usr_id'
    table_schema = {
        'usr_id': {
            'type': Model.con().types['int'],
            'ln': 8,
            'ai': True,
            'pk': True,
        },
        'usr_email' : {
            'type': Model.con().types['str'],
            'ln': 150,
            'un': True,
        },
        'usr_password' : {
            'type': Model.con().types['str'],
            'ln': 150,
        },
        'usr_otp' : {
            'type': Model.con().types['char'],
            'ln': 6,
            # 'df': random.randrange(100000, 999999),
        },
        'usr_active' : {
            'type': Model.con().types['bool'],
            'ln': 1,
            'df': False,
        },
        Status.pk: {
            'type': Status.table_schema[Status.pk]['type'],
            'ln': Status.table_schema[Status.pk]['ln'],
            'fk': Status.table_name,
        }
    }