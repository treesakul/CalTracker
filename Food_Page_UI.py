import sys

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *


from Food import *

class Food_Page_UI(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, None)
        self.parent = parent
        self.food_page_init()

    def food_page_init(self):
        loader = QUiLoader()
        form = loader.load("UIDesigner/Food_page_ui.ui", None)
        self.setCentralWidget(form)

        # set QLineEdit
        self.food_search_textEdit = form.findChild(QLineEdit, "food_search_textEdit")

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
        self.food_pic = form.findChild(QLabel, "food_pic")
        self.food_pic.setPixmap("./fresh-healthy-apples.jpg")
        self.food_pic.setScaledContents(True)

        #self.food_info_name.setText("Name: eiei")
        ####################
        #connect QPushButton
        self.food_back_bt.clicked.connect(self.back_main)
        self.food_search_bt.clicked.connect(self.search)
        self.food_clear_bt.clicked.connect(self.clear)

    

    def set_scrollarea(self):
        self.name = ["fant", "Krai", "Nine", "Pim"]
        self.cal = ["100", "80", "50", "280"]
        #self.name = ["fant", "Krai", "Nine", "Pim" , "a1", "a2", "a1", "a2", "a1", "a2", "a1", "a2", "a1", "a2", "a1", "a2", "a1", "a2"]
        #self.cal = ["100" , "80" , "50" , "280", "a1", "a2", "a1", "a2", "a1", "a2", "a1", "a2", "a1", "a2", "a1", "a2", "a1", "a2"]
        #self.bt = []
        #button = []
        #for i in self.name:
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

        #self.namea = self.name
        #self.namea.clicked.connect(self.show_info)

    def show_info(self):
        self.name_info = self.sender().text()
        print(self.name_info)

        text = "Name: "+self.name_info
        self.food_info_name.setText(text)


    def search(self):
        self.food_search = self.food_search_textEdit.text()
        print("search: ", self.food_search)
        for i in self.name:
            if( self.food_search == i):

                self.widget = QWidget()  # create very large + long widget
                #box = QBoxLayout.TopToBottom
                layouth = QHBoxLayout()
                self.bt = QPushButton(self.food_search)
                self.bt.clicked.connect(self.show_info)
                layouth.addWidget(self.bt)
                layouth.addWidget(QLabel("222"))

                layouth.setAlignment(Qt.AlignTop)
                self.widget.setLayout(layouth)

                self.food_scrollArea.setWidget(self.widget)

    def clear(self):
        print("clear")
        self.set_scrollarea()


    def back_main(self):
        self.parent.changePage("Main_Page")

