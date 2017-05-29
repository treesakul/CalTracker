from pony.orm import *
db = Database()
db.bind('oracle', 'TANAKORN/password@127.0.0.1')

class Food(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    calorie = Required(int)
    description = Optional(str)
    pic = Optional(str)

db.generate_mapping(create_tables=True)

@db_session
def print_food(f_id):
    f = Food[f_id]
    print(f.name)

@db_session
def search(name):
    f = Food.select_by_sql("SELECT * FROM Food")
    lis = []
    for i in range(len(f)):
        if name in f[i].name:
            lis.append(f[i])
    return lis

@db_session
def add_food( n, a, p= "", des = ""):
    Food(name = n,calorie= a, pic = p)

@db_session
def remove_food(f_id):
    Food[f_id].delete()

@db_session
def get_pic(f_id):
    path = Food[f_id].pic
    return path

