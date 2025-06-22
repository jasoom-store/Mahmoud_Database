from models.users import Users
from models.posts import Posts

print("Delete Posts Table: "+ str(Posts.delete_table()))
print("Delete Users Table: "+ str(Users.delete_table()))

print("Create Users Table: "+ str(Users.create_table()))
print("Create Posts Table: "+ str(Posts.create_table()))
