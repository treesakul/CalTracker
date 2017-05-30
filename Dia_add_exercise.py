import sys

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *



class Dia_add_exercise(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, None)
        self.parent = parent
        self.dia_add_exercise_init()


    def dia_add_exercise_init(self):
        loader = QUiLoader()
        form = loader.load("UIDesigner/Exercise_add_dialog_ui.ui", None)
        self.setCentralWidget(form)

        self.list_info = []
        # set QComboBox
        self.exerciseDai_search_cb = form.findChild(QComboBox, "exerciseDai_search_cb")

        #set QPushButton
        self.exerciseDai_save_bt = form.findChild(QPushButton, "exerciseDai_save_bt")
        self.exerciseDai_back_bt = form.findChild(QPushButton, "exerciseDai_back_bt")
        self.exerciseDai_add_bt = form.findChild(QPushButton, "exerciseDai_add_bt")
        self.exerciseDai_delete_bt = form.findChild(QPushButton, "exerciseDai_delete_bt")

        #set QScrollArea
        self.exerciseDai_scrollArea = form.findChild(QScrollArea, "exerciseDai_scrollArea")
        self.set_scrollarea()


        #self.exercise_pic.setScaledContents(True)


        ####################

        #connect QPushButton
        self.exerciseDai_save_bt.clicked.connect(self.save)
        self.exerciseDai_back_bt.clicked.connect(self.back_main)
        self.exerciseDai_add_bt.clicked.connect(self.add)
        self.exerciseDai_delete_bt.clicked.connect(self.delete)




        self.name = ["fant", "Krai", "Nine", "Pim"]
        self.cal = ["100", "80", "50", "280"]
        for i in self.name:
            self.exerciseDai_search_cb.addItem(i)


        print(self.list_info)


    def back_main(self):
        print("im in")
        self.addDialog.close()
        #sys.exit(self.exec_())


    def add(self):
        print("add")
        currentcb = self.exerciseDai_search_cb.currentText()
        if(currentcb not in self.list_info):
            self.list_info.append(currentcb)
            self.set_scrollarea()

    def delete(self):
        print("delete")
        currentcb = self.exerciseDai_search_cb.currentText()
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

        self.exerciseDai_scrollArea.setWidget(self.widgetS)


    def back_main(self):
        self.parent.changePage("Main_Page")

