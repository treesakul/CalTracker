import sys

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

import random

class Summarize_Page_UI(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, None)
        self.parent = parent

    def summarize_init(self):
        
        loader = QUiLoader()
        form = loader.load("UIDesigner/Summarize_page_ui.ui", None)
        self.setCentralWidget(form)

        #self.graph_widget = QWidget()
        self.graph_widget = form.findChild(QWidget, "graph_widget")

        


        '''
        # a figure instance to plot on
        self.graph_widget.figure = plt.figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.graph_widget.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget

        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        # Just some button connected to `plot` method
        self.graph_widget.button = QPushButton('Plot')
        self.graph_widget.button.clicked.connect(self.plot)
        self.graph_widget.button2 = QPushButton('Switch')
        self.graph_widget.button.clicked.connect(self.plot)
        self.graph_widget.button.clicked.connect(self.switch)

        # set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.addWidget(self.button)
        layout.addWidget(self.button2)
        #self.setLayout(layout)
        self.graph_widget.setLayout(layout)
        self.verticalLayout.addWidget(self.graph_widget)
        self.verticalLayout.a.ddWidget(button)
        self.setLayout(self.verticalLayout)

        self.lis = []
        self.dates = []
        self.num = 0
        '''
    
    def switch(self):
        self.add_list([100,200,300],3,['Johnny','Arnoldie','Mavisie'])
        
    def add_list(self,num ,l ,d):
        #self.food = f
        #self.exercise = e
        #self.goal = g
       # self.dates = d
        self.lis = l
        self.dates = d
        self.num = num
        
    def plot(self):
        ''' plot some random stuff '''
        temp = []
        for i in range(self.num):
            temp.append(i)
        
        # random data
        data = self.lis

        # create an axis
        ax = self.figure.add_subplot(111)

        
        # discards the old graph
        ax.hold(False)

        # plot data
        ax.plot(temp,[150,150,150],data, '*-')
        
        ax.set_xticks(temp)
        ax.set_xticklabels(self.dates)
        # refresh canvas
        self.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = Summarize_Page_UI()
    main.add_list(3,[100,200,300],['John','Arnold','Mavis'] )
    main.show()

    sys.exit(app.exec_())

