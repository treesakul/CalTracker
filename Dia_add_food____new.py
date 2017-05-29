
import sys

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *


class Dia_add_food:
    def dia_add_food_init(self,dia):
        self.dia_add_food(dia)



    def dia_add_food(self,dia):
        # Dialog box
        self.addDialog = QDialog(dia)
        self.addDialog.setMinimumSize(660, 600)
        layout = QVBoxLayout()

        loader = QUiLoader()
        dialogForm = loader.load("./UIDesigner/Food_add_dialog_ui_3.ui", None)
        self.addDialog.setWindowTitle("Food Add Dialog")

        layout.addWidget(dialogForm)

        # show dialog box
        self.addDialog.setLayout(layout)
        self.addDialog.show()



        ###############################################################


        # init all attribute

        # set QPushButton
        self.foodDai_delete_bt = dialogForm.findChild(QPushButton, "foodDai_delete_bt")
        self.foodDai_ok_bt = dialogForm.findChild(QPushButton, "foodDai_ok_bt")
        self.foodDai_add_bt = dialogForm.findChild(QPushButton, "foodDai_add_bt")


        # set QComboBox
        self.foodDai_search_cb = dialogForm.findChild(QComboBox, "foodDai_search_cb")

        # set QScrollArea
        self.foodDai_scrollArea = dialogForm.findChild(QScrollArea, "foodDai_scrollArea")





        #####################

        # connect QPushButton
        self.foodDai_delete_bt.clicked.connect(self.delete)
        self.foodDai_ok_bt.clicked.connect(self.ok)
        self.foodDai_add_bt.clicked.connect(self.addd)



        # connect QComboBox
        #self.foodDai_search_cb.currentIndexChanged.connect(self.show_info)

        self.name =  ["fant", "Krai", "Nine", "Pim"]
        self.cal = ["100", "80", "50", "280"]
        for i in self.name:
            self.foodDai_search_cb.addItem(i)




        self.list_info = []

    def ok(self):
        print("im in")
        self.addDialog.close()
        #sys.exit(self.exec_())


    def addd(self):
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



        def set_all_scrollarea(self):
            self.name = ["fant", "Krai", "Nine", "Pim"]
            self.cal = ["100", "80", "50", "280"]
            # self.name = ["fant", "Krai", "Nine", "Pim" , "a1", "a2", "a1", "a2", "a1", "a2", "a1", "a2", "a1", "a2", "a1", "a2", "a1", "a2"]
            # self.cal = ["100" , "80" , "50" , "280", "a1", "a2", "a1", "a2", "a1", "a2", "a1", "a2", "a1", "a2", "a1", "a2", "a1", "a2"]
            # self.bt = []
            # button = []
            # for i in self.name:
            #  button[i] = QPushButton(i)
            count = 0

            self.widgetS = QWidget()  # create very large + long widget
            layoutx = QVBoxLayout()  # layout for tht wiget
            for i in self.name:
                layouth = QHBoxLayout()
                self.bt = QPushButton(i)
                self.bt.clicked.connect(self.show_info)
                layouth.addWidget(self.bt)

                layouth.addWidget(QLabel(self.cal[count]))
                # layouth.addWidget(self.bt[i])
                layoutx.addLayout(layouth)
                count = count + 1
            layoutx.setAlignment(Qt.AlignTop)
            self.widgetS.setLayout(layoutx)

            self.food_scrollArea.setWidget(self.widgetS)

            # self.namea = self.name
            # self.namea.clicked.connect(self.show_info)



