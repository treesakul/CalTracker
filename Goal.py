from Account import *
from Profile import *
from pony.orm import *
db = Database()
db.bind('oracle', 'TANAKORN/password@127.0.01')

class Goal(db.Entity):
    id = PrimaryKey(int)
    height = Required(int)
    start_weight = Required(int)
    current_weight = Required(int)
    goal_weight = Required(int)
    amount = Required(float)   # kg per week (can be negative)
    
    def edit_goal(self, iden, hei, start, cur, goal, a):
        with db_session:
            Goal[iden].height = hei
            Goal[iden].start_weight = start
            Goal[iden].current_weight = cur
            Goal[iden].goal_weight = goal
            Goal[iden].amount = a

db.generate_mapping(create_tables= True)

@db_session
def add_goal(iden, hei, start, cur, goal, a):
    Goal(id=iden, height=hei, start_weight=start, current_weight=cur,
         goal_weight=goal, amount=a)
