from pony.orm import *
from User import *
db = Database()
db.bind('oracle', 'TANAKORN/password@127.0.01')

class Account(db.Entity):
    id = PrimaryKey(int, auto=True)
    username = Required(str, unique= True)
    password = Required(str)
##    pic = Optional(str)
         
db.generate_mapping(create_tables= True)

@db_session
def add_account(u,p):
    Account(username= u, password = p)

@db_session
def remove_account(a_id):
    Account[a_id].delete()
           

