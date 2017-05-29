import sys

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *


class Dia_add_exercise:
    def dia_add_ex_init(self,dia):
        print("inside")
        self.dia_add_ex(dia)



    def dia_add_ex(self,dia):
        # Dialog box
        self.addDialog = QDialog(dia)
        self.addDialog.setMinimumSize(700, 600)
        layout = QVBoxLayout()

        loader = QUiLoader()
        dialogForm = loader.load("./UIDesigner/Exercise_add_dialog_ui.ui", None)
        self.addDialog.setWindowTitle("Exercise Add Dialog")

        layout.addWidget(dialogForm)



        # init all attribute
        # self.typeLabel = dialogForm.findChild(QLabel, "typeLabel")


        # show dialog box
        self.addDialog.setLayout(layout)
        self.addDialog.show()