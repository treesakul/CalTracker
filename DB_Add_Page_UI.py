import sys

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

from Food import *
from Exercise import *
from MainSystem import *


class DB_Add_Page_UI(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, None)
        self.parent = parent
        self.from_page = ""
        self.db_add_page_init()
        self.filename = ""

    def db_add_page_init(self):
        loader = QUiLoader()
        form = loader.load("UIDesigner/DB_add_page_ui.ui", None)
        self.setCentralWidget(form)

        #self.system = MainSystem()
        self.current_click = ""
        self.datalist = []
        self.system = MainSystem()


        # set QLineEdit
        self.DB_name = form.findChild(QLineEdit, "DB_name")
        self.DB_cal = form.findChild(QLineEdit, "DB_cal")

        # set QTextEdit
        self.DB_des = form.findChild(QTextEdit, "DB_des")

        #set QPushButton
        self.DB_up_pic_bt = form.findChild(QPushButton, "DB_up_pic_bt")
        self.DB_save_bt = form.findChild(QPushButton, "DB_save_bt")
        self.DB_back_bt = form.findChild(QPushButton, "DB_back_bt")

        #set QRadioButton
        self.DB_food_ra = form.findChild(QRadioButton, "DB_food_ra")
        self.DB_exercise_ra = form.findChild(QRadioButton, "DB_exercise_ra")
        self.GenderGroup = QButtonGroup()
        self.GenderGroup.addButton(self.DB_food_ra)
        self.GenderGroup.addButton(self.DB_exercise_ra)


        # set QLabel
        self.DB_pic = form.findChild(QLabel, "DB_pic")
        
        ####################
        #connect QPushButton
        self.DB_back_bt.clicked.connect(self.back_page)
        self.DB_save_bt.clicked.connect(self.save)
        self.DB_up_pic_bt.clicked.connect(self.get_pic)

        #connect QRadioButton
        self.DB_food_ra.clicked.connect(self.raclick)
        self.DB_exercise_ra.clicked.connect(self.raclick)

    def raclick(self):
        if self.sender() == self.DB_food_ra:
 
            self.from_page = "food"
        elif self.sender() == self.DB_exercise_ra:
 
            self.from_page = "exercise"
        

    def get_pic(self):
        self.filename,type = QFileDialog.getOpenFileName(self, 'Open Image','./' , "Image files(*.png *.jpg *.bmp *.gif)")

        self.DB_pic.setPixmap(QPixmap(self.filename))

        self.DB_pic.setScaledContents(True)
        

    def save(self):
        self.name = self.DB_name.text()
        self.cal = self.DB_cal.text()
        self.des = self.DB_des.toPlainText()
        self.pic = self.filename
        
        if self.from_page == "food":
            
            self.system.add_food(self.name, self.cal,self.pic, self.des)

        elif self.from_page == "exercise":
        
            self.system.add_exercise(self.name,self.cal,self.des, self.pic) 

        dialog = QMessageBox(self)
        dialog.setText("saved")
        dialog.setStandardButtons(QMessageBox.Ok)#|QMessageBox.Cancel
        dialog.exec_()

        self.DB_name.setText("")
        self.DB_cal.setText("")
        self.DB_des.setText("")
        self.DB_pic.clear()
        
        self.back_page()
        
    def back_page(self):
        self.DB_name.setText("")
        self.DB_cal.setText("")
        self.DB_des.setText("")
        self.DB_pic.clear()
        
        if self.from_page == "food":
            
            self.parent.changePage("Food_Page_UI")

        elif self.from_page == "exercise":
            
            self.parent.changePage("Exercise_Page_UI")

        else:
            self.parent.changePage("Main_Page")
            

