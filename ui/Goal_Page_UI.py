import sys

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

class Goal_Page_UI(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, None)
        self.parent = parent
        self.goal_page_init()

    def goal_page_init(self):
        loader = QUiLoader()
        form = loader.load("UIDesigner/Goal_page_ui.ui", None)
        self.setCentralWidget(form)


        # set QComboBox
        self.Goal_start_weight_cb = form.findChild(QComboBox, "Goal_start_weight_cb")
        self.Goal_current_weight_cb = form.findChild(QComboBox, "Goal_current_weight_cb")
        self.Goal_height_cb = form.findChild(QComboBox, "Goal_height_cb")
        self.Goal_goal_weight_cb = form.findChild(QComboBox, "Goal_goal_weight_cb")
        self.Goal_duration_cb = form.findChild(QComboBox, "Goal_duration_cb")
        self.set_range_cb()


        # set QDateEdit
        self.Goal_dateEdit = form.findChild(QDateEdit, "Goal_dateEdit")



        # set QPushButton
        self.Goal_save_bt = form.findChild(QPushButton, "Goal_save_bt")
        self.Goal_back_bt = form.findChild(QPushButton, "Goal_back_bt")



        # connect QComboBox
        '''
        self.Goal_start_weight_cb.currentIndexChanged.connect(self.show_info)
        self.Goal_current_weight_cb.currentIndexChanged.connect(self.show_info)
        self.Goal_height_cb.currentIndexChanged.connect(self.show_info)
        self.Goal_goal_weight_cb.currentIndexChanged.connect(self.show_info)
        self.Goal_duration_cb.currentIndexChanged.connect(self.show_info)

        '''

        #connect QPushButton
        self.Goal_back_bt.clicked.connect(self.back_main)
        self.Goal_save_bt.clicked.connect(self.save)


    def show_info(self):
        pass

    def set_range_cb(self):
        #############self.Goal_start_weight_cb
        for i in range(30,201):
            self.Goal_start_weight_cb.addItem(str(i))

        #############self.Goal_current_weight_cb
        for i in range(30, 201):
            self.Goal_current_weight_cb.addItem(str(i))

        #############self.Goal_height_cb
        for i in range(130, 221):
            self.Goal_height_cb.addItem(str(i))

        #############self.Goal_goal_weight_cb
        for i in range(30, 201):
            self.Goal_goal_weight_cb.addItem(str(i))


        #############self.Goal_duration_cb
        for i in range(1, 366):
            self.Goal_duration_cb.addItem(str(i))



    def back_main(self):
        #self.show_textEdit.setText("")
        self.parent.changePage("Main_Page")


    def save(self):
#############################################################################
        self.date = self.Goal_dateEdit.date().day()
        self.month = self.Goal_dateEdit.date().month()
        self.year = self.Goal_dateEdit.date().year()


        self.list_info = []
        self.list_info.append(self.Goal_start_weight_cb.currentText())
        self.list_info.append(self.Goal_current_weight_cb.currentText())
        self.list_info.append(self.Goal_height_cb.currentText())
        self.list_info.append(self.Goal_goal_weight_cb.currentText())
        self.list_info.append(self.Goal_duration_cb.currentText())
        self.list_info.append(str(self.date))
        self.list_info.append(str(self.month))
        self.list_info.append(str(self.year))


        print(self.list_info)
#############################################################################


