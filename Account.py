from pony.orm import *
from Profile import *
from Goal import *
from pony.orm import *
db = Database()
db.bind('oracle', 'TANAKORN/password@127.0.01')

class Account(db.Entity):
    id = PrimaryKey(int, auto=True)
    username = Required(str, unique= True)
    password = Required(str)

    def edit_account(self,iden,user,pasw):
        with db_session:
            Account[iden].username = user
            Account[iden].password = pasw
         
db.generate_mapping(create_tables= True)

@db_session
def add_account(u,p):
    Account(username= u, password = p)

@db_session
def remove_account(a_id):
    Account[a_id].delete()

