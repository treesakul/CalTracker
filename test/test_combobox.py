'''import sys
from PySide.QtCore import *
from PySide.QtGui import *

class combodemo(QWidget):
   def __init__(self, parent = None):
      super(combodemo, self).__init__(parent)
      
      layout = QHBoxLayout()
      self.cb = QComboBox()
      self.cb.addItem("C")
      self.cb.addItem("C++")
      self.cb.addItems(["Java", "C#", "Python"])
      self.cb.currentIndexChanged.connect(self.selectionchange)
		
      layout.addWidget(self.cb)
      self.setLayout(layout)
      self.setWindowTitle("combo box demo")

   def selectionchange(self,i):
      print ("Items in the list are :")
		
      for count in range(self.cb.count()):
         print (self.cb.itemText(count))
      print ("Current index",i,"selection changed ",self.cb.currentText())
		
def main():
   app = QApplication(sys.argv)
   ex = combodemo()
   ex.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()


'''

import sys

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *


class UI_Manager(QWidget):
    def __init__(self, parent = None): #init
        QWidget.__init__(self, None)
        

        self.setWindowTitle("CALTracker")

        
        self.layout = QVBoxLayout()


        self.comboBox = QComboBox(self)
        for i in range(10):
            self.comboBox.addItem(i)
            '''
        self.comboBox.addItem("motif")
        self.comboBox.addItem("Windows")
        self.comboBox.addItem("cde")
        self.comboBox.addItem("Plastique")
        self.comboBox.addItem("Cleanlooks")
        self.comboBox.addItem("windowsvista")'''

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

