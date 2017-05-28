from pony.orm import *
from datetime import *
from Account import *
db = Database()
db.bind('oracle', 'TANAKORN/password@127.0.01')

class User(db.Entity):
    id = PrimaryKey(int)
    fname = Required(str)
    lname = Required(str)
##    birthday = Required(date)
    pic = Optional(str)
    
db.generate_mapping(create_tables= True)

@db_session
def add_user(iden, fname, lname):
    User(id = iden, fname = fname, lname = lname)

