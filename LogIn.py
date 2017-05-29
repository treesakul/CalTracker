from Account import *
from Profile import *
from Goal import *
from pony.orm import *
db = Database()
db.bind('oracle', 'TANAKORN/password@127.0.01')

class LoginSystem:
    def __init__(self):
        self.account = None
        
    def check(self, username, pswd):
        with db_session:
            x = Account.select_by_sql(
                "SELECT * FROM Account WHERE username =\'" + username+"\'" )
            for i in range(len(x)):
                if (x != None and x[i].password == pswd):
                    self.account = x[i]
                    return True
                else:
                    return False

    def getId(self):
        if(self.account != None):
            return self.account.id
        
    def signup(self, user, pasw, fname, lname, bd):
        with db_session:
            add_account(user, pasw)
            x = Account.select_by_sql(
                "SELECT * FROM Account WHERE username =\'" + user +"\' AND password =\'" + pasw +"\'")
            add_profile(x[0].id,fname,lname,bd)
