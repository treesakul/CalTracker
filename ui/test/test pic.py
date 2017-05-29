import sys
from PySide.QtCore import *
from PySide.QtGui import *

class filedialogdemo(QWidget):
   def __init__(self, parent = None):
      super(filedialogdemo, self).__init__(parent)
		
      layout = QVBoxLayout()
      self.btn = QPushButton("QFileDialog static method demo")
      self.btn.clicked.connect(self.getfile)
		
      layout.addWidget(self.btn)
      self.le = QLabel("Hello")
		
      layout.addWidget(self.le)
      self.btn1 = QPushButton("QFileDialog object")
      self.btn1.clicked.connect(self.getfiles)
      layout.addWidget(self.btn1)
		
      self.contents = QTextEdit()
      layout.addWidget(self.contents)
      self.setLayout(layout)
      self.setWindowTitle("File Dialog demo")
		
   def getfile(self):
      fname = QFileDialog.getOpenFileName(self, 'Open file', 
         'c:\\',"Image files (*.jpg *.gif)")
      self.le.setPixmap(QPixmap(fname))
      print(QPixmap(fname))
      print(self.le)
		
   def getfiles(self):
      dlg = QFileDialog()
      dlg.setFileMode(QFileDialog.AnyFile)
      dlg.setFilter("Text files (*.txt)")
      filenames = [] #QStringList()
		
      if dlg.exec_():
         filenames = dlg.selectedFiles()
         f = open(filenames[0], 'r')
			
         with f:
            data = f.read()
            self.contents.setText(data)
				
def main():
   app = QApplication(sys.argv)
   ex = filedialogdemo()
   ex.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()
'''







class MainWindow(QMainWindow):

    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        dlg = QFileDialog(self)       
        openAction = QAction('Open', self)  
        openAction.triggered.connect(dlg.open)     
        fileMenu.addAction(openAction)


    def open(self):
        # This function is called when the user clicks File->Open.
        filename = QFileDialog.getOpenFileName()
        print(filename)
        # Do your pixmap stuff here.
        
        label = QLabel(self)
        pixmap = QPixmap(filename)
        label.setPixmap(pixmap)

def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()

if __name__ == '__main__':
    sys.exit(main())
'''
