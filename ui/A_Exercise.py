from pony.orm import *
db = Database()
db.bind('oracle', 'TANAKORN/password@127.0.0.1')

class Exercise(db.Entity):
    id =  PrimaryKey(int, auto= True)
    name = Required(str, unique= True)
    calorie = Required(int)

##    def generate_mapping():
##        db.generate_mapping(create_tables= True)

db.generate_mapping(create_tables= True)

@db_session
def add_exercise(n,a, des= "", p = ""):
    Exercise(name = n, calorie= a, description=des, pic= p )

@db_session
def remove_exercise(e_id):
    Exercise[e_id].delete()

@db_session
def print_exercise(e_id):
    e = Exercise[e_id]
    print(e.name)

@db_session
def search(name):
    e = Exercise.select_by_sql("SELECT * FROM Exercise")
    lis = []
    for i in range(len(e)):
        if name in e[i].name:
            lis.append(e[i])
    return lis

@db_session
def get_pic(e_id):
    path = Exercise[e_id].pic
    return path

##Exercise.generate_mapping()
