from Account import *
from User import *
from pony.orm import *
db = Database()
db.bind('oracle', 'TANAKORN/password@127.0.01')

class LoginSystem:
    def __init__(self):
        pass
    def check(self, username, pswd):
        with db_session:
            x = Account.select_by_sql(
                "SELECT * FROM Account WHERE username =\'" + username+"\'" )
            for i in range(len(x)):
                if (x != None and x[i].password == pswd):
                    return True
##                    user = User.select_by_sql(
##                        "SELECT *FROM User WHERE 
                else:
                    return False

    def signup(self, user, pasw, fname, lname):
        with db_session:
            add_account(user, pasw)
            x = Account.select_by_sql(
                "SELECT * FROM Account WHERE username =\'" + user +"\' AND password =\'" + pasw +"\'")
            add_user(x[0].id,fname,lname)
