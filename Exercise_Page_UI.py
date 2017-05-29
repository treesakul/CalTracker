import sys

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

class Exercise_Page_UI(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, None)
        self.parent = parent
        self.exercise_page_init()

    def exercise_page_init(self):
        loader = QUiLoader()
        form = loader.load("UIDesigner/Exercise_page_ui.ui", None)
        self.setCentralWidget(form)

        # set QLineEdit
        self.exercise_search_textEdit = form.findChild(QLineEdit, "exercise_search_textEdit")

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


        ####################
        #connect QPushButton
        self.exercise_back_bt.clicked.connect(self.back_main)
        self.exercise_search_bt.clicked.connect(self.search)
        self.exercise_clear_bt.clicked.connect(self.clear)




    def set_scrollarea(self):
        self.name = ["fant", "Krai", "Nine", "Pim"]
        self.Type = ["Endurance", "Strength", "Balance", "Flexibility"]
        #self.name = ["fant", "Krai", "Nine", "Pim" , "a1", "a2", "a1", "a2", "a1", "a2", "a1", "a2", "a1", "a2", "a1", "a2", "a1", "a2"]
        #self.cal = ["100" , "80" , "50" , "280", "a1", "a2", "a1", "a2", "a1", "a2", "a1", "a2", "a1", "a2", "a1", "a2", "a1", "a2"]
        #self.bt = []
        #button = []
        #for i in self.name:
          #  button[i] = QPushButton(i)
        count = 0


        self.widgetWoi = QWidget()  # create very large + long widget
        layoutx = QVBoxLayout()  # layout for tht wiget
        for i in self.name:
            layouth = QHBoxLayout()
            self.bt = QPushButton(i)
            self.bt.clicked.connect(self.show_info)
            layouth.addWidget(self.bt)


            layouth.addWidget(QLabel(self.Type[count]))
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
        print(self.name_info)

        text = "Name: "+self.name_info
        self.exercise_name_lb.setText(text)


    def search(self):
        self.exercise_search = self.exercise_search_textEdit.text()
        print("search: ", self.exercise_search)
        for i in self.name:
            if( self.exercise_search == i):

                self.widget = QWidget()  # create very large + long widget
                #box = QBoxLayout.TopToBottom
                layouth = QHBoxLayout()
                self.bt = QPushButton(self.exercise_search)
                self.bt.clicked.connect(self.show_info)
                layouth.addWidget(self.bt)
                layouth.addWidget(QLabel("222"))

                layouth.setAlignment(Qt.AlignTop)
                self.widget.setLayout(layouth)

                self.exercise_scrollArea.setWidget(self.widget)



    def clear(self):
        print("clear")
        self.set_scrollarea()



    def back_main(self):
        self.parent.changePage("Main_Page")

