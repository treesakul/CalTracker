import sys

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *



class Dia_add_food(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, None)
        self.parent = parent
        self.dia_add_food_init()


    def dia_add_food_init(self):
        loader = QUiLoader()
        form = loader.load("UIDesigner/Food_add_dialog_ui.ui", None)
        self.setCentralWidget(form)

        self.list_info = []
        # set QComboBox
        self.foodDai_search_cb = form.findChild(QComboBox, "foodDai_search_cb")

        #set QPushButton
        self.foodDai_save_bt = form.findChild(QPushButton, "foodDai_save_bt")
        self.foodDai_back_bt = form.findChild(QPushButton, "foodDai_back_bt")
        self.foodDai_add_bt = form.findChild(QPushButton, "foodDai_add_bt")
        self.foodDai_delete_bt = form.findChild(QPushButton, "foodDai_delete_bt")

        #set QScrollArea
        self.foodDai_scrollArea = form.findChild(QScrollArea, "foodDai_scrollArea")
        self.set_scrollarea()


        #self.food_pic.setScaledContents(True)


        ####################

        #connect QPushButton
        self.foodDai_save_bt.clicked.connect(self.save)
        self.foodDai_back_bt.clicked.connect(self.back_main)
        self.foodDai_add_bt.clicked.connect(self.add)
        self.foodDai_delete_bt.clicked.connect(self.delete)




        self.name = ["fant", "Krai", "Nine", "Pim"]
        self.cal = ["100", "80", "50", "280"]
        for i in self.name:
            self.foodDai_search_cb.addItem(i)


        print(self.list_info)


    def back_main(self):
        print("im in")
        self.addDialog.close()
        #sys.exit(self.exec_())


    def add(self):
        print("add")
        currentcb = self.foodDai_search_cb.currentText()
        if(currentcb not in self.list_info):
            self.list_info.append(currentcb)
            self.set_scrollarea()

    def delete(self):
        print("delete")
        currentcb = self.foodDai_search_cb.currentText()
        if (currentcb in self.list_info):
            self.list_info.remove(currentcb)
            self.set_scrollarea()

    def save(self):
        print(self.list_info)
    def set_scrollarea(self):
        self.widgetS = QWidget()
        layoutx = QVBoxLayout()
        for i in self.list_info:
            layouth = QHBoxLayout()
            self.label = QLabel(i)

            layouth.addWidget(self.label)

            layoutx.addLayout(layouth)
        layoutx.setAlignment(Qt.AlignTop)

        self.widgetS.setLayout(layoutx)

        self.foodDai_scrollArea.setWidget(self.widgetS)


    def back_main(self):
        self.parent.changePage("Main_Page")

