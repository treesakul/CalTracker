import sys

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

from PersonalSystem import *

class Dia_add_exercise(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, None)
        self.parent = parent
        self.dia_add_exercise_init()


    def dia_add_exercise_init(self):
        loader = QUiLoader()
        form = loader.load("UIDesigner/Exercise_add_dialog_ui.ui", None)
        self.setCentralWidget(form)
        self.system = PersonalSystem()
        self.list_info = []
        self.current_click = ""
        if(self.parent.getUser() != None):
            self.system.set_user(self.parent.getUser())
            self.list_info = self.system.show_personal_exercise()

        
        # set QComboBox
        self.exerciseDai_search_cb = form.findChild(QComboBox, "exerciseDai_search_cb")
        self.exerciseDai_min_cb = form.findChild(QComboBox, "exerciseDai_min_cb")
        
        #set QPushButton
        self.exerciseDai_back_bt = form.findChild(QPushButton, "exerciseDai_back_bt")
        self.exerciseDai_add_bt = form.findChild(QPushButton, "exerciseDai_add_bt")
        self.exerciseDai_delete_bt = form.findChild(QPushButton, "exerciseDai_delete_bt")

        #set QScrollArea
        self.exerciseDai_scrollArea = form.findChild(QScrollArea, "exerciseDai_scrollArea")
        self.set_scrollarea()


        #self.exercise_pic.setScaledContents(True)


        ####################

        #connect QPushButton
        self.exerciseDai_back_bt.clicked.connect(self.back_main)
        self.exerciseDai_add_bt.clicked.connect(self.add)
        self.exerciseDai_delete_bt.clicked.connect(self.delete)


        #add data combobox
        all_names = self.system.show_exercise()
       
        for i in all_names:
            self.exerciseDai_search_cb.addItem(i.name)

        for i in range(10,91,10):
            self.exerciseDai_min_cb.addItem(str(i))


        




    def add(self):
       
        currentcb = self.exerciseDai_search_cb.currentText()
        current_min = self.exerciseDai_min_cb.currentText()
        
        #if(currentcb not in self.list_info):
        
        exercise = self.system.search_exercise(currentcb)
        
        self.system.add_personal_exercise(exercise,current_min)
        #self.list_info.append(currentcb)
        self.set_scrollarea()

    def delete(self):
        
        a,b=self.current_click.split(":")
        #currentcb = self.exerciseDai_search_cb.currentText()
        with db_session:
            ExerciseRecord[a].delete()
        self.update()

        
    def set_scrollarea(self):
        self.widgetS = QWidget()
        layoutx = QVBoxLayout()
        self.system.set_user(self.parent.getUser())

        if(self.parent.getUser() != None):
            self.list_info = self.system.show_personal_exercise()
            
        for i in self.list_info:
            layouth = QHBoxLayout()
            #self.label = QLabel(i)
            self.bt = QPushButton(str(i.id)+":"+str(self.system.search_exercise_by_id(i.exercise_id)))
            self.bt.clicked.connect(self.click)
            layouth.addWidget(self.bt)

            #layouth.addWidget(self.label)

            layoutx.addLayout(layouth)
        layoutx.setAlignment(Qt.AlignTop)

        self.widgetS.setLayout(layoutx)

        self.exerciseDai_scrollArea.setWidget(self.widgetS)


    def click(self):
        self.current_click = self.sender().text()
        

    def update(self):
        self.system.set_user(self.parent.getUser())
        if(self.parent.getUser() != None):
            self.list_info = self.system.show_personal_exercise()
        self.set_scrollarea()

    def back_main(self):
        self.parent.changePage("Main_Page")


