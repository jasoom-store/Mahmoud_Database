from config import config

from models.permutations import Permutations
from models.status import Status
from models.per_p_state import PermutationsPerState
from models.users import Users

status = Status.table_name[len(config.hix):]
users = Users.table_name[len(config.hix):]
permutations = Permutations.table_name[len(config.hix):]
permutations_per_state = PermutationsPerState.table_name[len(config.hix):]

n = 10
print(" ")
print(f">{ '-' * n }[ Delete ]{ '-' * n }<")
print(f"Delete table `{ permutations_per_state }`: "+ str(PermutationsPerState.delete_table()))
print(f"Delete table `{ permutations }`: "+ str(Permutations.delete_table()))
print(f"Delete table `{ users }`: "+ str(Users.delete_table()))
print(f"Delete table `{ status }`: "+ str(Status.delete_table()))

print(" ")
print(f">{ '-' * n }[ Create ]{ '-' * n }<")
print(f"Create table `{ status }`: "+ str(Status.create_table()))
print(f"Create table `{ permutations }`: "+ str(Permutations.create_table()))
print(f"Create table `{ permutations_per_state }`: "+ str(PermutationsPerState.create_table()))
print(f"Create table `{ users }`: "+ str(Users.create_table()))

print(" ")
print(f">{ '-' * n }[ Add Data ]{ '-' * n }<")

add = [] 
for state in ['User', 'Admin', 'Developer', 'Banned']:
    add.append(str(Status.add_data({
        'sts_name': state,
    })))

print(f"Add data to `{ status }`: "+ ", ".join(add))

add = [] 
for permutation in ['Login', 'Dashboard', 'Setting']:
    add.append(str(Permutations.add_data({
        'per_name': permutation,
    })))

print(f"Add data to `{ permutations }`: "+ ", ".join(add))

add = []
add.append(str(PermutationsPerState.add_data({
    Permutations.pk: Permutations.get_permutation_id('Login'),
    Status.pk: Status.get_state_id('User'),
})))

add.append(str(PermutationsPerState.add_data({
    Permutations.pk: Permutations.get_permutation_id('Login'),
    Status.pk: Status.get_state_id('Admin'),
})))

add.append(str(PermutationsPerState.add_data({
    Permutations.pk: Permutations.get_permutation_id('Login'),
    Status.pk: Status.get_state_id('Developer'),
})))

add.append(str(PermutationsPerState.add_data({
    Permutations.pk: Permutations.get_permutation_id('Dashboard'),
    Status.pk: Status.get_state_id('Admin'),
})))

add.append(str(PermutationsPerState.add_data({
    Permutations.pk: Permutations.get_permutation_id('Dashboard'),
    Status.pk: Status.get_state_id('Developer'),
})))

add.append(str(PermutationsPerState.add_data({
    Permutations.pk: Permutations.get_permutation_id('Setting'),
    Status.pk: Status.get_state_id('Developer'),
})))

print(f"Add data to `{ permutations_per_state }`: "+ ", ".join(add))

import random

add = []
add.append(str(Users.add_data({
    'usr_email': 'admin@jasoom.dev',
    'usr_password': '12345678',
    'usr_otp': random.randrange(100000, 999999),
    'usr_active': True,
    Status.pk: Status.get_state_id('Developer'),
})))

add.append(str(Users.add_data({
    'usr_email': 'user@jasoom.dev',
    'usr_password': '12345678',
    'usr_otp': random.randrange(100000, 999999),
    'usr_active': True,
    Status.pk: Status.get_state_id('User'),
})))

add.append(str(Users.add_data({
    'usr_email': 'ban@jasoom.dev',
    'usr_password': '12345678',
    'usr_otp': random.randrange(100000, 999999),
    'usr_active': True,
    Status.pk: Status.get_state_id('Banned'),
})))

add.append(str(Users.add_data({
    'usr_email': 'not_active@jasoom.dev',
    'usr_password': '12345678',
    'usr_otp': random.randrange(100000, 999999),
    'usr_active': False,
    Status.pk: Status.get_state_id('User'),
})))

print(f"Add data to `{ users }`: "+ ", ".join(add))
