from pony.orm import *
db = Database()
db.bind('oracle', 'TREESAKUL/123159@127.0.01')

class Account(db.Entity):
    id = PrimaryKey(int, auto=True)
    username = Required(str, unique= True)
    password = Required(str)
    pic = Optional(str)
    
    def generate_mapping():
        db.generate_mapping(create_tables= True)

    def test(self):
        print("test")

@db_session
def add_account(u,p):
    Account(username= u, password = p)
    
Account.generate_mapping()
'''
with db_session:
        x = Account.select_by_sql("SELECT * FROM Account WHERE username =" + username )
'''
           

