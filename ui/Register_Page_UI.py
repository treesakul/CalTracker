import sys

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

class Register_Page_UI(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, None)
        self.parent = parent
        self.register_page_init()

    def register_page_init(self):
        loader = QUiLoader()
        form = loader.load("UIDesigner/Register_page_ui.ui", None)
        self.setCentralWidget(form)

        # set QLineEdit
        self.Register_Fname_textEdit = form.findChild(QLineEdit, "Register_Fname_textEdit")
        self.Register_Lname_textEdit = form.findChild(QLineEdit, "Register_Lname_textEdit")
        self.Register_userName_textEdit = form.findChild(QLineEdit, "Register_userName_textEdit")
        self.Register_passWord_textEdit = form.findChild(QLineEdit, "Register_passWord_textEdit")
        self.Register_weight_textEdit = form.findChild(QLineEdit, "Register_weight_textEdit")
        self.Register_height_textEdit = form.findChild(QLineEdit, "Register_height_textEdit")


        #set QRadioButton
        self.Register_Gender_Female_radioBT = form.findChild(QRadioButton, "Register_Gender_Female_radioBT")
        self.Register_Gender_Male_radioBT = form.findChild(QRadioButton, "Register_Gender_Male_radioBT")
        self.GenderGroup = QButtonGroup()
        self.GenderGroup.addButton(self.Register_Gender_Female_radioBT)
        self.GenderGroup.addButton(self.Register_Gender_Male_radioBT)



        #set QDateEdit
        self.Register_Bday_dateEdit = form.findChild(QDateEdit, "Register_Bday_dateEdit")


        #set QTextEdit
        self.show_textEdit = form.findChild(QTextEdit, "show_textEdit")


        #set QPushButton
        self.Register_save_bt = form.findChild(QPushButton, "Register_save_bt")
        self.Register_back_bt = form.findChild(QPushButton, "Register_back_bt")





        #connect QPushButton
        self.Register_back_bt.clicked.connect(self.back_login)
        self.Register_save_bt.clicked.connect(self.save)

        #connect QRadioButton
        self.Register_Gender_Female_radioBT.clicked.connect(self.genderclick)
        self.Register_Gender_Male_radioBT.clicked.connect(self.genderclick)


    def genderclick(self):
        if self.sender() == self.Register_Gender_Female_radioBT:
            print("female")
            self.gender = "female"
        elif self.sender() == self.Register_Gender_Male_radioBT:
            print("male")
            self.gender = "male"



    def back_login(self):
        print("back")
        self.parent.changePage("Login_Page_UI")


    def save(self):
        ###### .text() use with lineedit  ###### .toPlainText() use with textedit

        self.show_textEdit.setText("")

        self.Fname = self.Register_Fname_textEdit.text()
        self.Lname = self.Register_Lname_textEdit.text()
        self.Username = self.Register_userName_textEdit.text()
        self.password = self.Register_passWord_textEdit.text()
        self.weigth = self.Register_weight_textEdit.text()
        self.heigth = self.Register_height_textEdit.text()

        self.date = self.Register_Bday_dateEdit.date().day()
        self.month = self.Register_Bday_dateEdit.date().month()
        self.year = self.Register_Bday_dateEdit.date().year()


        self.show_textEdit.append(self.Fname)
        self.show_textEdit.append(self.Lname)
        self.show_textEdit.append(self.Username)
        self.show_textEdit.append(self.password)
        self.show_textEdit.append(self.gender)
        self.show_textEdit.append(self.weigth)
        self.show_textEdit.append(self.heigth)
        self.show_textEdit.append(str(self.date))
        self.show_textEdit.append(str(self.month))
        self.show_textEdit.append(str(self.year))


