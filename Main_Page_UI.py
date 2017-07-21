import sys

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *


from SGraph import *
from Goal import *
from MainSystem import *
from Dia_add_food import *
from Dia_add_exercise import *
from Edit_Profile_Page_UI import *

class Main_Page_UI(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, None)
        self.parent = parent
        self.user = None
        self.system = MainSystem()
        self.mainPageInit()
        self.set_user()
        self.list = None
        self.pic = ""
        self.in_stylesheet = ""

    def set_user(self):
        self.system.set_user(self.parent.getUser())
        self.user = self.parent.getUser()
        
    def mainPageInit(self):
        loader = QUiLoader()
        form = loader.load("UIDesigner/MainPageUI.ui", None)
        self.setCentralWidget(form)
        self.set_user()
        #if self.sender() == "Edit_Profile_Page_UI":
            #print("from edit pro")

        # set QPushButton
        self.Main_profile_bt = form.findChild(QPushButton, "Main_profile_bt")
        self.Main_food_bt = form.findChild(QPushButton, "Main_food_bt")
        self.Main_ex_bt = form.findChild(QPushButton, "Main_ex_bt")
        self.Main_sum_bt = form.findChild(QPushButton, "Main_sum_bt")
        self.Main_food_add_bt = form.findChild(QPushButton, "Main_food_add_bt")
        self.Main_ex_add_bt = form.findChild(QPushButton, "Main_ex_add_bt")
        self.Main_goal_bt = form.findChild(QPushButton, "Main_goal_bt")
        self.Main_logout = form.findChild(QPushButton, "Main_logout")

        
        
        # set QLabel
        self.Main_food_cal = form.findChild(QLabel, "Main_food_cal")
        self.Main_ex_cal = form.findChild(QLabel, "Main_ex_cal")
        self.Main_sum_cal = form.findChild(QLabel, "Main_sum_cal")
        self.Main_profile = form.findChild(QLabel, "Main_profile")

        #################################################
        # set QProgressBar
        self.progressBar_food = form.findChild(QProgressBar, "progressBar_food")




        #####################
        # connect QPushButton
        self.Main_profile_bt.clicked.connect(self.go_edit_profile)
        self.Main_food_bt.clicked.connect(self.go_food)
        self.Main_ex_bt.clicked.connect(self.go_exercise)
        self.Main_logout.clicked.connect(self.logout)

        # connect QPushButton dialog
        self.Main_food_add_bt.clicked.connect(self.go_dia_add_food)
        self.Main_ex_add_bt.clicked.connect(self.go_dia_add_exercise)
        self.Main_goal_bt.clicked.connect(self.go_goal)
        self.Main_sum_bt.clicked.connect(self.go_to_sum)

        self.set_progressbar()


    def set_pic_user(self):
        if self.pic is not None:
            self.Main_profile_bt.setText("")
            self.pic = self.system.user.pic
            self.in_stylesheet = "QPushButton {border-image: url("+str(self.pic)+") }"
            self.Main_profile_bt.setStyleSheet(self.in_stylesheet)

        else:
            self.Main_profile_bt.setText("")
            self.pic = self.system.user.pic
            self.in_stylesheet = "QPushButton {border-image: url("+str(self.pic)+") }"
            self.Main_profile_bt.setStyleSheet(self.in_stylesheet)
            


    '''def choose_pic(self):
        
        self.Main_profile_bt.setText("")
        #self.in_stylesheet = "QPushButton {border-image: url("+str(self.cur_pic)+") }"
        #self.EditPro_pic_bt.setStyleSheet(self.in_stylesheet)
        print(self.in_stylesheet)



        #filename = QFileDialog.getOpenFileName(self, 'Open File', '.')
        filename,type = QFileDialog.getOpenFileName(self, 'Open Image','./' , "Image files(*.png *.jpg *.bmp *.gif)")
        self.pic = filename
        self.in_stylesheet = "QPushButton {border-image: url("+str(self.pic)+") }"
        self.Main_profile_bt.setStyleSheet(self.in_stylesheet)

        print('Path file :', filename)

        #ready'''

    def set_progressbar(self):
        if(self.user != None):
            food_min = 0
            food_max = 100 #int(self.system.get_goal())
            food_value = int((self.system.get_total_net() / self.system.get_goal())*100)
            if(food_value<=0):
                food_value = 0
            elif(food_value>=100):
                food_value = 100

            
            
            self.progressBar_food.setMinimum(food_min)
            self.progressBar_food.setMaximum(food_max)
            self.progressBar_food.setValue(food_value)


  
        
    def set_Main_profile(self):
        fname = "     First name : "+str(self.system.get_fname())
        lname = "     Last name : "+str(self.system.get_lname())
        birthday = "     Birthday : "+str(self.system.get_birthday())
        gender = "     Gender : "+str(self.system.get_gender())
        start_weight = "     Start weight: "+str(self.system.start_weight())
        current_weight = "     Current weight : "+str(self.system.current_weight())
        height = "     Height : "+str(self.system.height())
        goal_weight = "     Goal weight : "+str(self.system.get_goal_need().goal_weight)
        bmi = "     Bmi : "+str("%0.2f"%self.system.get_bmi())
        status = "     State: "+str(self.system.get_user_state())

        text = fname +"\n"+lname + "\n"+ birthday + "\n" +gender+ "\n"+start_weight + "\n" +current_weight+ "\n" + height + "\n" +goal_weight+ "\n" + bmi+"\n"+status
        self.Main_profile.setText(text)

        
        
        

        
    def update(self):
        self.set_user()
        if(self.user != None):
            g = "goal = "+ str( self.system.get_goal())
            self.Main_goal_bt.setText(g)
            self.Main_food_cal.setText(str(self.system.get_total_food()))
            self.Main_ex_cal.setText(str(self.system.get_total_exercise()))
            self.Main_sum_cal.setText(str(self.system.get_total_net()))
            
            self.pic =self.system.user.pic
            self.set_pic_user()
            
            
            self.set_progressbar()
            self.set_Main_profile()
        
    def valuechange(self):
        size = self.sl.value()
        self.val_slide.setText(size)

    def go_edit_profile(self):
        self.parent.changePage("Edit_Profile_Page_UI")

    def go_goal(self):
        self.parent.changePage("Goal_Page_UI")

    def go_food(self):
        self.parent.changePage("Food_Page_UI")


    def go_exercise(self):
        self.parent.changePage("Exercise_Page_UI")

    def setlist(self,l):
        self.list = l
        
    def go_dia_add_food(self):
        self.parent.changePage("Food_add_dialog_ui")
    
    
    def go_dia_add_exercise(self):
        self.parent.changePage("Exercise_add_dialog_ui")
        
    
    def go_to_sum(self):
        self.graph = Graph()
        exercise = []
        dates = []
        date = []
        food = []
        net = []
        record = self.system.get_exercise_record()
        for i in record:
            dates.append(i.c_date)
        for j in set(dates):
            date.append(j)
            e = self.system.get_total_exercise_by_date(j)
            exercise.append(e)
            f = self.system.get_total_food_by_date(j)
            food.append(f)
            
            net.append(f-e)
        

        self.graph.add_list(net,exercise,date,food,len(date) )
        self.graph.show()

        

    def set_goal_label(self):
        self.Main_goal_bt.setText(self.user.name)


    def logout(self):
        self.parent.set_user_none()
        self.parent.changePage("Login_Page_UI")
        
