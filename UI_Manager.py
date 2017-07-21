import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *
from Login_Page_UI import *
from Main_Page_UI import *
from Edit_Profile_Page_UI import *
from Food_Page_UI import *
from Dia_add_food import *
from DB_Add_Page_UI import *

from Exercise_Page_UI import *
from Dia_add_exercise import *
from Register_Page_UI import*
from Goal_Page_UI import *

from pony.orm import *
db = Database()
db.bind('oracle', 'TANAKORN/password@127.0.01')

class UI_Manager(QMainWindow):

    def __init__(self, parent = None):
        QMainWindow.__init__(self, None) #init
        self.parent = parent
        self.setWindowTitle("CALTracker")
        
        #QMacintoshstyle

        '''
        motif
        Windows
        cde
        Plastique
        Cleanlooks
        windowsvista
        Macintosh
        GTK
        
        '''
        QApplication.setStyle(QStyleFactory.create("Plastique"))

        #add background img

        '''
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("pngUI/LoginPageUI.png")))
        self.setPalette(palette)
        '''

        # user data
        self.current_account = None
        self.current_user = None
        self.current_goal = None
        
        #self.page_list = ["login_page",  "main_page"]

        # create stackedwidget + show first page
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
        login_widget = Login_Page_UI(self)
        self.central_widget.addWidget(login_widget)

        # add widget
        self.login_page_widget = Login_Page_UI(self)
        self.main_page_widget = Main_Page_UI(self)
        self.edit_profile_page_widget = Edit_Profile_Page_UI(self)
        self.goal_page_widget = Goal_Page_UI(self)
        self.food_page_widget = Food_Page_UI(self)
        self.dia_add_food_widget = Dia_add_food(self)
        self.db_add_widget = DB_Add_Page_UI(self)
        self.exercise_page_widget = Exercise_Page_UI(self)
        self.dia_add_exercise_widget = Dia_add_exercise(self)
        Exercise_Page_UI(self)
        self.register_page_widget = Register_Page_UI(self)

        # set central widget
        self.central_widget.addWidget(self.login_page_widget)
        self.central_widget.addWidget(self.main_page_widget)
        self.central_widget.addWidget(self.edit_profile_page_widget)
        self.central_widget.addWidget(self.goal_page_widget)
        self.central_widget.addWidget(self.food_page_widget)
        self.central_widget.addWidget(self.dia_add_food_widget)
        self.central_widget.addWidget(self.db_add_widget)
        self.central_widget.addWidget(self.exercise_page_widget)
        self.central_widget.addWidget(self.dia_add_exercise_widget)
        self.central_widget.addWidget(self.register_page_widget)

    def loginAs(self, user):
        with db_session:
            self.current_account = Account[user]
            self.current_user = Profile[user]
            self.current_goal = Goal[user]

    def getId(self):
        return self.current_user.id

    def getUser(self):
        return self.current_user
    
    def changePage(self, toPage):
        if (toPage == "Login_Page_UI"):
            self.login_page_widget.update()
            self.centralWidget().setCurrentWidget(self.login_page_widget)

        elif(toPage == "Main_Page"):
            self.main_page_widget.update()
            self.centralWidget().setCurrentWidget(self.main_page_widget)

        elif (toPage == "Edit_Profile_Page_UI"):
            self.edit_profile_page_widget.update()
            self.centralWidget().setCurrentWidget(self.edit_profile_page_widget)

        elif (toPage == "Goal_Page_UI"):
            self.centralWidget().setCurrentWidget(self.goal_page_widget)

        elif (toPage == "Food_Page_UI"):
            self.food_page_widget.update()
            self.centralWidget().setCurrentWidget(self.food_page_widget)

        elif (toPage == "Food_add_dialog_ui"):
            self.dia_add_food_widget.update()
            self.centralWidget().setCurrentWidget(self.dia_add_food_widget)

        elif (toPage == "DB_Add_Page_UI"):
            self.centralWidget().setCurrentWidget(self.db_add_widget)

  
        elif (toPage == "Exercise_Page_UI"):
            self.exercise_page_widget.update()
            self.centralWidget().setCurrentWidget(self.exercise_page_widget)

        elif (toPage == "Exercise_add_dialog_ui"):
            self.dia_add_exercise_widget.update()
            self.centralWidget().setCurrentWidget(self.dia_add_exercise_widget)

        elif (toPage == "Register_Page_UI"):
            self.centralWidget().setCurrentWidget(self.register_page_widget)

    def set_user_none(self):
        self.current_user = None
def main():
        app = QApplication(sys.argv)

        w = UI_Manager()
        w.show()
        return app.exec_()

if __name__ == "__main__":
        sys.exit(main())
