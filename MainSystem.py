from Account import *
from pony.orm import *
from FoodRecord import *
from ExerciseRecord import *
from Food import *
from Exercise import *
from System import *
import time
db = Database()
db.bind('oracle', 'TREESAKUL/123159@127.0.01')

class MainSystem:
    def __init__(self, user):
         self.user = user
        
    def show_food(self):
        with db_session:
            x = Food.select_by_sql("SELECT * FROM Food" )
        return x

    def show_exercise(self):
        with db_session:
            x = Exercise.select_by_sql("SELECT * FROM Exercise")
        return x

    def add_food(self, food):
        with db_session:
            x = FoodRecord(user_id=self.user.id,food_id =food.id, c_date= time.strftime("%x"))

    def add_exercise(self, exercise):
        with db_session:
            x = ExerciseRecord(user_id=self.user.id,exercise_id =exercise.id, c_date= time.strftime("%x"))

    def show_personal_food(self):
        with db_session:
            x = FoodRecord.select_by_sql("SELECT * FROM FoodRecord WHERE user_id="+str(self.user.id)+" and c_date = \'"+str(time.strftime("%x"))+"\'")
            return x
    def show_personal_exercise(self):
        with db_session:
            x = ExerciseRecord.select_by_sql("SELECT * FROM ExerciseRecord WHERE user_id="+str(self.user.id)+" and c_date = \'"+str(time.strftime("%x"))+"\'")
            return x

a = LoginSystem()
k = a.check('treesakul','1234')      
a = MainSystem(k)
a.show_food()
a.show_exercise()
l = search_food("Ham")
a.add_food(l)
'''
a.show_personal_food()
'''
