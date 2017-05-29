
import sys

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *


class UI_Manager(QWidget):
    def __init__(self, parent = None): #init
        QWidget.__init__(self, None)
        

        self.setWindowTitle("CALTracker")

        
        self.layout = QVBoxLayout()



        self.progressBar = QProgressBar()
        self.progressBar.setRange(0, 10000)
        self.progressBar.setValue(0)

        self.statusBar().addPermanentWidget(self.progressBar)
        self.progressBar.show()

        

        self.layout.addWidget(self.comboBox)


        self.setLayout(self.layout)

        self.comboBox.currentIndexChanged.connect(self.show_info)

    def show_info(self):
        print(self.comboBox.itemText(2))
        print(self.comboBox.currentText())
        
def main():
        app = QApplication(sys.argv)

        w = UI_Manager()
        w.show()
        return app.exec_()

if __name__ == "__main__":
        sys.exit(main())
