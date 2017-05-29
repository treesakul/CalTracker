from pony.orm import *
from Account import *
from Profile import *
db = Database()
db.bind('oracle', 'TANAKORN/password@127.0.01')

class Goal(db.Entity):
    id = PrimaryKey(int)
    height = Required(int)
    start_weight = Required(int)
    current_weight = Required(int)
    goal_weight = Required(int)
    duration = Required(int)   # kg per week (can be negative)

db.generate_mapping(create_tables= True)

@db_session
def set_goal(iden, hei, start_wei, cur_wei, g_wei, d):  # iden come from Profile
    Goal(id = iden, height = hei, start_weight = start_wei,
         current_weight = cur_wei, goal_weight = g_wei, duration = d)
