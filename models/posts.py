from abstract.model import Model
from config import config

from models.users import Users

class Posts(Model):
    table_name = config.table_hix +'posts'
    pk = 'post_id'
    table_schema = {
        'post_id': {
            'type': Model.con().types['int'],
            'ln': 8,
            'ai': True,
            'pk': True,
        },
        'title': {
            'type': Model.con().types['str'],
            'ln': 50
        },
        Users.pk: {
            'type': Users.table_schema[Users.pk]['type'],
            'ln': Users.table_schema[Users.pk]['ln'],
            'fk': Users.table_name
        }
    }
