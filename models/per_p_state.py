from abstract.model import Model
from config import config

from models.permutations import Permutations
from models.status import Status

class PermutationsPerState(Model):
    table_name = config.hix + 'permutations_per_state'
    pk = 'per_state_id'
    table_schema = {
        'per_state_id': {
            'type': Model.con().types['int'],
            'ln': 8,
            'ai': True,
            'pk': True,
        },
        Permutations.pk: {
            'type': Permutations.table_schema[Permutations.pk]['type'],
            'ln': Permutations.table_schema[Permutations.pk]['ln'],
            'fk': Permutations.table_name,
        },
        Status.pk: {
            'type': Status.table_schema[Status.pk]['type'],
            'ln': Status.table_schema[Status.pk]['ln'],
            'fk': Status.table_name,
        }
    }
