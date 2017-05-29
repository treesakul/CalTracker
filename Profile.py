from Account import *
from Goal import *
from pony.orm import *
db = Database()
db.bind('oracle', 'TANAKORN/password@127.0.01')

class Profile(db.Entity):
    id = PrimaryKey(int)
    fname = Required(str)
    lname = Required(str)
    gender = Required(str)
    birthday = Required(str)
    pic = Optional(str)

    def edit_profile(self,iden,fname,lname,bd,pic):
        with db_session:
            Profile[iden].fname = fname
            Profile[iden].lname = lname
##            Profile[iden].weight = wei
##            Profile[iden].height = hei
            Profile[iden].birthday = bd
            Profile[iden].pic = pic
##            Account[iden].username = user
##            Account[iden].password = pasw
    
db.generate_mapping(create_tables= True)

@db_session
def add_profile(iden, fname, lname, gen, bd):
    Profile(id = iden, fname = fname, lname = lname, gender = gen, birthday = bd)

@db_session
def get():
    pass

