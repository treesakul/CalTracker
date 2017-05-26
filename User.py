from pony.orm import *
from Date import * 
db = Database()
db.bind('oracle', 'TREESAKUL/123159@127.0.01')

class User(db.Entity):
    id = PrimaryKey(int, auto=True)
    fname = Required(str)
    lname = Required(str)
    birthday = Required(date)
    pic = Optional(str)
    
    def generate_mapping():
        db.generate_mapping(create_tables= True)

@db_session
def add_user(u,p):
    Account(username= u, password = p)
    
Account.generate_mapping()
