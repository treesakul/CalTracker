import sys
from PySide.QtCore import *
from PySide.QtGui import *

from PySide.QtUiTools import *


class ShowFant(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        self.testinit()


    def testinit(self):
        loader = QUiLoader()
        form = loader.load("UIDesigner/test_scrollarea.ui", None)
        self.setCentralWidget(form)
        
        #self.mainLayout = QVBoxLayout() #main layout
        
        self.widgetWoi = QWidget() #create very large + long widget
        layout = QVBoxLayout() #layout for tht wiget
        for i in range(200):
            layout.addWidget(QLabel("hello"+str(i)))
        self.widgetWoi.setLayout(layout)


        self.scrollArea = form.findChild(QScrollArea, "scrollArea")


        #self.sa = QScrollArea() #scroll area
        self.scrollArea.setWidget(self.widgetWoi) #add that huge widget
        
       #self.mainLayout.addWidget(self.sa) #add it to main layout
        #self.setLayout(self.mainLayout)


            
        
def main():
        app = QApplication(sys.argv)

        a = ShowFant()
        a.show()

        return app.exec_()

if __name__ == "__main__":
        sys.exit(main())
