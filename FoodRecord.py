from pony.orm import *
db = Database()
db.bind('oracle', 'TANAKORN/password@127.0.0.1')

class FoodRecord(db.Entity):
    user_id = Required(int)
    food_id = Required(int)
    food_amnt = Required(int)
    c_date = Required(str)
    


db.generate_mapping(create_tables=True)    

