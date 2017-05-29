from pony.orm import *
db = Database()
db.bind('oracle', 'TREESAKUL/123159@127.0.0.1')

class FoodRecord(db.Entity):
    user_id = Required(int)
    food_id = Required(int)
    c_date = Required(str)
    


db.generate_mapping(create_tables=True)    

