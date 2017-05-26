from pony.orm import *
db = Database()
db.bind('oracle', 'TREESAKUL/123159@127.0.0.1')

class Food(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str, unique = True)
    calorie = Required(int)
    description = Optional(str)
    pic = Optional(str)
    
    def generate_mapping():
        db.generate_mapping(create_tables=True)

@db_session
def add_food( n,a, des = "", p= ""):
    Food(name = n,calorie= a, description=  des, pic = pic)

Food.generate_mapping()
