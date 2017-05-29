import sys

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *


class UI_Manager(QWidget):
    def __init__(self, parent = None): #init
        QWidget.__init__(self, None)
        

        self.setWindowTitle("CALTracker")

        
        self.layout = QVBoxLayout()




        for i in range(5):
            self.infoList = QHBoxLayout()
            self.infoList.addWidget(QLabel("Food Name: "))
            self.infoList.addWidget(QLineEdit())
            self.layout.addLayout(self.infoList)
            #self.infoList.add'''

        self.setLayout(self.layout)

        
def main():
        app = QApplication(sys.argv)

        w = UI_Manager()
        w.show()
        return app.exec_()

if __name__ == "__main__":
        sys.exit(main())




'''

import sys
from PySide.QtCore import *
from PySide.QtGui import *


class ShowFant(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)

        self.mainLayout = QVBoxLayout()

        self.itemList = []

        for i in range(10):
            layout = QGridLayout()
            layout.addWidget(QLabel("Name: "), 1, 0)
            layout.addWidget(QLineEdit(), 1, 1)
            layout.addWidget(QLabel("Description: "), 2, 0)
            layout.addWidget(QLineEdit(), 2, 1)
            layout.addWidget(QLabel("----------------------------"),3,0)
            layout.addWidget(QLabel("----------------------------"),3,1)
            
            self.mainLayout.addLayout(layout)

        self.setLayout(self.mainLayout)
        
def main():
        app = QApplication(sys.argv)

        a = ShowFant()
        a.show()

        return app.exec_()

if __name__ == "__main__":
        sys.exit(main())
'''
