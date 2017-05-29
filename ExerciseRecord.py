from pony.orm import *
db = Database()
db.bind('oracle', 'TREESAKUL/123159@127.0.0.1')

class ExerciseRecord(db.Entity):
    user_id = Required(int)
    exercise_id = Required(int)
    c_date = Required(str)
    
    def __init__(self):
        pass


db.generate_mapping(create_tables=True)    


