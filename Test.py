from Food import *
from pony.orm import *
db = Database()
db.bind('oracle', 'TANAKORN/password@127.0.01')

class Test:
    def pic(self):
        a = "rice"
        with db_session:
            selected = Food.select_by_sql("SELECT * FROM Food WHERE name = $a")
        return selected[0].name
