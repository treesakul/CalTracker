from pony.orm import *
from datetime import *
from Account import *
db = Database()
db.bind('oracle', 'TANAKORN/password@127.0.01')

class Profile(db.Entity):
    id = PrimaryKey(int)
    fname = Required(str)
    lname = Required(str)
##    birthday = Required(date)
    pic = Optional(str)
    
db.generate_mapping(create_tables= True)

@db_session
def add_profile(iden, fname, lname):
    Profile(id = iden, fname = fname, lname = lname)

@db_session
def edit_profile(fname,lname,user,pasw,wei,hei):
    pass

@db_session
def get():
    pass

