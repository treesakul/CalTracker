from Account import *
from Profile import *
from Goal import *
from pony.orm import *
import time

db = Database()
db.bind('oracle', 'TANAKORN/password@127.0.01')

class Report(db.Entity):
    user_id = Required(int)
    report_date = Required(str)
    food_cal = Required(float)
    exercise_cal = Required(float)
    sum_cal = Required(float)

db.generate_mapping(create_tables=True)

def add_report(i,r,f,x,re):
    with db_session:
        Report(user_id = i, report_date = r, food_cal = f, exercise_cal = x, sum_cal = re)
    
