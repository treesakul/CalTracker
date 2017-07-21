import sys

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

from MainSystem import *


from Food import *

class Food_Page_UI(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, None)
        self.parent = parent
        self.cur_pic = "D:/SE/SEP/project/Cal Tracker/Cal Tracker2/CalTracker-e6f5620a53ae6aea39b1c608d6ce27ee48a7f4ea/un_food.jpg"
        self.food_page_init()

    def food_page_init(self):
        loader = QUiLoader()
        form = loader.load("UIDesigner/Food_page_ui.ui", None)
        self.setCentralWidget(form)

        self.system = MainSystem()
        self.current_click = ""

        # set QLineEdit
        self.food_search_textEdit = form.findChild(QLineEdit, "food_search_textEdit")

        # set QTextEdit
        self.food_info_des_textedit = form.findChild(QTextEdit, "food_info_des_textedit")

        #set QPushButton
        self.food_search_bt = form.findChild(QPushButton, "food_search_bt")
        self.food_clear_bt = form.findChild(QPushButton, "food_clear_bt")
        self.food_back_bt = form.findChild(QPushButton, "food_back_bt")
        self.food_add_bt = form.findChild(QPushButton, "food_add_bt")
        self.food_delete_bt = form.findChild(QPushButton, "food_delete_bt")

        #set QScrollArea
        self.food_scrollArea = form.findChild(QScrollArea, "food_scrollArea")
        self.set_scrollarea()


        # set QLabel
        self.food_info_name = form.findChild(QLabel, "food_info_name")
        self.food_info_cal = form.findChild(QLabel, "food_info_cal")
        self.food_info_des = form.findChild(QLabel, "food_info_des")
        self.food_back = form.findChild(QLabel, "food_back")
        
        
        self.food_pic = form.findChild(QLabel, "food_pic")
        #self.food_pic.setPixmap("./fresh-healthy-apples.jpg")
        #self.food_pic.setScaledContents(True)

        #self.food_info_name.setText("Name: eiei")
        ####################
        #connect QPushButton
        self.food_back_bt.clicked.connect(self.back_main)
        self.food_search_bt.clicked.connect(self.search)
        self.food_clear_bt.clicked.connect(self.clear)
        self.food_delete_bt.clicked.connect(self.delete)
        self.food_add_bt.clicked.connect(self.go_db_food)

        self.cur_pic = "D:\SE\SEP\project\Cal Tracker\Cal Tracker2\CalTracker-e6f5620a53ae6aea39b1c608d6ce27ee48a7f4ea"
        self.in_stylesheet = "QLabel {border-image: url("+str(self.cur_pic)+") }"
        self.food_pic.setStyleSheet(self.in_stylesheet)


        self.food_pic.hide()
        self.food_info_des_textedit.hide()
        self.food_info_des.hide()
        self.food_info_cal.hide()
        self.food_info_name.hide()
        self.food_back.hide()

 
    

    def set_scrollarea(self):
        self.name = self.system.show_food()
        
        count = 0


        self.widgetS = QWidget()  # create very large + long widget
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
        self.widgetS.setLayout(layoutx)

        self.food_scrollArea.setWidget(self.widgetS)

        #self.namea = self.name
        #self.namea.clicked.connect(self.show_info)

    def show_info(self):
        self.name_info = self.sender().text()
        self.current_click = self.name_info

        self.food_pic.show()
        self.food_info_des_textedit.show()
        self.food_info_des.show()
        self.food_info_cal.show()
        self.food_info_name.show()
        self.food_back.show()

        for n in self.name:
            if self.name_info.lower() == n.name.lower():
                t = n

        text_name = "Name : "+str(self.name_info)
        text_cal = "Cal : " + str(t.calorie)
        text_des = str(t.description)
        pic = t.pic


        #self.food_pic.setText("")
        
        self.cur_pic = pic

        if(pic is None):
            #self.cur_pic = self.system.get_food_pic
            self.cur_pic = "D:/SE/SEP/project/Cal Tracker/Cal Tracker2/CalTracker-e6f5620a53ae6aea39b1c608d6ce27ee48a7f4ea/un_food.jpg"   
        self.in_stylesheet = "QLabel {border-image: url("+str(self.cur_pic)+") }"
        self.food_pic.setStyleSheet(self.in_stylesheet)
         
        
        self.food_info_name.setText(text_name)
        self.food_info_cal.setText(text_cal)
        self.food_info_des_textedit.setText(text_des)


    def search(self):
        self.food_search = self.food_search_textEdit.text()
        for i in self.name:
            if( self.food_search.lower() == i.name.lower()):

                self.widget = QWidget()  # create very large + long widget
                #box = QBoxLayout.TopToBottom
                layouth = QHBoxLayout()
                self.bt = QPushButton(self.food_search)
                self.bt.clicked.connect(self.show_info)
                layouth.addWidget(self.bt)
                layouth.addWidget(QLabel(str(i.calorie)))

                layouth.setAlignment(Qt.AlignTop)
                self.widget.setLayout(layouth)

                self.food_scrollArea.setWidget(self.widget)
                
    def update(self):
        self.set_scrollarea()

        
    def delete(self):
        #food_info_name
        #self.food_search = self.sender().text()
        #print("foodsearch=",self.food_search)
        a = self.system.search_food(self.current_click)


        self.system.remove_food(a.id)
        self.set_scrollarea()
        
        
    def clear(self):
        self.set_scrollarea()


    def go_db_food(self):
        self.parent.changePage("DB_Add_Page_UI")
        
    def back_main(self):
        self.food_pic.hide()
        self.food_info_des_textedit.hide()
        self.food_info_des.hide()
        self.food_info_cal.hide()
        self.food_info_name.hide()
        self.food_back.hide()
        self.parent.changePage("Main_Page")

