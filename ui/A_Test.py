from Food import *
from pony.orm import *
db = Database()
db.bind('oracle', 'TANAKORN/password@127.0.01')

class Test:
    def __init__(self):
        pass
    def pic(self, f_id):
        with db_session:
            selected = Food.select_by_sql(
                "SELECT pic FROM Food WHERE id =\'" + str(f_id) + "\'")
        return selected.pic
