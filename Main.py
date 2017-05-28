from Account import *
from Profile import *
from LogIn import *
from pony.orm import *
db = Database()
db.bind('oracle', 'TANAKORN/password@127.0.01')

class Main:
    def __init__(self):
        self.current = None
        self.a = LoginSystem()

    def setAcc(self,x,y):
        self.a.check(x,y)       # become the account that logged in
        theAcc = self.a.account.id
        with db_session:
            find = Profile.select_by_sql(
                "SELECT * FROM Profile WHERE id = $theAcc")
        print(find)

    def getAcc(self):
        print(self.current)

##with db_session:
##    n = Profile.select_by_sql("SELECT * FROM Profile")
##print(n[0])

with db_session:
    find = Profile.select_by_sql("SELECT * FROM Profile WHERE id = 12")

print(find)
