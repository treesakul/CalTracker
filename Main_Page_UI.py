import sys

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

from Dia_add_food import *
from Dia_add_exercise import *
from Edit_Profile_Page_UI import *
class Main_Page_UI(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, None)
        self.parent = parent
        self.user = None
        self.mainPageInit()

    def set_user(self, user):
        self.user =user
    
    def mainPageInit(self):
        loader = QUiLoader()
        form = loader.load("UIDesigner/MainPageUI.ui", None)
        self.setCentralWidget(form)

        #if self.sender() == "Edit_Profile_Page_UI":
            #print("from edit pro")

        # set QPushButton
        self.Main_profile_bt = form.findChild(QPushButton, "Main_profile_bt")
        self.Main_food_bt = form.findChild(QPushButton, "Main_food_bt")
        self.Main_ex_bt = form.findChild(QPushButton, "Main_ex_bt")
        self.Main_sum_bt = form.findChild(QPushButton, "Main_sum_bt")
        self.Main_food_add_bt = form.findChild(QPushButton, "Main_food_add_bt")
        self.Main_ex_add_bt = form.findChild(QPushButton, "Main_ex_add_bt")
        self.Main_goal_bt = form.findChild(QPushButton, "Main_goal_bt")


        # set QLabel
        self.Main_food_cal = form.findChild(QLabel, "Main_food_cal")
        self.Main_ex_cal = form.findChild(QLabel, "Main_ex_cal")
        self.Main_sum_cal = form.findChild(QLabel, "Main_sum_cal")

        #################################################
        self.main_Slider = form.findChild(QSlider, "main_Slider")
        self.val_slide = form.findChild(QLabel, "val_slide")

        self.minVal = 0
        self.maxVal = 100

        layout = QVBoxLayout()
        self.l1 = QLabel("Hello")
        self.l1.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.l1)

        self.sl = QSlider(Qt.Horizontal)
        self.sl.setMinimum(self.minVal)
        self.sl.setMaximum(self.maxVal)
        self.sl.setValue(20)

        layout.addWidget(self.sl)
        self.sl.valueChanged.connect(self.valuechange)
        self.setLayout(layout)
        self.setWindowTitle("SpinBox demo")



        #####################
        # connect QPushButton
        self.Main_profile_bt.clicked.connect(self.go_edit_profile)
        self.Main_food_bt.clicked.connect(self.go_food)
        self.Main_ex_bt.clicked.connect(self.go_exercise)

        # connect QPushButton dialog
        self.Main_food_add_bt.clicked.connect(self.dia_add_food)
        self.Main_ex_add_bt.clicked.connect(self.dia_add_exercise)
        self.Main_goal_bt.clicked.connect(self.go_goal)

        #self.set_goal_label()

    def valuechange(self):
        size = self.sl.value()
        self.val_slide.setText(size)

    def go_edit_profile(self):
        self.parent.changePage("Edit_Profile_Page_UI")

    def go_goal(self):
        self.parent.changePage("Goal_Page_UI")

    def go_food(self):
        self.parent.changePage("Food_Page_UI")


    def go_exercise(self):
        self.parent.changePage("Exercise_Page_UI")


    def dia_add_food(self):

        d = Dia_add_food()
        d.dia_add_food_init(self)



    def dia_add_exercise(self):
        d = Dia_add_exercise()
        d.dia_add_ex_init(self)


    def set_goal_label(self):
        self.Main_goal_bt.setText("Goal: eiei")

    def set_pic_user(self):
        e = Edit_Profile_Page_UI()
        filename = e.get_pic()
        self.pic = QPixmap(filename)

        width = self.EditPro_pic_bt.size().width()
        height = self.EditPro_pic_bt.size().height()

        self.pic.scaled(width, height, Qt.KeepAspectRatio)
        icon = QIcon(self.pic)
        # icon = QIcon(QPixmap(filename))

        self.EditPro_pic_bt.setText("")
        self.EditPro_pic_bt.setIcon(icon)

        self.EditPro_pic_bt.setIconSize(QSize(self.EditPro_pic_bt.size().width(), self.EditPro_pic_bt.size().height()))
        # self.EditPro_pic_bt.setScaledContents(True)


