from database.db import DB

from database.sqlite_db import SQLite_DB
from database.mysql_db import MYSQL_DB

# print(DB.run({
#     'type': 'MYSQL',
#     'host': 'localhost',
#     'user': 'root',
#     'pass': '',
#     'name': 'test'
# }))

# print(DB.run({
#     'type': 'SQLITE',
#     'path': 'sqlite/main.db'
# }))
print(" ")
print("=" * 30)
print(" ")

# db1 = SQLite_DB('sqlite/main.db')
# db2 = SQLite_DB('sqlite/main.db')
# db3 = SQLite_DB('sqlite/main.db')
# db4 = SQLite_DB('sqlite/main.db')

db1 = MYSQL_DB({
    'host': 'localhost',
    'user': 'root',
    'pass': '',
    'name': 'test'
})

db2 = MYSQL_DB({
    'host': 'localhost',
    'user': 'root',
    'pass': '',
    'name': 'test'
})

db3 = MYSQL_DB({
    'host': 'localhost',
    'user': 'root',
    'pass': '',
    'name': 'test'
})

db4 = MYSQL_DB({
    'host': 'localhost',
    'user': 'root',
    'pass': '',
    'name': 'test'
})

print(db1 is db2 is db3 is db4)
print(" ")

print(db1)
print(" ")
print(db2)
print(" ")
print(db3)
print(" ")
print(db4)

# class Dog:
#     name = ''
#     age = 0

#     def __new__(cls):
#         if not hasattr(cls, 'instance'):
#             cls.instance = super(Dog, cls).__new__(cls)
#         return cls.instance

# dog1 = Dog()
# dog1.name = 'roby'
# dog1.age = 2

# dog2 = Dog()
# dog2.name = 'hshs'
# dog2.age = 4

# print(dog1)
# print(dog1.name)
# print(dog1.age)
# print(" ")
# print(dog2)
# print(dog2.name)
# print(dog2.age)

print(" ")
print("=" * 30)
