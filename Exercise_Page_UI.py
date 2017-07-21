import sys

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

from MainSystem import *


class Exercise_Page_UI(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, None)
        self.parent = parent
        self.cur_pic = "D:/SE/SEP/project/Cal Tracker/Cal Tracker2/CalTracker-e6f5620a53ae6aea39b1c608d6ce27ee48a7f4ea/un_food.jpg"
        self.exercise_page_init()

    def exercise_page_init(self):
        loader = QUiLoader()
        form = loader.load("UIDesigner/Exercise_page_ui.ui", None)
        self.setCentralWidget(form)

        self.system = MainSystem()
        self.current_click = ""

        # set QLineEdit
        self.exercise_search_textEdit = form.findChild(QLineEdit, "exercise_search_textEdit")

        # set QTextEdit
        self.exercise_info_des_textedit = form.findChild(QTextEdit, "exercise_info_des_textEdit")

        #set QPushButton
        self.exercise_search_bt = form.findChild(QPushButton, "exercise_search_bt")
        self.exercise_clear_bt = form.findChild(QPushButton, "exercise_clear_bt")
        self.exercise_back_bt = form.findChild(QPushButton, "exercise_back_bt")
        self.exercise_add_bt = form.findChild(QPushButton, "exercise_add_bt")
        self.exercise_delete_bt = form.findChild(QPushButton, "exercise_delete_bt")


        # set QScrollArea
        self.exercise_scrollArea = form.findChild(QScrollArea, "exercise_scrollArea")
        self.set_scrollarea()

        # set QLabel
        self.exercise_name_lb = form.findChild(QLabel, "exercise_name_lb")
        self.exercise_type_lb = form.findChild(QLabel, "exercise_type_lb")
        self.exercise_howto_lb = form.findChild(QLabel, "exercise_howto_lb")
        self.exercise_pic = form.findChild(QLabel, "exercise_pic")
        self.exercise_back = form.findChild(QLabel, "exercise_back")
        
        ####################
        #connect QPushButton
        self.exercise_back_bt.clicked.connect(self.back_main)
        self.exercise_search_bt.clicked.connect(self.search)
        self.exercise_clear_bt.clicked.connect(self.clear)
        self.exercise_delete_bt.clicked.connect(self.delete)
        self.exercise_add_bt.clicked.connect(self.go_db_page)


        self.cur_pic = "D:\SE\SEP\project\Cal Tracker\Cal Tracker2\CalTracker-e6f5620a53ae6aea39b1c608d6ce27ee48a7f4ea"
        self.in_stylesheet = "QLabel {border-image: url("+str(self.cur_pic)+") }"
        self.exercise_pic.setStyleSheet(self.in_stylesheet)


        self.exercise_name_lb.hide()
        self.exercise_type_lb.hide() 
        self.exercise_howto_lb.hide()
        self.exercise_pic.hide()
        self.exercise_back.hide()
        self.exercise_info_des_textedit.hide()



    def set_scrollarea(self):
        self.name = self.system.show_exercise()
      
        count = 0


        self.widgetWoi = QWidget()  # create very large + long widget
        layoutx = QVBoxLayout()  # layout for tht wiget
        for i in self.name:
            layouth = QHBoxLayout()
            self.bt = QPushButton(i.name)
            self.bt.clicked.connect(self.show_info)
            layouth.addWidget(self.bt)
            a = QLabel(str(i.calorie))
            a.setAlignment(Qt.AlignCenter)

            layouth.addWidget(a)
           # layouth.addWidget(self.bt[i])
            layoutx.addLayout(layouth)
            count = count + 1
        layoutx.setAlignment(Qt.AlignTop)
        self.widgetWoi.setLayout(layoutx)

        self.exercise_scrollArea.setWidget(self.widgetWoi)

        #self.namea = self.name
        #self.namea.clicked.connect(self.show_info)




    def show_info(self):
        self.name_info = self.sender().text()
        self.current_click = self.name_info

        self.exercise_name_lb.show()
        self.exercise_type_lb.show() 
        self.exercise_howto_lb.show()
        self.exercise_pic.show()
        self.exercise_back.show()
        self.exercise_info_des_textedit.show()
        
        for n in self.name:
            if self.name_info.lower() == n.name.lower():
                t = n

        text_name = "Name : "+str(self.name_info)
        text_cal = "Cal : " + str(t.calorie)
        text_des = str(t.description)

        pic = t.pic


        #self.exercise_pic.setText("")
        self.cur_pic = pic 

        if(pic is None):
            self.cur_pic = "D:/SE/SEP/project/Cal Tracker/Cal Tracker2/CalTracker-e6f5620a53ae6aea39b1c608d6ce27ee48a7f4ea/un_exercise.jpg"   

        self.in_stylesheet = "QLabel {border-image: url("+str(self.cur_pic)+") }"
        self.exercise_pic.setStyleSheet(self.in_stylesheet)
        
        
        self.exercise_name_lb.setText(text_name)
        self.exercise_type_lb.setText(text_cal)
        self.exercise_info_des_textedit.setText(text_des)


    def search(self):
        self.exercise_search = self.exercise_search_textEdit.text()
        for i in self.name:
            if( self.exercise_search.lower() ==  i.name.lower()):

                self.widget = QWidget()  # create very large + long widget
                #box = QBoxLayout.TopToBottom
                layouth = QHBoxLayout()
                self.bt = QPushButton(self.exercise_search)
                self.bt.clicked.connect(self.show_info)
                layouth.addWidget(self.bt)
                layouth.addWidget(QLabel(str(i.calorie)))

                layouth.setAlignment(Qt.AlignTop)
                self.widget.setLayout(layouth)

                self.exercise_scrollArea.setWidget(self.widget)

    def delete(self):
        #food_info_name
        #self.food_search = self.sender().text()
        #print("foodsearch=",self.food_search)
        a = self.system.search_exercise(self.current_click)


        self.system.remove_exercise(a.id)
        self.set_scrollarea()

    def update(self):
        self.set_scrollarea()
    def clear(self):
        self.set_scrollarea()


    def go_db_page(self):
        self.parent.changePage("DB_Add_Page_UI")

    def back_main(self):
        self.exercise_name_lb.hide()
        self.exercise_type_lb.hide() 
        self.exercise_howto_lb.hide()
        self.exercise_pic.hide()
        self.exercise_back.hide()
        self.exercise_info_des_textedit.hide()
        self.parent.changePage("Main_Page")

