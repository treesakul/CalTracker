import sys

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

from PersonalSystem import *

class Dia_add_food(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, None)
        self.parent = parent
        self.dia_add_food_init()
        #self.system = PersonalSystem()


    def dia_add_food_init(self):
        loader = QUiLoader()
        form = loader.load("UIDesigner/Food_add_dialog_ui.ui", None)
        self.setCentralWidget(form)
        self.system = PersonalSystem()
        self.list_info = []
        self.current_click = ""
        if(self.parent.getUser() != None):

            self.system.set_user(self.parent.getUser())
            self.list_info = self.system.show_personal_food()

        
        # set QComboBox
        self.foodDai_search_cb = form.findChild(QComboBox, "foodDai_search_cb")
        self.foodDai_quantity_cb = form.findChild(QComboBox, "foodDai_quantity_cb")
        
        #set QPushButton
        self.foodDai_back_bt = form.findChild(QPushButton, "foodDai_back_bt")
        self.foodDai_add_bt = form.findChild(QPushButton, "foodDai_add_bt")
        self.foodDai_delete_bt = form.findChild(QPushButton, "foodDai_delete_bt")

        #set QScrollArea
        self.foodDai_scrollArea = form.findChild(QScrollArea, "foodDai_scrollArea")
        self.set_scrollarea()


        #self.food_pic.setScaledContents(True)


        ####################

        #connect QPushButton
        self.foodDai_back_bt.clicked.connect(self.back_main)
        self.foodDai_add_bt.clicked.connect(self.add)
        self.foodDai_delete_bt.clicked.connect(self.delete)



        #add data combobox
        #self.name = ["fant", "Krai", "Nine", "Pim"]
        all_names = self.system.show_food()
        
        for i in all_names:
            self.foodDai_search_cb.addItem(i.name)

        for i in range(1,11):
            self.foodDai_quantity_cb.addItem(str(i))







    def add(self):

        currentcb = self.foodDai_search_cb.currentText()
        current_qt = self.foodDai_quantity_cb.currentText()
        
        #if(currentcb not in self.list_info):
        
        food = self.system.search_food(currentcb)

        self.system.add_personal_food(food,current_qt)

        
        #self.list_info.append(currentcb)
        self.set_scrollarea()

    def delete(self):

        a,b=self.current_click.split(":")

        with db_session:
            FoodRecord[a].delete()
        self.update()


        
    def set_scrollarea(self):
        self.widgetS = QWidget()
        layoutx = QVBoxLayout()
        self.system.set_user(self.parent.getUser())
   
        if(self.parent.getUser() != None):
            self.list_info = self.system.show_personal_food()
            
        for i in self.list_info:
            layouth = QHBoxLayout()
            #self.label = QLabel(str(self.system.search_food_by_id(i.food_id)))
            self.bt = QPushButton(str(i.id)+":"+str(self.system.search_food_by_id(i.food_id)))
            self.bt.clicked.connect(self.click)
            layouth.addWidget(self.bt)
            #layouth.addWidget(self.label)

            layoutx.addLayout(layouth)
        layoutx.setAlignment(Qt.AlignTop)

        self.widgetS.setLayout(layoutx)

        self.foodDai_scrollArea.setWidget(self.widgetS)
        

    def click(self):
        self.current_click = self.sender().text()


    def update(self):
        self.system.set_user(self.parent.getUser())
        if(self.parent.getUser() != None):
            self.list_info = self.system.show_personal_food()
        self.set_scrollarea()

    def back_main(self):
        self.parent.changePage("Main_Page")

