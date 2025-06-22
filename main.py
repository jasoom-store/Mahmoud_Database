from database.db import DB

from database.sqlite_db import SQLite_DB
from database.mysql_db import MYSQL_DB

print(" ")
print("=" * 30)
print(" ")

# select which kind of database I will use
db = DB.run({
    'type': 'MYSQL',
    'host': 'localhost',
    'user': 'root',
    'pass': '',
    'name': 'test'
})

# db = DB.run({
#     'type': 'SQLITE',
#     'path': 'sqlite/main.db'
# })

# print(db)

# print(db.delete_all('users'))
# print(db.get_all('tt'))
# print(db.update_data('users', {
#     'username' : 'mmmmmmmmm',
#     'password' : 'mmmmmmmmmm',
# }, 'id', 3))
# print(db.update_data('tt', {
#     'name' : 'aliiiiiiiii',
# }, 'id', 3))
# print(db.add_data('tt', {
#     'name' : 'faccccccccttt',
# }))
print(db.get_last_pk('tt', 'id'))


print(" ")
print("=" * 30)
