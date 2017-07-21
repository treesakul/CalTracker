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
db.bind('oracle', 'TANAKORN/password@127.0.01')

class MainSystem:
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
        Food(name = n,calorie= a, description = des, pic = p)

    @db_session
    def remove_food(self,f_id):
        Food[f_id].delete()

    @db_session
    def get_food_pic(self,f_id):
        path = Food[f_id].pic
        return path

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
        return self.user.name

    def get_exercise_record(self):
        with db_session:
            sql = "SELECT * FROM ExerciseRecord WHERE user_id="+str(self.user.id)
            x = ExerciseRecord.select_by_sql(sql)
            return x

    def get_food_record(self):
        with db_session:
            sql = "SELECT * FROM FoodRecord WHERE user_id="+str(self.user.id)
            x = FoodRecord.select_by_sql(sql)
            return x
    
    @db_session
    def search_food(self,name):
        f = Food.select_by_sql("SELECT * FROM Food WHERE name = \'"+name+"\'")
        if(f != None):
            return f[0]
        else:
            return None

    @db_session
    def search_food_by_id(self,f_id):
        sql = "SELECT * FROM Food WHERE id = " +str(f_id)
        f = Food.select_by_sql(sql)
        if(f != None):
            return f[0]
        else:

            return None

    @db_session
    def search_exercise_by_id(self,e_id):
        sql = "SELECT * FROM Exercise WHERE id = " +str(e_id)
        f = Exercise.select_by_sql(sql)
        if(f != None):
            return f[0]
        else:
            return None

    @db_session
    def add_exercise(self,n,a, des= "", p = ""):
        Exercise(name = n, calorie= a, description=des, pic= p )

    @db_session
    def remove_exercise(self, e_id):
        Exercise[e_id].delete()

    @db_session
    def search_exercise(self,name):
        e = Exercise.select_by_sql("SELECT * FROM Exercise WHERE name = \'"+name+"\'")
        if(e != None):
            return e[0]
        else:

            return None

    @db_session
    def get_food_pic(e_id):
        path = Exercise[e_id].pic
        return path

    def get_total_food(self):
        with db_session:
            sql = "SELECT * FROM FoodRecord WHERE c_date =\'"+ str(time.strftime("%x")+"\' AND user_id = "+str(self.user.id) )

            total = FoodRecord.select_by_sql(sql)

        s = 0
        for i in total:
            f_id = i.food_id
            current_food = self.search_food_by_id(f_id)
            s += ((current_food.calorie)*i.food_amnt)
        return s

    def get_total_exercise(self):
        with db_session:
            sql = "SELECT * FROM ExerciseRecord WHERE c_date =\'"+ str(time.strftime("%x")+"\' AND user_id = "+str(self.user.id))
            total = ExerciseRecord.select_by_sql(sql)
        s = 0
        for i in total:
            e_id = i.exercise_id
            current_exercise = self.search_exercise_by_id(e_id)
            s += ((current_exercise.calorie)*i.exercise_amnt)
        return s

    def get_total_exercise_by_date(self,date):
        with db_session:
            sql = "SELECT * FROM ExerciseRecord WHERE c_date =\'"+date+"\'"
            total = ExerciseRecord.select_by_sql(sql)
        s = 0
        if(total != None):
            for i in total:
                e_id = i.exercise_id
                current_exercise = self.search_exercise_by_id(e_id)
                s += ((current_exercise.calorie)*i.exercise_amnt)
        return s

    def get_total_food_by_date(self,date):
        with db_session:
            sql = "SELECT * FROM FoodRecord WHERE c_date =\'"+ date+"\'"
            total = FoodRecord.select_by_sql(sql)

        s = 0
        if(total != None):
            for i in total:
                f_id = i.food_id
                current_food = self.search_food_by_id(f_id)
                s += ((current_food.calorie)*i.food_amnt)
        return s
    
    def get_total_exercise_list(self, date):
        with db_session:
            sql = "SELECT * FROM ExerciseRecord WHERE c_date ="+ date
            total = ExerciseRecord.select_by_sql(sql)
        return total

    def get_total_food_list(self, date):
        with db_session:
            sql = "SELECT * FROM ExerciseRecord WHERE c_date =\'"+ date+"\'"
            total = FoodRecord.select_by_sql(sql)
        return total


    def get_total_net(self):
        return (self.get_total_food() - self.get_total_exercise())

    def get_age(self):
        today = date.today()
        d = self.user.birthday.split('/')
        age = today.year - int(d[2]) - ((today.month, today.day)<(int(d[1]),int(d[0])))
        return age

    def get_fname(self):
        return self.user.fname
    
    def get_lname(self):
        return self.user.lname

    def get_pic(self):
        return self.user.pic

    def get_bmi(self):
        bmi = 0
        with db_session:
            sql = "SELECT * FROM Goal WHERE id ="+ str(self.user.id)
            goal = Goal.select_by_sql(sql)
        if(goal != None):
            goal = goal[0]
            bmi = ((goal.current_weight/goal.height)/goal.height)*10000
            #bmi = ((self.user.current_weight/self.user.height)/self.user.height)
        return bmi

    def get_gender(self):
        return self.user.gender
    
    def get_birthday(self):
        return self.user.birthday

    def get_user_state(self):
        bmi = self.get_bmi()
        state = ""
        if(bmi < 18):
            state = "underweight"
        elif(bmi>25):
            state = "overweight"
        else:
            state = "normal weight"
        return state
    def get_goal_need(self):
        with db_session:
            sql = "SELECT * FROM Goal WHERE id ="+ str(self.user.id)
            goal = Goal.select_by_sql(sql)
        if(goal != None):
            goal = goal[0]
        return goal

    def height(self):
        height = self.get_goal_need().height
        return height
    
    def start_weight(self):
        start_weight = self.get_goal_need().start_weight
        return start_weight
    
    def current_weight(self):
        current_weight = self.get_goal_need().current_weight
        return current_weight
    
    def get_goal(self):
        bmr = 0
        with db_session:
            sql = "SELECT * FROM Goal WHERE id ="+ str(self.user.id)
            goal = Goal.select_by_sql(sql)
        if(goal != None):
            goal = goal[0]
           
            age = self.get_age()
            if (self.user.gender == "male"):
                bmr = (10*goal.current_weight)+(6.25*goal.height)-(5*age)+5
            elif (self.user.gender == "female"):
                bmr = (10*goal.current_weight)+(6.25*goal.height)-(5*age)-161
        return bmr

