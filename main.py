from database.db import DB

from database.sqlite_db import SQLite_DB
from database.mysql_db import MYSQL_DB

print(" ")
print("=" * 30)
print(" ")

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

print(db)

print(db.get_all('about'))


print(" ")
print("=" * 30)
