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
        self.a.check(x,y)       # self.a become the account that logged in
        theAcc = self.a.account.id
        with db_session:
            find = Profile.select_by_sql(
                "SELECT * FROM Profile WHERE id = $theAcc")
        self.current = find[0]

    def getAcc(self):
        print(self.current)

##with db_session:
##    n = Profile.select_by_sql("SELECT * FROM Profile")
##print(n[0])

##x = 14
##with db_session:
##    find = Profile.select_by_sql("SELECT * FROM Profile WHERE id = $x")
##print(find)
