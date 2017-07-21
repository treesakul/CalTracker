from Account import *
from pony.orm import *
db = Database()
db.bind('oracle', 'TREESAKUL/123159@127.0.01')

class LoginSystem:
    def __init(self):
        pass
    def check(self, username, pswd):
        with db_session:
            x = Account.select_by_sql("SELECT * FROM Account WHERE username =\'" + username+"\'" )
            if (x != None and x[0].password == pswd):
                print("Successful")
                return True
            else:
                print("error")
                return False

#a = LoginSystem()
#a.check('treesakul','1234')
