import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *
from LogIn import *
from Account import *

class Login_Page_UI(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, None)
        self.parent = parent
        self.loginPageInit()
        self.system = LoginSystem()
        
    def loginPageInit(self):
        loader = QUiLoader()
        form = loader.load("./UIDesigner/LoginPageUI.ui", None)
        self.setCentralWidget(form)

        # set QPushButton
        self.login_button = form.findChild(QPushButton, "login_button")
        self.register_button = form.findChild(QPushButton, "register_button")

        # set QLineEdit
        self.username_entry = form.findChild(QLineEdit, "username_entry")
        self.password_entry = form.findChild(QLineEdit, "password_entry")

        # set QLabel
        self.login_pic = form.findChild(QLabel, "login_pic")
        self.login_pic.setPixmap("./fresh-healthy-apples.jpg")

        #############################
        # connect QPushbutton
        self.login_button.clicked.connect(self.login)
        self.register_button.clicked.connect(self.register)

    def login(self):
##        print(self.login_button )
##        print(self.username_entry)
        self.username = self.username_entry.text()
        self.password = self.password_entry.text()
##        print(self.username)
        
        if self.system.check(self.username,self.password) == True:
                #print(self.system.getId())
            self.parent.loginAs(self.system.getId()) #####
            self.parent.changePage("Main_Page")   
        else:
            print("login error")
            
    def register(self):
        self.parent.changePage("Register_Page_UI")
