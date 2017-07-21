from Account import *
from pony.orm import *
from FoodRecord import *
from ExerciseRecord import *
from Food import *
from Exercise import *
from FoodRecord import *
from ExerciseRecord import *
from LogIn import *
import time
from datetime import date
db = Database()
db.bind('oracle', 'TREESAKUL/123159@127.0.01')

class PersonalSystem:
    def __init__(self):
         self.user = None

    def set_user(self,user):
        self.user = user
        
    def show_food(self):
        with db_session:
            x = Food.select_by_sql("SELECT * FROM Food" )
        return x

    def show_exercise(self):
        with db_session:
            x = Exercise.select_by_sql("SELECT * FROM Exercise")
        return x

    @db_session
    def add_food( self,n, a, p= "", des = ""):
        Food(name = n,calorie= a, pic = p)

    @db_session
    def remove_food(self,f_id):
        Food[f_id].delete()

    def add_personal_food(self, food,quantity):
        with db_session:
            x = FoodRecord(user_id=self.user.id,food_id =food.id, food_amnt = quantity, c_date= time.strftime("%x"))

    def add_personal_exercise(self, exercise,am):
        with db_session:
            x = ExerciseRecord(user_id=self.user.id,exercise_id = exercise.id, exercise_amnt = am, c_date= time.strftime("%x"))

    def show_personal_food(self):
        with db_session:
            x = FoodRecord.select_by_sql("SELECT * FROM FoodRecord WHERE user_id="+str(self.user.id)+" and c_date = \'"+str(time.strftime("%x"))+"\'")
            return x
        
    def show_personal_exercise(self):
        with db_session:
            x = ExerciseRecord.select_by_sql("SELECT * FROM ExerciseRecord WHERE user_id="+str(self.user.id)+" and c_date = \'"+str(time.strftime("%x"))+"\'")
            return x
        
    def get_user(self):
        return self.user

    @db_session
    def search_food_by_id(self,f_id):
        sql = "SELECT * FROM Food WHERE id = " +str(f_id)
        f = Food.select_by_sql(sql)
        if(f != None):
            return f[0].name
        else:
            return None

    @db_session
    def search_exercise_by_id(self,e_id):
        sql = "SELECT * FROM Exercise WHERE id = " +str(e_id)
        f = Exercise.select_by_sql(sql)
        if(f != None):
            return f[0].name
        else:

            return None

    @db_session
    def search_food(self,name):
        f = Food.select_by_sql("SELECT * FROM Food WHERE name = \'"+name+"\'")
        if(f != None):
            return f[0]
        else:
            return None

    @db_session
    def search_exercise(self,name):
        e = Exercise.select_by_sql("SELECT * FROM Exercise WHERE name = \'"+name+"\'")
        if(e != None):
            return e[0]
        else:

            return None
