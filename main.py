from database.db import DB

print(DB.run({
    'type': 'MYSQL',
    'host': 'localhost',
    'user': 'root',
    'pass': '',
    'name': 'test'
}))

print(DB.run({
    'type': 'SQLITE',
    'path': 'sqlite/main.db'
}))

