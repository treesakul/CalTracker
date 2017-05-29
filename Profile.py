from pony.orm import *
from Account import *
db = Database()
db.bind('oracle', 'TANAKORN/password@127.0.01')

class Profile(db.Entity):
    id = PrimaryKey(int)
    fname = Required(str)
    lname = Required(str)
    weight = Required(int)
    height = Required(int)
    birthday = Required(str)
    goal = Required(int)
    pic = Optional(str)
    
db.generate_mapping(create_tables= True)

@db_session
def add_profile(iden, fname, lname):
    Profile(id = iden, fname = fname, lname = lname)

@db_session
def edit_profile(iden,fname,lname,user,pasw,wei,hei,bd,pic):
    Profile[iden].fname = fname
    Profile[iden].lname = lname
    Profile[iden].weight = wei
    Profile[iden].height = hei
    Profile[iden].birthday = bd
    Profile[iden].pic = pic
    Account[iden].username = user
    Account[iden].password = pasw

@db_session
def get():
    pass
